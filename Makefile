SHELL := /bin/bash

lint:
	terraform fmt -recursive
	pre-commit run --all-files
	black ./terraform/python/
