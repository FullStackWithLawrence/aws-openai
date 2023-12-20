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

# Change Log

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](http://keepachangelog.com/) and this project adheres to [Semantic Versioning](http://semver.org/).

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
