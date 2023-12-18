#------------------------------------------------------------------------------
# written by: Lawrence McDaniel
#             https://lawrencemcdaniel.com/
#
# date:   sep-2023
#
# usage:  implement a Python Lambda function to to format and pass
#         text-based http requests to OpenAI API.
#         - create a Lambda zip archive which includes openai PyPi package
#         - pass openai api key credentials to Lambda in a safe manner
#         - create a Cloudwatch log for the Lambda
#         * note that IAM permissions are implemented on the resource(s)
#           that call this Lambda, rather than here.
#------------------------------------------------------------------------------
locals {
  preflight_slug             = "cors_preflight_handler"
  preflight_build_path       = "${path.module}/build/"
  preflight_function_name    = "${var.shared_resource_identifier}_${local.preflight_slug}"
  preflight_source_directory = "${path.module}/nodejs/${local.preflight_function_name}"
  preflight_package_file     = "lambda_${local.preflight_slug}_dist_pkg"
}

resource "aws_lambda_function" "cors_preflight_handler" {
  # see https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/lambda_function.html
  # see https://docs.aws.amazon.com/lambda/latest/dg/lambda-runtimes.html
  function_name    = local.preflight_function_name
  description      = "CORS preflight handler for OpenAI API"
  role             = aws_iam_role.lambda.arn
  publish          = true
  runtime          = var.lambda_nodejs_runtime
  memory_size      = var.lambda_memory_size
  timeout          = var.lambda_timeout
  handler          = "index.handler"
  filename         = data.archive_file.cors_preflight_handler.output_path
  source_code_hash = data.archive_file.cors_preflight_handler.output_base64sha256
  tags             = var.tags
}

###############################################################################
# Python package
# https://alek-cora-glez.medium.com/deploying-aws-lambda-function-with-terraform-custom-dependencies-7874407cd4fc
###############################################################################

data "archive_file" "cors_preflight_handler" {
  # see https://registry.terraform.io/providers/hashicorp/archive/latest/docs/data-sources/file
  source_dir  = "${local.preflight_source_directory}/"
  output_path = "${local.preflight_build_path}/${local.preflight_package_file}.zip"
  type        = "zip"
}

###############################################################################
# Cloudwatch logging
###############################################################################
resource "aws_cloudwatch_log_group" "cors_preflight_handler" {
  name              = "/aws/lambda/${local.preflight_function_name}"
  retention_in_days = var.log_retention_days
  tags              = var.tags
}
