#------------------------------------------------------------------------------
# written by: Lawrence McDaniel
#             https://lawrencemcdaniel.com/
#
# date:   sep-2023
#
# usage:  implement a Python Lambda function to to format and pass
#         text-based http requests directly to OpenAI API.
#         - create a Lambda zip archive
#         - pass openai api key credentials to Lambda in a safe manner
#         - create a Cloudwatch log for the Lambda
#         * note that IAM permissions are implemented on the resource(s)
#           that call this Lambda, rather than here.
#------------------------------------------------------------------------------
locals {
  openai_v2_function_name     = "lambda_openai_v2"
  openai_v2_source_directory  = "${path.module}/python/openai_api"
}



###############################################################################
# OpenAI API key and organization
###############################################################################
data "external" "env_lambda_openai_v2" {
  # kluge to read and map the openai api key and org data contained in .env
  program = ["${local.openai_v2_source_directory}/${local.openai_v2_function_name}/env.sh"]

  # For Windows (or Powershell core on MacOS and Linux),
  # run a Powershell script instead
  #program = ["${path.module}/scripts/env.ps1"]
}



data "aws_ecr_image" "lambda_image" {
  repository_name = aws_ecr_repository.lambda_repo.name

  most_recent = true

  depends_on = [null_resource.build_and_push]
}

###############################################################################
# AWS Lambda function
###############################################################################
resource "aws_lambda_function" "lambda_openai_v2" {
  function_name = local.openai_v2_function_name
  role          = aws_iam_role.lambda.arn

  package_type = "Image"
  image_uri = "${aws_ecr_repository.lambda_repo.repository_url}@${data.aws_ecr_image.lambda_image.image_digest}"

  memory_size = var.lambda_memory_size
  timeout     = var.lambda_timeout

  architectures = var.compatible_architectures
  publish       = true

  environment {
    variables = {
      DEBUG_MODE                 = var.debug_mode
      OPENAI_API_ORGANIZATION    = data.external.env_lambda_openai_v2.result["OPENAI_API_ORGANIZATION"]
      OPENAI_API_KEY             = data.external.env_lambda_openai_v2.result["OPENAI_API_KEY"]
      OPENAI_ENDPOINT_IMAGE_N    = var.openai_endpoint_image_n
      OPENAI_ENDPOINT_IMAGE_SIZE = var.openai_endpoint_image_size
      AWS_DEPLOYED               = true
    }
  }

  depends_on = [null_resource.build_and_push]
}

###############################################################################
# Cloudwatch logging
###############################################################################
resource "aws_cloudwatch_log_group" "lambda_openai_v2" {
  name              = "/aws/lambda/${local.openai_v2_function_name}"
  retention_in_days = var.log_retention_days
  tags              = var.tags
}
