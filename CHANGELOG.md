## [0.11.1](https://github.com/FullStackWithLawrence/aws-openai/compare/v0.11.0...v0.11.1) (2025-05-14)


### Bug Fixes

* force a new release ([ca29be2](https://github.com/FullStackWithLawrence/aws-openai/commit/ca29be2b704415be27aa90a9914a35dda6f0a171))

# [0.11.0](https://github.com/FullStackWithLawrence/aws-openai/compare/v0.10.8...v0.11.0) (2025-02-01)


### Features

* containerize openai_api and push to AWS ECR ([e18651b](https://github.com/FullStackWithLawrence/aws-openai/commit/e18651b8f0b6bf59f9e40d0acdce49560baadb0f))

## [0.10.7](https://github.com/FullStackWithLawrence/aws-openai/compare/v0.10.6...v0.10.7) (2024-11-01)

### Bug Fixes

- force a new release ([95401cb](https://github.com/FullStackWithLawrence/aws-openai/commit/95401cb87fbf941eb3237981f48fc535fcf1a7a4))

## [0.10.6](https://github.com/FullStackWithLawrence/aws-openai/compare/v0.10.5...v0.10.6) (2024-01-29)

### Bug Fixes

- force a new release ([d411e41](https://github.com/FullStackWithLawrence/aws-openai/commit/d411e415f2657e1b2b9475c6434de55b677d8262))

## [0.10.5](https://github.com/FullStackWithLawrence/aws-openai/compare/v0.10.4...v0.10.5) (2024-01-28)

### Bug Fixes

- force a new release ([5b1ee95](https://github.com/FullStackWithLawrence/aws-openai/commit/5b1ee95dc155b93f04ad79d66ec01f3a6852d60c))

# Change Log

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](http://keepachangelog.com/) and this project adheres to [Semantic Versioning](http://semver.org/).

## [0.10.4](https://github.com/FullStackWithLawrence/aws-openai/compare/v0.10.3...v0.10.4) (2024-01-27)

OpenAI 'Function Calling' Lambda.

### Refactor

- Pydantic refactor ([ad39079](https://github.com/FullStackWithLawrence/aws-openai/commit/ad39079e2142368d7ab2d19360da2dcd2a034120)). [custom_config.py](./api/terraform/python/openai_api/lambda_openai_function/custom_config.py) now inherits from Pydantic BaseModel.
- Incremental development of the yaml file standard for plugins. This now has three well-defined for meta_data, prompting, function_calling.
- Added remote AWS S3 bucket support for custom config yaml file storage.
- Liam has replaced Marv as the default chatbot.

## [0.10.3](https://github.com/FullStackWithLawrence/aws-openai/compare/v0.10.2...v0.10.3) (2024-01-27)

### Refactor

- Add "additional information" feature based on a standardized yaml file format ([7c88275](https://github.com/FullStackWithLawrence/aws-openai/commit/7c88275ef2041744f6fbf46e28c73ef803b5e1e5))
- Add real-time weather forecasts ([bf6fa8f](https://github.com/FullStackWithLawrence/aws-openai/commit/bf6fa8f5c72541706023cde47bb378a65e126087))

## [0.10.2](https://github.com/FullStackWithLawrence/aws-openai/compare/v0.10.1...v0.10.2) (2024-01-23)

### Refactor

- add more granular info section selections ([ce870f0](https://github.com/FullStackWithLawrence/aws-openai/commit/ce870f0eca1f2519d1de8ee3cecdf26ce1acae1c))

## [0.10.1](https://github.com/FullStackWithLawrence/aws-openai/compare/v0.10.0...v0.10.1) (2024-01-23)

### Refactor

- configure google maps api for use in aws lambda. ([37068ee](https://github.com/FullStackWithLawrence/aws-openai/commit/37068ee3d84293b8f4c7e2095d625b1f35937cd1))
- graceful failure if google geolocation api key is missing. ([f601c64](https://github.com/FullStackWithLawrence/aws-openai/commit/f601c6401d61d8c81e841bc9f3ff05a398de9d96))
- implement get_current_weather() using google maps api + open-meteo ([453a432](https://github.com/FullStackWithLawrence/aws-openai/commit/453a432bd87be03aff3ec6628ca00555e91eaa34))

# [0.10.0](https://github.com/FullStackWithLawrence/aws-openai/compare/v0.9.1...v0.10.0) (2024-01-23)

### Refactor

- add handling for legacy native openai api responses ([b5de30c](https://github.com/FullStackWithLawrence/aws-openai/commit/b5de30cbbfebed2ca50189063b80f16a92b9b49e))

### Features

- add openai-function-calling app ([9033b6d](https://github.com/FullStackWithLawrence/aws-openai/commit/9033b6dd02fea818588ae9d926ded4cbf34411eb))
- code lambda_handler() to process tool_call(s) returned by openai api ([f4b076c](https://github.com/FullStackWithLawrence/aws-openai/commit/f4b076cff230fee81faf8d0858baf409f0b9ada2))
- convert urls in response text to links and add styling ([031eac7](https://github.com/FullStackWithLawrence/aws-openai/commit/031eac772627f13636501071ea212c0210476a95))
- create new layer_nlp lambda layer ([1c11515](https://github.com/FullStackWithLawrence/aws-openai/commit/1c115155252b954189418c9415aae7912d633b3d))
- scaffold a lambda that uses an openai function ([b6a5cc2](https://github.com/FullStackWithLawrence/aws-openai/commit/b6a5cc280fe57637e2cdf6ba869cc8760bc49d4e))

## [0.9.1](https://github.com/FullStackWithLawrence/aws-openai/compare/v0.9.0...v0.9.1) (2024-01-20)

### Bug Fixes

- force a new release ([a069aae](https://github.com/FullStackWithLawrence/aws-openai/commit/a069aae8d6d0959cbc74334f0ebdf0105d55c3a8))
- force a new release ([a2daf8a](https://github.com/FullStackWithLawrence/aws-openai/commit/a2daf8a58be94cbd6769c1ba7dedab5e18ef3fc1))

## [0.9.0](https://github.com/FullStackWithLawrence/aws-openai/compare/v0.8.2...v0.9.0) (2023-12-30)

### Features

- add /info end point ([bc7cdcd](https://github.com/FullStackWithLawrence/aws-openai/commit/bc7cdcdd02efb0f609eae24648b2e1867f38e3f9))

## [0.8.2](https://github.com/FullStackWithLawrence/aws-openai/compare/v0.8.1...v0.8.2) (2023-12-30)

### Bug Fixes

- refactor request templates for openai api v1 object_type ([c857082](https://github.com/FullStackWithLawrence/aws-openai/commit/c8570826c75a9f99f465ffa3ebd470795ffb70d3))

## [0.8.1](https://github.com/FullStackWithLawrence/aws-openai/compare/v0.8.0...v0.8.1) (2023-12-30)

### Bug Fixes

- ensure that AWS_ACCESS_KEY_ID and AWS_SECRET_ACCESS_KEY are set when running CI ([3d788b0](https://github.com/FullStackWithLawrence/aws-openai/commit/3d788b0d72f327d9f4711586499807c06831f5db))
- fix indentation error ([806865b](https://github.com/FullStackWithLawrence/aws-openai/commit/806865b2c5a0a250862b956319fe121ca452d423))

# [0.8.0](https://github.com/FullStackWithLawrence/aws-openai/compare/v0.7.2...v0.8.0) (2023-12-30)

### Bug Fixes

- add an error boundary ([4b7d021](https://github.com/FullStackWithLawrence/aws-openai/commit/4b7d02113d4c06f57aef067155f458ca3857d60c))
- convert return value to json if necessary. also verify dict keys before attempting to access anything ([376e14d](https://github.com/FullStackWithLawrence/aws-openai/commit/376e14defa77cef7d1bbc55ce98176f7b7be41bc))
- ensure that error messages are strings ([7c01083](https://github.com/FullStackWithLawrence/aws-openai/commit/7c01083e780391e637f551f4f49a76670ff771a7))
- scaffold an Error Boundary for the chatapp ([3fcbdb6](https://github.com/FullStackWithLawrence/aws-openai/commit/3fcbdb6c55d6748a1789d51e051cc8fab9b9456a))

### Features

- add v2 Settings class ([da8943d](https://github.com/FullStackWithLawrence/aws-openai/commit/da8943d55a568f1196e9389d8f3aaee1b15408bb))
- add v2 Settings class ([240433b](https://github.com/FullStackWithLawrence/aws-openai/commit/240433bd2a50c32da4bdf484420bc86b9db545d6))

## [0.7.2](https://github.com/FullStackWithLawrence/aws-openai/compare/v0.7.1...v0.7.2) (2023-12-19)

### Bug Fixes

- add unit tests for common ([ef7123f](https://github.com/FullStackWithLawrence/aws-openai/commit/ef7123f4adcd2fe3038ad6da8403a6ea73213cc5))

## [0.7.1](https://github.com/FullStackWithLawrence/aws-openai/compare/v0.7.0...v0.7.1) (2023-12-18)

### Bug Fixes

- refactor and update Layer build resources ([626034c](https://github.com/FullStackWithLawrence/aws-openai/commit/626034c06b7049d5a3638da017da66cddba72244))

# [0.7.0](https://github.com/FullStackWithLawrence/aws-openai/compare/v0.6.5...v0.7.0) (2023-12-18)

### Bug Fixes

- version writer was skipping first two lines ([5be9cf2](https://github.com/FullStackWithLawrence/aws-openai/commit/5be9cf2f313de60b4d5dfd64fcbd080194cff03c))

### Features

- add lists of .env and terraform.tfvars variables in use for settings ([ed64c74](https://github.com/FullStackWithLawrence/aws-openai/commit/ed64c74bfd7fdd7a99f684b5a22c65c1c1fc7a58))
- add openai and langchain parameters to unit tests ([d19af9f](https://github.com/FullStackWithLawrence/aws-openai/commit/d19af9fa108df885f091e23057f38e15f1df9552))
- add properties to report whether .env and/or terraform.tfvars files are in use ([5e3bea6](https://github.com/FullStackWithLawrence/aws-openai/commit/5e3bea603af3a9e96bb35ec601924edbe8e7d305))
- add Settings class and refactor ([b9f0286](https://github.com/FullStackWithLawrence/aws-openai/commit/b9f028632622c5a81eeee7bc8b5fe920d72a5bed))
- add unit test for langchain ([9a2b00d](https://github.com/FullStackWithLawrence/aws-openai/commit/9a2b00d903a8a6b097b52364b3fe4dd449cb165c))
- add unit tests for common ([cf3ac81](https://github.com/FullStackWithLawrence/aws-openai/commit/cf3ac81e2c2db889f2bcaaa43365af92e0437ca6))
- add unit tests for lambda_langchain ([4d94a87](https://github.com/FullStackWithLawrence/aws-openai/commit/4d94a875ea968dff85c48f6316fcd6ace5b31033))
- add unit tests for lambda_openai_v2 ([1b1a2c9](https://github.com/FullStackWithLawrence/aws-openai/commit/1b1a2c9d24d834e06d2d747845d1562b826437e5))
- refactor for OpenAI API v1 ([7fb6809](https://github.com/FullStackWithLawrence/aws-openai/commit/7fb6809a627eb8451af0054f24bd51bf3b52e07f))
- run Python unit tests on all pushes ([4957f63](https://github.com/FullStackWithLawrence/aws-openai/commit/4957f63028058504c11249b1c01a6ca28dd2bce1))

## [0.7.0]

- replace Terraform template_file() with templatefile()
- restructure Python modules. Place original lambda source code under openai_api and refactor common module so that it no longer needs to be pip installed. remove legacy lambda_openai.
- refactor layer_genai to remove pip-installed common code.
- refactor makefile and Github Actions so that these no longer have any special handling of Python source code.
- switch from pytest to built-in python unittest
- add Pydantic-based Settings class
- add unit testing of both lambdas + common code

## [0.6.5](https://github.com/FullStackWithLawrence/aws-openai/compare/v0.6.4...v0.6.5) (2023-12-05)

### Bug Fixes

- force a new release ([b5f8ee6](https://github.com/FullStackWithLawrence/aws-openai/commit/b5f8ee6541befb08c7e7f6b3a13bd841bc44680f))

## [0.6.4](https://github.com/FullStackWithLawrence/aws-openai/compare/v0.6.3...v0.6.4) (2023-11-24)

### Bug Fixes

- simulated bug to trigger new release ([f373039](https://github.com/FullStackWithLawrence/aws-openai/commit/f37303924693b4ffeae424476d9fdf3595efb311))

## [0.6.3](https://github.com/FullStackWithLawrence/aws-openai/compare/v0.6.2...v0.6.3) (2023-11-21)

### Bug Fixes

- Makefile evaluation of .env file ([9e068a3](https://github.com/FullStackWithLawrence/aws-openai/commit/9e068a37a0101e851ecbe619974ac0ba5ae597da))

## [0.6.2](https://github.com/FullStackWithLawrence/aws-openai/compare/v0.6.1...v0.6.2) (2023-11-19)

### Bug Fixes

- enable automated openai and langchain version bumps ([6d7fd81](https://github.com/FullStackWithLawrence/aws-openai/commit/6d7fd81a8527dd2d48268d0cbd9316ed372fc533))

## [0.6.1](https://github.com/FullStackWithLawrence/aws-openai/compare/v0.6.0...v0.6.1) (2023-11-19)

### Bug Fixes

- enable automated openai and langchain version bumps ([f3487ab](https://github.com/FullStackWithLawrence/aws-openai/commit/f3487ab1be0e343f787b373a4918eddefe3eb0d5))

# [0.6.0](https://github.com/FullStackWithLawrence/aws-openai/compare/v0.5.2...v0.6.0) (2023-11-17)

### Features

- automated pull requests ([aa27530](https://github.com/FullStackWithLawrence/aws-openai/commit/aa275303076943c9da7bdee28af1d9828d3b000c))

## [0.5.2](https://github.com/FullStackWithLawrence/aws-openai/compare/v0.5.1...v0.5.2) (2023-11-16)

### Features

- propagate merges to main back into dev branches: next, next-major, alpha, beta ([fd32caf](https://github.com/FullStackWithLawrence/aws-openai/pull/73/commits/959ebb91afe30bd7dec0ce93b994e2c0dfd32caf))
- create a top-level Pull Request workflow that triggers tech-specific unit ([fd32caf](https://github.com/FullStackWithLawrence/aws-openai/pull/73/commits/959ebb91afe30bd7dec0ce93b994e2c0dfd32caf))tests

### Refactoring

- refactor and expand the scope of automated PR revision workflows ([fd32caf](https://github.com/FullStackWithLawrence/aws-openai/pull/73/commits/959ebb91afe30bd7dec0ce93b994e2c0dfd32caf))
- consolidate all jobs related to merging to main into a single workflow ([fd32caf](https://github.com/FullStackWithLawrence/aws-openai/pull/73/commits/959ebb91afe30bd7dec0ce93b994e2c0dfd32caf))
- refactor Python unit test and only run when relevant modifications are ([fd32caf](https://github.com/FullStackWithLawrence/aws-openai/pull/73/commits/959ebb91afe30bd7dec0ce93b994e2c0dfd32caf))included in commit (\*.py, requirements.txt ([fd32caf](https://github.com/FullStackWithLawrence/aws-openai/pull/73/commits/959ebb91afe30bd7dec0ce93b994e2c0dfd32caf)), etc)
- scaffold a ReactJS unit test workflow ([fd32caf](https://github.com/FullStackWithLawrence/aws-openai/pull/73/commits/959ebb91afe30bd7dec0ce93b994e2c0dfd32caf))
- create a Terraform unit test workflow ([fd32caf](https://github.com/FullStackWithLawrence/aws-openai/pull/73/commits/959ebb91afe30bd7dec0ce93b994e2c0dfd32caf))

### Bug Fixes

- add GITHUB_TOKEN to semantic-release job ([bf4152d](https://github.com/FullStackWithLawrence/aws-openai/commit/bf4152d282b4652390b356711c0e84b422b07b30))

## [0.5.1](https://github.com/FullStackWithLawrence/aws-openai/compare/v0.5.0...v0.5.1) (2023-11-09)

### Bug Fixes

- don't persist credentials when calling actions/checkout ([72dea97](https://github.com/FullStackWithLawrence/aws-openai/commit/72dea975cb9d551f09ca329b354ac42189af14b2))
- downgrade openai to previous stable version ([bfc6962](https://github.com/FullStackWithLawrence/aws-openai/commit/bfc69624c9284c16a370b00c7d265f8898fb9c0f))
- revert last commit ([564e3fd](https://github.com/FullStackWithLawrence/aws-openai/commit/564e3fdd42465895f6f48937e420897a9d677348))
- revert to last stable version of openai ([d57c5db](https://github.com/FullStackWithLawrence/aws-openai/commit/d57c5db44853a06a7d32578932f86e92490637e0))
- stabilize openai breaking changes by making dependabot ignore related packages ([5ca1d81](https://github.com/FullStackWithLawrence/aws-openai/commit/5ca1d81e5cb3d8b8115e5343d114950506316597))

## [0.5.0](https://github.com/FullStackWithLawrence/aws-openai/compare/v0.4.0...v0.5.0) (2023-11-07)

### Bug Fixes

- add a hash of the output zip file ([c9b9a0b](https://github.com/FullStackWithLawrence/aws-openai/commit/c9b9a0b00561ea89b2f6e04f86baaf8d8ee099c5))
- do not run Python tests for dependabot pull requests until org secrets can be passed ([d0de24a](https://github.com/FullStackWithLawrence/aws-openai/commit/d0de24ad8ef9f62388f3aa1a70bc57ad34a2c19e))
- ensure that we're using --platform=linux/amd64 for the build ([aada484](https://github.com/FullStackWithLawrence/aws-openai/commit/aada4840d2ce31d93a738725ff01894d9370a0ab))
- merge conflict ([94d5833](https://github.com/FullStackWithLawrence/aws-openai/commit/94d5833ab319588c0138df1058501694d40b8fb4))
- replace hard-coded python version with ([868f118](https://github.com/FullStackWithLawrence/aws-openai/commit/868f1182ac490eeb16e6d144a6c888d125f82d13))
- switch event from pull_request to pull_request_target ([321ec8f](https://github.com/FullStackWithLawrence/aws-openai/commit/321ec8f8c806a86ed2f8263a1b326fb29fef10a5))
- switch from pull_requests event to pull_request_target event ([d70f2bc](https://github.com/FullStackWithLawrence/aws-openai/commit/d70f2bc57098d8066a5d1e5dd3c7d2e99bd8a60e))

### Features

- add a generic Langchain chat completion algorithm with chat history memory ([82dd402](https://github.com/FullStackWithLawrence/aws-openai/commit/82dd402e407c43f99d6499e6a4d2c5560f195421))
- add backward compatibility for Langchain responses ([93ad1d7](https://github.com/FullStackWithLawrence/aws-openai/commit/93ad1d7064fff6853b311c27218d1d9a1e96f191))
- upgrade Marv The Sarcastic Chatbot to Langchain w memory ([3c38ee2](https://github.com/FullStackWithLawrence/aws-openai/commit/3c38ee2d37ea0f880db0549286db2baa2717a81d))

## [0.4.0](https://github.com/FullStackWithLawrence/aws-openai/compare/v0.3.1...v0.4.0) (2023-11-03)

### Bug Fixes

- add a .env file to root so that test environment matches prod ([293b20e](https://github.com/FullStackWithLawrence/aws-openai/commit/293b20ec1537ef493539a59aa7a8d0216809b9f4))
- add openai_utils source location to the sys path for Python ([30eed8e](https://github.com/FullStackWithLawrence/aws-openai/commit/30eed8e2c6e1c27391d94597e43afee6db5eeb44))
- need to setup venv from ./requirements.txt so that the dev imports are included ([a907e98](https://github.com/FullStackWithLawrence/aws-openai/commit/a907e983051ad2cad721cb6a9347b0adb8f60c9a))
- paths should begin with ./ ([c8060bc](https://github.com/FullStackWithLawrence/aws-openai/commit/c8060bc2302190f074d3d7e78496781f5d6e627a))
- physically copy openai_utils to pip packages folder ([772b1d6](https://github.com/FullStackWithLawrence/aws-openai/commit/772b1d659b3bde6c5f80620e4539f23df68c3ffc))
- switch to Pytest ([be7746b](https://github.com/FullStackWithLawrence/aws-openai/commit/be7746bb090ac60d29ad42359d50c3c554ab80cf))

### Features

- add automated Python unit testing workflow to Github Actions ([dea18fc](https://github.com/FullStackWithLawrence/aws-openai/commit/dea18fc8cf2183d03613893f950ad30d7acd77fe))

## [0.3.1](https://github.com/FullStackWithLawrence/aws-openai/compare/v0.3.0...v0.3.1) (2023-11-03)

### Bug Fixes

- revert to secrets.PAT ([7342489](https://github.com/FullStackWithLawrence/aws-openai/commit/7342489ef7b7537419cc12732c1739a9fc3b42a8))

## [0.3.0] (2023-11-01)

The YouTube video for this release: [AWS Lambda Layers: When and How to use them](https://youtu.be/5Jf34t_UlZA)

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
