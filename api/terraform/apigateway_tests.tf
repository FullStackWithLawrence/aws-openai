locals {
  template_file_test_200 = templatefile("${path.module}/templates/test_200.json", {})
  template_file_test_400 = templatefile("${path.module}/templates/test_400.json", {})
  template_file_test_500 = jsonencode({
    "isBase64Encoded" : false,
    "statusCode" = 500
    "body" : {
      "error" : "Internal Server Error",
      "message" : "TEST 500 RESPONSE."
    }
  })

  template_file_test_504 = jsonencode({
    "statusCode" = 504
  })
}
resource "aws_api_gateway_resource" "tests" {
  path_part   = "tests"
  parent_id   = aws_api_gateway_rest_api.openai.root_resource_id
  rest_api_id = aws_api_gateway_rest_api.openai.id
}

###############################################################################
# Test 200
###############################################################################

resource "aws_api_gateway_resource" "test_200" {
  path_part   = "test_200"
  parent_id   = aws_api_gateway_resource.tests.id
  rest_api_id = aws_api_gateway_rest_api.openai.id
}

resource "aws_api_gateway_method" "test_200" {
  rest_api_id      = aws_api_gateway_rest_api.openai.id
  resource_id      = aws_api_gateway_resource.test_200.id
  http_method      = "POST"
  authorization    = "NONE"
  api_key_required = "false"
}

resource "aws_api_gateway_integration" "test_200" {
  rest_api_id             = aws_api_gateway_rest_api.openai.id
  resource_id             = aws_api_gateway_resource.test_200.id
  http_method             = aws_api_gateway_method.test_200.http_method
  integration_http_method = "POST"
  type                    = "MOCK"
  request_templates = {
    "application/json" = local.template_file_test_200
  }
  depends_on = [aws_api_gateway_method.test_200]
  lifecycle {
    ignore_changes = [
      integration_http_method
    ]
  }
}

resource "aws_api_gateway_method_response" "test_200" {
  rest_api_id = aws_api_gateway_rest_api.openai.id
  resource_id = aws_api_gateway_resource.test_200.id
  http_method = aws_api_gateway_method.test_200.http_method
  status_code = "200"
  response_models = {
    "application/json" = "Empty"
  }
  response_parameters = {
    "method.response.header.Content-Type"                 = true
    "method.response.header.Access-Control-Allow-Headers" = true
    "method.response.header.Access-Control-Allow-Methods" = true
    "method.response.header.Access-Control-Allow-Origin"  = true
  }
}

resource "aws_api_gateway_integration_response" "test_200" {
  rest_api_id       = aws_api_gateway_rest_api.openai.id
  resource_id       = aws_api_gateway_resource.test_200.id
  http_method       = aws_api_gateway_method.test_200.http_method
  status_code       = aws_api_gateway_method_response.test_200.status_code
  selection_pattern = 200

  response_parameters = {
    "method.response.header.Content-Type"                 = "'application/json'",
    "method.response.header.Access-Control-Allow-Headers" = "'*'",
    "method.response.header.Access-Control-Allow-Methods" = "'*'",
    "method.response.header.Access-Control-Allow-Origin"  = "'*'"
  }
  response_templates = {
    "application/json" = local.template_file_test_200
  }

  depends_on = [
    aws_api_gateway_integration.test_200
  ]
}


###############################################################################
# Test 400
###############################################################################

resource "aws_api_gateway_resource" "test_400" {
  path_part   = "test_400"
  parent_id   = aws_api_gateway_resource.tests.id
  rest_api_id = aws_api_gateway_rest_api.openai.id
}

resource "aws_api_gateway_method" "test_400" {
  rest_api_id      = aws_api_gateway_rest_api.openai.id
  resource_id      = aws_api_gateway_resource.test_400.id
  http_method      = "POST"
  authorization    = "NONE"
  api_key_required = "false"
}

resource "aws_api_gateway_integration" "test_400" {
  rest_api_id             = aws_api_gateway_rest_api.openai.id
  resource_id             = aws_api_gateway_resource.test_400.id
  http_method             = aws_api_gateway_method.test_400.http_method
  integration_http_method = "POST"
  type                    = "MOCK"
  request_templates = {
    "application/json" = local.template_file_test_400
  }
  depends_on = [aws_api_gateway_method.test_400]
  lifecycle {
    ignore_changes = [
      integration_http_method
    ]
  }
}

resource "aws_api_gateway_method_response" "test_400" {
  rest_api_id = aws_api_gateway_rest_api.openai.id
  resource_id = aws_api_gateway_resource.test_400.id
  http_method = aws_api_gateway_method.test_400.http_method
  status_code = "400"
  response_models = {
    "application/json" = "Error"
  }
  response_parameters = {
    "method.response.header.Content-Type"                 = true
    "method.response.header.Access-Control-Allow-Headers" = true
    "method.response.header.Access-Control-Allow-Methods" = true
    "method.response.header.Access-Control-Allow-Origin"  = true
  }
}

resource "aws_api_gateway_integration_response" "test_400" {
  rest_api_id       = aws_api_gateway_rest_api.openai.id
  resource_id       = aws_api_gateway_resource.test_400.id
  http_method       = aws_api_gateway_method.test_400.http_method
  status_code       = aws_api_gateway_method_response.test_400.status_code
  selection_pattern = "400"

  response_parameters = {
    "method.response.header.Content-Type"                 = "'application/json'",
    "method.response.header.Access-Control-Allow-Headers" = "'*'",
    "method.response.header.Access-Control-Allow-Methods" = "'*'",
    "method.response.header.Access-Control-Allow-Origin"  = "'*'"
  }
  response_templates = {
    "application/json" = local.template_file_test_400
  }

  depends_on = [
    aws_api_gateway_integration.test_400
  ]
}


