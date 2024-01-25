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

from openai_api.common.const import OpenAIEndPoint, OpenAIObjectTypes

# our stuff
from openai_api.common.exceptions import OpenAIAPIValueError
from openai_api.common.tests.test_setup import get_test_file  # noqa: E402
from openai_api.common.validators import (
    validate_completion_request,
    validate_embedding_request,
    validate_endpoint,
    validate_item,
    validate_max_tokens,
    validate_messages,
    validate_object_types,
    validate_request_body,
    validate_temperature,
)


class TestValidators(unittest.TestCase):
    """Test validators."""

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

    def test_validate_item(self):
        """Test validate_item."""
        valid_items = ["item1", "item2", "item3"]
        item = "item1"
        # verify that no exception is raised
        validate_item(item, valid_items, "valid_items")

        item = "i_cause_an_exception"
        with self.assertRaises(OpenAIAPIValueError):
            validate_item(item, valid_items, "valid_items")

    def test_validate_temperature(self):
        """Test validate_temperature."""
        temperature = 0.5
        # verify that no exception is raised
        validate_temperature(temperature)

        temperature = 1.5
        with self.assertRaises(OpenAIAPIValueError):
            validate_temperature(temperature)

        temperature = -1.5
        with self.assertRaises(OpenAIAPIValueError):
            validate_temperature(temperature)

        temperature = "not_a_float"
        try:
            validate_temperature(temperature)
        except ValueError:
            pass
        else:
            self.fail("ValueError not raised")

    def test_validate_max_tokens(self):
        """Test validate_max_tokens."""
        max_tokens = 100
        # verify that no exception is raised
        validate_max_tokens(max_tokens)

        max_tokens = 0
        with self.assertRaises(OpenAIAPIValueError):
            validate_max_tokens(max_tokens)

        max_tokens = 2049
        with self.assertRaises(OpenAIAPIValueError):
            validate_max_tokens(max_tokens)

        max_tokens = "not_an_int"
        with self.assertRaises(TypeError):
            validate_max_tokens(max_tokens)

    def test_validate_endpoint(self):
        """Test validate_endpoint."""
        end_point = OpenAIEndPoint.ChatCompletion
        # verify that no exception is raised
        validate_endpoint(end_point)

        end_point = "https://www.google.com/"
        with self.assertRaises(OpenAIAPIValueError):
            validate_endpoint(end_point)

    def test_validate_object_types(self):
        """Test validate_object_types."""
        object_type = OpenAIObjectTypes.ChatCompletion
        # verify that no exception is raised
        validate_object_types(object_type)

        object_type = "not_a_valid_object_type"
        with self.assertRaises(OpenAIAPIValueError):
            validate_object_types(object_type)

    def test_validate_request_body(self):
        """Test validate_request_body."""
        request_body = {"key1": "value1", "key2": "value2"}
        # verify that no exception is raised
        validate_request_body(request_body)

        request_body = "not_a_dict"
        with self.assertRaises(TypeError):
            validate_request_body(request_body)

    def test_validate_messages(self):
        """Test validate_messages."""
        messages_good = get_test_file("json/messages_good.json")
        messages_bad_role = get_test_file("json/messages_bad_role.json")

        # verify that no exception is raised
        request_body = messages_good
        validate_messages(request_body)

        request_body = messages_bad_role
        with self.assertRaises(OpenAIAPIValueError):
            validate_messages(request_body)

    def test_validate_completion_request(self):
        """Test validate_completion_request."""
        request_body = get_test_file("json/passthrough_openai_v2_request.json")
        # verify that no exception is raised
        validate_completion_request(request_body)

        request_body = {"prompt": "This is a test", "max_tokens": 100, "temperature": 0.5, "stop": "not_a_list"}
        with self.assertRaises(OpenAIAPIValueError):
            validate_completion_request(request_body)
