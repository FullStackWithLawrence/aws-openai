"""
 see: https://www.youtube.com/watch?v=aywZrzNaKjs
"""
from dotenv import load_dotenv, find_dotenv
import os

# substantive imports
from langchain.llms import OpenAI
from langchain.schema import AIMessage, HumanMessage, SystemMessage
from langchain.chat_models import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.chains import SimpleSequentialChain
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings import OpenAIEmbeddings

import pinecone
from langchain.vectorstores.pinecone import Pinecone

# Load environment variables from .env file in all folders
dotenv_path = find_dotenv()
if os.path.exists(dotenv_path):
    load_dotenv(dotenv_path=dotenv_path, verbose=True)
    OPENAI_API_KEY = os.environ["OPENAI_API_KEY"]
    OPENAI_API_ORGANIZATION = os.environ["OPENAI_API_ORGANIZATION"]
    PINECONE_API_KEY = os.environ["PINECONE_API_KEY"]
    PINECONE_ENVIRONMENT = os.environ["PINECONE_ENVIRONMENT"]
else:
    raise Exception("No .env file found in root directory of repository")


def test_01_basic():
    """Test a basic request"""

    llm = OpenAI(model_name="text-davinci-003")
    retval = llm("explain large language models in one sentence")
    print(retval)


def test_02_chat_model():
    chat = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0.3)
    messages = [
        SystemMessage(content="You are an expert data scientist"),
        HumanMessage(
            content="Write a Python script that trains a neural network on simulated data"
        ),
    ]
    retval = chat(messages)
    print(retval.content, end="\n")


def get_prompt():
    template = """
    You are an expert data scientist with an expertise in building deep learning models.
    Explain the concept of {concept} in a couple of lines.
    """
    prompt = PromptTemplate(input_variables=["concept"], template=template)
    return prompt


def test_03_prompt_templates():
    llm = OpenAI(model_name="text-davinci-003")
    prompt = get_prompt()
    retval = llm(prompt.format(concept="regularization"))
    print(retval)


def get_chain(llm, prompt):
    chain = LLMChain(llm=llm, prompt=prompt)
    return chain


def test_04_chain():
    llm = OpenAI(model_name="text-davinci-003")
    prompt = get_prompt()
    chain = get_chain(llm=llm, prompt=prompt)
    print(chain.run("autoencoder"))


def get_overall_chain(chains):
    return SimpleSequentialChain(chains=chains, verbose=True)


def get_prompt_two():
    second_prompt = PromptTemplate(
        input_variables=["ml_concept"],
        template="""
        Turn the concept description of {ml_concept} and explain it to me like I'm five in 500 words.
        """,
    )
    return second_prompt


def get_explanation():
    llm = OpenAI(model_name="text-davinci-003")
    prompt = get_prompt()
    chain_one = get_chain(llm=llm, prompt=prompt)

    second_prompt = get_prompt_two()
    chain_two = get_chain(llm=llm, prompt=second_prompt)
    overall_chain = get_overall_chain(chains=[chain_one, chain_two])
    return overall_chain.run("autoencoder")


def test_05_chains():
    explanation = get_explanation()
    print(explanation)


def test_06_embeddings():
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=100,
        chunk_overlap=0,
    )
    explanation = get_explanation()
    texts = text_splitter.create_documents([explanation])
    print(texts[0].page_content)

    embeddings = OpenAIEmbeddings(model_name="ada")
    # query_result = embeddings.embed_query(texts[0].page_content)

    print(PINECONE_API_KEY)
    pinecone.init(api_key=PINECONE_API_KEY, environment=PINECONE_ENVIRONMENT)
    index_name = "hello-world"
    search = Pinecone.from_documents(texts, embedding=embeddings, index_name=index_name)


def main():
    test_06_embeddings()


if __name__ == "__main__":
    main()
