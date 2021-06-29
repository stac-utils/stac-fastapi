FROM python:3.8-slim as base

FROM base as builder
# Any python libraries that require system libraries to be installed will likely
# need the following packages in order to build
RUN apt-get update && apt-get install -y build-essential git

ENV CURL_CA_BUNDLE=/etc/ssl/certs/ca-certificates.crt

ARG install_dev_dependencies=true

WORKDIR /app

# Install stac_fastapi.types
COPY . /app

ENV PATH=$PATH:/install/bin

RUN mkdir -p /install && \
    pip install -e ./stac_fastapi/api[dev]   && \
    pip install -e ./stac_fastapi/types[dev]  && \
    pip install -e ./stac_fastapi/extensions[dev,tiles]  && \
    pip install -e ./stac_fastapi/sqlalchemy[dev,server] && \
    pip install -e ./stac_fastapi/pgstac[dev,server]
