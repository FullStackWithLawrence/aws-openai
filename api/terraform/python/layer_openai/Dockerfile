# Use an AWS Lambda Python runtime as the base image
# https://hub.docker.com/r/amazon/aws-lambda-python
# ------------------------------------------------------

# Stage 1: Build dependencies for x86_64
FROM --platform=linux/amd64 public.ecr.aws/lambda/python:3.11

WORKDIR /var/task

COPY requirements.txt .

RUN yum install -y zip
RUN pip install -r requirements.txt --target python/lib/python3.11/site-packages
