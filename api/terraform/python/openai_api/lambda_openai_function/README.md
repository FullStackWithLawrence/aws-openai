# OpenAI Function Calling examples

## function_weather.py

Fully implements the "[get_current_weather()](https://platform.openai.com/docs/guides/function-calling)" from The official OpenAI API documentation. OpenAI's documentation provides scaffolding for this feature, but falls short of actually providing code that retrieves location-based current weather forecasts.

## function_refers_to.py

This module demonstrates an alternative implementation of prompt behavior modification involving both Function Calling, plus, dynamic modifications to the system prompt. This example relies on [lambda_config.yaml](./lambda_config.yaml) for personalization data.
