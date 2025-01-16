# -*- coding: utf-8 -*-
# pylint: disable=E1101
"""A module containing constants for the OpenAI API."""
import logging
import os
from pathlib import Path

import hcl2
import openai


MODULE_NAME = "openai_api"
HERE = os.path.abspath(os.path.dirname(__file__))
PROJECT_ROOT = str(Path(HERE).parent)
PYTHON_ROOT = str(Path(PROJECT_ROOT).parent)
TERRAFORM_ROOT = str(Path(PROJECT_ROOT).parent.parent)
REPO_ROOT = str(Path(TERRAFORM_ROOT).parent.parent)

TERRAFORM_TFVARS = os.path.join(TERRAFORM_ROOT, "terraform.tfvars")
if not os.path.exists(TERRAFORM_TFVARS):
    TERRAFORM_TFVARS = os.path.join(PROJECT_ROOT, "terraform.tfvars")

TFVARS = {}
IS_USING_TFVARS = False

logger = logging.getLogger(__name__)

try:
    with open(TERRAFORM_TFVARS, "r", encoding="utf-8") as f:
        TFVARS = hcl2.load(f)
    IS_USING_TFVARS = True
except FileNotFoundError:
    logger.debug("No terraform.tfvars file found. Using default values.")


# pylint: disable=too-few-public-methods
class OpenAIResponseCodes:
    """Http response codes from openai API"""

    HTTP_RESPONSE_OK = 200
    HTTP_RESPONSE_BAD_REQUEST = 400
    HTTP_RESPONSE_INTERNAL_SERVER_ERROR = 500


class OpenAIObjectTypes:
    """V1 API Object Types (replace OpeanAIEndPoint)"""

    Embedding = "embedding"
    ChatCompletion = "chat.completion"
    Moderation = "moderation"
    Image = "image"
    Audio = "audio"
    Models = "models"
    all_object_types = [Embedding, ChatCompletion, Moderation, Image, Audio, Models]


# pylint: disable=too-few-public-methods
class OpenAIEndPoint:
    """
    A class representing an endpoint for the OpenAI API.

    Attributes:
        api_key (str): The API key to use for authentication.
        endpoint (str): The URL of the OpenAI API endpoint.
    """

    Embedding = openai.Embedding.__name__
    ChatCompletion = "chat/completions"
    Moderation = openai.Moderation.__name__
    Image = openai.Image.__name__
    Audio = openai.Audio.__name__
    Models = openai.Model.__name__
    all_endpoints = [Embedding, ChatCompletion, Moderation, Image, Audio, Models]


# pylint: disable=too-few-public-methods
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
    "gpt-4-turbo",
    "gpt-4-32k",
    "gpt-4-1106-preview",
    "gpt-4-0613",
    "gpt-4-32k",
    "gpt-4-32k-0613",
    "gpt-4-turbo",
    "gpt-4-turbo-0613",
    "gpt-4-turbo-16k",
    "gpt-4-turbo-16k-0613",
    "gpt-4-turbo-1106",
    "gpt-4-turbo-instruct",
]
VALID_EMBEDDING_MODELS = [
    "text-embedding-ada-002",
    "text-similarity-*-001",
    "text-search-*-*-001",
    "code-search-*-*-001",
]

LANGCHAIN_MESSAGE_HISTORY_ROLES = ["user", "assistant"]
