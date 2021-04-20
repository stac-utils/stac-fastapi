"""arturo-stac-api."""
import os
from imp import load_source

from setuptools import find_namespace_packages, setup

with open("README.md") as f:
    desc = f.read()

# Get version from stac-fastapi-api
__version__ = load_source(
    "stac_fastapi.sqlalchemy.version",
    os.path.join(os.path.dirname(__file__), "stac_fastapi/sqlalchemy/version.py"),
).__version__  # type:ignore

install_requires = [
    "fastapi",
    "attrs",
    "pydantic[dotenv]",
    "stac_pydantic==1.3.8",
    "stac-fastapi.types",
    "stac-fastapi.api",
    "stac-fastapi.extensions",
    "sqlakeyset",
    "geoalchemy2<0.8.0",
    "sqlalchemy==1.3.23",
    "shapely",
    "psycopg2-binary",
    "alembic",
    "fastapi-utils",
]

extra_reqs = {
    "dev": ["pytest", "pytest-cov", "pytest-asyncio", "pre-commit", "requests"],
    "docs": ["mkdocs", "mkdocs-material", "pdocs"],
    "server": ["uvicorn[standard]>=0.12.0,<0.14.0"],
}


setup(
    name="stac-fastapi.sqlalchemy",
    description="An implementation of STAC API based on the FastAPI framework.",
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
    author=u"Arturo Engineering",
    author_email="engineering@arturo.ai",
    url="https://github.com/stac-utils/stac-fastapi",
    license="MIT",
    packages=find_namespace_packages(exclude=["alembic", "tests", "scripts"]),
    zip_safe=False,
    install_requires=install_requires,
    tests_require=extra_reqs["dev"],
    extras_require=extra_reqs,
)
