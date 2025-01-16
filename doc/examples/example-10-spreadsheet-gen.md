# Spreadsheet creator

Create spreadsheets of various kinds of data.

- See [https://platform.openai.com/examples/default-spreadsheet-gen](https://platform.openai.com/examples/default-spreadsheet-gen)
- [Open in OpenAI Playground](https://platform.openai.com/playground/p/default-spreadsheet-gen)

## Example Usage

```console
curl --location --request PUT 'https://api.openai.lawrencemcdaniel.com/examples/default-spreadsheet-gen' \
--header 'x-api-key: YOUR-API-GATEWAY-KEY' \
--header 'Content-Type: application/json' \
--data '{"Create a two-column CSV of top science fiction movies along with the year of release."}'
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
    "id": "chatcmpl-7yTx5LQgAulaMFHvI7bffH69wsRPe",
    "object": "chat.completion",
    "created": 1694649171,
    "model": "gpt-4-turbo-0613",
    "choices": [
      {
        "index": 0,
        "message": {
          "role": "assistant",
          "content": "Movie,Year of Release\n2001: A Space Odyssey,1968\nBlade Runner,1982\nThe Matrix,1999\nStar Wars: Episode IV - A New Hope,1977\nE.T. the Extra-Terrestrial,1982\nThe Terminator,1984\nInception,2010\nBack to the Future,1985\nThe Fifth Element,1997\nWar of the Worlds,2005\nInterstellar,2014\nThe Martian,2015\nAvatar,2009\nAlien,1979\nJurassic Park,1993"
        },
        "finish_reason": "stop"
      }
    ],
    "usage": {
      "prompt_tokens": 28,
      "completion_tokens": 118,
      "total_tokens": 146
    }
  }
}
```

## Official Documentation

![OpenAI Playground](https://raw.githubusercontent.com/FullStackWithLawrence/aws-openai/main/doc/img/examples/example-10-spreadsheet-gen.png "OpenAI Playground")
