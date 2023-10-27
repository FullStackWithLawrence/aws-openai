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
# see https://github.com/ruzin/terraform_aws_lambda_langchain/
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

mkdir -p $PACKAGE_FOLDER


# copy the python module(s) to the package folder
cp lambda_handler.py $PACKAGE_FOLDER/
cp -R $PACKAGE_NAME $PACKAGE_FOLDER/
