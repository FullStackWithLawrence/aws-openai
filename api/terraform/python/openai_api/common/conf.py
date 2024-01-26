# -*- coding: utf-8 -*-
# pylint: disable=no-member,no-self-argument,unused-argument
"""
Configuration for Lambda functions.

This module is used to configure the Lambda functions. It uses the pydantic_settings
library to validate the configuration values. The configuration values are initialized
according to the following prioritization sequence:
    1. constructor
    2. environment variables
    3. `.env` file
    4. tfvars file
    5. defaults

The Settings class also provides a dump property that returns a dictionary of all
configuration values. This is useful for debugging and logging.
"""

# python stuff
import importlib.util
import logging
import os  # library for interacting with the operating system
import platform  # library to view information about the server host this Lambda runs on
import re
from typing import Any, Dict, List, Optional, Tuple, Union

# 3rd party stuff
import boto3  # AWS SDK for Python https://boto3.amazonaws.com/v1/documentation/api/latest/index.html
import pkg_resources
from botocore.config import Config
from botocore.exceptions import ProfileNotFound
from dotenv import load_dotenv

# our stuff
from openai_api.common.const import IS_USING_TFVARS, PROJECT_ROOT, TFVARS
from openai_api.common.exceptions import (
    OpenAIAPIConfigurationError,
    OpenAIAPIValueError,
)
from openai_api.common.utils import recursive_sort_dict
from pydantic import Field, SecretStr, ValidationError, ValidationInfo, field_validator
from pydantic_settings import BaseSettings


logger = logging.getLogger(__name__)
TFVARS = TFVARS or {}
DOT_ENV_LOADED = load_dotenv()


def load_version() -> Dict[str, str]:
    """Stringify the __version__ module."""
    version_file_path = os.path.join(PROJECT_ROOT, "__version__.py")
    spec = importlib.util.spec_from_file_location("__version__", version_file_path)
    version_module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(version_module)
    return version_module.__dict__


VERSION = load_version()


def get_semantic_version() -> str:
    """
    Return the semantic version number.

    Example valid values of __version__.py are:
    0.1.17
    0.1.17-next.1
    0.1.17-next.2
    0.1.17-next.123456
    0.1.17-next-major.1
    0.1.17-next-major.2
    0.1.17-next-major.123456

    Note:
    - pypi does not allow semantic version numbers to contain a dash.
    - pypi does not allow semantic version numbers to contain a 'v' prefix.
    - pypi does not allow semantic version numbers to contain a 'next' suffix.
    """
    if not isinstance(VERSION, dict):
        return "unknown"

    version = VERSION.get("__version__")
    if not version:
        return "unknown"
    version = re.sub(r"-next\.\d+", "", version)
    return re.sub(r"-next-major\.\d+", "", version)


class Services:
    """Services enabled for this solution. This is intended to be permanently read-only"""

    # enabled
    AWS_CLI = ("aws-cli", True)
    AWS_APIGATEWAY = ("apigateway", True)
    AWS_CLOUDWATCH = ("cloudwatch", True)
    AWS_EC2 = ("ec2", True)
    AWS_IAM = ("iam", True)
    AWS_LAMBDA = ("lambda", True)
    AWS_ROUTE53 = ("route53", True)
    AWS_S3 = ("s3", True)

    # disabled
    AWS_SNS = ("sns", False)
    AWS_SQS = ("sqs", False)
    AWS_SES = ("ses", False)
    AWS_REKOGNITION = ("rekognition", False)
    AWS_DYNAMODB = ("dynamodb", False)
    AWS_RDS = ("rds", False)

    @classmethod
    def enabled(cls, service: Union[str, Tuple[str, bool]]) -> bool:
        """Is the service enabled?"""
        if isinstance(service, tuple):
            service = service[0]
        return service in cls.enabled_services()

    @classmethod
    def raise_error_on_disabled(cls, service: Union[str, Tuple[str, bool]]) -> None:
        """Raise an error if the service is disabled"""
        if not cls.enabled(service):
            raise OpenAIAPIConfigurationError(f"{service} is not enabled. See conf.Services")

    @classmethod
    def to_dict(cls):
        """Convert Services to dict"""
        return {
            key: value
            for key, value in Services.__dict__.items()
            if not key.startswith("__")
            and not callable(key)
            and key not in ["enabled", "raise_error_on_disabled", "to_dict", "enabled_services"]
        }

    @classmethod
    def enabled_services(cls) -> List[str]:
        """Return a list of enabled services"""
        return [
            getattr(cls, key)[0]
            for key in dir(cls)
            if not key.startswith("__")
            and not callable(getattr(cls, key))
            and key not in ["enabled", "raise_error_on_disabled", "to_dict", "enabled_services"]
            and getattr(cls, key)[1] is True
        ]


