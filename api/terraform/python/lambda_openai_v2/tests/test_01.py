# flake8: noqa: F401
# pylint: disable=R0801
# pylint: disable=duplicate-code
"""
Test requests to the OpenAI API using the Lambda Layer, 'genai'.
"""
import os

import pytest  # pylint: disable=unused-import
from dotenv import find_dotenv, load_dotenv
from lambda_openai_v2.lambda_handler import handler
from lambda_openai_v2.tests.init import get_event


# Load environment variables from .env file in all folders
dotenv_path = find_dotenv()
if os.path.exists(dotenv_path):
    load_dotenv(dotenv_path=dotenv_path, verbose=True)
    OPENAI_API_KEY = os.environ["OPENAI_API_KEY"]
    OPENAI_API_ORGANIZATION = os.environ["OPENAI_API_ORGANIZATION"]
    PINECONE_API_KEY = os.environ["PINECONE_API_KEY"]
else:
    raise FileNotFoundError("No .env file found in root directory of repository")


def handle_event_wrapper(event):
    """Wrapper for the Lambda handler function."""
    retval = handler(event=event, context=None)
    return retval


# pylint: disable=too-few-public-methods
class TestOpenAIText:
    """Test the OpenAI API using the Lambda Layer, 'genai'."""

    def test_basic_request(self):
        """Test a basic request"""
        event = get_event("tests/events/test_01.request.json")
        retval = handle_event_wrapper(event=event)
        print(retval)

        assert retval["statusCode"] == 200
        assert retval["body"]["object"] == "chat.completion"
        assert isinstance(retval["body"]["created"], int)
        assert retval["body"]["model"] == "gpt-3.5-turbo-0613"

        choice = retval["body"]["choices"][0]
        assert choice["index"] == 0
        assert choice["message"]["role"] == "assistant"
        assert choice["finish_reason"] == "stop"

        assert isinstance(retval["body"]["usage"]["prompt_tokens"], int)
        assert isinstance(retval["body"]["usage"]["completion_tokens"], int)
        assert isinstance(retval["body"]["usage"]["total_tokens"], int)
