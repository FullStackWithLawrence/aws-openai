# Tweet classifier

Detect sentiment in a tweet.

- See [https://platform.openai.com/examples/default-tweet-classifier](https://platform.openai.com/examples/default-tweet-classifier)
- [Open in OpenAI Playground](https://platform.openai.com/playground/p/default-tweet-classifier)

## Example Usage

```console
curl --location --request PUT 'https://api.openai.lawrencemcdaniel.com/examples/default-tweet-classifier' \
--header 'x-api-key: YOUR-API-GATEWAY-KEY' \
--header 'Content-Type: application/json' \
--data '{"I loved the new Batman movie!"}'
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
    "id": "chatcmpl-7yTxXj4nCx4xpjL9fWACgn5mwgEHw",
    "object": "chat.completion",
    "created": 1694649199,
    "model": "gpt-4-turbo-0613",
    "choices": [
      {
        "index": 0,
        "message": {
          "role": "assistant",
          "content": "positive"
        },
        "finish_reason": "stop"
      }
    ],
    "usage": {
      "prompt_tokens": 42,
      "completion_tokens": 1,
      "total_tokens": 43
    }
  }
}
```

## Official Documentation

![OpenAI Playground](https://raw.githubusercontent.com/FullStackWithLawrence/aws-openai/main/doc/img/examples/example-11-tweet-classifier.png "OpenAI Playground")
