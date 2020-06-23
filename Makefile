#!make
APP_HOST ?= 0.0.0.0
APP_PORT ?= 8081
EXTERNAL_APP_PORT ?= ${APP_PORT}
run_docker = docker run -it --rm \
				-p ${EXTERNAL_APP_PORT}:${APP_PORT} \
				-v $(shell pwd):/app \
				--env-file .env \
				--env APP_HOST=${APP_HOST} \
				--env APP_PORT=${APP_PORT} \
				arturo-ai/stac-api:latest

.PHONY: image
image:
	docker build \
		--build-arg environment=development \
		-t arturo-ai/stac-api:latest .

.PHONY: docker-shell
docker-shell: image
	$(run_docker) /bin/bash

.PHONY: test
test: image
	$(run_docker_test) pytest