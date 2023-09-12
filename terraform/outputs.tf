#------------------------------------------------------------------------------
# written by: Lawrence McDaniel
#             https://lawrencemcdaniel.com/
#
# date:       sep-2023
#
# usage:      all computed out values
#------------------------------------------------------------------------------
output "aws_account_id" {
  value = data.aws_caller_identity.current.account_id
}
output "aws_region" {
  value = var.aws_region
}
output "aws_profile" {
  value = var.aws_profile
}

output "api_gateway_deployment_stage" {
  value = var.stage
}
output "api_gateway_api_key" {
  value = nonsensitive(aws_api_gateway_api_key.openai.value)
}

output "api_apigateway_url" {
  value = aws_api_gateway_stage.openai.invoke_url
}

output "lambda_openai" {
  value = aws_lambda_function.openai_text.arn
}
