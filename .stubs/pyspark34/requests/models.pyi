from ._internal_utils import to_native_string as to_native_string, unicode_is_ascii as unicode_is_ascii
from .auth import HTTPBasicAuth as HTTPBasicAuth
from .compat import Callable as Callable, JSONDecodeError as JSONDecodeError, Mapping as Mapping, basestring as basestring, builtin_str as builtin_str, chardet as chardet, cookielib as cookielib, urlencode as urlencode, urlsplit as urlsplit, urlunparse as urlunparse
from .cookies import cookiejar_from_dict as cookiejar_from_dict, get_cookie_header as get_cookie_header
from .exceptions import ChunkedEncodingError as ChunkedEncodingError, ConnectionError as ConnectionError, ContentDecodingError as ContentDecodingError, HTTPError as HTTPError, InvalidJSONError as InvalidJSONError, InvalidURL as InvalidURL, MissingSchema as MissingSchema, StreamConsumedError as StreamConsumedError
from .hooks import default_hooks as default_hooks
from .status_codes import codes as codes
from .structures import CaseInsensitiveDict as CaseInsensitiveDict
from .utils import check_header_validity as check_header_validity, get_auth_from_url as get_auth_from_url, guess_filename as guess_filename, guess_json_utf as guess_json_utf, iter_slices as iter_slices, parse_header_links as parse_header_links, requote_uri as requote_uri, stream_decode_response_unicode as stream_decode_response_unicode, super_len as super_len, to_key_val_list as to_key_val_list
from _typeshed import Incomplete
from collections.abc import Generator

REDIRECT_STATI: Incomplete
DEFAULT_REDIRECT_LIMIT: int
CONTENT_CHUNK_SIZE: Incomplete
ITER_CHUNK_SIZE: int

class RequestEncodingMixin:
    @property
    def path_url(self):
        """Build the path URL to use."""

class RequestHooksMixin:
    def register_hook(self, event, hook) -> None:
        """Properly register a hook."""
    def deregister_hook(self, event, hook):
        """Deregister a previously registered hook.
        Returns True if the hook existed, False if not.
        """

class Request(RequestHooksMixin):
    """A user-created :class:`Request <Request>` object.

    Used to prepare a :class:`PreparedRequest <PreparedRequest>`, which is sent to the server.

    :param method: HTTP method to use.
    :param url: URL to send.
    :param headers: dictionary of headers to send.
    :param files: dictionary of {filename: fileobject} files to multipart upload.
    :param data: the body to attach to the request. If a dictionary or
        list of tuples ``[(key, value)]`` is provided, form-encoding will
        take place.
    :param json: json for the body to attach to the request (if files or data is not specified).
    :param params: URL parameters to append to the URL. If a dictionary or
        list of tuples ``[(key, value)]`` is provided, form-encoding will
        take place.
    :param auth: Auth handler or (user, pass) tuple.
    :param cookies: dictionary or CookieJar of cookies to attach to this request.
    :param hooks: dictionary of callback hooks, for internal usage.

    Usage::

      >>> import requests
      >>> req = requests.Request('GET', 'https://httpbin.org/get')
      >>> req.prepare()
      <PreparedRequest [GET]>
    """
    hooks: Incomplete
    method: Incomplete
    url: Incomplete
    headers: Incomplete
    files: Incomplete
    data: Incomplete
    json: Incomplete
    params: Incomplete
    auth: Incomplete
    cookies: Incomplete
    def __init__(self, method: Incomplete | None = None, url: Incomplete | None = None, headers: Incomplete | None = None, files: Incomplete | None = None, data: Incomplete | None = None, params: Incomplete | None = None, auth: Incomplete | None = None, cookies: Incomplete | None = None, hooks: Incomplete | None = None, json: Incomplete | None = None) -> None: ...
    def prepare(self):
        """Constructs a :class:`PreparedRequest <PreparedRequest>` for transmission and returns it."""

class PreparedRequest(RequestEncodingMixin, RequestHooksMixin):
    """The fully mutable :class:`PreparedRequest <PreparedRequest>` object,
    containing the exact bytes that will be sent to the server.

    Instances are generated from a :class:`Request <Request>` object, and
    should not be instantiated manually; doing so may produce undesirable
    effects.

    Usage::

      >>> import requests
      >>> req = requests.Request('GET', 'https://httpbin.org/get')
      >>> r = req.prepare()
      >>> r
      <PreparedRequest [GET]>

      >>> s = requests.Session()
      >>> s.send(r)
      <Response [200]>
    """
    method: Incomplete
    url: Incomplete
    headers: Incomplete
    body: Incomplete
    hooks: Incomplete
    def __init__(self) -> None: ...
    def prepare(self, method: Incomplete | None = None, url: Incomplete | None = None, headers: Incomplete | None = None, files: Incomplete | None = None, data: Incomplete | None = None, params: Incomplete | None = None, auth: Incomplete | None = None, cookies: Incomplete | None = None, hooks: Incomplete | None = None, json: Incomplete | None = None) -> None:
        """Prepares the entire request with the given parameters."""
    def copy(self): ...
    def prepare_method(self, method) -> None:
        """Prepares the given HTTP method."""
    def prepare_url(self, url, params) -> None:
        """Prepares the given HTTP URL."""
    def prepare_headers(self, headers) -> None:
        """Prepares the given HTTP headers."""
    def prepare_body(self, data, files, json: Incomplete | None = None) -> None:
        """Prepares the given HTTP body data."""
    def prepare_content_length(self, body) -> None:
        """Prepare Content-Length header based on request method and body"""
    def prepare_auth(self, auth, url: str = '') -> None:
        """Prepares the given HTTP auth data."""
    def prepare_cookies(self, cookies) -> None:
        '''Prepares the given HTTP cookie data.

        This function eventually generates a ``Cookie`` header from the
        given cookies using cookielib. Due to cookielib\'s design, the header
        will not be regenerated if it already exists, meaning this function
        can only be called once for the life of the
        :class:`PreparedRequest <PreparedRequest>` object. Any subsequent calls
        to ``prepare_cookies`` will have no actual effect, unless the "Cookie"
        header is removed beforehand.
        '''
    def prepare_hooks(self, hooks) -> None:
        """Prepares the given hooks."""

