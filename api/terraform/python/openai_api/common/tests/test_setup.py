# -*- coding: utf-8 -*-
# pylint: disable=wrong-import-position
"""Test Search Lambda function."""

import base64

# python stuff
import json
import os
import sys


HERE = os.path.abspath(os.path.dirname(__file__))
PYTHON_ROOT = os.path.dirname(HERE)
sys.path.append(PYTHON_ROOT)  # noqa: E402


def noop():
    """Test to ensure that test suite setup works and that lambda_handler is importable."""


def get_test_file(filename: str):
    """Load a mock lambda_index event."""
    path = os.path.join(HERE, "mock_data", filename)
    with open(path, "r", encoding="utf-8") as file:
        return json.load(file)


def get_test_image(filename: str):
    """Load a mock lambda_index event."""
    path = os.path.join(HERE, "mock_data", "img", filename)
    with open(path, "rb") as file:
        return file.read()


def pack_image_data(filename: str):
    """extract and decode the raw image data from the event"""
    image_raw = get_test_image(filename)
    image_decoded = base64.b64decode(image_raw)

    # https://stackoverflow.com/questions/6269765/what-does-the-b-character-do-in-front-of-a-string-literal
    # Image: base64-encoded bytes or an S3 object.
    # Image={
    #     'Bytes': b'bytes',
    #     'S3Object': {
    #         'Bucket': 'string',
    #         'Name': 'string',
    #         'Version': 'string'
    #     }
    # },
    return {"Bytes": image_decoded}
