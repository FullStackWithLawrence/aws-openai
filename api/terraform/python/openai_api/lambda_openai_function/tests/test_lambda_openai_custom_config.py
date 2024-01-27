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


from openai_api.lambda_openai_function.custom_config import CustomConfig

# pylint: disable=no-name-in-module
from openai_api.lambda_openai_function.function_refers_to import (
    get_additional_info,
    info_tool_factory,
)
from openai_api.lambda_openai_function.tests.test_setup import get_test_file_path


class TestLambdaOpenaiFunctionRefersTo(unittest.TestCase):
    """Test OpenAI Function Calling hook for refers_to."""

    def setUp(self):
        """Set up test fixtures."""
        config_path = get_test_file_path("config/everlasting-gobbstopper.yaml")
        with open(config_path, "r", encoding="utf-8") as file:
            config_json = yaml.safe_load(file)
        self.config = CustomConfig(config_json=config_json)

    # pylint: disable=broad-exception-caught
    def test_get_additional_info(self):
        """Test default return value of get_additional_info()"""
        try:
            # pylint: disable=no-value-for-parameter
            additional_information = get_additional_info(
                inquiry_type=self.config.function_calling.additional_information.keys[0]
            )
        except Exception:
            self.fail("get_additional_info() raised ExceptionType")

        self.assertTrue(additional_information is not None)

    def test_info_tool_factory(self):
        """Test integrity info_tool_factory()"""
        itf = info_tool_factory(config=self.config)
        self.assertIsInstance(itf, dict)

        self.assertIsInstance(itf, dict)
        self.assertTrue("type" in itf)
        self.assertTrue("function" in itf)
