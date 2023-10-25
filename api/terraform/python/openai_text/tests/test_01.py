from dotenv import load_dotenv
import os
import json
from ..openai_text import handler
import pytest


def get_repo_root():
    # Get the path to the root directory of the repository
    cmd = "git rev-parse --show-toplevel"
    result = os.popen(cmd).read().strip()
    return result


# Load environment variables from .env file in all folders
dotenv_path = os.path.join(get_repo_root(), ".env")
if os.path.exists(dotenv_path):
    load_dotenv(dotenv_path=dotenv_path, verbose=True)
    OPENAI_API_KEY = os.environ["OPENAI_API_KEY"]
    OPENAI_API_ORGANIZATION = os.environ["OPENAI_API_ORGANIZATION"]
else:
    raise Exception("No .env file found in root directory of repository")


def test_basic_request():
    print(f"OPENAI_API_KEY: {OPENAI_API_KEY}")
    print(f"OPENAI_API_ORGANIZATION: {OPENAI_API_ORGANIZATION}")

    with open("tests/events/test_01.request.json", "r") as f:
        event = json.load(f)

    retval = handler(
        event=event,
        context=None,
        api_key=OPENAI_API_KEY,
        organization=OPENAI_API_ORGANIZATION,
    )

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
