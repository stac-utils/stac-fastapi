#!make
APP_HOST ?= 0.0.0.0
APP_PORT ?= 8080
EXTERNAL_APP_PORT ?= ${APP_PORT}
run_docker = docker run -it --rm \
				-p ${EXTERNAL_APP_PORT}:${APP_PORT} \
				-v $(shell pwd):/app \
				--env-file .env \
				--env APP_HOST=${APP_HOST} \
				--env APP_PORT=${APP_PORT} \
				arturo-stac-api_app

.PHONY: docker-shell
docker-shell:
	$(run_docker) /bin/bash

.PHONY: test
test:
	$(run_docker) pytest