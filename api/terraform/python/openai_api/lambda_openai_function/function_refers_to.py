# -*- coding: utf-8 -*-
"""Example of
a.) how to customize the system prompt to adapt to keywords in the user's message
b.) how to call a function from the model
"""
import json

import yaml
from openai_api.common.const import PYTHON_ROOT
from openai_api.lambda_openai_function.natural_language_processing import does_refer_to


with open(PYTHON_ROOT + "/openai_api/lambda_openai_function/lambda_config.yaml", "r", encoding="utf-8") as file:
    lambda_config = yaml.safe_load(file)


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


def customized_prompt(messages: list) -> list:
    """Return a prompt for Lawrence McDaniel"""
    custom_prompt = {
        "role": "system",
        "content": lambda_config["system_prompt"],
    }

    for i, message in enumerate(messages):
        if message.get("role") == "system":
            messages[i] = custom_prompt
            break

    return messages


def get_additional_info(inquiry_type: str) -> str:
    """Return a table of URLs and other info about the location"""
    if inquiry_type == "biographical_info":
        return lambda_config["biographical_info"]

    if inquiry_type == "marketing_info":
        return json.dumps(lambda_config["marketing_info"])

    return json.dumps({"error": "inquiry_type not recognized"})


def info_tool_factory():
    """
    Return a dictionary of chat completion tools.
    """
    tools = [
        {
            "type": "function",
            "function": {
                "name": "get_additional_info",
                "description": "Get additional information about Lawrence McDaniel, full stack web developer.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "inquiry_type": {"type": "string", "enum": ["biographical_info", "marketing_info"]},
                    },
                    "required": ["inquiry_type"],
                },
            },
        }
    ]
    return tools
