# -*- coding: utf-8 -*-
# pylint: disable=no-member
# FIX NOTE: pylint is not recognizing the 'openai' module.
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
    does_refer_to,
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


openai.organization = settings.openai_api_organization
openai.api_key = settings.openai_api_key.get_secret_value()
with open(PYTHON_ROOT + "/openai_api/lambda_openai_function/lambda_config.yaml", "r", encoding="utf-8") as file:
    lambda_config = yaml.safe_load(file)


def chat_completion_tools_factory():
    """
    Return a dictionary of chat completion tools.
    """
    tools = [
        {
            "type": "function",
            "function": {
                "name": "get_current_weather",
                "description": "Get the current weather in a given location",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "location": {
                            "type": "string",
                            "description": "The city and state, e.g. San Francisco, CA",
                        },
                        "unit": {"type": "string", "enum": ["celsius", "fahrenheit"]},
                    },
                    "required": ["location"],
                },
            },
        }
    ]
    return tools


def search_terms_are_in_messages(messages: list, search_terms: list = None, search_pairs: list = None) -> bool:
    """
    Return True the user has mentioned Lawrence McDaniel or FullStackWithLawrence
    at any point in the history of the conversation.

    messages: [{"role": "user", "content": "some text"}]
    search_terms: ["Lawrence McDaniel", "FullStackWithLawrence"]
    search_pairs: [["Lawrence", "McDaniel"], ["FullStackWithLawrence", "Lawrence McDaniel"]]
    """
    for message in messages:
        if "role" in message and str(message["role"]).lower() == "user":
            content = message["content"]
            for term in search_terms:
                if does_refer_to(prompt=content, refers_to=term):
                    return True

            for lst in search_pairs:
                if does_refer_to(prompt=content, refers_to=lst[0]) and does_refer_to(prompt=content, refers_to=lst[1]):
                    return True

    return False


def customized_prompt(input_text: str) -> list:
    """Return a prompt for Lawrence McDaniel"""
    messages = [
        {
            "role": "system",
            "content": lambda_config["system_prompt"],
        },
        {"role": "user", "content": input_text},
    ]
    return messages


# pylint: disable=unused-argument
# pylint: disable=too-many-locals
def handler(event, context):
    """
    Main Lambda handler function.

    Responsible for processing incoming requests and invoking the appropriate
    OpenAI API endpoint based on the contents of the request.
    """
    cloudwatch_handler(event, settings.dump, debug_mode=settings.debug_mode)
    SEARCH_TERMS = lambda_config["search_terms"]
    SEARCH_PAIRS = lambda_config["search_pairs"]

    try:
        openai_results = {}
        request_body = get_request_body(event=event)
        object_type, model, messages, input_text, temperature, max_tokens = parse_request(request_body)
        request_meta_data = request_meta_data_factory(model, object_type, temperature, max_tokens, input_text)

        # does the prompt have anything to do with FullStackWithLawrence, or Lawrence McDaniel?
        if search_terms_are_in_messages(messages=messages, search_terms=SEARCH_TERMS, search_pairs=SEARCH_PAIRS):
            model = "gpt-4-1106-preview"
            messages = customized_prompt(input_text=input_text)
            temperature = (temperature,)

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
            tools=chat_completion_tools_factory(),
            temperature=temperature,
            max_tokens=max_tokens,
        )
        openai_results = openai_results.model_dump()

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
