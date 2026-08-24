import typing as t
from .datastructures import WWWAuthenticate as WWWAuthenticate
from .sansio.response import Response as Response
from .wrappers.request import Request as WSGIRequest
from _typeshed import Incomplete
from _typeshed.wsgi import StartResponse, WSGIEnvironment as WSGIEnvironment
from datetime import datetime

class HTTPException(Exception):
    """The base class for all HTTP exceptions. This exception can be called as a WSGI
    application to render a default error page or you can catch the subclasses
    of it independently and render nicer error messages.

    .. versionchanged:: 2.1
        Removed the ``wrap`` class method.
    """
    code: int | None
    description: str | None
    response: Incomplete
    def __init__(self, description: str | None = None, response: Response | None = None) -> None: ...
    @property
    def name(self) -> str:
        """The status name."""
    def get_description(self, environ: WSGIEnvironment | None = None, scope: dict | None = None) -> str:
        """Get the description."""
    def get_body(self, environ: WSGIEnvironment | None = None, scope: dict | None = None) -> str:
        """Get the HTML body."""
    def get_headers(self, environ: WSGIEnvironment | None = None, scope: dict | None = None) -> list[tuple[str, str]]:
        """Get a list of headers."""
    def get_response(self, environ: WSGIEnvironment | WSGIRequest | None = None, scope: dict | None = None) -> Response:
        """Get a response object.  If one was passed to the exception
        it's returned directly.

        :param environ: the optional environ for the request.  This
                        can be used to modify the response depending
                        on how the request looked like.
        :return: a :class:`Response` object or a subclass thereof.
        """
    def __call__(self, environ: WSGIEnvironment, start_response: StartResponse) -> t.Iterable[bytes]:
        """Call the exception as WSGI application.

        :param environ: the WSGI environment.
        :param start_response: the response callable provided by the WSGI
                               server.
        """

class BadRequest(HTTPException):
    """*400* `Bad Request`

    Raise if the browser sends something to the application the application
    or server cannot handle.
    """
    code: int
    description: str

class BadRequestKeyError(BadRequest, KeyError):
    """An exception that is used to signal both a :exc:`KeyError` and a
    :exc:`BadRequest`. Used by many of the datastructures.
    """
    show_exception: bool
    def __init__(self, arg: str | None = None, *args: t.Any, **kwargs: t.Any) -> None: ...
    @property
    def description(self) -> str: ...
    @description.setter
    def description(self, value: str) -> None: ...

class ClientDisconnected(BadRequest):
    """Internal exception that is raised if Werkzeug detects a disconnected
    client.  Since the client is already gone at that point attempting to
    send the error message to the client might not work and might ultimately
    result in another exception in the server.  Mainly this is here so that
    it is silenced by default as far as Werkzeug is concerned.

    Since disconnections cannot be reliably detected and are unspecified
    by WSGI to a large extent this might or might not be raised if a client
    is gone.

    .. versionadded:: 0.8
    """
class SecurityError(BadRequest):
    """Raised if something triggers a security error.  This is otherwise
    exactly like a bad request error.

    .. versionadded:: 0.9
    """
class BadHost(BadRequest):
    """Raised if the submitted host is badly formatted.

    .. versionadded:: 0.11.2
    """

class Unauthorized(HTTPException):
    """*401* ``Unauthorized``

    Raise if the user is not authorized to access a resource.

    The ``www_authenticate`` argument should be used to set the
    ``WWW-Authenticate`` header. This is used for HTTP basic auth and
    other schemes. Use :class:`~werkzeug.datastructures.WWWAuthenticate`
    to create correctly formatted values. Strictly speaking a 401
    response is invalid if it doesn't provide at least one value for
    this header, although real clients typically don't care.

    :param description: Override the default message used for the body
        of the response.
    :param www-authenticate: A single value, or list of values, for the
        WWW-Authenticate header(s).

    .. versionchanged:: 2.0
        Serialize multiple ``www_authenticate`` items into multiple
        ``WWW-Authenticate`` headers, rather than joining them
        into a single value, for better interoperability.

    .. versionchanged:: 0.15.3
        If the ``www_authenticate`` argument is not set, the
        ``WWW-Authenticate`` header is not set.

    .. versionchanged:: 0.15.3
        The ``response`` argument was restored.

    .. versionchanged:: 0.15.1
        ``description`` was moved back as the first argument, restoring
         its previous position.

    .. versionchanged:: 0.15.0
        ``www_authenticate`` was added as the first argument, ahead of
        ``description``.
    """
    code: int
    description: str
    www_authenticate: Incomplete
    def __init__(self, description: str | None = None, response: Response | None = None, www_authenticate: None | WWWAuthenticate | t.Iterable[WWWAuthenticate] = None) -> None: ...
    def get_headers(self, environ: WSGIEnvironment | None = None, scope: dict | None = None) -> list[tuple[str, str]]: ...

