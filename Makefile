.PHONY: image
image:
	docker build .

.PHONY: install
install:
	uv sync --dev

.PHONY: test
test: install
	uv run pytest

.PHONY: docs
docs:
	uvx --with-requirements requirements/requirements-docs.txt mkdocs build -f docs/mkdocs.yml

.PHONY: benchmark
benchmark: install
	uv run pytest stac_fastapi/api/tests/benchmarks.py --benchmark-only --benchmark-columns 'min, max, mean, median' 