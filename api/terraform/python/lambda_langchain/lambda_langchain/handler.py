"""
written by: Lawrence McDaniel
            https://lawrencemcdaniel.com/

date:       sep-2023

usage:
    see: https://www.youtube.com/watch?v=aywZrzNaKjs
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
import os  # library for interacting with the operating system
from dotenv import load_dotenv, find_dotenv

import openai
from lambda_langchain.wrapper import (
    process_request as process_langchain_request,
)
from lambda_langchain.const import (
    OpenAIEndPoint,
    HTTP_RESPONSE_OK,
    HTTP_RESPONSE_BAD_REQUEST,
    HTTP_RESPONSE_INTERNAL_SERVER_ERROR,
    VALID_CHAT_COMPLETION_MODELS,
    VALID_EMBEDDING_MODELS,
)
from lambda_langchain.utils import (
    http_response_factory,
    exception_response_factory,
    dump_environment,
    get_request_body,
    parse_request,
)
from lambda_langchain.validators import (
    validate_item,
    validate_request_body,
    validate_messages,
    validate_completion_request,
    validate_embedding_request,
)


###############################################################################
# https://platform.openai.com/api_keys
###############################################################################
dotenv_path = find_dotenv()
if os.path.exists(dotenv_path):
    # this is only used during local development and unit testing
    load_dotenv(dotenv_path=dotenv_path, verbose=True)

OPENAI_ENDPOINT_IMAGE_N = int(os.getenv("OPENAI_ENDPOINT_IMAGE_N", 4))
OPENAI_ENDPOINT_IMAGE_SIZE = os.getenv("OPENAI_ENDPOINT_IMAGE_SIZE", "1024x768")
openai.organization = os.getenv("OPENAI_API_ORGANIZATION")
openai.api_key = os.getenv("OPENAI_API_KEY")


def handler(event, context, api_key=None, organization=None, pinecone_api_key=None):
    """
    Main Lambda handler function.

    Responsible for processing incoming requests and invoking the appropriate
    OpenAI API endpoint based on the contents of the request.
    """
    # set api key if not already set
    if api_key and not openai.api_key:
        openai.api_key = api_key
    if organization and not openai.organization:
        openai.organization = organization
    if pinecone_api_key:
        pass

    dump_environment(event)
    try:
        openai_results = {}
        # ----------------------------------------------------------------------
        # initialize, parse and validate the request
        # ----------------------------------------------------------------------
        request_body = get_request_body(event=event)
        validate_request_body(request_body=request_body)
        end_point, model, messages, input_text, temperature, max_tokens = parse_request(
            request_body
        )
        validate_messages(request_body=request_body)

        match end_point:
            case OpenAIEndPoint.ChatCompletion:
                # https://platform.openai.com/docs/guides/gpt/chat-completions-api
                validate_item(
                    item=model,
                    valid_items=VALID_CHAT_COMPLETION_MODELS,
                    item_type="ChatCompletion models",
                )
                validate_completion_request(request_body)
                openai_results = process_langchain_request(
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
    except (openai.APIError, ValueError, TypeError, NotImplementedError) as e:
        # 400 Bad Request
        return http_response_factory(
            status_code=HTTP_RESPONSE_BAD_REQUEST, body=exception_response_factory(e)
        )
    except (openai.OpenAIError, Exception) as e:
        # 500 Internal Server Error
        return http_response_factory(
            status_code=HTTP_RESPONSE_INTERNAL_SERVER_ERROR,
            body=exception_response_factory(e),
        )

    # success!! return the results
    return http_response_factory(status_code=HTTP_RESPONSE_OK, body=openai_results)
