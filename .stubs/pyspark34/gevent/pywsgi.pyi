from _typeshed import Incomplete
from collections.abc import Generator
from gevent.server import StreamServer
from http import client

__all__ = ['WSGIServer', 'WSGIHandler', 'LoggingLogAdapter', 'Environ', 'SecureEnviron', 'WSGISecureEnviron']

class _InvalidClientInput(IOError): ...

class _InvalidClientRequest(ValueError):
    formatted_message: Incomplete
    def __init__(self, message) -> None: ...

class Input:
    rfile: Incomplete
    content_length: Incomplete
    socket: Incomplete
    position: int
    chunked_input: Incomplete
    chunk_length: int
    def __init__(self, rfile, content_length, socket: Incomplete | None = None, chunked_input: bool = False) -> None: ...
    def read(self, length: Incomplete | None = None): ...
    def readline(self, size: Incomplete | None = None): ...
    def readlines(self, hint: Incomplete | None = None): ...
    def __iter__(self): ...
    def next(self): ...
    __next__ = next

class OldMessage(client.HTTPMessage):
    status: str
    def __init__(self, **kwargs) -> None: ...
    def getheader(self, name, default: Incomplete | None = None): ...
    @property
    def headers(self) -> Generator[Incomplete, None, None]: ...
    @property
    def typeheader(self): ...

class WSGIHandler:
    """
    Handles HTTP requests from a socket, creates the WSGI environment, and
    interacts with the WSGI application.

    This is the default value of :attr:`WSGIServer.handler_class`.
    This class may be subclassed carefully, and that class set on a
    :class:`WSGIServer` instance through a keyword argument at
    construction time.

    Instances are constructed with the same arguments as passed to the
    server's :meth:`WSGIServer.handle` method followed by the server
    itself. The application and environment are obtained from the server.

    """
    protocol_version: str
    def MessageClass(self, *args): ...
    status: Incomplete
    response_headers: Incomplete
    code: Incomplete
    provided_date: Incomplete
    provided_content_length: Incomplete
    close_connection: bool
    time_start: int
    time_finish: int
    headers_sent: bool
    response_use_chunked: bool
    connection_upgraded: bool
    environ: Incomplete
    application: Incomplete
    requestline: Incomplete
    response_length: int
    result: Incomplete
    wsgi_input: Incomplete
    content_length: int
    headers: Incomplete
    request_version: Incomplete
    command: Incomplete
    path: Incomplete
    socket: Incomplete
    client_address: Incomplete
    server: Incomplete
    rfile: Incomplete
    def __init__(self, sock, address, server, rfile: Incomplete | None = None) -> None: ...
    def handle(self) -> None:
        """
        The main request handling method, called by the server.

        This method runs a request handling loop, calling
        :meth:`handle_one_request` until all requests on the
        connection have been handled (that is, it implements
        keep-alive).
        """
    def read_request(self, raw_requestline):
        """
        Parse the incoming request.

        Parses various headers into ``self.headers`` using
        :attr:`MessageClass`. Other attributes that are set upon a successful
        return of this method include ``self.content_length`` and ``self.close_connection``.

        :param str raw_requestline: A native :class:`str` representing
           the request line. A processed version of this will be stored
           into ``self.requestline``.

        :raises ValueError: If the request is invalid. This error will
           not be logged as a traceback (because it's a client issue, not a server problem).
        :return: A boolean value indicating whether the request was successfully parsed.
           This method should either return a true value or have raised a ValueError
           with details about the parsing error.

        .. versionchanged:: 1.1b6
           Raise the previously documented :exc:`ValueError` in more cases instead of returning a
           false value; this allows subclasses more opportunity to customize behaviour.
        """
    def log_error(self, msg, *args) -> None: ...
    def read_requestline(self):
        """
        Read and return the HTTP request line.

        Under both Python 2 and 3, this should return the native
        ``str`` type; under Python 3, this probably means the bytes read
        from the network need to be decoded (using the ISO-8859-1 charset, aka
        latin-1).
        """
    def handle_one_request(self):
        """
        Handles one HTTP request using ``self.socket`` and ``self.rfile``.

        Each invocation of this method will do several things, including (but not limited to):

        - Read the request line using :meth:`read_requestline`;
        - Read the rest of the request, including headers, with :meth:`read_request`;
        - Construct a new WSGI environment in ``self.environ`` using :meth:`get_environ`;
        - Store the application in ``self.application``, retrieving it from the server;
        - Handle the remainder of the request, including invoking the application,
          with :meth:`handle_one_response`

        There are several possible return values to indicate the state
        of the client connection:

        - ``None``
            The client connection is already closed or should
            be closed because the WSGI application or client set the
            ``Connection: close`` header. The request handling
            loop should terminate and perform cleanup steps.
        - (status, body)
            An HTTP status and body tuple. The request was in error,
            as detailed by the status and body. The request handling
            loop should terminate, close the connection, and perform
            cleanup steps. Note that the ``body`` is the complete contents
            to send to the client, including all headers and the initial
            status line.
        - ``True``
            The literal ``True`` value. The request was successfully handled
            and the response sent to the client by :meth:`handle_one_response`.
            The connection remains open to process more requests and the connection
            handling loop should call this method again. This is the typical return
            value.

        .. seealso:: :meth:`handle`

        .. versionchanged:: 1.1b6
           Funnel exceptions having to do with invalid HTTP requests through
           :meth:`_handle_client_error` to allow subclasses to customize. Note that
           this is experimental and may change in the future.
        """
    def finalize_headers(self) -> None: ...
    ApplicationError = AssertionError
    def write(self, data) -> None: ...
    def start_response(self, status, headers, exc_info: Incomplete | None = None):
        """
         .. versionchanged:: 1.2a1
            Avoid HTTP header injection by raising a :exc:`ValueError`
            if *status* or any *header* name or value contains a carriage
            return or newline.
         .. versionchanged:: 1.1b5
            Pro-actively handle checking the encoding of the status line
            and headers during this method. On Python 2, avoid some
            extra encodings.
        """
    def log_request(self) -> None: ...
    def format_request(self): ...
    def process_result(self) -> None: ...
    def run_application(self) -> None: ...
    ignored_socket_errors: Incomplete
    def handle_one_response(self) -> None:
        """
        Invoke the application to produce one response.

        This is called by :meth:`handle_one_request` after all the
        state for the request has been established. It is responsible
        for error handling.
        """
    def handle_error(self, t, v, tb) -> None: ...
    def get_environ(self):
        """
        Construct and return a new WSGI environment dictionary for a specific request.

        This should begin with asking the server for the base environment
        using :meth:`WSGIServer.get_environ`, and then proceed to add the
        request specific values.

        By the time this method is invoked the request line and request shall have
        been parsed and ``self.headers`` shall be populated.
        """

