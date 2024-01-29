# -*- coding: utf-8 -*-
# pylint: disable=wrong-import-position
# pylint: disable=duplicate-code
"""Test configuration Settings class."""

# python stuff
import os
import sys
import unittest
from pathlib import Path

# 3rd party stuff
import boto3
from dotenv import load_dotenv


HERE = os.path.abspath(os.path.dirname(__file__))
PROJECT_ROOT = str(Path(HERE).parent.parent)
PYTHON_ROOT = str(Path(PROJECT_ROOT).parent)
if PYTHON_ROOT not in sys.path:
    sys.path.append(PYTHON_ROOT)  # noqa: E402

from openai_api.common.aws import aws_infrastructure_config  # noqa: E402
from openai_api.common.conf import settings


class TestAWSInfrastructure(unittest.TestCase):
    """Test AWS infrastructure."""

    # -------------------------------------------------------------------------
    # Tests
    # -------------------------------------------------------------------------
    def test_aws_connection_works(self):
        """Test that the AWS connection works."""
        self.assertTrue(aws_infrastructure_config.aws_connection_works(), "AWS connection failed.")

    def test_domain_exists(self):
        """Test that domain name exists in API Gateway."""
        # skip this test if we are using the default domain name
        if settings.aws_apigateway_root_domain == "example.com":
            return

        self.assertTrue(
            aws_infrastructure_config.domain_exists, f"Domain {aws_infrastructure_config.domain} does not exist."
        )

    def test_api_exists(self):
        """Test that the API Gateway exists."""
        api = aws_infrastructure_config.get_api(aws_infrastructure_config.api_gateway_name)
        self.assertIsInstance(api, dict, "API Gateway does not exist.")

    def test_api_resource_example_airportcodes_exists(self):
        """Test that the API Gateway examples/default-airport-codes end point exists."""
        self.assertTrue(
            aws_infrastructure_config.api_resource_and_method_exists("/examples/default-airport-codes", "POST"),
            "API Gateway /examples/default-airport-codes (POST) resource does not exist.",
        )

    def test_api_key_exists(self):
        """Test that an API key exists."""
        api_key = aws_infrastructure_config.get_api_keys()
        self.assertIsInstance(api_key, str, "API key does not exist.")
        self.assertGreaterEqual(len(api_key), 15, "API key is too short.")
