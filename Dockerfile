FROM python:3.8-slim

# Any python libraries that require system libraries to be installed will likely
# need the following packages in order to build
RUN apt-get update && apt-get install -y build-essential git

RUN pip install pipenv
ENV PIPENV_NOSPIN=true
ENV PIPENV_HIDE_EMOJIS=true
ENV CURL_CA_BUNDLE=/etc/ssl/certs/ca-certificates.crt

ARG install_dev_dependencies=true

RUN mkdir -p /app

# Install stac_fastapi.types
COPY ./stac_fastapi_types /app/stac_fastapi_types
WORKDIR /app/stac_fastapi_types
RUN pipenv install --deploy --ignore-pipfile ${install_dev_dependencies:+--dev}

# Install stac_api.extensions.
COPY ./stac_fastapi_extensions /app/stac_fastapi_extensions
WORKDIR /app/stac_fastapi_extensions
RUN pipenv install --deploy --ignore-pipfile ${install_dev_dependencies:+--dev}

# Install stac_api.api.
COPY ./stac_fastapi_api /app/stac_fastapi_api
WORKDIR /app/stac_fastapi_api
RUN pipenv install --deploy --ignore-pipfile ${install_dev_dependencies:+--dev}

# Install stac_api.postgres.
COPY ./stac_fastapi_postgres /app/stac_fastapi_postgres
WORKDIR /app/stac_fastapi_postgres
RUN pipenv install --deploy --ignore-pipfile ${install_dev_dependencies:+--dev}

# Install stac_api.server.
COPY ./stac_fastapi_server /app/stac_fastapi_server
WORKDIR /app/stac_fastapi_server
RUN pipenv install --deploy --ignore-pipfile ${install_dev_dependencies:+--dev}

# Install base package
COPY ./setup.py /app/
COPY ./Pipfile /app/
COPY ./Pipfile.lock /app/
WORKDIR /app
RUN pipenv install --deploy --ignore-pipfile ${install_dev_dependencies:+--dev}

ENV APP_HOST=0.0.0.0
ENV APP_PORT=80
ENV RELOAD="true"

ENTRYPOINT ["pipenv", "run"]

CMD if [ "$RELOAD" ]; then uvicorn stac_fastapi.server.app:app --host=${APP_HOST} --port=${APP_PORT} --reload ; \
    else gunicorn stac_fastapi.server.app:app --preload -k uvicorn.workers.UvicornWorker --bind ${APP_HOST}:${APP_PORT} --log-level info; fi