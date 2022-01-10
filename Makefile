#!make
APP_HOST ?= 0.0.0.0
APP_PORT ?= 8080
EXTERNAL_APP_PORT ?= ${APP_PORT}
run_docker = docker-compose run --rm \
				-p ${EXTERNAL_APP_PORT}:${APP_PORT} \
				-e APP_HOST=${APP_HOST} \
				-e APP_PORT=${APP_PORT} \
				app-sqlalchemy

run_pgstac = docker-compose run --rm \
				-p ${EXTERNAL_APP_PORT}:${APP_PORT} \
				-e APP_HOST=${APP_HOST} \
				-e APP_PORT=${APP_PORT} \
				app-pgstac

run_mongo = docker-compose -f docker-compose.mongo.yml \
				run \
				-p ${EXTERNAL_APP_PORT}:${APP_PORT} \
				-e PY_IGNORE_IMPORTMISMATCH=1 \
				-e APP_HOST=${APP_HOST} \
				-e APP_PORT=${APP_PORT} \
				app-mongo

.PHONY: image
image:
	docker-compose build

.PHONY: mongo-image
mongo-image:
	docker-compose -f docker-compose.mongo.yml build

.PHONY: docker-run
docker-run: image
	$(run_docker)

.PHONY: docker-run-pgstac
docker-run-pgstac: image
	$(run_pgstac)

.PHONY: docker-run-mongo
docker-run-mongo: mongo-image
	$(run_mongo)

.PHONY: docker-shell
docker-shell:
	$(run_docker) /bin/bash

.PHONY: docker-shell-pgstac
docker-shell-pgstac:
	$(run_pgstac) /bin/bash

.PHONY: docker-shell-mongo
docker-shell-mongo:
	$(run_mongo) /bin/bash

.PHONY: test-sqlalchemy
test-sqlalchemy: run-joplin-sqlalchemy
	$(run_docker) /bin/bash -c 'export && ./scripts/wait-for-it.sh database:5432 && cd /app/stac_fastapi/sqlalchemy/tests/ && pytest'

.PHONY: test-pgstac
test-pgstac:
	$(run_pgstac) /bin/bash -c 'export && ./scripts/wait-for-it.sh database:5432 && cd /app/stac_fastapi/pgstac/tests/ && pytest'

.PHONY: test-mongo
test-mongo:
	$(run_mongo) /bin/bash -c 'export && cd /app/stac_fastapi/mongo/tests/ && pytest'

.PHONY: run-database
run-database:
	docker-compose run --rm database

.PHONY: run-mongo-database
run-mongo-database:
	docker-compose -f docker-compose.mongo.yml run --rm mongo_db

.PHONY: run-joplin-sqlalchemy
run-joplin-sqlalchemy:
	docker-compose run --rm loadjoplin-sqlalchemy

.PHONY: run-joplin-pgstac
run-joplin-pgstac:
	docker-compose run --rm loadjoplin-pgstac

.PHONY: test
test: test-sqlalchemy test-pgstac test-mongo

.PHONY: pybase-install
pybase-install:
	pip install wheel && \
	pip install -e ./stac_fastapi/api[dev] && \
	pip install -e ./stac_fastapi/types[dev] && \
	pip install -e ./stac_fastapi/extensions[dev]

.PHONY: pgstac-install
pgstac-install: pybase-install
	pip install -e ./stac_fastapi/pgstac[dev,server]

.PHONY: sqlalchemy-install
sqlalchemy-install: pybase-install
	pip install -e ./stac_fastapi/sqlalchemy[dev,server]

.PHONY: mongo-install
mongo-install: pybase-install
	pip install -e ./stac_fastapi/mongo[dev,server]

.PHONY: docs-image
docs-image:
	docker-compose -f docker-compose.docs.yml \
		build

.PHONY: docs
docs: docs-image
	docker-compose -f docker-compose.docs.yml \
		run docs
