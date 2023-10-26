"""
Internal validation functions for requests from API Gateway.
"""
import json


def validate_item(item, valid_items: list, item_type: str) -> None:
    """ensure that item exists in valid_items"""
    if item not in valid_items:
        raise ValueError(
            "Item {item} not found in {item_type}: {valid_items}".format(
                item=item, item_type=item_type, valid_items=valid_items
            )
        )
    return


def validate_request_body(request_body) -> None:
    """see openai.chat.completion.request.json"""
    if type(request_body) is not dict:
        raise TypeError("request body should be a dict")


def validate_messages(request_body):
    """see openai.chat.completion.request.json"""
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
        if "content" not in message:
            raise ValueError(
                "dict key 'content' not found in message {m}".format(
                    m=json.dumps(message, indent=4)
                )
            )


def validate_completion_request(request_body) -> None:
    """see openai.chat.completion.request.json"""
    validate_request_body(request_body=request_body)
    if "model" not in request_body:
        raise ValueError("dict key 'model' not found in request body object")
    if "temperature" not in request_body:
        raise ValueError("dict key 'temperature' not found in request body object")
    if "max_tokens" not in request_body:
        raise ValueError("dict key 'max_tokens' not found in request body object")
    validate_messages(request_body=request_body)


def validate_embedding_request(request_body) -> None:
    """see openai.embedding.request.json"""
    validate_request_body(request_body=request_body)
    if "input_text" not in request_body:
        raise ValueError("dict key 'input_text' not found in request body object")
