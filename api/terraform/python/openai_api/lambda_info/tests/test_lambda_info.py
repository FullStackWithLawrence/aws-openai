# -*- coding: utf-8 -*-
# pylint: disable=wrong-import-position
# pylint: disable=R0801
# pylint: disable=broad-exception-caught
"""Test lambda_openai_v2 function."""

# python stuff
import json
import os
import sys
import unittest
from pathlib import Path

import yaml


HERE = os.path.abspath(os.path.dirname(__file__))
PROJECT_ROOT = str(Path(HERE).parent.parent)
PYTHON_ROOT = str(Path(PROJECT_ROOT).parent)
if PYTHON_ROOT not in sys.path:
    sys.path.append(PYTHON_ROOT)  # noqa: E402


from openai_api.lambda_info.lambda_handler import handler  # noqa: E402; handler,


class TestLambdaInfo(unittest.TestCase):
    """Test Index Lambda function."""

    def setUp(self):
        """Set up test fixtures."""

    def check_response(self, response):
        """Check response structure from lambda_handler."""
        self.assertEqual(response["statusCode"], 200)
        self.assertEqual(response["statusCode"], 200)
        self.assertTrue("body" in response)
        self.assertTrue("isBase64Encoded" in response)
        body = json.loads(response["body"])
        self.assertTrue("aws" in body)
        self.assertTrue("settings" in body)

    def test_lambda_handler(self):
        """Test lambda_handler."""
        response = None
        event = {}

        try:
            response = handler(event, None)
        except Exception as error:
            self.fail(f"handler() raised {error}")
        self.check_response(response)
