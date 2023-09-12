#!/bin/bash
#------------------------------------------------------------------------------
# written by: Lawrence McDaniel
#             https://lawrencemcdaniel.com/
#
# date: sep-2023
#
# usage:  copy python module(s) plus any requirements
#         to a dedicated folder so that it can be archived
#         for upload to AWS Lambda by Terraform.
#
# see https://github.com/ruzin/terraform_aws_lambda_python/
#------------------------------------------------------------------------------

cd $source_code_path

if [ -d $package_folder ]; then
  rm -rf $package_folder
fi

if [ -f "${package_folder}.zip" ]; then
  rm "${package_folder}.zip"
fi

mkdir -p $package_folder

if [ ! -d "venv" ]; then
  virtualenv -p $runtime venv
fi

source venv/bin/activate
pip install -r requirements.txt
deactivate

cp -r "venv/lib/$runtime/site-packages/openai" $package_folder/
cp *.py $package_folder/
