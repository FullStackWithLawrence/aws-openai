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
#    Convert ungrammatical statements into standard English.
###############################################################################
module "default_grammar" {
  source    = "./endpoint"
  path_part = "default-grammar"

  # OpenAI application definition
  mapping_object_type         = "chat.completion"
  mapping_model               = "gpt-4-turbo"
  mapping_role_system_content = "You will be provided with statements, and your task is to convert them to standard English."

  # integrate this endpoint to the AWS Gateway API.
  aws_region                                 = var.aws_region
  aws_api_gateway_rest_api_parent_id         = aws_api_gateway_resource.examples.id
  aws_api_gateway_rest_api_id                = aws_api_gateway_rest_api.openai.id
  aws_lambda_function_openai_text_invoke_arn = aws_lambda_function.lambda_openai_v2.invoke_arn
  aws_lambda_function_openai_text            = aws_lambda_function.lambda_openai_v2.function_name
  aws_iam_role_arn                           = aws_iam_role.apigateway.arn
}

###############################################################################
# 2. see https://platform.openai.com/examples/default-summarize
#    Simplify text to a level appropriate for a second-grade student.
###############################################################################
module "default_summarize" {
  source    = "./endpoint"
  path_part = "default-summarize"

  # OpenAI application definition
  mapping_object_type         = "chat.completion"
  mapping_model               = "gpt-4-turbo"
  mapping_role_system_content = "Summarize content you are provided with for a second-grade student."
  mapping_temperature         = 0
  mapping_max_tokens          = 1024

  # integrate this endpoint to the AWS Gateway API.
  aws_region                                 = var.aws_region
  aws_api_gateway_rest_api_parent_id         = aws_api_gateway_resource.examples.id
  aws_api_gateway_rest_api_id                = aws_api_gateway_rest_api.openai.id
  aws_lambda_function_openai_text_invoke_arn = aws_lambda_function.lambda_openai_v2.invoke_arn
  aws_lambda_function_openai_text            = aws_lambda_function.lambda_openai_v2.function_name
  aws_iam_role_arn                           = aws_iam_role.apigateway.arn
}

###############################################################################
# 3. see https://platform.openai.com/examples/default-parse-data
#    Create tables from unstructured text.
###############################################################################
module "default_parse_data" {
  source    = "./endpoint"
  path_part = "default-parse-data"

  # OpenAI application definition
  mapping_object_type         = "chat.completion"
  mapping_model               = "gpt-4-turbo"
  mapping_role_system_content = "You will be provided with unstructured data, and your task is to parse it into CSV format."
  mapping_temperature         = 0
  mapping_max_tokens          = 256

  # integrate this endpoint to the AWS Gateway API.
  aws_region                                 = var.aws_region
  aws_api_gateway_rest_api_parent_id         = aws_api_gateway_resource.examples.id
  aws_api_gateway_rest_api_id                = aws_api_gateway_rest_api.openai.id
  aws_lambda_function_openai_text_invoke_arn = aws_lambda_function.lambda_openai_v2.invoke_arn
  aws_lambda_function_openai_text            = aws_lambda_function.lambda_openai_v2.function_name
  aws_iam_role_arn                           = aws_iam_role.apigateway.arn
}


###############################################################################
# 4. see https://platform.openai.com/examples/default-emoji-translation
#    Translate regular text into emoji text.
###############################################################################
module "default_emoji_translation" {
  source    = "./endpoint"
  path_part = "default-emoji-translation"

  # OpenAI application definition
  mapping_object_type         = "chat.completion"
  mapping_model               = "gpt-4-turbo"
  mapping_role_system_content = "You will be provided with text, and your task is to translate it into emojis. Do not use any regular text. Do your best with emojis only."
  mapping_temperature         = 0.8
  mapping_max_tokens          = 256

  # integrate this endpoint to the AWS Gateway API.
  aws_region                                 = var.aws_region
  aws_api_gateway_rest_api_parent_id         = aws_api_gateway_resource.examples.id
  aws_api_gateway_rest_api_id                = aws_api_gateway_rest_api.openai.id
  aws_lambda_function_openai_text_invoke_arn = aws_lambda_function.lambda_openai_v2.invoke_arn
  aws_lambda_function_openai_text            = aws_lambda_function.lambda_openai_v2.function_name
  aws_iam_role_arn                           = aws_iam_role.apigateway.arn
}

###############################################################################
# 5. see https://platform.openai.com/examples/default-time-complexity
#    Find the time complexity of a function written in Python
###############################################################################
module "default_time_complexity" {
  source    = "./endpoint"
  path_part = "default-time-complexity"

