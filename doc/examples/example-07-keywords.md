# Explain code

Extract keywords from a block of text.

- See [https://platform.openai.com/examples/default-keywords](https://platform.openai.com/examples/default-keywords)
- [Open in OpenAI Playground](https://platform.openai.com/playground/p/default-keywords)

## Example Usage

```console
curl --location --request PUT 'https://api.openai.lawrencemcdaniel.com/examples/default-keywords' \
--header 'x-api-key: YOUR-API-GATEWAY-KEY' \
--header 'Content-Type: application/json' \
--data '{"Black-on-black ware is a 20th- and 21st-century pottery tradition developed by the Puebloan Native American ceramic artists in Northern New Mexico. Traditional reduction-fired blackware has been made for centuries by pueblo artists. Black-on-black ware of the past century is produced with a smooth surface, with the designs applied through selective burnishing or the application of refractory slip. Another style involves carving or incising designs and selectively polishing the raised areas. For generations several families from Kha'po Owingeh and P'ohwhóge Owingeh pueblos have been making black-on-black ware with the techniques passed down from matriarch potters. Artists from other pueblos have also produced black-on-black ware. Several contemporary artists have created works honoring the pottery of their ancestors."}'
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
    "id": "chatcmpl-7yTwFseUXth0Jju4SRdvs9T3r4W8Y",
    "object": "chat.completion",
    "created": 1694649119,
    "model": "gpt-4-turbo-0613",
    "choices": [
      {
        "index": 0,
        "message": {
          "role": "assistant",
          "content": "- Black-on-black ware\n- 20th-century\n- 21st-century\n- pottery tradition\n- Puebloan Native American\n- ceramic artists\n- Northern New Mexico\n- reduction-fired blackware\n- pueblo artists\n- smooth surface\n- designs\n- selective burnishing\n- refractory slip\n- carving\n- incising designs\n- polishing\n- raised areas\n- generations\n- families\n- Kha'po Owingeh\n- P'ohwhóge Owingeh\n- pueblos\n- techniques\n- matriarch potters\n- contemporary artists\n- ancestors\n- works honoring\n- pottery"
        },
        "finish_reason": "stop"
      }
    ],
    "usage": {
      "prompt_tokens": 200,
      "completion_tokens": 136,
      "total_tokens": 336
    }
  }
}
```

## Official Documentation

![OpenAI Playground](https://raw.githubusercontent.com/FullStackWithLawrence/aws-openai/main/doc/img/examples/example-07-keywords.png "OpenAI Playground")
