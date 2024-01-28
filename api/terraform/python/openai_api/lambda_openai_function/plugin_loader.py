# -*- coding: utf-8 -*-
# pylint: disable=E1101
"""
This module contains the Plugin class, which is used to parse YAML config objects for
plugin.function_calling_plugin().
"""
import json
import logging
import os
from typing import Optional

import yaml
from openai_api.common.conf import settings
from openai_api.common.const import PYTHON_ROOT
from pydantic import BaseModel, Field, ValidationError, field_validator, root_validator


log = logging.getLogger(__name__)
CONFIG_PATH = PYTHON_ROOT + "/openai_api/lambda_openai_function/config/"


def do_error(class_name: str, err: str) -> None:
    """Print the error message and raise a ValueError"""
    err = f"{class_name} - {err}"
    print(err)
    log.error(err)
    raise ValueError(err)


def validate_required_keys(class_name: str, required_keys: list, config_json: dict) -> None:
    """Validate the required keys"""
    for key in required_keys:
        if key not in config_json:
            do_error(class_name, err=f"Invalid search_terms: {config_json}. Missing key: {key}.")


class PluginBase(BaseModel):
    """Base class for Plugin and Plugins"""

    class Config:
        """Pydantic config"""

        extra = "forbid"  # this will forbid any extra attributes during model initialization

    def __repr__(self):
        return f"{self.__class__.__name__}({self.__dict__})"

    def __str__(self):
        return f"{self.to_json()}"

    def to_json(self) -> json:
        """Return the config as a JSON object"""
        raise NotImplementedError


class SystemPrompt(PluginBase):
    """System prompt of a Plugin object"""

    system_prompt: str = Field(..., description="System prompt")

    @field_validator("system_prompt")
    @classmethod
    def validate_system_prompt(cls, system_prompt) -> str:
        """Validate the system_prompt field"""
        if not isinstance(system_prompt, str):
            do_error(class_name=cls.__name__, err=f"Expected a string but received {type(system_prompt)}")
        return system_prompt

    def to_json(self) -> json:
        """Return the config as a JSON object"""
        return self.system_prompt


class SearchTerms(PluginBase):
    """Search terms of a Plugin object"""

    config_json: dict = Field(..., description="Config object")

    @field_validator("config_json")
    @classmethod
    def validate_config_json(cls, config_json) -> dict:
        """Validate the config_json object"""
        if not isinstance(config_json, dict):
            do_error(class_name=cls.__name__, err=f"Expected a dict but received {type(config_json)}")

        required_keys = ["strings", "pairs"]
        validate_required_keys(class_name=cls.__name__, required_keys=required_keys, config_json=config_json)

        strings = config_json["strings"]
        pairs = config_json["pairs"]
        if not all(isinstance(item, str) for item in strings):
            do_error(
                class_name=cls.__name__, err=f"Invalid config object: {strings}. 'strings' should be a list of strings."
            )

        if not all(
            isinstance(pair, list) and len(pair) == 2 and all(isinstance(item, str) for item in pair) for pair in pairs
        ):
            do_error(
                class_name=cls.__name__,
                err=f"Invalid config object: {config_json}. 'pairs' should be a list of pairs of strings.",
            )
        return config_json

    @property
    def strings(self) -> list:
        """Return a list of search terms"""
        return self.config_json.get("strings")

    @property
    def pairs(self) -> list:
        """Return a list of search terms"""
        return self.config_json.get("pairs")

    def to_json(self) -> json:
        """Return the config as a JSON object"""
        return self.config_json


class AdditionalInformation(PluginBase):
    """Additional information of a Plugin object"""

    config_json: dict = Field(..., description="Config object")

    @field_validator("config_json")
    @classmethod
    def validate_config_json(cls, config_json) -> dict:
        """Validate the config object"""
        if not isinstance(config_json, dict):
            do_error(class_name=cls.__name__, err=f"Expected a dict but received {type(config_json)}")
        return config_json

    @property
    def keys(self) -> list:
        """Return a list of keys for additional information"""
        return list(self.config_json.keys())

    def to_json(self) -> json:
        """Return the config as a JSON object"""
        return self.config_json


