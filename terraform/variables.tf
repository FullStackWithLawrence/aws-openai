#------------------------------------------------------------------------------
# written by: Lawrence McDaniel
#             https://lawrencemcdaniel.com/
#
# date:       sep-2023
#
# usage:      all Terraform variable declarations
#------------------------------------------------------------------------------
variable "aws_account_id" {
  description = "12-digit AWS account number"
  type        = string
}
variable "aws_region" {
  description = "A valid AWS data center region code"
  type        = string
  default     = "us-east-1"
}
variable "aws_profile" {
  description = "a valid AWS CLI profile located in $HOME/.aws/credentials"
  type        = string
  default     = "default"
}

variable "debug_mode" {
  type    = bool
  default = false
}
variable "tags" {
  description = "A map of tags to add to all resources. Tags added to launch configuration or templates override these values."
  type        = map(string)
  default     = {}
}

###############################################################################
# OpenAI API parameters
###############################################################################
variable "openai_endpoint_image_n" {
  description = "FIX NOTE: what is this?"
  type        = number
  default     = 4
}
variable "openai_endpoint_image_size" {
  description = "Image output dimensions in pixels"
  type        = string
  default     = "1024x768"
}


variable "create_custom_domain" {
  description = "a valid Internet domain name which you directly control using AWS Route53 in this account"
  type        = bool
  default     = false
}
variable "root_domain" {
  description = "a valid Internet domain name which you directly control using AWS Route53 in this account"
  type        = string
  default     = ""
}

variable "shared_resource_identifier" {
  description = "A common identifier/prefix for resources created for this demo"
  type        = string
  default     = "openai"
}

variable "stage" {
  description = "Examples: dev, staging, prod, v0, v1, etc."
  type        = string
  default     = "v1"
}

variable "logging_level" {
  type    = string
  default = "INFO"
}
variable "log_retention_days" {
  type    = number
  default = 3
}

variable "quota_settings_limit" {
  type    = number
  default = 20
}

variable "quota_settings_offset" {
  type    = number
  default = 2
}

variable "quota_settings_period" {
  type    = string
  default = "WEEK"
}

variable "throttle_settings_burst_limit" {
  type    = number
  default = 5
}
variable "throttle_settings_rate_limit" {
  type    = number
  default = 10
}

variable "lambda_python_runtime" {
  type    = string
  default = "python3.11"
}
variable "lambda_memory_size" {
  description = "Lambda function memory allocations in Mb"
  type        = number
  default     = 256
}

variable "lambda_timeout" {
  description = "Lambda function timeout in seconds"
  type        = number
  default     = 60
}
