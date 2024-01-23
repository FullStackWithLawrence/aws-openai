# -*- coding: utf-8 -*-
# pylint: disable=wrong-import-position
# pylint: disable=R0801
"""Test lambda_openai_v2 function."""

# python stuff
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


from openai_api.lambda_openai_function.lambda_handler import (  # noqa: E402; handler,
    search_terms_are_in_messages,
)
from openai_api.lambda_openai_function.natural_language_processing import does_refer_to

# our stuff
from openai_api.lambda_openai_function.tests.test_setup import (  # noqa: E402
    get_test_file,
)


class TestLambdaOpenai(unittest.TestCase):
    """Test Index Lambda function."""

    # load a mock lambda_index event
    event_about_lawrence = get_test_file("json/prompt_about_lawrence.json")
    SEARCH_TERMS = []
    SEARCH_PAIRS = []

    def setUp(self):
        """Set up test fixtures."""
        with open(PYTHON_ROOT + "/openai_api/lambda_openai_function/lambda_config.yaml", "r", encoding="utf-8") as file:
            lambda_config = yaml.safe_load(file)
        self.SEARCH_TERMS = lambda_config["search_terms"]
        self.SEARCH_PAIRS = lambda_config["search_pairs"]

    def test_does_not_refer_to(self):
        """Test simple false outcomes for does_refer_to."""
        self.assertFalse(does_refer_to("larry", "lawrence"))
        self.assertFalse(does_refer_to("dev", "developer"))

    def test_does_refer_to_camel_case(self):
        """Test does_refer_to works correctly with camel case."""
        self.assertTrue(does_refer_to("FullStackWithLawrence", "Full Stack With Lawrence"))

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

    def test_search_terms_are_in_messages(self):
        """Test search_terms_are_in_messages()."""

        def list_factory(content: str) -> list:
            return [
                {"role": "system", "content": "You are a helpful chatbot."},
                {"role": "user", "content": "what is web development?"},
                {"role": "system", "content": "blah blah answer answer."},
                {"role": "user", "content": content},
            ]

        def false_assertion(content: str):
            self.assertFalse(
                search_terms_are_in_messages(
                    messages=list_factory(content),
                    search_terms=self.SEARCH_TERMS,
                    search_pairs=self.SEARCH_PAIRS,
                )
            )
            print("False - content:", content)

        def true_assertion(content: str):
            self.assertTrue(
                search_terms_are_in_messages(
                    messages=list_factory(content),
                    search_terms=self.SEARCH_TERMS,
                    search_pairs=self.SEARCH_PAIRS,
                )
            )
            print("True - content:", content)

        # false cases
        false_assertion("when was leisure suit larry released?")
        false_assertion("is larry carlton a good guitarist?")
        false_assertion("do full stack developers earn a lot of money?")
        false_assertion("who is John Kennedy?")
        false_assertion("Hello world!")
        false_assertion("test test test")
        false_assertion("what is the airport code the airport in Dallas, Texas?")

        # true cases
        true_assertion("who is lawrence mcdaniel?")
        true_assertion("is FullStackWithLawrence a youtube channel?")
        true_assertion("have you ever seen the youtube channel full stack with lawrence?")
        true_assertion("Is it true that larry mcdaniel has a YouTube channel?")
        true_assertion("Is it true that Lawrence McDaniel has a YouTube channel?")
        true_assertion("Is it true that Lawrence P. McDaniel has a YouTube channel?")
        true_assertion("Is it true that Larry McDaniel has a YouTube channel?")

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
