# Grammar correction

## Usage

```console
curl --location --request PUT 'https://ntivxlkmv7.execute-api.us-east-1.amazonaws.com/v1/default-grammar' \
--header 'x-api-key: dOQAFTyJ8c7OnTJxlde3G8NFo4iRnRrA6j1IZyF3' \
--header 'Content-Type: application/json' \
--data '{
    "model": "gpt-3.5-turbo",
    "end_point": "ChatCompletion",
    "messages": [
        {"role": "user", "content": "She no went to the market."}
        ]
}'```

## Sample results

```json
{
    "id": "chatcmpl-7y5TvSLe4m1oU1cxPC5qX7fI4HCL9",
    "object": "chat.completion",
    "created": 1694555107,
    "model": "gpt-3.5-turbo-0613",
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

[https://platform.openai.com/examples/default-grammar](https://platform.openai.com/examples/default-grammar)

![OpenAI Settings](https://raw.githubusercontent.com/FullStackWithLawrence/aws-openai/main/doc/openai-settings.png "OpenAI Settings")
