# -*- coding: utf-8 -*-
# pylint: disable=wrong-import-position
"""Test configuration Settings class."""

# python stuff
import os
import sys
import unittest
from unittest.mock import patch

# 3rd party stuff
from dotenv import load_dotenv
from pydantic_core import ValidationError as PydanticValidationError


PYTHON_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
sys.path.append(PYTHON_ROOT)  # noqa: E402

# our stuff
from openai_api.common.conf import Settings, SettingsDefaults  # noqa: E402
from openai_api.common.exceptions import OpenAIAPIValueError  # noqa: E402


class TestConfiguration(unittest.TestCase):
    """Test configuration."""

    # Get the directory of the current script
    here = os.path.dirname(os.path.abspath(__file__))

    def setUp(self):
        """Set up test fixtures."""

    def env_path(self, filename):
        """Return the path to the .env file."""
        return os.path.join(self.here, filename)

    def test_conf_defaults(self):
        """Test that settings == SettingsDefaults when no .env is in use."""
        os.environ.clear()
        mock_settings = Settings()

        self.assertEqual(mock_settings.aws_region, SettingsDefaults.AWS_REGION)
        self.assertEqual(mock_settings.aws_dynamodb_table_id, SettingsDefaults.AWS_DYNAMODB_TABLE_ID)

        self.assertEqual(mock_settings.openai_endpoint_image_n, SettingsDefaults.OPENAI_ENDPOINT_IMAGE_N)
        self.assertEqual(mock_settings.openai_endpoint_image_size, SettingsDefaults.OPENAI_ENDPOINT_IMAGE_SIZE)

        self.assertEqual(mock_settings.aws_rekognition_collection_id, SettingsDefaults.AWS_REKOGNITION_COLLECTION_ID)
        self.assertEqual(
            mock_settings.aws_rekognition_face_detect_max_faces_count,
            SettingsDefaults.AWS_REKOGNITION_FACE_DETECT_MAX_FACES_COUNT,
        )
        self.assertEqual(
            mock_settings.aws_rekognition_face_detect_attributes,
            SettingsDefaults.AWS_REKOGNITION_FACE_DETECT_ATTRIBUTES,
        )
        self.assertEqual(
            mock_settings.aws_rekognition_face_detect_quality_filter,
            SettingsDefaults.AWS_REKOGNITION_FACE_DETECT_QUALITY_FILTER,
        )
        self.assertEqual(
            mock_settings.aws_rekognition_face_detect_threshold, SettingsDefaults.AWS_REKOGNITION_FACE_DETECT_THRESHOLD
        )

    def test_conf_defaults_secrets(self):
        """Test that settings == SettingsDefaults when no .env is in use."""
        os.environ.clear()
        mock_settings = Settings()

        self.assertEqual(mock_settings.openai_api_key, None)
        self.assertEqual(mock_settings.openai_api_organization, None)
        self.assertEqual(mock_settings.pinecone_api_key, None)

    def test_env_nulls(self):
        """Test that settings handles missing .env values."""
        os.environ.clear()
        env_path = self.env_path(".env.test_nulls")
        loaded = load_dotenv(env_path)
        self.assertTrue(loaded)

        mock_settings = Settings()

        self.assertEqual(mock_settings.aws_region, SettingsDefaults.AWS_REGION)
        self.assertEqual(mock_settings.aws_dynamodb_table_id, SettingsDefaults.AWS_DYNAMODB_TABLE_ID)
        self.assertEqual(mock_settings.aws_rekognition_collection_id, SettingsDefaults.AWS_REKOGNITION_COLLECTION_ID)
        self.assertEqual(
            mock_settings.aws_rekognition_face_detect_max_faces_count,
            SettingsDefaults.AWS_REKOGNITION_FACE_DETECT_MAX_FACES_COUNT,
        )
        self.assertEqual(
            mock_settings.aws_rekognition_face_detect_attributes,
            SettingsDefaults.AWS_REKOGNITION_FACE_DETECT_ATTRIBUTES,
        )
        self.assertEqual(
            mock_settings.aws_rekognition_face_detect_quality_filter,
            SettingsDefaults.AWS_REKOGNITION_FACE_DETECT_QUALITY_FILTER,
        )
        self.assertEqual(
            mock_settings.aws_rekognition_face_detect_threshold, SettingsDefaults.AWS_REKOGNITION_FACE_DETECT_THRESHOLD
        )

    def test_env_overrides(self):
        """Test that settings takes custom .env values."""
        os.environ.clear()
        env_path = self.env_path(".env.test_01")
        loaded = load_dotenv(env_path)
        self.assertTrue(loaded)

        mock_settings = Settings()

        self.assertEqual(mock_settings.aws_region, "us-west-1")
        self.assertEqual(mock_settings.aws_dynamodb_table_id, "TEST_facialrecognition")
        self.assertEqual(mock_settings.aws_rekognition_collection_id, "TEST_facialrecognition-collection")
        self.assertEqual(mock_settings.aws_rekognition_face_detect_max_faces_count, 100)
        self.assertEqual(mock_settings.aws_rekognition_face_detect_attributes, "TEST_DEFAULT")
        self.assertEqual(mock_settings.aws_rekognition_face_detect_quality_filter, "TEST_AUTO")
        self.assertEqual(mock_settings.aws_rekognition_face_detect_threshold, 100)
        self.assertEqual(mock_settings.debug_mode, True)

    @patch.dict(os.environ, {"AWS_REGION": "invalid-region"})
    def test_invalid_aws_region_code(self):
        """Test that Pydantic raises a validation error for environment variable with non-existent aws region code."""

        with self.assertRaises(OpenAIAPIValueError):
            Settings()

    @patch.dict(os.environ, {"AWS_REKOGNITION_FACE_DETECT_MAX_FACES_COUNT": "-1"})
    def test_invalid_max_faces_count(self):
        """Test that Pydantic raises a validation error for environment variable w negative integer values."""

        with self.assertRaises(PydanticValidationError):
            Settings()

    @patch.dict(os.environ, {"AWS_REKOGNITION_FACE_DETECT_THRESHOLD": "-1"})
    def test_invalid_threshold(self):
        """Test that Pydantic raises a validation error for environment variable w negative integer values."""

        with self.assertRaises(PydanticValidationError):
            Settings()

    def test_configure_with_class_constructor(self):
        """test that we can set values with the class constructor"""

        mock_settings = Settings(
            aws_region="eu-west-1",
            aws_dynamodb_table_id="TEST_facialrecognition",
            aws_rekognition_collection_id="TEST_facialrecognition-collection",
            aws_rekognition_face_detect_max_faces_count=101,
            aws_rekognition_face_detect_attributes="TEST_DEFAULT",
            aws_rekognition_face_detect_quality_filter="TEST_AUTO",
            aws_rekognition_face_detect_threshold=102,
            debug_mode=True,
        )

        self.assertEqual(mock_settings.aws_region, "eu-west-1")
        self.assertEqual(mock_settings.aws_dynamodb_table_id, "TEST_facialrecognition")
        self.assertEqual(mock_settings.aws_rekognition_collection_id, "TEST_facialrecognition-collection")
        self.assertEqual(mock_settings.aws_rekognition_face_detect_max_faces_count, 101)
        self.assertEqual(mock_settings.aws_rekognition_face_detect_attributes, "TEST_DEFAULT")
        self.assertEqual(mock_settings.aws_rekognition_face_detect_quality_filter, "TEST_AUTO")
        self.assertEqual(mock_settings.aws_rekognition_face_detect_threshold, 102)
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

    def test_cloudwatch_dump(self):
        """Test that cloudwatch_dump is a dict."""

        mock_settings = Settings()
        self.assertIsInstance(mock_settings.cloudwatch_dump, dict)

    def test_cloudwatch_dump_keys(self):
        """Test that cloudwatch_dump contains the expected keys."""

        environment = Settings().cloudwatch_dump["environment"]
        self.assertIn("openai_api_version", environment)
        self.assertIn("os", environment)
        self.assertIn("system", environment)
        self.assertIn("release", environment)
        self.assertIn("boto3", environment)
        self.assertIn("AWS_REKOGNITION_COLLECTION_ID", environment)
        self.assertIn("AWS_DYNAMODB_TABLE_ID", environment)
        self.assertIn("AWS_REKOGNITION_FACE_DETECT_MAX_FACES_COUNT", environment)
        self.assertIn("AWS_REKOGNITION_FACE_DETECT_ATTRIBUTES", environment)
        self.assertIn("AWS_REKOGNITION_QUALITY_FILTER", environment)
        self.assertIn("DEBUG_MODE", environment)

    def test_cloudwatch_values(self):
        """Test that cloudwatch_dump contains the expected values."""

        mock_settings = Settings()
        environment = mock_settings.cloudwatch_dump["environment"]

        self.assertEqual(environment["AWS_REKOGNITION_COLLECTION_ID"], mock_settings.aws_rekognition_collection_id)
        self.assertEqual(environment["AWS_DYNAMODB_TABLE_ID"], mock_settings.aws_dynamodb_table_id)
        # self.assertEqual(environment["MAX_FACES"], mock_settings.aws_rekognition_face_detect_max_faces_count)
        self.assertEqual(
            environment["AWS_REKOGNITION_FACE_DETECT_ATTRIBUTES"], mock_settings.aws_rekognition_face_detect_attributes
        )
        # self.assertEqual(environment["QUALITY_FILTER"], mock_settings.)
        self.assertEqual(environment["DEBUG_MODE"], mock_settings.debug_mode)
