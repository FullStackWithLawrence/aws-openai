#------------------------------------------------------------------------------
# written by: Lawrence McDaniel
#             https://lawrencemcdaniel.com/
#
# date: sep-2023
#
# usage:  implement a Python Lambda function to search the openai handler
#         for an image uploaded using the REST API endpoint.
#------------------------------------------------------------------------------
locals {
  slug                = "openai"
  index_function_name = "${var.shared_resource_identifier}-${local.slug}"
}
data "external" "env" {
  program = ["${path.module}/env.sh"]

  # For Windows (or Powershell core on MacOS and Linux),
  # run a Powershell script instead
  #program = ["${path.module}/env.ps1"]
}

resource "aws_lambda_function" "openai" {
  # see https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/lambda_function.html
  # see https://docs.aws.amazon.com/lambda/latest/dg/lambda-runtimes.html
  function_name    = local.index_function_name
  description      = "OpenAI calls using text-based inputs"
  role             = aws_iam_role.lambda.arn
  publish          = true
  runtime          = var.lambda_python_runtime
  memory_size      = var.lambda_memory_size
  timeout          = var.lambda_timeout
  handler          = "lambda_handler.handler"
  filename         = data.archive_file.lambda_handler.output_path
  source_code_hash = data.archive_file.lambda_handler.output_base64sha256
  tags             = var.tags

  environment {
    variables = {
      DEBUG_MODE                 = var.debug_mode
      OPENAI_API_ORGANIZATION    = data.external.env.result["OPENAI_API_ORGANIZATION"]
      OPENAI_API_KEY             = data.external.env.result["OPENAI_API_KEY"]
      OPENAI_ENDPOINT_IMAGE_N    = var.openai_endpoint_image_n
      OPENAI_ENDPOINT_IMAGE_SIZE = var.openai_endpoint_image_size
    }
  }
}

# see https://registry.terraform.io/providers/hashicorp/archive/latest/docs/data-sources/file
data "archive_file" "lambda_handler" {
  type = "zip"

  source {
    content  = "${path.module}/python/lambda_${local.slug}.py"
    filename = "lambda_${local.slug}.py"
  }

  source {
    content  = "${path.module}/.venv/lib/python3.11/site-packages/openai"
    filename = "openai"
  }

  output_path = "${path.module}/python/lambda_${local.slug}_payload.zip"
}

###############################################################################
# Cloudwatch logging
###############################################################################
resource "aws_cloudwatch_log_group" "openai" {
  name              = "/aws/lambda/${local.index_function_name}"
  retention_in_days = var.log_retention_days
  tags              = var.tags
}
