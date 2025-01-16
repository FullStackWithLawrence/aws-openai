# Product name generator

Generate product names from a description and seed words.

- See [https://platform.openai.com/examples/default-product-name-gen](https://platform.openai.com/examples/default-product-name-gen)
- [Open in OpenAI Playground](https://platform.openai.com/playground/p/default-product-name-gen)

## Example Usage

```console
curl --location --request PUT 'https://api.openai.lawrencemcdaniel.com/examples/default-product-name-gen' \
--header 'x-api-key: YOUR-API-GATEWAY-KEY' \
--header 'Content-Type: application/json' \
--data '{"Product description: A home milkshake maker. Seed words: fast, healthy, compact."}'
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
    "id": "chatcmpl-7yTweQPrLD9ZTIIV1WU9EaaJmuxe0",
    "object": "chat.completion",
    "created": 1694649144,
    "model": "gpt-4-turbo-0613",
    "choices": [
      {
        "index": 0,
        "message": {
          "role": "assistant",
          "content": "1. SpeedBlend\n2. FitShake\n3. CompactBlend\n4. QuickMix\n5. HealthyMix\n6. PowerShake\n7. MiniShaker\n8. SlimBlend\n9. SwiftShake\n10. NutriBlend"
        },
        "finish_reason": "stop"
      }
    ],
    "usage": {
      "prompt_tokens": 50,
      "completion_tokens": 54,
      "total_tokens": 104
    }
  }
}
```

## Official Documentation

![OpenAI Playground](https://raw.githubusercontent.com/FullStackWithLawrence/aws-openai/main/doc/img/examples/example-08-product-name-gen.png "OpenAI Playground")
