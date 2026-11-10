# Develop & Contribute

## Prerequisites

We recommend using [`uv`](https://docs.astral.sh/uv) as the project manager for development.

See https://docs.astral.sh/uv/getting-started/installation/ for installation.

## Install & Test

```bash
# Clone the repository
git clone https://github.com/stac-utils/stac-fastapi.git
cd stac-fastapi

# Install dependencies (dev + runtime)
uv sync --dev

# Run tests to confirm everything works
uv run pytest
```

If all tests pass, your environment is ready.

## Local Documentation

`stac-fastapi` uses [MkDocs-Material](https://squidfunk.github.io/mkdocs-material/). Build or serve docs with `uv`.

```bash
# Static build (output → ./site)
uv run --group docs mkdocs build -f docs/mkdocs.yml

# Live‑reload dev server
uv run --group docs mkdocs serve -f docs/mkdocs.yml --livereload
```

??? info "Manual docs deployment"
    If you need to manually deploy docs, run:

    ```bash
    uv run --group docs mkdocs gh-deploy -f docs/mkdocs.yml
    ```

    **Note that** you should never need to do this because GitHub Actions deploys automatically for new commits.

## Create Custom Extensions

STAC FastAPI [embeds many API extensions](./index.md#extensions). But if you need to add deployment-specific routes (e.g., custom analytics, map tiles, or proprietary workflows) to your STAC API, you can build custom extensions without forking or modifying the core repository. 

The framework is designed to seamlessly mount external routes alongside the standard endpoints and include them in the OpenAPI schema.

### 1. Define the Extension

Create a class that inherits from `stac_fastapi.types.extension.ApiExtension` and bind your FastAPI routes inside the `register()` method:

```python
from fastapi import APIRouter
from stac_fastapi.types.extension import ApiExtension

class MyCustomExtension(ApiExtension):
    """Example of a custom out-of-tree extension."""

    def register(self, app):
        router = APIRouter()

        @router.get("/api/custom-route")
        async def my_route():
            return {"message": "Hello from my custom extension!"}

        app.include_router(router)
```

### 2. Inject it into your Backend

Modern `stac-fastapi` backends (such as `pgstac` and `elasticsearch-opensearch`) utilize a factory pattern (`instantiate_api`) that accepts custom extensions. Depending on the backend's implementation, you can typically inject your custom class into the application during startup via an `extra_map` or an `extensions` array.

For a comprehensive, real-world example of wiring routes, models, and dependencies in a standalone extension, see the [Multi-Tenant Catalogs extension](https://github.com/StacLabs/stac-fastapi-catalogs-extension).

## Response Validation

A common question when using this package is how request and response types are validated?

This package uses [`stac-pydantic`](https://github.com/stac-utils/stac-pydantic) to validate and document STAC objects. However, by default, validation of response types is turned off and the API will simply forward responses without validating them against the Pydantic model first. This decision was made with the assumption that responses usually come from a (typed) database and can be considered safe. Extra validation would only increase latency, in particular for large payloads.

To turn on response validation, set `ENABLE_RESPONSE_MODELS` to `True`. Either as an environment variable or directly in the `ApiSettings`.

With the introduction of Pydantic 2, the extra [time it takes to validate models became negatable](https://github.com/stac-utils/stac-fastapi/pull/625#issuecomment-2045824578). While `ENABLE_RESPONSE_MODELS` still defaults to `False` there should be no penalty for users to turn on this feature but users discretion is advised.

## Contributing

Contributions are welcome! Feel free to [open an issue](https://github.com/stac-utils/stac-fastapi/issues) in order to discuss changes before offering a Pull Request.

### Setting up pre‑commit locally

This repo is set to use `pre-commit` to run *ruff*, *pydocstring* and *mypy* when committing new code.

```bash
# Install the Git hook
uv run pre-commit install

# Run all checks manually (optional)
uv run pre-commit run --all-files
```

## Release Process

This is a checklist for releasing a new version of **stac-fastapi**.

1. Merge pull requests with Conventional Commit titles (`fix:`, `feat:`, `feat!:` for breaking changes). [release-please](https://github.com/googleapis/release-please) then opens or updates a `chore(main): release X.Y.Z` PR that bumps the three `version.py` files, `VERSION` and `uv.lock`. To force a version, add a `Release-As: X.Y.Z` footer to a commit merged to `main`.
2. Just before merging that PR, push a commit to it that updates [CHANGES.md](./CHANGES.md): add the header and update the links at the bottom of the file. (release-please rewrites the branch whenever new commits land on `main`.)
3. Audit CHANGES.md for completeness and accuracy. Also, ensure that the changes in this version are appropriate for the version number change (i.e. if you're making breaking changes, you should be increasing the `MAJOR` version number).
4. (optional) If you have permissions, run `scripts/publish --test` to test your PyPI publish. If successful, the published packages will be available on <http://test.pypy.org>.
5. Get approval and merge the release PR. release-please tags `X.Y.Z` and creates the GitHub release, which kicks off the [publishing workflow](.github/workflows/publish.yml).

Releases from maintenance branches stay manual: bump with `uv run --with bump-my-version bump-my-version bump --new-version X.Y.Z` (it also updates `.release-please-manifest.json`), then tag and create the release by hand.
