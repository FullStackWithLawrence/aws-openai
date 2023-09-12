# ------------------------------------------------------------------------------
# written by: Lawrence McDaniel
#             https://lawrencemcdaniel.com/
#
# date:       sep-2023
#
# usage:
#             API Documentation: https://platform.openai.com/docs/api-reference/making-requests?lang=python
#             Source: https://github.com/openai/openai-python
#             Code Samples: https://github.com/openai/openai-cookbook/
#
#            ENDPOINT	                MODEL NAME
#            ------------------------   --------------------------------------------------------------------------------------------------------------------
#            /v1/audio/transcriptions	whisper-1
#            /v1/audio/translations	    whisper-1
#            /v1/chat/completions	    gpt-4, gpt-4-0613, gpt-4-32k, gpt-4-32k-0613, gpt-3.5-turbo,
#                                       gpt-3.5-turbo-0613, gpt-3.5-turbo-16k, gpt-3.5-turbo-16k-0613
#            /v1/completions (Legacy)	text-davinci-003, text-davinci-002, text-davinci-001, text-curie-001,
#                                       text-babbage-001, text-ada-001, davinci, curie, babbage, ada
#            /v1/embeddings	            text-embedding-ada-002, text-similarity-*-001,
#                                       text-search-*-*-001, code-search-*-*-001
#            /v1/fine_tuning/jobs	    gpt-3.5-turbo, babbage-002, davinci-002
#            /v1/fine-tunes	            davinci, curie, babbage, ada
#            /v1/moderations	        text-moderation-stable, text-moderation-latest
#
# openai.Model.list()
# ------------------------------------------------------------------------------

import sys, traceback  # libraries for error management
import os  # library for interacting with the operating system
import platform  # library to view informatoin about the server host this Lambda runs on
import json  # library for interacting with JSON data https://www.json.org/json-en.html
import base64
import openai

DEBUG_MODE = os.getenv("DEBUG_MODE", "False").lower() in ("true", "1", "t")
OPENAI_ENDPOINT_IMAGE_N = int(os.getenv("OPENAI_ENDPOINT_IMAGE_N", 4))
OPENAI_ENDPOINT_IMAGE_SIZE = os.getenv("OPENAI_ENDPOINT_IMAGE_SIZE", "1024x768")
openai.organization = os.environ["OPENAI_API_ORGANIZATION", "Personal"]
openai.api_key = os.environ["OPENAI_API_KEY"]


class OpenAIEndPoint:
    Embedding = openai.Embedding.__name__
    ChatCompletion = openai.ChatCompletion.__name__
    Moderation = openai.Moderation.__name__
    Image = openai.Image.__name__
    Audio = openai.Audio.__name__
    Models = openai.Model.__name__


OPENAI_ENDPOINTS = [
    OpenAIEndPoint.Embedding,
    OpenAIEndPoint.ChatCompletion,
    OpenAIEndPoint.Moderation,
    OpenAIEndPoint.Image,
    OpenAIEndPoint.Audio,
    OpenAIEndPoint.Models,
]


