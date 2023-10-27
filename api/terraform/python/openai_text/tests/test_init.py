from dotenv import load_dotenv, find_dotenv
import os
import json
from openai_text.lambda_handler import handler

# Load environment variables from .env file in all folders
dotenv_path = find_dotenv()
if os.path.exists(dotenv_path):
    load_dotenv(dotenv_path=dotenv_path, verbose=True)
    OPENAI_API_KEY = os.environ["OPENAI_API_KEY"]
    OPENAI_API_ORGANIZATION = os.environ["OPENAI_API_ORGANIZATION"]
    PINECONE_API_KEY = os.environ["PINECONE_API_KEY"]
else:
    raise Exception("No .env file found in root directory of repository")


def get_event(filespec):
    with open(filespec, "r") as f:
        event = json.load(f)
        return event


def handle_event(event):
    retval = handler(
        event=event,
        context=None,
        api_key=OPENAI_API_KEY,
        organization=OPENAI_API_ORGANIZATION,
        pinecone_api_key=PINECONE_API_KEY,
    )
    return retval
