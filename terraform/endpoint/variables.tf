variable "aws_region" {
  description = "AWS data center where API Gateway resources are deployed."
  type        = string
  default     = "us-east-1"
}

variable "path_part" {
  description = "URL endpoint"
  type        = string
  default     = "default-grammar"
}

variable "aws_api_gateway_rest_api_root_resource_id" {
  description = "root resource id of API gateway api"
  type        = string
}

variable "aws_api_gateway_rest_api_id" {
  description = "id of API gateway api"
  type        = string
}

variable "aws_lambda_function_openai_text_invoke_arn" {
  description = "ARN of lambda function to manage OpenAI API request"
  type        = string
}

variable "aws_lambda_function_openai_text" {
  description = "Name of Lambda function to manage OpenAI API request"
  type        = string
}

variable "aws_iam_role_arn" {
  description = "ARN of API Gateway IAM role providing Lambda execution privileges"
  type        = string
}

###############################################################################
# OpenAI mapping template
###############################################################################
variable "mapping_end_point" {
  description = "OpenAI Python API class to invoke."
  type        = string
  default     = "ChatCompletion"
}

variable "mapping_role_system_content" {
  description = "value"
  type        = string
  default     = "You will be provided with statements, and your task is to convert them to standard English."
}
