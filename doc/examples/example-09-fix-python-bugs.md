# Python bug fixer

Find and fix bugs in Python source code.

- See [https://platform.openai.com/examples/default-fix-python-bugs](https://platform.openai.com/examples/default-fix-python-bugs)
- [Open in OpenAI Playground](https://platform.openai.com/playground/p/default-fix-python-bugs)

## Example Usage

```console
curl --location --request PUT 'https://api.openai.lawrencemcdaniel.com/examples/default-fix-python-bugs' \
--header 'x-api-key: YOUR-API-GATEWAY-KEY' \
--header 'Content-Type: application/json' \
--data '{"import Random
a = random.randint(1,12)
b = random.randint(1,12)
for i in range(10):
    question = "What is "+a+" x "+b+"? "
    answer = input(question)
    if answer = a*b
        print (Well done!)
    else:
        print("No.")
  "}'
```

## Example results

```json

```

## Official Documentation

![OpenAI Playground](https://raw.githubusercontent.com/FullStackWithLawrence/aws-openai/main/doc/examples/example-09-fix-python-bugs.png "OpenAI Playground")
