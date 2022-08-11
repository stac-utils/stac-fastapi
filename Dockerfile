FROM python:3.8-slim

# build-essential is required to build a wheel for ciso8601
RUN apt update && apt install -y build-essential

RUN python -m pip install --upgrade pip

COPY . /opt/src

WORKDIR /opt/src

RUN python -m pip install .[dev,docs]
