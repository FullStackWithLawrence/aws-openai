# AWS Lambda - openai_text

## Environment Variables

| Variable                   | Example value                |
| -------------------------- | ---------------------------- |
| DEBUG_MODE                 | true                         |
| OPENAI_API_KEY             | sk-7DoB4YOUR-OPENAI-API-KEY  |
| OPENAI_API_ORGANIZATION    | org-YJz82abcdefthijklmnophcy |
| OPENAI_ENDPOINT_IMAGE_N    | 4                            |
| OPENAI_ENDPOINT_IMAGE_SIZE | 1024x768                     |

## Logging

### environment dump

Generated when DEBUG_MODEL=true

```json
{
  "environment": {
    "os": "posix",
    "system": "Linux",
    "release": "5.10.184-194.730.amzn2.x86_64",
    "openai": "0.28.0",
    "openai_app_info": null,
    "openai_end_points": [
      "Embedding",
      "ChatCompletion",
      "Moderation",
      "Image",
      "Audio",
      "Model"
    ],
    "DEBUG_MODE": true
  }
}
```

## event dump

Generated when DEBUG_MODEL=true

```json
{
  "event": {
    "model": "gpt-4-turbo",
    "end_point": "ChatCompletion",
    "messages": [
      {
        "role": "system",
        "content": "You will be provided with statements, and your task is to convert them to standard English."
      },
      {
        "role": "user",
        "content": "imma bust you upside the head"
      }
    ]
  }
}
```

### response dump

Generated when DEBUG_MODEL=true

````json
{
    "retval": {
        "isBase64Encoded": false,
        "statusCode": 200,
        "headers": {
            "Content-Type": "application/json"
        },
        "body": {
            "id": "chatcmpl-7yLQhuumejaNNSCzKqDD6SPgOCHfe",
            "object": "chat.completion",
            "created": 1694616411,
            "model": "gpt-4-turbo-0613",
            "choices": [
                {
                    "index": 0,
                    "message": {
                        "role": "assistant",
                        "content": "I am going to hit you on the head."
                    },
                    "finish_reason": "stop"
                }
            ],
            "usage": {
                "prompt_tokens": 36,
                "completion_tokens": 10,
                "total_tokens": 46
            }
        }
    }
}```
````
