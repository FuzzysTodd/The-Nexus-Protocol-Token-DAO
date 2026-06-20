import dataclasses
import typing as t
from .datastructures import Authorization as Authorization, CallbackDict as CallbackDict, CombinedMultiDict as CombinedMultiDict, EnvironHeaders as EnvironHeaders, FileMultiDict as FileMultiDict, Headers as Headers, MultiDict as MultiDict
from .http import dump_cookie as dump_cookie, dump_options_header as dump_options_header, parse_cookie as parse_cookie, parse_date as parse_date, parse_options_header as parse_options_header
from .sansio.multipart import Data as Data, Epilogue as Epilogue, Field as Field, File as File, MultipartEncoder as MultipartEncoder, Preamble as Preamble
from .urls import iri_to_uri as iri_to_uri
from .utils import cached_property as cached_property, get_content_type as get_content_type
from .wrappers.request import Request as Request
from .wrappers.response import Response as Response
from .wsgi import ClosingIterator as ClosingIterator, get_current_url as get_current_url
from _typeshed import Incomplete
from _typeshed.wsgi import WSGIApplication as WSGIApplication, WSGIEnvironment as WSGIEnvironment
from datetime import datetime

def stream_encode_multipart(data: t.Mapping[str, t.Any], use_tempfile: bool = True, threshold: int = ..., boundary: str | None = None) -> tuple[t.IO[bytes], int, str]:
    """Encode a dict of values (either strings or file descriptors or
    :class:`FileStorage` objects.) into a multipart encoded string stored
    in a file descriptor.

    .. versionchanged:: 3.0
        The ``charset`` parameter was removed.
    """
def encode_multipart(values: t.Mapping[str, t.Any], boundary: str | None = None) -> tuple[str, bytes]:
    """Like `stream_encode_multipart` but returns a tuple in the form
    (``boundary``, ``data``) where data is bytes.

    .. versionchanged:: 3.0
        The ``charset`` parameter was removed.
    """

