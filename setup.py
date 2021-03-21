"""arturo-stac-api."""

from setuptools import find_packages, setup

with open("README.md") as f:
    desc = f.read()


install_requires = [
    "stac-fastapi-api",
    "stac-fastapi-extensions"
]

extra_reqs = {
    "postgres": ["stac-fastapi-postgres"],
    "dev": ["pytest", "pytest-cov", "pytest-asyncio", "pre-commit", "requests"],
    "docs": ["mkdocs", "mkdocs-material"],
}


setup(
    name="stac-fastapi",
    description="An implementation of STAC API based on the FastAPI framework.",
    long_description=desc,
    long_description_content_type="text/markdown",
    version="1.1.0",
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
    packages=find_packages(exclude=["alembic", "tests", "scripts"]),
    zip_safe=False,
    install_requires=install_requires,
    tests_require=extra_reqs["dev"],
    extras_require=extra_reqs,
)
