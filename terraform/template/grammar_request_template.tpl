With input template:
{
  "model": "gpt-3.5-turbo",
  "messages": [
    {"role": "system", "content": "You will be provided with statements, and your task is to convert them to standard English."},
    {"role": "user", "content": $util.escapeJavaScript($input.json('$.text'))}
    ]
}
