#!make
APP_HOST ?= 0.0.0.0
APP_PORT ?= 8080
EXTERNAL_APP_PORT ?= ${APP_PORT}
run_sqlalchemy = docker-compose run --rm \
				-p ${EXTERNAL_APP_PORT}:${APP_PORT} \
				-e APP_HOST=${APP_HOST} \
				-e APP_PORT=${APP_PORT} \
				app-sqlalchemy

run_pgstac = docker-compose run --rm \
				-p ${EXTERNAL_APP_PORT}:${APP_PORT} \
				-e APP_HOST=${APP_HOST} \
				-e APP_PORT=${APP_PORT} \
				app-pgstac

.PHONY: image
image:
	docker-compose build

.PHONY: docker-run-all
docker-run-all:
	docker-compose up

.PHONY: docker-run-sqlalchemy
docker-run-sqlalchemy: image
	$(run_sqlalchemy)

.PHONY: docker-run-pgstac
docker-run-pgstac: image
	$(run_pgstac)

.PHONY: docker-run-nginx-proxy
docker-run-nginx-proxy:
	docker-compose -f docker-compose.yml -f docker-compose.nginx.yml up

.PHONY: docker-shell-sqlalchemy
docker-shell-sqlalchemy:
	$(run_sqlalchemy) /bin/bash

.PHONY: docker-shell-pgstac
docker-shell-pgstac:
	$(run_pgstac) /bin/bash

.PHONY: test-sqlalchemy
test-sqlalchemy: run-joplin-sqlalchemy
	$(run_sqlalchemy) /bin/bash -c 'export && ./scripts/wait-for-it.sh database:5432 && cd /app/stac_fastapi/sqlalchemy/tests/ && pytest -vvv'

.PHONY: test-pgstac
test-pgstac:
	$(run_pgstac) /bin/bash -c 'export && ./scripts/wait-for-it.sh database:5432 && cd /app/stac_fastapi/pgstac/tests/ && pytest -vvv'

.PHONY: test-api
test-api:
	$(run_sqlalchemy) /bin/bash -c 'cd /app/stac_fastapi/api && pytest -svvv'

.PHONY: run-database
run-database:
	docker-compose run --rm database

.PHONY: run-joplin-sqlalchemy
run-joplin-sqlalchemy:
	docker-compose run --rm loadjoplin-sqlalchemy

.PHONY: run-joplin-pgstac
run-joplin-pgstac:
	docker-compose run --rm loadjoplin-pgstac

.PHONY: test
test: test-sqlalchemy test-pgstac

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

.PHONY: docs-image
docs-image:
	docker-compose -f docker-compose.docs.yml \
		build

.PHONY: docs
docs: docs-image
	docker-compose -f docker-compose.docs.yml \
		run docs
