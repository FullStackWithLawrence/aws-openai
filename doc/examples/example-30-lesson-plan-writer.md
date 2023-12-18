# Lesson plan writer

Generate a lesson plan for a specific topic.

- See [https://platform.openai.com/examples/default-lesson-plan-writer](https://platform.openai.com/examples/default-lesson-plan-writer)
- [Open in OpenAI Playground](https://platform.openai.com/playground/p/default-lesson-plan-writer)

## Example Usage

```console
curl --location --request PUT 'https://api.openai.lawrencemcdaniel.com/examples/default-lesson-plan-writer' \
--header 'x-api-key: YOUR-API-GATEWAY-KEY' \
--header 'Content-Type: application/json' \
--data '{"Write a lesson plan for an introductory algebra class. The lesson plan should cover the distributive law, in particular how it works in simple cases involving mixes of positive and negative numbers. Come up with some examples that show common student errors."}'
```

## Example results

```json

```

## Official Documentation

![OpenAI Playground](https://raw.githubusercontent.com/FullStackWithLawrence/aws-openai/main/doc/img/examples/example-30-lesson-plan-writer.png "OpenAI Playground")
