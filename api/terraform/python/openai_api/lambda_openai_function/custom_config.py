# -*- coding: utf-8 -*-
"""
This module contains the CustomConfig class, which is used to parse YAML config objects for
function_refers_to.get_additional_info().
"""
import json
import logging
import os

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
        err = f"{self.__class__.__name__} - {err}"
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
        """Return True if the config object is valid"""
        try:
            self.validate()
            return True
        except ValueError:
            return False

    def validate(self) -> None:
        """Validate the config object"""
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

    def __init__(self, config_json: dict = None):
        super().__init__()
        self.config_json = config_json
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
        """Return True if the config object is valid"""
        try:
            self.validate()
            return True
        except ValueError:
            return False

    def validate(self) -> None:
        """Validate the config object"""
        if not isinstance(self.config_json, dict):
            self.do_error(f"Expected a dict but received {type(self.config_json)}")

        required_keys = ["strings", "pairs"]
        for key in required_keys:
            if key not in self.config_json:
                self.do_error(f"Invalid search_terms: {self.config_json}. Missing key: {key}.")

        if not all(isinstance(item, str) for item in self.strings):
            self.do_error(f"Invalid config object: {self.config_json}. 'strings' should be a list of strings.")

        if not all(
            isinstance(pair, list) and len(pair) == 2 and all(isinstance(item, str) for item in pair)
            for pair in self.pairs
        ):
            self.do_error(f"Invalid config object: {self.config_json}. 'pairs' should be a list of pairs of strings.")

    def to_json(self) -> json:
        """Return the config as a JSON object"""
        return self.config_json

    def __str__(self):
        """Return the config object as a string"""
        return f"{self.to_json()}"


class AdditionalInformation(CustomConfigBase):
    """Additional information of a CustomConfig object"""

    config_json: dict = None

    def __init__(self, config_json: dict = None):
        super().__init__()
        self.config_json = config_json
        self.validate()

    @property
    def keys(self) -> list:
        """Return a list of keys for additional information"""
        return list(self.config_json.keys())

    @property
    def is_valid(self) -> bool:
        """Return True if the config object is valid"""
        try:
            self.validate()
            return True
        except ValueError:
            return False

    def validate(self) -> None:
        """Validate the config object"""
        if not isinstance(self.config_json, dict):
            self.do_error(f"Expected a dict but received {type(self.config_json)}")

    def to_json(self) -> json:
        """Return the config as a JSON object"""
        return self.config_json

    def __str__(self):
        """Return the config object as a string"""
        return f"{self.to_json()}"


class Prompting(CustomConfigBase):
    """Prompting child class of a CustomConfig object"""

    config_json: dict = None
    search_terms: SearchTerms = None
    system_prompt: SystemPrompt = None

    def __init__(self, config_json: dict = None):
        super().__init__()
        self.config_json = config_json
        self.validate()
        self.search_terms = SearchTerms(config_json=self.config_json["search_terms"])
        self.system_prompt = SystemPrompt(system_prompt=self.config_json["system_prompt"])

    @property
    def is_valid(self) -> bool:
        """Return True if the config object is valid"""
        try:
            self.validate()
        except ValueError:
            return False
        return True

    def validate(self):
        """Validate the config object"""
        if not isinstance(self.config_json, dict):
            self.do_error(f"Expected a dict but received {type(self.config_json)}")
        required_keys = ["search_terms", "system_prompt"]
        for key in required_keys:
            if key not in self.config_json:
                self.do_error(f"Invalid config object: {self.config_json}. Missing key: {key}.")

    def to_json(self) -> json:
        """Return the config as a JSON object"""
        return {
            "search_terms": self.search_terms.to_json(),
            "system_prompt": self.system_prompt.system_prompt,
        }


