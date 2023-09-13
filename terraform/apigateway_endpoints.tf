#------------------------------------------------------------------------------
# written by: Lawrence McDaniel
#             https://lawrencemcdaniel.com/
#
# date:   sep-2023
#
# usage:  modularized api endpoint implementations, one per OpenAI example
#         application.
#
# see:    https://platform.openai.com/examples
#         https://github.com/openai/openai-cookbook/
#------------------------------------------------------------------------------


###############################################################################
# see https://platform.openai.com/examples/default-grammar
###############################################################################
module "default_grammar" {
  source    = "./endpoint"
  path_part = "default-grammar"

  # OpenAI application definition
  mapping_end_point           = "ChatCompletion"
  mapping_model               = "gpt-3.5-turbo"
  mapping_role_system_content = "You will be provided with statements, and your task is to convert them to standard English."

  # integrate this endpoint to the AWS Gateway API.
  aws_region                                 = var.aws_region
  aws_api_gateway_rest_api_parent_id         = aws_api_gateway_resource.examples.id
  aws_api_gateway_rest_api_id                = aws_api_gateway_rest_api.openai.id
  aws_lambda_function_openai_text_invoke_arn = aws_lambda_function.openai_text.invoke_arn
  aws_lambda_function_openai_text            = aws_lambda_function.openai_text.function_name
  aws_iam_role_arn                           = aws_iam_role.apigateway.arn
}

###############################################################################
# see https://platform.openai.com/examples/default-summarize
###############################################################################
module "default_summarize" {
  source    = "./endpoint"
  path_part = "default-summarize"

  # OpenAI application definition
  mapping_end_point           = "ChatCompletion"
  mapping_model               = "gpt-3.5-turbo"
  mapping_role_system_content = "Summarize content you are provided with for a second-grade student."
  mapping_temperature         = 0
  mapping_max_tokens          = 1024

  # integrate this endpoint to the AWS Gateway API.
  aws_region                                 = var.aws_region
  aws_api_gateway_rest_api_parent_id         = aws_api_gateway_resource.examples.id
  aws_api_gateway_rest_api_id                = aws_api_gateway_rest_api.openai.id
  aws_lambda_function_openai_text_invoke_arn = aws_lambda_function.openai_text.invoke_arn
  aws_lambda_function_openai_text            = aws_lambda_function.openai_text.function_name
  aws_iam_role_arn                           = aws_iam_role.apigateway.arn
}

###############################################################################
# see https://platform.openai.com/examples/default-parse-data
###############################################################################
module "default_parse_data" {
  source    = "./endpoint"
  path_part = "default-parse-data"

  # OpenAI application definition
  mapping_end_point           = "ChatCompletion"
  mapping_model               = "gpt-3.5-turbo"
  mapping_role_system_content = "You will be provided with unstructured data, and your task is to parse it into CSV format."
  mapping_temperature         = 0
  mapping_max_tokens          = 256

  # integrate this endpoint to the AWS Gateway API.
  aws_region                                 = var.aws_region
  aws_api_gateway_rest_api_parent_id         = aws_api_gateway_resource.examples.id
  aws_api_gateway_rest_api_id                = aws_api_gateway_rest_api.openai.id
  aws_lambda_function_openai_text_invoke_arn = aws_lambda_function.openai_text.invoke_arn
  aws_lambda_function_openai_text            = aws_lambda_function.openai_text.function_name
  aws_iam_role_arn                           = aws_iam_role.apigateway.arn
}
