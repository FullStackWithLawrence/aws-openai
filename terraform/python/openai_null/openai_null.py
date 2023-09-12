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

# import openai

DEBUG_MODE = os.getenv("DEBUG_MODE", "False").lower() in ("true", "1", "t")
OPENAI_ENDPOINT_IMAGE_N = int(os.getenv("OPENAI_ENDPOINT_IMAGE_N", 4))
OPENAI_ENDPOINT_IMAGE_SIZE = os.getenv("OPENAI_ENDPOINT_IMAGE_SIZE", "1024x768")
# openai.organization = os.environ["OPENAI_API_ORGANIZATION", "Personal"]
# openai.api_key = os.environ["OPENAI_API_KEY"]


def http_response_factory(status_code: int, body: json) -> json:
    if status_code < 100 or status_code > 599:
        raise ValueError(
            "Invalid HTTP response code received: {status_code}".format(
                status_code=status_code
            )
        )

    retval = {
        "isBase64Encoded": False,
        "statusCode": status_code,
        "headers": {"Content-Type": "application/json"},
        "body": json.dumps(body),
    }

    return retval


def handler(event, context):
    """
    test
    """
    openai_results = {
        "environment": {
            "os": os.name,
            "system": platform.system(),
            "release": platform.release(),
            #            "openai": openai.__version__,
            #            "openai_app_info": openai.app_info,
            "DEBUG_MODE": DEBUG_MODE,
        }
    }
    return http_response_factory(status_code=200, body=openai_results)
