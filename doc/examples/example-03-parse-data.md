# Parse unstructured data

Create tables from unstructured text.

- See [https://platform.openai.com/examples/default-parse-data](https://platform.openai.com/examples/default-parse-data)
- [Open in OpenAI Playground](https://platform.openai.com/playground/p/default-parse-data)

## Example Usage

```console
curl --location --request PUT 'https://api.openai.lawrencemcdaniel.com/examples/default-parse-data' \
--header 'x-api-key: YOUR-API-GATEWAY-KEY' \
--header 'Content-Type: application/json' \
--data '{
    "input_text": "There are many fruits that were found on the recently discovered planet Goocrux. There are neoskizzles that grow there, which are purple and taste like candy. There are also loheckles, which are a grayish blue fruit and are very tart, a little bit like a lemon. Pounits are a bright green color and are more savory than sweet. There are also plenty of loopnovas which are a neon pink flavor and taste like cotton candy. Finally, there are fruits called glowls, which have a very sour and bitter taste which is acidic and caustic, and a pale orange tinge to them."
}'
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
    "id": "chatcmpl-7yTtGjKLP0wq1Vz4I5dRpLYbFvB7I",
    "object": "chat.completion",
    "created": 1694648934,
    "model": "gpt-4-turbo-0613",
    "choices": [
      {
        "index": 0,
        "message": {
          "role": "assistant",
          "content": "Fruit,Color,Flavor\nNeoskizzles,Purple,Candy\nLoheckles,Grayish blue,Tart\nPounits,Bright green,Savory\nLoopnovas,Neon pink,Cotton candy\nGlowls,Pale orange,Sour and bitter"
        },
        "finish_reason": "stop"
      }
    ],
    "usage": {
      "prompt_tokens": 161,
      "completion_tokens": 59,
      "total_tokens": 220
    }
  }
}
```

## Official Documentation

![OpenAI Playground](https://raw.githubusercontent.com/FullStackWithLawrence/aws-openai/main/doc/img/examples/example-03-parse-data.png "OpenAI Playground")
