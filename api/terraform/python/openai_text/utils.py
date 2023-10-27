import json
import base64
import json  # library for interacting with JSON data https://www.json.org/json-en.html
import openai
import os  # library for interacting with the operating system
import platform  # library to view informatoin about the server host this Lambda runs on
import sys  # libraries for error management
import traceback  # libraries for error management

from const import (
    OpenAIEndPoint,
    DEBUG_MODE,
)
from validators import validate_item


def http_response_factory(status_code: int, body) -> dict:
    """
    Generate a standardized JSON return dictionary for all possible response scenarios.

    status_code: an HTTP response code. see https://developer.mozilla.org/en-US/docs/Web/HTTP/Status
    body: a JSON dict of openai results for status 200, an error dict otherwise.

    see https://docs.aws.amazon.com/lambda/latest/dg/python-handler.html
    """
    if status_code < 100 or status_code > 599:
        raise ValueError(
            "Invalid HTTP response code received: {status_code}".format(
                status_code=status_code
            )
        )

    retval = {
        "isBase64Encoded": False,
        "statusCode": status_code,
        "body": body,
    }
    event_log(json.dumps({"retval": retval}))
    return retval


def exception_response_factory(exception: Exception) -> dict:
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


def event_log(log_entry):
    """print to CloudWatch Logs"""
    if DEBUG_MODE:
        print(log_entry)


def dump_environment(event):
    """print to CloudWatch Logs"""
    if DEBUG_MODE:
        cloudwatch_dump = {
            "environment": {
                "os": os.name,
                "system": platform.system(),
                "release": platform.release(),
                "openai": openai.__version__,
                "openai_app_info": openai.app_info,
                "openai_end_points": OpenAIEndPoint.all_endpoints,
                "DEBUG_MODE": DEBUG_MODE,
            }
        }
        print(json.dumps(cloudwatch_dump))
        print(json.dumps({"event": event}))


def get_request_body(event) -> dict:
    """
    Returns the request body as a dictionary.

    Args:
        event: The event object containing the request body.

    Returns:
        A dictionary representing the request body.
    """
    if hasattr(event, "isBase64Encoded") and bool(event["isBase64Encoded"]):
        #  https://stackoverflow.com/questions/9942594/unicodeencodeerror-ascii-codec-cant-encode-character-u-xa0-in-position-20
        #  https://stackoverflow.com/questions/53340627/typeerror-expected-bytes-like-object-not-str
        request_body = str(event["body"]).encode("ascii")
        request_body = base64.b64decode(request_body)
    else:
        request_body = event
    return request_body


def parse_request(request_body: dict):
    """parse the request body and return the endpoint, model, messages, and input_text"""
    end_point = request_body.get("end_point")
    model = request_body.get("model")
    messages = request_body.get("messages")
    input_text = request_body.get("input_text")
    temperature = request_body.get("temperature")
    max_tokens = request_body.get("max_tokens")

    if not end_point:
        raise ValueError("end_point key not found in request body")

    validate_item(
        item=end_point,
        valid_items=OpenAIEndPoint.all_endpoints,
        item_type="OpenAI Endpoints",
    )

    if not messages and not input_text:
        raise ValueError("A value for either messages or input_text is required")

    return end_point, model, messages, input_text, temperature, max_tokens
