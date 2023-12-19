# -*- coding: utf-8 -*-
# pylint: disable=wrong-import-position
# pylint: disable=R0801
"""Test lambda_langchain function."""

# python stuff
import os
import sys
import unittest
from pathlib import Path


HERE = os.path.abspath(os.path.dirname(__file__))
PROJECT_ROOT = str(Path(HERE).parent.parent)
PYTHON_ROOT = str(Path(PROJECT_ROOT).parent)
if PYTHON_ROOT not in sys.path:
    sys.path.append(PYTHON_ROOT)  # noqa: E402

from openai_api.lambda_langchain.lambda_handler import handler  # noqa: E402

# our stuff
from openai_api.lambda_langchain.tests.test_setup import get_test_file  # noqa: E402


class TestLambdaLangchain(unittest.TestCase):
    """Test Index Lambda function."""

    # load a mock lambda_index event
    event = get_test_file("json/passthrough_langchain_request.json")

    def setUp(self):
        """Set up test fixtures."""

    def test_lambda_handler(self):
        """Test lambda_handler."""
        response = handler(self.event, None)
        self.assertEqual(response["statusCode"], 200)
        self.assertTrue("body" in response)
        self.assertTrue("isBase64Encoded" in response)
        body = response["body"]
        self.assertTrue("chat_memory" in body)
        self.assertTrue("memory_key" in body)
        self.assertTrue("request_meta_data" in body)
