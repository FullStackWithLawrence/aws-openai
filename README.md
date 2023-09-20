[![OpenAI](https://a11ybadges.com/badge?logo=openai)](https://platform.openai.com/)
[![AWS](https://img.shields.io/badge/AWS-%23FF9900.svg?style=for-the-badge&logo=amazon-aws&logoColor=white)](https://aws.amazon.com/)

# OpenAI API on AWS

A REST API implementing each of the [30 example applications](https://platform.openai.com/examples) from the official [OpenAI API Documentation](https://platform.openai.com/docs/api-reference/making-requests?lang=python) using a modularized Terraform approach. Implemented as a serverless microservice using AWS [API Gateway](https://aws.amazon.com/api-gateway/), [Lambda](https://aws.amazon.com/lambda/) and the [OpenAI Python Library](https://pypi.org/project/openai/). Leverages OpenAI's suite of AI models, including [GPT-3.5](https://platform.openai.com/docs/models/gpt-3-5), [GPT-4](https://platform.openai.com/docs/models/gpt-4), [DALL·E](https://platform.openai.com/docs/models/dall-e), [Whisper](https://platform.openai.com/docs/models/whisper), [Embeddings](https://platform.openai.com/docs/models/embeddings), and [Moderation](https://platform.openai.com/docs/models/moderation).

- Creating new OpenAI applications and endpoints for this API only takes a few lines of code and is as easy as it is fun! Follow [this link](./terraform/apigateway_endpoints.tf) to see how each of these are coded.
- **Follow [this link](./doc/examples/README.md) for detailed documentation on each URL endpoint.**

## Usage

An example request and response. This endpoint inspects and corrects gramatical errors.

```console
curl --location --request PUT 'https://api.openai.yourdomain.com/examples/default-grammar' \
--header 'x-api-key: your-apigateway-api-key' \
--header 'Content-Type: application/json' \
--data '{"input_text": "She no went to the market."}'
```

return value

```json
{
    "isBase64Encoded": false,
    "statusCode": 200,
    "headers": {
        "Content-Type": "application/json"
    },
    "body": {
        "id": "chatcmpl-7yLxpF7ZsJzF3FTUICyUKDe1Ob9nd",
        "object": "chat.completion",
        "created": 1694618465,
        "model": "gpt-3.5-turbo-0613",
        "choices": [
            {
                "index": 0,
                "message": {
                  "role": "assistant",
                  "content": "The correct way to phrase this sentence would be: \"She did not go to the market.\""
                },
                "finish_reason": "stop"
            }
        ],
        "usage": {
            "prompt_tokens": 36,
            "completion_tokens": 10,
            "total_tokens": 46
        }
    }
}
```

## Official YouTube Video For This Repo

[![OpenAI Python API With AWS API Gateway + Lambda](https://img.youtube.com/vi/FqARAi8nS2M/hqdefault.jpg)](https://www.youtube.com/watch?v=FqARAi8nS2M)

## Requirements

- [AWS account](https://aws.amazon.com/)
- [AWS Command Line Interface](https://aws.amazon.com/cli/)
- [Terraform](https://www.terraform.io/).
    *If you're new to Terraform then see [Getting Started With AWS and Terraform](./doc/terraform-getting-started.md)*
- [OpenAI platform API key](https://platform.openai.com/).
    *If you're new to OpenAI API then see [How to Get an OpenAI API Key](./doc/openai-api-key.md)*

## Setup

1. clone this repo and setup a Python virtual environment

    ```console
    git clone https://github.com/FullStackWithLawrence/aws-openai.git
    cd aws-openai
    make init
    ```

2. add your OpenAI API credentials to the [.env](./.env) file in the root folder of this repo. Your organization ID and API Key should appear similar in format to these examples below.

    ```console
    OPENAI_API_ORGANIZATION=org-YJzABCDEFGHIJESMShcyulf0
    OPENAI_API_KEY=sk-7doQ4gAITSez7ABCDEFGHIJlbkFJKLOuEbRhAFadzjtnzAV2
    ```

    *Windows/Powershell users: you'll need to modify [./terraform/lambda_openai.tf](./terraform/lambda_openai.tf) data "external" "env" as per instructions in this code block.*


3. Add your AWS account number and region to Terraform. Set these three values in [terraform.tfvars](./terraform/terraform.tfvars):

    ```terraform
    account_id           = "012345678912"   # Required: your 12-digit AWS account number
    aws_region           = "us-east-1"      # Optional: an AWS data center
    aws_profile          = "default"        # Optional: for aws cli credentials
    ```

    *see the README section **"Installation Prerequisites"** below for instructions on setting up Terraform for first-time use.*

4. Build and deploy the microservice..

    ```terraform
    terraform init
    terraform apply
    ```

    *Note the output variables for your API Gateway root URL and API key.*
    ![Postman](https://raw.githubusercontent.com/FullStackWithLawrence/aws-openai/main/doc/terraform-apply2.png "Postman")

5. (Optional) use the [preconfigured import files](./postman/) to setup a Postman collection with all 30 URL endpoints.

    ![Postman](https://raw.githubusercontent.com/FullStackWithLawrence/aws-openai/main/doc/postman-1.png "Postman")

### Custom Domain (Optional)

If you manage a domain name using AWS Route53 then you can optionally deploy this API using your own custom domain name. Modify the following variables in [terraform/terraform.tfvars](./terraform/terraform.tfvars) and Terraform wil take care of the rest.

```terraform
create_custom_domain       = true
root_domain                = "yourdomain.com"
```

## How It Works

![API Workflow](https://raw.githubusercontent.com/FullStackWithLawrence/aws-openai/main/doc/api-workflow.png "API Workflow")

1. a JSON object and custom headers are added to an HTTP request and sent to the API as a 'PUT' method.
2. API Gateway uses a [Request Mapping Template](https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-mapping-template-reference.html) in a non-proxy Lambda integration request to combine user request text with your OpenAPI application definition, and then forward the combined data as a custom JSON object to a Lambda function.
3. Lambda parses and validates the custom JSON object and then invokes the OpenAI API, passing your api key which is stored as a Lambda environment variable.
4. OpenAI API results are returned as JSON objects.
5. Lambda creates a custom JSON response containing the http response body as well as system information for API Gateway.
6. API Gateway passes through the http response to the client.

You'll find a detailed narrative explanation of the design strategy in this article, [OpenAI API With AWS Lambda](https://blog.lawrencemcdaniel.com/openai-api-with-aws-lambda/)

### Services and Technologies Used

* **[OpenAI](https://pypi.org/project/openai/)**: a PyPi package thata provides convenient access to the OpenAI API from applications written in the Python language. It includes a pre-defined set of classes for API resources that initialize themselves dynamically from API responses which makes it compatible with a wide range of versions of the OpenAI API.
* **[API Gateway](https://aws.amazon.com/api-gateway/)**: an AWS service for creating, publishing, maintaining, monitoring, and securing REST, HTTP, and WebSocket APIs at any scale.
* **[IAM](https://aws.amazon.com/iam/)**: a web service that helps you securely control access to AWS resources. With IAM, you can centrally manage permissions that control which AWS resources users can access. You use IAM to control who is authenticated (signed in) and authorized (has permissions) to use resources.
* **[Lambda](https://aws.amazon.com/lambda/)**: an event-driven, serverless computing platform provided by Amazon as a part of Amazon Web Services. It is a computing service that runs code in response to events and automatically manages the computing resources required by that code. It was introduced on November 13, 2014.
* **[CloudWatch](https://aws.amazon.com/cloudwatch/)**: CloudWatch enables you to monitor your complete stack (applications, infrastructure, network, and services) and use alarms, logs, and events data to take automated actions and reduce mean time to resolution (MTTR).
* **[Route53](https://aws.amazon.com/route53/)**: (OPTIONAL). a scalable and highly available Domain Name System service. Released on December 5, 2010.
* **[Certificate Manager](https://aws.amazon.com/certificate-manager/)**: (OPTIONAL). handles the complexity of creating, storing, and renewing public and private SSL/TLS X.509 certificates and keys that protect your AWS websites and applications.

## OpenAI API

This project leverages the official [OpenAI PyPi](https://pypi.org/project/openai/) Python library. The openai library is added to the AWS Lambda installation package. You can review [terraform/lambda_openai_text.tf](./terraform/lambda_openai_text.tf) to see how this actually happens from a technical perspective.

Other reference materials on how to use this libary:

- [How to Get an OpenAI API Key](./doc/openai-api-key.md)
- [OpenAI Official Example Applications](https://platform.openai.com/examples)
- [OpenAI API Documentation](https://platform.openai.com/docs/api-reference/making-requests?lang=python)
- [OpenAI PyPi](https://pypi.org/project/openai/)
- [OpenAI Python Source](https://github.com/openai/openai-python)
- [OpenAI Official Cookbook](https://github.com/openai/openai-cookbook/)

Be aware that the OpenAI platform API is not free. Moreover, the costing models vary signficantly across the family of OpenAI models. GPT-4 for example cost significantly more to use than GPT-3.5. Having said that, for development purposes, the cost likely will be negligible. I spent a total of around $0.025 USD while developing and testing the initial release of this project, whereupon I invoked the openai api around 200 times (rough guess).

## Trouble Shooting and Logging

The terraform scripts will automatically create a collection of CloudWatch Log Groups. Additionally, note the Terraform global variable 'debug_mode' (defaults to 'true') which will increase the verbosity of log entries in the [Lambda functions](./terraform/python/), which are implemented with Python.

I refined the contents and formatting of each log group to suit my own needs while building this solution, and in particular while coding the Python Lambda functions.

![CloudWatch Logs](https://raw.githubusercontent.com/FullStackWithLawrence/aws-openai/main/doc/cloudwatch-1.png "CloudWatch Logs")
![CloudWatch Logs](https://raw.githubusercontent.com/FullStackWithLawrence/aws-openai/main/doc/cloudwatch-2.png "CloudWatch Logs")

## Documentation

Detailed documentation for each endpoint is available here: [Documentation](./doc/examples/)

## Support

To get community support, go to the official [Issues Page](https://github.com/FullStackWithLawrence/aws-openai/issues) for this project.

## Contributing

We welcome contributions! There are a variety of ways for you to get involved, regardless of your background. In additional to Pull requests, this project would benefit from contributors focused on documentation and how-to video content creation, testing, community engagement, and stewards to help us to ensure that we comply with evolving standards for the ethical use of AI.

You can also contact [Lawrence McDaniel](https://lawrencemcdaniel.com/contact) directly.
