#!make
include .env.db.local
export $(shell sed 's/=.*//' .env.db.local)
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

run_docker_test = docker run -it --rm \
				-p ${EXTERNAL_APP_PORT}:${APP_PORT} \
				-v $(shell pwd):/app \
				--env-file .env.test \
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

.PHONY: docker-run
docker-run: image
	$(run_docker)

.PHONY: test
test: image
	$(run_docker_test) pytest

.PHONY: database
database:
	docker volume create pg_data
	docker run \
		-d \
		-p 5432:5432 \
		-v pg_data:/var/lib/postgresql \
		-e ALLOW_IP_RANGE=0.0.0.0/0 \
		--name=postgis \
		--env-file .env.db.local \
		kartoza/postgis:latest
	sleep 10
	alembic upgrade head

.PHONY: cleanup
cleanup:
	docker stop postgis && docker rm postgis && docker volume rm pg_data