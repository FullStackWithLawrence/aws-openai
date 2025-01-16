# Emoji Translation

Translate regular text into emoji text.

- See [https://platform.openai.com/examples/default-emoji-translation](https://platform.openai.com/examples/default-emoji-translation)
- [Open in OpenAI Playground](https://platform.openai.com/playground/p/default-emoji-translation)

## Example Usage

```console
curl --location --request PUT 'https://api.openai.lawrencemcdaniel.com/examples/default-emoji-translation' \
--header 'x-api-key: YOUR-API-GATEWAY-KEY' \
--header 'Content-Type: application/json' \
--data '{"Artificial intelligence is a technology with great promise."}'
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
    "id": "chatcmpl-7yTuWCwvgecRstWKGGv13q4bLvXyA",
    "object": "chat.completion",
    "created": 1694649012,
    "model": "gpt-4-turbo-0613",
    "choices": [
      {
        "index": 0,
        "message": {
          "role": "assistant",
          "content": "🤖🧠💡🌟👍"
        },
        "finish_reason": "stop"
      }
    ],
    "usage": {
      "prompt_tokens": 52,
      "completion_tokens": 14,
      "total_tokens": 66
    }
  }
}
```

## Official Documentation

![OpenAI Playground](https://raw.githubusercontent.com/FullStackWithLawrence/aws-openai/main/doc/img/examples/example-04-emoji-translation.png "OpenAI Playground")
