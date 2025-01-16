# Mood to color

Turn a text description into a color.

- See [https://platform.openai.com/examples/default-mood-color](https://platform.openai.com/examples/default-mood-color)
- [Open in OpenAI Playground](https://platform.openai.com/playground/p/default-mood-color)

## Example Usage

```console
curl --location --request PUT 'https://api.openai.lawrencemcdaniel.com/examples/default-mood-color' \
--header 'x-api-key: YOUR-API-GATEWAY-KEY' \
--header 'Content-Type: application/json' \
--data '{"Blue sky at dusk."}'
```

## Example results

```json
{
  "isBase64Encoded": false,
  "statusCode": 200,
  "headers": {
    "Content-Type": "application/json"
  },
  "body": {
    "id": "chatcmpl-7yUfR6uI3iC12pDzpJQUWCDujVDMs",
    "object": "chat.completion",
    "created": 1694651921,
    "model": "gpt-4-turbo-0613",
    "choices": [
      {
        "index": 0,
        "message": {
          "role": "assistant",
          "content": "{\n  \"css_code\": \"background-color: #24556a;\"\n}"
        },
        "finish_reason": "stop"
      }
    ],
    "usage": {
      "prompt_tokens": 57,
      "completion_tokens": 16,
      "total_tokens": 73
    }
  }
}
```

## Official Documentation

![OpenAI Playground](https://raw.githubusercontent.com/FullStackWithLawrence/aws-openai/main/doc/img/examples/example-13-mood-color.png "OpenAI Playground")
