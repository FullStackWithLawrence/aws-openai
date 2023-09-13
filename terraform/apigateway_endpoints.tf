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


module "default_grammar" {
  source                      = "./endpoint"
  path_part                   = "default-grammar"
  mapping_end_point           = "ChatCompletion"
  mapping_role_system_content = "You will be provided with statements, and your task is to convert them to standard English."

  # integrate this endpoint to the AWS Gateway API.
  aws_region                                 = var.aws_region
  aws_api_gateway_rest_api_root_resource_id  = aws_api_gateway_rest_api.openai.root_resource_id
  aws_api_gateway_rest_api_id                = aws_api_gateway_rest_api.openai.id
  aws_lambda_function_openai_text_invoke_arn = aws_lambda_function.openai_text.invoke_arn
  aws_lambda_function_openai_text            = aws_lambda_function.openai_text.function_name
  aws_iam_role_arn                           = aws_iam_role.apigateway.arn
}
