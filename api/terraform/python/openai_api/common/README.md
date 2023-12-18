# OpenAI API shared code

Common constants, validations and misc utility functions that are called by both the openai and langchain lambdas.

## Settings class

This shared class manages configuration settings for all uses cases, including: local developments, test, QA, CI-CD, and production.

### Validations and strong data typing

The Settings class leverages [Pydantic](https://docs.pydantic.dev/latest/) to enforce strong data typing as well as to assist with common-sense validations of several of the configuration values. Additionally, it enables us to enforce a read-only state of the settings attributes.

### Ambiguous initialization scenarios

Sources of configuration data vary depending on the use case, which can invariably introduce ambiguities with regard to which source takes priority in varying scenarios. The Settings class resolves these potential ambiguities by consistently applying the following order of precedence by source:

1. Python constructor arguments passed from inside the source code
2. `.env` files which can be saved anywhere inside the repo, and nothing prevents multiple .env files from being created.
3. environment variables initialized in the form of `export VARIABLE_NAME=some-value`
4. `terraform.tfvars` if it exists
5. default values declared in SettingsDefaults class

Where possible, we use [Pydantic](https://docs.pydantic.dev/latest/) to seamlessly resolve some of these ambiguities.

### CloudWatch logging

The Settings class is also a provider to CloudWatch when debug_mode is set to `True`. The Settings property `cloudwatch_dump` generates a context sensitive JSON dict of the state data for all settings as well as some meta data that can be helpful during development trouble shooting.

An example CloudWatch dump:

```json
{
  "environment": {
    "is_using_tfvars_file": true,
    "is_using_dotenv_file": true,
    "os": "posix",
    "system": "Linux",
    "release": "6.2.0-1018-azure",
    "boto3": "1.34.2",
    "shared_resource_identifier": "openai",
    "debug_mode": true,
    "openai_api_version": "0.7.0",
    "dotenv": [
      "AWS_REGION",
      "DEBUG_MODE",
      "AWS_DYNAMODB_TABLE_ID",
      "AWS_REKOGNITION_FACE_DETECT_MAX_FACES_COUNT",
      "AWS_REKOGNITION_FACE_DETECT_THRESHOLD",
      "AWS_REKOGNITION_FACE_DETECT_ATTRIBUTES",
      "AWS_REKOGNITION_FACE_DETECT_QUALITY_FILTER",
      "AWS_REKOGNITION_COLLECTION_ID",
      "LANGCHAIN_MEMORY_KEY",
      "OPENAI_ENDPOINT_IMAGE_N",
      "OPENAI_ENDPOINT_IMAGE_SIZE"
    ],
    "tfvars": [
      "aws_account_id",
      "tags",
      "aws_region",
      "openai_endpoint_image_n",
      "openai_endpoint_image_size",
      "lambda_python_runtime",
      "debug_mode",
      "lambda_memory_size",
      "lambda_timeout",
      "logging_level",
      "log_retention_days",
      "create_custom_domain",
      "root_domain",
      "shared_resource_identifier",
      "stage",
      "quota_settings_limit",
      "quota_settings_offset",
      "quota_settings_period",
      "throttle_settings_burst_limit",
      "throttle_settings_rate_limit"
    ]
  },
  "aws_api_gateway": {
    "aws_apigateway_root_domain": "example.com",
    "aws_apigateway_custom_domain_name_create": false,
    "aws_apigateway_custom_domain_name": "api.openai.example.com"
  },
  "openai_api": {
    "langchain_memory_key": "chat_history",
    "openai_endpoint_image_n": 4,
    "openai_endpoint_image_size": "1024x768"
  }
}
```
