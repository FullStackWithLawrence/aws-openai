SHELL := /bin/bash
S3_BUCKET = openai.lawrencemcdaniel.com
CLOUDFRONT_DISTRIBUTION_ID = E3AIBM1KMSJOP1

.PHONY: api-init api-activate api-lint api-clean api-test client-init client-lint client-update client-run client-build client-release

api-init: $(.env)
	ifeq ($(wildcard .venv),)
		python3.11 -m venv .venv
	endif
	ifeq ($(wildcard .env),)
		echo -e "OPENAI_API_ORGANIZATION=PLEASE-ADD-ME\nOPENAI_API_KEY=PLEASE-ADD-ME" >> .env
	endif
	pre-commit install

api-activate:
	. .venv/bin/activate &&  \
	pip install -r requirements.txt

api-test:
	cd ./api/terraform/python/openai_text && \
	pytest -k "not lambda_dist_pkg" tests/

api-lint:
	terraform fmt -recursive && \
	pre-commit run --all-files && \
	black ./api/terraform/python/

api-clean:
	rm -rf .venv

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
