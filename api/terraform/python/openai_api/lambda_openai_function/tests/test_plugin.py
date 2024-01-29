# -*- coding: utf-8 -*-
# pylint: disable=wrong-import-position
# pylint: disable=R0801,E1101
"""Test lambda_openai_v2 function."""

# python stuff
import os
import sys
import unittest
from pathlib import Path

import yaml
from botocore.exceptions import ClientError


HERE = os.path.abspath(os.path.dirname(__file__))
PROJECT_ROOT = str(Path(HERE).parent.parent)
PYTHON_ROOT = str(Path(PROJECT_ROOT).parent)
if PYTHON_ROOT not in sys.path:
    sys.path.append(PYTHON_ROOT)  # noqa: E402


from openai_api.common.conf import settings

# pylint: disable=no-name-in-module
from openai_api.lambda_openai_function.plugin_loader import (
    AdditionalInformation,
    FunctionCalling,
    Plugin,
    Prompting,
    SearchTerms,
    Selector,
    validate_required_keys,
)
from openai_api.lambda_openai_function.tests.test_setup import (  # noqa: E402
    get_test_file_path,
    get_test_file_yaml,
)


class TestLambdaOpenaiFunctionRefersTo(unittest.TestCase):
    """Test OpenAI Function Calling hook for refers_to."""

    def setUp(self):
        """Set up test fixtures."""
        self.everlasting_gobbstopper = get_test_file_yaml("plugins/everlasting-gobbstopper.yaml")
        self.everlasting_gobbstopper_invalid = get_test_file_yaml("plugins/everlasting-gobbstopper-invalid.yaml")

    def test_validate_required_keys(self):
        """Test validate_required_keys."""
        required_keys = ["meta_data", "prompting", "function_calling"]
        validate_required_keys(
            class_name="Plugin", plugin_json=self.everlasting_gobbstopper, required_keys=required_keys
        )

        with self.assertRaises(ValueError):
            required_keys = ["meta_data", "prompting", "some_other_key"]
            validate_required_keys(
                class_name="Plugin", plugin_json=self.everlasting_gobbstopper_invalid, required_keys=required_keys
            )

    def test_search_terms(self):
        """Test search_terms."""
        plugin_json = self.everlasting_gobbstopper["selector"]["search_terms"]
        search_terms = SearchTerms(plugin_json=plugin_json)

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
        plugin_json = self.everlasting_gobbstopper_invalid["selector"]["search_terms"]
        with self.assertRaises(ValueError):
            SearchTerms(plugin_json=plugin_json)

    def test_additional_information(self):
        """Test additional_information."""
        plugin_json = self.everlasting_gobbstopper["function_calling"]["additional_information"]
        print("test_additional_information type plugin_json: ", type(plugin_json))
        additional_information = AdditionalInformation(plugin_json=plugin_json)
        print(
            "test_additional_information type additional_information.plugin_json: ",
            type(additional_information.plugin_json),
        )

        self.assertTrue(isinstance(additional_information, AdditionalInformation))
        self.assertTrue(isinstance(additional_information.plugin_json, dict))
        self.assertTrue(isinstance(additional_information.keys, list))
        self.assertListEqual(
            additional_information.keys, ["contact", "biographical", "sales_promotions", "coupon_codes"]
        )

    def test_additional_information_invalid(self):
        """Test additional_information."""
        plugin_json = self.everlasting_gobbstopper_invalid["function_calling"]["additional_information"]
        with self.assertRaises(ValueError):
            AdditionalInformation(plugin_json=plugin_json)

    def test_refers_to(self):
        """Test refers_to."""
        config_path = get_test_file_path("plugins/everlasting-gobbstopper.yaml")
        with open(config_path, "r", encoding="utf-8") as file:
            plugin_json = yaml.safe_load(file)

        refers_to = Plugin(plugin_json=plugin_json)

        self.assertEqual(refers_to.name, "EverlastingGobstopper")
        self.assertEqual(refers_to.index, 0)

        self.assertDictEqual(
            refers_to.selector.search_terms.to_json(),
            {
                "strings": ["Gobstopper", "Gobstoppers", "Gobbstopper", "Gobbstoppers"],
                "pairs": [["everlasting", "gobstopper"], ["everlasting", "gobstoppers"]],
            },
        )
        self.assertEqual(
            refers_to.prompting.system_prompt,
            "You are a helpful marketing agent for the [Willy Wonka Chocolate Factory](https://wwcf.com).\n",
        )

        additional_information = refers_to.function_calling.additional_information
        self.assertTrue(isinstance(additional_information, AdditionalInformation))
        self.assertTrue(isinstance(additional_information.plugin_json, dict))
        self.assertTrue(isinstance(additional_information.keys, list))
        self.assertListEqual(
            additional_information.keys, ["contact", "biographical", "sales_promotions", "coupon_codes"]
        )

    def test_prompting(self):
        """Test prompting."""
        plugin = Plugin(plugin_json=self.everlasting_gobbstopper)
        prompting_config_json = plugin.prompting.to_json()
        Prompting(plugin_json=prompting_config_json)

        with self.assertRaises(ValueError):
            Prompting(plugin_json={})

    def test_selector(self):
        """Test selector."""
        plugin = Plugin(plugin_json=self.everlasting_gobbstopper)
        selector_config_json = plugin.selector.to_json()
        Selector(plugin_json=selector_config_json)

        with self.assertRaises(ValueError):
            Selector(plugin_json={})

    def test_function_calling(self):
        """Test function_calling."""
        plugin = Plugin(plugin_json=self.everlasting_gobbstopper)
        function_calling_config_json = plugin.function_calling.to_json()
        FunctionCalling(plugin_json=function_calling_config_json)

        with self.assertRaises(ValueError):
            FunctionCalling(plugin_json={})

    def test_aws_s3_bucket(self):
        """Test aws_s3_bucket."""

        # If the aws_s3_bucket_name is example.com, then we don't need to test it.
        if settings.aws_apigateway_root_domain == "example.com":
            return

        aws_s3_bucket_name = settings.aws_s3_bucket_name
        s3 = settings.aws_s3_client

        folder_name = "test_folder/"
        file_name = folder_name + "test_file"

        print("Testing aws_s3_bucket_name: ", aws_s3_bucket_name)
        # Connect to the aws_s3_bucket_name
        try:
            s3.head_bucket(Bucket=aws_s3_bucket_name)
        except ClientError:
            self.fail("Couldn't connect to the aws_s3_bucket_name.")

        # Create a folder
        s3.put_object(Bucket=aws_s3_bucket_name, Key=folder_name)

        # Write a file to the folder
        s3.put_object(Bucket=aws_s3_bucket_name, Key=file_name, Body=b"Test data")

        # Delete the file and the folder
        s3.delete_objects(Bucket=aws_s3_bucket_name, Delete={"Objects": [{"Key": file_name}, {"Key": folder_name}]})
