#!make
APP_HOST ?= 0.0.0.0
APP_PORT ?= 8080
EXTERNAL_APP_PORT ?= ${APP_PORT}
run_docker = docker run -it --rm \
				-p ${EXTERNAL_APP_PORT}:${APP_PORT} \
				-v $(shell pwd):/app \
				--env APP_HOST=${APP_HOST} \
				--env APP_PORT=${APP_PORT} \
				--env POSTGRES_USER=username \
				--env POSTGRES_PASS=password \
				--env POSTGRES_DBNAME=postgis \
				--env POSTGRES_HOST_READER=host.docker.internal \
				--env POSTGRES_HOST_WRITER=host.docker.internal \
				--env POSTGRES_PORT=5432 \
				--env ENVIRONMENT=development \
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