class Response:
    """The :class:`Response <Response>` object, which contains a
    server's response to an HTTP request.
    """
    __attrs__: Incomplete
    status_code: Incomplete
    headers: Incomplete
    raw: Incomplete
    url: Incomplete
    encoding: Incomplete
    history: Incomplete
    reason: Incomplete
    cookies: Incomplete
    elapsed: Incomplete
    request: Incomplete
    def __init__(self) -> None: ...
    def __enter__(self): ...
    def __exit__(self, *args) -> None: ...
    def __bool__(self) -> bool:
        """Returns True if :attr:`status_code` is less than 400.

        This attribute checks if the status code of the response is between
        400 and 600 to see if there was a client error or a server error. If
        the status code, is between 200 and 400, this will return True. This
        is **not** a check to see if the response code is ``200 OK``.
        """
    def __nonzero__(self):
        """Returns True if :attr:`status_code` is less than 400.

        This attribute checks if the status code of the response is between
        400 and 600 to see if there was a client error or a server error. If
        the status code, is between 200 and 400, this will return True. This
        is **not** a check to see if the response code is ``200 OK``.
        """
    def __iter__(self):
        """Allows you to use a response as an iterator."""
    @property
    def ok(self):
        """Returns True if :attr:`status_code` is less than 400, False if not.

        This attribute checks if the status code of the response is between
        400 and 600 to see if there was a client error or a server error. If
        the status code is between 200 and 400, this will return True. This
        is **not** a check to see if the response code is ``200 OK``.
        """
    @property
    def is_redirect(self):
        """True if this Response is a well-formed HTTP redirect that could have
        been processed automatically (by :meth:`Session.resolve_redirects`).
        """
    @property
    def is_permanent_redirect(self):
        """True if this Response one of the permanent versions of redirect."""
    @property
    def next(self):
        """Returns a PreparedRequest for the next request in a redirect chain, if there is one."""
    @property
    def apparent_encoding(self):
        """The apparent encoding, provided by the charset_normalizer or chardet libraries."""
    def iter_content(self, chunk_size: int = 1, decode_unicode: bool = False):
        """Iterates over the response data.  When stream=True is set on the
        request, this avoids reading the content at once into memory for
        large responses.  The chunk size is the number of bytes it should
        read into memory.  This is not necessarily the length of each item
        returned as decoding can take place.

        chunk_size must be of type int or None. A value of None will
        function differently depending on the value of `stream`.
        stream=True will read data as it arrives in whatever size the
        chunks are received. If stream=False, data is returned as
        a single chunk.

        If decode_unicode is True, content will be decoded using the best
        available encoding based on the response.
        """
    def iter_lines(self, chunk_size=..., decode_unicode: bool = False, delimiter: Incomplete | None = None) -> Generator[Incomplete, Incomplete, None]:
        """Iterates over the response data, one line at a time.  When
        stream=True is set on the request, this avoids reading the
        content at once into memory for large responses.

        .. note:: This method is not reentrant safe.
        """
    @property
    def content(self):
        """Content of the response, in bytes."""
    @property
    def text(self):
        """Content of the response, in unicode.

        If Response.encoding is None, encoding will be guessed using
        ``charset_normalizer`` or ``chardet``.

        The encoding of the response content is determined based solely on HTTP
        headers, following RFC 2616 to the letter. If you can take advantage of
        non-HTTP knowledge to make a better guess at the encoding, you should
        set ``r.encoding`` appropriately before accessing this property.
        """
    def json(self, **kwargs):
        """Returns the json-encoded content of a response, if any.

        :param \\*\\*kwargs: Optional arguments that ``json.loads`` takes.
        :raises requests.exceptions.JSONDecodeError: If the response body does not
            contain valid json.
        """
    @property
    def links(self):
        """Returns the parsed header links of the response, if any."""
    def raise_for_status(self) -> None:
        """Raises :class:`HTTPError`, if one occurred."""
    def close(self) -> None:
        """Releases the connection back to the pool. Once this method has been
        called the underlying ``raw`` object must not be accessed again.

        *Note: Should not normally need to be called explicitly.*
        """
