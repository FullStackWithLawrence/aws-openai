#!/bin/bash
#------------------------------------------------------------------------------
# written by: Lawrence McDaniel
#             https://lawrencemcdaniel.com/
#
# date: sep-2023
#
# usage:  Lambda Python packaging tool.
#         Called by Terraform "null_resource". Copies python
#         module(s) plus any requirements to a dedicated folder so that
#         it can be archived to a zip file for upload to
#         AWS Lambda by Terraform.
#
# see https://github.com/ruzin/terraform_aws_lambda_python/
#------------------------------------------------------------------------------
#LAYER_NAME       = "genai"
#SOURCE_CODE_PATH = "/Users/mcdaniel/desktop/aws-openai/api/terraform/python/layer_genai"
#PACKAGE_FOLDER   = "python"
#RUNTIME          = var.lambda_python_runtime

cd $SOURCE_CODE_PATH

# force a Terraform state change in the package
# by deleting any existing zip archive that might exist.
touch "layer_${LAYER_NAME}_dst.zip"
if [ -f "layer_${LAYER_NAME}_dst.zip" ]; then
  rm "layer_${LAYER_NAME}_dst.zip"
fi

# triggers a complete rebuild of the package
if [ -d "archive" ]; then
  rm -rf "archive"
fi

mkdir -p "archive/$PACKAGE_FOLDER/$LAYER_NAME"

# create a dedicated Python virtual environment
# for the Python Lambda resources calling this script.
if [ ! -d "venv" ]; then
  virtualenv -p $RUNTIME venv
fi

# launch the environment, install all requirements
# and then deactivate in order to avoid any
# potentially weird ghost effects later on.
source venv/bin/activate
pip install -r requirements.txt
pip install --no-cache-dir ./openai_utils
deactivate

# Note: this copies openai along with all of its requirements.
#       in aggregate there are around 2 dozen packages.
#
#       The overall size of this package exceeds that which is viewable
#       from within the AWS Lambda console.
cp -r "venv/" "archive/$PACKAGE_FOLDER"
