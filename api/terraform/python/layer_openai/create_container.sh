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


docker build -t $CONTAINER_NAME .
docker rm $CONTAINER_NAME
docker run --name $CONTAINER_NAME --entrypoint /bin/bash $CONTAINER_NAME -c "zip -r $PACKAGE_NAME ."

# Delete the distribution package if it exists
if [ -f $PACKAGE_NAME ]; then
    rm $PACKAGE_NAME
fi

docker cp $CONTAINER_NAME:/var/task/$PACKAGE_NAME .
