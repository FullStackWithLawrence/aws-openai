# Natural language to SQL

Convert natural language into SQL queries.

- See [https://platform.openai.com/examples/default-sql-translate](https://platform.openai.com/examples/default-sql-translate)
- [Open in OpenAI Playground](https://platform.openai.com/playground/p/default-sql-translate)

## Example Usage

```console
curl --location --request PUT 'https://api.openai.lawrencemcdaniel.com/examples/default-sql-translate' \
--header 'x-api-key: YOUR-API-GATEWAY-KEY' \
--header 'Content-Type: application/json' \
--data '{"Write a SQL query which computes the average total order value for all orders on 2023-04-01."}'
```

## Example results

```json

```

## Official Documentation

![OpenAI Playground](https://raw.githubusercontent.com/FullStackWithLawrence/aws-openai/main/doc/img/examples/example-26-sql-translate.png "OpenAI Playground")
