import typing as t
from ..exceptions import SecurityError as SecurityError
from ..urls import uri_to_iri as uri_to_iri

def host_is_trusted(hostname: str, trusted_list: t.Iterable[str]) -> bool:
    """Check if a host matches a list of trusted names.

    :param hostname: The name to check.
    :param trusted_list: A list of valid names to match. If a name
        starts with a dot it will match all subdomains.

    .. versionadded:: 0.9
    """
def get_host(scheme: str, host_header: str | None, server: tuple[str, int | None] | None = None, trusted_hosts: t.Iterable[str] | None = None) -> str:
    '''Return the host for the given parameters.

    This first checks the ``host_header``. If it\'s not present, then
    ``server`` is used. The host will only contain the port if it is
    different than the standard port for the protocol.

    Optionally, verify that the host is trusted using
    :func:`host_is_trusted` and raise a
    :exc:`~werkzeug.exceptions.SecurityError` if it is not.

    :param scheme: The protocol the request used, like ``"https"``.
    :param host_header: The ``Host`` header value.
    :param server: Address of the server. ``(host, port)``, or
        ``(path, None)`` for unix sockets.
    :param trusted_hosts: A list of trusted host names.

    :return: Host, with port if necessary.
    :raise ~werkzeug.exceptions.SecurityError: If the host is not
        trusted.
    '''
def get_current_url(scheme: str, host: str, root_path: str | None = None, path: str | None = None, query_string: bytes | None = None) -> str:
    '''Recreate the URL for a request. If an optional part isn\'t
    provided, it and subsequent parts are not included in the URL.

    The URL is an IRI, not a URI, so it may contain Unicode characters.
    Use :func:`~werkzeug.urls.iri_to_uri` to convert it to ASCII.

    :param scheme: The protocol the request used, like ``"https"``.
    :param host: The host the request was made to. See :func:`get_host`.
    :param root_path: Prefix that the application is mounted under. This
        is prepended to ``path``.
    :param path: The path part of the URL after ``root_path``.
    :param query_string: The portion of the URL after the "?".
    '''
def get_content_length(http_content_length: str | None = None, http_transfer_encoding: str | None = None) -> int | None:
    """Return the ``Content-Length`` header value as an int. If the header is not given
    or the ``Transfer-Encoding`` header is ``chunked``, ``None`` is returned to indicate
    a streaming request. If the value is not an integer, or negative, 0 is returned.

    :param http_content_length: The Content-Length HTTP header.
    :param http_transfer_encoding: The Transfer-Encoding HTTP header.

    .. versionadded:: 2.2
    """
