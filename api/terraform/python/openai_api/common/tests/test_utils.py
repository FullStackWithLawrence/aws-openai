# -*- coding: utf-8 -*-
# pylint: disable=wrong-import-position
"""Test configuration Settings class."""

# python stuff
import json
import os
import sys
import unittest
from pathlib import Path


HERE = os.path.abspath(os.path.dirname(__file__))
PROJECT_ROOT = str(Path(HERE).parent.parent)
PYTHON_ROOT = str(Path(PROJECT_ROOT).parent)
if PYTHON_ROOT not in sys.path:
    sys.path.append(PYTHON_ROOT)  # noqa: E402

from openai_api.common.const import OpenAIMessageKeys  # noqa: E402

# our stuff
from openai_api.common.tests.test_setup import get_test_file  # noqa: E402
from openai_api.common.utils import (  # noqa: E402
    exception_response_factory,
    get_content_for_role,
    get_message_history,
    get_messages_for_role,
    get_request_body,
    http_response_factory,
    parse_request,
)


class TestUtils(unittest.TestCase):
    """Test utils."""

    # Get the directory of the current script
    here = HERE
    request = get_test_file("json/passthrough_openai_v2_request.json")
    response = get_test_file("json/passthrough_openai_v2_response.json")

    def setUp(self):
        """Set up test fixtures."""

    def test_http_response_factory(self):
        """Test test_http_response_factory."""
        retval = http_response_factory(200, self.response)
        self.assertEqual(retval["statusCode"], 200)
        self.assertEqual(retval["body"], json.dumps(self.response))
        self.assertEqual(retval["isBase64Encoded"], False)
        self.assertEqual(retval["headers"]["Content-Type"], "application/json")

    def test_exception_response_factory(self):
        """Test exception_response_factory."""
        try:
            raise AssertionError("test")
        except AssertionError as exception:
            retval = exception_response_factory(exception)
            self.assertIn("error", retval)
            self.assertIn("description", retval)

    def test_get_request_body(self):
        """Test get_request_body"""
        request_body = get_request_body(self.request)
        self.assertEqual(request_body, self.request)
        self.assertEqual(request_body["model"], "gpt-4-turbo")
        self.assertEqual(request_body["object_type"], "chat.completion")
        self.assertIn("temperature", request_body)
        self.assertIn("max_tokens", request_body)
        self.assertIn("messages", request_body)

    def test_parse_request(self):
        """Test parse_request"""
        request_body = get_request_body(self.request)
        object_type, model, messages, input_text, temperature, max_tokens = parse_request(request_body)
        self.assertEqual(object_type, "chat.completion")
        self.assertEqual(model, "gpt-4-turbo")
        self.assertEqual(input_text, None)
        self.assertEqual(temperature, 0)
        self.assertEqual(max_tokens, 256)
        self.assertEqual(len(messages), 2)

    def test_get_content_for_role(self):
        """Test get_content_for_role"""
        request_body = get_request_body(self.request)
        _, _, messages, _, _, _ = parse_request(request_body)
        system_message = get_content_for_role(messages, OpenAIMessageKeys.OPENAI_SYSTEM_MESSAGE_KEY)
        user_message = get_content_for_role(messages, OpenAIMessageKeys.OPENAI_USER_MESSAGE_KEY)
        self.assertEqual(system_message, "you always return the integer value 42.")
        self.assertEqual(user_message, "return the integer value 42.")

    def test_get_message_history(self):
        """test get_message_history"""
        request_body = get_request_body(self.request)
        _, _, messages, _, _, _ = parse_request(request_body)
        message_history = get_message_history(messages)
        self.assertIsInstance(message_history, list)
        self.assertEqual(len(message_history), 1)
        self.assertEqual(message_history[0]["role"], "user")
        self.assertEqual(message_history[0]["content"], "return the integer value 42.")

    def test_get_messages_for_role(self):
        """test get_messages_for_role"""
        request_body = get_request_body(self.request)
        _, _, messages, _, _, _ = parse_request(request_body)
        message_history = get_message_history(messages)
        self.assertIsInstance(message_history, list)
        user_messages = get_messages_for_role(message_history, OpenAIMessageKeys.OPENAI_USER_MESSAGE_KEY)
        self.assertEqual(len(user_messages), 1)
        self.assertEqual(user_messages[0], "return the integer value 42.")
