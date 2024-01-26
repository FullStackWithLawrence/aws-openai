# -*- coding: utf-8 -*-
# pylint: disable=wrong-import-position
"""Test configuration Settings class.

TODO: Add tests for: 480, 487, 531, 595, 602, 609, 612-617, 623, 626-631, 654, 662-664, 671-673, 686, 702, 710-712, 725, 740-741
"""

import os

# python stuff
import re
import sys
import unittest
from unittest.mock import patch

# 3rd party stuff
from dotenv import load_dotenv
from pydantic_core import ValidationError as PydanticValidationError


PYTHON_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
sys.path.append(PYTHON_ROOT)  # noqa: E402

from openai_api.common.conf import (  # noqa: E402
    Services,
    Settings,
    SettingsDefaults,
    empty_str_to_bool_default,
    empty_str_to_int_default,
    get_semantic_version,
)

# our stuff
from openai_api.common.exceptions import OpenAIAPIConfigurationError


# pylint: disable=too-many-public-methods
class TestConfiguration(unittest.TestCase):
    """Test configuration."""

    # Get the directory of the current script
    here = os.path.dirname(os.path.abspath(__file__))

    def setUp(self):
        # Save current environment variables
        self.saved_env = dict(os.environ)

    def tearDown(self):
        # Restore environment variables
        os.environ.clear()
        os.environ.update(self.saved_env)

    def env_path(self, filename):
        """Return the path to the .env file."""
        return os.path.join(self.here, filename)

    def test_conf_defaults(self):
        """Test that settings == SettingsDefaults when no .env is in use."""
        os.environ.clear()
        mock_settings = Settings(init_info="test_conf_defaults()")

        self.assertEqual(mock_settings.aws_region, SettingsDefaults.AWS_REGION)
        self.assertEqual(mock_settings.openai_endpoint_image_n, SettingsDefaults.OPENAI_ENDPOINT_IMAGE_N)
        self.assertEqual(mock_settings.openai_endpoint_image_size, SettingsDefaults.OPENAI_ENDPOINT_IMAGE_SIZE)

        self.assertEqual(mock_settings.debug_mode, SettingsDefaults.DEBUG_MODE)
        self.assertEqual(mock_settings.langchain_memory_key, SettingsDefaults.LANGCHAIN_MEMORY_KEY)
        self.assertEqual(mock_settings.openai_endpoint_image_n, SettingsDefaults.OPENAI_ENDPOINT_IMAGE_N)
        self.assertEqual(mock_settings.openai_endpoint_image_size, SettingsDefaults.OPENAI_ENDPOINT_IMAGE_SIZE)
        # pylint: disable=no-member
        self.assertEqual(
            mock_settings.openai_api_key.get_secret_value(), SettingsDefaults.OPENAI_API_KEY.get_secret_value()
        )
        self.assertEqual(mock_settings.openai_api_organization, SettingsDefaults.OPENAI_API_ORGANIZATION)
        # pylint: disable=no-member
        self.assertEqual(
            mock_settings.pinecone_api_key.get_secret_value(), SettingsDefaults.PINECONE_API_KEY.get_secret_value()
        )

    def test_conf_defaults_secrets(self):
        """Test that settings == SettingsDefaults when no .env is in use."""
        os.environ.clear()
        mock_settings = Settings(init_info="test_conf_defaults_secrets()")

        # pylint: disable=no-member
        self.assertEqual(mock_settings.openai_api_key.get_secret_value(), None)
        self.assertEqual(mock_settings.openai_api_organization, None)
        # pylint: disable=no-member
        self.assertEqual(mock_settings.pinecone_api_key.get_secret_value(), None)

    def test_env_legal_nulls(self):
        """Test that settings handles missing .env values."""
        os.environ.clear()
        env_path = self.env_path(".env.test_legal_nulls")
        loaded = load_dotenv(env_path)
        self.assertTrue(loaded)

        mock_settings = Settings(init_info="test_env_legal_nulls()")

        self.assertEqual(mock_settings.aws_region, SettingsDefaults.AWS_REGION)
        self.assertEqual(mock_settings.langchain_memory_key, SettingsDefaults.LANGCHAIN_MEMORY_KEY)
        self.assertEqual(mock_settings.openai_endpoint_image_n, SettingsDefaults.OPENAI_ENDPOINT_IMAGE_N)
        self.assertEqual(mock_settings.openai_endpoint_image_size, SettingsDefaults.OPENAI_ENDPOINT_IMAGE_SIZE)

    def test_env_illegal_nulls(self):
        """Test that settings handles missing .env values."""
        os.environ.clear()
        env_path = self.env_path(".env.test_illegal_nulls")
        loaded = load_dotenv(env_path)
        self.assertTrue(loaded)

        with self.assertRaises(PydanticValidationError):
            Settings(init_info="test_env_illegal_nulls()")

    def test_env_overrides(self):
        """Test that settings takes custom .env values."""
        os.environ.clear()
        env_path = self.env_path(".env.test_01")
        loaded = load_dotenv(env_path)
        self.assertTrue(loaded)

        mock_settings = Settings(init_info="test_env_overrides()")

        self.assertEqual(mock_settings.aws_region, "us-west-1")
        self.assertEqual(mock_settings.debug_mode, True)
        self.assertEqual(mock_settings.langchain_memory_key, "TEST_langchain_memory_key")
        self.assertEqual(mock_settings.openai_endpoint_image_n, 100)
        self.assertEqual(mock_settings.openai_endpoint_image_size, "TEST_image_size")

    @patch.dict(os.environ, {"AWS_REGION": "invalid-region"})
    def test_invalid_aws_region_code(self):
        """Test that Pydantic raises a validation error for environment variable with non-existent aws region code."""

        with self.assertRaises(Exception):
            Settings(init_info="test_invalid_aws_region_code()")

    def test_configure_with_class_constructor(self):
        """test that we can set values with the class constructor"""

        mock_settings = Settings(
            aws_region="eu-west-1", debug_mode=True, init_info="test_configure_with_class_constructor()"
        )

        self.assertEqual(mock_settings.aws_region, "eu-west-1")
        self.assertEqual(mock_settings.debug_mode, True)

    def test_configure_neg_int_with_class_constructor(self):
        """test that we cannot set negative int values with the class constructor"""

        with self.assertRaises(PydanticValidationError):
            Settings(face_detect_max_faces_count=-1)

        with self.assertRaises(PydanticValidationError):
            Settings(face_detect_threshold=-1)

    def test_readonly_settings(self):
        """test that we can't set readonly values with the class constructor"""

        mock_settings = Settings(aws_region="eu-west-1")
        with self.assertRaises(PydanticValidationError):
            mock_settings.aws_region = "us-west-1"

        with self.assertRaises(PydanticValidationError):
            mock_settings.table_id = "TEST_facialrecognition"

        with self.assertRaises(PydanticValidationError):
            mock_settings.collection_id = "TEST_facialrecognition-collection"

        with self.assertRaises(PydanticValidationError):
            mock_settings.face_detect_attributes = "TEST_DEFAULT"

        with self.assertRaises(PydanticValidationError):
            mock_settings.face_detect_quality_filter = "TEST_AUTO"

        with self.assertRaises(PydanticValidationError):
            mock_settings.debug_mode = True

        with self.assertRaises(PydanticValidationError):
            mock_settings.face_detect_max_faces_count = 25

        with self.assertRaises(PydanticValidationError):
            mock_settings.face_detect_threshold = 25

    def test_dump(self):
        """Test that dump is a dict."""

        mock_settings = Settings(init_info="test_dump()")
        self.assertIsInstance(mock_settings.dump, dict)

    def test_dump_keys(self):
        """Test that dump contains the expected keys."""

        mock_settings = Settings(init_info="test_dump_keys()")
        environment = mock_settings.dump["environment"]
        self.assertIn("DEBUG_MODE".lower(), environment)
        self.assertIn("os", environment)
        self.assertIn("system", environment)
        self.assertIn("release", environment)
        self.assertIn("boto3", environment)
        self.assertIn("SHARED_RESOURCE_IDENTIFIER".lower(), environment)
        self.assertIn("version", environment)

        aws_apigateway = mock_settings.dump["aws_apigateway"]
        self.assertIn("AWS_APIGATEWAY_ROOT_DOMAIN".lower(), aws_apigateway)

        openai_api = mock_settings.dump["openai_api"]
        self.assertIn("LANGCHAIN_MEMORY_KEY".lower(), openai_api)
        self.assertIn("OPENAI_ENDPOINT_IMAGE_N".lower(), openai_api)
        self.assertIn("OPENAI_ENDPOINT_IMAGE_SIZE".lower(), openai_api)

    def test_cloudwatch_values(self):
        """Test that dump contains the expected default values."""

        mock_settings = Settings(init_info="test_cloudwatch_values()")
        environment = mock_settings.dump["environment"]
        # aws_apigateway = mock_settings.dump["aws_apigateway"]
        openai_api = mock_settings.dump["openai_api"]

        self.assertEqual(environment["DEBUG_MODE".lower()], mock_settings.debug_mode)
        self.assertEqual(openai_api["LANGCHAIN_MEMORY_KEY".lower()], mock_settings.langchain_memory_key)
        self.assertEqual(openai_api["OPENAI_ENDPOINT_IMAGE_N".lower()], mock_settings.openai_endpoint_image_n)
        self.assertEqual(openai_api["OPENAI_ENDPOINT_IMAGE_SIZE".lower()], mock_settings.openai_endpoint_image_size)

    def test_initialize_with_values(self):
        """test that we can set values with the class constructor"""
        mock_settings = Settings(
            debug_mode=False,
            dump_defaults=False,
            aws_profile="test-profile",
            aws_region="eu-west-1",
            aws_apigateway_create_custom_domaim=False,
            aws_apigateway_root_domain="test-domain.com",
            langchain_memory_key="TEST_langchain_memory_key",
            openai_api_organization="TEST_openai_api_organization",
            openai_api_key="TEST_openai_api_key",
            openai_endpoint_image_n=100,
            openai_endpoint_image_size="TEST_image_size",
            pinecone_api_key="TEST_pinecone_api_key",
            shared_resource_identifier="TEST_shared_resource_identifier",
            init_info="test_initialize_with_values()",
        )
        self.assertEqual(mock_settings.debug_mode, False)
        self.assertEqual(mock_settings.dump_defaults, False)
        self.assertEqual(mock_settings.aws_profile, "test-profile")
        self.assertEqual(mock_settings.aws_region, "eu-west-1")
        self.assertEqual(mock_settings.aws_apigateway_create_custom_domaim, False)
        self.assertEqual(mock_settings.aws_apigateway_root_domain, "test-domain.com")
        self.assertEqual(mock_settings.langchain_memory_key, "TEST_langchain_memory_key")
        self.assertEqual(mock_settings.openai_api_organization, "TEST_openai_api_organization")
        # pylint: disable=no-member
        self.assertEqual(mock_settings.openai_api_key.get_secret_value(), "TEST_openai_api_key")
        self.assertEqual(mock_settings.openai_endpoint_image_n, 100)
        self.assertEqual(mock_settings.openai_endpoint_image_size, "TEST_image_size")
        # pylint: disable=no-member
        self.assertEqual(mock_settings.pinecone_api_key.get_secret_value(), "TEST_pinecone_api_key")
        self.assertEqual(mock_settings.shared_resource_identifier, "TEST_shared_resource_identifier")

    def test_semantic_version(self):
        """Test that the semantic version conforms to a valid pattern."""
        version = get_semantic_version()
        self.assertIsNotNone(version)
        pattern = r"^\d+\.\d+\.\d+$"
        match = re.match(pattern, version)
        self.assertIsNotNone(match, f"{version} is not a valid semantic version")

    def test_services(self):
        """Test that the services are valid."""
        services = Services()
        self.assertIsNotNone(services)
        self.assertTrue(services.enabled(services.AWS_CLI))
        with self.assertRaises(OpenAIAPIConfigurationError):
            services.raise_error_on_disabled(services.AWS_RDS)
        self.assertIsInstance(services.to_dict(), dict)
        self.assertIn(services.AWS_CLI[0], services.enabled_services())

    def test_empty_str_to_bool_default(self):
        """Test that empty strings are converted to bool defaults."""
        self.assertFalse(empty_str_to_bool_default("", False))
        self.assertTrue(empty_str_to_bool_default("true", True))

    def test_empty_str_to_int_default(self):
        """Test that empty strings are converted to int defaults."""
        self.assertEqual(empty_str_to_int_default("", 0), 0)
        self.assertEqual(empty_str_to_int_default("1", 1), 1)

    def test_settings_aws_account_id(self):
        """Test that the AWS account ID is valid."""
        mock_settings = Settings(init_info="test_settings_aws_account_id()")
        self.assertIsNotNone(mock_settings.aws_account_id)
        self.assertTrue(mock_settings.aws_account_id.isdigit())

    def test_settings_aws_session(self):
        """Test that the AWS session is valid."""
        mock_settings = Settings(init_info="test_settings_aws_session()")
        self.assertIsNotNone(mock_settings.aws_session)
        self.assertIsNotNone(mock_settings.aws_session.region_name)
        self.assertIsNotNone(mock_settings.aws_session.profile_name)

    def test_settings_dynamodb(self):
        """Test that the DynamoDB table is valid."""
        mock_settings = Settings(init_info="test_settings_dynamodb()")
        # pylint: disable=pointless-statement
        with self.assertRaises(OpenAIAPIConfigurationError):
            mock_settings.aws_dynamodb_client

    def test_settings_aws_s3_bucket_name(self):
        """Test that the S3 bucket name is valid."""
        mock_settings = Settings(init_info="test_settings_aws_s3_bucket_name()")
        if mock_settings.aws_apigateway_create_custom_domaim:
            self.assertIsNotNone(mock_settings.aws_s3_bucket_name)

    def test_settings_aws_apigateway_domain_name(self):
        """Test that the API Gateway domain name is valid."""
        mock_settings = Settings(init_info="test_settings_aws_apigateway_domain_name()")
        hostname = mock_settings.aws_apigateway_domain_name
        self.assertIsNotNone(mock_settings.aws_apigateway_domain_name)
        # pylint: disable=anomalous-backslash-in-string
        assert re.match(
            "^(([a-zA-Z0-9]|[a-zA-Z0-9][a-zA-Z0-9\-]*[a-zA-Z0-9])\.)*([A-Za-z0-9]|[A-Za-z0-9][A-Za-z0-9\-]*[A-Za-z0-9])$",
            hostname,
        ), "Invalid hostname"
