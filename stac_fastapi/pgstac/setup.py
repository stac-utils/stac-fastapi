"""arturo-stac-api."""
import os
from imp import load_source

from setuptools import find_namespace_packages, setup

with open("README.md") as f:
    desc = f.read()

# Get version from stac-fastapi-api
__version__ = load_source(
    "stac_fastapi.pgstac.version",
    os.path.join(os.path.dirname(__file__), "stac_fastapi/pgstac/version.py"),
).__version__  # type:ignore

install_requires = [
    "fastapi",
    "attrs",
    "orjson",
    "pydantic[dotenv]",
    "stac_pydantic==2.0.0",
    "stac-fastapi.types",
    "stac-fastapi.api",
    "stac-fastapi.extensions",
    "asyncpg",
    "buildpg",
    "shapely",
    "brotli_asgi",
]

extra_reqs = {
    "dev": [
        "pytest",
        "pytest-cov",
        "pytest-asyncio",
        "pre-commit",
        "requests",
        "pypgstac==0.2.7",
        "httpx",
    ],
    "docs": ["mkdocs", "mkdocs-material", "pdocs"],
    "server": ["uvicorn[standard]>=0.12.0,<0.14.0"],
    "awslambda": ["mangum"],
}


setup(
    name="stac-fastapi.pgstac",
    description="An implementation of STAC API based on the FastAPI framework and using the pgstac backend.",
    long_description=desc,
    long_description_content_type="text/markdown",
    version=__version__,
    python_requires=">=3.8",
    classifiers=[
        "Intended Audience :: Developers",
        "Intended Audience :: Information Technology",
        "Intended Audience :: Science/Research",
        "Programming Language :: Python :: 3.8",
        "License :: OSI Approved :: MIT License",
    ],
    keywords="STAC FastAPI COG",
    author=u"David Bitner",
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