# pylint: disable=too-few-public-methods
class SettingsDefaults:
    """Default values for Settings"""

    # defaults for this Python package
    SHARED_RESOURCE_IDENTIFIER = TFVARS.get("shared_resource_identifier", "openai")
    DEBUG_MODE: bool = bool(TFVARS.get("debug_mode", False))
    DUMP_DEFAULTS: bool = bool(TFVARS.get("dump_defaults", True))

    # aws auth
    AWS_PROFILE = TFVARS.get("aws_profile", None)
    AWS_ACCESS_KEY_ID = SecretStr(None)
    AWS_SECRET_ACCESS_KEY = SecretStr(None)
    AWS_REGION = TFVARS.get("aws_region", "us-east-1")

    # aws api gateway defaults
    AWS_APIGATEWAY_CREATE_CUSTOM_DOMAIN = TFVARS.get("create_custom_domain", False)
    AWS_APIGATEWAY_ROOT_DOMAIN = TFVARS.get("root_domain", None)
    AWS_APIGATEWAY_READ_TIMEOUT: int = TFVARS.get("aws_apigateway_read_timeout", 70)
    AWS_APIGATEWAY_CONNECT_TIMEOUT: int = TFVARS.get("aws_apigateway_connect_timeout", 70)
    AWS_APIGATEWAY_MAX_ATTEMPTS: int = TFVARS.get("aws_apigateway_max_attempts", 10)

    GOOGLE_MAPS_API_KEY: str = TFVARS.get("google_maps_api_key", None)

    LANGCHAIN_MEMORY_KEY = "chat_history"
    OPENAI_API_ORGANIZATION: str = None
    OPENAI_API_KEY = SecretStr(None)
    OPENAI_ENDPOINT_IMAGE_N = 4
    OPENAI_ENDPOINT_IMAGE_SIZE = "1024x768"
    PINECONE_API_KEY = SecretStr(None)

    @classmethod
    def to_dict(cls):
        """Convert SettingsDefaults to dict"""
        return {
            key: "***MASKED***" if key in ["AWS_ACCESS_KEY_ID", "AWS_SECRET_ACCESS_KEY"] else value
            for key, value in SettingsDefaults.__dict__.items()
            if not key.startswith("__") and not callable(key) and key != "to_dict"
        }


AWS_REGIONS = []
if Services.enabled(Services.AWS_EC2):
    ec2 = boto3.Session().client("ec2")
    regions = ec2.describe_regions()
    AWS_REGIONS = [region["RegionName"] for region in regions["Regions"]]


def empty_str_to_bool_default(v: str, default: bool) -> bool:
    """Convert empty string to default boolean value"""
    if v in [None, ""]:
        return default
    return v.lower() in ["true", "1", "t", "y", "yes"]


def empty_str_to_int_default(v: str, default: int) -> int:
    """Convert empty string to default integer value"""
    if v in [None, ""]:
        return default
    try:
        return int(v)
    except ValueError:
        return default


