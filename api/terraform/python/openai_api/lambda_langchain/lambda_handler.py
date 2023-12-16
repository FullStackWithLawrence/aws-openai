# -*- coding: utf-8 -*-
# pylint: disable=E1101,E0401
# pylint: disable=duplicate-code
"""
written by: Lawrence McDaniel
            https://lawrencemcdaniel.com/

date:       nov-2023

usage:      Use langchain to process requests to the OpenAI API.
            an OpenAI API key is required.
            see: https://platform.openai.com/api_keys

            https://python.langchain.com/docs/modules/memory/

            To do: persist message history to DynamoDB
            https://python.langchain.com/docs/integrations/memory/aws_dynamodb
            https://bobbyhadz.com/blog/react-generate-unique-id
"""
import json
import os

# OpenAI imports
import openai
from dotenv import find_dotenv, load_dotenv
from langchain.chains import LLMChain

# Langchain imports
from langchain.chat_models import ChatOpenAI
from langchain.memory import ConversationBufferMemory
from langchain.prompts import (
    ChatPromptTemplate,
    HumanMessagePromptTemplate,
    MessagesPlaceholder,
    SystemMessagePromptTemplate,
)

# local imports from 'layer_genai' virtual environment or AWS Lambda layer.
from openai_api.common.const import (
    HTTP_RESPONSE_BAD_REQUEST,
    HTTP_RESPONSE_INTERNAL_SERVER_ERROR,
    HTTP_RESPONSE_OK,
    VALID_CHAT_COMPLETION_MODELS,
    VALID_EMBEDDING_MODELS,
    OpenAIEndPoint,
    OpenAIMessageKeys,
)
from openai_api.common.utils import (
    dump_environment,
    exception_response_factory,
    get_content_for_role,
    get_message_history,
    get_messages_for_role,
    get_request_body,
    http_response_factory,
    parse_request,
)
from openai_api.common.validators import (
    validate_completion_request,
    validate_embedding_request,
    validate_item,
    validate_messages,
    validate_request_body,
)


# from langchain.memory.chat_message_histories.in_memory import ChatMessageHistory
# from langchain.schema.messages import HumanMessage, SystemMessage, AIMessage
# from langchain.schema.messages import BaseMessage


###############################################################################
# ENVIRONMENT CREDENTIALS
###############################################################################

# for local development and unit testing
dotenv_path = find_dotenv()
if os.path.exists(dotenv_path):
    load_dotenv(dotenv_path=dotenv_path, verbose=True)

# for production these values are set inside the AWS Lambda function environment
# see ./env.sh and lambda_langchain.tf
OPENAI_ENDPOINT_IMAGE_N = int(os.getenv("OPENAI_ENDPOINT_IMAGE_N", "4"))
OPENAI_ENDPOINT_IMAGE_SIZE = os.getenv("OPENAI_ENDPOINT_IMAGE_SIZE", "1024x768")
openai.organization = os.getenv("OPENAI_API_ORGANIZATION", "SET-ME-WITH-DOTENV")
openai.api_key = os.getenv("OPENAI_API_KEY", "SET-ME-WITH-DOTENV")

###############################################################################
# Transformations for the LangChain API for OpenAI
###############################################################################
LANGCHAIN_MEMORY_KEY = "chat_history"


# pylint: disable=too-many-locals
# pylint: disable=unused-argument
def handler(event, context, api_key=None, organization=None, pinecone_api_key=None):
    """
    Process incoming requests and invoking the appropriate
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
        end_point, model, messages, input_text, temperature, max_tokens = parse_request(request_body)
        validate_messages(request_body=request_body)
        request_meta_data = {
            "request_meta_data": {
                "lambda": "lambda_langchain",
                "model": model,
                "end_point": end_point,
                "temperature": temperature,
                "max_tokens": max_tokens,
            }
        }

        match end_point:
            case OpenAIEndPoint.ChatCompletion:
                # pylint: disable=pointless-string-statement
                """
                Need to keep in mind that this is a stateless operation. We have to bring
                along everything needed to run the conversation. This means we need to
                extract the message history from the request body, and we need to initialize
                the memory object with the message history.
                """
                # 1. extract and validate the source data from the http request
                # -------------------------------------------------------------
                validate_item(
                    item=model,
                    valid_items=VALID_CHAT_COMPLETION_MODELS,
                    item_type="ChatCompletion models",
                )
                validate_completion_request(request_body)
                system_message = get_content_for_role(messages, OpenAIMessageKeys.OPENAI_SYSTEM_MESSAGE_KEY)
                user_message = get_content_for_role(messages, OpenAIMessageKeys.OPENAI_USER_MESSAGE_KEY)

                # 2. initialize the LangChain ChatOpenAI model
                # -------------------------------------------------------------
                llm = ChatOpenAI(model=model, temperature=temperature, max_tokens=max_tokens)
                prompt = ChatPromptTemplate(
                    messages=[
                        SystemMessagePromptTemplate.from_template(system_message),
                        MessagesPlaceholder(variable_name=LANGCHAIN_MEMORY_KEY),
                        HumanMessagePromptTemplate.from_template("{question}"),
                    ]
                )

                # 3. extract message history and initialize memory
                # -------------------------------------------------------------
                memory = ConversationBufferMemory(
                    memory_key=LANGCHAIN_MEMORY_KEY,
                    return_messages=True,
                )
                message_history = get_message_history(messages)
                user_messages = get_messages_for_role(message_history, OpenAIMessageKeys.OPENAI_USER_MESSAGE_KEY)
                assistant_messages = get_messages_for_role(
                    message_history, OpenAIMessageKeys.OPENAI_ASSISTANT_MESSAGE_KEY
                )
                for i, assistant_message in enumerate(assistant_messages):
                    memory.chat_memory.add_user_message(user_messages[i])
                    memory.chat_memory.add_ai_message(assistant_message)  # pylint: disable=no-member

                # 4. run the conversation
                # -------------------------------------------------------------
                conversation = LLMChain(
                    llm=llm,
                    prompt=prompt,
                    verbose=True,
                    memory=memory,
                )
                conversation({"question": user_message})

                # 5. extract and return the results
                # -------------------------------------------------------------
                conversation_response = json.loads(conversation.memory.json())
                openai_results = conversation_response

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
                n = request_body.get("n", OPENAI_ENDPOINT_IMAGE_N)  # pylint: disable=invalid-name
                size = request_body.get("size", OPENAI_ENDPOINT_IMAGE_SIZE)
                return openai.Image.create(prompt=input_text, n=n, size=size)

            case OpenAIEndPoint.Moderation:
                # https://platform.openai.com/docs/guides/moderation
                openai_results = openai.Moderation.create(input=input_text)

            case OpenAIEndPoint.Models:
                openai_results = openai.Model.retrieve(model) if model else openai.Model.list()

            case OpenAIEndPoint.Audio:
                raise NotImplementedError("Audio support is coming soon")

    # handle anything that went wrong
    except (openai.APIError, ValueError, TypeError, NotImplementedError) as e:  # pylint: disable=invalid-name
        # 400 Bad Request
        return http_response_factory(status_code=HTTP_RESPONSE_BAD_REQUEST, body=exception_response_factory(e))
    # pylint: disable=broad-except
    except (openai.OpenAIError, Exception) as e:  # pylint: disable=broad-except,invalid-name
        # 500 Internal Server Error
        return http_response_factory(
            status_code=HTTP_RESPONSE_INTERNAL_SERVER_ERROR,
            body=exception_response_factory(e),
        )

    # success!! return the results
    return http_response_factory(status_code=HTTP_RESPONSE_OK, body={**openai_results, **request_meta_data})
