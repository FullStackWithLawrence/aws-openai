# Turn by turn directions

Convert natural language to turn-by-turn directions.

- See [https://platform.openai.com/examples/default-turn-by-turn-directions](https://platform.openai.com/examples/default-turn-by-turn-directions)
- [Open in OpenAI Playground](https://platform.openai.com/playground/p/default-turn-by-turn-directions)

## Example Usage

```console
curl --location --request PUT 'https://api.openai.lawrencemcdaniel.com/examples/default-turn-by-turn-directions' \
--header 'x-api-key: YOUR-API-GATEWAY-KEY' \
--header 'Content-Type: application/json' \
--data '{"Go south on 95 until you hit Sunrise boulevard then take it east to us 1 and head south. Tom Jenkins bbq will be on the left after several miles."}'
```

## Example results

```json

```

## Official Documentation

![OpenAI Playground](https://raw.githubusercontent.com/FullStackWithLawrence/aws-openai/main/doc/examples/example-16-turn-by-turn-directions.png "OpenAI Playground")