class EnvironBuilder:
    '''This class can be used to conveniently create a WSGI environment
    for testing purposes.  It can be used to quickly create WSGI environments
    or request objects from arbitrary data.

    The signature of this class is also used in some other places as of
    Werkzeug 0.5 (:func:`create_environ`, :meth:`Response.from_values`,
    :meth:`Client.open`).  Because of this most of the functionality is
    available through the constructor alone.

    Files and regular form data can be manipulated independently of each
    other with the :attr:`form` and :attr:`files` attributes, but are
    passed with the same argument to the constructor: `data`.

    `data` can be any of these values:

    -   a `str` or `bytes` object: The object is converted into an
        :attr:`input_stream`, the :attr:`content_length` is set and you have to
        provide a :attr:`content_type`.
    -   a `dict` or :class:`MultiDict`: The keys have to be strings. The values
        have to be either any of the following objects, or a list of any of the
        following objects:

        -   a :class:`file`-like object:  These are converted into
            :class:`FileStorage` objects automatically.
        -   a `tuple`:  The :meth:`~FileMultiDict.add_file` method is called
            with the key and the unpacked `tuple` items as positional
            arguments.
        -   a `str`:  The string is set as form data for the associated key.
    -   a file-like object: The object content is loaded in memory and then
        handled like a regular `str` or a `bytes`.

    :param path: the path of the request.  In the WSGI environment this will
                 end up as `PATH_INFO`.  If the `query_string` is not defined
                 and there is a question mark in the `path` everything after
                 it is used as query string.
    :param base_url: the base URL is a URL that is used to extract the WSGI
                     URL scheme, host (server name + server port) and the
                     script root (`SCRIPT_NAME`).
    :param query_string: an optional string or dict with URL parameters.
    :param method: the HTTP method to use, defaults to `GET`.
    :param input_stream: an optional input stream.  Do not specify this and
                         `data`.  As soon as an input stream is set you can\'t
                         modify :attr:`args` and :attr:`files` unless you
                         set the :attr:`input_stream` to `None` again.
    :param content_type: The content type for the request.  As of 0.5 you
                         don\'t have to provide this when specifying files
                         and form data via `data`.
    :param content_length: The content length for the request.  You don\'t
                           have to specify this when providing data via
                           `data`.
    :param errors_stream: an optional error stream that is used for
                          `wsgi.errors`.  Defaults to :data:`stderr`.
    :param multithread: controls `wsgi.multithread`.  Defaults to `False`.
    :param multiprocess: controls `wsgi.multiprocess`.  Defaults to `False`.
    :param run_once: controls `wsgi.run_once`.  Defaults to `False`.
    :param headers: an optional list or :class:`Headers` object of headers.
    :param data: a string or dict of form data or a file-object.
                 See explanation above.
    :param json: An object to be serialized and assigned to ``data``.
        Defaults the content type to ``"application/json"``.
        Serialized with the function assigned to :attr:`json_dumps`.
    :param environ_base: an optional dict of environment defaults.
    :param environ_overrides: an optional dict of environment overrides.
    :param auth: An authorization object to use for the
        ``Authorization`` header value. A ``(username, password)`` tuple
        is a shortcut for ``Basic`` authorization.

    .. versionchanged:: 3.0
        The ``charset`` parameter was removed.

    .. versionchanged:: 2.1
        ``CONTENT_TYPE`` and ``CONTENT_LENGTH`` are not duplicated as
        header keys in the environ.

    .. versionchanged:: 2.0
        ``REQUEST_URI`` and ``RAW_URI`` is the full raw URI including
        the query string, not only the path.

    .. versionchanged:: 2.0
        The default :attr:`request_class` is ``Request`` instead of
        ``BaseRequest``.

    .. versionadded:: 2.0
       Added the ``auth`` parameter.

    .. versionadded:: 0.15
        The ``json`` param and :meth:`json_dumps` method.

    .. versionadded:: 0.15
        The environ has keys ``REQUEST_URI`` and ``RAW_URI`` containing
        the path before percent-decoding. This is not part of the WSGI
        PEP, but many WSGI servers include it.

    .. versionchanged:: 0.6
       ``path`` and ``base_url`` can now be unicode strings that are
       encoded with :func:`iri_to_uri`.
    '''
    server_protocol: str
    wsgi_version: Incomplete
    request_class = Request
    json_dumps: Incomplete
    path: Incomplete
    request_uri: Incomplete
    method: Incomplete
    headers: Incomplete
    errors_stream: Incomplete
    multithread: Incomplete
    multiprocess: Incomplete
    run_once: Incomplete
    environ_base: Incomplete
    environ_overrides: Incomplete
    closed: bool
    def __init__(self, path: str = '/', base_url: str | None = None, query_string: t.Mapping[str, str] | str | None = None, method: str = 'GET', input_stream: t.IO[bytes] | None = None, content_type: str | None = None, content_length: int | None = None, errors_stream: t.IO[str] | None = None, multithread: bool = False, multiprocess: bool = False, run_once: bool = False, headers: Headers | t.Iterable[tuple[str, str]] | None = None, data: None | t.IO[bytes] | str | bytes | t.Mapping[str, t.Any] = None, environ_base: t.Mapping[str, t.Any] | None = None, environ_overrides: t.Mapping[str, t.Any] | None = None, mimetype: str | None = None, json: t.Mapping[str, t.Any] | None = None, auth: Authorization | tuple[str, str] | None = None) -> None: ...
    @classmethod
    def from_environ(cls, environ: WSGIEnvironment, **kwargs: t.Any) -> EnvironBuilder:
        """Turn an environ dict back into a builder. Any extra kwargs
        override the args extracted from the environ.

        .. versionchanged:: 2.0
            Path and query values are passed through the WSGI decoding
            dance to avoid double encoding.

        .. versionadded:: 0.15
        """
    @property
    def base_url(self) -> str:
        """The base URL is used to extract the URL scheme, host name,
        port, and root path.
        """
    script_root: Incomplete
    host: Incomplete
    url_scheme: Incomplete
    @base_url.setter
    def base_url(self, value: str | None) -> None: ...
    @property
    def content_type(self) -> str | None:
        """The content type for the request.  Reflected from and to
        the :attr:`headers`.  Do not set if you set :attr:`files` or
        :attr:`form` for auto detection.
        """
    @content_type.setter
    def content_type(self, value: str | None) -> None: ...
    @property
    def mimetype(self) -> str | None:
        """The mimetype (content type without charset etc.)

        .. versionadded:: 0.14
        """
    @mimetype.setter
    def mimetype(self, value: str) -> None: ...
    @property
    def mimetype_params(self) -> t.Mapping[str, str]:
        """The mimetype parameters as dict.  For example if the
        content type is ``text/html; charset=utf-8`` the params would be
        ``{'charset': 'utf-8'}``.

        .. versionadded:: 0.14
        """
    @property
    def content_length(self) -> int | None:
        """The content length as integer.  Reflected from and to the
        :attr:`headers`.  Do not set if you set :attr:`files` or
        :attr:`form` for auto detection.
        """
    @content_length.setter
    def content_length(self, value: int | None) -> None: ...
    @property
    def form(self) -> MultiDict:
        """A :class:`MultiDict` of form values."""
    @form.setter
    def form(self, value: MultiDict) -> None: ...
    @property
    def files(self) -> FileMultiDict:
        """A :class:`FileMultiDict` of uploaded files. Use
        :meth:`~FileMultiDict.add_file` to add new files.
        """
    @files.setter
    def files(self, value: FileMultiDict) -> None: ...
    @property
    def input_stream(self) -> t.IO[bytes] | None:
        """An optional input stream. This is mutually exclusive with
        setting :attr:`form` and :attr:`files`, setting it will clear
        those. Do not provide this if the method is not ``POST`` or
        another method that has a body.
        """
    @input_stream.setter
    def input_stream(self, value: t.IO[bytes] | None) -> None: ...
    @property
    def query_string(self) -> str:
        """The query string.  If you set this to a string
        :attr:`args` will no longer be available.
        """
    @query_string.setter
    def query_string(self, value: str | None) -> None: ...
    @property
    def args(self) -> MultiDict:
        """The URL arguments as :class:`MultiDict`."""
    @args.setter
    def args(self, value: MultiDict | None) -> None: ...
    @property
    def server_name(self) -> str:
        """The server name (read-only, use :attr:`host` to set)"""
    @property
    def server_port(self) -> int:
        """The server port as integer (read-only, use :attr:`host` to set)"""
    def __del__(self) -> None: ...
    def close(self) -> None:
        """Closes all files.  If you put real :class:`file` objects into the
        :attr:`files` dict you can call this method to automatically close
        them all in one go.
        """
    def get_environ(self) -> WSGIEnvironment:
        """Return the built environ.

        .. versionchanged:: 0.15
            The content type and length headers are set based on
            input stream detection. Previously this only set the WSGI
            keys.
        """
    def get_request(self, cls: type[Request] | None = None) -> Request:
        """Returns a request with the data.  If the request class is not
        specified :attr:`request_class` is used.

        :param cls: The request wrapper to use.
        """

