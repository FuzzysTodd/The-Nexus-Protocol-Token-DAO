import asyncio
from ..datastructures import Headers
from typing import Tuple

__all__ = ['read_request', 'read_response']

async def read_request(stream: asyncio.StreamReader) -> Tuple[str, Headers]:
    """
    Read an HTTP/1.1 GET request and return ``(path, headers)``.

    ``path`` isn't URL-decoded or validated in any way.

    ``path`` and ``headers`` are expected to contain only ASCII characters.
    Other characters are represented with surrogate escapes.

    :func:`read_request` doesn't attempt to read the request body because
    WebSocket handshake requests don't have one. If the request contains a
    body, it may be read from ``stream`` after this coroutine returns.

    Args:
        stream: Input to read the request from.

    Raises:
        EOFError: If the connection is closed without a full HTTP request.
        SecurityError: If the request exceeds a security limit.
        ValueError: If the request isn't well formatted.

    """
async def read_response(stream: asyncio.StreamReader) -> Tuple[int, str, Headers]:
    """
    Read an HTTP/1.1 response and return ``(status_code, reason, headers)``.

    ``reason`` and ``headers`` are expected to contain only ASCII characters.
    Other characters are represented with surrogate escapes.

    :func:`read_request` doesn't attempt to read the response body because
    WebSocket handshake responses don't have one. If the response contains a
    body, it may be read from ``stream`` after this coroutine returns.

    Args:
        stream: Input to read the response from.

    Raises:
        EOFError: If the connection is closed without a full HTTP response.
        SecurityError: If the response exceeds a security limit.
        ValueError: If the response isn't well formatted.

    """
