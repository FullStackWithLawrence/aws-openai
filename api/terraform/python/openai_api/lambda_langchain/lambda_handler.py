# -*- coding: utf-8 -*-
# pylint: disable=E1101,E0401
# pylint: disable=duplicate-code
# pylint: disable=R0911,R0912,W0718,R0801
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

from langchain.chains import LLMChain
from langchain.memory import ConversationBufferMemory
from langchain.prompts import (
    ChatPromptTemplate,
    HumanMessagePromptTemplate,
    MessagesPlaceholder,
    SystemMessagePromptTemplate,
)
from langchain_openai import ChatOpenAI
from openai_api.common.conf import settings
from openai_api.common.const import (  # VALID_EMBEDDING_MODELS,
    VALID_CHAT_COMPLETION_MODELS,
    OpenAIMessageKeys,
    OpenAIObjectTypes,
    OpenAIResponseCodes,
)
from openai_api.common.exceptions import EXCEPTION_MAP
from openai_api.common.utils import (
    cloudwatch_handler,
    exception_response_factory,
    get_content_for_role,
    get_message_history,
    get_messages_for_role,
    get_request_body,
    http_response_factory,
    parse_request,
    request_meta_data_factory,
)
from openai_api.common.validators import (  # validate_embedding_request,
    validate_completion_request,
    validate_item,
    validate_messages,
    validate_request_body,
)


# from langchain.memory.chat_message_histories.in_memory import ChatMessageHistory
# from langchain.schema.messages import HumanMessage, SystemMessage, AIMessage
# from langchain.schema.messages import BaseMessage


# pylint: disable=too-many-locals
# pylint: disable=unused-argument
def handler(event, context):
    """
    Process incoming requests and invoking the appropriate
    OpenAI API endpoint based on the contents of the request.
    """

    cloudwatch_handler(event, settings.dump, debug_mode=settings.debug_mode)
    try:
        openai_results = {}
        # ----------------------------------------------------------------------
        # initialize, parse and validate the request
        # ----------------------------------------------------------------------
        request_body = get_request_body(event=event)
        validate_request_body(request_body=request_body)
        object_type, model, messages, input_text, temperature, max_tokens = parse_request(request_body)
        request_meta_data = request_meta_data_factory(model, object_type, temperature, max_tokens, input_text)
        validate_messages(request_body=request_body)

        match object_type:
            case OpenAIObjectTypes.ChatCompletion:
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
                llm = ChatOpenAI(
                    model=model,
                    temperature=temperature,
                    max_tokens=max_tokens,
                    api_key=settings.openai_api_key.get_secret_value(),
                )
                prompt = ChatPromptTemplate(
                    messages=[
                        SystemMessagePromptTemplate.from_template(system_message),
                        MessagesPlaceholder(variable_name=settings.langchain_memory_key),
                        HumanMessagePromptTemplate.from_template("{question}"),
                    ]
                )

                # 3. extract message history and initialize memory
                # -------------------------------------------------------------
                memory = ConversationBufferMemory(
                    memory_key=settings.langchain_memory_key,
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
    except Exception as e:
        status_code, _message = EXCEPTION_MAP.get(type(e), (500, "Internal server error"))
        return http_response_factory(status_code=status_code, body=exception_response_factory(e))

    # success!! return the results
    return http_response_factory(
        status_code=OpenAIResponseCodes.HTTP_RESPONSE_OK, body={**openai_results, **request_meta_data}
    )
