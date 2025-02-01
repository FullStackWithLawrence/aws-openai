#------------------------------------------------------------------------------
# written by: Lawrence McDaniel
#             https://lawrencemcdaniel.com/
#
# date:       sep-2023
#
# usage:      override default variable values
#------------------------------------------------------------------------------

###############################################################################
# AWS CLI parameters
###############################################################################
aws_account_id = "090511222473"
tags = {
  "terraform" = "true",
  "project"   = "chatGPT microservice"
  "contact"   = "Lawrence McDaniel - https://lawrencemcdaniel.com/"
}
aws_region  = "us-east-2"
aws_profile = "lawrence"

###############################################################################
# OpenAI API parameters
###############################################################################
openai_endpoint_image_n    = 4
openai_endpoint_image_size = "1024x768"


###############################################################################
# CloudWatch logging parameters
###############################################################################
logging_level = "INFO"


###############################################################################
# APIGateway parameters
###############################################################################
root_domain                = "lawrencemcdaniel.com"
shared_resource_identifier = "openai"
stage                      = "v1"