class ClientRedirectError(Exception):
    """If a redirect loop is detected when using follow_redirects=True with
    the :cls:`Client`, then this exception is raised.
    """

class Client:
    """Simulate sending requests to a WSGI application without running a WSGI or HTTP
    server.

    :param application: The WSGI application to make requests to.
    :param response_wrapper: A :class:`.Response` class to wrap response data with.
        Defaults to :class:`.TestResponse`. If it's not a subclass of ``TestResponse``,
        one will be created.
    :param use_cookies: Persist cookies from ``Set-Cookie`` response headers to the
        ``Cookie`` header in subsequent requests. Domain and path matching is supported,
        but other cookie parameters are ignored.
    :param allow_subdomain_redirects: Allow requests to follow redirects to subdomains.
        Enable this if the application handles subdomains and redirects between them.

    .. versionchanged:: 2.3
        Simplify cookie implementation, support domain and path matching.

    .. versionchanged:: 2.1
        All data is available as properties on the returned response object. The
        response cannot be returned as a tuple.

    .. versionchanged:: 2.0
        ``response_wrapper`` is always a subclass of :class:``TestResponse``.

    .. versionchanged:: 0.5
        Added the ``use_cookies`` parameter.
    """
    application: Incomplete
    response_wrapper: Incomplete
    allow_subdomain_redirects: Incomplete
    def __init__(self, application: WSGIApplication, response_wrapper: type[Response] | None = None, use_cookies: bool = True, allow_subdomain_redirects: bool = False) -> None: ...
    def get_cookie(self, key: str, domain: str = 'localhost', path: str = '/') -> Cookie | None:
        """Return a :class:`.Cookie` if it exists. Cookies are uniquely identified by
        ``(domain, path, key)``.

        :param key: The decoded form of the key for the cookie.
        :param domain: The domain the cookie was set for.
        :param path: The path the cookie was set for.

        .. versionadded:: 2.3
        """
    def set_cookie(self, key: str, value: str = '', *, domain: str = 'localhost', origin_only: bool = True, path: str = '/', **kwargs: t.Any) -> None:
        """Set a cookie to be sent in subsequent requests.

        This is a convenience to skip making a test request to a route that would set
        the cookie. To test the cookie, make a test request to a route that uses the
        cookie value.

        The client uses ``domain``, ``origin_only``, and ``path`` to determine which
        cookies to send with a request. It does not use other cookie parameters that
        browsers use, since they're not applicable in tests.

        :param key: The key part of the cookie.
        :param value: The value part of the cookie.
        :param domain: Send this cookie with requests that match this domain. If
            ``origin_only`` is true, it must be an exact match, otherwise it may be a
            suffix match.
        :param origin_only: Whether the domain must be an exact match to the request.
        :param path: Send this cookie with requests that match this path either exactly
            or as a prefix.
        :param kwargs: Passed to :func:`.dump_cookie`.

        .. versionchanged:: 3.0
            The parameter ``server_name`` is removed. The first parameter is
            ``key``. Use the ``domain`` and ``origin_only`` parameters instead.

        .. versionchanged:: 2.3
            The ``origin_only`` parameter was added.

        .. versionchanged:: 2.3
            The ``domain`` parameter defaults to ``localhost``.
        """
    def delete_cookie(self, key: str, *, domain: str = 'localhost', path: str = '/') -> None:
        """Delete a cookie if it exists. Cookies are uniquely identified by
        ``(domain, path, key)``.

        :param key: The decoded form of the key for the cookie.
        :param domain: The domain the cookie was set for.
        :param path: The path the cookie was set for.

        .. versionchanged:: 3.0
            The ``server_name`` parameter is removed. The first parameter is
            ``key``. Use the ``domain`` parameter instead.

        .. versionchanged:: 3.0
            The ``secure``, ``httponly`` and ``samesite`` parameters are removed.

        .. versionchanged:: 2.3
            The ``domain`` parameter defaults to ``localhost``.
        """
    def run_wsgi_app(self, environ: WSGIEnvironment, buffered: bool = False) -> tuple[t.Iterable[bytes], str, Headers]:
        """Runs the wrapped WSGI app with the given environment.

        :meta private:
        """
    def resolve_redirect(self, response: TestResponse, buffered: bool = False) -> TestResponse:
        """Perform a new request to the location given by the redirect
        response to the previous request.

        :meta private:
        """
    def open(self, *args: t.Any, buffered: bool = False, follow_redirects: bool = False, **kwargs: t.Any) -> TestResponse:
        """Generate an environ dict from the given arguments, make a
        request to the application using it, and return the response.

        :param args: Passed to :class:`EnvironBuilder` to create the
            environ for the request. If a single arg is passed, it can
            be an existing :class:`EnvironBuilder` or an environ dict.
        :param buffered: Convert the iterator returned by the app into
            a list. If the iterator has a ``close()`` method, it is
            called automatically.
        :param follow_redirects: Make additional requests to follow HTTP
            redirects until a non-redirect status is returned.
            :attr:`TestResponse.history` lists the intermediate
            responses.

        .. versionchanged:: 2.1
            Removed the ``as_tuple`` parameter.

        .. versionchanged:: 2.0
            The request input stream is closed when calling
            ``response.close()``. Input streams for redirects are
            automatically closed.

        .. versionchanged:: 0.5
            If a dict is provided as file in the dict for the ``data``
            parameter the content type has to be called ``content_type``
            instead of ``mimetype``. This change was made for
            consistency with :class:`werkzeug.FileWrapper`.

        .. versionchanged:: 0.5
            Added the ``follow_redirects`` parameter.
        """
    def get(self, *args: t.Any, **kw: t.Any) -> TestResponse:
        """Call :meth:`open` with ``method`` set to ``GET``."""
    def post(self, *args: t.Any, **kw: t.Any) -> TestResponse:
        """Call :meth:`open` with ``method`` set to ``POST``."""
    def put(self, *args: t.Any, **kw: t.Any) -> TestResponse:
        """Call :meth:`open` with ``method`` set to ``PUT``."""
    def delete(self, *args: t.Any, **kw: t.Any) -> TestResponse:
        """Call :meth:`open` with ``method`` set to ``DELETE``."""
    def patch(self, *args: t.Any, **kw: t.Any) -> TestResponse:
        """Call :meth:`open` with ``method`` set to ``PATCH``."""
    def options(self, *args: t.Any, **kw: t.Any) -> TestResponse:
        """Call :meth:`open` with ``method`` set to ``OPTIONS``."""
    def head(self, *args: t.Any, **kw: t.Any) -> TestResponse:
        """Call :meth:`open` with ``method`` set to ``HEAD``."""
    def trace(self, *args: t.Any, **kw: t.Any) -> TestResponse:
        """Call :meth:`open` with ``method`` set to ``TRACE``."""