  # OpenAI application definition
  mapping_object_type         = "chat.completion"
  mapping_model               = "gpt-4-turbo"
  mapping_role_system_content = "You will be provided with Python code, and your task is to calculate its time complexity."
  mapping_temperature         = 0
  mapping_max_tokens          = 256

  # integrate this endpoint to the AWS Gateway API.
  aws_region                                 = var.aws_region
  aws_api_gateway_rest_api_parent_id         = aws_api_gateway_resource.examples.id
  aws_api_gateway_rest_api_id                = aws_api_gateway_rest_api.openai.id
  aws_lambda_function_openai_text_invoke_arn = aws_lambda_function.lambda_openai_v2.invoke_arn
  aws_lambda_function_openai_text            = aws_lambda_function.lambda_openai_v2.function_name
  aws_iam_role_arn                           = aws_iam_role.apigateway.arn
}

###############################################################################
# 6. see https://platform.openai.com/examples/default-explain-code
#    Explain a complicated piece of code written in Python.
###############################################################################
module "default_explain_code" {
  source    = "./endpoint"
  path_part = "default-explain-code"

  # OpenAI application definition
  mapping_object_type         = "chat.completion"
  mapping_model               = "gpt-4"
  mapping_role_system_content = "You will be provided with a piece of code, and your task is to explain it in a concise way."
  mapping_temperature         = 0
  mapping_max_tokens          = 1024

  # integrate this endpoint to the AWS Gateway API.
  aws_region                                 = var.aws_region
  aws_api_gateway_rest_api_parent_id         = aws_api_gateway_resource.examples.id
  aws_api_gateway_rest_api_id                = aws_api_gateway_rest_api.openai.id
  aws_lambda_function_openai_text_invoke_arn = aws_lambda_function.lambda_openai_v2.invoke_arn
  aws_lambda_function_openai_text            = aws_lambda_function.lambda_openai_v2.function_name
  aws_iam_role_arn                           = aws_iam_role.apigateway.arn
}

###############################################################################
# 7. see https://platform.openai.com/examples/default-keywords
#    extract keywords from a block of text.
###############################################################################
module "default_keywords" {
  source    = "./endpoint"
  path_part = "default-keywords"

  # OpenAI application definition
  mapping_object_type         = "chat.completion"
  mapping_model               = "gpt-4-turbo"
  mapping_role_system_content = "You will be provided with a block of text, and your task is to extract a list of keywords from it."
  mapping_temperature         = 0.5
  mapping_max_tokens          = 256

  # integrate this endpoint to the AWS Gateway API.
  aws_region                                 = var.aws_region
  aws_api_gateway_rest_api_parent_id         = aws_api_gateway_resource.examples.id
  aws_api_gateway_rest_api_id                = aws_api_gateway_rest_api.openai.id
  aws_lambda_function_openai_text_invoke_arn = aws_lambda_function.lambda_openai_v2.invoke_arn
  aws_lambda_function_openai_text            = aws_lambda_function.lambda_openai_v2.function_name
  aws_iam_role_arn                           = aws_iam_role.apigateway.arn
}

###############################################################################
# 8. see https://platform.openai.com/examples/default-product-name-gen
#    Generate product names from a description and seed words.
###############################################################################
module "default_product_name_gen" {
  source    = "./endpoint"
  path_part = "default-product-name-gen"

  # OpenAI application definition
  mapping_object_type         = "chat.completion"
  mapping_model               = "gpt-4-turbo"
  mapping_role_system_content = "You will be provided with a product description and seed words, and your task is to generate product names."
  mapping_temperature         = 0.8
  mapping_max_tokens          = 256

  # integrate this endpoint to the AWS Gateway API.
  aws_region                                 = var.aws_region
  aws_api_gateway_rest_api_parent_id         = aws_api_gateway_resource.examples.id
  aws_api_gateway_rest_api_id                = aws_api_gateway_rest_api.openai.id
  aws_lambda_function_openai_text_invoke_arn = aws_lambda_function.lambda_openai_v2.invoke_arn
  aws_lambda_function_openai_text            = aws_lambda_function.lambda_openai_v2.function_name
  aws_iam_role_arn                           = aws_iam_role.apigateway.arn
}

###############################################################################
# 9. see https://platform.openai.com/examples/default-fix-python-bugs
#    Find and fix bugs in Python source code.
###############################################################################
module "default_fix_python_bugs" {
  source    = "./endpoint"
  path_part = "default-fix-python-bugs"

  # OpenAI application definition
  mapping_object_type         = "chat.completion"
  mapping_model               = "gpt-4"
  mapping_role_system_content = "You will be provided with a piece of Python code, and your task is to find and fix bugs in it."
  mapping_temperature         = 0
  mapping_max_tokens          = 1024

