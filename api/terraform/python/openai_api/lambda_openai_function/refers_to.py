# -*- coding: utf-8 -*-
"""
This module contains the RefersTo class, which is used to parse the YAML config file for a given Lambda function.

search_terms:
  strings:
    - everlasting gobstopper
  pairs:
    - - everlasting
      - gobstopper
system_prompt: >
  You are a helpful marketing agent for the [Everlasting Gobstopper Company](https://everlasting-gobstoppers.com).
additional_information:
  contact:
    - name: Willy Wonka
    - title: Founder and CEO
  biographical: >
    Willy Wonka is a fictional character appearing ...
  sales_promotions:
    - name: Everlasting Gobstopper
      description: >
        The Everlasting Gobstopper is a candy that, according to Willy Wonka, "Never Gets Smaller Or Ever Gets Eaten". It is the main focus of Charlie and the Chocolate Factory, both the 1971 film and the 2005 film, and Willy Wonka and the Chocolate Factory, the 1971 film adaptation of the novel.
      price: $1.00
      image: https://upload.wikimedia.org/wikipedia/commons/thumb/6/6e/Everlasting_Gobstopper.jpg/220px-Everlasting_Gobstopper.jpg
  coupon_codes:
    - name: 10% off
      code: 10OFF
      description: >
        10% off your next purchase
"""
import json
import os
import re

import yaml
from openai_api.common.const import PYTHON_ROOT


CONFIG_PATH = PYTHON_ROOT + "/openai_api/lambda_openai_function/config/"


class SystemPrompt:
    """System prompt of a RefersTo object"""

    config: str = None

    def __init__(self, system_prompt=None):
        self.config = system_prompt
        self.validate()

    def validate(self) -> None:
        """Validate the config file"""
        if not isinstance(self.system_prompt, str):
            raise ValueError(f"Expected a string but received {type(self.config)}")

    @property
    def system_prompt(self) -> str:
        """Return the system prompt"""
        return self.config

    def __str__(self):
        return f"{self.config}"


class SearchTerms:
    """Search terms of a RefersTo object"""

    def __init__(self, search_terms: dict = None):
        self.config_json = search_terms
        self.validate()

    @property
    def strings(self) -> list:
        """Return a list of search terms"""
        return self.config_json["strings"]

    @property
    def pairs(self) -> list:
        """Return a list of search terms"""
        return self.config_json["pairs"]

    def validate(self) -> None:
        """Validate the config file"""
        required_keys = ["strings", "pairs"]
        if not self.config_json:
            raise ValueError("search_terms is empty")

        for key in required_keys:
            if key not in self.config_json:
                raise ValueError(f"Invalid search_terms: {self.config_json}. Missing key: {key}.")

        if not all(isinstance(item, str) for item in self.strings):
            raise ValueError(f"Invalid config file: {self.config_json}. 'strings' should be a list of strings.")

        if not all(
            isinstance(pair, list) and len(pair) == 2 and all(isinstance(item, str) for item in pair)
            for pair in self.pairs
        ):
            raise ValueError(f"Invalid config file: {self.config_json}. 'pairs' should be a list of pairs of strings.")

    def to_json(self) -> json:
        """Return the config file as a JSON object"""
        return self.config_json

    def __str__(self):
        """Return the config file as a string"""
        return f"{self.config_json}"


class AdditionalInformation:
    """Additional information of a RefersTo object"""

    config_json: dict = None

    def __init__(self, additional_information: dict = None):
        self.config_json = additional_information
        self.validate()

    @property
    def keys(self) -> list:
        """Return a list of keys for additional information"""
        return list(self.config_json.keys())

    def validate(self) -> None:
        """Validate the config file"""
        if not isinstance(self.config_json, dict):
            raise ValueError(f"Expected a dict but received {type(self.config_json)}")

    def to_json(self) -> json:
        """Return the config file as a JSON object"""
        return self.config_json

    def __str__(self):
        """Return the config file as a string"""
        return f"{self.config_json}"


class RefersTo:
    """Parse the YAML config file for a given Lambda function"""

    additional_information: str = None
    search_terms: SearchTerms = None
    additional_information: AdditionalInformation = None
    system_prompt: SystemPrompt = None

    def __init__(self, config_path: str, index: int = 0):
        self.config_path = config_path
        self.index = index

        if not self.file_name.endswith((".yaml", ".yml")):
            raise ValueError(f"Invalid file type: {self.file_name}. Expected a YAML file.")

        with open(self.config_path, "r", encoding="utf-8") as file:
            self.config_json = yaml.safe_load(file)

        self.validate()
        self.search_terms = SearchTerms(search_terms=self.config_json["search_terms"])
        self.system_prompt = SystemPrompt(system_prompt=self.config_json["system_prompt"])
        self.additional_information = AdditionalInformation(
            additional_information=self.config_json["additional_information"]
        )

    @property
    def name(self) -> str:
        """Return a name in the format: "WillyWonka"""
        return self.parsed_filename.replace(" ", "")

    @property
    def file_name(self) -> str:
        """Return the name of the config file"""
        return os.path.basename(self.config_path)

    @property
    def parsed_filename(self) -> str:
        """Return a name in the format: "Willy Wonka" """
        name = os.path.splitext(self.file_name)[0]
        name = re.sub("-", " ", name)
        name = re.sub(r"(?<=[a-z])(?=[A-Z])", " ", name)
        name = name.title()
        name = "".join(name.split())
        return name

    def validate(self) -> None:
        """Validate the config file"""
        required_keys = ["search_terms", "system_prompt", "additional_information"]
        if not self.config_json:
            raise ValueError(f"Invalid config file: {self.config_path}")

        for key in required_keys:
            if key not in self.config_json:
                raise ValueError(f"Invalid config file: {self.config_path}. Missing key: {key}.")

    def to_json(self) -> json:
        """Return the config file as a JSON object"""
        return {
            "name": self.name,
            "search_terms": self.search_terms.to_json(),
            "system_prompt": self.system_prompt.system_prompt,
            "additional_information": self.additional_information.to_json(),
        }

    def __str__(self):
        return f"{self.to_json()}"


def loader() -> list[RefersTo]:
    """Load all the config files"""
    i = 0
    retval = []
    for filename in os.listdir(CONFIG_PATH):
        if filename.endswith((".yaml", ".yml")):
            i += 1
            config_path = os.path.join(CONFIG_PATH, filename)
            refers_to = RefersTo(config_path=config_path, index=i)
            retval.append(refers_to)
    return retval


config: list[RefersTo] = loader()
