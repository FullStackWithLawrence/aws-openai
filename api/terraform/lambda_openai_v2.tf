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
  openai_v2_build_path        = "${path.module}/build/distribution_package"
  openai_v2_source_directory  = "${path.module}/python/openai_api"
  openai_v2_packaging_script  = "${local.openai_v2_source_directory}/create_pkg.sh"
  openai_v2_dist_package_name = "${local.openai_v2_function_name}_dist_pkg.zip"
}

###############################################################################
# Python package
# https://alek-cora-glez.medium.com/deploying-aws-lambda-function-with-terraform-custom-dependencies-7874407cd4fc
###############################################################################
resource "null_resource" "package_lambda_openai_v2" {
  triggers = {
    always_redeploy = timestamp()
  }

  provisioner "local-exec" {
    interpreter = ["/bin/bash"]
    command     = local.openai_v2_packaging_script

    environment = {
      TERRAFORM_ROOT   = path.module
      SOURCE_CODE_PATH = local.openai_v2_source_directory
      BUILD_PATH       = local.openai_v2_build_path
      PACKAGE_FOLDER   = local.openai_v2_function_name
    }
  }
}

data "archive_file" "lambda_openai_v2" {
  # see https://registry.terraform.io/providers/hashicorp/archive/latest/docs/data-sources/file
  source_dir  = local.openai_v2_build_path
  output_path = "${path.module}/build/${local.openai_v2_dist_package_name}"
  type        = "zip"
  depends_on  = [null_resource.package_lambda_openai_v2]
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

###############################################################################
# AWS Lambda function
###############################################################################
resource "aws_lambda_function" "lambda_openai_v2" {
  # see https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/lambda_function.html
  # see https://docs.aws.amazon.com/lambda/latest/dg/lambda-runtimes.html
  function_name    = local.openai_v2_function_name
  description      = "LangChain request handler"
  role             = aws_iam_role.lambda.arn
  publish          = true
  runtime          = var.lambda_python_runtime
  memory_size      = var.lambda_memory_size
  timeout          = var.lambda_timeout
  handler          = "openai_api.lambda_openai_v2.lambda_handler.handler"
  architectures    = var.compatible_architectures
  filename         = data.archive_file.lambda_openai_v2.output_path
  source_code_hash = data.archive_file.lambda_openai_v2.output_base64sha256
  layers           = [aws_lambda_layer_version.openai.arn]
  tags             = var.tags

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
}

###############################################################################
# Cloudwatch logging
###############################################################################
resource "aws_cloudwatch_log_group" "lambda_openai_v2" {
  name              = "/aws/lambda/${local.openai_v2_function_name}"
  retention_in_days = var.log_retention_days
  tags              = var.tags
}
