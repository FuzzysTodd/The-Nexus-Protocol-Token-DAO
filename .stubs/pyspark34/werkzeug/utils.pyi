import os
import typing as t
from ._internal import _DictAccessorProperty, _TAccessorValue
from .datastructures import Headers as Headers
from .exceptions import NotFound as NotFound, RequestedRangeNotSatisfiable as RequestedRangeNotSatisfiable
from .security import safe_join as safe_join
from .wrappers.request import Request as Request
from .wrappers.response import Response as Response
from .wsgi import wrap_file as wrap_file
from _typeshed import Incomplete
from _typeshed.wsgi import WSGIEnvironment as WSGIEnvironment
from datetime import datetime

class cached_property(property, t.Generic[_T]):
    """A :func:`property` that is only evaluated once. Subsequent access
    returns the cached value. Setting the property sets the cached
    value. Deleting the property clears the cached value, accessing it
    again will evaluate it again.

    .. code-block:: python

        class Example:
            @cached_property
            def value(self):
                # calculate something important here
                return 42

        e = Example()
        e.value  # evaluates
        e.value  # uses cache
        e.value = 16  # sets cache
        del e.value  # clears cache

    If the class defines ``__slots__``, it must add ``_cache_{name}`` as
    a slot. Alternatively, it can add ``__dict__``, but that's usually
    not desirable.

    .. versionchanged:: 2.1
        Works with ``__slots__``.

    .. versionchanged:: 2.0
        ``del obj.name`` clears the cached value.
    """
    slot_name: Incomplete
    __module__: Incomplete
    def __init__(self, fget: t.Callable[[t.Any], _T], name: str | None = None, doc: str | None = None) -> None: ...
    def __set__(self, obj: object, value: _T) -> None: ...
    def __get__(self, obj: object, type: type = None) -> _T: ...
    def __delete__(self, obj: object) -> None: ...

class environ_property(_DictAccessorProperty[_TAccessorValue]):
    """Maps request attributes to environment variables. This works not only
    for the Werkzeug request object, but also any other class with an
    environ attribute:

    >>> class Test(object):
    ...     environ = {'key': 'value'}
    ...     test = environ_property('key')
    >>> var = Test()
    >>> var.test
    'value'

    If you pass it a second value it's used as default if the key does not
    exist, the third one can be a converter that takes a value and converts
    it.  If it raises :exc:`ValueError` or :exc:`TypeError` the default value
    is used. If no default value is provided `None` is used.

    Per default the property is read only.  You have to explicitly enable it
    by passing ``read_only=False`` to the constructor.
    """
    read_only: bool
    def lookup(self, obj: Request) -> WSGIEnvironment: ...

class header_property(_DictAccessorProperty[_TAccessorValue]):
    """Like `environ_property` but for headers."""
    def lookup(self, obj: Request | Response) -> Headers: ...

def get_content_type(mimetype: str, charset: str) -> str:
    """Returns the full content type string with charset for a mimetype.

    If the mimetype represents text, the charset parameter will be
    appended, otherwise the mimetype is returned unchanged.

    :param mimetype: The mimetype to be used as content type.
    :param charset: The charset to be appended for text mimetypes.
    :return: The content type.

    .. versionchanged:: 0.15
        Any type that ends with ``+xml`` gets a charset, not just those
        that start with ``application/``. Known text types such as
        ``application/javascript`` are also given charsets.
    """
def secure_filename(filename: str) -> str:
    '''Pass it a filename and it will return a secure version of it.  This
    filename can then safely be stored on a regular file system and passed
    to :func:`os.path.join`.  The filename returned is an ASCII only string
    for maximum portability.

    On windows systems the function also makes sure that the file is not
    named after one of the special device files.

    >>> secure_filename("My cool movie.mov")
    \'My_cool_movie.mov\'
    >>> secure_filename("../../../etc/passwd")
    \'etc_passwd\'
    >>> secure_filename(\'i contain cool \\xfcml\\xe4uts.txt\')
    \'i_contain_cool_umlauts.txt\'

    The function might return an empty filename.  It\'s your responsibility
    to ensure that the filename is unique and that you abort or
    generate a random filename if the function returned an empty one.

    .. versionadded:: 0.5

    :param filename: the filename to secure
    '''