###############################################################################
# Test 500
###############################################################################

resource "aws_api_gateway_resource" "test_500" {
  path_part   = "test_500"
  parent_id   = aws_api_gateway_resource.tests.id
  rest_api_id = aws_api_gateway_rest_api.openai.id
}

resource "aws_api_gateway_method" "test_500" {
  rest_api_id      = aws_api_gateway_rest_api.openai.id
  resource_id      = aws_api_gateway_resource.test_500.id
  http_method      = "POST"
  authorization    = "NONE"
  api_key_required = "false"
}

resource "aws_api_gateway_integration" "test_500" {
  rest_api_id             = aws_api_gateway_rest_api.openai.id
  resource_id             = aws_api_gateway_resource.test_500.id
  http_method             = aws_api_gateway_method.test_500.http_method
  integration_http_method = "POST"
  type                    = "MOCK"
  request_templates = {
    "application/json" = local.template_file_test_500
  }
  depends_on = [aws_api_gateway_method.test_500]
  lifecycle {
    ignore_changes = [
      integration_http_method
    ]
  }
}

resource "aws_api_gateway_method_response" "test_500" {
  rest_api_id = aws_api_gateway_rest_api.openai.id
  resource_id = aws_api_gateway_resource.test_500.id
  http_method = aws_api_gateway_method.test_500.http_method
  status_code = "500"
  response_models = {
    "application/json" = "Error"
  }
  response_parameters = {
    "method.response.header.Content-Type"                 = true
    "method.response.header.Access-Control-Allow-Headers" = true
    "method.response.header.Access-Control-Allow-Methods" = true
    "method.response.header.Access-Control-Allow-Origin"  = true
  }
}

resource "aws_api_gateway_integration_response" "test_500" {
  rest_api_id       = aws_api_gateway_rest_api.openai.id
  resource_id       = aws_api_gateway_resource.test_500.id
  http_method       = aws_api_gateway_method.test_500.http_method
  status_code       = aws_api_gateway_method_response.test_500.status_code
  selection_pattern = "500"

  response_parameters = {
    "method.response.header.Content-Type"                 = "'application/json'",
    "method.response.header.Access-Control-Allow-Headers" = "'*'",
    "method.response.header.Access-Control-Allow-Methods" = "'*'",
    "method.response.header.Access-Control-Allow-Origin"  = "'*'"
  }
  response_templates = {
    "application/json" = local.template_file_test_500
  }

  depends_on = [
    aws_api_gateway_integration.test_500
  ]
}

###############################################################################
# Test 504
###############################################################################

resource "aws_api_gateway_resource" "test_504" {
  path_part   = "test_504"
  parent_id   = aws_api_gateway_resource.tests.id
  rest_api_id = aws_api_gateway_rest_api.openai.id
}

resource "aws_api_gateway_method" "test_504" {
  rest_api_id      = aws_api_gateway_rest_api.openai.id
  resource_id      = aws_api_gateway_resource.test_504.id
  http_method      = "POST"
  authorization    = "NONE"
  api_key_required = "false"
}

resource "aws_api_gateway_integration" "test_504" {
  rest_api_id             = aws_api_gateway_rest_api.openai.id
  resource_id             = aws_api_gateway_resource.test_504.id
  http_method             = aws_api_gateway_method.test_504.http_method
  integration_http_method = "POST"
  type                    = "MOCK"
  request_templates = {
    "application/json" = local.template_file_test_504
  }
  depends_on = [aws_api_gateway_method.test_504]
  lifecycle {
    ignore_changes = [
      integration_http_method
    ]
  }
}

resource "aws_api_gateway_method_response" "test_504" {
  rest_api_id = aws_api_gateway_rest_api.openai.id
  resource_id = aws_api_gateway_resource.test_504.id
  http_method = aws_api_gateway_method.test_504.http_method
  status_code = "504"
  response_models = {
    "application/json" = "Error"
  }
  response_parameters = {
    "method.response.header.Content-Type"                 = true
    "method.response.header.Access-Control-Allow-Headers" = true
    "method.response.header.Access-Control-Allow-Methods" = true
    "method.response.header.Access-Control-Allow-Origin"  = true
  }
}

resource "aws_api_gateway_integration_response" "test_504" {
  rest_api_id       = aws_api_gateway_rest_api.openai.id
  resource_id       = aws_api_gateway_resource.test_504.id
  http_method       = aws_api_gateway_method.test_504.http_method
  status_code       = aws_api_gateway_method_response.test_504.status_code
  selection_pattern = "504"

  response_parameters = {
    "method.response.header.Content-Type"                 = "'application/json'",
    "method.response.header.Access-Control-Allow-Headers" = "'*'",
    "method.response.header.Access-Control-Allow-Methods" = "'*'",
    "method.response.header.Access-Control-Allow-Origin"  = "'*'"
  }
  response_templates = {
    "application/json" = jsonencode({ "message" : "TEST 504 RESPONSE." })
  }

  depends_on = [
    aws_api_gateway_integration.test_504
  ]
}
