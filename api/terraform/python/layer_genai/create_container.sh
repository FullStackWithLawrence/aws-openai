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
#------------------------------------------------------------------------------
cd $SOURCE_CODE_PATH

# we have to phyically copy the python module(s) to the dist venv site-packages folder
# because we're installing this package as an executate and pip therefore won't
# copy the module(s) to the site-packages folder for us.
cp -R $PARENT_DIRECTORY/openai_utils/ $SOURCE_CODE_PATH/venv/lib/python3.11/site-packages/
cp -rf SOURCE_CODE_PATH/venv/lib/python3.11/site-packages/openai_utils/__pycache__
cp -rf SOURCE_CODE_PATH/venv/lib/python3.11/site-packages/openai_utils/openai_utils.egg-info
cp -rf SOURCE_CODE_PATH/venv/lib/python3.11/openai_utils/tests

docker build -t $CONTAINER_NAME .
docker rm $CONTAINER_NAME
docker run --name $CONTAINER_NAME --entrypoint /bin/bash $CONTAINER_NAME -c "zip -r $PACKAGE_NAME ."

# Delete the distribution package if it exists
if [ -f $PACKAGE_NAME ]; then
    rm $PACKAGE_NAME
fi

docker cp $CONTAINER_NAME:/var/task/$PACKAGE_NAME .
