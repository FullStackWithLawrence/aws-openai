# -*- coding: utf-8 -*-
"""
This module contains the CustomConfig class, which is used to parse YAML config files for
function_refers_to.get_additional_info().
"""
import json
import logging
import os
import re

import yaml
from openai_api.common.conf import settings
from openai_api.common.const import PYTHON_ROOT


log = logging.getLogger(__name__)
CONFIG_PATH = PYTHON_ROOT + "/openai_api/lambda_openai_function/config/"


class CustomConfigBase:
    """Base class for CustomConfig and CustomConfigs"""

    def __init__(self) -> None:
        pass

    def __repr__(self):
        return f"{self.__class__.__name__}({self.__dict__})"

    def __str__(self):
        return f"{self.__dict__}"

    def do_error(self, err: str) -> None:
        """Print the error message and raise a ValueError"""
        print(err)
        log.error(err)
        raise ValueError(err)


class SystemPrompt(CustomConfigBase):
    """System prompt of a CustomConfig object"""

    config: str = None

    def __init__(self, system_prompt=None):
        super().__init__()
        system_prompt = system_prompt or ""
        self.config = system_prompt
        self.validate()

    @property
    def is_valid(self) -> bool:
        """Return True if the config file is valid"""
        try:
            self.validate()
            return True
        except ValueError:
            return False

    def validate(self) -> None:
        """Validate the config file"""
        if not isinstance(self.system_prompt, str):
            self.do_error(f"Expected a string but received {type(self.system_prompt)}")

    @property
    def system_prompt(self) -> str:
        """Return the system prompt"""
        return self.config

    def __str__(self):
        return f"{self.config}"


class SearchTerms(CustomConfigBase):
    """Search terms of a CustomConfig object"""

    def __init__(self, search_terms: dict = None):
        super().__init__()
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

    @property
    def is_valid(self) -> bool:
        """Return True if the config file is valid"""
        try:
            self.validate()
            return True
        except ValueError:
            return False

    def validate(self) -> None:
        """Validate the config file"""
        required_keys = ["strings", "pairs"]
        if not self.config_json:
            self.do_error("search_terms is empty")

        for key in required_keys:
            if key not in self.config_json:
                self.do_error(f"Invalid search_terms: {self.config_json}. Missing key: {key}.")

        if not all(isinstance(item, str) for item in self.strings):
            self.do_error(f"Invalid config file: {self.config_json}. 'strings' should be a list of strings.")

        if not all(
            isinstance(pair, list) and len(pair) == 2 and all(isinstance(item, str) for item in pair)
            for pair in self.pairs
        ):
            self.do_error(f"Invalid config file: {self.config_json}. 'pairs' should be a list of pairs of strings.")

    def to_json(self) -> json:
        """Return the config file as a JSON object"""
        return self.config_json

    def __str__(self):
        """Return the config file as a string"""
        return f"{self.to_json()}"


class AdditionalInformation(CustomConfigBase):
    """Additional information of a CustomConfig object"""

    config_json: dict = None

    def __init__(self, additional_information: dict = None):
        super().__init__()
        self.config_json = additional_information
        self.validate()

    @property
    def keys(self) -> list:
        """Return a list of keys for additional information"""
        return list(self.config_json.keys())

    @property
    def is_valid(self) -> bool:
        """Return True if the config file is valid"""
        try:
            self.validate()
            return True
        except ValueError:
            return False

    def validate(self) -> None:
        """Validate the config file"""
        if not isinstance(self.config_json, dict):
            self.do_error(f"Expected a dict but received {type(self.config_json)}")

    def to_json(self) -> json:
        """Return the config file as a JSON object"""
        return self.config_json

    def __str__(self):
        """Return the config file as a string"""
        return f"{self.to_json()}"


class CustomConfig(CustomConfigBase):
    """Parse the YAML config file for a given Lambda function"""

    additional_information: str = None
    function_description: str = None
    search_terms: SearchTerms = None
    additional_information: AdditionalInformation = None
    system_prompt: SystemPrompt = None

    def __init__(self, config_path: str = None, config_json: dict = None, index: int = 0):
        super().__init__()
        self.config_path = config_path
        self.index = index
        if not config_path and not config_json:
            raise ValueError("Expected a config_path or config_json")
        if config_path and config_json:
            raise ValueError("Expected a config_path or config_json, not both")

        if config_path:
            if not self.file_name.endswith((".yaml", ".yml")):
                raise ValueError(f"Invalid file type: {self.file_name}. Expected a YAML file.")

            with open(self.config_path, "r", encoding="utf-8") as file:
                self.config_json = yaml.safe_load(file)

        if config_json:
            self.config_json = config_json

        self.validate()
        self.search_terms = SearchTerms(search_terms=self.config_json["search_terms"])
        self.system_prompt = SystemPrompt(system_prompt=self.config_json["system_prompt"])
        self.function_description = self.config_json["function_description"]
        self.additional_information = AdditionalInformation(
            additional_information=self.config_json["additional_information"]
        )

    @property
    def name(self) -> str:
        """Return a name in the format: "WillyWonka"""
        if self.parsed_filename:
            return self.parsed_filename.replace(" ", "")
        return None

    @property
    def file_name(self) -> str:
        """Return the name of the config file"""
        if self.config_path:
            return os.path.basename(self.config_path)
        return None

    @property
    def parsed_filename(self) -> str:
        """Return a name in the format: "Willy Wonka" """
        if self.file_name:
            name = os.path.splitext(self.file_name)[0]
            name = re.sub("-", " ", name)
            name = re.sub(r"(?<=[a-z])(?=[A-Z])", " ", name)
            name = name.title()
            name = "".join(name.split())
            return name
        return None

    @property
    def is_valid(self) -> bool:
        """Return True if the config file is valid"""
        try:
            self.validate()
        except ValueError:
            return False
        return self.additional_information.is_valid and self.search_terms.is_valid and self.system_prompt.is_valid

    def validate(self) -> None:
        """Validate the config file"""
        required_keys = ["search_terms", "system_prompt", "function_description", "additional_information"]
        if not self.config_json:
            self.do_error(f"Invalid config file: {self.config_path}")

        for key in required_keys:
            if key not in self.config_json:
                self.do_error(f"Invalid config file: {self.config_path}. Missing key: {key}.")

    def to_json(self) -> json:
        """Return the config file as a JSON object"""
        return {
            "name": self.name,
            "search_terms": self.search_terms.to_json(),
            "system_prompt": self.system_prompt.system_prompt,
            "function_description": self.function_description,
            "additional_information": self.additional_information.to_json(),
        }

    def __str__(self):
        return f"{self.to_json()}"


