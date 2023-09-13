# Function from specification

Create a Python function from a specification.

- See [https://platform.openai.com/examples/default-function-from-spec](https://platform.openai.com/examples/default-function-from-spec)
- [Open in OpenAI Playground](https://platform.openai.com/playground/p/default-function-from-spec)

## Example Usage

```console
curl --location --request PUT 'https://api.openai.lawrencemcdaniel.com/examples/default-function-from-spec' \
--header 'x-api-key: YOUR-API-GATEWAY-KEY' \
--header 'Content-Type: application/json' \
--data '{"Write a Python function that takes as input a file path to an image, loads the image into memory as a numpy array, then crops the rows and columns around the perimeter if they are darker than a threshold value. Use the mean value of rows and columns to decide if they should be marked for deletion."}'
```

## Example results

```json

```

## Official Documentation

![OpenAI Playground](https://raw.githubusercontent.com/FullStackWithLawrence/aws-openai/main/doc/examples/example-18-function-from-spec.png "OpenAI Playground")
