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

from langchain.chat_models import ChatOpenAI
from langchain.prompts import (
    ChatPromptTemplate,
    MessagesPlaceholder,
    SystemMessagePromptTemplate,
    HumanMessagePromptTemplate,
)
from langchain.chains import LLMChain
from langchain.memory import ConversationBufferMemory

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
from openai_utils.utils import (
    http_response_factory,
    exception_response_factory,
    dump_environment,
    get_request_body,
    parse_request,
    get_content_for_role,
    get_message_history,
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
LANGCHAIN_MEMORY_KEY = "chat_history"


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
                """
                Need to keep in mind that this is a stateless operation. We have to bring
                everything we need to run the conversation with us. This means we need to
                extract the message history from the request body, and we need to initialize
                the memory object with the message history.
                """
                # 1. extract and validate the source data from the http request
                validate_item(
                    item=model,
                    valid_items=VALID_CHAT_COMPLETION_MODELS,
                    item_type="ChatCompletion models",
                )
                validate_completion_request(request_body)
                system_message = get_content_for_role(messages, "system")
                user_message = get_content_for_role(messages, "user")

                # 2. initialize the LangChain ChatOpenAI model
                # https://python.langchain.com/docs/modules/memory/
                llm = ChatOpenAI(
                    model=model, temperature=temperature, max_tokens=max_tokens
                )
                prompt = ChatPromptTemplate(
                    messages=[
                        SystemMessagePromptTemplate.from_template(system_message),
                        MessagesPlaceholder(variable_name=LANGCHAIN_MEMORY_KEY),
                        HumanMessagePromptTemplate.from_template("{question}"),
                    ]
                )

                # 3. extract message history and initialize memory
                message_history = get_message_history(messages)
                memory = ConversationBufferMemory(
                    memory_key=LANGCHAIN_MEMORY_KEY, return_messages=True
                )
                memory.load_memory_variables(message_history)

                # 4. run the conversation
                conversation = LLMChain(
                    llm=llm, prompt=prompt, memory=memory, verbose=True
                )
                conversation({"question": user_message})

                # 5. return the results
                openai_results = conversation

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
