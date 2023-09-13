## see https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-mapping-template-reference.html
{
  "model": "$input.path('$.model')",
  "end_point": "ChatCompletion",
  "messages": [
    {"role": "system", "content": "You will be provided with statements, and your task is to convert them to standard English."},
    {"role": "user", "content": "$input.path('$.input_text')"}
    ]
}
