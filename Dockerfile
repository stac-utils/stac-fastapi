FROM ghcr.io/astral-sh/uv:python3.14-bookworm-slim

WORKDIR /app

RUN apt-get update && apt-get install -y gcc
COPY . /app

ENV CURL_CA_BUNDLE=/etc/ssl/certs/ca-certificates.crt
ENV UV_COMPILE_BYTECODE=1
ENV UV_LINK_MODE=copy
ENV UV_TOOL_BIN_DIR=/usr/local/bin
RUN --mount=type=cache,target=/root/.cache/uv \
  --mount=type=bind,source=uv.lock,target=uv.lock \
  uv sync --locked --no-dev

ENV PATH="/app/.venv/bin:$PATH"
