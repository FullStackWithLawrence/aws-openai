#------------------------------------------------------------------------------
# written by: Lawrence McDaniel
#             https://lawrencemcdaniel.com/
#
# date:   sep-2023
#
# usage:  modularized api endpoint implementations, one per OpenAI example
#         application.
#
# see:    https://platform.openai.com/examples
#         https://github.com/openai/openai-cookbook/
#------------------------------------------------------------------------------


###############################################################################
# 1. see https://platform.openai.com/examples/default-grammar
###############################################################################
module "default_grammar" {
  source    = "./endpoint"
  path_part = "default-grammar"

  # OpenAI application definition
  mapping_end_point           = "ChatCompletion"
  mapping_model               = "gpt-3.5-turbo"
  mapping_role_system_content = "You will be provided with statements, and your task is to convert them to standard English."

  # integrate this endpoint to the AWS Gateway API.
  aws_region                                 = var.aws_region
  aws_api_gateway_rest_api_parent_id         = aws_api_gateway_resource.examples.id
  aws_api_gateway_rest_api_id                = aws_api_gateway_rest_api.openai.id
  aws_lambda_function_openai_text_invoke_arn = aws_lambda_function.openai_text.invoke_arn
  aws_lambda_function_openai_text            = aws_lambda_function.openai_text.function_name
  aws_iam_role_arn                           = aws_iam_role.apigateway.arn
}

###############################################################################
# 2. see https://platform.openai.com/examples/default-summarize
###############################################################################
module "default_summarize" {
  source    = "./endpoint"
  path_part = "default-summarize"

  # OpenAI application definition
  mapping_end_point           = "ChatCompletion"
  mapping_model               = "gpt-3.5-turbo"
  mapping_role_system_content = "Summarize content you are provided with for a second-grade student."
  mapping_temperature         = 0
  mapping_max_tokens          = 1024

  # integrate this endpoint to the AWS Gateway API.
  aws_region                                 = var.aws_region
  aws_api_gateway_rest_api_parent_id         = aws_api_gateway_resource.examples.id
  aws_api_gateway_rest_api_id                = aws_api_gateway_rest_api.openai.id
  aws_lambda_function_openai_text_invoke_arn = aws_lambda_function.openai_text.invoke_arn
  aws_lambda_function_openai_text            = aws_lambda_function.openai_text.function_name
  aws_iam_role_arn                           = aws_iam_role.apigateway.arn
}

###############################################################################
# 3. see https://platform.openai.com/examples/default-parse-data
###############################################################################
module "default_parse_data" {
  source    = "./endpoint"
  path_part = "default-parse-data"

  # OpenAI application definition
  mapping_end_point           = "ChatCompletion"
  mapping_model               = "gpt-3.5-turbo"
  mapping_role_system_content = "You will be provided with unstructured data, and your task is to parse it into CSV format."
  mapping_temperature         = 0
  mapping_max_tokens          = 256

  # integrate this endpoint to the AWS Gateway API.
  aws_region                                 = var.aws_region
  aws_api_gateway_rest_api_parent_id         = aws_api_gateway_resource.examples.id
  aws_api_gateway_rest_api_id                = aws_api_gateway_rest_api.openai.id
  aws_lambda_function_openai_text_invoke_arn = aws_lambda_function.openai_text.invoke_arn
  aws_lambda_function_openai_text            = aws_lambda_function.openai_text.function_name
  aws_iam_role_arn                           = aws_iam_role.apigateway.arn
}


###############################################################################
# 4. see https://platform.openai.com/examples/default-emoji-translation
###############################################################################
module "default_emoji_translation" {
  source    = "./endpoint"
  path_part = "default-emoji-translation"

  # OpenAI application definition
  mapping_end_point           = "ChatCompletion"
  mapping_model               = "gpt-3.5-turbo"
  mapping_role_system_content = "You will be provided with text, and your task is to translate it into emojis. Do not use any regular text. Do your best with emojis only."
  mapping_temperature         = 0.8
  mapping_max_tokens          = 256

  # integrate this endpoint to the AWS Gateway API.
  aws_region                                 = var.aws_region
  aws_api_gateway_rest_api_parent_id         = aws_api_gateway_resource.examples.id
  aws_api_gateway_rest_api_id                = aws_api_gateway_rest_api.openai.id
  aws_lambda_function_openai_text_invoke_arn = aws_lambda_function.openai_text.invoke_arn
  aws_lambda_function_openai_text            = aws_lambda_function.openai_text.function_name
  aws_iam_role_arn                           = aws_iam_role.apigateway.arn
}

###############################################################################
# 5. see https://platform.openai.com/examples/default-time-complexity
###############################################################################
module "default_time_complexity" {
  source    = "./endpoint"
  path_part = "default-time-complexity"

