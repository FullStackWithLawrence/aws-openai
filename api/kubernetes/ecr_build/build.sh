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
cd $BUILD_PATH

pwd
cp -R ../../python/openai_api/ ./openai_api

# Step 1: Build your Docker image
docker build -t $CONTAINER_NAME .

# Step 2: Authenticate Docker to your Amazon ECR registry
aws ecr get-login-password --region $AWS_REGION | docker login --username AWS --password-stdin $AWS_ACCOUNT_ID.dkr.ecr.$AWS_REGION.amazonaws.com

# Step 3: Tag your Docker image
docker tag chat_api:latest $AWS_ACCOUNT_ID.dkr.ecr.$AWS_REGION.amazonaws.com/chat_api:latest

# Step 4: Push your Docker image
docker push $AWS_ACCOUNT_ID.dkr.ecr.$AWS_REGION.amazonaws.com/chat_api:latest

rm -r ./openai_api
