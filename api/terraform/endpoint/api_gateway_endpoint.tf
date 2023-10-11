###############################################################################
# REST API resources - default-endpoint
# https://platform.openai.com/examples/default-endpoint
#
# see: https://mrponath.medium.com/terraform-and-aws-api-gateway-a137ee48a8ac
###############################################################################
resource "aws_api_gateway_resource" "endpoint" {
  path_part   = var.path_part
  parent_id   = var.aws_api_gateway_rest_api_parent_id
  rest_api_id = var.aws_api_gateway_rest_api_id
}

resource "aws_api_gateway_method" "post" {
  rest_api_id      = var.aws_api_gateway_rest_api_id
  resource_id      = aws_api_gateway_resource.endpoint.id
  http_method      = "POST"
  authorization    = "NONE"
  api_key_required = "true"
}

data "template_file" "openai_integration" {
  template = file("${path.module}/mapping-templates/openai-integration.tpl")
  vars = {
    mapping_model               = var.mapping_model
    mapping_role_system_content = var.mapping_role_system_content
    mapping_end_point           = var.mapping_end_point
    mapping_temperature         = var.mapping_temperature
    mapping_max_tokens          = var.mapping_max_tokens
  }
}

resource "aws_api_gateway_integration" "post" {
  rest_api_id             = var.aws_api_gateway_rest_api_id
  resource_id             = aws_api_gateway_resource.endpoint.id
  http_method             = aws_api_gateway_method.post.http_method
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
  depends_on           = [aws_api_gateway_method.post]
}

resource "aws_api_gateway_method_response" "post" {
  rest_api_id = var.aws_api_gateway_rest_api_id
  resource_id = aws_api_gateway_resource.endpoint.id
  http_method = aws_api_gateway_method.post.http_method
  status_code = "200"
  response_parameters = {
    "method.response.header.Access-Control-Allow-Origin" = true
  }

  response_models = {
    "application/json" = "Empty"
  }
}
resource "aws_api_gateway_integration_response" "post" {
  rest_api_id        = var.aws_api_gateway_rest_api_id
  resource_id        = aws_api_gateway_resource.endpoint.id
  http_method        = aws_api_gateway_method.post.http_method
  status_code        = aws_api_gateway_method_response.post.status_code
  response_templates = {}
  depends_on = [
    aws_api_gateway_integration.post
  ]
}