class Forbidden(HTTPException):
    """*403* `Forbidden`

    Raise if the user doesn't have the permission for the requested resource
    but was authenticated.
    """
    code: int
    description: str

class NotFound(HTTPException):
    """*404* `Not Found`

    Raise if a resource does not exist and never existed.
    """
    code: int
    description: str

class MethodNotAllowed(HTTPException):
    """*405* `Method Not Allowed`

    Raise if the server used a method the resource does not handle.  For
    example `POST` if the resource is view only.  Especially useful for REST.

    The first argument for this exception should be a list of allowed methods.
    Strictly speaking the response would be invalid if you don't provide valid
    methods in the header which you can do with that list.
    """
    code: int
    description: str
    valid_methods: Incomplete
    def __init__(self, valid_methods: t.Iterable[str] | None = None, description: str | None = None, response: Response | None = None) -> None:
        """Takes an optional list of valid http methods
        starting with werkzeug 0.3 the list will be mandatory."""
    def get_headers(self, environ: WSGIEnvironment | None = None, scope: dict | None = None) -> list[tuple[str, str]]: ...

class NotAcceptable(HTTPException):
    """*406* `Not Acceptable`

    Raise if the server can't return any content conforming to the
    `Accept` headers of the client.
    """
    code: int
    description: str

class RequestTimeout(HTTPException):
    """*408* `Request Timeout`

    Raise to signalize a timeout.
    """
    code: int
    description: str

class Conflict(HTTPException):
    """*409* `Conflict`

    Raise to signal that a request cannot be completed because it conflicts
    with the current state on the server.

    .. versionadded:: 0.7
    """
    code: int
    description: str

class Gone(HTTPException):
    """*410* `Gone`

    Raise if a resource existed previously and went away without new location.
    """
    code: int
    description: str

class LengthRequired(HTTPException):
    """*411* `Length Required`

    Raise if the browser submitted data but no ``Content-Length`` header which
    is required for the kind of processing the server does.
    """
    code: int
    description: str

class PreconditionFailed(HTTPException):
    """*412* `Precondition Failed`

    Status code used in combination with ``If-Match``, ``If-None-Match``, or
    ``If-Unmodified-Since``.
    """
    code: int
    description: str

class RequestEntityTooLarge(HTTPException):
    """*413* `Request Entity Too Large`

    The status code one should return if the data submitted exceeded a given
    limit.
    """
    code: int
    description: str

class RequestURITooLarge(HTTPException):
    """*414* `Request URI Too Large`

    Like *413* but for too long URLs.
    """
    code: int
    description: str

class UnsupportedMediaType(HTTPException):
    """*415* `Unsupported Media Type`

    The status code returned if the server is unable to handle the media type
    the client transmitted.
    """
    code: int
    description: str

class RequestedRangeNotSatisfiable(HTTPException):
    """*416* `Requested Range Not Satisfiable`

    The client asked for an invalid part of the file.

    .. versionadded:: 0.7
    """
    code: int
    description: str
    length: Incomplete
    units: Incomplete
    def __init__(self, length: int | None = None, units: str = 'bytes', description: str | None = None, response: Response | None = None) -> None:
        """Takes an optional `Content-Range` header value based on ``length``
        parameter.
        """
    def get_headers(self, environ: WSGIEnvironment | None = None, scope: dict | None = None) -> list[tuple[str, str]]: ...

class ExpectationFailed(HTTPException):
    """*417* `Expectation Failed`

    The server cannot meet the requirements of the Expect request-header.

    .. versionadded:: 0.7
    """
    code: int
    description: str

class ImATeapot(HTTPException):
    """*418* `I'm a teapot`

    The server should return this if it is a teapot and someone attempted
    to brew coffee with it.

    .. versionadded:: 0.7
    """
    code: int
    description: str

class UnprocessableEntity(HTTPException):
    """*422* `Unprocessable Entity`

    Used if the request is well formed, but the instructions are otherwise
    incorrect.
    """
    code: int
    description: str

class Locked(HTTPException):
    """*423* `Locked`

    Used if the resource that is being accessed is locked.
    """
    code: int
    description: str

class FailedDependency(HTTPException):
    """*424* `Failed Dependency`

    Used if the method could not be performed on the resource
    because the requested action depended on another action and that action failed.
    """
    code: int
    description: str

