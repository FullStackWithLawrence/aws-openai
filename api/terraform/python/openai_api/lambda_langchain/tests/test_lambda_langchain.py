# -*- coding: utf-8 -*-
# pylint: disable=wrong-import-position
"""Test Search Lambda function."""

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
    """Test Search Lambda function."""

    # load a mock lambda_index event
    search_event = get_test_file("json/apigateway_search_lambda_event.json")
    index_event = get_test_file("json/apigateway_index_lambda_event.json")
    response = get_test_file("json/apigateway_search_lambda_response.json")
    dynamodb_records = get_test_file("json/dynamodb-sample-records.json")
    rekognition_search_output = get_test_file("json/rekognition_search_output.json")

    def setUp(self):
        """Set up test fixtures."""
