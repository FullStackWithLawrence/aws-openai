# -*- coding: utf-8 -*-
# pylint: disable=wrong-import-position
# pylint: disable=R0801
"""Test Index Lambda function."""

# python stuff
import os
import sys
import unittest


HERE = os.path.abspath(os.path.dirname(__file__))
PYTHON_ROOT = os.path.dirname(os.path.dirname(HERE))
sys.path.append(PYTHON_ROOT)  # noqa: E402


# our stuff
from openai_api.common.tests.test_setup import get_test_file  # noqa: E402


class TestLambdaIndex(unittest.TestCase):
    """Test Index Lambda function."""

    # load a mock lambda_index event
    event = get_test_file("json/apigateway_index_lambda_event.json")
    event = event["event"]
    response = get_test_file("json/apigateway_index_lambda_response.json")

    def setUp(self):
        """Set up test fixtures."""

    def get_event(self, event):
        """Get the event json from the mock file."""
        return event["event"]
