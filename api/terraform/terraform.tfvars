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
aws_region = "us-east-1"
aws_profile = "lawrence"

###############################################################################
# OpenAI API parameters
###############################################################################
openai_endpoint_image_n    = 4
openai_endpoint_image_size = "1024x768"


###############################################################################
# Lambda parameters
###############################################################################
lambda_python_runtime = "python3.11"
debug_mode            = true
lambda_memory_size    = 256
lambda_timeout        = 600

###############################################################################
# CloudWatch logging parameters
###############################################################################
logging_level      = "INFO"
log_retention_days = 3


###############################################################################
# APIGateway parameters
###############################################################################
create_custom_domain       = true
root_domain                = "lawrencemcdaniel.com"
shared_resource_identifier = "openai"
stage                      = "v1"

# Maximum number of requests that can be made in a given time period.
quota_settings_limit = 500

# Number of requests subtracted from the given limit in the initial time period.
quota_settings_offset = 0

# Time period in which the limit applies. Valid values are "DAY", "WEEK" or "MONTH".
quota_settings_period = "DAY"

# The API request burst limit, the maximum rate limit over a time ranging from one to a few seconds,
# depending upon whether the underlying token bucket is at its full capacity.
throttle_settings_burst_limit = 5

# The API request steady-state rate limit.
throttle_settings_rate_limit = 10
