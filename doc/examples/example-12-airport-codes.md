# Airport code extractor

Extract airport codes from text.

- See [https://platform.openai.com/examples/default-airport-codes](https://platform.openai.com/examples/default-airport-codes)
- [Open in OpenAI Playground](https://platform.openai.com/playground/p/default-airport-codes)

## Example Usage

```console
curl --location --request PUT 'https://api.openai.lawrencemcdaniel.com/examples/default-airport-codes' \
--header 'x-api-key: YOUR-API-GATEWAY-KEY' \
--header 'Content-Type: application/json' \
--data '{"I want to fly from Orlando to Boston"}'
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
    "id": "chatcmpl-7yTxxjFtIQ28fRyUgcDejHq4KytP8",
    "object": "chat.completion",
    "created": 1694649225,
    "model": "gpt-4-turbo-0613",
    "choices": [
      {
        "index": 0,
        "message": {
          "role": "assistant",
          "content": "The airport code for Orlando is MCO, and the airport code for Boston is BOS."
        },
        "finish_reason": "stop"
      }
    ],
    "usage": {
      "prompt_tokens": 39,
      "completion_tokens": 19,
      "total_tokens": 58
    }
  }
}
```

## Official Documentation

![OpenAI Playground](https://raw.githubusercontent.com/FullStackWithLawrence/aws-openai/main/doc/img/examples/example-12-airport-codes.png "OpenAI Playground")
