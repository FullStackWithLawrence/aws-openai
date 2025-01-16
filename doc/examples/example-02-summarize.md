# Summarize for a 2nd grader

Simplify text to a level appropriate for a second-grade student.

- See [https://platform.openai.com/examples/default-summarize](https://platform.openai.com/examples/default-summarize)
- [Open in OpenAI Playground](https://platform.openai.com/playground/p/default-summarize)

## Example Usage

```console
curl --location --request PUT 'https://api.openai.lawrencemcdaniel.com/examples/default-summarize' \
--header 'x-api-key: YOUR-API-GATEWAY-KEY' \
--header 'Content-Type: application/json' \
--data '{
    "input_text": "Jupiter is a really big planet in our Solar System. It is the fifth planet from the Sun and it is the largest planet. It is called a gas giant because it is made mostly of gas. Jupiter is much smaller than the Sun, but it is bigger than all the other planets combined. It is very bright and can be seen in the night sky without a telescope. People have known about Jupiter for a very long time, even before they started writing things down. It is named after a god from ancient Rome. Sometimes, Jupiter is so bright that it can make shadows on Earth. It is usually the third-brightest thing we can see in the night sky, after the Moon and Venus."
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
    "id": "chatcmpl-7yTflEBQpKxSpKN5MZtnvCLoSkoDM",
    "object": "chat.completion",
    "created": 1694648097,
    "model": "gpt-4-turbo-0613",
    "choices": [
      {
        "index": 0,
        "message": {
          "role": "assistant",
          "content": "Jupiter is a really big and bright planet in our Solar System. It is the fifth planet from the Sun and it is the largest planet. It is called a gas giant because it is made mostly of gas. Even though it is smaller than the Sun, it is bigger than all the other planets put together. People have known about Jupiter for a very long time, even before they started writing things down. It is named after a god from ancient Rome. Jupiter is so bright that it can sometimes make shadows on Earth. It is usually the third-brightest thing we can see in the night sky, after the Moon and Venus."
        },
        "finish_reason": "stop"
      }
    ],
    "usage": {
      "prompt_tokens": 167,
      "completion_tokens": 128,
      "total_tokens": 295
    }
  }
}
```

## Official Documentation

![OpenAI Playground](https://raw.githubusercontent.com/FullStackWithLawrence/aws-openai/main/doc/img/examples/example-02-summarize.png "OpenAI Playground")
