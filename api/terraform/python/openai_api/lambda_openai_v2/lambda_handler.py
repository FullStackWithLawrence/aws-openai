# -*- coding: utf-8 -*-
# pylint: disable=no-member
# pylint: disable=R0801
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
    /v1/chat/completions	    gpt-4, gpt-4-0613, gpt-4-32k, gpt-4-32k-0613, gpt-4-turbo,
                                gpt-4-turbo-0613, gpt-4-turbo-16k, gpt-4-turbo-16k-0613
    /v1/completions (Legacy)	text-davinci-003, text-davinci-002, text-davinci-001, text-curie-001,
                                text-babbage-001, text-ada-001, davinci, curie, babbage, ada
    /v1/embeddings	            text-embedding-ada-002, text-similarity-*-001,
                                text-search-*-*-001, code-search-*-*-001
    /v1/fine_tuning/jobs	    gpt-4-turbo, babbage-002, davinci-002
    /v1/fine-tunes	            davinci, curie, babbage, ada
    /v1/moderations	            text-moderation-stable, text-moderation-latest

"""
import openai
from openai_api.common.conf import settings
from openai_api.common.const import (  # VALID_EMBEDDING_MODELS,
    VALID_CHAT_COMPLETION_MODELS,
    OpenAIObjectTypes,
    OpenAIResponseCodes,
)
from openai_api.common.exceptions import EXCEPTION_MAP
from openai_api.common.utils import (
    cloudwatch_handler,
    exception_response_factory,
    get_request_body,
    http_response_factory,
    parse_request,
    request_meta_data_factory,
)
from openai_api.common.validators import (  # validate_embedding_request,
    validate_completion_request,
    validate_item,
)


openai.organization = settings.openai_api_organization
openai.api_key = settings.openai_api_key.get_secret_value()


# pylint: disable=unused-argument
# pylint: disable=too-many-locals
def handler(event, context):
    """
    Main Lambda handler function.

    Responsible for processing incoming requests and invoking the appropriate
    OpenAI API endpoint based on the contents of the request.
    """
    cloudwatch_handler(event, settings.dump, debug_mode=settings.debug_mode)
    try:
        openai_results = {}
        request_body = get_request_body(event=event)
        object_type, model, messages, input_text, temperature, max_tokens = parse_request(request_body)
        request_meta_data = request_meta_data_factory(model, object_type, temperature, max_tokens, input_text)

        match object_type:
            case OpenAIObjectTypes.ChatCompletion:
                # https://platform.openai.com/docs/guides/gpt/chat-completions-api
                validate_item(
                    item=model,
                    valid_items=VALID_CHAT_COMPLETION_MODELS,
                    item_type="ChatCompletion models",
                )
                validate_completion_request(request_body)
                openai_results = openai.chat.completions.create(
                    model=model,
                    messages=messages,
                    temperature=temperature,
                    max_tokens=max_tokens,
                )
                openai_results = openai_results.model_dump()

            case OpenAIObjectTypes.Embedding:
                # https://platform.openai.com/docs/guides/embeddings/embeddings
                raise NotImplementedError("Refactoring of Embedding API v1 is in progress.")
                # validate_item(
                #     item=model,
                #     valid_items=VALID_EMBEDDING_MODELS,
                #     item_type="Embedding models",
                # )
                # validate_embedding_request(request_body)
                # openai_results = openai.Embedding.create(input=input_text, model=model)

            case OpenAIObjectTypes.Image:
                # https://platform.openai.com/docs/guides/images
                raise NotImplementedError("Refactoring of Image API v1 is in progress.")
                # n = request_body.get("n", settings.openai_endpoint_image_n)  # pylint: disable=invalid-name
                # size = request_body.get("size", settings.openai_endpoint_image_size)
                # return openai.Image.create(prompt=input_text, n=n, size=size)

            case OpenAIObjectTypes.Moderation:
                # https://platform.openai.com/docs/guides/moderation
                raise NotImplementedError("Refactoring of Moderation API v1 is in progress.")
                # openai_results = openai.Moderation.create(input=input_text)

            case OpenAIObjectTypes.Models:
                raise NotImplementedError("Refactoring of Models API v1 is in progress.")
                # openai_results = openai.Model.retrieve(model) if model else openai.Model.list()

            case OpenAIObjectTypes.Audio:
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
