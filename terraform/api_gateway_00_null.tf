###############################################################################
# REST API resources - default-test
# https://platform.openai.com/examples/default-test
#
#
###############################################################################

resource "aws_api_gateway_resource" "test" {
  path_part   = "test"
  parent_id   = aws_api_gateway_rest_api.openai.root_resource_id
  rest_api_id = aws_api_gateway_rest_api.openai.id
}
resource "aws_api_gateway_method" "test" {
  rest_api_id      = aws_api_gateway_rest_api.openai.id
  resource_id      = aws_api_gateway_resource.test.id
  http_method      = "ANY"
  authorization    = "NONE"
  api_key_required = "true"
}

resource "aws_api_gateway_integration" "test" {
  rest_api_id             = aws_api_gateway_rest_api.openai.id
  resource_id             = aws_api_gateway_resource.test.id
  http_method             = aws_api_gateway_method.test.http_method
  integration_http_method = "POST"
  type                    = "AWS_PROXY"
  uri                     = aws_lambda_function.openai_null.invoke_arn
  # https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-mapping-template-reference.html#input-variable-reference
  # https://goessner.net/articles/JsonPath/
  request_templates = {
  }
}

resource "aws_api_gateway_method_response" "test_response_200" {
  rest_api_id = aws_api_gateway_rest_api.openai.id
  resource_id = aws_api_gateway_resource.test.id
  http_method = aws_api_gateway_method.test.http_method
  status_code = "200"
  response_models = {
    "application/json" = "Empty"
  }
  response_parameters = {}
}

resource "aws_lambda_permission" "test" {
  # More: http://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-control-access-using-iam-policies-to-invoke-api.html
  statement_id  = "AllowExecutionFromAPIGateway"
  action        = "lambda:InvokeFunction"
  function_name = aws_lambda_function.openai_null.function_name
  principal     = "apigateway.amazonaws.com"
  source_arn    = "arn:aws:execute-api:${var.aws_region}:${data.aws_caller_identity.current.account_id}:${aws_api_gateway_rest_api.openai.id}/*/${aws_api_gateway_method.test.http_method}${aws_api_gateway_resource.test.path}"
}