class _NoopLog:
    def write(self, *args, **kwargs) -> None: ...
    def flush(self) -> None: ...
    def writelines(self, *args, **kwargs) -> None: ...

class LoggingLogAdapter:
    """
    An adapter for :class:`logging.Logger` instances
    to let them be used with :class:`WSGIServer`.

    .. warning:: Unless the entire process is monkey-patched at a very
        early part of the lifecycle (before logging is configured),
        loggers are likely to not be gevent-cooperative. For example,
        the socket and syslog handlers use the socket module in a way
        that can block, and most handlers acquire threading locks.

    .. warning:: It *may* be possible for the logging functions to be
       called in the :class:`gevent.Hub` greenlet. Code running in the
       hub greenlet cannot use any gevent blocking functions without triggering
       a ``LoopExit``.

    .. versionadded:: 1.1a3

    .. versionchanged:: 1.1b6
       Attributes not present on this object are proxied to the underlying
       logger instance. This permits using custom :class:`~logging.Logger`
       subclasses (or indeed, even duck-typed objects).

    .. versionchanged:: 1.1
       Strip trailing newline characters on the message passed to :meth:`write`
       because log handlers will usually add one themselves.
    """
    def __init__(self, logger, level: int = 20) -> None:
        """
        Write information to the *logger* at the given *level* (default to INFO).
        """
    def write(self, msg) -> None: ...
    def flush(self) -> None:
        """No-op; required to be a file-like object"""
    def writelines(self, lines) -> None: ...
    def __getattr__(self, name): ...
    def __setattr__(self, name, value) -> None: ...
    def __delattr__(self, name) -> None: ...

class Environ(dict):
    """
    A base class that can be used for WSGI environment objects.

    Provisional API.

    .. versionadded:: 1.2a1
    """
    def copy(self): ...
    def iteritems(self): ...
    def __reduce_ex__(self, proto): ...

