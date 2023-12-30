# Technical Overview of this Architecture

![AWS Diagram](https://github.com/FullStackWithLawrence/aws-openai/blob/main/doc/img/aws-diagram.png "AWS Diagram")

- **[IAM](https://aws.amazon.com/iam/)**: a web service that helps you securely control access to AWS resources. With IAM, you can centrally manage permissions that control which AWS resources users can access. You use IAM to control who is authenticated (signed in) and authorized (has permissions) to use resources.
- **[S3](https://aws.amazon.com/s3/)**: Amazon Simple Storage Service is a service offered by Amazon Web Services that provides object storage through a web service interface. Amazon S3 uses the same scalable storage infrastructure that Amazon.com uses to run its e-commerce network.
- **[Lambda](https://aws.amazon.com/lambda/)**: an event-driven, serverless computing platform provided by Amazon as a part of Amazon Web Services. It is a computing service that runs code in response to events and automatically manages the computing resources required by that code. It was introduced on November 13, 2014.
- **[API Gateway](https://aws.amazon.com/api-gateway/)**: an AWS service for creating, publishing, maintaining, monitoring, and securing REST, HTTP, and WebSocket APIs at any scale.
- **[Certificate Manager](https://aws.amazon.com/certificate-manager/)**: handles the complexity of creating, storing, and renewing public and private SSL/TLS X.509 certificates and keys that protect your AWS websites and applications.
- **[Route53](https://aws.amazon.com/route53/)**: a scalable and highly available Domain Name System service. Released on December 5, 2010.
- **[CloudWatch](https://aws.amazon.com/cloudwatch/)**: CloudWatch enables you to monitor your complete stack (applications, infrastructure, network, and services) and use alarms, logs, and events data to take automated actions and reduce mean time to resolution (MTTR).

## Lambda Functions

These lambdas are designed to work exclusively as back ends for an AWS API Gateway end point resource. PyPi dependencies for these Lambdas are stored in this [AWS Lambda Layer](../api/terraform/python/layer_genai/). Additionally, a locally sourced package named [common](../api/terraform/python/openai_api/common/) is a shared code library used by all Lambdas in this project.

### OpenAI Lambda

Accepts a JSON event with a schema matching the input parameters found in each of the OpenAI API [example application code snippets](https://platform.openai.com/examples/default-grammar/).

### LangChain Lambda

Accepts a simplified JSON schema matching the [LangChain](https://www.langchain.com/) documentation.

## Trouble Shooting and Logging

The terraform scripts will automatically create a collection of CloudWatch Log Groups. Additionally, note the Terraform global variable 'debug_mode' (defaults to 'true') which will increase the verbosity of log entries in the [Lambda functions](./terraform/python/), which are implemented with Python.

I refined the contents and formatting of each log group to suit my own needs while building this solution, and in particular while coding the Python Lambda functions.

![CloudWatch Logs](https://github.com/FullStackWithLawrence/aws-openai/blob/main/doc/img/cloudwatch-1.png "CloudWatch Logs")
![CloudWatch Logs](https://github.com/FullStackWithLawrence/aws-openai/blob/main/doc/img/cloudwatch-2.png "CloudWatch Logs")
