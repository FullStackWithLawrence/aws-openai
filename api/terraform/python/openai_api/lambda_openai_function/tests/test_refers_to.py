# -*- coding: utf-8 -*-
# pylint: disable=wrong-import-position
# pylint: disable=R0801
"""Test lambda_openai_v2 function."""

# python stuff
import json
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


# pylint: disable=no-name-in-module
from openai_api.lambda_openai_function.refers_to import (
    AdditionalInformation,
    CustomConfig,
    SearchTerms,
    SystemPrompt,
)

# our stuff
from openai_api.lambda_openai_function.tests.test_setup import (  # noqa: E402
    get_test_file_path,
    get_test_file_yaml,
)


class TestLambdaOpenaiFunctionRefersTo(unittest.TestCase):
    """Test OpenAI Function Calling hook for refers_to."""

    def setUp(self):
        """Set up test fixtures."""
        self.everlasting_gobbstopper = get_test_file_yaml("config/everlasting-gobbstopper.yaml")
        self.everlasting_gobbstopper_invalid = get_test_file_yaml("config/everlasting-gobbstopper-invalid.yaml")

    def test_system_prompt(self):
        """Test system_prompt."""
        system_prompt = SystemPrompt(system_prompt=self.everlasting_gobbstopper["system_prompt"])

        self.assertEqual(
            system_prompt.system_prompt,
            "You are a helpful marketing agent for the [Everlasting Gobstopper Company](https://everlasting-gobstoppers.com).\n",
        )
        self.assertIsInstance(system_prompt, SystemPrompt)
        self.assertIsInstance(system_prompt.system_prompt, str)

    def test_system_prompt_invalid(self):
        """Test system_prompt."""
        with self.assertRaises(ValueError):
            SystemPrompt(system_prompt=self.everlasting_gobbstopper_invalid["system_prompt_invalid"])

    def test_search_terms(self):
        """Test search_terms."""
        search_terms = SearchTerms(search_terms=self.everlasting_gobbstopper["search_terms"])

        self.assertIsInstance(search_terms, SearchTerms)
        self.assertDictEqual(
            search_terms.to_json(),
            {
                "strings": ["everlasting gobstopper", "everlasting gobstoppers", "everlasting gobstopper's"],
                "pairs": [["everlasting", "gobstopper"], ["everlasting", "gobstoppers"]],
            },
        )

    def test_search_terms_invalid(self):
        """Test search_terms."""
        with self.assertRaises(ValueError):
            SearchTerms(search_terms=self.everlasting_gobbstopper_invalid["search_terms"])

    def test_additional_information(self):
        """Test additional_information."""
        additional_information = AdditionalInformation(
            additional_information=self.everlasting_gobbstopper["additional_information"]
        )

        self.assertTrue(isinstance(additional_information, AdditionalInformation))
        self.assertTrue(isinstance(additional_information.config_json, dict))
        self.assertTrue(isinstance(additional_information.keys, list))
        self.assertListEqual(
            additional_information.keys, ["contact", "biographical", "sales_promotions", "coupon_codes"]
        )

    def test_additional_information_invalid(self):
        """Test additional_information."""
        with self.assertRaises(ValueError):
            AdditionalInformation(
                additional_information=self.everlasting_gobbstopper_invalid["additional_information_invalid"]
            )

    def test_refers_to(self):
        """Test refers_to."""
        refers_to = CustomConfig(config_path=get_test_file_path("config/everlasting-gobbstopper.yaml"))

        self.assertEqual(refers_to.name, "EverlastingGobbstopper")
        self.assertEqual(refers_to.file_name, "everlasting-gobbstopper.yaml")
        self.assertEqual(refers_to.parsed_filename, "EverlastingGobbstopper")
        self.assertEqual(refers_to.index, 0)
        self.assertDictEqual(
            refers_to.search_terms.to_json(),
            {
                "strings": ["everlasting gobstopper", "everlasting gobstoppers", "everlasting gobstopper's"],
                "pairs": [["everlasting", "gobstopper"], ["everlasting", "gobstoppers"]],
            },
        )
        self.assertEqual(
            refers_to.system_prompt.system_prompt,
            "You are a helpful marketing agent for the [Everlasting Gobstopper Company](https://everlasting-gobstoppers.com).\n",
        )

        additional_information = refers_to.additional_information
        self.assertTrue(isinstance(additional_information, AdditionalInformation))
        self.assertTrue(isinstance(additional_information.config_json, dict))
        self.assertTrue(isinstance(additional_information.keys, list))
        self.assertListEqual(
            additional_information.keys, ["contact", "biographical", "sales_promotions", "coupon_codes"]
        )