def create_environ(*args: t.Any, **kwargs: t.Any) -> WSGIEnvironment:
    """Create a new WSGI environ dict based on the values passed.  The first
    parameter should be the path of the request which defaults to '/'.  The
    second one can either be an absolute path (in that case the host is
    localhost:80) or a full path to the request with scheme, netloc port and
    the path to the script.

    This accepts the same arguments as the :class:`EnvironBuilder`
    constructor.

    .. versionchanged:: 0.5
       This function is now a thin wrapper over :class:`EnvironBuilder` which
       was added in 0.5.  The `headers`, `environ_base`, `environ_overrides`
       and `charset` parameters were added.
    """
def run_wsgi_app(app: WSGIApplication, environ: WSGIEnvironment, buffered: bool = False) -> tuple[t.Iterable[bytes], str, Headers]:
    """Return a tuple in the form (app_iter, status, headers) of the
    application output.  This works best if you pass it an application that
    returns an iterator all the time.

    Sometimes applications may use the `write()` callable returned
    by the `start_response` function.  This tries to resolve such edge
    cases automatically.  But if you don't get the expected output you
    should set `buffered` to `True` which enforces buffering.

    If passed an invalid WSGI application the behavior of this function is
    undefined.  Never pass non-conforming WSGI applications to this function.

    :param app: the application to execute.
    :param buffered: set to `True` to enforce buffering.
    :return: tuple in the form ``(app_iter, status, headers)``
    """