  # integrate this endpoint to the AWS Gateway API.
  aws_region                                 = var.aws_region
  aws_api_gateway_rest_api_parent_id         = aws_api_gateway_resource.examples.id
  aws_api_gateway_rest_api_id                = aws_api_gateway_rest_api.openai.id
  aws_lambda_function_openai_text_invoke_arn = aws_lambda_function.lambda_openai_v2.invoke_arn
  aws_lambda_function_openai_text            = aws_lambda_function.lambda_openai_v2.function_name
  aws_iam_role_arn                           = aws_iam_role.apigateway.arn
}

###############################################################################
# 10. see https://platform.openai.com/examples/default-spreadsheet-gen
#     Create spreadsheets of various kinds of data.
###############################################################################
module "default_spreadsheet_gen" {
  source    = "./endpoint"
  path_part = "default-spreadsheet-gen"

  # OpenAI application definition
  mapping_object_type         = "chat.completion"
  mapping_model               = "gpt-4-turbo"
  mapping_role_system_content = "Your task is to create spreadsheets from various kinds of data"
  mapping_temperature         = 0.5
  mapping_max_tokens          = 256

  # integrate this endpoint to the AWS Gateway API.
  aws_region                                 = var.aws_region
  aws_api_gateway_rest_api_parent_id         = aws_api_gateway_resource.examples.id
  aws_api_gateway_rest_api_id                = aws_api_gateway_rest_api.openai.id
  aws_lambda_function_openai_text_invoke_arn = aws_lambda_function.lambda_openai_v2.invoke_arn
  aws_lambda_function_openai_text            = aws_lambda_function.lambda_openai_v2.function_name
  aws_iam_role_arn                           = aws_iam_role.apigateway.arn
}

###############################################################################
# 11. see https://platform.openai.com/examples/default-tweet-classifier
#     Detect sentiment in a tweet.
###############################################################################
module "default_tweet_classifier" {
  source    = "./endpoint"
  path_part = "default-tweet-classifier"

  # OpenAI application definition
  mapping_object_type         = "chat.completion"
  mapping_model               = "gpt-4-turbo"
  mapping_role_system_content = "You will be provided with a tweet, and your task is to classify its sentiment as positive, neutral, or negative."
  mapping_temperature         = 0
  mapping_max_tokens          = 256

  # integrate this endpoint to the AWS Gateway API.
  aws_region                                 = var.aws_region
  aws_api_gateway_rest_api_parent_id         = aws_api_gateway_resource.examples.id
  aws_api_gateway_rest_api_id                = aws_api_gateway_rest_api.openai.id
  aws_lambda_function_openai_text_invoke_arn = aws_lambda_function.lambda_openai_v2.invoke_arn
  aws_lambda_function_openai_text            = aws_lambda_function.lambda_openai_v2.function_name
  aws_iam_role_arn                           = aws_iam_role.apigateway.arn
}

###############################################################################
# 12. see https://platform.openai.com/examples/default-airport-codes
#     Extract airport codes from text.
###############################################################################
module "default_airport_codes" {
  source    = "./endpoint"
  path_part = "default-airport-codes"

  # OpenAI application definition
  mapping_object_type         = "chat.completion"
  mapping_model               = "gpt-4-turbo"
  mapping_role_system_content = "You will be provided with a text, and your task is to extract the airport codes from it."
  mapping_temperature         = 0
  mapping_max_tokens          = 256

  # integrate this endpoint to the AWS Gateway API.
  aws_region                                 = var.aws_region
  aws_api_gateway_rest_api_parent_id         = aws_api_gateway_resource.examples.id
  aws_api_gateway_rest_api_id                = aws_api_gateway_rest_api.openai.id
  aws_lambda_function_openai_text_invoke_arn = aws_lambda_function.lambda_openai_v2.invoke_arn
  aws_lambda_function_openai_text            = aws_lambda_function.lambda_openai_v2.function_name
  aws_iam_role_arn                           = aws_iam_role.apigateway.arn
}

###############################################################################
# 13. see https://platform.openai.com/examples/default-mood-color
#     Turn a text description into a color.
###############################################################################
module "default_mood_color" {
  source    = "./endpoint"
  path_part = "default-mood-color"

  # OpenAI application definition
  mapping_object_type         = "chat.completion"
  mapping_model               = "gpt-4-turbo"
  mapping_role_system_content = "You will be provided with a description of a mood, and your task is to generate the CSS code for a color that matches it. Write your output in json with a single key called 'css_code'."
  mapping_temperature         = 0
  mapping_max_tokens          = 256

