# -*- coding: utf-8 -*-
# pylint: disable=wrong-import-position
# pylint: disable=R0801,E1101
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


from openai_api.lambda_openai_function.plugin_loader import Plugin

# pylint: disable=no-name-in-module
from openai_api.lambda_openai_function.plugin_manager import (
    function_calling_plugin,
    plugin_tool_factory,
)
from openai_api.lambda_openai_function.tests.test_setup import get_test_file_path


class TestLambdaOpenaiFunctionRefersTo(unittest.TestCase):
    """Test OpenAI Function Calling hook for refers_to."""

    def setUp(self):
        """Set up test fixtures."""
        config_path = get_test_file_path("plugins/everlasting-gobbstopper.yaml")
        with open(config_path, "r", encoding="utf-8") as file:
            plugin_json = yaml.safe_load(file)
        self.plugin = Plugin(plugin_json=plugin_json)

    # pylint: disable=broad-exception-caught
    def test_get_additional_info(self):
        """Test default return value of function_calling_plugin()"""
        try:
            # pylint: disable=no-value-for-parameter
            additional_information = function_calling_plugin(
                inquiry_type=self.plugin.function_calling.additional_information.keys[0]
            )
        except Exception:
            self.fail("function_calling_plugin() raised ExceptionType")

        self.assertTrue(additional_information is not None)

    def test_info_tool_factory(self):
        """Test integrity plugin_tool_factory()"""
        itf = plugin_tool_factory(plugin=self.plugin)
        self.assertIsInstance(itf, dict)

        self.assertIsInstance(itf, dict)
        self.assertTrue("type" in itf)
        self.assertTrue("function" in itf)
