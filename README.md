[![OpenAI](https://a11ybadges.com/badge?logo=openai)](https://platform.openai.com/)
[![AWS](https://img.shields.io/badge/AWS-%23FF9900.svg?style=for-the-badge&logo=amazon-aws&logoColor=white)](https://aws.amazon.com/)
[![hack.d Lawrence McDaniel](https://img.shields.io/badge/hack.d-Lawrence%20McDaniel-orange.svg)](https://lawrencemcdaniel.com)

# OpenAI REST API Microservice

A REST API implementing every [OpenAI Example Application](https://platform.openai.com/examples). Implemented as a serverless microservice using AWS cloud resources. Leverages OpenAI's suite of AI models, including [GTP-4](https://platform.openai.com/docs/models/gpt-4), [DALL·E](https://platform.openai.com/docs/models/dall-e), [Whisper](https://platform.openai.com/docs/models/whisper), [Embeddings](https://platform.openai.com/docs/models/embeddings), and [Moderation](https://platform.openai.com/docs/models/moderation).

![OpenAI Examples](https://raw.githubusercontent.com/FullStackWithLawrence/aws-openai/main/doc/openai-examples.png "OpenAI Examples")

## Usage

1. clone this repo and setup a Python virtual environment.

```shell
git clone https://github.com/FullStackWithLawrence/aws-openai.git
cd aws-openai
make init
```

The Python virtual environment serves two purposes. When developing, it will allow you the convenience of auto-complete for code objects from the Boto3 and OpenAI Python libraries. But more importantly, the Terraform resource `aws_lambda_function` requires a complete code package in zip format, including any third party libraries. Hence, the references to these two libraries in [terraform/lambda_text.tf](./terraform/lambda_text.tf) and [terraform/lambda_binary.tf](./terraform/lambda_binary.tf).


2. configure Terraform for your AWS account. Set these three values in [terraform.tfvars](./terraform/terraform.tfvars):

```terraform
account_id           = "012345678912"   # Required: your 12-digit AWS account number
aws_region           = "us-east-1"      # Optional: an AWS data center
aws_profile          = "default"        # Optional: for aws cli credentials
```

3. Build and deploy the microservice

```terraform
terraform init
terraform apply
```

Note the output variables for your API Gateway root URL and API key.

4. Use your REST API endpoints


## Architecture

- **[OpenAI](https://pypi.org/project/openai/)**: a PyPi package thata provides convenient access to the OpenAI API from applications written in the Python language. It includes a pre-defined set of classes for API resources that initialize themselves dynamically from API responses which makes it compatible with a wide range of versions of the OpenAI API.
- **[API Gateway](https://aws.amazon.com/api-gateway/)**: an AWS service for creating, publishing, maintaining, monitoring, and securing REST, HTTP, and WebSocket APIs at any scale.
- **[IAM](https://aws.amazon.com/iam/)**: a web service that helps you securely control access to AWS resources. With IAM, you can centrally manage permissions that control which AWS resources users can access. You use IAM to control who is authenticated (signed in) and authorized (has permissions) to use resources.
- **[Lambda](https://aws.amazon.com/lambda/)**: an event-driven, serverless computing platform provided by Amazon as a part of Amazon Web Services. It is a computing service that runs code in response to events and automatically manages the computing resources required by that code. It was introduced on November 13, 2014.
- **[CloudWatch](https://aws.amazon.com/cloudwatch/)**: CloudWatch enables you to monitor your complete stack (applications, infrastructure, network, and services) and use alarms, logs, and events data to take automated actions and reduce mean time to resolution (MTTR).
- **[Certificate Manager](https://aws.amazon.com/certificate-manager/)**: handles the complexity of creating, storing, and renewing public and private SSL/TLS X.509 certificates and keys that protect your AWS websites and applications.
- **[Route53](https://aws.amazon.com/route53/)**: a scalable and highly available Domain Name System service. Released on December 5, 2010.

## Trouble Shooting and Logging

The terraform scripts will automatically create a collection of CloudWatch Log Groups. Additionally, note the Terraform global variable 'debug_mode' (defaults to 'true') which will increase the verbosity of log entries in the [Lambda functions](./terraform/python/), which are implemented with Python.

I refined the contents and formatting of each log group to suit my own needs while building this solution, and in particular while coding the Python Lambda functions.

![CloudWatch Logs](https://raw.githubusercontent.com/FullStackWithLawrence/aws-openai/main/doc/cloudwatch-1.png "CloudWatch Logs")
![CloudWatch Logs](https://raw.githubusercontent.com/FullStackWithLawrence/aws-openai/main/doc/cloudwatch-2.png "CloudWatch Logs")

## Getting Started With AWS and Terraform

This is a [Terraform](https://www.terraform.io/) based installation methodology that reliably automates the complete build, management and destruction processes of all resources. [Terraform](https://www.terraform.io/) is an [infrastructure-as-code](https://en.wikipedia.org/wiki/Infrastructure_as_code) command line tool that will create and configure all of the approximately two dozen software and cloud infrastructure resources that are needed for running the service on AWS infrastructure. These Terraform scripts will install and configure all cloud infrastructure resources and system software on which the service depends. This process will take around 2 minutes to complete and will generate copious amounts of console output.

The service stack consists of the following:

* AWS S3 bucket and DynamoDB table for managing Terraform state
* [AWS S3 bucket](https://aws.amazon.com/s3/) for storing train and test image sets.
* [DynamoDB Table](https://aws.amazon.com/dynamodb/) for persisting openai service results
* [AWS IAM Role](https://aws.amazon.com/iam/) for managing service-level role-based security for this service

**WARNINGS**:

**1. Terraform will create many AWS resources in other parts of your AWS account including API Gateway, IAM, DynamoDB, CloudWatch and Lambda. You should not directly modify any of these resources, as this could lead to unintended consequences in the safe operation of your microservice.**

**2. Terraform is a memory intensive application. For best results you should run this on a computer with at least 4Gib of free memory.**

## I. Installation Prerequisites

For Linux & macOS operating systems.

**Prerequisite:** An [AWS IAM User](https://aws.amazon.com/iam/) with administrator priviledges, access key and secret key.

Ensure that your environment includes the latest stable releases of the following software packages:

* [aws cli](https://aws.amazon.com/cli/)
* [terraform](https://www.terraform.io/)

### Install required software packages using Homebrew

If necessary, install [Homebrew](https://brew.sh/)

```console
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
echo 'eval "$(/home/linuxbrew/.linuxbrew/bin/brew shellenv)"' >> /home/ubuntu/.profile
eval "$(/home/linuxbrew/.linuxbrew/bin/brew shellenv)"
```

Use homebrew to install all required packages.

```console
brew install awscli terraform
```

### Configure the AWS CLI

To configure the AWS CLI run the following command:

```console
aws configure
```

This will interactively prompt for your AWS IAM user access key, secret key and preferred region.


### Setup Terraform

Terraform is a declarative open-source infrastructure-as-code software tool created by HashiCorp. This repo leverages Terraform to create all cloud infrastructure as well as to install and configure all software packages that run inside of Kubernetes. Terraform relies on an S3 bucket for storing its state data, and a DynamoDB table for managing a semaphore lock during operations.

Use these three environment variables for creating the uniquely named resources that the Terraform modules in this repo will be expecting to find at run-time.

**IMPORTANT: these three settings should be consistent with the values your set in terraform.tfvars in the next section.**

```console
AWS_ACCOUNT=012345678912      # add your 12-digit AWS account number here
AWS_REGION=us-east-1          # any valid AWS region code.
AWS_ENVIRONMENT=openai   # any valid string. Keep it short -- 3 characters is ideal.
```

First create an AWS S3 Bucket

```console
AWS_S3_BUCKET="${AWS_ACCOUNT}-tfstate-${AWS_ENVIRONMENT}"

# for buckets created in us-east-1
aws s3api create-bucket --bucket $AWS_S3_BUCKET --region $AWS_REGION

# for all other regions
aws s3api create-bucket --bucket $AWS_S3_BUCKET --region $AWS_REGION --create-bucket-configuration LocationConstraint=$AWS_REGION
```

Then create a DynamoDB table

```console
AWS_DYNAMODB_TABLE="${AWS_ACCOUNT}-tfstate-lock-${AWS_ENVIRONMENT}"
aws dynamodb create-table --region $AWS_REGION --table-name $AWS_DYNAMODB_TABLE  \
               --attribute-definitions AttributeName=LockID,AttributeType=S  \
               --key-schema AttributeName=LockID,KeyType=HASH --provisioned-throughput  \
               ReadCapacityUnits=1,WriteCapacityUnits=1
```

## II. Build and Deploy

### Step 1. Checkout the repository

```console
git clone https://github.com/FullStackWithLawrence/aws-openai.git
```

### Step 2. Configure your Terraform backend

Edit the following snippet so that bucket, region and dynamodb_table are consistent with your values of $AWS_REGION, $AWS_S3_BUCKET, $AWS_DYNAMODB_TABLE

```console
vim terraform/terraform.tf
```

```terraform
  backend "s3" {
    bucket         = "012345678912-tfstate-openai"
    key            = "openai/terraform.tfstate"
    region         = "us-east-1"
    dynamodb_table = "012345678912-tfstate-lock-openai"
    profile        = "default"
    encrypt        = false
  }
````

### Step 4. Configure your environment by setting Terraform global variable values

```console
vim terraform/terraform.tfvars
```

Required inputs are as follows:

```terraform
account_id           = "012345678912"
aws_region           = "us-east-1"
aws_profile          = "default"
```


### Step 3. Run the following command to initialize and build the solution

The Terraform modules in this repo rely extensively on calls to other third party Terraform modules published and maintained by [AWS](https://registry.terraform.io/namespaces/terraform-aws-modules). These modules will be downloaded by Terraform so that these can be executed locally from your computer. Noteworth examples of such third party modules include:

* [terraform-aws-modules/s3](https://registry.terraform.io/modules/terraform-aws-modules/s3-bucket/aws/latest)
* [terraform-aws-modules/dynamodb](https://registry.terraform.io/modules/terraform-aws-modules/dynamodb-table/aws/latest)

```console
cd terraform
terraform init
```

Screen output should resemble the following:
![Terraform init](https://raw.githubusercontent.com/FullStackWithLawrence/aws-openai/main/doc/terraform-init.png "Terraform init")

```console
terraform plan
```

Screen output should resemble the following:
![Terraform plan](https://raw.githubusercontent.com/FullStackWithLawrence/aws-openai/main/doc/terraform-plan.png "Terraform plan")

To deploy the service run the following

```console
terraform apply
```

![Terraform apply](https://raw.githubusercontent.com/FullStackWithLawrence/aws-openai/main/doc/terraform-apply2.png "Terraform apply")

## III. Uninstall

The following completely destroys all AWS resources. Note that this operation might take up to 20 minutes to complete.

```console
cd terraform
terraform init
terraform destroy
```

Delete Terraform state management resources

```console
AWS_ACCOUNT=012345678912      # add your 12-digit AWS account number here
AWS_REGION=us-east-1
AWS_ENVIRONMENT=openai   # any valid string. Keep it short
AWS_S3_BUCKET="${AWS_ACCOUNT}-tfstate-${AWS_ENVIRONMENT}"
AWS_DYNAMODB_TABLE="${AWS_ACCOUNT}-tfstate-lock-${AWS_ENVIRONMENT}"
```

To delete the DynamoDB table

```console
aws dynamodb delete-table --region $AWS_REGION --table-name $AWS_DYNAMODB_TABLE
```

To delete the AWS S3 bucket

```console
aws s3 rm s3://$AWS_S3_BUCKET --recursive
aws s3 rb s3://$AWS_S3_BUCKET --force
```
