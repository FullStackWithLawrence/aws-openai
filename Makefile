SHELL := /bin/bash

init:
	python3.11 -m venv .venv
	source .venv/bin/activate
	pip install -r requirements.txt

activate:
	source .venv/bin/activate

lint:
	terraform fmt -recursive
	pre-commit run --all-files
	black ./terraform/python/
