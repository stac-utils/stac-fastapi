"""Functionality to assist link construction."""

import re
from http.client import HTTP_PORT, HTTPS_PORT
from urllib.parse import urljoin

from starlette.requests import Request


def get_base_url_from_request(request: Request) -> str:
    """
    Account for forwarding headers when deriving base URL.

    Prioritise standard Forwarded header, look for non-standard X-Forwarded-* if missing.
    Default to what can be derived from the URL if no headers provided.
    """
    if not isinstance(request, Request):
        # Lots of tests execute setup logic with MockStarletteRequest
        # and this type only has a single property: base_url.
        return request.base_url
    domain = request.url.hostname
    proto = request.url.scheme
    port_str = str(request.url.port) if request.url.port is not None else None
    forwarded = request.headers.get("forwarded")
    if forwarded is not None:
        parts = forwarded.split(";")
        for part in parts:
            if len(part) > 0 and re.search("=", part):
                key, value = part.split("=")
                if key == "proto":
                    proto = value
                elif key == "host":
                    host_parts = value.split(":")
                    domain = host_parts[0]
                    port_str = host_parts[1] if len(host_parts) == 2 else None
    else:
        proto = request.headers.get("x-forwarded-proto", proto)
        port_str = request.headers.get("x-forwarded-port", port_str)
    port_suffix = ""
    if port_str is not None and port_str.isdigit():
        if (proto == "http" and port_str == str(HTTP_PORT)) or (
            proto == "https" and port_str == str(HTTPS_PORT)
        ):
            pass
        else:
            port_suffix = f":{port_str}"
    # ensure url ends with slash
    url = re.sub(
        r"([^/])$",
        r"\1/",
        urljoin(
            f"{proto}://{domain}{port_suffix}",
            # ensure root path starts with slash
            re.sub(r"^([^/])", r"/\1", request.scope.get("root_path")),
        ),
    )
    return url
