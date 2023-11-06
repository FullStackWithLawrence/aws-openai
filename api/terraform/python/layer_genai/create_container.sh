#!/bin/bash
#------------------------------------------------------------------------------
# written by: Lawrence McDaniel
#             https://lawrencemcdaniel.com/
#
# date:   nov-2023
#
# usage:  Lambda Python packaging tool.
#         Called by Terraform "null_resource". Copies python
#         module(s) plus any requirements to a dedicated folder so that
#         it can be archived to a zip file for upload to
#         AWS Lambda by Terraform.
#
# see https://github.com/ruzin/terraform_aws_lambda_python/
#------------------------------------------------------------------------------
cd $SOURCE_CODE_PATH
echo "source-code-path: $SOURCE_CODE_PATH"

docker build -t lambda-genai .
docker rm lambda-genai
docker run --name lambda-genai --entrypoint /bin/bash lambda-genai -c "zip -r layer.zip ."

# Delete the layer.zip file if it exists
if [ -f layer.zip ]; then
    rm layer.zip
fi

docker cp lambda-genai:/var/task/layer.zip .
