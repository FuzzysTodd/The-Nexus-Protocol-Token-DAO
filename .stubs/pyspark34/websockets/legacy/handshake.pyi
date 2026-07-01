from ..datastructures import Headers

__all__ = ['build_request', 'check_request', 'build_response', 'check_response']

def build_request(headers: Headers) -> str:
    """
    Build a handshake request to send to the server.

    Update request headers passed in argument.

    Args:
        headers: Handshake request headers.

    Returns:
        str: ``key`` that must be passed to :func:`check_response`.

    """
def check_request(headers: Headers) -> str:
    """
    Check a handshake request received from the client.

    This function doesn't verify that the request is an HTTP/1.1 or higher GET
    request and doesn't perform ``Host`` and ``Origin`` checks. These controls
    are usually performed earlier in the HTTP request handling code. They're
    the responsibility of the caller.

    Args:
        headers: Handshake request headers.

    Returns:
        str: ``key`` that must be passed to :func:`build_response`.

    Raises:
        InvalidHandshake: If the handshake request is invalid.
            Then, the server must return a 400 Bad Request error.

    """
def build_response(headers: Headers, key: str) -> None:
    """
    Build a handshake response to send to the client.

    Update response headers passed in argument.

    Args:
        headers: Handshake response headers.
        key: Returned by :func:`check_request`.

    """
def check_response(headers: Headers, key: str) -> None:
    """
    Check a handshake response received from the server.

    This function doesn't verify that the response is an HTTP/1.1 or higher
    response with a 101 status code. These controls are the responsibility of
    the caller.

    Args:
        headers: Handshake response headers.
        key: Returned by :func:`build_request`.

    Raises:
        InvalidHandshake: If the handshake response is invalid.

    """