  # OpenAI application definition
  mapping_end_point           = "ChatCompletion"
  mapping_model               = "gpt-3.5-turbo"
  mapping_role_system_content = "You will be provided with Python code, and your task is to calculate its time complexity."
  mapping_temperature         = 0
  mapping_max_tokens          = 256

  # integrate this endpoint to the AWS Gateway API.
  aws_region                                 = var.aws_region
  aws_api_gateway_rest_api_parent_id         = aws_api_gateway_resource.examples.id
  aws_api_gateway_rest_api_id                = aws_api_gateway_rest_api.openai.id
  aws_lambda_function_openai_text_invoke_arn = aws_lambda_function.openai_text.invoke_arn
  aws_lambda_function_openai_text            = aws_lambda_function.openai_text.function_name
  aws_iam_role_arn                           = aws_iam_role.apigateway.arn
}

###############################################################################
# 6. see https://platform.openai.com/examples/default-explain-code
###############################################################################
module "default_explain_code" {
  source    = "./endpoint"
  path_part = "default-explain-code"

  # OpenAI application definition
  mapping_end_point           = "ChatCompletion"
  mapping_model               = "gpt-4"
  mapping_role_system_content = "You will be provided with a piece of code, and your task is to explain it in a concise way."
  mapping_temperature         = 0
  mapping_max_tokens          = 1024

  # integrate this endpoint to the AWS Gateway API.
  aws_region                                 = var.aws_region
  aws_api_gateway_rest_api_parent_id         = aws_api_gateway_resource.examples.id
  aws_api_gateway_rest_api_id                = aws_api_gateway_rest_api.openai.id
  aws_lambda_function_openai_text_invoke_arn = aws_lambda_function.openai_text.invoke_arn
  aws_lambda_function_openai_text            = aws_lambda_function.openai_text.function_name
  aws_iam_role_arn                           = aws_iam_role.apigateway.arn
}

###############################################################################
# 7. see https://platform.openai.com/examples/default-keywords
###############################################################################
module "default_keywords" {
  source    = "./endpoint"
  path_part = "default-keywords"

  # OpenAI application definition
  mapping_end_point           = "ChatCompletion"
  mapping_model               = "gpt-3.5-turbo"
  mapping_role_system_content = "You will be provided with a block of text, and your task is to extract a list of keywords from it."
  mapping_temperature         = 0.5
  mapping_max_tokens          = 256

  # integrate this endpoint to the AWS Gateway API.
  aws_region                                 = var.aws_region
  aws_api_gateway_rest_api_parent_id         = aws_api_gateway_resource.examples.id
  aws_api_gateway_rest_api_id                = aws_api_gateway_rest_api.openai.id
  aws_lambda_function_openai_text_invoke_arn = aws_lambda_function.openai_text.invoke_arn
  aws_lambda_function_openai_text            = aws_lambda_function.openai_text.function_name
  aws_iam_role_arn                           = aws_iam_role.apigateway.arn
}

###############################################################################
# 8. see https://platform.openai.com/examples/default-product-name-gen
###############################################################################
module "default_product_name_gen" {
  source    = "./endpoint"
  path_part = "default-product-name-gen"

  # OpenAI application definition
  mapping_end_point           = "ChatCompletion"
  mapping_model               = "gpt-3.5-turbo"
  mapping_role_system_content = "You will be provided with a product description and seed words, and your task is to generate product names."
  mapping_temperature         = 0.8
  mapping_max_tokens          = 256

  # integrate this endpoint to the AWS Gateway API.
  aws_region                                 = var.aws_region
  aws_api_gateway_rest_api_parent_id         = aws_api_gateway_resource.examples.id
  aws_api_gateway_rest_api_id                = aws_api_gateway_rest_api.openai.id
  aws_lambda_function_openai_text_invoke_arn = aws_lambda_function.openai_text.invoke_arn
  aws_lambda_function_openai_text            = aws_lambda_function.openai_text.function_name
  aws_iam_role_arn                           = aws_iam_role.apigateway.arn
}

###############################################################################
# 9. see https://platform.openai.com/examples/default-fix-python-bugs
###############################################################################
module "default_fix_python_bugs" {
  source    = "./endpoint"
  path_part = "default-fix-python-bugs"

  # OpenAI application definition
  mapping_end_point           = "ChatCompletion"
  mapping_model               = "gpt-4"
  mapping_role_system_content = "You will be provided with a piece of Python code, and your task is to find and fix bugs in it."
  mapping_temperature         = 0
  mapping_max_tokens          = 1024

