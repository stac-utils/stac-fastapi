#!make
.PHONY: image
image:
	docker-compose build

.PHONY: test
test: image
	docker-compose run test

.PHONY: docs
docs: image
	docker-compose run docs
