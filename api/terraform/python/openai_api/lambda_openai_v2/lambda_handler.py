# -*- coding: utf-8 -*-
# pylint: disable=no-member
# FIX NOTE: pylint is not recognizing the 'openai' module.
"""
written by: Lawrence McDaniel
            https://lawrencemcdaniel.com/

date:       nov-2023

usage:
    API Documentation: https://platform.openai.com/docs/api-reference/making-requests?lang=python
    Source: https://github.com/openai/openai-python
    Code Samples: https://github.com/openai/openai-cookbook/

    ENDPOINT	                MODEL NAME
    ------------------------   ------------------------------------------------------------------
    /v1/audio/transcriptions	whisper-1
    /v1/audio/translations	    whisper-1
    /v1/chat/completions	    gpt-4, gpt-4-0613, gpt-4-32k, gpt-4-32k-0613, gpt-3.5-turbo,
                                gpt-3.5-turbo-0613, gpt-3.5-turbo-16k, gpt-3.5-turbo-16k-0613
    /v1/completions (Legacy)	text-davinci-003, text-davinci-002, text-davinci-001, text-curie-001,
                                text-babbage-001, text-ada-001, davinci, curie, babbage, ada
    /v1/embeddings	            text-embedding-ada-002, text-similarity-*-001,
                                text-search-*-*-001, code-search-*-*-001
    /v1/fine_tuning/jobs	    gpt-3.5-turbo, babbage-002, davinci-002
    /v1/fine-tunes	            davinci, curie, babbage, ada
    /v1/moderations	            text-moderation-stable, text-moderation-latest

"""
# All of these imports are sourced from genai Lambda Layer
# -----------------------
import openai
from openai_api.common.conf import settings
from openai_api.common.const import (
    VALID_CHAT_COMPLETION_MODELS,
    VALID_EMBEDDING_MODELS,
    OpenAIEndPoint,
    OpenAIResponseCodes,
)
from openai_api.common.exceptions import EXCEPTION_MAP
from openai_api.common.utils import (
    cloudwatch_handler,
    exception_response_factory,
    get_request_body,
    http_response_factory,
    parse_request,
)
from openai_api.common.validators import (
    validate_completion_request,
    validate_embedding_request,
    validate_item,
)


openai.organization = settings.openai_api_organization
openai.api_key = settings.openai_api_key


# pylint: disable=unused-argument
# pylint: disable=too-many-locals
def handler(event, context):
    """
    Main Lambda handler function.

    Responsible for processing incoming requests and invoking the appropriate
    OpenAI API endpoint based on the contents of the request.
    """
    cloudwatch_handler(event)
    try:
        openai_results = {}
        request_body = get_request_body(event=event)
        end_point, model, messages, input_text, temperature, max_tokens = parse_request(request_body)
        request_meta_data = {
            "request_meta_data": {
                "lambda": "lambda_openai_v2",
                "model": model,
                "end_point": end_point,
                "temperature": temperature,
                "max_tokens": max_tokens,
            }
        }

        match end_point:
            case OpenAIEndPoint.ChatCompletion:
                # https://platform.openai.com/docs/guides/gpt/chat-completions-api
                validate_item(
                    item=model,
                    valid_items=VALID_CHAT_COMPLETION_MODELS,
                    item_type="ChatCompletion models",
                )
                validate_completion_request(request_body)
                openai_results = openai.ChatCompletion.create(
                    model=model,
                    messages=messages,
                    temperature=temperature,
                    max_tokens=max_tokens,
                )

            case OpenAIEndPoint.Embedding:
                # https://platform.openai.com/docs/guides/embeddings/embeddings
                validate_item(
                    item=model,
                    valid_items=VALID_EMBEDDING_MODELS,
                    item_type="Embedding models",
                )
                validate_embedding_request(request_body)
                openai_results = openai.Embedding.create(input=input_text, model=model)

            case OpenAIEndPoint.Image:
                # https://platform.openai.com/docs/guides/images
                n = request_body.get("n", settings.openai_endpoint_image_n)  # pylint: disable=invalid-name
                size = request_body.get("size", settings.openai_endpoint_image_size)
                return openai.Image.create(prompt=input_text, n=n, size=size)

            case OpenAIEndPoint.Moderation:
                # https://platform.openai.com/docs/guides/moderation
                openai_results = openai.Moderation.create(input=input_text)

            case OpenAIEndPoint.Models:
                openai_results = openai.Model.retrieve(model) if model else openai.Model.list()

            case OpenAIEndPoint.Audio:
                raise NotImplementedError("Audio support is coming soon")

    # handle anything that went wrong
    # pylint: disable=broad-exception-caught
    except Exception as e:
        status_code, _message = EXCEPTION_MAP.get(type(e), (500, "Internal server error"))
        return http_response_factory(status_code=status_code, body=exception_response_factory(e))

    # success!! return the results
    return http_response_factory(
        status_code=OpenAIResponseCodes.HTTP_RESPONSE_OK,
        body={**openai_results, **request_meta_data},
    )