class FunctionCalling(CustomConfigBase):
    """FunctionCalling child class of a CustomConfig"""

    config_json: dict = None
    function_description: str = None
    additional_information: AdditionalInformation = None

    def __init__(self, config_json: dict = None):
        super().__init__()

        self.config_json = config_json
        self.validate()
        self.function_description = self.config_json["function_description"]
        self.additional_information = AdditionalInformation(config_json=self.config_json["additional_information"])

    @property
    def is_valid(self) -> bool:
        """Return True if the config object is valid"""
        try:
            self.validate()
        except ValueError:
            return False
        return True

    def validate(self):
        """Validate the config object"""
        if not isinstance(self.config_json, dict):
            self.do_error(f"Expected a dict but received {type(self.config_json)}")
        required_keys = ["function_description", "additional_information"]
        for key in required_keys:
            if key not in self.config_json:
                self.do_error(f"Invalid config object: {self.config_json}. Missing key: {key}.")
        if not isinstance(self.config_json["function_description"], str):
            self.do_error(f"Invalid config object: {self.config_json}. 'function_description' should be a string.")
        if not isinstance(self.config_json["additional_information"], dict):
            self.do_error(f"Invalid config object: {self.config_json}. 'additional_information' should be a dict.")

    def to_json(self) -> json:
        """Return the config as a JSON object"""
        return {
            "function_description": self.function_description,
            "additional_information": self.additional_information.to_json(),
        }


class MetaData(CustomConfigBase):
    """Metadata of a CustomConfig object"""

    config_json: dict = None

    def __init__(self, config_json: dict = None):
        super().__init__()
        self.config_json = config_json
        self.validate()

    @property
    def is_valid(self) -> bool:
        """Return True if the config object is valid"""
        try:
            self.validate()
            return True
        except ValueError:
            return False

    @property
    def name(self) -> str:
        """Return the name of the config object"""
        return self.config_json["name"]

    @property
    def config_path(self) -> str:
        """Return the path of the config object"""
        return self.config_json["config_path"]

    @property
    def description(self) -> str:
        """Return the description of the config object"""
        return self.config_json["description"]

    @property
    def version(self) -> str:
        """Return the version of the config object"""
        return self.config_json["version"]

    @property
    def author(self) -> str:
        """Return the author of the config object"""
        return self.config_json["author"]

    def validate(self) -> None:
        """Validate the config object"""
        if not isinstance(self.config_json, dict):
            self.do_error(f"Expected a dict but received {type(self.config_json)}")

        required_keys = ["config_path", "name", "description", "version", "author"]
        for key in required_keys:
            if key not in self.config_json:
                self.do_error(f"Invalid config object: {self.config_path}. Missing key: {key}.")

    def to_json(self) -> json:
        """Return the config as a JSON object"""
        return self.config_json

    def __str__(self):
        """Return the config object as a string"""
        return f"{self.to_json()}"


class CustomConfig(CustomConfigBase):
    """Parse the YAML config object for a given Lambda function"""

    config_json: dict = None
    meta_data: MetaData = None
    prompting: Prompting = None
    function_calling: FunctionCalling = None

    def __init__(self, config_json: dict = None, index: int = 0):
        super().__init__()
        self.index = index
        self.config_json = config_json
        self.validate()
        self.meta_data = MetaData(config_json=self.config_json["meta_data"])
        self.prompting = Prompting(config_json=self.config_json["prompting"])
        self.function_calling = FunctionCalling(config_json=self.config_json["function_calling"])

    @property
    def name(self) -> str:
        """Return a name in the format: "WillyWonka"""
        return self.meta_data.name

    @property
    def is_valid(self) -> bool:
        """Return True if the config object is valid"""
        try:
            self.validate()
            return True
        except ValueError:
            pass
        return False

    def validate(self) -> None:
        """Validate the config object"""

        if not isinstance(self.config_json, dict):
            self.do_error(f"Expected a dict but received {type(self.config_json)}")

        required_keys = ["meta_data", "prompting", "function_calling"]
        for key in required_keys:
            if key not in self.config_json:
                self.do_error(f"Invalid config object: {self.config_json}. Missing key: {key}.")
            if not isinstance(self.config_json[key], dict):
                self.do_error(
                    f"Expected a dict for {key} but received {type(self.config_json[key])}: {self.config_json[key]}"
                )

    def to_json(self) -> json:
        """Return the config as a JSON object"""
        return {
            "name": self.name,
            "meta_data": self.meta_data.to_json(),
            "prompting": self.prompting.to_json(),
            "function_calling": self.function_calling.to_json(),
        }

    def __str__(self):
        return f"{self.to_json()}"