  # integrate this endpoint to the AWS Gateway API.
  aws_region                                 = var.aws_region
  aws_api_gateway_rest_api_parent_id         = aws_api_gateway_resource.examples.id
  aws_api_gateway_rest_api_id                = aws_api_gateway_rest_api.openai.id
  aws_lambda_function_openai_text_invoke_arn = aws_lambda_function.lambda_openai_v2.invoke_arn
  aws_lambda_function_openai_text            = aws_lambda_function.lambda_openai_v2.function_name
  aws_iam_role_arn                           = aws_iam_role.apigateway.arn
}

###############################################################################
# 14. see https://platform.openai.com/examples/default-vr-fitness
#     Generate ideas for fitness promoting virtual reality games.
###############################################################################
module "default_vr_fitness" {
  source    = "./endpoint"
  path_part = "default-vr-fitness"

  # OpenAI application definition
  mapping_object_type         = "chat.completion"
  mapping_model               = "gpt-4-turbo"
  mapping_role_system_content = "You are a helpful assistant. Your task is to generate ideas for fitness promoting virtual reality games"
  mapping_temperature         = 0.6
  mapping_max_tokens          = 256

  # integrate this endpoint to the AWS Gateway API.
  aws_region                                 = var.aws_region
  aws_api_gateway_rest_api_parent_id         = aws_api_gateway_resource.examples.id
  aws_api_gateway_rest_api_id                = aws_api_gateway_rest_api.openai.id
  aws_lambda_function_openai_text_invoke_arn = aws_lambda_function.lambda_openai_v2.invoke_arn
  aws_lambda_function_openai_text            = aws_lambda_function.lambda_openai_v2.function_name
  aws_iam_role_arn                           = aws_iam_role.apigateway.arn
}

###############################################################################
# 15. see https://platform.openai.com/examples/default-marv-sarcastic-chat
#     Marv is a factual chatbot that is also sarcastic.
#
#     Note: migrated to Langchain in v0.5.0
###############################################################################
module "default_marv_sarcastic_chat" {
  source    = "./endpoint"
  path_part = "default-marv-sarcastic-chat"

  # OpenAI application definition
  mapping_object_type         = "chat.completion"
  mapping_model               = "gpt-4-turbo"
  mapping_role_system_content = "You are Marv, a chatbot that reluctantly answers questions with sarcastic responses."
  mapping_temperature         = 0.5
  mapping_max_tokens          = 256

  # integrate this endpoint to the AWS Gateway API.
  aws_region                                 = var.aws_region
  aws_api_gateway_rest_api_parent_id         = aws_api_gateway_resource.examples.id
  aws_api_gateway_rest_api_id                = aws_api_gateway_rest_api.openai.id
  aws_lambda_function_openai_text_invoke_arn = aws_lambda_function.lambda_langchain.invoke_arn
  aws_lambda_function_openai_text            = aws_lambda_function.lambda_langchain.function_name
  aws_iam_role_arn                           = aws_iam_role.apigateway.arn
}

###############################################################################
# 16. see https://platform.openai.com/examples/default-turn-by-turn-directions
#     Convert natural language to turn-by-turn directions.
###############################################################################
module "default_turn_by_turn_directions" {
  source    = "./endpoint"
  path_part = "default-turn-by-turn-directions"

  # OpenAI application definition
  mapping_object_type         = "chat.completion"
  mapping_model               = "gpt-4-turbo"
  mapping_role_system_content = "You will be provided with a text, and your task is to create a numbered list of turn-by-turn directions from it."
  mapping_temperature         = 0.3
  mapping_max_tokens          = 256

  # integrate this endpoint to the AWS Gateway API.
  aws_region                                 = var.aws_region
  aws_api_gateway_rest_api_parent_id         = aws_api_gateway_resource.examples.id
  aws_api_gateway_rest_api_id                = aws_api_gateway_rest_api.openai.id
  aws_lambda_function_openai_text_invoke_arn = aws_lambda_function.lambda_openai_v2.invoke_arn
  aws_lambda_function_openai_text            = aws_lambda_function.lambda_openai_v2.function_name
  aws_iam_role_arn                           = aws_iam_role.apigateway.arn
}

###############################################################################
# 17. see https://platform.openai.com/examples/default-interview-questions
#     Create job interview questions.
###############################################################################
module "default_interview_questions" {
  source    = "./endpoint"
  path_part = "default-interview-questions"

  # OpenAI application definition
  mapping_object_type         = "chat.completion"
  mapping_model               = "gpt-4-turbo"
  mapping_role_system_content = "Your are a helpful assistant. Your task is to create job interview questions."
  mapping_temperature         = 0.5
  mapping_max_tokens          = 1024

