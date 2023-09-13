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

###############################################################################
# 14. see https://platform.openai.com/examples/default-vr-fitness
###############################################################################
module "default_vr_fitness" {
  source    = "./endpoint"
  path_part = "default-vr-fitness"

  # OpenAI application definition
  mapping_end_point   = "ChatCompletion"
  mapping_model       = "gpt-3.5-turbo"
  mapping_temperature = 0.6
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
# 15. see https://platform.openai.com/examples/default-marv-sarcastic-chat
###############################################################################
module "default_marv_sarcastic_chat" {
  source    = "./endpoint"
  path_part = "default-marv-sarcastic-chat"

  # OpenAI application definition
  mapping_end_point           = "ChatCompletion"
  mapping_model               = "gpt-3.5-turbo"
  mapping_role_system_content = "You are Marv, a chatbot that reluctantly answers questions with sarcastic responses."
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
# 16. see https://platform.openai.com/examples/default-turn-by-turn-directions
###############################################################################
module "default_turn_by_turn_directions" {
  source    = "./endpoint"
  path_part = "default-turn-by-turn-directions"

  # OpenAI application definition
  mapping_end_point           = "ChatCompletion"
  mapping_model               = "gpt-3.5-turbo"
  mapping_role_system_content = "You will be provided with a text, and your task is to create a numbered list of turn-by-turn directions from it."
  mapping_temperature         = 0.3
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
# 17. see https://platform.openai.com/examples/default-interview-questions
###############################################################################
module "default_interview_questions" {
  source    = "./endpoint"
  path_part = "default-interview-questions"

  # OpenAI application definition
  mapping_end_point   = "ChatCompletion"
  mapping_model       = "gpt-3.5-turbo"
  mapping_temperature = 0.5
  mapping_max_tokens  = 1024

  # integrate this endpoint to the AWS Gateway API.
  aws_region                                 = var.aws_region
  aws_api_gateway_rest_api_parent_id         = aws_api_gateway_resource.examples.id
  aws_api_gateway_rest_api_id                = aws_api_gateway_rest_api.openai.id
  aws_lambda_function_openai_text_invoke_arn = aws_lambda_function.openai_text.invoke_arn
  aws_lambda_function_openai_text            = aws_lambda_function.openai_text.function_name
  aws_iam_role_arn                           = aws_iam_role.apigateway.arn
}

###############################################################################
# 18. see https://platform.openai.com/examples/default-function-from-spec
###############################################################################
module "default_function_from_spec" {
  source    = "./endpoint"
  path_part = "default-function-from-spec"

  # OpenAI application definition
  mapping_end_point   = "ChatCompletion"
  mapping_model       = "gpt-4"
  mapping_temperature = 0
  mapping_max_tokens  = 1024

  # integrate this endpoint to the AWS Gateway API.
  aws_region                                 = var.aws_region
  aws_api_gateway_rest_api_parent_id         = aws_api_gateway_resource.examples.id
  aws_api_gateway_rest_api_id                = aws_api_gateway_rest_api.openai.id
  aws_lambda_function_openai_text_invoke_arn = aws_lambda_function.openai_text.invoke_arn
  aws_lambda_function_openai_text            = aws_lambda_function.openai_text.function_name
  aws_iam_role_arn                           = aws_iam_role.apigateway.arn
}

###############################################################################
# 19. see https://platform.openai.com/examples/default-code-improvement
###############################################################################
module "default_code_improvement" {
  source    = "./endpoint"
  path_part = "default-code-improvement"

  # OpenAI application definition
  mapping_end_point           = "ChatCompletion"
  mapping_model               = "gpt-4"
  mapping_role_system_content = "You will be provided with a piece of Python code, and your task is to provide ideas for efficiency improvements."
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
# 20. see https://platform.openai.com/examples/default-single-page-website
###############################################################################
module "default_single_page_website" {
  source    = "./endpoint"
  path_part = "default-single-page-website"

  # OpenAI application definition
  mapping_end_point   = "ChatCompletion"
  mapping_model       = "gpt-4"
  mapping_temperature = 0
  mapping_max_tokens  = 2048

  # integrate this endpoint to the AWS Gateway API.
  aws_region                                 = var.aws_region
  aws_api_gateway_rest_api_parent_id         = aws_api_gateway_resource.examples.id
  aws_api_gateway_rest_api_id                = aws_api_gateway_rest_api.openai.id
  aws_lambda_function_openai_text_invoke_arn = aws_lambda_function.openai_text.invoke_arn
  aws_lambda_function_openai_text            = aws_lambda_function.openai_text.function_name
  aws_iam_role_arn                           = aws_iam_role.apigateway.arn
}

###############################################################################
# 21. see https://platform.openai.com/examples/default-rap-battle
###############################################################################
module "default_rap_battle" {
  source    = "./endpoint"
  path_part = "default-rap-battle"

  # OpenAI application definition
  mapping_end_point   = "ChatCompletion"
  mapping_model       = "gpt-4"
  mapping_temperature = 0.8
  mapping_max_tokens  = 1024

