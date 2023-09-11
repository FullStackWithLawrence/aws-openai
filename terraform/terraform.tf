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
    bucket         = "090511222473-tfstate-rekognition"
    key            = "rekognition/terraform.tfstate"
    region         = "us-east-1"
    dynamodb_table = "090511222473-tfstate-lock-rekognition"
    profile        = "lawrence"
    encrypt        = false
  }

  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.8"
    }
  }
}
