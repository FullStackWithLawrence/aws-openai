###############################################################################
# REST API resources - Search
# This is an HTTP Get request, to retrieve the configuration settings for the
# facial recognition system.
#
# workflow is: 1. method request        (from Postman, curl, your application, etc.)
#              2. integration request   (we're integrating to an AWS Lambda function)
#              3. integration response  (the results from the Lambda function)
#              4. method response       (hopefully, an http 200 response)
#
###############################################################################
resource "aws_api_gateway_resource" "info" {
  path_part   = "info"
  parent_id   = aws_api_gateway_rest_api.openai.root_resource_id
  rest_api_id = aws_api_gateway_rest_api.openai.id
}
resource "aws_api_gateway_method" "info" {
  rest_api_id      = aws_api_gateway_rest_api.openai.id
  resource_id      = aws_api_gateway_resource.info.id
  http_method      = "ANY"
  authorization    = "NONE"
  api_key_required = "true"
}

resource "aws_api_gateway_integration" "info" {
  rest_api_id             = aws_api_gateway_rest_api.openai.id
  resource_id             = aws_api_gateway_resource.info.id
  http_method             = aws_api_gateway_method.info.http_method
  integration_http_method = "POST"
  type                    = "AWS_PROXY"
  uri                     = aws_lambda_function.info.invoke_arn
}

resource "aws_lambda_permission" "info" {
  statement_id  = "AllowExecutionFromAPIGateway"
  action        = "lambda:InvokeFunction"
  function_name = aws_lambda_function.info.function_name
  principal     = "apigateway.amazonaws.com"

  # More: http://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-control-access-using-iam-policies-to-invoke-api.html
  source_arn = "arn:aws:execute-api:${var.aws_region}:${data.aws_caller_identity.current.account_id}:${aws_api_gateway_rest_api.openai.id}/*/${aws_api_gateway_method.info.http_method}${aws_api_gateway_resource.info.path}"

}

resource "aws_api_gateway_method_response" "info_response_200" {
  rest_api_id = aws_api_gateway_rest_api.openai.id
  resource_id = aws_api_gateway_resource.info.id
  http_method = aws_api_gateway_method.info.http_method
  status_code = "200"
  response_models = {
    "application/json" = "Empty"
  }
  response_parameters = {}
}
