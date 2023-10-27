from lambda_langchain.handler import handler as langchain_handler


def handler(event, context, api_key=None, organization=None, pinecone_api_key=None):
    retval = langchain_handler(event, context, api_key, organization, pinecone_api_key)
    return retval