class CustomConfigs:
    """List of CustomConfig objects"""

    _custom_configs: list[CustomConfig] = None
    _aws_bucket_name: str = None
    _aws_bucket_path: str = "aws_openai/lambda_openai_function/custom_configs/"
    _aws_bucket_path_validated: bool = False

    def __init__(self, config_path: str = None, aws_s3_bucket_name: str = None):
        i = 0
        self._custom_configs = []
        self._aws_bucket_name = aws_s3_bucket_name
        self.verify_bucket(bucket_name=aws_s3_bucket_name)

        # Load all the config objects in this repo
        for filename in os.listdir(config_path):
            if filename.endswith((".yaml", ".yml")):
                i += 1
                full_config_path = os.path.join(config_path, filename)
                with open(full_config_path, "r", encoding="utf-8") as file:
                    config_json = yaml.safe_load(file)

                custom_config = CustomConfig(config_json=config_json, index=i)
                self._custom_configs.append(custom_config)

        # Load config objects from the AWS S3 bucket
        if self.aws_bucket_path_validated:
            s3 = settings.aws_session.resource("s3")
            bucket = s3.Bucket(self._aws_bucket_name)

            for obj in bucket.objects.filter(Prefix=self.aws_bucket_path):
                if obj.key.endswith(".yaml") or obj.key.endswith(".yml"):
                    i += 1
                    file_content = obj.get()["Body"].read().decode("utf-8")
                    config_json = yaml.safe_load(file_content)
                    if config_json:
                        custom_config = CustomConfig(config_json=config_json, index=i)
                        self._custom_configs.append(custom_config)
                        print(
                            f"Loaded custom configuration from AWS S3 bucket: {custom_config.name} {custom_config.meta_data.version} created by {custom_config.meta_data.author}"
                        )

    @property
    def valid_configs(self) -> list[CustomConfig]:
        """Return a list of valid configs"""
        return [config for config in self._custom_configs if config.is_valid]

    @property
    def invalid_configs(self) -> list[CustomConfig]:
        """Return a list of invalid configs"""
        return [config for config in self._custom_configs if not config.is_valid]

    @property
    def aws_bucket_path(self) -> str:
        """Return the remote host"""
        return self._aws_bucket_path

    @property
    def aws_bucket_path_validated(self) -> bool:
        """Return True if the remote host is valid"""
        return self._aws_bucket_path_validated

    def verify_bucket(self, bucket_name: str):
        """Verify that the remote host is valid"""
        if not bucket_name:
            return

        s3 = settings.aws_session.resource("s3")
        try:
            # Check if bucket exists
            s3.meta.client.head_bucket(Bucket=bucket_name)
        # pylint: disable=broad-exception-caught
        except Exception as e:
            log.warning("Bucket %s does not exist: %s", bucket_name, e)
            return

        # Create any missing folders
        bucket = s3.Bucket(bucket_name)
        if not any(s3_object.key.startswith(self.aws_bucket_path) for s3_object in bucket.objects.all()):
            print(f"Creating folder {self.aws_bucket_path} in bucket {bucket_name}")
            s3.Object(bucket_name, self.aws_bucket_path).put()
        self._aws_bucket_path_validated = True

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


_custom_configs = SingletonCustomConfigs().custom_configs
config = _custom_configs.valid_configs
if len(_custom_configs.invalid_configs) > 0:
    invalid_configurations = [config.name for config in _custom_configs.invalid_configs]
    log.error("Invalid custom config objects: %s", invalid_configurations)
