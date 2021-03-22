"""stac-fastapi api submodule."""
import os
from imp import load_source

from setuptools import find_namespace_packages, setup

name = "stac-fastapi-server"
description = "Standalone FastAPI server to serve stac-fastapi, a STAC compliant API layer build with FastAPI."

__version__ = load_source(
    "stac_fastapi.server.version",
    os.path.join(os.path.dirname(__file__), "stac_fastapi/server/version.py"),
).__version__  # type:ignore

install_requires = [
    "stac-fastapi-api",
    "stac-fastapi-postgres",
]

with open(
    os.path.join(os.path.abspath(os.path.dirname(__file__)), "README.md")
) as readme_file:
    readme = readme_file.read()

setup(
    name=name,
    python_requires=">=3.8",
    description=description,
    version=__version__,
    long_description=readme,
    long_description_content_type="text/markdown",
    author=u"Arturo Engineering",
    author_email="engineering@arturo.ai",
    url="https://github.com/stac-utils/fastapi-stac.git",
    packages=find_namespace_packages(),
    include_package_data=False,
    install_requires=install_requires,
    license="MIT",
    keywords=["stac", "fastapi", "imagery", "raster", "catalog", "STAC"],
)
