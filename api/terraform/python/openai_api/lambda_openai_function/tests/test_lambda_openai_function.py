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


from openai_api.common.utils import does_refer_to
from openai_api.lambda_openai_function.lambda_handler import (  # noqa: E402
    handler,
    its_about_me,
)

# our stuff
from openai_api.lambda_openai_function.tests.test_setup import (  # noqa: E402
    get_test_file,
)


class TestLambdaOpenai(unittest.TestCase):
    """Test Index Lambda function."""

    # load a mock lambda_index event
    event_about_lawrence = get_test_file("json/prompt_about_lawrence.json")

    def setUp(self):
        """Set up test fixtures."""

    def test_does_refer_to_easy(self):
        """Test does_refer_to."""
        self.assertTrue(does_refer_to("lawrence", "lawrence"))
        self.assertTrue(does_refer_to("Lawrence McDaniel", "lawrence"))
        self.assertTrue(does_refer_to("Who is Lawrence McDaniel?", "Lawrence McDaniel"))

    def test_does_refer_to_harder(self):
        """Test does_refer_to."""
        self.assertTrue(does_refer_to("Is it true that larry mcdaniel has a YouTube channel?", "larry mcdaniel"))
        self.assertTrue(does_refer_to("Is it true that Lawrence P. McDaniel has a YouTube channel?", "mcdaniel"))
        self.assertTrue(does_refer_to("Is it true that Lawrence P. McDaniel has a YouTube channel?", "lawrence"))
        self.assertTrue(does_refer_to("Is it true that Larry McDaniel has a YouTube channel?", "larry McDaniel"))

    def test_its_about_me(self):
        """Test its_about_me()."""

        def list_factory(content: str) -> list:
            return [
                {"role": "system", "content": "You are a helpful chatbot."},
                {"role": "user", "content": "what is web development?"},
                {"role": "system", "content": "blah blah answer answer."},
                {"role": "user", "content": content},
            ]

        # false cases
        self.assertFalse(its_about_me(list_factory("how is leisure suit larry?")))
        self.assertFalse(its_about_me(list_factory("do full stack developers earn a lot of money?")))
        self.assertFalse(its_about_me(list_factory("who is John Kennedy?")))
        self.assertFalse(its_about_me(list_factory("Hello world!")))
        self.assertFalse(its_about_me(list_factory("test test test")))
        self.assertFalse(its_about_me(list_factory("what is the airport code the airport in Dallas, Texas?")))

        # true cases
        self.assertTrue(its_about_me(list_factory("who is lawrence mcdaniel?")))
        self.assertTrue(its_about_me(list_factory("is FullStackWithLawrence a youtube channel?")))
        self.assertTrue(its_about_me(list_factory("have you ever seen the youtube channel full stack with lawrence?")))
        self.assertTrue(its_about_me(list_factory("Is it true that larry mcdaniel has a YouTube channel?")))
        self.assertTrue(its_about_me(list_factory("Is it true that Lawrence McDaniel has a YouTube channel?")))
        self.assertTrue(its_about_me(list_factory("Is it true that Lawrence P. McDaniel has a YouTube channel?")))
        self.assertTrue(its_about_me(list_factory("Is it true that Larry McDaniel has a YouTube channel?")))

    # def test_lambda_handler(self):
    #     """Test lambda_handler."""
    #     response = handler(self.event_about_lawrence, None)

    #     self.assertEqual(response["statusCode"], 200)
    #     self.assertTrue("body" in response)
    #     self.assertTrue("isBase64Encoded" in response)
    #     body = response["body"]
    #     self.assertTrue("id" in body)
    #     self.assertTrue("object" in body)
    #     self.assertTrue("created" in body)
    #     self.assertTrue("model" in body)
    #     self.assertTrue("choices" in body)
    #     self.assertTrue("completion" in body)
    #     self.assertTrue("request_meta_data" in body)
    #     self.assertTrue("usage" in body)
