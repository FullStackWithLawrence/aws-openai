## see https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-mapping-template-reference.html
{
  "object_type": "${mapping_object_type}",
  "model": "${mapping_model}",
  "end_point": "${mapping_end_point}",
  "temperature": ${mapping_temperature},
  "max_tokens": ${mapping_max_tokens},
  "messages": [
    {"role": "system", "content": "${mapping_role_system_content}"},
    {"role": "user", "content": "$input.path('$.input_text')"}
    ],
  "input_text": "$input.path('$.input_text')",
  "chat_history": $input.path('$.chat_history')
}
