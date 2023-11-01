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
  openai_function_name     = "lambda_${var.shared_resource_identifier}"
  openai_source_directory  = "${path.module}/python/${local.openai_function_name}"
  openai_packaging_script  = "${local.openai_source_directory}/create_pkg.sh"
  openai_package_folder    = "lambda_dist_pkg"
  openai_dist_package_name = "lambda_dist_pkg"
}

###############################################################################
# Python package
# https://alek-cora-glez.medium.com/deploying-aws-lambda-function-with-terraform-custom-dependencies-7874407cd4fc
###############################################################################
resource "null_resource" "package_lambda_openai" {
  triggers = {
    redeployment = sha1(jsonencode([
      file("${local.openai_source_directory}/lambda_handler.py"),
      file("${local.openai_source_directory}/requirements.txt"),
      file("${local.openai_packaging_script}")
    ]))
  }

  provisioner "local-exec" {
    interpreter = ["/bin/bash"]
    command     = local.openai_packaging_script

    environment = {
      PACKAGE_NAME     = local.openai_function_name
      SOURCE_CODE_PATH = local.openai_source_directory
      PACKAGE_FOLDER   = local.openai_package_folder
      RUNTIME          = var.lambda_python_runtime
    }
  }
}

data "archive_file" "lambda_openai" {
  # see https://registry.terraform.io/providers/hashicorp/archive/latest/docs/data-sources/file
  source_dir  = "${local.openai_source_directory}/${local.openai_package_folder}/"
  output_path = "${local.openai_source_directory}/${local.openai_dist_package_name}.zip"
  type        = "zip"
  depends_on  = [null_resource.package_lambda_openai]
}

###############################################################################
# OpenAI API key and organization
###############################################################################
data "external" "env_lambda_openai" {
  # kluge to read and map the openai api key and org data contained in .env
  program = ["${local.openai_source_directory}/env.sh"]

  # For Windows (or Powershell core on MacOS and Linux),
  # run a Powershell script instead
  #program = ["${path.module}/scripts/env.ps1"]
}

###############################################################################
# AWS Lambda function
###############################################################################
resource "aws_lambda_function" "lambda_openai" {
  # see https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/lambda_function.html
  # see https://docs.aws.amazon.com/lambda/latest/dg/lambda-runtimes.html
  function_name    = local.openai_function_name
  description      = "OpenAI API request handler"
  role             = aws_iam_role.lambda.arn
  publish          = true
  runtime          = var.lambda_python_runtime
  memory_size      = var.lambda_memory_size
  timeout          = var.lambda_timeout
  handler          = "lambda_handler.handler"
  filename         = data.archive_file.lambda_openai.output_path
  source_code_hash = data.archive_file.lambda_openai.output_base64sha256
  tags             = var.tags

  environment {
    variables = {
      DEBUG_MODE                 = var.debug_mode
      OPENAI_API_ORGANIZATION    = data.external.env_lambda_openai.result["OPENAI_API_ORGANIZATION"]
      OPENAI_API_KEY             = data.external.env_lambda_openai.result["OPENAI_API_KEY"]
      OPENAI_ENDPOINT_IMAGE_N    = var.openai_endpoint_image_n
      OPENAI_ENDPOINT_IMAGE_SIZE = var.openai_endpoint_image_size
    }
  }
}

###############################################################################
# Cloudwatch logging
###############################################################################
resource "aws_cloudwatch_log_group" "lambda_openai" {
  name              = "/aws/lambda/${local.openai_function_name}"
  retention_in_days = var.log_retention_days
  tags              = var.tags
}
