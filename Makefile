SHELL := /bin/bash
S3_BUCKET = openai.lawrencemcdaniel.com
CLOUDFRONT_DISTRIBUTION_ID = E3AIBM1KMSJOP1

.PHONY: api-init api-activate api-lint api-clean api-test client-init client-lint client-update client-run client-build client-release

# Default target executed when no arguments are given to make.
all: help

######################
# AWS API Gateway + Lambda + OpenAI
######################
api-init: $(.env)
	ifeq ($(wildcard .venv),)
		python3.11 -m venv .venv
	endif
	ifeq ($(wildcard .env),)
		echo -e "OPENAI_API_ORGANIZATION=PLEASE-ADD-ME\nOPENAI_API_KEY=PLEASE-ADD-ME\nPINECONE_API_KEY=PLEASE-ADD-ME\nDEBUG_MODE=True\n" >> .env
	endif
	pre-commit install

api-activate:
	. .venv/bin/activate && \
	pip install -r requirements.txt

api-test:
	cd ./api/terraform/python/openai_text/openai_text/ && \
	pytest -v -s tests/

api-lint:
	terraform fmt -recursive && \
	pre-commit run --all-files && \
	black ./api/terraform/python/

api-clean:
	rm -rf .venv

######################
# React app
######################
client-init:
	cd ./client && npm install

client-lint:
	cd ./client && npm run lint

client-update:
	npm install -g npm
	npm install -g npm-check-updates
	ncu --upgrade --packageFile ./client/package.json
	npm update -g
	npm install ./client/

client-run:
	cd ./client && npm run dev

client-build:
	cd ./client && npm run build

client-release:
	#---------------------------------------------------------
	# usage:      deploy prouduction build of the React
	#             app to AWS S3 bucket.
	#
	#             1. Build the React application
	#             2. Upload to AWS S3
	#             3. Invalidate all items in the AWS Cloudfront CDN.
	#---------------------------------------------------------
	npm run build --prefix ./client/

	# ------------------------
	# add all built files to the S3 bucket.
	# ------------------------
	aws s3 sync ./client/dist/ s3://$(S3_BUCKET) \
				--acl public-read \
				--delete --cache-control max-age=31536000,public \
				--expires '31 Dec 2050 00:00:01 GMT'

	# ------------------------
	# remove the cache-control header created above with a "no-cache" header so that browsers never cache this page
	# ------------------------
	aws s3 cp s3://$(S3_BUCKET)/index.html s3://$(S3_BUCKET)/index.html --metadata-directive REPLACE --cache-control max-age=0,no-cache,no-store,must-revalidate --content-type text/html --acl public-read

	# invalidate the Cloudfront cache
	aws cloudfront create-invalidation --distribution-id $(CLOUDFRONT_DISTRIBUTION_ID) --paths "/*" "/index.html"

######################
# HELP
######################

help:
	@echo '===================='
	@echo '-- AWS API Gateway + Lambda --'
	@echo 'api-init            - create a Python virtual environment and install dependencies'
	@echo 'api-activate        - activate the Python virtual environment'
	@echo 'api-test            - run Python unit tests'
	@echo 'api-lint            - run Python linting'
	@echo 'api-clean           - destroy the Python virtual environment'
	@echo '-- React App --'
	@echo 'client-init         - run npm install'
	@echo 'client-lint         - run npm lint'
	@echo 'client-update       - update npm packages'
	@echo 'client-run          - run the React app in development mode'
	@echo 'client-build        - build the React app for production'
	@echo 'client-release      - deploy the React app to AWS S3 and invalidate the Cloudfront CDN'
