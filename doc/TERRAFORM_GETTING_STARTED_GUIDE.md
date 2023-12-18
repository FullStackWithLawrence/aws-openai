# Getting Started With AWS and Terraform

This is a [Terraform](https://www.terraform.io/) based installation methodology that reliably automates the complete build, management and destruction processes of all resources. [Terraform](https://www.terraform.io/) is an [infrastructure-as-code](https://en.wikipedia.org/wiki/Infrastructure_as_code) command line tool that will create and configure all of the approximately two dozen software and cloud infrastructure resources that are needed for running the service on AWS infrastructure. These Terraform scripts will install and configure all cloud infrastructure resources and system software on which the service depends. This process will take around 2 minutes to complete and will generate copious amounts of console output.

Terraform depends on the following resources:

- [AWS S3 bucket](https://aws.amazon.com/s3/) for managing Terraform state
- [DynamoDB Table](https://aws.amazon.com/dynamodb/) for managing Terraform locks
- [AWS IAM Role](https://aws.amazon.com/iam/) for managing service-level role-based security for this service

**WARNINGS**:

**1. Terraform will create many AWS resources in other parts of your AWS account including API Gateway, IAM, DynamoDB, CloudWatch and Lambda. You should not directly modify any of these resources, as this could lead to unintended consequences in the safe operation of your microservice.**

**2. Terraform is a memory intensive application. For best results you should run this on a computer with at least 4Gib of free memory.**

## I. Installation Prerequisites

For Linux & macOS operating systems.

**Prerequisite:** An [AWS IAM User](https://aws.amazon.com/iam/) with administrator privileges, access key and secret key.

Ensure that your environment includes the latest stable releases of the following software packages:

- [aws cli](https://aws.amazon.com/cli/)
- [terraform](https://www.terraform.io/)

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
AWS_ENVIRONMENT=openai        # any valid string. Keep it short -- 3 characters is ideal.
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
```

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

- [terraform-aws-modules/s3](https://registry.terraform.io/modules/terraform-aws-modules/s3-bucket/aws/latest)
- [terraform-aws-modules/dynamodb](https://registry.terraform.io/modules/terraform-aws-modules/dynamodb-table/aws/latest)

```console
cd terraform
terraform init
```

Screen output should resemble the following:
![Terraform init](https://raw.githubusercontent.com/FullStackWithLawrence/aws-openai/main/doc/img/terraform-init.png "Terraform init")

```console
terraform plan
```

Screen output should resemble the following:
![Terraform Plan](https://raw.githubusercontent.com/FullStackWithLawrence/aws-openai/main/doc/img/terraform-apply1.png "Terraform Plan")

To deploy the service run the following

```console
terraform apply
```

![Terraform Apply](https://raw.githubusercontent.com/FullStackWithLawrence/aws-openai/main/doc/img/terraform-apply2.png "Terraform Apply")

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
