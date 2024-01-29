# AWS Lambdas for API Gateway

The Python modules in this folder form a unit-tested common code base that is used to implement a collection of AWS Lambda functions. These Lambdas back the [AWS API Gateway](https://aws.amazon.com/api-gateway/) endpoint resources and are fully responsible for generating the [JSON](https://www.json.org/json-en.html) API responses that drive this app.

[AWS Lambda](https://aws.amazon.com/pm/lambda/) is a serverless compute managed service that gives you the ability to deploy a Python function to highly scalable compute infrastructure. The deployment process for these Lambdas is managed by Terraform and essentially takes care of the following:

1. Creating a collection of AWS Lambda and [AWS Lambda Layer](https://docs.aws.amazon.com/lambda/latest/dg/chapter-layers.html) resources in your AWS account.

2. Packaging the source code and any Python requirements into zip files, and uploading these to the corresponding AWS Lambda/Layer

3. Configuring environment variables on which the Lambdas depend in order to function. Examples include your OpenAI API key, debug flags, and CloudWath log settings.

4. Configuring AWS IAM role-based security for your Lambdas.

Note that **version**.py is maintained by Github Actions automations, hence you should avoid making modifications to this .

## lambda_langchain

A general purpose handler for the OpenAI API via Langchain. This is the primary Lambda function for this project, as it powers all 30 of the sample chatbot applications.

## lambda_openai_function

An adaptive ChatGPT interface that uses a combination of dynamic prompting and [Function Calling](https://platform.openai.com/docs/guides/function-calling) to create highly customized ChatGPT responses to user prompts. See these [example plugins](../openai_api/lambda_openai_function/plugins/) demonstrating some of the exciting things you can implement with this feature. This module leverages [Pydantic](https://docs.pydantic.dev/latest/) to validate the yaml plugin files that drive the behavior of this function.

## lambda_openai_v2

A general purpose handler for native calls to the OpenAI API. This function demonstrate how to work directly with the OpenAI API, without the abstraction layers that are provided by LangChain. It is generally preferable to use the LangChain function when possible, where this function is included more for instructional purposes than for production use.

## common

Contains shared code supporting the entire collection of AWS Lambda handlers. Modules of note:

- **conf.py**: a common [configuration module](./common/conf.py) that fully encapsulates the majority of the complexity of the backend for this project. This project is designed to run out-of-the-box in multiple environments, including your local dev machine, Ubuntu Linux-based GitHub Actions runners, and of course, the AWS Linux-based Lambda environment. This module leverages [Pydantic](https://docs.pydantic.dev/latest/) to manage the complexity that is introduced by allowing configuration data from multiple sources, including: a.) constants, b.) environment variables, c.) a .env file, and d.) Terraform variables.

- **aws.py**: mostly used by unit tests, this module includes helpful code patterns for using boto3 to interact with AWS infrastructure resources.

- **validators.py**: contains abstracted validation rules for working with the OpenAI Python API.

## lambda_info

Returns [this JSON dump](../../../../doc/json/apigateway_endpoing_info.json) of the AWS Lambda operating environment. This is a convenience tool aimed at assisting you with administration and diagnostics. It is not part of the application. However, an endpoint for this is included in the API which itself is included in the Postman template.
