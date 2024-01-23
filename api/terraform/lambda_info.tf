#------------------------------------------------------------------------------
# written by: Lawrence McDaniel
#             https://lawrencemcdaniel.com/
#
# date: dec-2023
#
# usage:  - implement a Python Lambda function to create a dump of the
#           configuration settings for the facial recognition system.
#------------------------------------------------------------------------------
locals {
  info_function_name = "lambda_${var.shared_resource_identifier}_info"

  info_build_path        = "${path.module}/build/distribution_package"
  info_source_directory  = "${path.module}/python/openai_api"
  info_packaging_script  = "${local.info_source_directory}/create_pkg.sh"
  info_dist_package_name = "${local.info_function_name}_dist_pkg.zip"

}


###############################################################################
# Cloudwatch logging
###############################################################################
resource "aws_cloudwatch_log_group" "info" {
  name              = "/aws/lambda/${local.info_function_name}"
  retention_in_days = var.log_retention_days
  tags              = var.tags
}


###############################################################################
# Python package
# https://alek-cora-glez.medium.com/deploying-aws-lambda-function-with-terraform-custom-dependencies-7874407cd4fc
###############################################################################
resource "null_resource" "package_lambda_info" {
  triggers = {
    always_redeploy = timestamp()
  }

  provisioner "local-exec" {
    interpreter = ["/bin/bash"]
    command     = local.info_packaging_script

    environment = {
      TERRAFORM_ROOT   = path.module
      SOURCE_CODE_PATH = local.info_source_directory
      BUILD_PATH       = local.info_build_path
      PACKAGE_FOLDER   = local.info_function_name
    }
  }
}

# see https://registry.terraform.io/providers/hashicorp/archive/latest/docs/data-sources/file
data "archive_file" "lambda_info" {
  source_dir  = local.info_build_path
  output_path = "${path.module}/build/${local.info_dist_package_name}"
  type        = "zip"
  depends_on  = [null_resource.package_lambda_info]

}

resource "aws_lambda_function" "info" {

  # see https://docs.aws.amazon.com/lambda/latest/dg/lambda-runtimes.html
  function_name    = local.info_function_name
  description      = "OpenAI API configuration settings. invoked by API Gateway."
  role             = aws_iam_role.lambda.arn
  publish          = true
  runtime          = var.lambda_python_runtime
  memory_size      = var.lambda_memory_size
  timeout          = var.lambda_timeout
  handler          = "openai_api.lambda_info.lambda_handler.handler"
  filename         = data.archive_file.lambda_info.output_path
  source_code_hash = data.archive_file.lambda_info.output_base64sha256
  layers           = [aws_lambda_layer_version.openai.arn]
  tags             = var.tags

  environment {
    variables = {
      DEBUG_MODE   = var.debug_mode
      AWS_DEPLOYED = true
    }
  }
}
