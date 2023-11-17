# -*- coding: utf-8 -*-
"""Internal validation functions for requests from API Gateway."""
import json

from openai_utils.const import OpenAIEndPoint, OpenAIMessageKeys


def validate_item(item, valid_items: list, item_type: str) -> None:
    """Ensure that item exists in valid_items"""
    if item not in valid_items:
        raise ValueError(
            "Item {item} not found in {item_type}: {valid_items}".format(
                item=item, item_type=item_type, valid_items=valid_items
            )
        )
    return


def validate_temperature(temperature: any) -> None:
    """Ensure that temperature is a float between 0 and 1"""
    try:
        float_temperature = float(temperature)
        if float_temperature < 0 or float_temperature > 1:
            raise ValueError("temperature should be between 0 and 1")
    except ValueError:
        raise ValueError("Temperature must be a float")


def validate_max_tokens(max_tokens: any) -> None:
    """Ensure that max_tokens is an int between 1 and 2048"""
    if type(max_tokens) is not int:
        raise TypeError("max_tokens should be an int")

    if max_tokens < 1 or max_tokens > 2048:
        raise ValueError("max_tokens should be between 1 and 2048")


def validate_endpoint(end_point: any) -> None:
    """Ensure that end_point is a valid endpoint based on the OpenAIEndPoint enum"""
    if type(end_point) is not str:
        raise TypeError("end_point should be a string")

    if end_point not in OpenAIEndPoint.all_endpoints:
        raise ValueError(
            "end_point should be one of {end_points}".format(
                end_points=OpenAIEndPoint.all_endpoints
            )
        )


def validate_request_body(request_body) -> None:
    """See openai.chat.completion.request.json"""
    if type(request_body) is not dict:
        raise TypeError("request body should be a dict")


def validate_messages(request_body):
    """See openai.chat.completion.request.json"""
    if "messages" not in request_body:
        raise ValueError("dict key 'messages' not found in request body object")
    messages = request_body["messages"]
    if type(messages) is not list:
        raise ValueError("dict key 'messages' should be a JSON list")
    for message in messages:
        if type(message) is not dict:
            raise ValueError(
                "invalid ojbect type {t} found in messages list".format(t=type(message))
            )
        if "role" not in message:
            raise ValueError(
                "dict key 'role' not found in message {m}".format(
                    m=json.dumps(message, indent=4)
                )
            )
        if message["role"] not in OpenAIMessageKeys.all:
            raise ValueError(
                "invalid role {r} found in message {m}. Should be one of {valid_roles}".format(
                    r=message["role"],
                    m=json.dumps(message, indent=4),
                    valid_roles=OpenAIMessageKeys.all,
                )
            )
        if "content" not in message:
            raise ValueError(
                "dict key 'content' not found in message {m}".format(
                    m=json.dumps(message, indent=4)
                )
            )


def validate_completion_request(request_body) -> None:
    """See openai.chat.completion.request.json"""
    validate_request_body(request_body=request_body)
    if "model" not in request_body:
        raise ValueError("dict key 'model' not found in request body object")
    if "temperature" not in request_body:
        raise ValueError("dict key 'temperature' not found in request body object")
    if "max_tokens" not in request_body:
        raise ValueError("dict key 'max_tokens' not found in request body object")
    validate_messages(request_body=request_body)


def validate_embedding_request(request_body) -> None:
    """See openai.embedding.request.json"""
    validate_request_body(request_body=request_body)
    if "input_text" not in request_body:
        raise ValueError("dict key 'input_text' not found in request body object")
