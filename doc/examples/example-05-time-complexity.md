# Calculate time complexity

Find the time complexity of a function.

- See [https://platform.openai.com/examples/default-time-complexity](https://platform.openai.com/examples/default-time-complexity)
- [Open in OpenAI Playground](https://platform.openai.com/playground/p/default-time-complexity)

## Example Usage

```console
curl --location --request PUT 'https://api.openai.lawrencemcdaniel.com/examples/default-time-complexity' \
--header 'x-api-key: YOUR-API-GATEWAY-KEY' \
--header 'Content-Type: application/json' \
--data '{
    "input_text": "def foo(n, k):\\r\\n    accum = 0\\r\\n    for i in range(n):\\r\\n        for l in range(k):\\r\\n            accum += i\\r\\n    return accum\\r\\n"
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
    "id": "chatcmpl-7yUXtcSDMvMWI0eldblWaFa3UGc4d",
    "object": "chat.completion",
    "created": 1694651453,
    "model": "gpt-4-turbo-0613",
    "choices": [
      {
        "index": 0,
        "message": {
          "role": "assistant",
          "content": "The time complexity of the code is O(n * k), where n and k are the inputs to the function.\n\nThe outer loop runs 'n' times, and the inner loop runs 'k' times for each iteration of the outer loop. Therefore, the total number of iterations of the inner loop is n * k.\n\nInside the loops, we have a constant-time operation 'accum += i', which takes O(1) time.\n\nHence, the overall time complexity of the code is O(n * k)."
        },
        "finish_reason": "stop"
      }
    ],
    "usage": {
      "prompt_tokens": 64,
      "completion_tokens": 104,
      "total_tokens": 168
    }
  }
}
```

## Official Documentation

![OpenAI Playground](https://raw.githubusercontent.com/FullStackWithLawrence/aws-openai/main/doc/img/examples/example-05-time-complexity.png "OpenAI Playground")
