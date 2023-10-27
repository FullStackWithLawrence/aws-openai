import sys
import os

# Add the path to the layer to the sys.path list
# see: https://docs.aws.amazon.com/lambda/latest/dg/configuration-envvars.html
layer_path = os.path.join(os.environ["LAMBDA_TASK_ROOT"], "python", "langchain")
sys.path.append(layer_path)

from lambda_langchain.handler import handler as langchain_handler


def handler(event, context, api_key=None, organization=None, pinecone_api_key=None):
    print(f"layer_path: {layer_path}".format(layer_path=layer_path))
    retval = langchain_handler(event, context, api_key, organization, pinecone_api_key)
    return retval
