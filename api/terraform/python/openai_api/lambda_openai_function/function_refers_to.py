# -*- coding: utf-8 -*-
"""Example of
a.) how to customize the system prompt to adapt to keywords in the user's message
b.) how to call a function from the model
"""
import json

from openai_api.common.const import PYTHON_ROOT
from openai_api.lambda_openai_function.custom_config import CustomConfig
from openai_api.lambda_openai_function.custom_config import config as refers_to_config
from openai_api.lambda_openai_function.natural_language_processing import does_refer_to


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


def customized_prompt(config: CustomConfig, messages: list) -> list:
    """Modify the system prompt based on the custom configuration object"""

    for i, message in enumerate(messages):
        if message.get("role") == "system":
            system_prompt = message.get("content")
            custom_prompt = {
                "role": "system",
                "content": system_prompt + "\n\n and also " + config.prompting.system_prompt.system_prompt,
            }
            messages[i] = custom_prompt
            break

    return messages


# pylint: disable=too-many-return-statements
def get_additional_info(inquiry_type: str) -> str:
    """Return select info from custom config object"""

    for config in refers_to_config:
        try:
            additional_information = config.function_calling.additional_information.to_json()
            retval = additional_information[inquiry_type]
            return json.dumps(retval)
        except KeyError:
            pass

    raise KeyError(f"Invalid inquiry_type: {inquiry_type}")


def info_tool_factory(config: CustomConfig):
    """
    Return a dictionary of chat completion tools.
    """
    tool = {
        "type": "function",
        "function": {
            "name": "get_additional_info",
            "description": config.function_calling.function_description,
            "parameters": {
                "type": "object",
                "properties": {
                    "inquiry_type": {
                        "type": "string",
                        "enum": config.function_calling.additional_information.keys,
                    },
                },
                "required": ["inquiry_type"],
            },
        },
    }
    return tool
