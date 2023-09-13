# Product name generator

Generate product names from a description and seed words.

- See [https://platform.openai.com/examples/default-product-name-gen](https://platform.openai.com/examples/default-product-name-gen)
- [Open in OpenAI Playground](https://platform.openai.com/playground/p/default-product-name-gen)

## Example Usage

```console
curl --location --request PUT 'https://api.openai.lawrencemcdaniel.com/examples/default-product-name-gen' \
--header 'x-api-key: YOUR-API-GATEWAY-KEY' \
--header 'Content-Type: application/json' \
--data '{"Product description: A home milkshake maker. Seed words: fast, healthy, compact."}'
```

## Example results

```json

```

## Official Documentation

![OpenAI Playground](https://raw.githubusercontent.com/FullStackWithLawrence/aws-openai/main/doc/examples/example-08-product-name-gen.png "OpenAI Playground")