class TestResponse(Response):
    """:class:`~werkzeug.wrappers.Response` subclass that provides extra
    information about requests made with the test :class:`Client`.

    Test client requests will always return an instance of this class.
    If a custom response class is passed to the client, it is
    subclassed along with this to support test information.

    If the test request included large files, or if the application is
    serving a file, call :meth:`close` to close any open files and
    prevent Python showing a ``ResourceWarning``.

    .. versionchanged:: 2.2
        Set the ``default_mimetype`` to None to prevent a mimetype being
        assumed if missing.

    .. versionchanged:: 2.1
        Response instances cannot be treated as tuples.

    .. versionadded:: 2.0
        Test client methods always return instances of this class.
    """
    default_mimetype: Incomplete
    request: Request
    history: tuple[TestResponse, ...]
    __test__: bool
    def __init__(self, response: t.Iterable[bytes], status: str, headers: Headers, request: Request, history: tuple[TestResponse] = (), **kwargs: t.Any) -> None: ...
    def text(self) -> str:
        """The response data as text. A shortcut for
        ``response.get_data(as_text=True)``.

        .. versionadded:: 2.1
        """

@dataclasses.dataclass
class Cookie:
    """A cookie key, value, and parameters.

    The class itself is not a public API. Its attributes are documented for inspection
    with :meth:`.Client.get_cookie` only.

    .. versionadded:: 2.3
    """
    key: str
    value: str
    decoded_key: str
    decoded_value: str
    expires: datetime | None
    max_age: int | None
    domain: str
    origin_only: bool
    path: str
    secure: bool | None
    http_only: bool | None
    same_site: str | None
    def __init__(self, key, value, decoded_key, decoded_value, expires, max_age, domain, origin_only, path, secure, http_only, same_site) -> None: ...
