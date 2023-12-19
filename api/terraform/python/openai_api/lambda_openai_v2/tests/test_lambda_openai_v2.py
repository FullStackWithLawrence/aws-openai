# -*- coding: utf-8 -*-
# pylint: disable=wrong-import-position
# pylint: disable=R0801
"""Test lambda_openai_v2 function."""

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


from openai_api.lambda_openai_v2.lambda_handler import handler  # noqa: E402

# our stuff
from openai_api.lambda_openai_v2.tests.test_setup import get_test_file  # noqa: E402


class TestLambdaOpenai(unittest.TestCase):
    """Test Index Lambda function."""

    # load a mock lambda_index event
    event = get_test_file("json/passthrough_openai_v2_request.json")

    def setUp(self):
        """Set up test fixtures."""

    def test_lambda_handler(self):
        """Test lambda_handler."""
        response = handler(self.event, None)
        self.assertEqual(response["statusCode"], 200)
        self.assertTrue("body" in response)
        self.assertTrue("isBase64Encoded" in response)
        body = response["body"]
        self.assertTrue("id" in body)
        self.assertTrue("object" in body)
        self.assertTrue("created" in body)
        self.assertTrue("model" in body)
        self.assertTrue("choices" in body)
        self.assertTrue("completion" in body)
        self.assertTrue("request_meta_data" in body)
        self.assertTrue("usage" in body)
