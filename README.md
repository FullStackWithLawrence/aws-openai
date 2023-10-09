[![OpenAI](https://a11ybadges.com/badge?logo=openai)](https://platform.openai.com/)
[![Amazon AWS](https://a11ybadges.com/badge?logo=amazonaws)](https://aws.amazon.com/)
[![ReactJS](https://a11ybadges.com/badge?logo=react)](https://react.dev/)
[![FullStackWithLawrence](https://a11ybadges.com/badge?text=FullStackWithLawrence&badgeColor=orange&logo=youtube&&logoColor=red)](https://www.youtube.com/@FullStackWithLawrence)

# Customized chatGPT Application

## ReactJS chat application

add text here.

## Custom OpenAI REST API Backend

A REST API implementing each of the [30 example applications](https://platform.openai.com/examples) from the official [OpenAI API Documentation](https://platform.openai.com/docs/api-reference/making-requests?lang=python) using a modularized Terraform approach. Implemented as a serverless microservice using AWS [API Gateway](https://aws.amazon.com/api-gateway/), [Lambda](https://aws.amazon.com/lambda/) and the [OpenAI Python Library](https://pypi.org/project/openai/). Leverages OpenAI's suite of AI models, including [GPT-3.5](https://platform.openai.com/docs/models/gpt-3-5), [GPT-4](https://platform.openai.com/docs/models/gpt-4), [DALL·E](https://platform.openai.com/docs/models/dall-e), [Whisper](https://platform.openai.com/docs/models/whisper), [Embeddings](https://platform.openai.com/docs/models/embeddings), and [Moderation](https://platform.openai.com/docs/models/moderation).

- Creating new OpenAI applications and endpoints for this API only takes a few lines of code and is as easy as it is fun! Follow [this link](./terraform/apigateway_endpoints.tf) to see how each of these are coded.
- **Follow [this link](./doc/examples/README.md) for detailed documentation on each URL endpoint.**

## Official YouTube Video For This Repo

[![OpenAI Python API With AWS API Gateway + Lambda](https://img.youtube.com/vi/FqARAi8nS2M/hqdefault.jpg)](https://www.youtube.com/watch?v=FqARAi8nS2M)

## Requirements

- [AWS account](https://aws.amazon.com/)
- [AWS Command Line Interface](https://aws.amazon.com/cli/)
- [Terraform](https://www.terraform.io/).
    *If you're new to Terraform then see [Getting Started With AWS and Terraform](./doc/terraform-getting-started.md)*
- [OpenAI platform API key](https://platform.openai.com/).
    *If you're new to OpenAI API then see [How to Get an OpenAI API Key](./doc/openai-api-key.md)*

## Documentation

Detailed documentation for each endpoint is available here: [Documentation](./doc/examples/)

## Support

To get community support, go to the official [Issues Page](https://github.com/FullStackWithLawrence/aws-openai/issues) for this project.

## Contributing

We welcome contributions! There are a variety of ways for you to get involved, regardless of your background. In additional to Pull requests, this project would benefit from contributors focused on documentation and how-to video content creation, testing, community engagement, and stewards to help us to ensure that we comply with evolving standards for the ethical use of AI.

You can also contact [Lawrence McDaniel](https://lawrencemcdaniel.com/contact) directly.
