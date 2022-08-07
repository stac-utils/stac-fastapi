#!make
.PHONY: test-api
test:
	pytest -svvv

.PHONY: docs-image
docs-image:
	docker-compose -f docker-compose.docs.yml \
		build

.PHONY: docs
docs: docs-image
	docker-compose -f docker-compose.docs.yml \
		run docs
