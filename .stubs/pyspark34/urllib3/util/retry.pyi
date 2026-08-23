from ..exceptions import ConnectTimeoutError as ConnectTimeoutError, InvalidHeader as InvalidHeader, MaxRetryError as MaxRetryError, ProtocolError as ProtocolError, ProxyError as ProxyError, ReadTimeoutError as ReadTimeoutError, ResponseError as ResponseError
from _typeshed import Incomplete
from typing import NamedTuple

log: Incomplete

class RequestHistory(NamedTuple):
    method: Incomplete
    url: Incomplete
    error: Incomplete
    status: Incomplete
    redirect_location: Incomplete

class _RetryMeta(type):
    @property
    def DEFAULT_METHOD_WHITELIST(cls): ...
    @DEFAULT_METHOD_WHITELIST.setter
    def DEFAULT_METHOD_WHITELIST(cls, value) -> None: ...
    @property
    def DEFAULT_REDIRECT_HEADERS_BLACKLIST(cls): ...
    @DEFAULT_REDIRECT_HEADERS_BLACKLIST.setter
    def DEFAULT_REDIRECT_HEADERS_BLACKLIST(cls, value) -> None: ...
    @property
    def BACKOFF_MAX(cls): ...
    @BACKOFF_MAX.setter
    def BACKOFF_MAX(cls, value) -> None: ...

