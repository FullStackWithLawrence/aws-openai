from openai_text.handler import handler as openai_handler


def handler(event, context, api_key=None, organization=None, pinecone_api_key=None):
    retval = openai_handler(event, context, api_key, organization, pinecone_api_key)
    return retval
