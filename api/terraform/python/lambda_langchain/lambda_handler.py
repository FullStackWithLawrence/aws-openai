"""
lambda_langchain/
├── lambda_handler.py
├── lambda_langchain/
│   ├── __init__.py
│   ├── const.py
│   └── handler.py
│   └── utils.py
│   └── validators.py
│   └── wrapper.py
└── python/
    └── my_layer/
        ├── python/
        │   ├── my_module/
        │   │   ├── __init__.py
        │   │   ├── module1.py
        │   │   └── module2.py
        │   └── other_module/
        │       ├── __init__.py
        │       ├── module3.py
        │       └── module4.py
        └── my_layer.py                 <<----- NOT CORRECT?????
"""
from lambda_langchain.handler import handler as langchain_handler


def handler(event, context, api_key=None, organization=None, pinecone_api_key=None):
    retval = langchain_handler(event, context, api_key, organization, pinecone_api_key)
    return retval
