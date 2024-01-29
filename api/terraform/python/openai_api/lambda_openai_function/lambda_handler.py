# -*- coding: utf-8 -*-
# pylint: disable=no-member
# pylint: disable=R0801
"""
written by: Lawrence McDaniel
            https://lawrencemcdaniel.com/

date:       jan-2024

usage: Demonstrate usage of Function Calling with OpenAI API v2.
In an API call, you can describe functions and have the model intelligently
choose to output a JSON object containing arguments to call one or many functions.
The Chat Completions API does not call the function; instead, the model
generates JSON that you can use to call the function in your code.

API Documentation: https://platform.openai.com/docs/guides/function-calling
"""
import json

import openai
import yaml
from openai_api.common.conf import settings
from openai_api.common.const import (
    PYTHON_ROOT,
    VALID_CHAT_COMPLETION_MODELS,
    OpenAIResponseCodes,
)
from openai_api.common.exceptions import EXCEPTION_MAP
from openai_api.common.utils import (
    cloudwatch_handler,
    exception_response_factory,
    get_request_body,
    http_response_factory,
    parse_request,
    request_meta_data_factory,
)
from openai_api.common.validators import (  # validate_embedding_request,
    validate_completion_request,
    validate_item,
)

# OpenAI functions
from openai_api.lambda_openai_function.function_weather import (
    get_current_weather,
    weather_tool_factory,
)
from openai_api.lambda_openai_function.plugin_loader import plugins
from openai_api.lambda_openai_function.plugin_manager import (
    customized_prompt,
    function_calling_plugin,
    plugin_tool_factory,
    search_terms_are_in_messages,
)


openai.organization = settings.openai_api_organization
openai.api_key = settings.openai_api_key.get_secret_value()


# pylint: disable=unused-argument
# pylint: disable=too-many-locals
def handler(event, context):
    """
    Main Lambda handler function.

    Responsible for processing incoming requests and invoking the appropriate
    OpenAI API endpoint based on the contents of the request.
    """
    cloudwatch_handler(event, settings.dump, debug_mode=settings.debug_mode)
    weather_tool = weather_tool_factory()
    tools = [weather_tool]

    try:
        openai_results = {}
        request_body = get_request_body(event=event)
        object_type, model, messages, input_text, temperature, max_tokens = parse_request(request_body)
        request_meta_data = request_meta_data_factory(model, object_type, temperature, max_tokens, input_text)

        # does the prompt have anything to do with any of the search terms defined in a plugin?
        # FIX NOTE: need to decide on how to resolve which of many plugin values sets to use for model, temperature, max_tokens
        for plugin in plugins:
            if search_terms_are_in_messages(
                messages=messages,
                search_terms=plugin.selector.search_terms.strings,
                search_pairs=plugin.selector.search_terms.pairs,
            ):
                model = plugin.prompting.model
                temperature = plugin.prompting.temperature
                max_tokens = plugin.prompting.max_tokens
                messages = customized_prompt(plugin=plugin, messages=messages)
                custom_tool = plugin_tool_factory(plugin=plugin)
                tools.append(custom_tool)
                print(
                    f"Adding plugin: {plugin.name} {plugin.meta_data.plugin_version} created by {plugin.meta_data.plugin_author}"
                )

        # https://platform.openai.com/docs/guides/gpt/chat-completions-api
        validate_item(
            item=model,
            valid_items=VALID_CHAT_COMPLETION_MODELS,
            item_type="ChatCompletion models",
        )
        validate_completion_request(request_body)
        openai_results = openai.chat.completions.create(
            model=model,
            messages=messages,
            tools=tools,
            temperature=temperature,
            max_tokens=max_tokens,
        )
        response_message = openai_results.choices[0].message
        openai_results = openai_results.model_dump()
        tool_calls = response_message.tool_calls
        if tool_calls:
            # Step 3: call the function
            # Note: the JSON response may not always be valid; be sure to handle errors
            available_functions = {
                "get_current_weather": get_current_weather,
                "function_calling_plugin": function_calling_plugin,
            }  # only one function in this example, but you can have multiple
            messages.append(response_message)  # extend conversation with assistant's reply
            # Step 4: send the info for each function call and function response to the model
            for tool_call in tool_calls:
                function_name = tool_call.function.name
                function_to_call = available_functions[function_name]
                function_args = json.loads(tool_call.function.arguments)

                if function_name == "get_current_weather":
                    function_response = function_to_call(
                        location=function_args.get("location"),
                        unit=function_args.get("unit"),
                    )
                elif function_name == "function_calling_plugin":
                    function_response = function_to_call(inquiry_type=function_args.get("inquiry_type"))
                messages.append(
                    {
                        "tool_call_id": tool_call.id,
                        "role": "tool",
                        "name": function_name,
                        "content": function_response,
                    }
                )  # extend conversation with function response
            second_response = openai.chat.completions.create(
                model=model,
                messages=messages,
            )  # get a new response from the model where it can see the function response
            openai_results = second_response.model_dump()

    # handle anything that went wrong
    # pylint: disable=broad-exception-caught
    except Exception as e:
        status_code, _message = EXCEPTION_MAP.get(type(e), (500, "Internal server error"))
        return http_response_factory(status_code=status_code, body=exception_response_factory(e))

    # success!! return the results
    return http_response_factory(
        status_code=OpenAIResponseCodes.HTTP_RESPONSE_OK,
        body={**openai_results, **request_meta_data},
    )
