# -*- coding: utf-8 -*-
"""A module containing constants for the OpenAI API."""
import os
import openai

HTTP_RESPONSE_OK = 200
HTTP_RESPONSE_BAD_REQUEST = 400
HTTP_RESPONSE_INTERNAL_SERVER_ERROR = 500
DEBUG_MODE = os.getenv("DEBUG_MODE", "False").lower() in ("true", "1", "t")


class OpenAIEndPoint:
    """
    A class representing an endpoint for the OpenAI API.

    Attributes:
        api_key (str): The API key to use for authentication.
        endpoint (str): The URL of the OpenAI API endpoint.
    """

    Embedding = openai.Embedding.__name__
    ChatCompletion = openai.ChatCompletion.__name__
    Moderation = openai.Moderation.__name__
    Image = openai.Image.__name__
    Audio = openai.Audio.__name__
    Models = openai.Model.__name__
    all_endpoints = [Embedding, ChatCompletion, Moderation, Image, Audio, Models]


class OpenAIMessageKeys:
    """A class representing the keys for a message in the OpenAI API."""

    OPENAI_USER_MESSAGE_KEY = "user"
    OPENAI_ASSISTANT_MESSAGE_KEY = "assistant"
    OPENAI_SYSTEM_MESSAGE_KEY = "system"
    all = [
        OPENAI_SYSTEM_MESSAGE_KEY,
        OPENAI_USER_MESSAGE_KEY,
        OPENAI_ASSISTANT_MESSAGE_KEY,
    ]


VALID_CHAT_COMPLETION_MODELS = [
    "gpt-4",
    "gpt-4-0613",
    "gpt-4-32k",
    "gpt-4-32k-0613",
    "gpt-3.5-turbo",
    "gpt-3.5-turbo-0613",
    "gpt-3.5-turbo-16k",
    "gpt-3.5-turbo-16k-0613",
]
VALID_EMBEDDING_MODELS = [
    "text-embedding-ada-002",
    "text-similarity-*-001",
    "text-search-*-*-001",
    "code-search-*-*-001",
]

LANGCHAIN_MESSAGE_HISTORY_ROLES = ["user", "assistant"]
