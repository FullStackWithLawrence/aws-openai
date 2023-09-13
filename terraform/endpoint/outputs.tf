
output "aws_api_gateway_integration" {
  value = aws_api_gateway_integration.endpoint
}

output "aws_api_gateway_method" {
  value = aws_api_gateway_method.endpoint
}

output "aws_api_gateway_method_response_endpoint_response_200" {
  value = aws_api_gateway_method_response.grammar_response_200.id
}

output "sha1_deployment_trigger" {
  value = sha1(jsonencode([
    aws_api_gateway_integration.endpoint,
    aws_api_gateway_method.endpoint,
    aws_api_gateway_method_response.grammar_response_200.id
  ]))
}
