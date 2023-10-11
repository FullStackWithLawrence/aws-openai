
output "aws_api_gateway_integration" {
  value = aws_api_gateway_integration.post
}

output "aws_api_gateway_method" {
  value = aws_api_gateway_method.post
}

output "aws_api_gateway_method_response_endpoint_response_200" {
  value = aws_api_gateway_method_response.post.id
}

output "sha1_deployment_trigger" {
  value = sha1(jsonencode([
    aws_api_gateway_integration.post,
    aws_api_gateway_method.post,
    aws_api_gateway_method_response.post.id,
    #  aws_api_gateway_integration.cors,
    #  aws_api_gateway_method.cors,
    #  aws_api_gateway_method_response.cors.id
  ]))
}
