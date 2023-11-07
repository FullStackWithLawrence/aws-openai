# flake8: noqa: F401
"""
Test requests to the OpenAI API via Langchain using the Lambda Layer, 'genai'.
"""
import pytest
import os
from dotenv import load_dotenv, find_dotenv
from lambda_langchain.tests.init import get_event
from lambda_langchain.lambda_handler import handler

# Load environment variables from .env file in all folders
dotenv_path = find_dotenv()
if os.path.exists(dotenv_path):
    load_dotenv(dotenv_path=dotenv_path, verbose=True)
    OPENAI_API_KEY = os.environ["OPENAI_API_KEY"]
    OPENAI_API_ORGANIZATION = os.environ["OPENAI_API_ORGANIZATION"]
    PINECONE_API_KEY = os.environ["PINECONE_API_KEY"]
else:
    raise Exception("No .env file found in root directory of repository")


def handle_event_wrapper(event):
    retval = handler(event=event, context=None)
    return retval


class TestLangchain:
    def test_basic_request(self):
        """Test a basic request"""
        event = get_event("tests/events/test_01.request.json")
        retval = handle_event_wrapper(event=event)
        print(retval)

        assert "statusCode" in retval, "statusCode key not found in retval"
        assert "isBase64Encoded" in retval, "isBase64Encoded key not found in retval"
        assert "body" in retval, "body key not found in retval"

        assert retval["statusCode"] == 200
        assert retval["isBase64Encoded"] == False
        assert isinstance(retval["body"], dict)
