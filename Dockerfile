FROM python:3.8-slim

# Any python libraries that require system libraries to be installed will likely
# need the following packages in order to build
RUN apt-get update && apt-get install -y build-essential git libgeos-dev

RUN pip install pipenv
ENV PIPENV_NOSPIN=true
ENV PIPENV_HIDE_EMOJIS=true
ENV CURL_CA_BUNDLE=/etc/ssl/certs/ca-certificates.crt

ARG install_dev_dependencies=true

WORKDIR /app

COPY Pipfile Pipfile.lock setup.py ./
RUN pipenv install --deploy --ignore-pipfile ${install_dev_dependencies:+--dev}

COPY . ./

ENV APP_HOST=0.0.0.0
ENV APP_PORT=80
ENV RELOAD="true"

ENTRYPOINT ["pipenv", "run"]
CMD if [ "$RELOAD" ]; then uvicorn stac_api.app:app --host=${APP_HOST} --port=${APP_PORT} --reload ; \
    else gunicorn stac_api.app:app --preload -k uvicorn.workers.UvicornWorker --bind ${APP_HOST}:${APP_PORT} --log-level info; fi