###############################################################################
# CORS setup
###############################################################################
resource "aws_api_gateway_resource" "proxy_plus" {
  path_part   = "{proxy+}"
  parent_id   = aws_api_gateway_rest_api.openai.root_resource_id
  rest_api_id = aws_api_gateway_rest_api.openai.id
}

resource "aws_api_gateway_method" "cors" {
  rest_api_id      = aws_api_gateway_rest_api.openai.id
  resource_id      = aws_api_gateway_resource.proxy_plus.id
  http_method      = "OPTIONS"
  authorization    = "NONE"
  api_key_required = "false"
}

resource "aws_api_gateway_integration" "cors" {
  rest_api_id             = aws_api_gateway_rest_api.openai.id
  resource_id             = aws_api_gateway_resource.proxy_plus.id
  http_method             = aws_api_gateway_method.cors.http_method
  integration_http_method = "POST"
  type                    = "AWS"
  uri                     = aws_lambda_function.cors_preflight_handler.invoke_arn
  credentials             = aws_iam_role.apigateway.arn
  passthrough_behavior    = "WHEN_NO_TEMPLATES"
  depends_on              = [aws_api_gateway_method.cors]
}

resource "aws_api_gateway_integration_response" "cors" {
  rest_api_id = aws_api_gateway_rest_api.openai.id
  resource_id = aws_api_gateway_resource.proxy_plus.id
  http_method = aws_api_gateway_method.cors.http_method
  status_code = aws_api_gateway_method_response.cors.status_code
  # response_parameters = {
  #   "method.response.header.Access-Control-Allow-Headers" = "'Content-Type,X-Amz-Date,Authorization,X-Api-Key,X-Amz-Security-Token'"
  #   "method.response.header.Access-Control-Allow-Methods" = "'GET,OPTIONS,POST,PUT,PATCH,DELETE'"
  #   "method.response.header.Access-Control-Allow-Origin"  = "'*'"
  # }
  response_parameters = {
    "method.response.header.Access-Control-Allow-Headers" = "integration.response.header.Access-Control-Allow-Headers"
    "method.response.header.Access-Control-Allow-Methods" = "integration.response.header.Access-Control-Allow-Methods"
    "method.response.header.Access-Control-Allow-Origin"  = "integration.response.header.Access-Control-Allow-Origin"
  }
  depends_on = [
    aws_api_gateway_integration.cors
  ]
}

resource "aws_api_gateway_method_response" "cors" {
  rest_api_id = aws_api_gateway_rest_api.openai.id
  resource_id = aws_api_gateway_resource.proxy_plus.id
  http_method = aws_api_gateway_method.cors.http_method
  status_code = "200"
  response_models = {
    "application/json" = "Empty"
  }
  response_parameters = {
    "method.response.header.Access-Control-Allow-Headers" = true
    "method.response.header.Access-Control-Allow-Methods" = true
    "method.response.header.Access-Control-Allow-Origin"  = true
  }
}
