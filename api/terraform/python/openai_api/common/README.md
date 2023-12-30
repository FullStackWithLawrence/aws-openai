# OpenAI API shared code

Common constants, validations and misc utility functions that are called by both the openai and langchain lambdas.

## Settings class

This shared class manages configuration settings for all uses cases, including: local development, test, QA, CI-CD, and production.

### Validations and strong data typing

The Settings class leverages [Pydantic](https://docs.pydantic.dev/latest/) to enforce strong data typing as well as to assist with common-sense validations of several of the configuration values. Additionally, it enables us to enforce a read-only state of the settings attributes in able to thwart potential side effects from erroneous CD-CD processes.

### Avoids ambiguous initialization scenarios

Sources of configuration data vary depending on the use case, which can invariably introduce ambiguities with regard to which source takes priority in varying scenarios. The Settings class resolves these potential ambiguities by consistently applying the following order of precedence by source:

1. Python constructor arguments passed from inside the source code
2. `.env` files which can be saved anywhere inside the repo, and nothing prevents multiple .env files from being created.
3. environment variables initialized in the form of `export VARIABLE_NAME=some-value`
4. `terraform.tfvars` if it exists
5. default values declared in SettingsDefaults class

Where possible, we use [Pydantic](https://docs.pydantic.dev/latest/) to seamlessly resolve some of these ambiguities.

### Protects sensitive data

The Settings class will not expose sensitive data under any circumstances, including logging and dumps.

#### AWS configuration

The Settings class contains instance variables for `aws_profile` and `aws_region`. If either of these is unset then standard behavior of [AWS CLI](https://aws.amazon.com/cli/) will take precedence.

#### OpenAI API configuration

The Settings class contains an instance variable for `openai_api_key` which will take precedence if it is set.

#### Pinecone API configuration

The Settings class contains an instance variable for `pinecone_api_key` which will take precedence if it is set.

### CloudWatch logging

The Settings class is also a provider to CloudWatch when both `DEBUG_MODE` and `DUMP_DEFAULTS` environment variables are set to `True`. The Settings property `dump` generates a context sensitive JSON dict of the state data for all settings as well as class instance meta data that can be helpful during development trouble shooting.

An example [CloudWatch Dump](../../../../../doc/json/settings_cloudwatch_dump_example.json)