  # integrate this endpoint to the AWS Gateway API.
  aws_region                                 = var.aws_region
  aws_api_gateway_rest_api_parent_id         = aws_api_gateway_resource.examples.id
  aws_api_gateway_rest_api_id                = aws_api_gateway_rest_api.openai.id
  aws_lambda_function_openai_text_invoke_arn = aws_lambda_function.lambda_openai_v2.invoke_arn
  aws_lambda_function_openai_text            = aws_lambda_function.lambda_openai_v2.function_name
  aws_iam_role_arn                           = aws_iam_role.apigateway.arn
}

###############################################################################
# 18. see https://platform.openai.com/examples/default-function-from-spec
#     Create a Python function from a specification.
###############################################################################
module "default_function_from_spec" {
  source    = "./endpoint"
  path_part = "default-function-from-spec"

  # OpenAI application definition
  mapping_object_type         = "chat.completion"
  mapping_model               = "gpt-4"
  mapping_role_system_content = "You are an expert Python programmer. Your task is to create a Python function from a specification."
  mapping_temperature         = 0
  mapping_max_tokens          = 1024

  # integrate this endpoint to the AWS Gateway API.
  aws_region                                 = var.aws_region
  aws_api_gateway_rest_api_parent_id         = aws_api_gateway_resource.examples.id
  aws_api_gateway_rest_api_id                = aws_api_gateway_rest_api.openai.id
  aws_lambda_function_openai_text_invoke_arn = aws_lambda_function.lambda_openai_v2.invoke_arn
  aws_lambda_function_openai_text            = aws_lambda_function.lambda_openai_v2.function_name
  aws_iam_role_arn                           = aws_iam_role.apigateway.arn
}

###############################################################################
# 19. see https://platform.openai.com/examples/default-code-improvement
#     Provide ideas for efficiency improvements to Python code.
###############################################################################
module "default_code_improvement" {
  source    = "./endpoint"
  path_part = "default-code-improvement"

  # OpenAI application definition
  mapping_object_type         = "chat.completion"
  mapping_model               = "gpt-4"
  mapping_role_system_content = "You will be provided with a piece of Python code, and your task is to provide ideas for efficiency improvements."
  mapping_temperature         = 0
  mapping_max_tokens          = 1024

  # integrate this endpoint to the AWS Gateway API.
  aws_region                                 = var.aws_region
  aws_api_gateway_rest_api_parent_id         = aws_api_gateway_resource.examples.id
  aws_api_gateway_rest_api_id                = aws_api_gateway_rest_api.openai.id
  aws_lambda_function_openai_text_invoke_arn = aws_lambda_function.lambda_openai_v2.invoke_arn
  aws_lambda_function_openai_text            = aws_lambda_function.lambda_openai_v2.function_name
  aws_iam_role_arn                           = aws_iam_role.apigateway.arn
}

###############################################################################
# 20. see https://platform.openai.com/examples/default-single-page-website
#     Create a single page website based on a spec.
###############################################################################
module "default_single_page_website" {
  source    = "./endpoint"
  path_part = "default-single-page-website"

  # OpenAI application definition
  mapping_object_type         = "chat.completion"
  mapping_model               = "gpt-4"
  mapping_role_system_content = "You are an expert front-end developer. Your task is to create a single page website based on a spec."
  mapping_temperature         = 0
  mapping_max_tokens          = 2048

  # integrate this endpoint to the AWS Gateway API.
  aws_region                                 = var.aws_region
  aws_api_gateway_rest_api_parent_id         = aws_api_gateway_resource.examples.id
  aws_api_gateway_rest_api_id                = aws_api_gateway_rest_api.openai.id
  aws_lambda_function_openai_text_invoke_arn = aws_lambda_function.lambda_openai_v2.invoke_arn
  aws_lambda_function_openai_text            = aws_lambda_function.lambda_openai_v2.function_name
  aws_iam_role_arn                           = aws_iam_role.apigateway.arn
}

###############################################################################
# 21. see https://platform.openai.com/examples/default-rap-battle
#     Generate a rap battle between two characters.
###############################################################################
module "default_rap_battle" {
  source    = "./endpoint"
  path_part = "default-rap-battle"

  # OpenAI application definition
  mapping_object_type         = "chat.completion"
  mapping_model               = "gpt-4"
  mapping_role_system_content = "You are an accomplished rapper. Your task is to generate a rap battle between two characters."
  mapping_temperature         = 0.8
  mapping_max_tokens          = 1024

  # integrate this endpoint to the AWS Gateway API.
  aws_region                                 = var.aws_region
  aws_api_gateway_rest_api_parent_id         = aws_api_gateway_resource.examples.id
  aws_api_gateway_rest_api_id                = aws_api_gateway_rest_api.openai.id
  aws_lambda_function_openai_text_invoke_arn = aws_lambda_function.lambda_openai_v2.invoke_arn
  aws_lambda_function_openai_text            = aws_lambda_function.lambda_openai_v2.function_name
  aws_iam_role_arn                           = aws_iam_role.apigateway.arn
}

