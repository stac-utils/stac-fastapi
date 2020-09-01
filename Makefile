#!make
APP_HOST ?= 0.0.0.0
APP_PORT ?= 8080
EXTERNAL_APP_PORT ?= ${APP_PORT}
run_docker = docker run -it --rm \
				-p ${EXTERNAL_APP_PORT}:${APP_PORT} \
                -v ~/.aws:/root/.aws \
				-v $(shell pwd):/app \
				--env APP_HOST=${APP_HOST} \
				--env APP_PORT=${APP_PORT} \
				--env-file .env.example \
				arturo-ai/stac-api:latest

.PHONY: image
image:
	docker build -t arturo-ai/stac-api:latest .

.PHONY: docker-run
docker-run: image
	$(run_docker)

.PHONY: docker-shell
docker-shell:
	$(run_docker) /bin/bash

.PHONY: test
test:
	$(run_docker) pytest