class CustomConfigs:
    """List of CustomConfig objects"""

    _custom_configs: list[CustomConfig] = None
    _aws_bucket_name: str = None
    _aws_bucket_path: str = "/aws_openai/lambda_openai_function/custom_configs/"
    _aws_bucket_path_validated: bool = False

    def __init__(self, config_path: str = None, aws_s3_bucket_name: str = None):
        i = 0
        self._custom_configs = []
        self._aws_bucket_name = aws_s3_bucket_name
        self.verify_bucket(bucket_name=aws_s3_bucket_name)

        # Load all the config files in this repo
        for filename in os.listdir(config_path):
            if filename.endswith((".yaml", ".yml")):
                i += 1
                full_config_path = os.path.join(config_path, filename)
                custom_config = CustomConfig(config_path=full_config_path, index=i)
                self._custom_configs.append(custom_config)

        # Load config files from the AWS S3 bucket
        if self.aws_bucket_path_validated:
            s3 = settings.aws_session.resource("s3")
            bucket = s3.Bucket(self._aws_bucket_name)

            for obj in bucket.objects.filter(Prefix=self._aws_bucket_path):
                i += 1
                file_content = obj.get()["Body"].read().decode("utf-8")
                config_json = yaml.safe_load(file_content)
                custom_config = CustomConfig(config_json=config_json, index=i)
                self._custom_configs.append(custom_config)

    def list_yaml_files(bucket_name):
        """List all the YAML files in the AWS S3 bucket"""
        s3 = settings.aws_session.resource("s3")
        bucket = s3.Bucket(bucket_name)

        for obj in bucket.objects.all():
            if obj.key.endswith(".yaml") or obj.key.endswith(".yml"):
                print("Found YAML file:", obj.key)

    @property
    def valid_configs(self) -> list[CustomConfig]:
        """Return a list of valid configs"""
        return [config for config in self._custom_configs if config.is_valid]

    @property
    def invalid_configs(self) -> list[CustomConfig]:
        """Return a list of invalid configs"""
        return [config for config in self._custom_configs if not config.is_valid]

    @property
    def aws_bucket_path_validated(self) -> bool:
        """Return True if the remote host is valid"""
        return self._aws_bucket_path_validated

    @property
    def aws_bucket_full_path(self) -> str:
        """Return the remote host"""
        if self.aws_bucket_path_validated:
            return self._aws_bucket_name + self._aws_bucket_path
        return None

    def verify_bucket(self, bucket_name: str):
        """Verify that the remote host is valid"""
        s3 = settings.aws_session.resource("s3")
        bucket = s3.Bucket(bucket_name)
        folder_path = self._aws_bucket_path
        try:
            # Check if bucket exists
            s3.meta.client.head_bucket(Bucket=bucket_name)
        # pylint: disable=broad-exception-caught
        except Exception:
            return

        try:
            # Create any missing folders
            if not any(s3_object.key.startswith(folder_path) for s3_object in bucket.objects.all()):
                s3.Object(bucket_name, folder_path).put()
            self._aws_bucket_path_validated = True
        # pylint: disable=broad-exception-caught
        except Exception:
            pass

    def to_json(self) -> json:
        """Return the _custom_configs list as a JSON object"""
        return self.valid_configs


class SingletonCustomConfigs:
    """Singleton for Settings"""

    _instance = None
    _custom_configs = None

    def __new__(cls):
        """Create a new instance of Settings"""
        if cls._instance is None:
            cls._instance = super(SingletonCustomConfigs, cls).__new__(cls)
            cls._instance._custom_configs = CustomConfigs(
                config_path=CONFIG_PATH, aws_s3_bucket_name=settings.aws_s3_bucket_name
            )
        return cls._instance

    @property
    def custom_configs(self) -> CustomConfigs:
        """Return the settings"""
        return self._custom_configs


config = SingletonCustomConfigs().custom_configs.valid_configs