def redirect(location: str, code: int = 302, Response: type[Response] | None = None) -> Response:
    """Returns a response object (a WSGI application) that, if called,
    redirects the client to the target location. Supported codes are
    301, 302, 303, 305, 307, and 308. 300 is not supported because
    it's not a real redirect and 304 because it's the answer for a
    request with a request with defined If-Modified-Since headers.

    .. versionadded:: 0.6
       The location can now be a unicode string that is encoded using
       the :func:`iri_to_uri` function.

    .. versionadded:: 0.10
        The class used for the Response object can now be passed in.

    :param location: the location the response should redirect to.
    :param code: the redirect status code. defaults to 302.
    :param class Response: a Response class to use when instantiating a
        response. The default is :class:`werkzeug.wrappers.Response` if
        unspecified.
    """
def append_slash_redirect(environ: WSGIEnvironment, code: int = 308) -> Response:
    """Redirect to the current URL with a slash appended.

    If the current URL is ``/user/42``, the redirect URL will be
    ``42/``. When joined to the current URL during response
    processing or by the browser, this will produce ``/user/42/``.

    The behavior is undefined if the path ends with a slash already. If
    called unconditionally on a URL, it may produce a redirect loop.

    :param environ: Use the path and query from this WSGI environment
        to produce the redirect URL.
    :param code: the status code for the redirect.

    .. versionchanged:: 2.1
        Produce a relative URL that only modifies the last segment.
        Relevant when the current path has multiple segments.

    .. versionchanged:: 2.1
        The default status code is 308 instead of 301. This preserves
        the request method and body.
    """
def send_file(path_or_file: os.PathLike | str | t.IO[bytes], environ: WSGIEnvironment, mimetype: str | None = None, as_attachment: bool = False, download_name: str | None = None, conditional: bool = True, etag: bool | str = True, last_modified: datetime | int | float | None = None, max_age: None | int | t.Callable[[str | None], int | None] = None, use_x_sendfile: bool = False, response_class: type[Response] | None = None, _root_path: os.PathLike | str | None = None) -> Response:
    """Send the contents of a file to the client.

    The first argument can be a file path or a file-like object. Paths
    are preferred in most cases because Werkzeug can manage the file and
    get extra information from the path. Passing a file-like object
    requires that the file is opened in binary mode, and is mostly
    useful when building a file in memory with :class:`io.BytesIO`.

    Never pass file paths provided by a user. The path is assumed to be
    trusted, so a user could craft a path to access a file you didn't
    intend. Use :func:`send_from_directory` to safely serve user-provided paths.

    If the WSGI server sets a ``file_wrapper`` in ``environ``, it is
    used, otherwise Werkzeug's built-in wrapper is used. Alternatively,
    if the HTTP server supports ``X-Sendfile``, ``use_x_sendfile=True``
    will tell the server to send the given path, which is much more
    efficient than reading it in Python.

    :param path_or_file: The path to the file to send, relative to the
        current working directory if a relative path is given.
        Alternatively, a file-like object opened in binary mode. Make
        sure the file pointer is seeked to the start of the data.
    :param environ: The WSGI environ for the current request.
    :param mimetype: The MIME type to send for the file. If not
        provided, it will try to detect it from the file name.
    :param as_attachment: Indicate to a browser that it should offer to
        save the file instead of displaying it.
    :param download_name: The default name browsers will use when saving
        the file. Defaults to the passed file name.
    :param conditional: Enable conditional and range responses based on
        request headers. Requires passing a file path and ``environ``.
    :param etag: Calculate an ETag for the file, which requires passing
        a file path. Can also be a string to use instead.
    :param last_modified: The last modified time to send for the file,
        in seconds. If not provided, it will try to detect it from the
        file path.
    :param max_age: How long the client should cache the file, in
        seconds. If set, ``Cache-Control`` will be ``public``, otherwise
        it will be ``no-cache`` to prefer conditional caching.
    :param use_x_sendfile: Set the ``X-Sendfile`` header to let the
        server to efficiently send the file. Requires support from the
        HTTP server. Requires passing a file path.
    :param response_class: Build the response using this class. Defaults
        to :class:`~werkzeug.wrappers.Response`.
    :param _root_path: Do not use. For internal use only. Use
        :func:`send_from_directory` to safely send files under a path.

    .. versionchanged:: 2.0.2
        ``send_file`` only sets a detected ``Content-Encoding`` if
        ``as_attachment`` is disabled.

    .. versionadded:: 2.0
        Adapted from Flask's implementation.

    .. versionchanged:: 2.0
        ``download_name`` replaces Flask's ``attachment_filename``
         parameter. If ``as_attachment=False``, it is passed with
         ``Content-Disposition: inline`` instead.

    .. versionchanged:: 2.0
        ``max_age`` replaces Flask's ``cache_timeout`` parameter.
        ``conditional`` is enabled and ``max_age`` is not set by
        default.

    .. versionchanged:: 2.0
        ``etag`` replaces Flask's ``add_etags`` parameter. It can be a
        string to use instead of generating one.

    .. versionchanged:: 2.0
        If an encoding is returned when guessing ``mimetype`` from
        ``download_name``, set the ``Content-Encoding`` header.
    """
