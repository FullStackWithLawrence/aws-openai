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

from langchain_experimental.agents.agent_toolkits.python.base import create_python_agent
from langchain.tools.python.tool import PythonAstREPLTool
from langchain.python import PythonREPL
from langchain.llms.openai import OpenAI

PINECONE_INDEX_NAME = "langchain-quickstart"

# Load environment variables from .env file in all folders
dotenv_path = find_dotenv()
if os.path.exists(dotenv_path):
    load_dotenv(dotenv_path=dotenv_path, verbose=True)
    OPENAI_API_KEY = os.environ["OPENAI_API_KEY"]
    OPENAI_API_ORGANIZATION = os.environ["OPENAI_API_ORGANIZATION"]
    PINECONE_API_KEY = os.environ["PINECONE_API_KEY"]
    PINECONE_ENVIRONMENT = os.environ["PINECONE_ENVIRONMENT"]
    pinecone.init(api_key=PINECONE_API_KEY, environment=PINECONE_ENVIRONMENT)
else:
    raise Exception("No .env file found in root directory of repository")


class PineconeTests:
    multi_prompt_explanation = None
    texts_splitter_results = None
    pinecone_search = None
    openai_embedding = OpenAIEmbeddings(model_name="ada")
    query_result = None
    agent_executor = create_python_agent(
        llm=OpenAI(temperature=0, max_tokens=1000),
        tool=PythonAstREPLTool(),
        verbose=True,
    )

    def test_01_basic(self):
        """Test a basic request"""

        llm = OpenAI(model_name="text-davinci-003")
        retval = llm("explain large language models in one sentence")
        print(retval)

    def test_02_chat_model(self):
        chat = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0.3)
        messages = [
            SystemMessage(content="You are an expert data scientist"),
            HumanMessage(
                content="Write a Python script that trains a neural network on simulated data"
            ),
        ]
        retval = chat(messages)
        print(retval.content, end="\n")

    def get_prompt(self):
        template = """
        You are an expert data scientist with an expertise in building deep learning models.
        Explain the concept of {concept} in a couple of lines.
        """
        prompt = PromptTemplate(input_variables=["concept"], template=template)
        return prompt

    def test_03_prompt_templates(self):
        llm = OpenAI(model_name="text-davinci-003")
        prompt = self.get_prompt()
        retval = llm(prompt.format(concept="regularization"))
        print(retval)

    def get_chain(self, llm, prompt):
        chain = LLMChain(llm=llm, prompt=prompt)
        return chain

    def test_04_chain(self):
        llm = OpenAI(model_name="text-davinci-003")
        prompt = self.get_prompt()
        chain = self.get_chain(llm=llm, prompt=prompt)
        print(chain.run("autoencoder"))

    def get_overall_chain(self, chains):
        return SimpleSequentialChain(chains=chains, verbose=True)

    def get_prompt_two(self):
        second_prompt = PromptTemplate(
            input_variables=["ml_concept"],
            template="""
            Turn the concept description of {ml_concept} and explain it to me like I'm five in 500 words.
            """,
        )
        return second_prompt

    def get_explanation(self):
        llm = OpenAI(model_name="text-davinci-003")
        prompt = self.get_prompt()
        chain_one = self.get_chain(llm=llm, prompt=prompt)

        second_prompt = self.get_prompt_two()
        chain_two = self.get_chain(llm=llm, prompt=second_prompt)
        overall_chain = self.get_overall_chain(chains=[chain_one, chain_two])
        return overall_chain.run("autoencoder")

    def test_05_chains(self):
        self.multi_prompt_explanation = self.get_explanation()
        print(self.multi_prompt_explanation)

    def test_06_embeddings(self):
        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=100,
            chunk_overlap=0,
        )
        self.multi_prompt_explanation = self.get_explanation()
        if not self.texts_splitter_results:
            self.texts_splitter_results = text_splitter.create_documents(
                [self.multi_prompt_explanation]
            )
            print(self.texts_splitter_results[0].page_content)

    def test_06_embeddings_b(self):
        if not self.query_result:
            self.query_result = self.openai_embedding.embed_query(
                self.texts_splitter_results[0].page_content
            )
            print(self.query_result)
        self.pinecone_search = Pinecone.from_documents(
            self.texts_splitter_results,
            embedding=self.openai_embedding,
            index_name=PINECONE_INDEX_NAME,
        )

    def test_07_pinecone_search(self):
        query = "What is magical about an autoencoder?"
        result = self.pinecone_search.similarity_search(query)
        print(result)

    def test_08_agent_executor(self):
        retval = self.agent_executor.run(
            "Find the roots (zeros) of the quadratic function 3 * x**2 + 2*x -1"
        )
        print(retval)

    def main(self):
        # self.test_06_embeddings()
        # self.test_06_embeddings_b()
        # self.test_07_pinecone_search()
        self.test_08_agent_executor


def main():
    pintcode_tests = PineconeTests()
    pintcode_tests.main()


if __name__ == "__main__":
    main()
