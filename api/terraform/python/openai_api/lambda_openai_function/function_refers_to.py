# -*- coding: utf-8 -*-
"""Example of
a.) how to customize the system prompt to adapt to keywords in the user's message
b.) how to call a function from the model
"""
import json

import requests
import yaml
from openai_api.common.const import PYTHON_ROOT
from openai_api.lambda_openai_function.natural_language_processing import does_refer_to


with open(PYTHON_ROOT + "/openai_api/lambda_openai_function/lambda_config.yaml", "r", encoding="utf-8") as file:
    lambda_config = yaml.safe_load(file)

client_list_url = "https://api.lawrencemcdaniel.com/wp-json/wp/v2/posts?categories=46&tags=55&_embed&per_page=100"
try:
    client_list_response = requests.get(client_list_url, timeout=60)
# pylint: disable=broad-except
except Exception as e:
    client_list_response = None


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


def get_client_list() -> list:
    """Return a list of clients"""
    if not client_list_response:
        return []

    if client_list_response.status_code == 200:
        client_list = client_list_response.json()
        client_list = [
            client["title"]["rendered"] for client in client_list if "title" in client and "rendered" in client["title"]
        ]
        return client_list
    return []


# pylint: disable=too-many-return-statements
def get_additional_info(inquiry_type: str = "biographical_info") -> str:
    """Return select info from lambda_config.yaml"""
    inquiry_type = inquiry_type or "biographical_info"
    lambda_config["clients"] = get_client_list()

    if inquiry_type == "client_list":
        return json.dumps(lambda_config["clients"])

    if inquiry_type == "contact_info":
        return json.dumps(lambda_config["contact_information"])

    if inquiry_type == "educational_info":
        return json.dumps(
            {
                "education": lambda_config["professional_profile"]["education"],
                "certifications": lambda_config["professional_profile"]["certifications"],
            }
        )

    if inquiry_type == "teaching":
        return json.dumps(lambda_config["teaching"])

    if inquiry_type == "biographical_info":
        return json.dumps(lambda_config)

    if inquiry_type == "marketing_info":
        return json.dumps(lambda_config["marketing_info"])

    return json.dumps(lambda_config)


def info_tool_factory():
    """
    Return a dictionary of chat completion tools.
    """
    tools = [
        {
            "type": "function",
            "function": {
                "name": "get_additional_info",
                "description": "Get additional information about Lawrence McDaniel, full stack web developer and host of YouTube channel FullStackwithLawrence. returns a personal bio, contact information, marketing information, client list, education background, professional certifications, etc.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "inquiry_type": {
                            "type": "string",
                            "enum": [
                                "biographical_info",
                                "marketing_info",
                                "contact_info",
                                "educational_info",
                                "teaching",
                                "client_list",
                            ],
                        },
                    },
                    "required": ["inquiry_type"],
                },
            },
        }
    ]
    return tools
