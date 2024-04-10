.PHONY: image
image:
	docker build .

.PHONY: install
install:
	python -m pip install wheel && \
	python -m pip install -e ./stac_fastapi/types[dev] && \
	python -m pip install -e ./stac_fastapi/api[dev] && \
	python -m pip install -e ./stac_fastapi/extensions[dev]

.PHONY: docs-image
docs-image:
	docker-compose -f docker-compose.docs.yml \
		build

.PHONY: docs
docs: docs-image
	docker-compose -f docker-compose.docs.yml \
		run docs

.PHONY: test
test: image
	python -m pytest .
