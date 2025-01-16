# Interview questions

Create interview questions.

- See [https://platform.openai.com/examples/default-interview-questions](https://platform.openai.com/examples/default-interview-questions)
- [Open in OpenAI Playground](https://platform.openai.com/playground/p/default-interview-questions)

## Example Usage

```console
curl --location --request PUT 'https://api.openai.lawrencemcdaniel.com/examples/default-interview-questions' \
--header 'x-api-key: YOUR-API-GATEWAY-KEY' \
--header 'Content-Type: application/json' \
--data '{"Create a list of 8 questions for an interview with a science fiction author."}'
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
    "id": "chatcmpl-7yU3L73zU6uRTO0JyDZvl3tNpuE5u",
    "object": "chat.completion",
    "created": 1694649559,
    "model": "gpt-4-turbo-0613",
    "choices": [
      {
        "index": 0,
        "message": {
          "role": "assistant",
          "content": "1. When did your interest in science fiction begin and what inspired you to start writing in this genre?\n2. What do you think makes science fiction such a popular and enduring genre?\n3. Can you tell us about your writing process? How do you develop ideas and create unique and believable worlds for your stories?\n4. Many science fiction authors explore themes of technology and its impact on society. What are some of the ethical or moral dilemmas you like to explore through your writing?\n5. In your opinion, how does science fiction reflect or comment on our current societal issues?\n6. Science fiction often involves envisioning possible futures. How do you balance scientific plausibility with creating an engaging story for readers?\n7. Can you share some of the challenges you have faced as a science fiction author and how you have overcome them in your writing journey?\n8. Science fiction has often been regarded as a genre that reflects our hopes and fears for the future. Can you discuss how your work has addressed some of these hopes and fears?"
        },
        "finish_reason": "stop"
      }
    ],
    "usage": {
      "prompt_tokens": 27,
      "completion_tokens": 207,
      "total_tokens": 234
    }
  }
}
```

## Official Documentation

![OpenAI Playground](https://raw.githubusercontent.com/FullStackWithLawrence/aws-openai/main/doc/img/examples/example-17-interview-questions.png "OpenAI Playground")
