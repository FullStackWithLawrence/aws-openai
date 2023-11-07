# Use an AWS Lambda Python runtime as the base image
# https://hub.docker.com/r/amazon/aws-lambda-python
#
# create the docker image for both x86_64 and arm64.
# ------------------------------------------------------

# ------------------------------------------------------
# Stage 1: Build dependencies for x86_64
# ------------------------------------------------------
FROM public.ecr.aws/lambda/python:3.11 as builder-x86_64

# Set a working directory
WORKDIR /var/task

# Copy the requirements.txt file into the Docker container
COPY requirements.txt .
COPY openai_utils ./openai_utils

# Install the Python packages
RUN yum install -y zip
RUN pip install -r requirements.txt --target python/lib/python3.11/site-packages
RUN cp -R openai_utils python/lib/python3.11/site-packages

# ------------------------------------------------------
# Stage 2: Build dependencies for arm64
# ------------------------------------------------------
FROM --platform=linux/arm64 public.ecr.aws/lambda/python:3.11 as builder-arm64

WORKDIR /var/task

COPY requirements.txt .
COPY openai_utils ./openai_utils

RUN yum install -y zip
RUN pip install -r requirements.txt --target python/lib/python3.11/site-packages
RUN cp -R openai_utils python/lib/python3.11/site-packages

# ------------------------------------------------------
# Stage 3: Combine dependencies
# ------------------------------------------------------
FROM public.ecr.aws/lambda/python:3.11

WORKDIR /var/task
RUN yum install -y zip

COPY --from=builder-x86_64 /var/task/python/lib/python3.11/site-packages ./python/lib/python3.11/site-packages
COPY --from=builder-arm64 /var/task/python/lib/python3.11/site-packages ./python/lib/python3.11/site-packages
