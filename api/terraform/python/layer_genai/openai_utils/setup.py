from setuptools import setup, find_packages

setup(
    name="openai_utils",
    version="0.5.0",
    description="Common utilities for OpenAI",
    author="Lawrence McDaniel",
    author_email="lpm0073@gmail.com",
    packages=find_packages(),
    install_requires=["openai>=0.28"],
)
