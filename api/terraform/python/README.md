# AWS Lambda Functions

Python integrations for OpenAI API. Note that due to size constraints with AWS Lambda functions, this code is compulsorily split into various separate modules, as follows:

1. **openai_api**: contains the actual Python source code to implement each API endpoint. Follow [this link](./openai_api/README.md) for additional documentation on this source code.

2. **layer_langchain**: deploys an [AWS Lambda Layer](https://docs.aws.amazon.com/lambda/latest/dg/chapter-layers.html) containing additional Python [PyPi](https://pypi.org/) requirements used by [lambda_langchain](../lambda_langchain.tf).

3. **layer_nlp**: deploys an [AWS Lambda Layer](https://docs.aws.amazon.com/lambda/latest/dg/chapter-layers.html) containing additional Python [PyPi](https://pypi.org/) requirements used by [lambda_openai_function](../lambda_openai_function.tf) to implement the function_weather.py feature

4. **layer_openai**: deploys an [AWS Lambda Layer](https://docs.aws.amazon.com/lambda/latest/dg/chapter-layers.html) containing additional Python [PyPi](https://pypi.org/) requirements used by [lambda_openai_function](../lambda_openai_function.tf) to implement the function_weather.py feature

5. **layer_pandas**: deploys an [AWS Lambda Layer](https://docs.aws.amazon.com/lambda/latest/dg/chapter-layers.html) containing common Python [PyPi](https://pypi.org/) requirements used by all lambda functions.

AWS Lambda distribution packages are limited to 50mb in zipped compressed format, and 250mb when uncompressed. It turns out to be surprisingly challenging to squeeze all of the various Python requirements into a manageable combination of Layers that satisfy this limitation. Hence, there are four layers for this project. Note that this limitation is unique to AWS Lambda. You certainly would not face this challenge if instead you were to deploy this code to say, AWS Elastic Container Service or AWS Elastic Kubernetes Service.
