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

echo SOURCE_CODE_PATH ${SOURCE_CODE_PATH}
echo PACKAGE_FOLDER ${PACKAGE_FOLDER}
echo RUNTIME ${RUNTIME}

cd $SOURCE_CODE_PATH

# triggers a complete rebuild of the package
if [ -d $PACKAGE_FOLDER ]; then
  rm -rf $PACKAGE_FOLDER
fi

# force a Terraform state change in the package
# by deleting any existing zip archive that might exist.
if [ -f "${PACKAGE_FOLDER}.zip" ]; then
  rm "${PACKAGE_FOLDER}.zip"
fi

mkdir -p $LAYER_NAME/$PACKAGE_FOLDER

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
cp -r "venv/" $LAYER_NAME/$PACKAGE_FOLDER/