class Retry:
    """Retry configuration.

    Each retry attempt will create a new Retry object with updated values, so
    they can be safely reused.

    Retries can be defined as a default for a pool::

        retries = Retry(connect=5, read=2, redirect=5)
        http = PoolManager(retries=retries)
        response = http.request('GET', 'http://example.com/')

    Or per-request (which overrides the default for the pool)::

        response = http.request('GET', 'http://example.com/', retries=Retry(10))

    Retries can be disabled by passing ``False``::

        response = http.request('GET', 'http://example.com/', retries=False)

    Errors will be wrapped in :class:`~urllib3.exceptions.MaxRetryError` unless
    retries are disabled, in which case the causing exception will be raised.

    :param int total:
        Total number of retries to allow. Takes precedence over other counts.

        Set to ``None`` to remove this constraint and fall back on other
        counts.

        Set to ``0`` to fail on the first retry.

        Set to ``False`` to disable and imply ``raise_on_redirect=False``.

    :param int connect:
        How many connection-related errors to retry on.

        These are errors raised before the request is sent to the remote server,
        which we assume has not triggered the server to process the request.

        Set to ``0`` to fail on the first retry of this type.

    :param int read:
        How many times to retry on read errors.

        These errors are raised after the request was sent to the server, so the
        request may have side-effects.

        Set to ``0`` to fail on the first retry of this type.

    :param int redirect:
        How many redirects to perform. Limit this to avoid infinite redirect
        loops.

        A redirect is a HTTP response with a status code 301, 302, 303, 307 or
        308.

        Set to ``0`` to fail on the first retry of this type.

        Set to ``False`` to disable and imply ``raise_on_redirect=False``.

    :param int status:
        How many times to retry on bad status codes.

        These are retries made on responses, where status code matches
        ``status_forcelist``.

        Set to ``0`` to fail on the first retry of this type.

    :param int other:
        How many times to retry on other errors.

        Other errors are errors that are not connect, read, redirect or status errors.
        These errors might be raised after the request was sent to the server, so the
        request might have side-effects.

        Set to ``0`` to fail on the first retry of this type.

        If ``total`` is not set, it's a good idea to set this to 0 to account
        for unexpected edge cases and avoid infinite retry loops.

    :param iterable allowed_methods:
        Set of uppercased HTTP method verbs that we should retry on.

        By default, we only retry on methods which are considered to be
        idempotent (multiple requests with the same parameters end with the
        same state). See :attr:`Retry.DEFAULT_ALLOWED_METHODS`.

        Set to a ``False`` value to retry on any verb.

        .. warning::

            Previously this parameter was named ``method_whitelist``, that
            usage is deprecated in v1.26.0 and will be removed in v2.0.

    :param iterable status_forcelist:
        A set of integer HTTP status codes that we should force a retry on.
        A retry is initiated if the request method is in ``allowed_methods``
        and the response status code is in ``status_forcelist``.

        By default, this is disabled with ``None``.

    :param float backoff_factor:
        A backoff factor to apply between attempts after the second try
        (most errors are resolved immediately by a second try without a
        delay). urllib3 will sleep for::

            {backoff factor} * (2 ** ({number of total retries} - 1))

        seconds. If the backoff_factor is 0.1, then :func:`.sleep` will sleep
        for [0.0s, 0.2s, 0.4s, ...] between retries. It will never be longer
        than :attr:`Retry.DEFAULT_BACKOFF_MAX`.

        By default, backoff is disabled (set to 0).

    :param bool raise_on_redirect: Whether, if the number of redirects is
        exhausted, to raise a MaxRetryError, or to return a response with a
        response code in the 3xx range.

    :param bool raise_on_status: Similar meaning to ``raise_on_redirect``:
        whether we should raise an exception, or return a response,
        if status falls in ``status_forcelist`` range and retries have
        been exhausted.

    :param tuple history: The history of the request encountered during
        each call to :meth:`~Retry.increment`. The list is in the order
        the requests occurred. Each list item is of class :class:`RequestHistory`.

    :param bool respect_retry_after_header:
        Whether to respect Retry-After header on status codes defined as
        :attr:`Retry.RETRY_AFTER_STATUS_CODES` or not.

    :param iterable remove_headers_on_redirect:
        Sequence of headers to remove from the request when a response
        indicating a redirect is returned before firing off the redirected
        request.
    """
    DEFAULT_ALLOWED_METHODS: Incomplete
    RETRY_AFTER_STATUS_CODES: Incomplete
    DEFAULT_REMOVE_HEADERS_ON_REDIRECT: Incomplete
    DEFAULT_BACKOFF_MAX: int
    total: Incomplete
    connect: Incomplete
    read: Incomplete
    status: Incomplete
    other: Incomplete
    redirect: Incomplete
    status_forcelist: Incomplete
    allowed_methods: Incomplete
    backoff_factor: Incomplete
    raise_on_redirect: Incomplete
    raise_on_status: Incomplete
    history: Incomplete
    respect_retry_after_header: Incomplete
    remove_headers_on_redirect: Incomplete
    def __init__(self, total: int = 10, connect: Incomplete | None = None, read: Incomplete | None = None, redirect: Incomplete | None = None, status: Incomplete | None = None, other: Incomplete | None = None, allowed_methods=..., status_forcelist: Incomplete | None = None, backoff_factor: int = 0, raise_on_redirect: bool = True, raise_on_status: bool = True, history: Incomplete | None = None, respect_retry_after_header: bool = True, remove_headers_on_redirect=..., method_whitelist=...) -> None: ...
    def new(self, **kw): ...
    @classmethod
    def from_int(cls, retries, redirect: bool = True, default: Incomplete | None = None):
        """Backwards-compatibility for the old retries format."""
    def get_backoff_time(self):
        """Formula for computing the current backoff

        :rtype: float
        """
    def parse_retry_after(self, retry_after): ...
    def get_retry_after(self, response):
        """Get the value of Retry-After in seconds."""
    def sleep_for_retry(self, response: Incomplete | None = None): ...
    def sleep(self, response: Incomplete | None = None) -> None:
        """Sleep between retry attempts.

        This method will respect a server's ``Retry-After`` response header
        and sleep the duration of the time requested. If that is not present, it
        will use an exponential backoff. By default, the backoff factor is 0 and
        this method will return immediately.
        """
    def is_retry(self, method, status_code, has_retry_after: bool = False):
        """Is this method/status code retryable? (Based on allowlists and control
        variables such as the number of total retries to allow, whether to
        respect the Retry-After header, whether this header is present, and
        whether the returned status code is on the list of status codes to
        be retried upon on the presence of the aforementioned header)
        """
    def is_exhausted(self):
        """Are we out of retries?"""
    def increment(self, method: Incomplete | None = None, url: Incomplete | None = None, response: Incomplete | None = None, error: Incomplete | None = None, _pool: Incomplete | None = None, _stacktrace: Incomplete | None = None):
        """Return a new Retry object with incremented retry counters.

        :param response: A response object, or None, if the server did not
            return a response.
        :type response: :class:`~urllib3.response.HTTPResponse`
        :param Exception error: An error encountered during the request, or
            None if the response was received successfully.

        :return: A new ``Retry`` object.
        """
    def __getattr__(self, item): ...
