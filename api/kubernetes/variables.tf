#------------------------------------------------------------------------------
# written by: Lawrence McDaniel
#             https://lawrencemcdaniel.com/
#
# date:       sep-2023
#
# usage:      all Terraform variable declarations
#------------------------------------------------------------------------------
variable "shared_resource_identifier" {
  description = "A common identifier/prefix for resources created for this demo"
  type        = string
  default     = "openai"
}

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


variable "root_domain" {
  description = "a valid Internet domain name which you directly control using AWS Route53 in this account"
  type        = string
  default     = ""
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
