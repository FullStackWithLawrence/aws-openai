With input template:
{
  "model": "$util.escapeJavaScript($input.json('$.model'))",
  "messages": [
    {"role": "system", "content": "You will be provided with statements, and your task is to convert them to standard English."},
    {"role": "user", "content": "$util.escapeJavaScript($input.json('$.input_text'))"}
    ]
}
