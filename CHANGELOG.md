# [0.4.0](https://github.com/FullStackWithLawrence/aws-openai/compare/v0.3.1...v0.4.0) (2023-11-03)


### Bug Fixes

* add a .env file to root so that test environment matches prod ([293b20e](https://github.com/FullStackWithLawrence/aws-openai/commit/293b20ec1537ef493539a59aa7a8d0216809b9f4))
* add openai_utils source location to the sys path for Python ([30eed8e](https://github.com/FullStackWithLawrence/aws-openai/commit/30eed8e2c6e1c27391d94597e43afee6db5eeb44))
* need to setup venv from ./requirements.txt so that the dev imports are included ([a907e98](https://github.com/FullStackWithLawrence/aws-openai/commit/a907e983051ad2cad721cb6a9347b0adb8f60c9a))
* paths should begin with ./ ([c8060bc](https://github.com/FullStackWithLawrence/aws-openai/commit/c8060bc2302190f074d3d7e78496781f5d6e627a))
* physically copy openai_utils to pip packages folder ([772b1d6](https://github.com/FullStackWithLawrence/aws-openai/commit/772b1d659b3bde6c5f80620e4539f23df68c3ffc))
* switch to Pytest ([be7746b](https://github.com/FullStackWithLawrence/aws-openai/commit/be7746bb090ac60d29ad42359d50c3c554ab80cf))


### Features

* add automated Python unit testing workflow to Github Actions ([dea18fc](https://github.com/FullStackWithLawrence/aws-openai/commit/dea18fc8cf2183d03613893f950ad30d7acd77fe))

## [0.3.1](https://github.com/FullStackWithLawrence/aws-openai/compare/v0.3.0...v0.3.1) (2023-11-03)


### Bug Fixes

* revert to secrets.PAT ([7342489](https://github.com/FullStackWithLawrence/aws-openai/commit/7342489ef7b7537419cc12732c1739a9fc3b42a8))

# CHANGE LOG

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](http://keepachangelog.com/)
and this project adheres to [Semantic Versioning](http://semver.org/).

## [0.3.0] (2023-11-01)

The YouTube video for this release: [AWS Lamba Layers: When and How to use them](https://youtu.be/5Jf34t_UlZA)

- add lambda_langchain
- add lambda_openai_v2
- improve Terraform Lambda state management
- create a shared Lambda Layer
- move common Python validation code to Lambda Layer

## [0.2.2] (2023-10-17)

The YouTube video for this release: [Build a ChatGPT chatbot with React and AWS Serverless](https://youtu.be/emW0E8E6M0c)

- fix CORS headers on non-200 responses
- add error handling with modal popup for non-200 responses
- add test url endpoints for response codes 400, 500, 504

## [0.2.1] (2023-10-14)

- bug fix: strip html tags from pasted input text

## [0.2.0] (2023-10-11)

The YouTube video for this release: [OpenAI Python API With AWS API Gateway + Lambda](https://youtu.be/FqARAi8nS2M)

- add full CORS support to API
- add a Vite ReactJS front end

## [0.1.2] (2023-10-08)

- CoPilot code improvement suggestions
- enhance Makefile
- add Python documentation
- add PR and code review Github Action automation
- add issue template
- add pull request template
- add dependabot Github Action automation
- add sponsorship links

## [0.1.1] (2023-9-20)

- Improvements to documentation.

## [0.1.0] (2023-9-14)

- Initial release.
