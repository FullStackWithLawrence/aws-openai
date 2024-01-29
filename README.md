# OpenAI Code Samples

[![FullStackWithLawrence](https://a11ybadges.com/badge?text=FullStackWithLawrence&badgeColor=orange&logo=youtube&logoColor=282828)](https://www.youtube.com/@FullStackWithLawrence)<br>
[![OpenAI](https://a11ybadges.com/badge?logo=openai)](https://platform.openai.com/)
[![LangChain](https://a11ybadges.com/badge?text=LangChain&badgeColor=0834ac)](https://www.langchain.com/)
[![Amazon AWS](https://a11ybadges.com/badge?logo=amazonaws)](https://aws.amazon.com/)
[![ReactJS](https://a11ybadges.com/badge?logo=react)](https://react.dev/)
[![Python](https://a11ybadges.com/badge?logo=python)](https://www.python.org/)
[![Terraform](https://a11ybadges.com/badge?logo=terraform)](https://www.terraform.io/)<br>
[![12-Factor](https://img.shields.io/badge/12--Factor-Compliant-green.svg)](./doc/Twelve_Factor_Methodology.md)
![Unit Tests](https://github.com/FullStackWithLawrence/aws-openai/actions/workflows/testsPython.yml/badge.svg?branch=main)
![GHA pushMain Status](https://img.shields.io/github/actions/workflow/status/FullStackWithLawrence/aws-openai/pushMain.yml?branch=main)
![Auto Assign](https://github.com/FullStackwithLawrence/aws-openai/actions/workflows/auto-assign.yml/badge.svg)
[![Release Notes](https://img.shields.io/github/release/FullStackWithLawrence/aws-openai)](https://github.com/FullStackWithLawrence/aws-openai/releases)
[![License: AGPL v3](https://img.shields.io/badge/License-AGPL_v3-blue.svg)](https://www.gnu.org/licenses/agpl-3.0)
[![hack.d Lawrence McDaniel](https://img.shields.io/badge/hack.d-Lawrence%20McDaniel-orange.svg)](https://lawrencemcdaniel.com)

A [React](https://react.dev/) + [AWS Serverless](https://aws.amazon.com/serverless/) full stack implementation of the [example applications](https://platform.openai.com/examples) found in the official OpenAI API documentation. See this [system architectural diagram](./doc/README.md) for details. This is an instructional tool for the YouTube channel "[Full Stack With Lawrence](https://youtube.com/@FullStackWithLawrence)" and for University of British Columbia course, "[Artificial Intelligence Cloud Technology Implementation](https://extendedlearning.ubc.ca/courses/artificial-intelligence-cloud-technology-implementation/mg202)".

## Quickstart

Works with Linux, Windows and macOS environments.

1. Verify project requirements: [AWS Account](https://aws.amazon.com/free/) and [CLI](https://aws.amazon.com/cli/) access, [Terraform](https://www.terraform.io/), [Python 3.11](https://www.python.org/), [NPM](https://www.npmjs.com/) and [Docker Compose](https://docs.docker.com/compose/install/).

2. Review and edit the master [Terraform configuration](./api/terraform/terraform.tfvars) file.

3. Run `make` and add your credentials to the newly created `.env` file in the root of the repo.

4. Initialize, build and run the application.

```console
git clone https://github.com/FullStackWithLawrence/aws-openai.git
make        # scaffold a .env file in the root of the repo
make init   # initialize Terraform, Python virtual environment and NPM
make build  # deploy AWS cloud infrastructure, build ReactJS web app
make run    # run the web app locally in your dev environment
```

## Features

- **Complete OpenAI API**: Deploys a production-ready API for integrating to OpenAI's complete suite of services, including ChatGTP, DALL·E, Whisper, and TTS.

- **LangChain Integration**: A simple API endpoint for building context-aware, reasoning applications with LangChain’s flexible abstractions and AI-first toolkit. Use this endpoint to develop a wide range of applications, from chatbots to question-answering systems.

- **Dynamic ChatGPT Prompting**: Simple [Terraform templates](./api/terraform/apigateway_endpoints.tf) to create highly presonalized ChatBots. Program and skin your own custom chat apps in minutes.

- **Function Calling**: OpenAI's most advanced integration feature to date. OpenAI API Function Calling is a feature that enables developers to integrate their own custom Python functions into the processing of chat responses. For example, when a chatbot powered by OpenAI's GPT-3 model is generating responses, it can call these custom Python functions to perform specific tasks or computations, and then include the results of these functions in its responses. This powerful feature can be used to create more dynamic and interactive chatbots that can perform tasks such as fetching real-time data, performing calculations, or interacting with other APIs or services. See the [Python source code](./api/terraform/python/openai_api/lambda_openai_function/) for additional documentation and examples, including, "[get_current_weather()](./api/terraform/python/openai_api/lambda_openai_function/function_weather.py)" from The official [OpenAI API documentation](https://platform.openai.com/docs/guides/function-calling/common-use-cases)

- **Function Calling Plugins**: We created our own yaml-based "plugin" model. See this [example plugin](./api/terraform/python/openai_api/lambda_openai_function/plugins/example-configuration.yaml) and this [documentation](./api/terraform/python/openai_api/lambda_openai_function/README.md) for details, or try it out on this [live site](https://openai.lawrencemcdaniel.com/). Yaml templates can be stored locally or served from a secure AWS S3 bucket. You'll find set of fun example plugins [here](./api/terraform/python/openai_api/lambda_openai_function/plugins/).

![Marv](https://cdn.lawrencemcdaniel.com/marv.gif)

## ReactJS chat application

Complete source code and documentation is located [here](./client/).

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
Python code is located [here](./api/terraform/python/openai_api/)

A REST API implementing each of the [30 example applications](https://platform.openai.com/examples) from the official [OpenAI API Documentation](https://platform.openai.com/docs/api-reference/making-requests?lang=python) using a modularized Terraform approach. Leverages OpenAI's suite of AI models, including [GPT-3.5](https://platform.openai.com/docs/models/gpt-3-5), [GPT-4](https://platform.openai.com/docs/models/gpt-4), [DALL·E](https://platform.openai.com/docs/models/dall-e), [Whisper](https://platform.openai.com/docs/models/whisper), [Embeddings](https://platform.openai.com/docs/models/embeddings), and [Moderation](https://platform.openai.com/docs/models/moderation).

### API Key features

- [OpenAI API](https://pypi.org/project/openai/) library for Python. [LangChain](https://www.langchain.com/) enabled API endpoints where designated.
- [Pydantic](https://docs.pydantic.dev/latest/) based CI-CD friendly [Settings](./api/terraform/python/openai_api/common/README.md) configuration class that consistently and automatically manages Python Lambda initializations from multiple sources including bash environment variables, `.env` and `terraform.tfvars` files.
- [CloudWatch](https://aws.amazon.com/cloudwatch/) logging
- [Terraform](https://www.terraform.io/) fully automated and [parameterized](./api/terraform/terraform.tfvars) build. Usually builds your infrastructure in less than a minute.
- Secure: uses AWS role-based security and custom IAM policies. Best practice handling of secrets and sensitive data in all environments (dev, test, CI-CD, prod). Proxy-based API that hides your OpenAI API calls and credentials. Runs on https with AWS-managed SSL/TLS certificate.
- Excellent [documentation](./doc/)
- [AWS serverless](https://aws.amazon.com/serverless/) implementation. Free or nearly free in most cases
- Deploy to a custom domain name

## Requirements

- [git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git). _pre-installed on Linux and macOS_
- [make](https://gnuwin32.sourceforge.net/packages/make.htm). _pre-installed on Linux and macOS._
- [AWS account](https://aws.amazon.com/)
- [AWS Command Line Interface](https://aws.amazon.com/cli/)
- [Terraform](https://www.terraform.io/).
  _If you're new to Terraform then see [Getting Started With AWS and Terraform](./doc/TERRAFORM_GETTING_STARTED_GUIDE.md)_
- [OpenAI platform API key](https://platform.openai.com/).
  _If you're new to OpenAI API then see [How to Get an OpenAI API Key](./doc/OPENAI_API_GETTING_STARTED_GUIDE.md)_
- [Python 3.11](https://www.python.org/downloads/): for creating virtual environment used for building AWS Lambda Layer, and locally by pre-commit linters and code formatters.
- [NodeJS](https://nodejs.org/en/download): used with NPM for local ReactJS developer environment, and for configuring/testing Semantic Release.
- [Docker Compose](https://docs.docker.com/compose/install/): used by an automated Terraform process to create the AWS Lambda Layer for OpenAI and LangChain.

Optional requirements:

- [Google Maps API key](https://developers.google.com/maps/documentation/geocoding/overview). This is used the OpenAI API Function Calling coding example, "[get_current_weather()](https://platform.openai.com/docs/guides/function-calling)".
- [Pinecone API key](https://docs.pinecone.io/docs/quickstart). This is used for OpenAI API Embedding examples.

## Documentation

Detailed documentation for each endpoint is available here: [Documentation](./doc/examples/)

## Support

To get community support, go to the official [Issues Page](https://github.com/FullStackWithLawrence/aws-openai/issues) for this project.

## Good Coding Best Practices

This project demonstrates a wide variety of good coding best practices for managing mission-critical cloud-based micro services in a team environment, namely its adherence to [12-Factor Methodology](./doc/Twelve_Factor_Methodology.md). Please see this [Code Management Best Practices](./doc/GOOD_CODING_PRACTICE.md) for additional details.

We want to make this project more accessible to students and learners as an instructional tool while not adding undue code review workloads to anyone with merge authority for the project. To this end we've also added several pre-commit code linting and code style enforcement tools, as well as automated procedures for version maintenance of package dependencies, pull request evaluations, and semantic releases.

## Contributing

We welcome contributions! There are a variety of ways for you to get involved, regardless of your background. In addition to Pull requests, this project would benefit from contributors focused on documentation and how-to video content creation, testing, community engagement, and stewards to help us to ensure that we comply with evolving standards for the ethical use of AI.

For developers, please see:

- the [Developer Setup Guide](./doc/CONTRIBUTING.md)
- and these [commit comment guidelines](./doc/SEMANTIC_VERSIONING.md) 😬😬😬 for managing CI rules for automated semantic releases.

You can also contact [Lawrence McDaniel](https://lawrencemcdaniel.com/contact) directly. Code composition as of Feb-2024:

```console
-------------------------------------------------------------------------------
Language                     files          blank        comment           code
-------------------------------------------------------------------------------
Python                          29            732            722           2663
HCL                             30            352            714           2353
Markdown                        52            779              6           2344
YAML                            23            112            149           1437
JavaScript                      39            114            127           1088
JSX                              6             45             47            858
CSS                              5             32             14            180
make                             1             27             30            120
Text                             6             13              0            117
INI                              2             15              0             70
HTML                             2              1              0             65
Jupyter Notebook                 1              0            186             48
Bourne Shell                     5             17             55             47
TOML                             1              1              0             23
Dockerfile                       1              4              4              5
-------------------------------------------------------------------------------
SUM:                           203          2,244          2,054         11,418
-------------------------------------------------------------------------------
```
