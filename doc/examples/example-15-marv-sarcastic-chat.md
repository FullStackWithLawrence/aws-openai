# Marv the sarcastic chat bot

Marv is a factual chatbot that is also sarcastic.

- See [https://platform.openai.com/examples/default-marv-sarcastic-chat](https://platform.openai.com/examples/default-marv-sarcastic-chat)
- [Open in OpenAI Playground](https://platform.openai.com/playground/p/default-marv-sarcastic-chat)

## Example Usage

```console
curl --location --request PUT 'https://api.openai.lawrencemcdaniel.com/examples/default-marv-sarcastic-chat' \
--header 'x-api-key: YOUR-API-GATEWAY-KEY' \
--header 'Content-Type: application/json' \
--data '{"How many pounds are in a kilogram?"}'
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
    "id": "chatcmpl-7yU2U5PzOyaOuOXMuz0a0rKYBn5C9",
    "object": "chat.completion",
    "created": 1694649506,
    "model": "gpt-4-turbo-0613",
    "choices": [
      {
        "index": 0,
        "message": {
          "role": "assistant",
          "content": "Oh, let me grab my calculator and do some rocket science for you. Just kidding! It's 2.20462 pounds in a kilogram. Now go lift some weights or something."
        },
        "finish_reason": "stop"
      }
    ],
    "usage": {
      "prompt_tokens": 37,
      "completion_tokens": 39,
      "total_tokens": 76
    }
  }
}
```

## Official Documentation

![OpenAI Playground](https://raw.githubusercontent.com/FullStackWithLawrence/aws-openai/main/doc/img/examples/example-15-marv-sarcastic-chat.png "OpenAI Playground")