# pylint: disable=too-many-public-methods
# pylint: disable=too-many-instance-attributes
class Settings(BaseSettings):
    """Settings for Lambda functions"""

    _aws_session: boto3.Session = None
    _aws_apigateway_client = None
    _aws_s3_client = None
    _aws_dynamodb_client = None
    _aws_rekognition_client = None
    _aws_access_key_id_source: str = "unset"
    _aws_secret_access_key_source: str = "unset"
    _dump: dict = None
    _initialized: bool = False

    # pylint: disable=too-many-branches,too-many-statements
    def __init__(self, **data: Any):  # noqa: C901
        super().__init__(**data)
        if not Services.enabled(Services.AWS_CLI):
            self._initialized = True
            return

        if bool(os.environ.get("AWS_DEPLOYED", False)):
            # If we're running inside AWS Lambda, then we don't need to set the AWS credentials.
            logger.info("running inside AWS Lambda")
            self._aws_access_key_id_source: str = "overridden by IAM role-based security"
            self._aws_secret_access_key_source: str = "overridden by IAM role-based security"
            self._aws_session = boto3.Session()
            self._initialized = True

        if not self.initialized and bool(os.environ.get("GITHUB_ACTIONS", False)):
            console_handler = logging.StreamHandler()
            console_handler.setLevel(logging.DEBUG)
            logger.addHandler(console_handler)
            logger.setLevel(logging.DEBUG)

            logger.info("running inside GitHub Actions")
            aws_access_key_id = os.environ.get("AWS_ACCESS_KEY_ID", None)
            aws_secret_access_key = os.environ.get("AWS_SECRET_ACCESS_KEY", None)
            if not aws_access_key_id or not aws_secret_access_key and not self.aws_profile:
                raise OpenAIAPIConfigurationError(
                    "required environment variable(s) AWS_ACCESS_KEY_ID and/or AWS_SECRET_ACCESS_KEY not set"
                )
            region_name = os.environ.get("AWS_REGION", None)
            if not region_name and not self.aws_profile:
                raise OpenAIAPIConfigurationError("required environment variable AWS_REGION not set")
            try:
                self._aws_session = boto3.Session(
                    region_name=region_name,
                    aws_access_key_id=aws_access_key_id,
                    aws_secret_access_key=aws_secret_access_key,
                )
                self._initialized = True
                self._aws_access_key_id_source = "environ"
                self._aws_secret_access_key_source = "environ"
            except ProfileNotFound:
                # only log this if the aws_profile is set
                if self.aws_profile:
                    logger.warning("aws_profile %s not found", self.aws_profile)

            if self.aws_profile:
                self._aws_access_key_id_source = "aws_profile"
                self._aws_secret_access_key_source = "aws_profile"
            else:
                self._aws_access_key_id_source = "environ"
                self._aws_secret_access_key_source = "environ"

            self._initialized = True

        if not self.initialized:
            if self.aws_profile:
                self._aws_access_key_id_source = "aws_profile"
                self._aws_secret_access_key_source = "aws_profile"
                self._initialized = True

        if not self.initialized:
            if "aws_access_key_id" in data or "aws_secret_access_key" in data:
                if "aws_access_key_id" in data:
                    self._aws_access_key_id_source = "constructor"
                if "aws_secret_access_key" in data:
                    self._aws_secret_access_key_source = "constructor"
                self._initialized = True

        if not self.initialized:
            if "AWS_ACCESS_KEY_ID" in os.environ:
                self._aws_access_key_id_source = "environ"
            if "AWS_SECRET_ACCESS_KEY" in os.environ:
                self._aws_secret_access_key_source = "environ"

        if self.debug_mode:
            logger.setLevel(logging.DEBUG)

        # pylint: disable=logging-fstring-interpolation
        logger.debug(f"initialized settings: {self.aws_auth}")
        self._initialized = True

    shared_resource_identifier: Optional[str] = Field(
        SettingsDefaults.SHARED_RESOURCE_IDENTIFIER, env="SHARED_RESOURCE_IDENTIFIER"
    )
    debug_mode: Optional[bool] = Field(
        SettingsDefaults.DEBUG_MODE,
        env="DEBUG_MODE",
        pre=True,
        getter=lambda v: empty_str_to_bool_default(v, SettingsDefaults.DEBUG_MODE),
    )
    dump_defaults: Optional[bool] = Field(
        SettingsDefaults.DUMP_DEFAULTS,
        env="DUMP_DEFAULTS",
        pre=True,
        getter=lambda v: empty_str_to_bool_default(v, SettingsDefaults.DUMP_DEFAULTS),
    )
    aws_profile: Optional[str] = Field(
        SettingsDefaults.AWS_PROFILE,
        env="AWS_PROFILE",
    )
    aws_access_key_id: Optional[SecretStr] = Field(
        SettingsDefaults.AWS_ACCESS_KEY_ID,
        env="AWS_ACCESS_KEY_ID",
    )
    aws_secret_access_key: Optional[SecretStr] = Field(
        SettingsDefaults.AWS_SECRET_ACCESS_KEY,
        env="AWS_SECRET_ACCESS_KEY",
    )
    aws_regions: Optional[List[str]] = Field(AWS_REGIONS, description="The list of AWS regions")
    aws_region: Optional[str] = Field(
        SettingsDefaults.AWS_REGION,
        env="AWS_REGION",
    )
    aws_apigateway_create_custom_domaim: Optional[bool] = Field(
        SettingsDefaults.AWS_APIGATEWAY_CREATE_CUSTOM_DOMAIN,
        env="AWS_APIGATEWAY_CREATE_CUSTOM_DOMAIN",
        pre=True,
        getter=lambda v: empty_str_to_bool_default(v, SettingsDefaults.AWS_APIGATEWAY_CREATE_CUSTOM_DOMAIN),
    )
    aws_apigateway_root_domain: Optional[str] = Field(
        SettingsDefaults.AWS_APIGATEWAY_ROOT_DOMAIN,
        env="AWS_APIGATEWAY_ROOT_DOMAIN",
    )
    init_info: Optional[str] = Field(
        None,
        env="INIT_INFO",
    )
    google_maps_api_key: Optional[str] = Field(
        SettingsDefaults.GOOGLE_MAPS_API_KEY,
        env="GOOGLE_MAPS_API_KEY",
    )
    langchain_memory_key: Optional[str] = Field(SettingsDefaults.LANGCHAIN_MEMORY_KEY, env="LANGCHAIN_MEMORY_KEY")
    openai_api_organization: Optional[str] = Field(
        SettingsDefaults.OPENAI_API_ORGANIZATION, env="OPENAI_API_ORGANIZATION"
    )
    openai_api_key: Optional[SecretStr] = Field(SettingsDefaults.OPENAI_API_KEY, env="OPENAI_API_KEY")
    openai_endpoint_image_n: Optional[int] = Field(
        SettingsDefaults.OPENAI_ENDPOINT_IMAGE_N, env="OPENAI_ENDPOINT_IMAGE_N"
    )
    openai_endpoint_image_size: Optional[str] = Field(
        SettingsDefaults.OPENAI_ENDPOINT_IMAGE_SIZE, env="OPENAI_ENDPOINT_IMAGE_SIZE"
    )
    pinecone_api_key: Optional[SecretStr] = Field(SettingsDefaults.PINECONE_API_KEY, env="PINECONE_API_KEY")

    @property
    def initialized(self):
        """Is settings initialized?"""
        return self._initialized

    @property
    def aws_account_id(self):
        """AWS account id"""
        Services.raise_error_on_disabled(Services.AWS_CLI)
        sts_client = self.aws_session.client("sts")
        if not sts_client:
            logger.warning("could not initialize sts_client")
            return None
        retval = sts_client.get_caller_identity()
        if not isinstance(retval, dict):
            logger.warning("sts_client.get_caller_identity() did not return a dict")
            return None
        return retval.get("Account", None)

    @property
    def aws_access_key_id_source(self):
        """Source of aws_access_key_id"""
        return self._aws_access_key_id_source

    @property
    def aws_secret_access_key_source(self):
        """Source of aws_secret_access_key"""
        return self._aws_secret_access_key_source

    @property
    def aws_auth(self) -> dict:
        """AWS authentication"""
        retval = {
            "aws_profile": self.aws_profile,
            "aws_access_key_id_source": self.aws_access_key_id_source,
            "aws_secret_access_key_source": self.aws_secret_access_key_source,
            "aws_region": self.aws_region,
        }
        if self.init_info:
            retval["init_info"] = self.init_info
        return retval

    @property
    def aws_session(self):
        """AWS session"""
        Services.raise_error_on_disabled(Services.AWS_CLI)
        if not self._aws_session:
            if self.aws_profile:
                logger.debug("creating new aws_session with aws_profile: %s", self.aws_profile)
                try:
                    self._aws_session = boto3.Session(profile_name=self.aws_profile, region_name=self.aws_region)
                except ProfileNotFound:
                    logger.warning("aws_profile %s not found", self.aws_profile)

                return self._aws_session
            if self.aws_access_key_id.get_secret_value() is not None and self.aws_secret_access_key is not None:
                logger.debug("creating new aws_session with aws keypair: %s", self.aws_access_key_id_source)
                self._aws_session = boto3.Session(
                    region_name=self.aws_region,
                    aws_access_key_id=self.aws_access_key_id.get_secret_value(),
                    aws_secret_access_key=self.aws_secret_access_key.get_secret_value(),
                )
                return self._aws_session
            logger.debug("creating new aws_session without aws credentials")
            self._aws_session = boto3.Session(region_name=self.aws_region)
        return self._aws_session

    @property
    def aws_route53_client(self):
        """Route53 client"""
        Services.raise_error_on_disabled(Services.AWS_ROUTE53)
        return self.aws_session.client("route53")

    @property
    def aws_apigateway_client(self):
        """API Gateway client"""
        Services.raise_error_on_disabled(Services.AWS_APIGATEWAY)
        if not self._aws_apigateway_client:
            config = Config(
                read_timeout=SettingsDefaults.AWS_APIGATEWAY_READ_TIMEOUT,
                connect_timeout=SettingsDefaults.AWS_APIGATEWAY_CONNECT_TIMEOUT,
                retries={"max_attempts": SettingsDefaults.AWS_APIGATEWAY_MAX_ATTEMPTS},
            )
            self._aws_apigateway_client = self.aws_session.client("apigateway", config=config)
        return self._aws_apigateway_client

    @property
    def aws_dynamodb_client(self):
        """DynamoDB client"""
        Services.raise_error_on_disabled(Services.AWS_DYNAMODB)
        if not self._aws_dynamodb_client:
            self._aws_dynamodb_client = self.aws_session.client("dynamodb")
        return self._aws_dynamodb_client

    @property
    def aws_s3_client(self):
        """S3 client"""
        Services.raise_error_on_disabled(Services.AWS_S3)
        if not self._aws_s3_client:
            self._aws_s3_client = self.aws_session.client("s3")
        return self._aws_s3_client

    @property
    def aws_apigateway_name(self) -> str:
        """Return the API name."""
        return self.shared_resource_identifier + "-api"

    @property
    def aws_apigateway_domain_name(self) -> str:
        """Return the API domain."""
        if self.aws_apigateway_create_custom_domaim:
            return "api." + self.shared_resource_identifier + "." + self.aws_apigateway_root_domain

        response = self.aws_apigateway_client.get_rest_apis()
        for item in response["items"]:
            if item["name"] == self.aws_apigateway_name:
                api_id = item["id"]
                return f"{api_id}.execute-api.{settings.aws_region}.amazonaws.com"
        return None

    @property
    def aws_s3_bucket_name(self) -> str:
        """Return the S3 bucket name."""
        if self.shared_resource_identifier and self.aws_apigateway_root_domain:
            return "api." + self.shared_resource_identifier + "." + self.aws_apigateway_root_domain
        return None

    @property
    def is_using_dotenv_file(self) -> bool:
        """Is the dotenv file being used?"""
        return DOT_ENV_LOADED

    @property
    def environment_variables(self) -> List[str]:
        """Environment variables"""
        return list(os.environ.keys())

    @property
    def is_using_tfvars_file(self) -> bool:
        """Is the tfvars file being used?"""
        return IS_USING_TFVARS

    @property
    def tfvars_variables(self) -> dict:
        """Terraform variables"""
        masked_tfvars = TFVARS.copy()
        if "aws_account_id" in masked_tfvars:
            masked_tfvars["aws_account_id"] = "****"
        return masked_tfvars

    @property
    def version(self) -> str:
        """OpenAI API version"""
        return get_semantic_version()

    @property
    def dump(self) -> dict:
        """Dump all settings."""

        def get_installed_packages():
            installed_packages = pkg_resources.working_set
            # pylint: disable=not-an-iterable
            package_list = [(d.project_name, d.version) for d in installed_packages]
            return package_list

        if self._dump and self.initialized:
            return self._dump

        if not self.initialized:
            return {}

        packages = get_installed_packages()
        packages_dict = [{"name": name, "version": version} for name, version in packages]

        self._dump = {
            "services": Services.enabled_services(),
            "environment": {
                "is_using_tfvars_file": self.is_using_tfvars_file,
                "is_using_dotenv_file": self.is_using_dotenv_file,
                "os": os.name,
                "system": platform.system(),
                "release": platform.release(),
                "boto3": boto3.__version__,
                "shared_resource_identifier": self.shared_resource_identifier,
                "debug_mode": self.debug_mode,
                "dump_defaults": self.dump_defaults,
                "version": self.version,
                "python_version": platform.python_version(),
                "python_implementation": platform.python_implementation(),
                "python_compiler": platform.python_compiler(),
                "python_build": platform.python_build(),
                "python_installed_packages": packages_dict,
            },
            "aws_auth": self.aws_auth,
            "aws_apigateway": {
                "aws_apigateway_create_custom_domaim": self.aws_apigateway_create_custom_domaim,
                "aws_apigateway_name": self.aws_apigateway_name,
                "aws_apigateway_root_domain": self.aws_apigateway_root_domain,
                "aws_apigateway_domain_name": self.aws_apigateway_domain_name,
            },
            "aws_lambda": {},
            "google": {
                "google_maps_api_key": self.google_maps_api_key,
            },
            "openai_api": {
                "aws_s3_bucket_name": self.aws_s3_bucket_name,
                "langchain_memory_key": self.langchain_memory_key,
                "openai_endpoint_image_n": self.openai_endpoint_image_n,
                "openai_endpoint_image_size": self.openai_endpoint_image_size,
            },
        }
        if self.dump_defaults:
            settings_defaults = SettingsDefaults.to_dict()
            self._dump["settings_defaults"] = settings_defaults

        if self.is_using_dotenv_file:
            self._dump["environment"]["dotenv"] = self.environment_variables

        if self.is_using_tfvars_file:
            self._dump["environment"]["tfvars"] = self.tfvars_variables

        self._dump = recursive_sort_dict(self._dump)
        return self._dump

    # pylint: disable=too-few-public-methods
    class Config:
        """Pydantic configuration"""

        frozen = True

    @field_validator("shared_resource_identifier")
    def validate_shared_resource_identifier(cls, v) -> str:
        """Validate shared_resource_identifier"""
        if v in [None, ""]:
            return SettingsDefaults.SHARED_RESOURCE_IDENTIFIER
        return v

    @field_validator("aws_profile")
    def validate_aws_profile(cls, v) -> str:
        """Validate aws_profile"""
        if v in [None, ""]:
            return SettingsDefaults.AWS_PROFILE
        return v

    @field_validator("aws_access_key_id")
    def validate_aws_access_key_id(cls, v, values: ValidationInfo) -> str:
        """Validate aws_access_key_id"""
        if not isinstance(v, SecretStr):
            v = SecretStr(v)
        if v.get_secret_value() in [None, ""]:
            return SettingsDefaults.AWS_ACCESS_KEY_ID
        aws_profile = values.data.get("aws_profile", None)
        if aws_profile and len(aws_profile) > 0 and aws_profile != SettingsDefaults.AWS_PROFILE:
            # pylint: disable=logging-fstring-interpolation
            logger.warning(f"aws_access_key_id is being ignored. using aws_profile {aws_profile}.")
            return SettingsDefaults.AWS_ACCESS_KEY_ID
        return v

    @field_validator("aws_secret_access_key")
    def validate_aws_secret_access_key(cls, v, values: ValidationInfo) -> str:
        """Validate aws_secret_access_key"""
        if not isinstance(v, SecretStr):
            v = SecretStr(v)
        if v.get_secret_value() in [None, ""]:
            return SettingsDefaults.AWS_SECRET_ACCESS_KEY
        aws_profile = values.data.get("aws_profile", None)
        if aws_profile and len(aws_profile) > 0 and aws_profile != SettingsDefaults.AWS_PROFILE:
            # pylint: disable=logging-fstring-interpolation
            logger.warning(f"aws_secret_access_key is being ignored. using aws_profile {aws_profile}.")
            return SettingsDefaults.AWS_SECRET_ACCESS_KEY
        return v

    @field_validator("aws_region")
    def validate_aws_region(cls, v, values: ValidationInfo, **kwargs) -> str:
        """Validate aws_region"""
        valid_regions = values.data.get("aws_regions", [])
        if v in [None, ""]:
            return SettingsDefaults.AWS_REGION
        if v not in valid_regions:
            raise OpenAIAPIValueError(f"aws_region {v} not in aws_regions")
        return v

    @field_validator("aws_apigateway_root_domain")
    def validate_aws_apigateway_root_domain(cls, v) -> str:
        """Validate aws_apigateway_root_domain"""
        if v in [None, ""]:
            return SettingsDefaults.AWS_APIGATEWAY_ROOT_DOMAIN
        return v

    @field_validator("aws_apigateway_create_custom_domaim")
    def validate_aws_apigateway_create_custom_domaim(cls, v) -> bool:
        """Validate aws_apigateway_create_custom_domaim"""
        if v in [None, ""]:
            return SettingsDefaults.AWS_APIGATEWAY_CREATE_CUSTOM_DOMAIN
        return v

    @field_validator("debug_mode")
    def parse_debug_mode(cls, v) -> bool:
        """Parse debug_mode"""
        if isinstance(v, bool):
            return v
        if v in [None, ""]:
            return SettingsDefaults.DEBUG_MODE
        return v.lower() in ["true", "1", "t", "y", "yes"]

    @field_validator("dump_defaults")
    def parse_dump_defaults(cls, v) -> bool:
        """Parse dump_defaults"""
        if isinstance(v, bool):
            return v
        if v in [None, ""]:
            return SettingsDefaults.DUMP_DEFAULTS
        return v.lower() in ["true", "1", "t", "y", "yes"]

    @field_validator("google_maps_api_key")
    def check_google_maps_api_key(cls, v) -> str:
        """Check google_maps_api_key"""
        if v in [None, ""]:
            return SettingsDefaults.GOOGLE_MAPS_API_KEY
        return v

    @field_validator("langchain_memory_key")
    def check_langchain_memory_key(cls, v) -> str:
        """Check langchain_memory_key"""
        if isinstance(v, int):
            return v
        if v in [None, ""]:
            return SettingsDefaults.LANGCHAIN_MEMORY_KEY
        return v

    @field_validator("openai_api_organization")
    def check_openai_api_organization(cls, v) -> str:
        """Check openai_api_organization"""
        if v in [None, ""]:
            return SettingsDefaults.OPENAI_API_ORGANIZATION
        return v

    @field_validator("openai_api_key")
    def check_openai_api_key(cls, v) -> SecretStr:
        """Check openai_api_key"""
        if v in [None, ""]:
            return SettingsDefaults.OPENAI_API_KEY
        return v

    @field_validator("openai_endpoint_image_n")
    def check_openai_endpoint_image_n(cls, v) -> int:
        """Check openai_endpoint_image_n"""
        if isinstance(v, int):
            return v
        if v in [None, ""]:
            return SettingsDefaults.OPENAI_ENDPOINT_IMAGE_N
        return int(v)

    @field_validator("openai_endpoint_image_size")
    def check_openai_endpoint_image_size(cls, v) -> str:
        """Check openai_endpoint_image_size"""
        if v in [None, ""]:
            return SettingsDefaults.OPENAI_ENDPOINT_IMAGE_SIZE
        return v

    @field_validator("pinecone_api_key")
    def check_pinecone_api_key(cls, v) -> SecretStr:
        """Check pinecone_api_key"""
        if v in [None, ""]:
            return SettingsDefaults.PINECONE_API_KEY
        return v


class SingletonSettings:
    """Singleton for Settings"""

    _instance = None

    def __new__(cls):
        """Create a new instance of Settings"""
        if cls._instance is None:
            cls._instance = super(SingletonSettings, cls).__new__(cls)
            try:
                cls._instance._settings = Settings()
            except ValidationError as e:
                raise OpenAIAPIConfigurationError("Invalid configuration: " + str(e)) from e
        return cls._instance

    @property
    def settings(self) -> Settings:
        """Return the settings"""
        return self._settings


settings = SingletonSettings().settings