class SecureEnviron(Environ):
    """
    An environment that does not print its keys and values
    by default.

    Provisional API.

    This is intended to keep potentially sensitive information like
    HTTP authorization and cookies from being inadvertently printed
    or logged.

    For debugging, each instance can have its *secure_repr* attribute
    set to ``False``, which will cause it to print like a normal dict.

    When *secure_repr* is ``True`` (the default), then the value of
    the *whitelist_keys* attribute is consulted; if this value is
    true-ish, it should be a container (something that responds to
    ``in``) of key names (typically a list or set). Keys and values in
    this dictionary that are in *whitelist_keys* will then be printed,
    while all other values will be masked. These values may be
    customized on the class by setting the *default_secure_repr* and
    *default_whitelist_keys*, respectively::

        >>> environ = SecureEnviron(key='value')
        >>> environ # doctest: +ELLIPSIS
        <pywsgi.SecureEnviron dict (keys: 1) at ...

    If we whitelist the key, it gets printed::

        >>> environ.whitelist_keys = {'key'}
        >>> environ
        {'key': 'value'}

    A non-whitelisted key (*only*, to avoid doctest issues) is masked::

        >>> environ['secure'] = 'secret'; del environ['key']
        >>> environ
        {'secure': '<MASKED>'}

    We can turn it off entirely for the instance::

        >>> environ.secure_repr = False
        >>> environ
        {'secure': 'secret'}

    We can also customize it at the class level (here we use a new
    class to be explicit and to avoid polluting the true default
    values; we would set this class to be the ``environ_class`` of the
    server)::

        >>> class MyEnviron(SecureEnviron):
        ...    default_whitelist_keys = ('key',)
        ...
        >>> environ = MyEnviron({'key': 'value'})
        >>> environ
        {'key': 'value'}

    .. versionadded:: 1.2a1
    """
    default_secure_repr: bool
    default_whitelist_keys: Incomplete
    default_print_masked_keys: bool
    def __getattr__(self, name): ...

class WSGISecureEnviron(SecureEnviron):
    """
    Specializes the default list of whitelisted keys to a few
    common WSGI variables.

    Example::

       >>> environ = WSGISecureEnviron(REMOTE_ADDR='::1', HTTP_AUTHORIZATION='secret')
       >>> environ
       {'REMOTE_ADDR': '::1', (hidden keys: 1)}
       >>> import pprint
       >>> pprint.pprint(environ)
       {'REMOTE_ADDR': '::1', (hidden keys: 1)}
       >>> print(pprint.pformat(environ))
       {'REMOTE_ADDR': '::1', (hidden keys: 1)}
    """
    default_whitelist_keys: Incomplete
    default_print_masked_keys: bool

class WSGIServer(StreamServer):
    """
    A WSGI server based on :class:`StreamServer` that supports HTTPS.


    :keyword log: If given, an object with a ``write`` method to which
        request (access) logs will be written. If not given, defaults
        to :obj:`sys.stderr`. You may pass ``None`` to disable request
        logging. You may use a wrapper, around e.g., :mod:`logging`,
        to support objects that don't implement a ``write`` method.
        (If you pass a :class:`~logging.Logger` instance, or in
        general something that provides a ``log`` method but not a
        ``write`` method, such a wrapper will automatically be created
        and it will be logged to at the :data:`~logging.INFO` level.)

    :keyword error_log: If given, a file-like object with ``write``,
        ``writelines`` and ``flush`` methods to which error logs will
        be written. If not given, defaults to :obj:`sys.stderr`. You
        may pass ``None`` to disable error logging (not recommended).
        You may use a wrapper, around e.g., :mod:`logging`, to support
        objects that don't implement the proper methods. This
        parameter will become the value for ``wsgi.errors`` in the
        WSGI environment (if not already set). (As with *log*,
        wrappers for :class:`~logging.Logger` instances and the like
        will be created automatically and logged to at the :data:`~logging.ERROR`
        level.)

    .. seealso::

        :class:`LoggingLogAdapter`
            See important warnings before attempting to use :mod:`logging`.

    .. versionchanged:: 1.1a3
        Added the ``error_log`` parameter, and set ``wsgi.errors`` in the WSGI
        environment to this value.
    .. versionchanged:: 1.1a3
        Add support for passing :class:`logging.Logger` objects to the ``log`` and
        ``error_log`` arguments.
    .. versionchanged:: 20.6.0
        Passing a ``handle`` kwarg to the constructor is now officially deprecated.
    """
    handler_class = WSGIHandler
    log: Incomplete
    error_log: Incomplete
    environ_class = dict
    secure_environ_class = WSGISecureEnviron
    base_env: Incomplete
    application: Incomplete
    def __init__(self, listener, application: Incomplete | None = None, backlog: Incomplete | None = None, spawn: str = 'default', log: str = 'default', error_log: str = 'default', handler_class: Incomplete | None = None, environ: Incomplete | None = None, **ssl_args) -> None: ...
    environ: Incomplete
    def set_environ(self, environ: Incomplete | None = None) -> None: ...
    max_accept: int
    def set_max_accept(self) -> None: ...
    def get_environ(self): ...
    def init_socket(self) -> None: ...
    def update_environ(self) -> None:
        """
        Called before the first request is handled to fill in WSGI environment values.

        This includes getting the correct server name and port.
        """
    def handle(self, sock, address) -> None:
        """
        Create an instance of :attr:`handler_class` to handle the request.

        This method blocks until the handler returns.
        """
