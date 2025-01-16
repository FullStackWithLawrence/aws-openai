# OpenAI Function Calling examples

## Sample usage

The following screenshots demonstrate the two Function Calling Python functions that are included in this project, for real-time weather data, and to include additional information in ChatGPT responses based on user prompt search terms and a custom JSON dict that is returned to ChatGPT via a Python API call.

![Terraform init](https://raw.githubusercontent.com/FullStackWithLawrence/aws-openai/main/doc/img/openai-function-calling-example.png "Function Calling example")

![Terraform init](https://raw.githubusercontent.com/FullStackWithLawrence/aws-openai/main/doc/img/openai-function-calling-cloudwatch.png "Function Calling Cloudwatch")

## function_weather.py

Fully implements the "[get_current_weather()](https://platform.openai.com/docs/guides/function-calling)" from The official OpenAI API documentation. OpenAI's documentation provides scaffolding for this feature, but falls short of actually providing code that retrieves location-based current weather forecasts.

## plugin_manager.py

This module demonstrates an alternative implementation of prompt behavior modification involving both Function Calling, plus, dynamic modifications to the system prompt. The module passes a customized configuration object to `function_calling_plugin()` based on a configurable set of search terms that it looks for in the user prompt. The function works with multiple customized configurations. That is, it maintains a list of plugins, and user prompts including search terms associated with multiple plugins will result in prompt configuration multiple "Function Calling" apis. The plugins are persisted both inside this repository in the [config](./plugins/) folder as well as via a remote AWS S3 bucket that Terraform creates and configures for you automatically. Custom configurations are data-driven via a standardized yaml format. Use [example-configuration.yaml](./plugins/example-configuration.yaml) as a template to create your own plugins. Storing these in the AWS S3 bucket is preferable to keeping these inside your repo.

### Example plugins

The following two sample plugins are included in this project:

1. [Everlasting Gobstopper](./plugins/everlasting-gobstopper.yaml): An example of a consumer product, complete with pricing information and coupon codes.
2. [Lawrence McDaniel](./plugins/lawrence-mcdaniel.yaml): Similar in functionality to a personal web site, this configuration demonstrates how you can get ChatGPT to showcase your professional profile, including your job and project history, your project portfolio, skill set and context-sensitive contact information.

### Custom Configuration Yaml format

```yaml
meta_data:
  plugin_name: ExampleConfiguration
  plugin_description: A 'hello world' style plugin.
  plugin_version: 0.1.0
  plugin_author: Lawrence McDaniel
selector:
  directive: search_terms
  search_terms:
    strings:
      - example function calling configuration
    pairs:
      - - Example
        - configuration
      - - example
        - function calling
prompting:
  system_prompt: >
    Your job is to provide helpful technical information about the OpenAI API Function Calling feature. You should include the following information in your response:
    "Congratulations!!! OpenAI API Function Calling chose to call this function. Here is the additional information that you requested:"
function_calling:
  function_description: an example plugin to integrate with OpenAI API Function Calling additional information function, in this module.
  additional_information:
    platform_provider: OpenAI
    about: >
      In an API call, you can describe functions and have the model intelligently choose to output a JSON object containing arguments to call one or many functions. The Chat Completions API does not call the function; instead, the model generates JSON that you can use to call the function in your code.
      The latest models (gpt-4-turbo-1106 and gpt-4-1106-preview) have been trained to both detect when a function should to be called (depending on the input) and to respond with JSON that adheres to the function signature more closely than previous models. With this capability also comes potential risks. We strongly recommend building in user confirmation flows before taking actions that impact the world on behalf of users (sending an email, posting something online, making a purchase, etc).
    links:
      - documentation: https://platform.openai.com/docs/guides/function-calling
      - website: https://openai.com/
      - wikipedia: https://en.wikipedia.org/wiki/OpenAI
```
