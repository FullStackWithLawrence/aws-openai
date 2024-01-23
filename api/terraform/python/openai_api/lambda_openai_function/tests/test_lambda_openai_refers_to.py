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
from openai_api.lambda_openai_function.function_refers_to import (
    get_additional_info,
    get_client_list,
    info_tool_factory,
)

# our stuff
from openai_api.lambda_openai_function.tests.test_setup import (  # noqa: E402
    get_test_file,
)


class TestLambdaOpenaiFunctionRefersTo(unittest.TestCase):
    """Test OpenAI Function Calling hook for refers_to."""

    lambda_config: dict = None
    client_list: list = None

    def setUp(self):
        """Set up test fixtures."""
        self.client_list = get_client_list()
        with open(PYTHON_ROOT + "/openai_api/lambda_openai_function/lambda_config.yaml", "r", encoding="utf-8") as file:
            self.lambda_config = yaml.safe_load(file)

    # pylint: disable=broad-exception-caught
    def test_get_additional_info(self):
        """Test default return value of get_additional_info()"""
        try:
            # pylint: disable=no-value-for-parameter
            retval = get_additional_info()
        except Exception:
            self.fail("get_additional_info() raised ExceptionType")

        self.assertIsInstance(retval, str)
        try:
            d = json.loads(retval)

        except Exception:
            self.fail("get_additional_info() returned invalid JSON")

        self.assertTrue("search_terms" in d)
        self.assertTrue("search_pairs" in d)
        self.assertTrue("system_prompt" in d)
        self.assertTrue("clients" in d)
        self.assertTrue("contact_information" in d)
        self.assertTrue("biographical_info" in d)
        self.assertTrue("marketing_info" in d)
        self.assertTrue("profile" in d)

    def test_info_tool_factory(self):
        """Test integrity info_tool_factory()"""
        itf = info_tool_factory()
        self.assertIsInstance(itf, list)

        d = itf[0]
        self.assertIsInstance(d, dict)
        self.assertTrue("type" in d)
        self.assertTrue("function" in d)