###############################################################################
# 22. see https://platform.openai.com/examples/default-memo-writer
#     Generate a company memo based on provided points.
###############################################################################
module "default_memo_writer" {
  source    = "./endpoint"
  path_part = "default-memo-writer"

  # OpenAI application definition
  mapping_object_type         = "chat.completion"
  mapping_model               = "gpt-4"
  mapping_role_system_content = "You are a helpful assistant. Your task is to generate a company memo based on provided points."
  mapping_temperature         = 0
  mapping_max_tokens          = 1024

  # integrate this endpoint to the AWS Gateway API.
  aws_region                                 = var.aws_region
  aws_api_gateway_rest_api_parent_id         = aws_api_gateway_resource.examples.id
  aws_api_gateway_rest_api_id                = aws_api_gateway_rest_api.openai.id
  aws_lambda_function_openai_text_invoke_arn = aws_lambda_function.lambda_openai_v2.invoke_arn
  aws_lambda_function_openai_text            = aws_lambda_function.lambda_openai_v2.function_name
  aws_iam_role_arn                           = aws_iam_role.apigateway.arn
}

###############################################################################
# 23. see https://platform.openai.com/examples/default-emoji-chatbot
#     Generate conversational replies using emojis only.
###############################################################################
module "default_emoji_chatbot" {
  source    = "./endpoint"
  path_part = "default-emoji-chatbot"

  # OpenAI application definition
  mapping_object_type         = "chat.completion"
  mapping_model               = "gpt-4"
  mapping_role_system_content = "You will be provided with a message, and your task is to respond using emojis only."
  mapping_temperature         = 0.8
  mapping_max_tokens          = 256

  # integrate this endpoint to the AWS Gateway API.
  aws_region                                 = var.aws_region
  aws_api_gateway_rest_api_parent_id         = aws_api_gateway_resource.examples.id
  aws_api_gateway_rest_api_id                = aws_api_gateway_rest_api.openai.id
  aws_lambda_function_openai_text_invoke_arn = aws_lambda_function.lambda_openai_v2.invoke_arn
  aws_lambda_function_openai_text            = aws_lambda_function.lambda_openai_v2.function_name
  aws_iam_role_arn                           = aws_iam_role.apigateway.arn
}

###############################################################################
# 24. see https://platform.openai.com/examples/default-translation
#     Translate natural language text.
###############################################################################
module "default_translation" {
  source    = "./endpoint"
  path_part = "default-translation"

  # OpenAI application definition
  mapping_object_type         = "chat.completion"
  mapping_model               = "gpt-4"
  mapping_role_system_content = "You will be provided with a sentence in English, and your task is to translate it into French."
  mapping_temperature         = 0
  mapping_max_tokens          = 256

  # integrate this endpoint to the AWS Gateway API.
  aws_region                                 = var.aws_region
  aws_api_gateway_rest_api_parent_id         = aws_api_gateway_resource.examples.id
  aws_api_gateway_rest_api_id                = aws_api_gateway_rest_api.openai.id
  aws_lambda_function_openai_text_invoke_arn = aws_lambda_function.lambda_openai_v2.invoke_arn
  aws_lambda_function_openai_text            = aws_lambda_function.lambda_openai_v2.function_name
  aws_iam_role_arn                           = aws_iam_role.apigateway.arn
}

###############################################################################
# 25. see https://platform.openai.com/examples/default-socratic-tutor
#     Generate responses as a Socratic tutor.
###############################################################################
module "default_socratic_tutor" {
  source    = "./endpoint"
  path_part = "default-socratic-tutor"

  # OpenAI application definition
  mapping_object_type         = "chat.completion"
  mapping_model               = "gpt-4"
  mapping_role_system_content = "You are a Socratic tutor. Use the following principles in responding to students: a.) Ask thought-provoking, open-ended questions that challenge preconceptions of students and encourage them to engage in deeper reflection and critical thinking. b.) Facilitate open and respectful dialogue among students, creating an environment where diverse viewpoints are valued and students feel comfortable sharing their ideas. c.) Actively listen to responses of students, paying careful attention to their underlying thought processes and making a genuine effort to understand their perspectives. d.) Guide students in their exploration of topics by encouraging them to discover answers independently, rather than providing direct answers, to enhance their reasoning and analytical skills. e.) Promote critical thinking by encouraging students to question assumptions, evaluate evidence, and consider alternative viewpoints in order to arrive at well-reasoned conclusions. f.) Demonstrate humility by acknowledging your own limitations and uncertainties, modeling a growth mindset and exemplifying the value of lifelong learning."
  mapping_temperature         = 0.8
  mapping_max_tokens          = 1024

