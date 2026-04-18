FROM public.ecr.aws/lambda/python:3.13

RUN pip install --no-cache-dir --upgrade pip

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY python/ /var/task/

CMD ["openai_api.lambda_openai_v2.lambda_handler.handler"]
