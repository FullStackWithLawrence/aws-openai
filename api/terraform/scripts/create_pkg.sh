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

cd $source_code_path

# triggers a complete rebuild of the package
if [ -d $package_folder ]; then
  rm -rf $package_folder
fi

# force a Terraform state change in the package
# by deleting any existing zip archive that might exist.
if [ -f "${package_folder}.zip" ]; then
  rm "${package_folder}.zip"
fi

mkdir -p $package_folder

# create a dedicated Python virtual environment
# for the Python Lambda resources calling this script.
if [ ! -d "venv" ]; then
  virtualenv -p $runtime venv
fi

# launch the environment, install all requirements
# and then deactivate in order to avoid any
# potentially weird ghost effects later on.
source venv/bin/activate
pip install -r requirements.txt
deactivate

# Note: this copies openai along with all of its requirements.
#       in aggregate there are around 2 dozen packages.
#
#       The overall size of this package exceeds that which is viewable
#       from within the AWS Lambda console.
cp -r "venv/lib/$runtime/site-packages/" $package_folder/
cp *.py $package_folder/
