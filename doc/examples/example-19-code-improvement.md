# Improve code efficiency

Provide ideas for efficiency improvements to Python code.

- See [https://platform.openai.com/examples/default-code-improvement](https://platform.openai.com/examples/default-code-improvement)
- [Open in OpenAI Playground](https://platform.openai.com/playground/p/default-code-improvement)

## Example Usage

```console
curl --location --request PUT 'https://api.openai.lawrencemcdaniel.com/examples/default-code-improvement' \
--header 'x-api-key: YOUR-API-GATEWAY-KEY' \
--header 'Content-Type: application/json' \
--data '{
    "input_text": "from typing import List\\r\\n\\r\\ndef has_sum_k(nums: List[int], k: int) -> bool:\\r\\n    n = len(nums)\\r\\n    for i in range(n):\\r\\n        for j in range(i+1, n):\\r\\n            if nums[i] + nums[j] == k:\\r\\n                return True\\r\\n    return False"
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
    "id": "chatcmpl-7yUk2FIKLOQebVHB4tUhQ5ggiee6b",
    "object": "chat.completion",
    "created": 1694652206,
    "model": "gpt-4-0613",
    "choices": [
      {
        "index": 0,
        "message": {
          "role": "assistant",
          "content": "1. Leverage `set` for O(1) lookups: Rather than performing a linear scan on the list for each element, which leads to O(n^2) complexity, we can use a set to store the numbers as we process them. Every time when we look at a new number, we can check if there's a number previously stored in the set such that the two numbers sum up to `k`. This approach has O(n) time complexity.\n\n2. Avoid unnecessary typecasting: In this case, Python type hints were used correctly and there's no unnecessary typecasting, but it's worth mentioning as a general efficiency improvement tip. Unnecessary typecasting can be a costly operation, it's better to avoid it where possible.\n\nHere's the proposed improvement:\n\n```python\nfrom typing import List\n\ndef has_sum_k(nums: List[int], k: int) -> bool:\n    seen = set()\n    for num in nums:\n        if k - num in seen:\n            return True\n        seen.add(num)\n    return False\n```\nThis version of the code accomplishes the same goal with better time complexity: it reduces from O(n^2) to O(n). The space complexity is O(n), as in worst case scenario the set will store all unique elements."
        },
        "finish_reason": "stop"
      }
    ],
    "usage": {
      "prompt_tokens": 97,
      "completion_tokens": 262,
      "total_tokens": 359
    }
  }
}
````

## Official Documentation

![OpenAI Playground](https://raw.githubusercontent.com/FullStackWithLawrence/aws-openai/main/doc/img/examples/example-19-code-improvement.png "OpenAI Playground")
