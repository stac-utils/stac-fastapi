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
    "asyncpg",
    "buildpg",
    "brotli_asgi",
    "pygeofilter>=0.2",
    "pypgstac==0.7.*",
]

extra_reqs = {
    "dev": [
        "pypgstac[psycopg]==0.7.*",
        "pytest",
        "pytest-cov",
        "pytest-asyncio>=0.17",
        "pre-commit",
        "requests",
        "httpx",
    ],
    "docs": ["mkdocs", "mkdocs-material", "pdocs"],
    "server": ["uvicorn[standard]==0.19.0"],
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
