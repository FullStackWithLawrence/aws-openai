# Use an AWS Lambda Python runtime as the base image
FROM public.ecr.aws/lambda/python:3.11

# Set a working directory
WORKDIR /var/task

# Copy the requirements.txt file into the Docker container
COPY requirements.txt .
COPY openai_utils ./openai_utils

# Install the Python packages
RUN yum install -y zip
RUN pip install -r requirements.txt -t python/lib/python3.11/site-packages
RUN cp -R openai_utils python/lib/python3.11/site-packages
