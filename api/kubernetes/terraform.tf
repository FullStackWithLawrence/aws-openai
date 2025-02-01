#------------------------------------------------------------------------------
# written by: Lawrence McDaniel
#             https://lawrencemcdaniel.com/
#
# date:       July-2023
#
# usage:      Terraform configuration
#------------------------------------------------------------------------------

terraform {
  required_version = "~> 1.5"
  backend "s3" {
    bucket         = "090511222473-tfstate-openai"
    key            = "chat_api/terraform.tfstate"
    region         = "us-east-1"
    dynamodb_table = "090511222473-tfstate-lock-openai"
    profile        = "lawrence"
    encrypt        = false
  }

  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.35"
    }
    null = {
      source  = "hashicorp/null"
      version = "~> 3.2"
    }
    kubernetes = {
      source  = "hashicorp/kubernetes"
      version = "~> 2.25"
    }
  }
}