  # integrate this endpoint to the AWS Gateway API.
  aws_region                                 = var.aws_region
  aws_api_gateway_rest_api_parent_id         = aws_api_gateway_resource.examples.id
  aws_api_gateway_rest_api_id                = aws_api_gateway_rest_api.openai.id
  aws_lambda_function_openai_text_invoke_arn = aws_lambda_function.openai_text.invoke_arn
  aws_lambda_function_openai_text            = aws_lambda_function.openai_text.function_name
  aws_iam_role_arn                           = aws_iam_role.apigateway.arn
}

###############################################################################
# 10. see https://platform.openai.com/examples/default-spreadsheet-gen
###############################################################################
module "default_spreadsheet_gen" {
  source    = "./endpoint"
  path_part = "default-spreadsheet-gen"

  # OpenAI application definition
  mapping_end_point   = "ChatCompletion"
  mapping_model       = "gpt-3.5-turbo"
  mapping_temperature = 0.5
  mapping_max_tokens  = 256

  # integrate this endpoint to the AWS Gateway API.
  aws_region                                 = var.aws_region
  aws_api_gateway_rest_api_parent_id         = aws_api_gateway_resource.examples.id
  aws_api_gateway_rest_api_id                = aws_api_gateway_rest_api.openai.id
  aws_lambda_function_openai_text_invoke_arn = aws_lambda_function.openai_text.invoke_arn
  aws_lambda_function_openai_text            = aws_lambda_function.openai_text.function_name
  aws_iam_role_arn                           = aws_iam_role.apigateway.arn
}

###############################################################################
# 11. see https://platform.openai.com/examples/default-tweet-classifier
###############################################################################
module "default_tweet_classifier" {
  source    = "./endpoint"
  path_part = "default-tweet-classifier"

  # OpenAI application definition
  mapping_end_point           = "ChatCompletion"
  mapping_model               = "gpt-3.5-turbo"
  mapping_role_system_content = "You will be provided with a tweet, and your task is to classify its sentiment as positive, neutral, or negative."
  mapping_temperature         = 0
  mapping_max_tokens          = 256

  # integrate this endpoint to the AWS Gateway API.
  aws_region                                 = var.aws_region
  aws_api_gateway_rest_api_parent_id         = aws_api_gateway_resource.examples.id
  aws_api_gateway_rest_api_id                = aws_api_gateway_rest_api.openai.id
  aws_lambda_function_openai_text_invoke_arn = aws_lambda_function.openai_text.invoke_arn
  aws_lambda_function_openai_text            = aws_lambda_function.openai_text.function_name
  aws_iam_role_arn                           = aws_iam_role.apigateway.arn
}

###############################################################################
# 12. see https://platform.openai.com/examples/default-airport-codes
###############################################################################
module "default_airport_codes" {
  source    = "./endpoint"
  path_part = "default-airport-codes"

  # OpenAI application definition
  mapping_end_point           = "ChatCompletion"
  mapping_model               = "gpt-3.5-turbo"
  mapping_role_system_content = "You will be provided with a text, and your task is to extract the airport codes from it."
  mapping_temperature         = 0
  mapping_max_tokens          = 256

  # integrate this endpoint to the AWS Gateway API.
  aws_region                                 = var.aws_region
  aws_api_gateway_rest_api_parent_id         = aws_api_gateway_resource.examples.id
  aws_api_gateway_rest_api_id                = aws_api_gateway_rest_api.openai.id
  aws_lambda_function_openai_text_invoke_arn = aws_lambda_function.openai_text.invoke_arn
  aws_lambda_function_openai_text            = aws_lambda_function.openai_text.function_name
  aws_iam_role_arn                           = aws_iam_role.apigateway.arn
}

###############################################################################
# 13. see https://platform.openai.com/examples/default-mood-color
###############################################################################
module "default_mood_color" {
  source    = "./endpoint"
  path_part = "default-mood-color"

  # OpenAI application definition
  mapping_end_point           = "ChatCompletion"
  mapping_model               = "gpt-3.5-turbo"
  mapping_role_system_content = "You will be provided with a description of a mood, and your task is to generate the CSS code for a color that matches it. Write your output in json with a single key called \"css_code\"."
  mapping_temperature         = 0
  mapping_max_tokens          = 256

  # integrate this endpoint to the AWS Gateway API.
  aws_region                                 = var.aws_region
  aws_api_gateway_rest_api_parent_id         = aws_api_gateway_resource.examples.id
  aws_api_gateway_rest_api_id                = aws_api_gateway_rest_api.openai.id
  aws_lambda_function_openai_text_invoke_arn = aws_lambda_function.openai_text.invoke_arn
  aws_lambda_function_openai_text            = aws_lambda_function.openai_text.function_name
  aws_iam_role_arn                           = aws_iam_role.apigateway.arn
}
