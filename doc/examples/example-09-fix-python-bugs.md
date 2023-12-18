# Python bug fixer

Find and fix bugs in Python source code.

- See [https://platform.openai.com/examples/default-fix-python-bugs](https://platform.openai.com/examples/default-fix-python-bugs)
- [Open in OpenAI Playground](https://platform.openai.com/playground/p/default-fix-python-bugs)

## Example Usage

```console
curl --location --request PUT 'https://api.openai.lawrencemcdaniel.com/examples/default-fix-python-bugs' \
--header 'x-api-key: YOUR-API-GATEWAY-KEY' \
--header 'Content-Type: application/json' \
--data '{
    "input_text": "import Random\\r\\na = random.randint(1,12)\\r\\nb = random.randint(1,12)\\r\\nfor i in range(10):\\r\\n    question = '\''What is '\''+a+'\'' x '\''+b+'\''? '\''\\r\\n    answer = input(question)\\r\\n    if answer = a*b\\r\\n        print (Well done!)\\r\\n    else:\\r\\n        print('\''No.'\'')\\r\\n"
}'
```

## Example results

````json
{
  "isBase64Encoded": false,
  "statusCode": 200,
  "headers": {
    "Content-Type": "application/json"
  },
  "body": {
    "id": "chatcmpl-7yUeCThVHPQPnTUTF7mrDrKp5ZmJ9",
    "object": "chat.completion",
    "created": 1694651844,
    "model": "gpt-4-0613",
    "choices": [
      {
        "index": 0,
        "message": {
          "role": "assistant",
          "content": "There are several problems with the given piece of Python code. Here is the corrected version:\n\n```Python\nimport random\na = random.randint(1,12)\nb = random.randint(1,12)\nfor i in range(10):\n    question = 'What is {} x {}? '.format(a, b)\n    answer = int(input(question))\n    if answer == a*b:\n        print ('Well done!')\n    else:\n        print('No.')\n```\n\nProblem explanations:\n\n1) In Python, module names are case-sensitive. So, \"import Random\" should be \"import random\".\n2) You need to convert user input (which will be a string) to int before comparing with other integers. Hence, `answer = int(input(question))`.\n3) In Python, \"=\" is an assignment operator, not a comparison operator. You should use \"==\" for comparison. So, `if answer == a*b:`\n4) The print statement needs to be a string, so 'Well done!' needs quotes around it.\n5) ‘a’ and ‘b’ are variable and need to change for each iteration in for loop. But in the given code, they are not changing. So, they should be inside the loop. \n6) Python does not support '+' operator for concatenating string with integer. Hence, we need to use `format()` function to format the string."
        },
        "finish_reason": "stop"
      }
    ],
    "usage": {
      "prompt_tokens": 106,
      "completion_tokens": 282,
      "total_tokens": 388
    }
  }
}
````

## Official Documentation

![OpenAI Playground](https://raw.githubusercontent.com/FullStackWithLawrence/aws-openai/main/doc/img/examples/example-09-fix-python-bugs.png "OpenAI Playground")
