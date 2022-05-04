"""stac_fastapi: pgstac module."""

from setuptools import find_namespace_packages, setup

with open("README.md") as f:
    desc = f.read()

install_requires = [
    "attrs",
    "orjson",
    "pydantic[dotenv]",
    "stac_pydantic==2.0.*",
    "stac-fastapi.types",
    "stac-fastapi.api",
    "stac-fastapi.extensions",
    "psycopg[binary]",
    "asyncpg",
    "buildpg",
    "brotli_asgi",
    "pygeofilter @ git+https://github.com/geopython/pygeofilter@v0.1.1#egg=pygeofilter",
    # TODO: "pypgstac==0.5.2",
    "pypgstac @ git+https://github.com/stac-utils/pgstac@dc11b66539aac5aa37b81fb09b23b79a185a29d7#egg=pypgstac&subdirectory=pypgstac",
]

extra_reqs = {
    "dev": [
        # TODO: replace with pypgstac[psycopg] after pypgstac is published
        "psycopg[binary]==3.0.*",
        "psycopg-pool==3.1.*",
        # ====
        "pytest",
        "pytest-cov",
        "pytest-asyncio>=0.17",
        "pre-commit",
        "requests",
        "httpx",
    ],
    "docs": ["mkdocs", "mkdocs-material", "pdocs"],
    "server": ["uvicorn[standard]==0.17.0"],
    "awslambda": ["mangum"],
}


setup(
    name="stac-fastapi.pgstac",
    description="An implementation of STAC API based on the FastAPI framework and using the pgstac backend.",
    long_description=desc,
    long_description_content_type="text/markdown",
    python_requires=">=3.8",
    classifiers=[
        "Intended Audience :: Developers",
        "Intended Audience :: Information Technology",
        "Intended Audience :: Science/Research",
        "Programming Language :: Python :: 3.8",
        "License :: OSI Approved :: MIT License",
    ],
    keywords="STAC FastAPI COG",
    author="David Bitner",
    author_email="david@developmentseed.org",
    url="https://github.com/stac-utils/stac-fastapi",
    license="MIT",
    packages=find_namespace_packages(exclude=["alembic", "tests", "scripts"]),
    zip_safe=False,
    install_requires=install_requires,
    tests_require=extra_reqs["dev"],
    extras_require=extra_reqs,
    entry_points={
        "console_scripts": ["stac-fastapi-pgstac=stac_fastapi.pgstac.app:run"]
    },
)
