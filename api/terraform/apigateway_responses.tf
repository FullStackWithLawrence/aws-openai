resource "aws_api_gateway_gateway_response" "DEFAULT_5XX" {
  rest_api_id   = aws_api_gateway_rest_api.openai.id
  response_type = "DEFAULT_5XX"

  response_templates = {
    "application/json" = "{\"message\":$context.error.messageString}"
  }

  response_parameters = {
    "gatewayresponse.header.Access-Control-Allow-Headers" = "'*'",
    "gatewayresponse.header.Access-Control-Allow-Methods" = "'*'",
    "gatewayresponse.header.Access-Control-Allow-Origin"  = "'*'"
  }
}

resource "aws_api_gateway_gateway_response" "DEFAULT_4XX" {
  rest_api_id   = aws_api_gateway_rest_api.openai.id
  response_type = "DEFAULT_4XX"

  response_templates = {
    "application/json" = "{\"message\":$context.error.messageString}"
  }

  response_parameters = {
    "gatewayresponse.header.Access-Control-Allow-Headers" = "'*'",
    "gatewayresponse.header.Access-Control-Allow-Methods" = "'*'",
    "gatewayresponse.header.Access-Control-Allow-Origin"  = "'*'"
  }
}