class Prompting(PluginBase):
    """Prompting child class of a Plugin object"""

    config_json: dict = Field(..., description="Config object")
    search_terms: SearchTerms = Field(None, description="Search terms of the config object")
    system_prompt: SystemPrompt = Field(None, description="System prompt of the config object")

    @root_validator(pre=True)
    def set_fields(cls, values):
        """proxy for __init__() - Set the fields"""
        config_json = values.get("config_json")
        if not isinstance(config_json, dict):
            raise ValueError(f"Expected config_json to be a dict but received {type(config_json)}")
        if config_json:
            values["search_terms"] = SearchTerms(config_json=config_json["search_terms"])
            values["system_prompt"] = SystemPrompt(system_prompt=config_json["system_prompt"])
        return values

    @field_validator("config_json")
    @classmethod
    def validate_config_json(cls, config_json) -> dict:
        """Validate the config object"""
        required_keys = ["search_terms", "system_prompt"]
        validate_required_keys(class_name=cls.__name__, required_keys=required_keys, config_json=config_json)

    def to_json(self) -> json:
        """Return the config as a JSON object"""
        return {
            "search_terms": self.search_terms.to_json(),
            "system_prompt": self.system_prompt.system_prompt,
        }


class FunctionCalling(PluginBase):
    """FunctionCalling child class of a Plugin"""

    config_json: dict = Field(..., description="Config object")
    function_description: str = Field(None, description="Description of the function")
    additional_information: AdditionalInformation = Field(None, description="Additional information of the function")

    @root_validator(pre=True)
    def set_fields(cls, values):
        """proxy for __init__() - Set the fields"""
        config_json = values.get("config_json")
        if not isinstance(config_json, dict):
            raise ValueError(f"Expected config_json to be a dict but received {type(config_json)}")
        if config_json:
            values["function_description"] = config_json["function_description"]
            values["additional_information"] = AdditionalInformation(config_json=config_json["additional_information"])
        return values

    @field_validator("config_json")
    @classmethod
    def validate_config_json(cls, config_json) -> dict:
        """Validate the config object"""
        if not isinstance(config_json, dict):
            do_error(class_name=cls.__name__, err=f"Expected a dict but received {type(config_json)}")
        required_keys = ["function_description", "additional_information"]
        validate_required_keys(class_name=cls.__name__, required_keys=required_keys, config_json=config_json)
        if not isinstance(config_json["function_description"], str):
            do_error(
                class_name=cls.__name__,
                err=f"Invalid config object: {config_json}. 'function_description' should be a string.",
            )
        if not isinstance(config_json["additional_information"], dict):
            do_error(
                class_name=cls.__name__,
                err=f"Invalid config object: {config_json}. 'additional_information' should be a dict.",
            )
        return config_json

    def to_json(self) -> json:
        """Return the config as a JSON object"""
        return {
            "function_description": self.function_description,
            "additional_information": self.additional_information.to_json(),
        }


class MetaData(PluginBase):
    """Metadata of a Plugin object"""

    config_json: dict = Field(..., description="Config object")

    @root_validator(pre=True)
    def set_fields(cls, values):
        """proxy for __init__() - Set the fields"""
        config_json = values.get("config_json")
        if not isinstance(config_json, dict):
            raise ValueError(f"Expected config_json to be a dict but received {type(config_json)}")
        return values

    @field_validator("config_json")
    @classmethod
    def validate_config_json(cls, config_json) -> dict:
        """Validate the config object"""
        if not isinstance(config_json, dict):
            do_error(class_name=cls.__name__, err=f"Expected a dict but received {type(config_json)}")

        required_keys = ["config_path", "name", "description", "version", "author"]
        validate_required_keys(class_name=cls.__name__, required_keys=required_keys, config_json=config_json)
        return config_json

    @property
    def name(self) -> str:
        """Return the name of the config object"""
        return self.config_json.get("name") if self.config_json else None

    @property
    def config_path(self) -> str:
        """Return the path of the config object"""
        return self.config_json.get("config_path") if self.config_json else None

    @property
    def description(self) -> str:
        """Return the description of the config object"""
        return self.config_json.get("description") if self.config_json else None

    @property
    def version(self) -> str:
        """Return the version of the config object"""
        return self.config_json.get("version") if self.config_json else None

    @property
    def author(self) -> str:
        """Return the author of the config object"""
        return self.config_json.get("author") if self.config_json else None

    def to_json(self) -> json:
        """Return the config as a JSON object"""
        return self.config_json