  # integrate this endpoint to the AWS Gateway API.
  aws_region                                 = var.aws_region
  aws_api_gateway_rest_api_parent_id         = aws_api_gateway_resource.examples.id
  aws_api_gateway_rest_api_id                = aws_api_gateway_rest_api.openai.id
  aws_lambda_function_openai_text_invoke_arn = aws_lambda_function.lambda_openai_v2.invoke_arn
  aws_lambda_function_openai_text            = aws_lambda_function.lambda_openai_v2.function_name
  aws_iam_role_arn                           = aws_iam_role.apigateway.arn
}

###############################################################################
# 26. see https://platform.openai.com/examples/default-sql-translate
#     Convert natural language into SQL queries.
###############################################################################
module "default_sql_translate" {
  source    = "./endpoint"
  path_part = "default-sql-translate"

  # OpenAI application definition
  mapping_object_type         = "chat.completion"
  mapping_model               = "gpt-4"
  mapping_role_system_content = "Given the following SQL tables, your job is to write queries given a user’s request.\n\nCREATE TABLE Orders (\n  OrderID int,\n  CustomerID int,\n  OrderDate datetime,\n  OrderTime varchar(8),\n  PRIMARY KEY (OrderID)\n);\n\nCREATE TABLE OrderDetails (\n  OrderDetailID int,\n  OrderID int,\n  ProductID int,\n  Quantity int,\n  PRIMARY KEY (OrderDetailID)\n);\n\nCREATE TABLE Products (\n  ProductID int,\n  ProductName varchar(50),\n  Category varchar(50),\n  UnitPrice decimal(10, 2),\n  Stock int,\n  PRIMARY KEY (ProductID)\n);\n\nCREATE TABLE Customers (\n  CustomerID int,\n  FirstName varchar(50),\n  LastName varchar(50),\n  Email varchar(100),\n  Phone varchar(20),\n  PRIMARY KEY (CustomerID)\n);\n"
  mapping_temperature         = 0
  mapping_max_tokens          = 1024

  # integrate this endpoint to the AWS Gateway API.
  aws_region                                 = var.aws_region
  aws_api_gateway_rest_api_parent_id         = aws_api_gateway_resource.examples.id
  aws_api_gateway_rest_api_id                = aws_api_gateway_rest_api.openai.id
  aws_lambda_function_openai_text_invoke_arn = aws_lambda_function.lambda_openai_v2.invoke_arn
  aws_lambda_function_openai_text            = aws_lambda_function.lambda_openai_v2.function_name
  aws_iam_role_arn                           = aws_iam_role.apigateway.arn
}

###############################################################################
# 27. see https://platform.openai.com/examples/default-meeting-notes-summarizer
#     Summarize meeting notes including overall discussion, action items, and future topics.
###############################################################################
module "default_meeting_notes_summarizer" {
  source    = "./endpoint"
  path_part = "default-meeting-notes-summarizer"

  # OpenAI application definition
  mapping_object_type         = "chat.completion"
  mapping_model               = "gpt-4"
  mapping_role_system_content = "You will be provided with meeting notes, and your task is to summarize the meeting as follows:\n\n-Overall summary of discussion\n-Action items (what needs to be done and who is doing it)\n-If applicable, a list of topics that need to be discussed more fully in the next meeting.\n"
  mapping_temperature         = 0
  mapping_max_tokens          = 1024

  # integrate this endpoint to the AWS Gateway API.
  aws_region                                 = var.aws_region
  aws_api_gateway_rest_api_parent_id         = aws_api_gateway_resource.examples.id
  aws_api_gateway_rest_api_id                = aws_api_gateway_rest_api.openai.id
  aws_lambda_function_openai_text_invoke_arn = aws_lambda_function.lambda_openai_v2.invoke_arn
  aws_lambda_function_openai_text            = aws_lambda_function.lambda_openai_v2.function_name
  aws_iam_role_arn                           = aws_iam_role.apigateway.arn
}

###############################################################################
# 28. see https://platform.openai.com/examples/default-review-classifier
#     Classify user reviews based on a set of tags.
###############################################################################
module "default_review_classifier" {
  source    = "./endpoint"
  path_part = "default-review-classifier"