def handler(event, context):
    """
    OpenAI API integrator
    """
    if DEBUG_MODE:
        cloudwatch_dump = {
            "environment": {
                "os": os.name,
                "system": platform.system(),
                "release": platform.release(),
                "openai": openai.__version__,
                "openai_app_info": openai.app_info,
                "DEBUG_MODE": DEBUG_MODE,
            }
        }
        print(json.dumps(cloudwatch_dump))
        print(json.dumps({"event": event}))

    def http_response_factory(status_code: int, body: json) -> json:
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

        if DEBUG_MODE:
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

    def validate_item(item, valid_items, item_type):
        if item not in valid_items:
            raise ValueError(
                "Item {item} not found in {item_type}: {valid_items}".format(
                    item=item, item_type=item_type, valid_items=valid_items
                )
            )
        return

    records = event["Records"]

    # Some basic business rule validations to ensure that the contents of the
    # 'event' variable match what we are expecting.
    try:
        if not "Records" in event:
            raise TypeError("Records object not found in event object")
    except TypeError as e:
        return http_response_factory(
            status_code=500, body=exception_response_factory(e)
        )

    for record in records:
        openai_results = {}

        if hasattr(event, "isBase64Encoded") and bool(event["isBase64Encoded"]):
            #  https://stackoverflow.com/questions/9942594/unicodeencodeerror-ascii-codec-cant-encode-character-u-xa0-in-position-20
            #  https://stackoverflow.com/questions/53340627/typeerror-expected-bytes-like-object-not-str
            request_body = str(event["body"]).encode("ascii")
            request_body = base64.b64decode(request_body)
        else:
            request_body = json.loads("{}".format(event["body"]))

        end_point = request_body.get("end_point")
        model = request_body.get("model")
        messages = request_body.get("messages")
        input_text = request_body.get("input_text")

        try:
            if not end_point:
                raise ValueError("end_point key not found in request body")

            if not messages and not input_text:
                raise ValueError(
                    "A value for either messages or input_text is required"
                )

        except ValueError as e:
            return http_response_factory(
                status_code=500, body=exception_response_factory(e)
            )

        if DEBUG_MODE:
            print(json.dumps({"event_record": record}))

        try:
            validate_item(
                item=end_point,
                valid_items=OPENAI_ENDPOINTS,
                item_type="OpenAI Endpoints",
            )

            match end_point:
                case OpenAIEndPoint.ChatCompletion:
                    # https://platform.openai.com/docs/guides/gpt/chat-completions-api
                    valid_items = [
                        "gpt-4",
                        "gpt-4-0613",
                        "gpt-4-32k",
                        "gpt-4-32k-0613",
                        "gpt-3.5-turbo",
                        "gpt-3.5-turbo-0613",
                        "gpt-3.5-turbo-16k",
                        "gpt-3.5-turbo-16k-0613",
                    ]
                    validate_item(
                        item=model,
                        valid_items=valid_items,
                        item_type="ChatCompletion models",
                    )
                    openai_results = openai.ChatCompletion.create(
                        model=model, messages=messages
                    )

                case OpenAIEndPoint.Embedding:
                    # https://platform.openai.com/docs/guides/embeddings/embeddings
                    valid_items = [
                        "text-embedding-ada-002",
                        "text-similarity-*-001",
                        "text-search-*-*-001",
                        "code-search-*-*-001",
                    ]
                    validate_item(
                        item=model,
                        valid_items=valid_items,
                        item_type="Embedding models",
                    )
                    openai_results = openai.Embedding.create(
                        input=input_text, model=model
                    )

                case OpenAIEndPoint.Image:
                    # https://platform.openai.com/docs/guides/images
                    n = request_body.get("n", OPENAI_ENDPOINT_IMAGE_N)
                    size = request_body.get("size", OPENAI_ENDPOINT_IMAGE_SIZE)
                    return openai.Image.create(prompt=input_text, n=n, size=size)

                case OpenAIEndPoint.Moderation:
                    # https://platform.openai.com/docs/guides/moderation
                    openai_results = openai.Moderation.create(input=input_text)

                case OpenAIEndPoint.Models:
                    openai_results = (
                        openai.Model.retrieve(model) if model else openai.Model.list()
                    )

                case OpenAIEndPoint.Audio:
                    raise NotImplementedError("Audio support is coming soon")

        # handle anything that went wrong
        # see https://docs.aws.amazon.com/openai/latest/dg/error-handling.html
        except (openai.APIError, ValueError) as e:
            # 400 Bad Request
            return http_response_factory(
                status_code=400, body=exception_response_factory(e)
            )
        except openai.OpenAIError as e:
            # 500 Internal Server Error
            return http_response_factory(
                status_code=500, body=exception_response_factory(e)
            )

        # success!! return the results
        return http_response_factory(status_code=200, body=openai_results)
