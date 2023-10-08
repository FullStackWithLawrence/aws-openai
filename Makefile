SHELL := /bin/bash

.PHONY: init activate lint clean test

init: $(.env)
	python3.11 -m venv .venv
	echo -e "OPENAI_API_ORGANIZATION=PLEASE-ADD-ME\nOPENAI_API_KEY=PLEASE-ADD-ME" >> .env
	pre-commit install

activate:
	. .venv/bin/activate
	pip install -r requirements.txt

lint:
	terraform fmt -recursive
	pre-commit run --all-files
	black ./terraform/python/

clean:
	rm -rf .venv
	# Add any other generated files to remove here