  # OpenAI application definition
  mapping_object_type         = "chat.completion"
  mapping_model               = "gpt-4"
  mapping_role_system_content = "You will be presented with user reviews and your job is to provide a set of tags from the following list. Provide your answer in bullet point form. Choose ONLY from the list of tags provided here (choose either the positive or the negative tag but NOT both):\n\n- Provides good value for the price OR Costs too much\n- Works better than expected OR Did not work as well as expected\n- Includes essential features OR Lacks essential features\n- Easy to use OR Difficult to use\n- High quality and durability OR Poor quality and durability\n- Easy and affordable to maintain or repair OR Difficult or costly to maintain or repair\n- Easy to transport OR Difficult to transport\n- Easy to store OR Difficult to store\n- Compatible with other devices or systems OR Not compatible with other devices or systems\n- Safe and user-friendly OR Unsafe or hazardous to use\n- Excellent customer support OR Poor customer support\n- Generous and comprehensive warranty OR Limited or insufficient warranty\n"
  mapping_temperature         = 0
  mapping_max_tokens          = 1024

  # integrate this endpoint to the AWS Gateway API.
  aws_region                                 = var.aws_region
  aws_api_gateway_rest_api_parent_id         = aws_api_gateway_resource.examples.id
  aws_api_gateway_rest_api_id                = aws_api_gateway_rest_api.openai.id
  aws_lambda_function_openai_text_invoke_arn = aws_lambda_function.lambda_openai_v2.invoke_arn
  aws_lambda_function_openai_text            = aws_lambda_function.lambda_openai_v2.function_name
  aws_iam_role_arn                           = aws_iam_role.apigateway.arn
}

###############################################################################
# 29. see https://platform.openai.com/examples/default-pro-con-discusser
#     Analyze the pros and cons of a given topic.
###############################################################################
module "default_pro_con_discusser" {
  source    = "./endpoint"
  path_part = "default-pro-con-discusser"

  # OpenAI application definition
  mapping_object_type         = "chat.completion"
  mapping_model               = "gpt-4"
  mapping_role_system_content = "You are a helpful assistant. Your task is to analyze the pros and cons of a given topic."
  mapping_temperature         = 0.8
  mapping_max_tokens          = 1024

  # integrate this endpoint to the AWS Gateway API.
  aws_region                                 = var.aws_region
  aws_api_gateway_rest_api_parent_id         = aws_api_gateway_resource.examples.id
  aws_api_gateway_rest_api_id                = aws_api_gateway_rest_api.openai.id
  aws_lambda_function_openai_text_invoke_arn = aws_lambda_function.lambda_openai_v2.invoke_arn
  aws_lambda_function_openai_text            = aws_lambda_function.lambda_openai_v2.function_name
  aws_iam_role_arn                           = aws_iam_role.apigateway.arn
}

###############################################################################
# 30. see https://platform.openai.com/examples/default-lesson-plan-writer
#     Generate a lesson plan for a specific topic.
###############################################################################
module "default_lesson_plan_writer" {
  source    = "./endpoint"
  path_part = "default-lesson-plan-writer"

  # OpenAI application definition
  mapping_object_type         = "chat.completion"
  mapping_model               = "gpt-4"
  mapping_role_system_content = "You are an experienced teacher. Your task is to generate a lesson plan for a specific topic."
  mapping_temperature         = 0.8
  mapping_max_tokens          = 2048

  # integrate this endpoint to the AWS Gateway API.
  aws_region                                 = var.aws_region
  aws_api_gateway_rest_api_parent_id         = aws_api_gateway_resource.examples.id
  aws_api_gateway_rest_api_id                = aws_api_gateway_rest_api.openai.id
  aws_lambda_function_openai_text_invoke_arn = aws_lambda_function.lambda_openai_v2.invoke_arn
  aws_lambda_function_openai_text            = aws_lambda_function.lambda_openai_v2.function_name
  aws_iam_role_arn                           = aws_iam_role.apigateway.arn
}

###############################################################################
# 31. Openai function calling example
#
#
###############################################################################
module "openai_function_calling" {
  source    = "./endpoint"
  path_part = "openai-function-calling"

  # OpenAI application definition
  mapping_object_type         = "chat.completion"
  mapping_model               = "gpt-4-turbo"
  mapping_role_system_content = "You are a helpful assistant. You were created by Lawrence McDaniel (or just Lawrence) in January, 2024."
  mapping_max_tokens          = 2048

  # integrate this endpoint to the AWS Gateway API.
  aws_region                                 = var.aws_region
  aws_api_gateway_rest_api_parent_id         = aws_api_gateway_resource.examples.id
  aws_api_gateway_rest_api_id                = aws_api_gateway_rest_api.openai.id
  aws_lambda_function_openai_text_invoke_arn = aws_lambda_function.lambda_openai_function.invoke_arn
  aws_lambda_function_openai_text            = aws_lambda_function.lambda_openai_function.function_name
  aws_iam_role_arn                           = aws_iam_role.apigateway.arn
}
