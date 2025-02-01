# Use an AWS Lambda Python runtime as the base image
# https://hub.docker.com/r/amazon/aws-lambda-python
# ------------------------------------------------------
FROM --platform=linux/amd64 python:3.11-buster

WORKDIR /app

COPY openai_api .
COPY requirements.txt .

RUN apt-get update && apt-get install -y zip
RUN pip install -r requirements.txt

CMD ["python", "service_controller.py"]

EXPOSE 8000

ENV DEBUG_MODE=False
ARG OPENAI_API_KEY
ARG PINECONE_API_KEY
ARG PINECONE_ENVIRONMENT
ARG GOOGLE_MAPS_API_KEY
