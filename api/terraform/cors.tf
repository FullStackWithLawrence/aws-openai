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
  api_key_required = "true"
}

resource "aws_api_gateway_integration" "cors" {
  rest_api_id             = aws_api_gateway_rest_api.openai.id
  resource_id             = aws_api_gateway_resource.proxy_plus.id
  http_method             = aws_api_gateway_method.cors.http_method
  integration_http_method = "OPTIONS"
  type                    = "AWS_PROXY"

  uri                  = "arn:aws:lambda:us-east-1:090511222473:function:preflightRequestHandler"
  credentials          = aws_iam_role.apigateway.arn
  request_templates    = {}
  passthrough_behavior = "WHEN_NO_TEMPLATES"
  depends_on           = [aws_api_gateway_method.cors]
}

resource "aws_api_gateway_integration_response" "cors" {
  rest_api_id = aws_api_gateway_rest_api.openai.id
  resource_id = aws_api_gateway_resource.proxy_plus.id
  http_method = aws_api_gateway_method.cors.http_method
  status_code = aws_api_gateway_method_response.cors.status_code
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
