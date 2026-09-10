import io
from . import util as util
from ._collections import HTTPHeaderDict as HTTPHeaderDict
from .connection import BaseSSLError as BaseSSLError, HTTPException as HTTPException
from .exceptions import BodyNotHttplibCompatible as BodyNotHttplibCompatible, DecodeError as DecodeError, HTTPError as HTTPError, IncompleteRead as IncompleteRead, InvalidChunkLength as InvalidChunkLength, InvalidHeader as InvalidHeader, ProtocolError as ProtocolError, ReadTimeoutError as ReadTimeoutError, ResponseNotChunked as ResponseNotChunked, SSLError as SSLError
from .util.response import is_fp_closed as is_fp_closed, is_response_to_head as is_response_to_head
from _typeshed import Incomplete
from collections.abc import Generator

log: Incomplete

class DeflateDecoder:
    def __init__(self) -> None: ...
    def __getattr__(self, name): ...
    def decompress(self, data): ...

class GzipDecoderState:
    FIRST_MEMBER: int
    OTHER_MEMBERS: int
    SWALLOW_DATA: int

class GzipDecoder:
    def __init__(self) -> None: ...
    def __getattr__(self, name): ...
    def decompress(self, data): ...

class BrotliDecoder:
    decompress: Incomplete
    def __init__(self) -> None: ...
    def flush(self): ...

class MultiDecoder:
    """
    From RFC7231:
        If one or more encodings have been applied to a representation, the
        sender that applied the encodings MUST generate a Content-Encoding
        header field that lists the content codings in the order in which
        they were applied.
    """
    def __init__(self, modes) -> None: ...
    def flush(self): ...
    def decompress(self, data): ...

class HTTPResponse(io.IOBase):
    """
    HTTP Response container.

    Backwards-compatible with :class:`http.client.HTTPResponse` but the response ``body`` is
    loaded and decoded on-demand when the ``data`` property is accessed.  This
    class is also compatible with the Python standard library's :mod:`io`
    module, and can hence be treated as a readable object in the context of that
    framework.

    Extra parameters for behaviour not present in :class:`http.client.HTTPResponse`:

    :param preload_content:
        If True, the response's body will be preloaded during construction.

    :param decode_content:
        If True, will attempt to decode the body based on the
        'content-encoding' header.

    :param original_response:
        When this HTTPResponse wrapper is generated from an :class:`http.client.HTTPResponse`
        object, it's convenient to include the original for debug purposes. It's
        otherwise unused.

    :param retries:
        The retries contains the last :class:`~urllib3.util.retry.Retry` that
        was used during the request.

    :param enforce_content_length:
        Enforce content length checking. Body returned by server must match
        value of Content-Length header, if present. Otherwise, raise error.
    """
    CONTENT_DECODERS: Incomplete
    REDIRECT_STATUSES: Incomplete
    headers: Incomplete
    status: Incomplete
    version: Incomplete
    reason: Incomplete
    strict: Incomplete
    decode_content: Incomplete
    retries: Incomplete
    enforce_content_length: Incomplete
    auto_close: Incomplete
    msg: Incomplete
    chunked: bool
    chunk_left: Incomplete
    length_remaining: Incomplete
    def __init__(self, body: str = '', headers: Incomplete | None = None, status: int = 0, version: int = 0, reason: Incomplete | None = None, strict: int = 0, preload_content: bool = True, decode_content: bool = True, original_response: Incomplete | None = None, pool: Incomplete | None = None, connection: Incomplete | None = None, msg: Incomplete | None = None, retries: Incomplete | None = None, enforce_content_length: bool = False, request_method: Incomplete | None = None, request_url: Incomplete | None = None, auto_close: bool = True) -> None: ...
    def get_redirect_location(self):
        """
        Should we redirect and where to?

        :returns: Truthy redirect location string if we got a redirect status
            code and valid location. ``None`` if redirect status and no
            location. ``False`` if not a redirect status code.
        """
    def release_conn(self) -> None: ...
    def drain_conn(self) -> None:
        """
        Read and discard any remaining HTTP response data in the response connection.

        Unread data in the HTTPResponse connection blocks the connection from being released back to the pool.
        """
    @property
    def data(self): ...
    @property
    def connection(self): ...
    def isclosed(self): ...
    def tell(self):
        """
        Obtain the number of bytes pulled over the wire so far. May differ from
        the amount of content returned by :meth:``urllib3.response.HTTPResponse.read``
        if bytes are encoded on the wire (e.g, compressed).
        """
    DECODER_ERROR_CLASSES: Incomplete
    def read(self, amt: Incomplete | None = None, decode_content: Incomplete | None = None, cache_content: bool = False):
        """
        Similar to :meth:`http.client.HTTPResponse.read`, but with two additional
        parameters: ``decode_content`` and ``cache_content``.

        :param amt:
            How much of the content to read. If specified, caching is skipped
            because it doesn't make sense to cache partial content as the full
            response.

        :param decode_content:
            If True, will attempt to decode the body based on the
            'content-encoding' header.

        :param cache_content:
            If True, will save the returned data such that the same result is
            returned despite of the state of the underlying file object. This
            is useful if you want the ``.data`` property to continue working
            after having ``.read()`` the file object. (Overridden if ``amt`` is
            set.)
        """
    def stream(self, amt=..., decode_content: Incomplete | None = None) -> Generator[Incomplete, None, None]:
        """
        A generator wrapper for the read() method. A call will block until
        ``amt`` bytes have been read from the connection or until the
        connection is closed.

        :param amt:
            How much of the content to read. The generator will return up to
            much data per iteration, but may return less. This is particularly
            likely when using compressed data. However, the empty string will
            never be returned.

        :param decode_content:
            If True, will attempt to decode the body based on the
            'content-encoding' header.
        """
    @classmethod
    def from_httplib(ResponseCls, r, **response_kw):
        """
        Given an :class:`http.client.HTTPResponse` instance ``r``, return a
        corresponding :class:`urllib3.response.HTTPResponse` object.

        Remaining parameters are passed to the HTTPResponse constructor, along
        with ``original_response=r``.
        """
    def getheaders(self): ...
    def getheader(self, name, default: Incomplete | None = None): ...
    def info(self): ...
    def close(self) -> None: ...
    @property
    def closed(self): ...
    def fileno(self): ...
    def flush(self): ...
    def readable(self): ...
    def readinto(self, b): ...
    def supports_chunked_reads(self):
        """
        Checks if the underlying file-like object looks like a
        :class:`http.client.HTTPResponse` object. We do this by testing for
        the fp attribute. If it is present we assume it returns raw chunks as
        processed by read_chunked().
        """
    def read_chunked(self, amt: Incomplete | None = None, decode_content: Incomplete | None = None) -> Generator[Incomplete, None, None]:
        """
        Similar to :meth:`HTTPResponse.read`, but with an additional
        parameter: ``decode_content``.

        :param amt:
            How much of the content to read. If specified, caching is skipped
            because it doesn't make sense to cache partial content as the full
            response.

        :param decode_content:
            If True, will attempt to decode the body based on the
            'content-encoding' header.
        """
    def geturl(self):
        """
        Returns the URL that was the source of this response.
        If the request that generated this response redirected, this method
        will return the final redirect location.
        """
    def __iter__(self): ...
