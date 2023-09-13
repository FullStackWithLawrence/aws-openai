# Grammar correction

Simplify text to a level appropriate for a second-grade student.

## Example Usage

```console
curl --location --request PUT 'https://api.openai.lawrencemcdaniel.com/examples/default-summarize' \
--header 'x-api-key: YOUR-API-GATEWAY-KEY' \
--header 'Content-Type: application/json' \
--data '{
    "model": "gpt-3.5-turbo",
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
        "id": "chatcmpl-7yN1lU67WGts9b9yDtMflmJgIhkcz",
        "object": "chat.completion",
        "created": 1694622553,
        "model": "gpt-3.5-turbo-0613",
        "choices": [
            {
                "index": 0,
                "message": {
                    "role": "assistant",
                    "content": "Jupiter is a really big planet in our Solar System. It is the fifth planet from the Sun and it is the largest planet. It is called a gas giant because it is made mostly of gas. It is much smaller than the Sun, but it is bigger than all the other planets combined. Jupiter is very bright and can be seen in the night sky without a telescope. People have known about Jupiter for a long time. It is named after a god from ancient Rome. Sometimes it is so bright that it can make shadows on Earth. It is usually the third-brightest thing we can see at night, after the Moon and Venus."
                },
                "finish_reason": "stop"
            }
        ],
        "usage": {
            "prompt_tokens": 167,
            "completion_tokens": 130,
            "total_tokens": 297
        }
    }
}
```

## Official Documentation

[https://platform.openai.com/examples/default-summarize](https://platform.openai.com/examples/default-grasummarizemmar)

![OpenAI Settings](https://raw.githubusercontent.com/FullStackWithLawrence/aws-openai/main/doc/examples/example-02-summarize.png "OpenAI Settings")
