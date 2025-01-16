###############################################################################
# Simple passthrough_v2 endpoint that passes the request body directly to Lambda.
# Expects a request body of the form found here: https://platform.openai.com/examples
#
# A valid request body:
#   {
#    "model": "gpt-4-turbo",
#    "end_point": "ChatCompletion",
#    "temperature": 0.9,
#    "max_tokens": 1024,
#    "messages": [
#      {
#         "role": "system",
#         "content": "Summarize content you are provided with for a second-grade student."
#      },
#      {
#         "role": "user",
#         "content": "what is quantum computing?"
#       }
#     ]
#   }
#
###############################################################################
resource "aws_api_gateway_resource" "passthrough_v2" {
  path_part   = "passthrough_v2"
  parent_id   = aws_api_gateway_rest_api.openai.root_resource_id
  rest_api_id = aws_api_gateway_rest_api.openai.id
}

# -----------------------------------------------------------------------------
# POST
# -----------------------------------------------------------------------------
resource "aws_api_gateway_method" "passthrough_v2_post" {
  rest_api_id      = aws_api_gateway_rest_api.openai.id
  resource_id      = aws_api_gateway_resource.passthrough_v2.id
  http_method      = "POST"
  authorization    = "NONE"
  api_key_required = "true"
}

resource "aws_api_gateway_integration" "passthrough_v2_post" {
  rest_api_id             = aws_api_gateway_rest_api.openai.id
  resource_id             = aws_api_gateway_resource.passthrough_v2.id
  http_method             = aws_api_gateway_method.passthrough_v2_post.http_method
  integration_http_method = "POST"
  type                    = "AWS"
  uri                     = aws_lambda_function.lambda_openai_v2.invoke_arn
  credentials             = aws_iam_role.apigateway.arn
  passthrough_behavior    = "WHEN_NO_TEMPLATES"
  depends_on              = [aws_api_gateway_method.passthrough_v2_post]
}

# -----------------------------------------------------------------------------
# Response 200
# -----------------------------------------------------------------------------
resource "aws_api_gateway_method_response" "passthrough_v2_post_200" {
  rest_api_id = aws_api_gateway_rest_api.openai.id
  resource_id = aws_api_gateway_resource.passthrough_v2.id
  http_method = aws_api_gateway_method.passthrough_v2_post.http_method
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
resource "aws_api_gateway_integration_response" "passthrough_v2_post_200" {
  rest_api_id = aws_api_gateway_rest_api.openai.id
  resource_id = aws_api_gateway_resource.passthrough_v2.id
  http_method = aws_api_gateway_method.passthrough_v2_post.http_method
  status_code = aws_api_gateway_method_response.passthrough_v2_post_200.status_code
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

  depends_on = [aws_api_gateway_integration.passthrough_v2_post]
}

# -----------------------------------------------------------------------------
# Response 400
# -----------------------------------------------------------------------------
resource "aws_api_gateway_method_response" "passthrough_v2_post_400" {
  rest_api_id = aws_api_gateway_rest_api.openai.id
  resource_id = aws_api_gateway_resource.passthrough_v2.id
  http_method = aws_api_gateway_method.passthrough_v2_post.http_method
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
resource "aws_api_gateway_integration_response" "passthrough_v2_post_400" {
  rest_api_id       = aws_api_gateway_rest_api.openai.id
  resource_id       = aws_api_gateway_resource.passthrough_v2.id
  http_method       = aws_api_gateway_method.passthrough_v2_post.http_method
  status_code       = aws_api_gateway_method_response.passthrough_v2_post_400.status_code
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

  depends_on = [aws_api_gateway_integration.passthrough_v2_post]
}

# -----------------------------------------------------------------------------
# Response 500
# -----------------------------------------------------------------------------
resource "aws_api_gateway_method_response" "passthrough_v2_post_500" {
  rest_api_id = aws_api_gateway_rest_api.openai.id
  resource_id = aws_api_gateway_resource.passthrough_v2.id
  http_method = aws_api_gateway_method.passthrough_v2_post.http_method
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

resource "aws_api_gateway_integration_response" "passthrough_v2_post_500" {
  rest_api_id       = aws_api_gateway_rest_api.openai.id
  resource_id       = aws_api_gateway_resource.passthrough_v2.id
  http_method       = aws_api_gateway_method.passthrough_v2_post.http_method
  status_code       = aws_api_gateway_method_response.passthrough_v2_post_500.status_code
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

  depends_on = [aws_api_gateway_integration.passthrough_v2_post]
}
