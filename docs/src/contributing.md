# Develop & Contribute

## Prerequisites

We recommand using [`uv`](https://docs.astral.sh/uv) as project manager for development.

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

```python
# Example with pgstac – adjust for your chosen backend
from stac_fastapi.pgstac import instantiate_api

app = instantiate_api(
    database_url="postgresql://...",
    extensions=[MyCustomExtension()]   # or via an `extra_map`
)
```

For a comprehensive, real-world example of wiring routes, models, and dependencies in a standalone extension, see the [Multi-Tenant Catalogs extension](https://github.com/StacLabs/stac-fastapi-catalogs-extension).

## Response Validation

A common question when using this package is how request and response types are validated?

This package uses [`stac-pydantic`](https://github.com/stac-utils/stac-pydantic) to validate and document STAC objects. However, by default, validation of response types is turned off and the API will simply forward responses without validating them against the Pydantic model first. This decision was made with the assumption that responses usually come from a (typed) database and can be considered safe. Extra validation would only increase latency, in particular for large payloads.

To turn on response validation, set `ENABLE_RESPONSE_MODELS` to `True`. Either as an environment variable or directly in the `ApiSettings`.

With the introduction of Pydantic 2, the extra [time it takes to validate models became negatable](https://github.com/stac-utils/stac-fastapi/pull/625#issuecomment-2045824578). While `ENABLE_RESPONSE_MODELS` still defaults to `False` there should be no penalty for users to turn on this feature but users discretion is advised.

## Contributing

Contributions are welcome! Feel free to [open an issue](https://github.com/stac-utils/stac-fastapi/issues) in order to discuss changes before offering a Pull Request.

### Setting up pre‑commit locally

This repo is set to use `pre-commit` to run *ruff*, *pydocstring* and mypy when committing new code.

```bash
# Install the Git hook
uv run pre-commit install

# Run all checks manually (optional)
uv run pre-commit run --all-files
```

## Release Process

This is a checklist for releasing a new version of **stac-fastapi**.

1. Determine the next version. We currently do not have published versioning guidelines, but there is some text on the subject here: <https://github.com/radiantearth/stac-spec/discussions/1184>.
2. Create a release branch named `release/vX.Y.Z`, where `X.Y.Z` is the new version.
3. Search and replace all instances of the current version number with the new version. As of this writing, there's 3 different `version.py` files, and one `VERSION` file, in the repo.

    Note: You can use [`bump-my-version`](https://github.com/callowayproject/bump-my-version) CLI
    ```
    uv run --with bump-my-version bump-my-version bump --new-version 3.1.0
    ```

4. Update [CHANGES.md](./CHANGES.md) for the new version. Add the appropriate header, and update the links at the bottom of the file.
5. Audit CHANGES.md for completeness and accuracy. Also, ensure that the changes in this version are appropriate for the version number change (i.e. if you're making breaking changes, you should be increasing the `MAJOR` version number).
6. (optional) If you have permissions, run `scripts/publish --test` to test your PyPI publish. If successful, the published packages will be available on <http://test.pypy.org>.
7. Push your release branch, create a PR, and get approval.
8. Once the PR is merged, create a new (annotated, signed) tag on the appropriate commit. Name the tag `X.Y.Z`, and include `vX.Y.Z` as its annotation message.
9. Push your tag to Github, which will kick off the [publishing workflow](.github/workflows/publish.yml).
10. Create a [new release](https://github.com/stac-utils/stac-fastapi/releases/new) targeting the new tag, and use the "Generate release notes" feature to populate the description. Publish the release and mark it as the latest.
11. Publicize the release via the appropriate social channels, including [Gitter](https://matrix.to/#/#SpatioTemporal-Asset-Catalog_python:gitter.im).
