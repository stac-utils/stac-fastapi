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
    pip install -e ./stac_fastapi/sqlalchemy[dev,server]

# FROM base
# COPY --from=builder /install /usr/local

WORKDIR /app/stac_fastapi/sqlalchemy
ENV APP_HOST=0.0.0.0
ENV APP_PORT=80
ENV RELOAD="true"

CMD if [ "$RELOAD" ]; then uvicorn stac_fastapi.sqlalchemy.app:app --host=${APP_HOST} --port=${APP_PORT} --reload ; \
    else gunicorn stac_fastapi.sqlalchemy.app:app --preload -k uvicorn.workers.UvicornWorker --bind ${APP_HOST}:${APP_PORT} --log-level info; fi