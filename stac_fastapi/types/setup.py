"""stac_fastapi: types module."""

from setuptools import find_namespace_packages, setup

with open("README.md") as f:
    desc = f.read()

install_requires = [
    # We need to pin fastapi for the openapi schema
    # See https://github.com/stac-utils/stac-fastapi/issues/242
    "fastapi==0.67.*",
    "attrs",
    "pydantic[dotenv]",
    "stac_pydantic==2.0.*",
]

extra_reqs = {
    "dev": [
        "pytest",
        "pytest-cov",
        "pytest-asyncio",
        "pre-commit",
        "requests",
    ],
    "docs": ["mkdocs", "mkdocs-material", "pdocs"],
}


setup(
    name="stac-fastapi.types",
    description="An implementation of STAC API based on the FastAPI framework.",
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
