.PHONY: image
image:
	docker build .

.PHONY: install
install:
	uv sync --all-extras

.PHONY: test
test: install
	uv run pytest

.PHONY: docs
docs: install
	uv run pip install -r requirements/requirements-docs.txt && \
	uv run mkdocs build -f docs/mkdocs.yml

.PHONY: benchmark
benchmark: install
	uv run pytest stac_fastapi/api/tests/benchmarks.py --benchmark-only --benchmark-columns 'min, max, mean, median' 