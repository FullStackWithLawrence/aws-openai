# -*- coding: utf-8 -*-
# pylint: disable=wrong-import-position
# pylint: disable=duplicate-code
"""Test configuration Settings class."""

# python stuff
import json
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

from openai_api.common.conf import settings  # noqa: E402


# pylint: disable=too-many-instance-attributes,too-many-public-methods
class TestAWSInfrastructureBase(unittest.TestCase):
    """Base class for AWS infrastructure tests."""

    _aws_session: boto3.Session = None
    _domain = None
    _domain_exists: bool = False

    def env_path(self, filename):
        """Return the path to the .env file."""
        return os.path.join(HERE, filename)

    def setUp(self):
        """Set up test fixtures."""
        env_path = self.env_path(".env")
        load_dotenv(env_path)

        # environment variables
        self.aws_region = settings.aws_region
        self.aws_profile = settings.aws_profile

    @property
    def domain(self):
        """Return the domain."""
        if not self._domain:
            if self.create_custom_domain:
                self._domain = (
                    os.getenv(key="DOMAIN") or "api." + self.shared_resource_identifier + "." + self.root_domain
                )
                return self._domain

            response = self.api_client.get_rest_apis()
            for item in response["items"]:
                if item["name"] == self.api_gateway_name:
                    api_id = item["id"]
                    self._domain = f"{api_id}.execute-api.{self.aws_region}.amazonaws.com"
        return self._domain

    @property
    def api_gateway_name(self):
        """Return the API Gateway name."""
        return self.shared_resource_identifier + "-api"

    @property
    def shared_resource_identifier(self):
        """Return the shared resource identifier."""
        return settings.shared_resource_identifier

    @property
    def root_domain(self):
        """Return the root domain."""
        return settings.aws_apigateway_root_domain

    @property
    def aws_session(self) -> boto3.Session:
        """Return a new AWS session."""
        return settings.aws_session

    @property
    def s3_client(self):
        """Return the S3 client."""
        return settings.s3_client

    @property
    def dynamodb(self):
        """Return the DynamoDB client."""
        return settings.dynamodb_client

    @property
    def api_client(self):
        """Return the API Gateway client."""
        return settings.api_client

    @property
    def create_custom_domain(self) -> bool:
        """Return the CREATE_CUSTOM_DOMAIN_NAME value."""
        return settings.aws_apigateway_custom_domain_name_create

    def get_url(self, path):
        """Return the url for the given path."""
        return f"https://{self.domain}{path}"

    def aws_connection_works(self):
        """Test that the AWS connection works."""
        try:
            # Try a benign operation
            self.s3_client.list_buckets()
            return True
        except Exception:  # pylint: disable=broad-exception-caught
            return False

    def domain_exists(self):
        """Test that the domain exists in API Gateway."""
        if self._domain_exists:
            return True
        if self.create_custom_domain:
            response = self.api_client.get_domain_names()
            for item in response["items"]:
                if item.get("domainName") == self.domain:
                    self._domain_exists = True
                    break
                if item.get("regionalDomainName") == self.domain:
                    self._domain_exists = True
                    break
                if item.get("distributionDomainName") == self.domain:
                    self._domain_exists = True
                    break
        else:
            response = self.api_client.get_rest_apis()
            for item in response["items"]:
                constructed_url = f"{item['id']}.execute-api.{self.api_client.meta.region_name}.amazonaws.com"
                if constructed_url in self.domain:
                    self._domain_exists = True

        return self._domain_exists

    def dynamodb_table_exists(self, table_name):
        """Test that the DynamoDB table exists."""
        try:
            response = self.dynamodb.describe_table(TableName=table_name)
            return response["Table"]["TableStatus"] == "ACTIVE"
        except boto3.exceptions.botocore.exceptions.ClientError as e:
            if e.response["Error"]["Code"] == "ResourceNotFoundException":
                return False
            raise

    def api_exists(self, api_name: str):
        """Test that the API Gateway exists."""
        response = self.api_client.get_rest_apis()

        for item in response["items"]:
            if item["name"] == api_name:
                return True
        return False

    def get_api(self, api_name: str) -> json:
        """Test that the API Gateway exists."""
        response = self.api_client.get_rest_apis()

        for item in response["items"]:
            if item["name"] == api_name:
                return item
        return False

    def api_resource_and_method_exists(self, path, method):
        """Test that the API Gateway resource and method exists."""
        api = self.get_api(self.api_gateway_name)
        api_id = api["id"]
        resources = self.api_client.get_resources(restApiId=api_id)
        for resource in resources["items"]:
            if resource["path"] == path:
                try:
                    self.api_client.get_method(restApiId=api_id, resourceId=resource["id"], httpMethod=method)
                    return True
                except self.api_client.exceptions.NotFoundException:
                    return False

        return False

    def get_api_keys(self) -> str:
        """Test that the API Gateway exists."""
        response = self.api_client.get_api_keys(includeValues=True)
        for item in response["items"]:
            if item["name"] == self.shared_resource_identifier:
                return item["value"]
        return False


class TestAWSInfrastructure(TestAWSInfrastructureBase):
    """Test AWS infrastructure."""

    # -------------------------------------------------------------------------
    # Tests
    # -------------------------------------------------------------------------
    def test_aws_connection_works(self):
        """Test that the AWS connection works."""
        self.assertTrue(self.aws_connection_works(), "AWS connection failed.")

    def test_domain_exists(self):
        """Test that domain name exists in API Gateway."""
        self.assertTrue(self.domain_exists(), f"Domain {self.domain} does not exist.")

    def test_api_exists(self):
        """Test that the API Gateway exists."""
        api = self.get_api(self.api_gateway_name)
        self.assertIsInstance(api, dict, "API Gateway does not exist.")

    def test_api_resource_example_airportcodes_exists(self):
        """Test that the API Gateway examples/default-airport-codes end point exists."""
        self.assertTrue(
            self.api_resource_and_method_exists("/examples/default-airport-codes", "POST"),
            "API Gateway /examples/default-airport-codes (POST) resource does not exist.",
        )

    def test_api_key_exists(self):
        """Test that an API key exists."""
        api_key = self.get_api_keys()
        self.assertIsInstance(api_key, str, "API key does not exist.")
        self.assertGreaterEqual(len(api_key), 15, "API key is too short.")