class PreconditionRequired(HTTPException):
    '''*428* `Precondition Required`

    The server requires this request to be conditional, typically to prevent
    the lost update problem, which is a race condition between two or more
    clients attempting to update a resource through PUT or DELETE. By requiring
    each client to include a conditional header ("If-Match" or "If-Unmodified-
    Since") with the proper value retained from a recent GET request, the
    server ensures that each client has at least seen the previous revision of
    the resource.
    '''
    code: int
    description: str

class _RetryAfter(HTTPException):
    """Adds an optional ``retry_after`` parameter which will set the
    ``Retry-After`` header. May be an :class:`int` number of seconds or
    a :class:`~datetime.datetime`.
    """
    retry_after: Incomplete
    def __init__(self, description: str | None = None, response: Response | None = None, retry_after: datetime | int | None = None) -> None: ...
    def get_headers(self, environ: WSGIEnvironment | None = None, scope: dict | None = None) -> list[tuple[str, str]]: ...

class TooManyRequests(_RetryAfter):
    '''*429* `Too Many Requests`

    The server is limiting the rate at which this user receives
    responses, and this request exceeds that rate. (The server may use
    any convenient method to identify users and their request rates).
    The server may include a "Retry-After" header to indicate how long
    the user should wait before retrying.

    :param retry_after: If given, set the ``Retry-After`` header to this
        value. May be an :class:`int` number of seconds or a
        :class:`~datetime.datetime`.

    .. versionchanged:: 1.0
        Added ``retry_after`` parameter.
    '''
    code: int
    description: str

class RequestHeaderFieldsTooLarge(HTTPException):
    """*431* `Request Header Fields Too Large`

    The server refuses to process the request because the header fields are too
    large. One or more individual fields may be too large, or the set of all
    headers is too large.
    """
    code: int
    description: str

class UnavailableForLegalReasons(HTTPException):
    """*451* `Unavailable For Legal Reasons`

    This status code indicates that the server is denying access to the
    resource as a consequence of a legal demand.
    """
    code: int
    description: str

class InternalServerError(HTTPException):
    """*500* `Internal Server Error`

    Raise if an internal server error occurred.  This is a good fallback if an
    unknown error occurred in the dispatcher.

    .. versionchanged:: 1.0.0
        Added the :attr:`original_exception` attribute.
    """
    code: int
    description: str
    original_exception: Incomplete
    def __init__(self, description: str | None = None, response: Response | None = None, original_exception: BaseException | None = None) -> None: ...

class NotImplemented(HTTPException):
    """*501* `Not Implemented`

    Raise if the application does not support the action requested by the
    browser.
    """
    code: int
    description: str

class BadGateway(HTTPException):
    """*502* `Bad Gateway`

    If you do proxying in your application you should return this status code
    if you received an invalid response from the upstream server it accessed
    in attempting to fulfill the request.
    """
    code: int
    description: str

class ServiceUnavailable(_RetryAfter):
    """*503* `Service Unavailable`

    Status code you should return if a service is temporarily
    unavailable.

    :param retry_after: If given, set the ``Retry-After`` header to this
        value. May be an :class:`int` number of seconds or a
        :class:`~datetime.datetime`.

    .. versionchanged:: 1.0
        Added ``retry_after`` parameter.
    """
    code: int
    description: str

class GatewayTimeout(HTTPException):
    """*504* `Gateway Timeout`

    Status code you should return if a connection to an upstream server
    times out.
    """
    code: int
    description: str

class HTTPVersionNotSupported(HTTPException):
    """*505* `HTTP Version Not Supported`

    The server does not support the HTTP protocol version used in the request.
    """
    code: int
    description: str

default_exceptions: dict[int, type[HTTPException]]

class Aborter:
    """When passed a dict of code -> exception items it can be used as
    callable that raises exceptions.  If the first argument to the
    callable is an integer it will be looked up in the mapping, if it's
    a WSGI application it will be raised in a proxy exception.

    The rest of the arguments are forwarded to the exception constructor.
    """
    mapping: Incomplete
    def __init__(self, mapping: dict[int, type[HTTPException]] | None = None, extra: dict[int, type[HTTPException]] | None = None) -> None: ...
    def __call__(self, code: int | Response, *args: t.Any, **kwargs: t.Any) -> t.NoReturn: ...

def abort(status: int | Response, *args: t.Any, **kwargs: t.Any) -> t.NoReturn:
    """Raises an :py:exc:`HTTPException` for the given status code or WSGI
    application.

    If a status code is given, it will be looked up in the list of
    exceptions and will raise that exception.  If passed a WSGI application,
    it will wrap it in a proxy WSGI exception and raise that::

       abort(404)  # 404 Not Found
       abort(Response('Hello World'))

    """
