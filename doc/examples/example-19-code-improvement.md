# Improve code efficiency

Provide ideas for efficiency improvements to Python code.

- See [https://platform.openai.com/examples/default-code-improvement](https://platform.openai.com/examples/default-code-improvement)
- [Open in OpenAI Playground](https://platform.openai.com/playground/p/default-code-improvement)

## Example Usage

```console
curl --location --request PUT 'https://api.openai.lawrencemcdaniel.com/examples/default-code-improvement' \
--header 'x-api-key: YOUR-API-GATEWAY-KEY' \
--header 'Content-Type: application/json' \
--data '{"from typing import List

def has_sum_k(nums: List[int], k: int) -> bool:
    """
    Returns True if there are two distinct elements in nums such that their sum
    is equal to k, and otherwise returns False.
    """
    n = len(nums)
    for i in range(n):
        for j in range(i+1, n):
            if nums[i] + nums[j] == k:
                return True
    return False
  "}'
```

## Example results

```json

```

## Official Documentation

![OpenAI Playground](https://raw.githubusercontent.com/FullStackWithLawrence/aws-openai/main/doc/examples/example-19-code-improvement.png "OpenAI Playground")
