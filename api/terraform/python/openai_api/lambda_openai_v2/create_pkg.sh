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

# delete and recreate the package folder to remove any existing build artifacts
DEST_PATH=$BUILD_PATH/$PACKAGE_FOLDER
rm -rf $DEST_PATH
mkdir -p $DEST_PATH

# copy the python module(s) to the package folder
cp $SOURCE_CODE_PATH/*.py $PACKAGE_FOLDER/
cp -R $PARENT_DIRECTORY/common/ $PACKAGE_FOLDER/
cp -R $PARENT_DIRECTORY/*.py $PACKAGE_FOLDER/
