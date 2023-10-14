SHELL := /bin/bash

.PHONY: init activate lint clean test

api-init: $(.env)
	python3.11 -m venv .venv
	echo -e "OPENAI_API_ORGANIZATION=PLEASE-ADD-ME\nOPENAI_API_KEY=PLEASE-ADD-ME" >> .env
	pre-commit install

api-activate:
	. .venv/bin/activate
	pip install -r requirements.txt

api-lint:
	terraform fmt -recursive
	pre-commit run --all-files
	black ./api/terraform/python/

api-clean:
	rm -rf .venv
	# Add any other generated files to remove here


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

client-build:
	cd ./client && npm run build

client-release:
	#---------------------------------------------------------
	# usage:      deploy prouduction build of openai.lawrencemcdaniel.com
	#             app to AWS S3 bucket.
	#
	#             https://gist.github.com/kellyrmilligan/e242d3dc743105fe91a83cc933ee1314
	#
	#             1. Build the React application
	#             2. Upload to AWS S3
	#             3. Invalidate all items in the AWS Cloudfront CDN.
	#---------------------------------------------------------
	npm run build --prefix ./client/

	# ------------------------
	# add all built files to the S3 bucket.
	# ------------------------
	aws s3 sync ./client/dist/ s3://openai.lawrencemcdaniel.com \
				--acl public-read \
				--delete --cache-control max-age=31536000,public \
				--expires '31 Dec 2050 00:00:01 GMT'

	# ------------------------
	# remove the cache-control header created above with a "no-cache" header so that browsers never cache this page
	# ------------------------
	aws s3 cp s3://openai.lawrencemcdaniel.com/index.html s3://openai.lawrencemcdaniel.com/index.html --metadata-directive REPLACE --cache-control max-age=0,no-cache,no-store,must-revalidate --content-type text/html --acl public-read
	aws s3 cp s3://openai.lawrencemcdaniel.com/manifest.json s3://openai.lawrencemcdaniel.com/manifest.json --metadata-directive REPLACE --cache-control max-age=0,no-cache,no-store,must-revalidate --content-type text/json --acl public-read

	# invalidate the Cloudfront cache
	aws cloudfront create-invalidation --distribution-id E3AIBM1KMSJOP1 --paths "/*" "/index.html" "/manifest.json"