class Plugin(PluginBase):
    """A json object that contains the config for a plugin.function_calling_plugin() function"""

    index: int = Field(0, description="Index of the config object")
    config_json: dict = Field(..., description="Config object")
    meta_data: Optional[MetaData] = Field(None, description="Metadata of the config object")
    prompting: Optional[Prompting] = Field(None, description="Prompting of the config object")
    function_calling: Optional[FunctionCalling] = Field(None, description="FunctionCalling of the config object")

    @property
    def name(self) -> str:
        """Return a name in the format: "WillyWonka"""
        return self.meta_data.name

    @root_validator(pre=True)
    def set_fields(cls, values):
        """proxy for __init__() - Set the fields"""
        config_json = values.get("config_json")
        if not isinstance(config_json, dict):
            raise ValueError(f"Expected config_json to be a dict but received {type(config_json)}")
        if config_json:
            values["meta_data"] = MetaData(config_json=config_json.get("meta_data"))
            values["prompting"] = Prompting(config_json=config_json.get("prompting"))
            values["function_calling"] = FunctionCalling(config_json=config_json.get("function_calling"))
        return values

    @field_validator("config_json")
    @classmethod
    def validate_config_json(cls, config_json) -> None:
        """Validate the config object"""

        required_keys = ["meta_data", "prompting", "function_calling"]
        for key in required_keys:
            if key not in config_json:
                cls.do_error(f"Invalid config object: {config_json}. Missing key: {key}.")
            if not isinstance(config_json[key], dict):
                do_error(
                    class_name=cls.__name__,
                    err=f"Expected a dict for {key} but received {type(config_json[key])}: {config_json[key]}",
                )

    def to_json(self) -> json:
        """Return the config as a JSON object"""
        return {
            "name": self.name,
            "meta_data": self.meta_data.to_json(),
            "prompting": self.prompting.to_json(),
            "function_calling": self.function_calling.to_json(),
        }


class Plugins:
    """List of Plugin objects"""

    _custom_configs: list[Plugin] = None
    _aws_bucket_name: str = None
    _aws_bucket_path: str = "aws_openai/lambda_openai_function/plugins/"
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

                plugin = Plugin(config_json=config_json, index=i)
                self._custom_configs.append(plugin)

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
                        plugin = Plugin(config_json=config_json, index=i)
                        self._custom_configs.append(plugin)
                        # print(
                        #     f"Loaded plugin from AWS S3 bucket: {plugin.name} {plugin.meta_data.version} created by {plugin.meta_data.author}"
                        # )

    @property
    def valid_configs(self) -> list[Plugin]:
        """Return a list of valid configs"""
        return self._custom_configs

    @property
    def invalid_configs(self) -> list[Plugin]:
        """Return a list of invalid configs"""
        return []

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


class SingletonPlugins:
    """Singleton for Settings"""

    _instance = None
    _custom_configs = None

    def __new__(cls):
        """Create a new instance of Settings"""
        if cls._instance is None:
            cls._instance = super(SingletonPlugins, cls).__new__(cls)
            cls._instance._custom_configs = Plugins(
                config_path=CONFIG_PATH, aws_s3_bucket_name=settings.aws_s3_bucket_name
            )
        return cls._instance

    @property
    def plugins(self) -> Plugins:
        """Return the settings"""
        return self._custom_configs


plugins = SingletonPlugins().plugins.valid_configs
