###############################################################################
# REST API resources - default-endpoint
# https://platform.openai.com/examples/default-endpoint
#
#
###############################################################################
data "aws_caller_identity" "current" {}


resource "aws_api_gateway_resource" "endpoint" {
  path_part   = var.path_part
  parent_id   = var.aws_api_gateway_rest_api_parent_id
  rest_api_id = var.aws_api_gateway_rest_api_id
}

resource "aws_api_gateway_method" "endpoint" {
  rest_api_id      = var.aws_api_gateway_rest_api_id
  resource_id      = aws_api_gateway_resource.endpoint.id
  http_method      = "PUT"
  authorization    = "NONE"
  api_key_required = "true"
}

data "template_file" "openai_integration" {
  template = file("${path.module}/mapping-templates/openai-integration.tpl")
  vars = {
    mapping_role_system_content = var.mapping_role_system_content
    mapping_end_point           = var.mapping_end_point
    mapping_temperature         = var.mapping_temperature
    mapping_max_tokens          = var.mapping_max_tokens
  }
}

resource "aws_api_gateway_integration" "endpoint" {
  rest_api_id             = var.aws_api_gateway_rest_api_id
  resource_id             = aws_api_gateway_resource.endpoint.id
  http_method             = aws_api_gateway_method.endpoint.http_method
  integration_http_method = "POST"
  type                    = "AWS"
  uri                     = var.aws_lambda_function_openai_text_invoke_arn
  credentials             = var.aws_iam_role_arn
  # https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-mapping-template-reference.html#input-variable-reference
  # https://goessner.net/articles/JsonPath/
  request_templates = {
    "application/json" = data.template_file.openai_integration.rendered
  }
  passthrough_behavior = "WHEN_NO_TEMPLATES"
  depends_on           = [aws_api_gateway_method.endpoint]
}

resource "aws_api_gateway_method_response" "grammar_response_200" {
  rest_api_id = var.aws_api_gateway_rest_api_id
  resource_id = aws_api_gateway_resource.endpoint.id
  http_method = aws_api_gateway_method.endpoint.http_method
  status_code = "200"
  response_models = {
    "application/json" = "Empty"
  }
}

###############################################################################
# IAM
###############################################################################
# More: http://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-control-access-using-iam-policies-to-invoke-api.html
# resource "aws_lambda_permission" "endpoint" {
#   statement_id  = "AllowExecutionFromAPIGateway"
#   action        = "lambda:InvokeFunction"
#   function_name = var.aws_lambda_function_openai_text
#   principal     = "apigateway.amazonaws.com"
#   source_arn    = "arn:aws:execute-api:${var.aws_region}:${data.aws_caller_identity.current.account_id}:${var.aws_api_gateway_rest_api_id}/*/${aws_api_gateway_method.endpoint.http_method}${aws_api_gateway_resource.endpoint.path}"
# }
