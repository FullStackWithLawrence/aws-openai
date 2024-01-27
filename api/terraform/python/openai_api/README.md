# AWS Lambdas for API Gateway

These are the Lambdas that are called from API Gateway endpoint resources.

Note that **version**.py is maintained by Github Actions automations.

## lambda_info

Returns [this JSON dump](../../../../doc/json/apigateway_endpoing_info.json) of the AWS Lambda operating environment.

## lambda_langchain

A general purpose handler for the OpenAI API via Langchain.

## lambda_openai_function

An adaptive ChatGPT interface that uses a combination of dynamic prompting and [Function Calling](https://platform.openai.com/docs/guides/function-calling) to create highly customized ChatGPT responses to user prompts. See these [example custom configurations](../openai_api/lambda_openai_function/config/) demonstrating some of the exciting things you can implement with this feature.

## lambda_openai_v2

A general purpose handler for native calls to the OpenAI API.
