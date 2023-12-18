# Translation

Translate natural language text.

- See [https://platform.openai.com/examples/default-translation](https://platform.openai.com/examples/default-translation)
- [Open in OpenAI Playground](https://platform.openai.com/playground/p/default-translation)

## Example Usage

```console
curl --location --request PUT 'https://api.openai.lawrencemcdaniel.com/examples/default-translation' \
--header 'x-api-key: YOUR-API-GATEWAY-KEY' \
--header 'Content-Type: application/json' \
--data '{"My name is Jane. What is yours?"}'
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
    "id": "chatcmpl-7yUAN58A8B4AB4ssDK4UcnlYN19Tz",
    "object": "chat.completion",
    "created": 1694649995,
    "model": "gpt-4-0613",
    "choices": [
      {
        "index": 0,
        "message": {
          "role": "assistant",
          "content": "Mon nom est Jane. Quel est le tien?"
        },
        "finish_reason": "stop"
      }
    ],
    "usage": {
      "prompt_tokens": 40,
      "completion_tokens": 12,
      "total_tokens": 52
    }
  }
}
```

## Official Documentation

![OpenAI Playground](https://raw.githubusercontent.com/FullStackWithLawrence/aws-openai/main/doc/img/examples/example-24-translation.png "OpenAI Playground")
