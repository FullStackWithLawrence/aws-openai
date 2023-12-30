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
#------------------------------------------------------------------------------

# delete and recreate the package folder to remove any existing build artifacts
PACKAGE_NAME=openai_api

rm -rf $BUILD_PATH/$PACKAGE_NAME
mkdir -p $BUILD_PATH

# copy the python module(s) to the package folder
echo "BUILD_PATH: " $BUILD_PATH
echo "SOURCE_CODE_PATH: " $SOURCE_CODE_PATH

cp -R $SOURCE_CODE_PATH $BUILD_PATH/
cp terraform.tfvars $BUILD_PATH/$PACKAGE_NAME/
touch $BUILD_PATH/$PACKAGE_NAME/__init__.py

# remove any non-production artifacts
find $BUILD_PATH/$PACKAGE_NAME/ -name __pycache__ -type d -exec rm -rf {} +
find $BUILD_PATH/$PACKAGE_NAME/ -name tests -type d -exec rm -rf {} +
find $BUILD_PATH/$PACKAGE_NAME/ -name .gitignore -type f -exec rm -rf {} +
find $BUILD_PATH/$PACKAGE_NAME/ -name create_pkg.sh -type f -exec rm -rf {} +
find $BUILD_PATH/$PACKAGE_NAME/ -name .DS_Store -type f -exec rm -rf {} +
find $BUILD_PATH/$PACKAGE_NAME/ -name env.sh -type f -exec rm -rf {} +
