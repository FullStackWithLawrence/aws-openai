# -*- coding: utf-8 -*-
# pylint: disable=duplicate-code
# pylint: disable=E1101
"""Utility functions for the OpenAI Lambda functions"""
import base64
import json  # library for interacting with JSON data https://www.json.org/json-en.html
import sys  # libraries for error management
import traceback  # libraries for error management

from openai_api.common.conf import settings
from openai_api.common.const import LANGCHAIN_MESSAGE_HISTORY_ROLES, OpenAIEndPoint
from openai_api.common.validators import (
    validate_endpoint,
    validate_item,
    validate_max_tokens,
    validate_messages,
    validate_request_body,
    validate_temperature,
)


def cloudwatch_handler(event, quiet: bool = False):
    """Create a CloudWatch log entry for the event and dump the event to stdout."""
    if settings.debug_mode and not quiet:
        print(json.dumps(settings.cloudwatch_dump))
        print(json.dumps({"event": event}))


def http_response_factory(status_code: int, body: json) -> json:
    """
    Generate a standardized JSON return dictionary for all possible response scenarios.

    status_code: an HTTP response code. see https://developer.mozilla.org/en-US/docs/Web/HTTP/Status
    body: a JSON dict of Rekognition results for status 200, an error dict otherwise.

    see https://docs.aws.amazon.com/lambda/latest/dg/python-handler.html
    """
    if status_code < 100 or status_code > 599:
        raise ValueError(f"Invalid HTTP response code received: {status_code}")

    if settings.debug_mode:
        retval = {
            "isBase64Encoded": False,
            "statusCode": status_code,
            "headers": {"Content-Type": "application/json"},
            "body": body,
        }
        # log our output to the CloudWatch log for this Lambda
        print(json.dumps({"retval": retval}))

    # see https://docs.aws.amazon.com/apigateway/latest/developerguide/http-api-develop-integrations-lambda.html
    retval = {
        "isBase64Encoded": False,
        "statusCode": status_code,
        "headers": {"Content-Type": "application/json"},
        "body": json.dumps(body),
    }

    return retval


def exception_response_factory(exception) -> json:
    """
    Generate a standardized error response dictionary that includes
    the Python exception type and stack trace.

    exception: a descendant of Python Exception class
    """
    exc_info = sys.exc_info()
    retval = {
        "error": str(exception),
        "description": "".join(traceback.format_exception(*exc_info)),
    }

    return retval


def get_request_body(event) -> dict:
    """
    Returns the request body as a dictionary.

    Args:
        event: The event object containing the request body.

    Returns:
        A dictionary representing the request body.
    """
    if hasattr(event, "isBase64Encoded") and bool(event["isBase64Encoded"]):
        # pylint: disable=line-too-long
        #  https://stackoverflow.com/questions/9942594/unicodeencodeerror-ascii-codec-cant-encode-character-u-xa0-in-position-20
        #  https://stackoverflow.com/questions/53340627/typeerror-expected-bytes-like-object-not-str
        request_body = str(event["body"]).encode("ascii")
        request_body = base64.b64decode(request_body)
    else:
        request_body = event

    validate_request_body(request_body=request_body)

    if hasattr(request_body, "temperature"):
        temperature = request_body["temperature"]
        validate_temperature(temperature=temperature)

    if hasattr(request_body, "max_tokens"):
        max_tokens = request_body["max_tokens"]
        validate_max_tokens(max_tokens=max_tokens)

    if hasattr(request_body, "end_point"):
        end_point = request_body["end_point"]
        validate_endpoint(end_point=end_point)

    validate_messages(request_body=request_body)
    return request_body


def parse_request(request_body: dict):
    """Parse the request body and return the endpoint, model, messages, and input_text"""
    end_point = request_body.get("end_point")
    model = request_body.get("model")
    messages = request_body.get("messages")
    input_text = request_body.get("input_text")
    temperature = request_body.get("temperature")
    max_tokens = request_body.get("max_tokens")
    chat_history = request_body.get("chat_history")

    if not end_point:
        raise ValueError("end_point key not found in request body")

    validate_item(
        item=end_point,
        valid_items=OpenAIEndPoint.all_endpoints,
        item_type="OpenAI Endpoints",
    )

    if not messages and not input_text:
        raise ValueError("A value for either messages or input_text is required")

    if chat_history and input_text:
        # memory-enabled request assumed to be destined for lambda_langchain
        # we'll need to rebuild the messages list from the chat_history
        messages = []
        for chat in chat_history:
            messages.append({"role": chat["sender"], "content": chat["message"]})
        messages.append({"role": "user", "content": input_text})

    return end_point, model, messages, input_text, temperature, max_tokens


def get_content_for_role(messages: list, role: str) -> str:
    """Get the text content from the messages list for a given role"""
    retval = [d.get("content") for d in messages if d["role"] == role]
    try:
        return retval[-1]
    except IndexError:
        return ""


def get_message_history(messages: list) -> list:
    """Get the text content from the messages list for a given role"""
    message_history = [
        {"role": d["role"], "content": d.get("content")}
        for d in messages
        if d["role"] in LANGCHAIN_MESSAGE_HISTORY_ROLES
    ]
    return message_history


def get_messages_for_role(messages: list, role: str) -> list:
    """Get the text content from the messages list for a given role"""
    retval = [d.get("content") for d in messages if d["role"] == role]
    return retval


def get_messages_for_type(messages: list, message_type: str) -> list:
    """Get the text content from the messages list for a given role"""
    retval = [d.get("content") for d in messages if d["type"] == message_type]
    return retval
