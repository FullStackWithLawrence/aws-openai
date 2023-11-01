"""
written by: Lawrence McDaniel
            https://lawrencemcdaniel.com/

date:       nov-2023

usage:      Use langchain to process requests to the OpenAI API.
            an OpenAI API key is required.
            see: https://platform.openai.com/api_keys
"""
import os
from dotenv import load_dotenv, find_dotenv
from langchain.schema import HumanMessage, SystemMessage
from langchain.chat_models import ChatOpenAI
import openai

# local imports from 'layer_genai' virtual environment or AWS Lambda layer.
from openai_utils.const import (
    OpenAIEndPoint,
    HTTP_RESPONSE_OK,
    HTTP_RESPONSE_BAD_REQUEST,
    HTTP_RESPONSE_INTERNAL_SERVER_ERROR,
    VALID_CHAT_COMPLETION_MODELS,
    VALID_EMBEDDING_MODELS,
)
from openai_utils import (
    http_response_factory,
    exception_response_factory,
    dump_environment,
    get_request_body,
    parse_request,
)
from openai_utils.validators import (
    validate_item,
    validate_request_body,
    validate_messages,
    validate_completion_request,
    validate_embedding_request,
)

###############################################################################
# ENVIRONMENT CREDENTIALS
###############################################################################

# for local development and unit testing
dotenv_path = find_dotenv()
if os.path.exists(dotenv_path):
    load_dotenv(dotenv_path=dotenv_path, verbose=True)

# for production these values are set inside the AWS Lambda function environment
# see ./env.sh and lambda_langchain.tf
OPENAI_ENDPOINT_IMAGE_N = int(os.getenv("OPENAI_ENDPOINT_IMAGE_N", 4))
OPENAI_ENDPOINT_IMAGE_SIZE = os.getenv("OPENAI_ENDPOINT_IMAGE_SIZE", "1024x768")
openai.organization = os.getenv("OPENAI_API_ORGANIZATION", "SET-ME-WITH-DOTENV")
openai.api_key = os.getenv("OPENAI_API_KEY", "SET-ME-WITH-DOTENV")

###############################################################################
# Transformations for the LangChain API for OpenAI
###############################################################################


def get_content_for_role(messages: list, role: str) -> str:
    """Get the text content from the messages list for a given role"""
    retval = [d.get("content") for d in messages if d["role"] == role][0]
    return retval


def process_langchain_request(model, messages, temperature, max_tokens) -> str:
    chat = ChatOpenAI(model_name=model, temperature=temperature, max_tokens=max_tokens)

    system_message = get_content_for_role(messages, "system")
    user_message = get_content_for_role(messages, "user")
    messages = [
        SystemMessage(content=system_message),
        HumanMessage(content=user_message),
    ]
    retval = chat(messages)
    return retval.content


###############################################################################
# Main Lambda Handler
###############################################################################


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
