# Turn by turn directions

Convert natural language to turn-by-turn directions.

- See [https://platform.openai.com/examples/default-turn-by-turn-directions](https://platform.openai.com/examples/default-turn-by-turn-directions)
- [Open in OpenAI Playground](https://platform.openai.com/playground/p/default-turn-by-turn-directions)

## Example Usage

```console
curl --location --request PUT 'https://api.openai.lawrencemcdaniel.com/examples/default-turn-by-turn-directions' \
--header 'x-api-key: YOUR-API-GATEWAY-KEY' \
--header 'Content-Type: application/json' \
--data '{"Go south on 95 until you hit Sunrise boulevard then take it east to us 1 and head south. Tom Jenkins bbq will be on the left after several miles."}'
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
    "id": "chatcmpl-7yU31Yp12omgjVmZfM4jcyxMbidDp",
    "object": "chat.completion",
    "created": 1694649539,
    "model": "gpt-4-turbo-0613",
    "choices": [
      {
        "index": 0,
        "message": {
          "role": "assistant",
          "content": "1. Start by going south on 95.\n2. Continue on 95 until you reach Sunrise Boulevard.\n3. Take Sunrise Boulevard and go east.\n4. Follow Sunrise Boulevard until you reach US 1.\n5. Turn left onto US 1 and head south.\n6. Keep driving on US 1 for several miles.\n7. Look for Tom Jenkins BBQ on your left-hand side."
        },
        "finish_reason": "stop"
      }
    ],
    "usage": {
      "prompt_tokens": 72,
      "completion_tokens": 80,
      "total_tokens": 152
    }
  }
}
```

## Official Documentation

![OpenAI Playground](https://raw.githubusercontent.com/FullStackWithLawrence/aws-openai/main/doc/img/examples/example-16-turn-by-turn-directions.png "OpenAI Playground")