  # integrate this endpoint to the AWS Gateway API.
  aws_region                                 = var.aws_region
  aws_api_gateway_rest_api_parent_id         = aws_api_gateway_resource.examples.id
  aws_api_gateway_rest_api_id                = aws_api_gateway_rest_api.openai.id
  aws_lambda_function_openai_text_invoke_arn = aws_lambda_function.openai_text.invoke_arn
  aws_lambda_function_openai_text            = aws_lambda_function.openai_text.function_name
  aws_iam_role_arn                           = aws_iam_role.apigateway.arn
}

###############################################################################
# 22. see https://platform.openai.com/examples/default-memo-writer
###############################################################################
module "default_memo_writer" {
  source    = "./endpoint"
  path_part = "default-memo-writer"

  # OpenAI application definition
  mapping_end_point   = "ChatCompletion"
  mapping_model       = "gpt-4"
  mapping_temperature = 0
  mapping_max_tokens  = 1024

  # integrate this endpoint to the AWS Gateway API.
  aws_region                                 = var.aws_region
  aws_api_gateway_rest_api_parent_id         = aws_api_gateway_resource.examples.id
  aws_api_gateway_rest_api_id                = aws_api_gateway_rest_api.openai.id
  aws_lambda_function_openai_text_invoke_arn = aws_lambda_function.openai_text.invoke_arn
  aws_lambda_function_openai_text            = aws_lambda_function.openai_text.function_name
  aws_iam_role_arn                           = aws_iam_role.apigateway.arn
}

###############################################################################
# 23. see https://platform.openai.com/examples/default-emoji-chatbot
###############################################################################
module "default_emoji_chatbot" {
  source    = "./endpoint"
  path_part = "default-emoji-chatbot"

  # OpenAI application definition
  mapping_end_point           = "ChatCompletion"
  mapping_model               = "gpt-4"
  mapping_role_system_content = "You will be provided with a message, and your task is to respond using emojis only."
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
# 24. see https://platform.openai.com/examples/default-translation
###############################################################################
module "default_translation" {
  source    = "./endpoint"
  path_part = "default-translation"

  # OpenAI application definition
  mapping_end_point           = "ChatCompletion"
  mapping_model               = "gpt-4"
  mapping_role_system_content = "You will be provided with a sentence in English, and your task is to translate it into French."
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
# 25. see https://platform.openai.com/examples/default-socratic-tutor
###############################################################################
module "default_socratic_tutor" {
  source    = "./endpoint"
  path_part = "default-socratic-tutor"

  # OpenAI application definition
  mapping_end_point           = "ChatCompletion"
  mapping_model               = "gpt-4"
  mapping_role_system_content = <<EOH
  You are a Socratic tutor. Use the following principles in responding to students:
- Ask thought-provoking, open-ended questions that challenge students' preconceptions and encourage them to engage in deeper reflection and critical thinking.
- Facilitate open and respectful dialogue among students, creating an environment where diverse viewpoints are valued and students feel comfortable sharing their ideas.
- Actively listen to students' responses, paying careful attention to their underlying thought processes and making a genuine effort to understand their perspectives.
- Guide students in their exploration of topics by encouraging them to discover answers independently, rather than providing direct answers, to enhance their reasoning and analytical skills.
- Promote critical thinking by encouraging students to question assumptions, evaluate evidence, and consider alternative viewpoints in order to arrive at well-reasoned conclusions.
- Demonstrate humility by acknowledging your own limitations and uncertainties, modeling a growth mindset and exemplifying the value of lifelong learning.
EOH
  mapping_temperature         = 0.8
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
# 26. see https://platform.openai.com/examples/default-sql-translate
###############################################################################
module "default_sql_translate" {
  source    = "./endpoint"
  path_part = "default-sql-translate"

  # OpenAI application definition
  mapping_end_point           = "ChatCompletion"
  mapping_model               = "gpt-4"
  mapping_role_system_content = <<EOH
Given the following SQL tables, your job is to write queries given a user’s request.

CREATE TABLE Orders (
  OrderID int,
  CustomerID int,
  OrderDate datetime,
  OrderTime varchar(8),
  PRIMARY KEY (OrderID)
);

CREATE TABLE OrderDetails (
  OrderDetailID int,
  OrderID int,
  ProductID int,
  Quantity int,
  PRIMARY KEY (OrderDetailID)
);

CREATE TABLE Products (
  ProductID int,
  ProductName varchar(50),
  Category varchar(50),
  UnitPrice decimal(10, 2),
  Stock int,
  PRIMARY KEY (ProductID)
);

CREATE TABLE Customers (
  CustomerID int,
  FirstName varchar(50),
  LastName varchar(50),
  Email varchar(100),
  Phone varchar(20),
  PRIMARY KEY (CustomerID)
);
EOH
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
# 27. see https://platform.openai.com/examples/default-meeting-notes-summarizer
###############################################################################
module "default_meeting_notes_summarizer" {
  source    = "./endpoint"
  path_part = "default-meeting-notes-summarizer"

  # OpenAI application definition
  mapping_end_point           = "ChatCompletion"
  mapping_model               = "gpt-4"
  mapping_role_system_content = <<EOH
You will be provided with meeting notes, and your task is to summarize the meeting as follows:

-Overall summary of discussion
-Action items (what needs to be done and who is doing it)
-If applicable, a list of topics that need to be discussed more fully in the next meeting.
EOH
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
