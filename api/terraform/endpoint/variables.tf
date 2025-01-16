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

variable "aws_api_gateway_rest_api_parent_id" {
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
variable "mapping_object_type" {
  description = "OpenAI Python API class to invoke."
  type        = string
  default     = "chat.completion"

}
variable "mapping_model" {
  # see https://platform.openai.com/docs/models/overview
  description = "which OpenAI model to use"
  type        = string
  default     = "gpt-4-turbo"
}
variable "mapping_end_point" {
  description = "OpenAI Python API class to invoke."
  type        = string
  default     = "ChatCompletion"
}

variable "mapping_role_system_content" {
  description = "value"
  type        = string
  default     = ""
}

variable "mapping_temperature" {
  description = "a number between 0 and 2, with a default value of 1 or 0.7 depending on the model you choose. The temperature is used to control the randomness of the output."
  type        = number
  default     = 1
}

variable "mapping_max_tokens" {
  description = "the max tokens for a single prompt"
  type        = number
  default     = 4096
}
