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
  null_slug             = "null"
  null_function_name    = "${var.shared_resource_identifier}_${local.null_slug}"
  null_source_directory = "${path.module}/python/${local.null_function_name}"
  null_package_folder   = "lambda_dist_pkg"
}
data "external" "env_test" {
  # kluge to map .env data to Terraform format
  program = ["${path.module}/scripts/env.sh"]

  # For Windows (or Powershell core on MacOS and Linux),
  # run a Powershell script instead
  #program = ["${path.module}/scripts/env.ps1"]
}

resource "aws_lambda_function" "openai_null" {
  # see https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/lambda_function.html
  # see https://docs.aws.amazon.com/lambda/latest/dg/lambda-runtimes.html
  function_name    = local.null_function_name
  description      = "OpenAI API integrator for text-based inputs"
  role             = aws_iam_role.lambda.arn
  publish          = true
  runtime          = var.lambda_python_runtime
  memory_size      = var.lambda_memory_size
  timeout          = var.lambda_timeout
  handler          = "openai_${local.null_slug}.handler"
  filename         = data.archive_file.openai_null.output_path
  source_code_hash = data.archive_file.openai_null.output_base64sha256
  tags             = var.tags

  environment {
    variables = {
      DEBUG_MODE                 = var.debug_mode
      OPENAI_API_ORGANIZATION    = data.external.env_test.result["OPENAI_API_ORGANIZATION"]
      OPENAI_API_KEY             = data.external.env_test.result["OPENAI_API_KEY"]
      OPENAI_ENDPOINT_IMAGE_N    = var.openai_endpoint_image_n
      OPENAI_ENDPOINT_IMAGE_SIZE = var.openai_endpoint_image_size
    }
  }
}

###############################################################################
# Cloudwatch logging
###############################################################################
resource "aws_cloudwatch_log_group" "openai_test" {
  name              = "/aws/lambda/${local.null_function_name}"
  retention_in_days = var.log_retention_days
  tags              = var.tags
}

###############################################################################
# Python package
# https://alek-cora-glez.medium.com/deploying-aws-lambda-function-with-terraform-custom-dependencies-7874407cd4fc
###############################################################################
data "template_file" "openai_null" {
  template = file("${local.null_source_directory}/openai_null.py")
}
resource "null_resource" "package_openai_null" {
  triggers = {
    redeployment = sha1(jsonencode([
      data.template_file.openai_null.rendered
    ]))
  }

  provisioner "local-exec" {
    interpreter = ["/bin/bash"]
    command     = "${path.module}/scripts/create_pkg.sh"

    environment = {
      source_code_path = local.null_source_directory
      package_folder   = local.null_package_folder
      runtime          = var.lambda_python_runtime
    }
  }
}

data "archive_file" "openai_null" {
  # see https://registry.terraform.io/providers/hashicorp/archive/latest/docs/data-sources/file
  source_dir  = "${local.null_source_directory}/${local.null_package_folder}/"
  output_path = "${local.null_source_directory}/${local.null_package_folder}.zip"
  type        = "zip"
  depends_on  = [null_resource.package_openai_null]
}
