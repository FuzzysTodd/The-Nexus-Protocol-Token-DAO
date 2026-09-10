import typing as t
from ..http import parse_list_header as parse_list_header
from _typeshed import Incomplete
from _typeshed.wsgi import StartResponse, WSGIApplication as WSGIApplication, WSGIEnvironment as WSGIEnvironment

class ProxyFix:
    """Adjust the WSGI environ based on ``X-Forwarded-`` that proxies in
    front of the application may set.

    -   ``X-Forwarded-For`` sets ``REMOTE_ADDR``.
    -   ``X-Forwarded-Proto`` sets ``wsgi.url_scheme``.
    -   ``X-Forwarded-Host`` sets ``HTTP_HOST``, ``SERVER_NAME``, and
        ``SERVER_PORT``.
    -   ``X-Forwarded-Port`` sets ``HTTP_HOST`` and ``SERVER_PORT``.
    -   ``X-Forwarded-Prefix`` sets ``SCRIPT_NAME``.

    You must tell the middleware how many proxies set each header so it
    knows what values to trust. It is a security issue to trust values
    that came from the client rather than a proxy.

    The original values of the headers are stored in the WSGI
    environ as ``werkzeug.proxy_fix.orig``, a dict.

    :param app: The WSGI application to wrap.
    :param x_for: Number of values to trust for ``X-Forwarded-For``.
    :param x_proto: Number of values to trust for ``X-Forwarded-Proto``.
    :param x_host: Number of values to trust for ``X-Forwarded-Host``.
    :param x_port: Number of values to trust for ``X-Forwarded-Port``.
    :param x_prefix: Number of values to trust for
        ``X-Forwarded-Prefix``.

    .. code-block:: python

        from werkzeug.middleware.proxy_fix import ProxyFix
        # App is behind one proxy that sets the -For and -Host headers.
        app = ProxyFix(app, x_for=1, x_host=1)

    .. versionchanged:: 1.0
        The ``num_proxies`` argument and attribute; the ``get_remote_addr`` method; and
        the environ keys ``orig_remote_addr``, ``orig_wsgi_url_scheme``, and
        ``orig_http_host`` were removed.

    .. versionchanged:: 0.15
        All headers support multiple values. Each header is configured with a separate
        number of trusted proxies.

    .. versionchanged:: 0.15
        Original WSGI environ values are stored in the ``werkzeug.proxy_fix.orig`` dict.

    .. versionchanged:: 0.15
        Support ``X-Forwarded-Port`` and ``X-Forwarded-Prefix``.

    .. versionchanged:: 0.15
        ``X-Forwarded-Host`` and ``X-Forwarded-Port`` modify
        ``SERVER_NAME`` and ``SERVER_PORT``.
    """
    app: Incomplete
    x_for: Incomplete
    x_proto: Incomplete
    x_host: Incomplete
    x_port: Incomplete
    x_prefix: Incomplete
    def __init__(self, app: WSGIApplication, x_for: int = 1, x_proto: int = 1, x_host: int = 0, x_port: int = 0, x_prefix: int = 0) -> None: ...
    def __call__(self, environ: WSGIEnvironment, start_response: StartResponse) -> t.Iterable[bytes]:
        """Modify the WSGI environ based on the various ``Forwarded``
        headers before calling the wrapped application. Store the
        original environ values in ``werkzeug.proxy_fix.orig_{key}``.
        """
