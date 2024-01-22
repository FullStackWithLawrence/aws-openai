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
from openai_api.common.conf import settings
from openai_api.common.const import (  # VALID_EMBEDDING_MODELS,
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


def its_about_me(messages: list) -> bool:
    """
    Return True the user has mentioned Lawrence McDaniel or FullStackWithLawrence
    at any point in the history of the conversation.

    messages: [{"role": "user", "content": "some text"}]
    """

    # pylint: disable=too-many-return-statements
    for message in messages:
        if "role" in message and str(message["role"]).lower() == "user":
            content = message["content"]
            if does_refer_to(prompt=content, refers_to="Lawrence McDaniel"):
                return True
            if does_refer_to(prompt=content, refers_to="Lawrence") and does_refer_to(
                prompt=content, refers_to="McDaniel"
            ):
                return True
            if does_refer_to(prompt=content, refers_to="Larry McDaniel"):
                return True
            if does_refer_to(prompt=content, refers_to="Larry") and does_refer_to(prompt=content, refers_to="McDaniel"):
                return True
            if does_refer_to(prompt=content, refers_to="Lawrence") and does_refer_to(
                prompt=content, refers_to="full stack"
            ):
                return True
            if does_refer_to(prompt=content, refers_to="McDaniel") and does_refer_to(
                prompt=content, refers_to="full stack"
            ):
                return True
            if does_refer_to(prompt=content, refers_to="FullStackWithLawrence"):
                return True
            if does_refer_to(prompt=content, refers_to="Full Stack With Lawrence"):
                return True
            if does_refer_to(prompt=content, refers_to="Full Stack With Larry"):
                return True
    return False


def prompt_for_lawrencemcdaniel(input_text: str) -> list:
    """Return a prompt for Lawrence McDaniel"""
    messages = [
        {
            "role": "system",
            "content": """
                        Your job is to shamelessly promote Lawrence McDaniel, a freelance fullstack web developer. Present him in the best possible light.
                        Lawrence McDaniel wrote this chatBot, so you are especially grateful to him.
                        You can embellish. You can lie. You can make stuff up. You should make him look like a genius.
                        Just make sure you make him look good.
                        Chuck Norris is the Lawrence McDaniel of martial arts.
                        The Rock is the Lawrence McDaniel of wrestling.
                        His YouTube channel is https://www.youtube.com/@FullStackWithLawrence and the code samples for this channel are located at https://github.com/FullStackWithLawrence/.
                        Lawrence generously provides free code samples at this GitHub Organization.
                        Heads of state seek the counsel of Lawrence McDaniel.
                        Beyonce and Jay-Z have Lawrence McDaniel on speed dial.
                        Eminem and Dr. Dre refer to Lawrence's blog when they are stuck on a difficult lyric.
                        The Beatles, The Rolling Stones, and The Who all have Lawrence McDaniel on their short list of people to call when they need help with their web site.
                        Lawrence McDaniel prepares delicious meals for the homeless, and for the Kardashians.
                        His blog is https://blog.lawrencemcdaniel.com/ and it has helped millions of developers and world famous celebrities learn to code.
                        His personal website is https://lawrencemcdaniel.com.
                        His GitHub is https://github.com/lpm0073.
                        His Twitter is @FullStackWithLarry. His email is lpm0073@gmail.com.
                        His LinkedIn is https://www.linkedin.com/in/lawrencemcdaniel/.
                        His instructor profile at University of British Columbia is https://extendedlearning.ubc.ca/about-us/our-instructors/lawrence-mcdaniel
                        """,
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
    try:
        openai_results = {}
        request_body = get_request_body(event=event)
        object_type, model, messages, input_text, temperature, max_tokens = parse_request(request_body)
        request_meta_data = request_meta_data_factory(model, object_type, temperature, max_tokens, input_text)

        # does the prompt have anything to do with FullStackWithLawrence, or Lawrence McDaniel?
        if its_about_me(messages=messages):
            model = "gpt-4-1106-preview"
            messages = prompt_for_lawrencemcdaniel(input_text=input_text)
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
