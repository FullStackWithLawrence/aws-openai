# -*- coding: utf-8 -*-
"""Internal validation functions for requests from API Gateway."""
import json

from openai_utils.const import OpenAIEndPoint, OpenAIMessageKeys


def validate_item(item, valid_items: list, item_type: str) -> None:
    """Ensure that item exists in valid_items"""
    if item not in valid_items:
        raise ValueError(f"Item {item} not found in {item_type}: {valid_items}")


def validate_temperature(temperature: any) -> None:
    """Ensure that temperature is a float between 0 and 1"""
    try:
        float_temperature = float(temperature)
        if float_temperature < 0 or float_temperature > 1:
            raise ValueError("temperature should be between 0 and 1")
    except ValueError as exc:
        raise ValueError("Temperature must be a float") from exc


def validate_max_tokens(max_tokens: any) -> None:
    """Ensure that max_tokens is an int between 1 and 2048"""
    if not isinstance(max_tokens, int):
        raise TypeError("max_tokens should be an int")

    if max_tokens < 1 or max_tokens > 2048:
        raise ValueError("max_tokens should be between 1 and 2048")


def validate_endpoint(end_point: any) -> None:
    """Ensure that end_point is a valid endpoint based on the OpenAIEndPoint enum"""
    if not isinstance(end_point, str):
        raise TypeError(f"Invalid end_point '{end_point}'. end_point should be a string.")

    if end_point not in OpenAIEndPoint.all_endpoints:
        raise ValueError(f"Invalid end_point {end_point}. Should be one of {OpenAIEndPoint.all_endpoints}")


def validate_request_body(request_body) -> None:
    """See openai.chat.completion.request.json"""
    if not isinstance(request_body, dict):
        raise TypeError("request body should be a dict")


def validate_messages(request_body):
    """See openai.chat.completion.request.json"""
    if "messages" not in request_body:
        raise ValueError("dict key 'messages' was not found in request body object")
    messages = request_body["messages"]
    if not isinstance(messages, list):
        raise ValueError("dict key 'messages' should be a JSON list")
    for message in messages:
        if not isinstance(message, dict):
            raise ValueError(f"invalid object type {type(message)} found in messages list")
        if "role" not in message:
            raise ValueError(f"dict key 'role' not found in message {json.dumps(message, indent=4)}")
        if message["role"] not in OpenAIMessageKeys.all:
            raise ValueError(
                f"invalid role {message['role']} found in message {json.dumps(message, indent=4)}. "
                f"Should be one of {OpenAIMessageKeys.all}"
            )
        if "content" not in message:
            raise ValueError(f"dict key 'content' not found in message {json.dumps(message, indent=4)}")


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