def send_from_directory(directory: os.PathLike | str, path: os.PathLike | str, environ: WSGIEnvironment, **kwargs: t.Any) -> Response:
    """Send a file from within a directory using :func:`send_file`.

    This is a secure way to serve files from a folder, such as static
    files or uploads. Uses :func:`~werkzeug.security.safe_join` to
    ensure the path coming from the client is not maliciously crafted to
    point outside the specified directory.

    If the final path does not point to an existing regular file,
    returns a 404 :exc:`~werkzeug.exceptions.NotFound` error.

    :param directory: The directory that ``path`` must be located under. This *must not*
        be a value provided by the client, otherwise it becomes insecure.
    :param path: The path to the file to send, relative to ``directory``. This is the
        part of the path provided by the client, which is checked for security.
    :param environ: The WSGI environ for the current request.
    :param kwargs: Arguments to pass to :func:`send_file`.

    .. versionadded:: 2.0
        Adapted from Flask's implementation.
    """
def import_string(import_name: str, silent: bool = False) -> t.Any:
    """Imports an object based on a string.  This is useful if you want to
    use import paths as endpoints or something similar.  An import path can
    be specified either in dotted notation (``xml.sax.saxutils.escape``)
    or with a colon as object delimiter (``xml.sax.saxutils:escape``).

    If `silent` is True the return value will be `None` if the import fails.

    :param import_name: the dotted name for the object to import.
    :param silent: if set to `True` import errors are ignored and
                   `None` is returned instead.
    :return: imported object
    """
def find_modules(import_path: str, include_packages: bool = False, recursive: bool = False) -> t.Iterator[str]:
    """Finds all the modules below a package.  This can be useful to
    automatically import all views / controllers so that their metaclasses /
    function decorators have a chance to register themselves on the
    application.

    Packages are not returned unless `include_packages` is `True`.  This can
    also recursively list modules but in that case it will import all the
    packages to get the correct load path of that module.

    :param import_path: the dotted name for the package to find child modules.
    :param include_packages: set to `True` if packages should be returned, too.
    :param recursive: set to `True` if recursion should happen.
    :return: generator
    """

class ImportStringError(ImportError):
    """Provides information about a failed :func:`import_string` attempt."""
    import_name: str
    exception: BaseException
    def __init__(self, import_name: str, exception: BaseException) -> None: ...
