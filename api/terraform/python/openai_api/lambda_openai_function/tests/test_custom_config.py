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
from openai_api.lambda_openai_function.custom_config import (
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
        prompt = self.everlasting_gobbstopper["prompting"]["system_prompt"]
        system_prompt = SystemPrompt(system_prompt=prompt)

        self.assertEqual(
            system_prompt.system_prompt,
            "You are a helpful marketing agent for the [Willy Wonka Chocolate Factory](https://wwcf.com).\n",
        )
        self.assertIsInstance(system_prompt, SystemPrompt)
        self.assertIsInstance(system_prompt.system_prompt, str)

    def test_system_prompt_invalid(self):
        """Test system_prompt."""
        with self.assertRaises(ValueError):
            SystemPrompt(system_prompt=self.everlasting_gobbstopper_invalid["prompting"]["system_prompt_invalid"])

    def test_search_terms(self):
        """Test search_terms."""
        config_json = self.everlasting_gobbstopper["prompting"]["search_terms"]
        search_terms = SearchTerms(config_json=config_json)

        self.assertIsInstance(search_terms, SearchTerms)
        self.assertDictEqual(
            search_terms.to_json(),
            {
                "strings": ["Gobstopper", "Gobstoppers", "Gobbstopper", "Gobbstoppers"],
                "pairs": [["everlasting", "gobstopper"], ["everlasting", "gobstoppers"]],
            },
        )

    def test_search_terms_invalid(self):
        """Test search_terms."""
        config_json = self.everlasting_gobbstopper_invalid["prompting"]["search_terms"]
        with self.assertRaises(ValueError):
            SearchTerms(config_json=config_json)

    def test_additional_information(self):
        """Test additional_information."""
        config_json = self.everlasting_gobbstopper["function_calling"]["additional_information"]
        additional_information = AdditionalInformation(config_json=config_json)

        self.assertTrue(isinstance(additional_information, AdditionalInformation))
        self.assertTrue(isinstance(additional_information.config_json, dict))
        self.assertTrue(isinstance(additional_information.keys, list))
        self.assertListEqual(
            additional_information.keys, ["contact", "biographical", "sales_promotions", "coupon_codes"]
        )

    def test_additional_information_invalid(self):
        """Test additional_information."""
        config_json = self.everlasting_gobbstopper_invalid["function_calling"]["additional_information"]
        with self.assertRaises(ValueError):
            AdditionalInformation(config_json=config_json)

    def test_refers_to(self):
        """Test refers_to."""
        config_path = get_test_file_path("config/everlasting-gobbstopper.yaml")
        with open(config_path, "r", encoding="utf-8") as file:
            config_json = yaml.safe_load(file)

        refers_to = CustomConfig(config_json=config_json)

        self.assertEqual(refers_to.name, "EverlastingGobstopper")
        self.assertEqual(refers_to.index, 0)

        self.assertDictEqual(
            refers_to.prompting.search_terms.to_json(),
            {
                "strings": ["Gobstopper", "Gobstoppers", "Gobbstopper", "Gobbstoppers"],
                "pairs": [["everlasting", "gobstopper"], ["everlasting", "gobstoppers"]],
            },
        )
        self.assertEqual(
            refers_to.prompting.system_prompt.system_prompt,
            "You are a helpful marketing agent for the [Willy Wonka Chocolate Factory](https://wwcf.com).\n",
        )

        additional_information = refers_to.function_calling.additional_information
        self.assertTrue(isinstance(additional_information, AdditionalInformation))
        self.assertTrue(isinstance(additional_information.config_json, dict))
        self.assertTrue(isinstance(additional_information.keys, list))
        self.assertListEqual(
            additional_information.keys, ["contact", "biographical", "sales_promotions", "coupon_codes"]
        )
