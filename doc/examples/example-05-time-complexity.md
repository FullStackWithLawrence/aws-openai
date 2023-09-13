# Calculate time complexity

Find the time complexity of a function.

- See [https://platform.openai.com/examples/default-time-complexity](https://platform.openai.com/examples/default-time-complexity)
- [Open in OpenAI Playground](https://platform.openai.com/playground/p/default-time-complexity)


## Example Usage

```console
curl --location --request PUT 'https://api.openai.lawrencemcdaniel.com/examples/default-time-complexity' \
--header 'x-api-key: YOUR-API-GATEWAY-KEY' \
--header 'Content-Type: application/json' \
--data '{"def foo(n, k):
    accum = 0
    for i in range(n):
        for l in range(k):
            accum += i
    return accum
"}'
```

## Example results

```json

```

## Official Documentation

![OpenAI Playground](https://raw.githubusercontent.com/FullStackWithLawrence/aws-openai/main/doc/examples/example-05-time-complexity.png "OpenAI Playground")
