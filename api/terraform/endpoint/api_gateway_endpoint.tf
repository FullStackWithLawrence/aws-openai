###############################################################################
# REST API resources - default-endpoint
# https://platform.openai.com/examples/default-endpoint
#
# see: https://mrponath.medium.com/terraform-and-aws-api-gateway-a137ee48a8ac
###############################################################################
locals {
  openai_integration_template = templatefile(
    "${path.module}/mapping-templates/openai-integration.tpl",
    {
      mapping_object_type         = var.mapping_object_type
      mapping_model               = var.mapping_model
      mapping_role_system_content = var.mapping_role_system_content
      mapping_end_point           = var.mapping_end_point
      mapping_temperature         = var.mapping_temperature
      mapping_max_tokens          = var.mapping_max_tokens
    }
  )

}
resource "aws_api_gateway_resource" "endpoint" {
  path_part   = var.path_part
  parent_id   = var.aws_api_gateway_rest_api_parent_id
  rest_api_id = var.aws_api_gateway_rest_api_id
}

# -----------------------------------------------------------------------------
# POST
# -----------------------------------------------------------------------------
resource "aws_api_gateway_method" "post" {
  rest_api_id      = var.aws_api_gateway_rest_api_id
  resource_id      = aws_api_gateway_resource.endpoint.id
  http_method      = "POST"
  authorization    = "NONE"
  api_key_required = "true"
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
    "application/json" = local.openai_integration_template
  }
  passthrough_behavior = "WHEN_NO_TEMPLATES"
  depends_on           = [aws_api_gateway_method.post]
}

# -----------------------------------------------------------------------------
# Response 200
# -----------------------------------------------------------------------------
resource "aws_api_gateway_method_response" "post_200" {
  rest_api_id = var.aws_api_gateway_rest_api_id
  resource_id = aws_api_gateway_resource.endpoint.id
  http_method = aws_api_gateway_method.post.http_method
  status_code = "200"
  response_parameters = {
    "method.response.header.Content-Type"                 = true,
    "method.response.header.Access-Control-Allow-Headers" = true,
    "method.response.header.Access-Control-Allow-Methods" = true,
    "method.response.header.Access-Control-Allow-Origin"  = true
  }

  response_models = {
    "application/json" = "Empty"
  }
}
resource "aws_api_gateway_integration_response" "post_200" {
  rest_api_id = var.aws_api_gateway_rest_api_id
  resource_id = aws_api_gateway_resource.endpoint.id
  http_method = aws_api_gateway_method.post.http_method
  status_code = aws_api_gateway_method_response.post_200.status_code
  # make this the default integration response
  selection_pattern = ""

  response_parameters = {
    "method.response.header.Access-Control-Allow-Headers" = "'Content-Type,X-Amz-Date,Authorization,X-Api-Key,X-Amz-Security-Token'",
    "method.response.header.Access-Control-Allow-Methods" = "'GET,OPTIONS,POST,PUT'",
    "method.response.header.Access-Control-Allow-Origin"  = "'*'"
  }
  response_templates = {
    "application/json" = ""
  }

  depends_on = [
    aws_api_gateway_integration.post
  ]
}

# -----------------------------------------------------------------------------
# Response 400
# -----------------------------------------------------------------------------
resource "aws_api_gateway_method_response" "post_400" {
  rest_api_id = var.aws_api_gateway_rest_api_id
  resource_id = aws_api_gateway_resource.endpoint.id
  http_method = aws_api_gateway_method.post.http_method
  status_code = "400"
  response_parameters = {
    "method.response.header.Content-Type"                 = true,
    "method.response.header.Access-Control-Allow-Headers" = true,
    "method.response.header.Access-Control-Allow-Methods" = true,
    "method.response.header.Access-Control-Allow-Origin"  = true
  }

  response_models = {
    "application/json" = "Error"
  }
}
resource "aws_api_gateway_integration_response" "post_400" {
  rest_api_id       = var.aws_api_gateway_rest_api_id
  resource_id       = aws_api_gateway_resource.endpoint.id
  http_method       = aws_api_gateway_method.post.http_method
  status_code       = aws_api_gateway_method_response.post_400.status_code
  selection_pattern = "400"
  response_parameters = {
    "method.response.header.Content-Type"                 = "'application/json'",
    "method.response.header.Access-Control-Allow-Headers" = "'*'",
    "method.response.header.Access-Control-Allow-Methods" = "'*'",
    "method.response.header.Access-Control-Allow-Origin"  = "'*'"
  }
  response_templates = {
    "application/json" = ""
  }

  depends_on = [
    aws_api_gateway_integration.post
  ]
}

# -----------------------------------------------------------------------------
# Response 500
# -----------------------------------------------------------------------------
resource "aws_api_gateway_method_response" "post_500" {
  rest_api_id = var.aws_api_gateway_rest_api_id
  resource_id = aws_api_gateway_resource.endpoint.id
  http_method = aws_api_gateway_method.post.http_method
  status_code = "500"

  response_parameters = {
    "method.response.header.Content-Type"                 = true,
    "method.response.header.Access-Control-Allow-Headers" = true,
    "method.response.header.Access-Control-Allow-Methods" = true,
    "method.response.header.Access-Control-Allow-Origin"  = true
  }

  response_models = {
    "application/json" = "Error"
  }
}

resource "aws_api_gateway_integration_response" "post_500" {
  rest_api_id       = var.aws_api_gateway_rest_api_id
  resource_id       = aws_api_gateway_resource.endpoint.id
  http_method       = aws_api_gateway_method.post.http_method
  status_code       = aws_api_gateway_method_response.post_500.status_code
  selection_pattern = "500"
  response_parameters = {
    "method.response.header.Content-Type"                 = "'application/json'",
    "method.response.header.Access-Control-Allow-Headers" = "'*'",
    "method.response.header.Access-Control-Allow-Methods" = "'*'",
    "method.response.header.Access-Control-Allow-Origin"  = "'*'"
  }
  response_templates = {
    "application/json" = ""
  }

  depends_on = [
    aws_api_gateway_integration.post
  ]
}
