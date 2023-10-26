"""
Transformations for the LangChain API for OpenAI
"""
from langchain.schema import AIMessage, HumanMessage, SystemMessage
from langchain.chat_models import ChatOpenAI

# from langchain.llms.openai import OpenAI
# from langchain.prompts import PromptTemplate
# from langchain.chains import LLMChain
# from langchain.chains import SimpleSequentialChain
# from langchain.text_splitter import RecursiveCharacterTextSplitter
# from langchain.embeddings import OpenAIEmbeddings
# from langchain.vectorstores.pinecone import Pinecone
# from langchain_experimental.agents.agent_toolkits.python.base import create_python_agent
# from langchain.tools.python.tool import PythonAstREPLTool
# from langchain.python import PythonREPL


def get_content_for_role(messages: list, role: str) -> str:
    """Get the text content from the messages list for a given role"""
    retval = [d.get("content") for d in messages if d["role"] == role][0]
    return retval


def process_request(model, messages, temperature, max_tokens) -> str:
    chat = ChatOpenAI(model_name=model, temperature=temperature, max_tokens=max_tokens)

    system_message = get_content_for_role(messages, "system")
    user_message = get_content_for_role(messages, "user")
    messages = [
        SystemMessage(content=system_message),
        HumanMessage(content=user_message),
    ]
    retval = chat(messages)
    return retval.content
