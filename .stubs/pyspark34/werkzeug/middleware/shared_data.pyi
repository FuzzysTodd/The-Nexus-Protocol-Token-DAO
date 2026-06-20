import typing as t
from ..http import http_date as http_date, is_resource_modified as is_resource_modified
from ..security import safe_join as safe_join
from ..utils import get_content_type as get_content_type
from ..wsgi import get_path_info as get_path_info, wrap_file as wrap_file
from _typeshed import Incomplete
from _typeshed.wsgi import StartResponse, WSGIApplication as WSGIApplication, WSGIEnvironment as WSGIEnvironment
from datetime import datetime

class SharedDataMiddleware:
    """A WSGI middleware which provides static content for development
    environments or simple server setups. Its usage is quite simple::

        import os
        from werkzeug.middleware.shared_data import SharedDataMiddleware

        app = SharedDataMiddleware(app, {
            '/shared': os.path.join(os.path.dirname(__file__), 'shared')
        })

    The contents of the folder ``./shared`` will now be available on
    ``http://example.com/shared/``.  This is pretty useful during development
    because a standalone media server is not required. Files can also be
    mounted on the root folder and still continue to use the application because
    the shared data middleware forwards all unhandled requests to the
    application, even if the requests are below one of the shared folders.

    If `pkg_resources` is available you can also tell the middleware to serve
    files from package data::

        app = SharedDataMiddleware(app, {
            '/static': ('myapplication', 'static')
        })

    This will then serve the ``static`` folder in the `myapplication`
    Python package.

    The optional `disallow` parameter can be a list of :func:`~fnmatch.fnmatch`
    rules for files that are not accessible from the web.  If `cache` is set to
    `False` no caching headers are sent.

    Currently the middleware does not support non-ASCII filenames. If the
    encoding on the file system happens to match the encoding of the URI it may
    work but this could also be by accident. We strongly suggest using ASCII
    only file names for static files.

    The middleware will guess the mimetype using the Python `mimetype`
    module.  If it's unable to figure out the charset it will fall back
    to `fallback_mimetype`.

    :param app: the application to wrap.  If you don't want to wrap an
                application you can pass it :exc:`NotFound`.
    :param exports: a list or dict of exported files and folders.
    :param disallow: a list of :func:`~fnmatch.fnmatch` rules.
    :param cache: enable or disable caching headers.
    :param cache_timeout: the cache timeout in seconds for the headers.
    :param fallback_mimetype: The fallback mimetype for unknown files.

    .. versionchanged:: 1.0
        The default ``fallback_mimetype`` is
        ``application/octet-stream``. If a filename looks like a text
        mimetype, the ``utf-8`` charset is added to it.

    .. versionadded:: 0.6
        Added ``fallback_mimetype``.

    .. versionchanged:: 0.5
        Added ``cache_timeout``.
    """
    app: Incomplete
    exports: Incomplete
    cache: Incomplete
    cache_timeout: Incomplete
    fallback_mimetype: Incomplete
    def __init__(self, app: WSGIApplication, exports: dict[str, str | tuple[str, str]] | t.Iterable[tuple[str, str | tuple[str, str]]], disallow: None = None, cache: bool = True, cache_timeout: int = ..., fallback_mimetype: str = 'application/octet-stream') -> None: ...
    def is_allowed(self, filename: str) -> bool:
        """Subclasses can override this method to disallow the access to
        certain files.  However by providing `disallow` in the constructor
        this method is overwritten.
        """
    def get_file_loader(self, filename: str) -> _TLoader: ...
    def get_package_loader(self, package: str, package_path: str) -> _TLoader: ...
    def get_directory_loader(self, directory: str) -> _TLoader: ...
    def generate_etag(self, mtime: datetime, file_size: int, real_filename: str) -> str: ...
    def __call__(self, environ: WSGIEnvironment, start_response: StartResponse) -> t.Iterable[bytes]: ...
