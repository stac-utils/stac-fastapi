FROM python:3.8-slim

# Any python libraries that require system libraries to be installed will likely
# need the following packages in order to build
RUN apt-get update && apt-get install -y build-essential git

ENV CURL_CA_BUNDLE=/etc/ssl/certs/ca-certificates.crt

ARG install_dev_dependencies=true

WORKDIR /app

# Install stac_fastapi.types
COPY . /app

RUN pip install -e .[dev,sqlalchemy,tiles] uvicorn

ENV APP_HOST=0.0.0.0
ENV APP_PORT=80
ENV RELOAD="true"

CMD if [ "$RELOAD" ]; then uvicorn stac_fastapi.server.app:app --host=${APP_HOST} --port=${APP_PORT} --reload ; \
    else gunicorn stac_fastapi.server.app:app --preload -k uvicorn.workers.UvicornWorker --bind ${APP_HOST}:${APP_PORT} --log-level info; fi