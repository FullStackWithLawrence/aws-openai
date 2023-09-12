#!/bin/bash
# see https://github.com/ruzin/terraform_aws_lambda_python/

cd $source_code_path

if [-d $package_folder]
then
  rm -rf $package_folder
fi

mkdir -p $package_folder

virtualenv -p $runtime venv
source venv/bin/activate

pip install -r requirements.txt
deactivate

cp -r "venv/lib/$runtime/site-packages/openai" $package_folder/
cp *.py $package_folder/

rm -rf venv
