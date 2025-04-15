FROM python:3.12-slim AS base

# Any python libraries that require system libraries to be installed will likely
# need the following packages in order to build
RUN apt-get update && \
    apt-get -y upgrade && \
    apt-get install -y build-essential git && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

ENV CURL_CA_BUNDLE=/etc/ssl/certs/ca-certificates.crt

FROM base AS builder

WORKDIR /app

COPY . /app

RUN python -m pip install \
    -e ./stac_fastapi/types[dev] \
    -e ./stac_fastapi/api[dev] \
    -e ./stac_fastapi/extensions[dev]
