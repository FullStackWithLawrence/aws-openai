#------------------------------------------------------------------------------
# written by: Lawrence McDaniel
#             https://lawrencemcdaniel.com/
#
# date: sep-2023
#
# usage:  - implement a Python Lambda function to create a 'faceprint' of an image
#           triggered by uploading the image to the S3 bucket
#
#         - implement role-based security for both Lambda functions.
#------------------------------------------------------------------------------
locals {
  search_function_name = "${var.shared_resource_identifier}-binary"
}

resource "aws_lambda_function" "binary" {

  # see https://docs.aws.amazon.com/lambda/latest/dg/lambda-runtimes.html
  function_name    = local.search_function_name
  description      = "Facial recognition image analysis and search for indexed faces. invoked by API Gateway."
  role             = aws_iam_role.lambda.arn
  publish          = true
  runtime          = var.lambda_python_runtime
  memory_size      = var.lambda_memory_size
  timeout          = var.lambda_timeout
  handler          = "lambda_search.handler"
  filename         = data.archive_file.lambda_search.output_path
  source_code_hash = data.archive_file.lambda_search.output_base64sha256
  tags             = var.tags

  environment {
    variables = {
      DEBUG_MODE             = var.debug_mode
      MAX_FACES_COUNT        = var.max_faces_count
      FACE_DETECT_THRESHOLD  = var.face_detect_threshold
      QUALITY_FILTER         = var.face_detect_quality_filter
      FACE_DETECT_ATTRIBUTES = var.face_detect_attributes
      TABLE_ID               = local.table_name
      REGION                 = var.aws_region
      COLLECTION_ID          = local.collection_id
    }
  }
}

###############################################################################
# Lambda binary
###############################################################################
# see https://registry.terraform.io/providers/hashicorp/archive/latest/docs/data-sources/file
data "archive_file" "lambda_search" {
  type        = "zip"
  source_file = "${path.module}/python/lambda_search.py"

  # boto3 pip package
  source {
    content = "${path.module}/.venv/lib/python3.11/site-packages/boto3"
    filename = "boto3"
  }

  # openai pip package
  source {
    content = "${path.module}/.venv/lib/python3.11/site-packages/openai"
    filename = "openai"
  }
  output_path = "${path.module}/python/lambda_search_payload.zip"
}

###############################################################################
# Cloudwatch logging
###############################################################################
resource "aws_cloudwatch_log_group" "binary" {
  name              = "/aws/lambda/${local.search_function_name}"
  retention_in_days = var.log_retention_days
  tags              = var.tags
}
