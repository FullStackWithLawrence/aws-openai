# Grammar correction

Convert ungrammatical statements into standard English.

- See [https://platform.openai.com/examples/default-grammar](https://platform.openai.com/examples/default-grammar)
- [Open in OpenAI Playground](https://platform.openai.com/playground/p/default-grammar)

## Example Usage

```console
curl --location --request PUT 'https://YOUR-API-GATEWAY-URL.amazonaws.com/v1/examples/default-grammar' \
--header 'x-api-key: YOUR-API-GATEWAY-KEY' \
--header 'Content-Type: application/json' \
--data '{"input_text": "She no went to the market."}'
```

## Example results

```json
{
  "id": "chatcmpl-7y5TvSLe4m1oU1cxPC5qX7fI4HCL9",
  "object": "chat.completion",
  "created": 1694555107,
  "model": "gpt-4-turbo-0613",
  "choices": [
    {
      "index": 0,
      "message": {
        "role": "assistant",
        "content": "The correct way to phrase this sentence would be: \"She did not go to the market.\""
      },
      "finish_reason": "stop"
    }
  ],
  "usage": {
    "prompt_tokens": 14,
    "completion_tokens": 19,
    "total_tokens": 33
  }
}
```

## Official Documentation

![OpenAI Playground](https://raw.githubusercontent.com/FullStackWithLawrence/aws-openai/main/doc/img/examples/example-01-grammar.png "OpenAI Playground")
