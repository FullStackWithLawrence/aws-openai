[![OpenAI](https://a11ybadges.com/badge?logo=openai)](https://platform.openai.com/)
[![LangChain](https://a11ybadges.com/badge?text=LangChain&badgeColor=0834ac)](https://www.langchain.com/)
[![Amazon AWS](https://a11ybadges.com/badge?logo=amazonaws)](https://aws.amazon.com/)
[![ReactJS](https://a11ybadges.com/badge?logo=react)](https://react.dev/)
[![FullStackWithLawrence](https://a11ybadges.com/badge?text=FullStackWithLawrence&badgeColor=orange&logo=youtube&logoColor=282828)](https://www.youtube.com/@FullStackWithLawrence)

# OpenAI Code Samples

A [React](https://react.dev/) + [AWS Serverless](https://aws.amazon.com/serverless/) full stack implementation of the [30 example applications](https://platform.openai.com/examples) found in the official OpenAI API documentation. Now with [LangChain](https://www.langchain.com/)!

[![React front end](https://github.com/FullStackWithLawrence/aws-openai/blob/main/doc/front-end.png)](https://openai.lawrencemcdaniel.com/)

**IMPORTANT DISCLAIMER: AWS' Lambda service has a hard 29-second timeout. OpenAI API calls often take longer than this, in which case the AWS API Gateway endpoint will return a 504 "Gateway timeout error" response to the React client. This happens frequently with apps created using chatgpt-4. Each of the 30 OpenAI API example applications are nonetheless implemented exactly as they are specified in the official documentation.**

## ReactJS chat application

Complete documentation is located [here](./client/).

React app that leverages [Vite.js](https://github.com/FullStackWithLawrence/aws-openai), [@chatscope/chat-ui-kit-react](https://www.npmjs.com/package/@chatscope/chat-ui-kit-react), and [react-pro-sidebar](https://www.npmjs.com/package/react-pro-sidebar).

### Webapp Key features

- robust, highly customizable chat features
- A component model for implementing your own highly personalized OpenAI apps
- Skinnable UI for each app
- Includes default assets for each app
- Small compact code base
- Robust error handling for non-200 response codes from the custom REST API
- Handles direct text input as well as file attachments
- Info link to the OpenAI API official code sample
- Build-deploy managed with Vite

## Custom OpenAI REST API Backend

Complete documentation is located [here](./api/).

A REST API implementing each of the [30 example applications](https://platform.openai.com/examples) from the official [OpenAI API Documentation](https://platform.openai.com/docs/api-reference/making-requests?lang=python) using a modularized Terraform approach. Leverages OpenAI's suite of AI models, including [GPT-3.5](https://platform.openai.com/docs/models/gpt-3-5), [GPT-4](https://platform.openai.com/docs/models/gpt-4), [DALL·E](https://platform.openai.com/docs/models/dall-e), [Whisper](https://platform.openai.com/docs/models/whisper), [Embeddings](https://platform.openai.com/docs/models/embeddings), and [Moderation](https://platform.openai.com/docs/models/moderation).

### API Key features

- Built on the [OpenAI API Python Library](https://pypi.org/project/openai/)
- [LangChain](https://www.langchain.com/) enabled API endpoints where designated.
- Customizable. [Modularized endpoints](./terraform/apigateway_endpoints.tf) that only take a few lines of code each.
- Highly secure. Your OpenAI API key is stored in a local .env file, and is kept safe during development, build and deployment to production.
- Implements excellent [CloudWatch](https://aws.amazon.com/cloudwatch/) logs for Lambda as well as API Gateway
- Fully automated and [parameterized](./api/terraform/terraform.tfvars) Terraform build
- well documented code plus supplemental [documentation resources](./doc/) as well as detailed documentation on each [URL endpoint](./doc/examples/README.md).
- Low-cost [AWS serverless](https://aws.amazon.com/serverless/) implementation using [AWS API Gateway](https://aws.amazon.com/api-gateway/) and [AWS Lambda](https://aws.amazon.com/lambda/); free or nearly free in most cases
- Robust, performant and infinitely scalable
- Fast build time; usually less than 60 seconds to fully implement
- Includes both Python and Node.js Lambda examples
- Deploy https to a custom domain
- Preconfigured [Postman](https://www.postman.com/) files for testing
- includes AWS API Gateway usage policy and api key
- Full CORS configuration

## Requirements

- [AWS account](https://aws.amazon.com/)
- [AWS Command Line Interface](https://aws.amazon.com/cli/)
- [Terraform](https://www.terraform.io/).
    *If you're new to Terraform then see [Getting Started With AWS and Terraform](./doc/terraform-getting-started.md)*
- [OpenAI platform API key](https://platform.openai.com/).
    *If you're new to OpenAI API then see [How to Get an OpenAI API Key](./doc/openai-api-key.md)*

## Documentation

Detailed documentation for each endpoint is available here: [Documentation](./doc/examples/)

## Examples of Code Management Best Practices

This repo is referenced by multiple YouTube videos, including various tutorials about good coding practices and good code management. Of note:

- [python-dotenv](https://pypi.org/project/python-dotenv/) for storing sensitive data for local development
- [.gitignore](./.gitignore)  ensures that no sensitive nor useless data accidentally gets pushed to GitHub.
- [tox.ini](./tox.ini) file for configuring behaviors of Python testing tools
- [GitHub Actions](https://github.com/features/actions) automates unit testing, semantic release rule checking, and dependabot actions.
- [GitHub Secrets](https://github.com/FullStackWithLawrence/aws-openai/settings/secrets/actions) to provide sensitive data to Github Actions workflows
- [GitHub Issues](https://github.com/features/issues)
- [Makefile](./Makefile) automates procedures like init, build, test, release and linting for Python, ReactJS and Terraform.
- [pre-commit](https://pre-commit.com/) automatically enforces a multitude of code quality, coding style and security policies.
- [Dependabot](https://github.com/dependabot) automatically updates the version pins of code library dependencies for Python, ReactJS and Terraform.
- [Unit Tests](https://docs.pytest.org/) are automated and can be invoked
  - manually from the command line
  - manually from GitHub Actions
  - automatically by Dependabot.
- [Mergify](https://mergify.com/) automates processing of bot-created pull requests
- [Semantic Release](https://github.com/semantic-release/semantic-release) automates version releases as well as maintains the [CHANGELOG](./CHANGELOG.md) for the repo.
- [Change Log](http://keepachangelog.com/)

## Support

To get community support, go to the official [Issues Page](https://github.com/FullStackWithLawrence/aws-openai/issues) for this project.

## Contributing

We welcome contributions! There are a variety of ways for you to get involved, regardless of your background. In additional to Pull requests, this project would benefit from contributors focused on documentation and how-to video content creation, testing, community engagement, and stewards to help us to ensure that we comply with evolving standards for the ethical use of AI.

Please review these [commit comment guidelines](./SEMANTIC_VERSIONING.md) for managing CI rules for automated semantic versioning as well as automated comment generation in CHANGELOG.md.

You can also contact [Lawrence McDaniel](https://lawrencemcdaniel.com/contact) directly.
