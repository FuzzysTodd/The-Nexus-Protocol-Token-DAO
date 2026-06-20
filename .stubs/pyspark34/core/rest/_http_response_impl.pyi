from ..exceptions import HttpResponseError as HttpResponseError, ResponseNotReadError as ResponseNotReadError, StreamClosedError as StreamClosedError, StreamConsumedError as StreamConsumedError
from ..utils._pipeline_transport_rest_shared import BytesIOSocket as BytesIOSocket
from ..utils._utils import case_insensitive_dict as case_insensitive_dict
from ._helpers import decode_to_text as decode_to_text, get_charset_encoding as get_charset_encoding
from ._rest_py3 import HttpRequest as _HttpRequest, HttpResponse as _HttpResponse, _HttpResponseBase
from typing import Any, Iterator, MutableMapping

class _HttpResponseBackcompatMixinBase:
    """Base Backcompat mixin for responses.

    This mixin is used by both sync and async HttpResponse
    backcompat mixins.
    """
    def __getattr__(self, attr): ...
    def __setattr__(self, attr, value) -> None: ...

class HttpResponseBackcompatMixin(_HttpResponseBackcompatMixinBase):
    """Backcompat mixin for sync HttpResponses"""
    def __getattr__(self, attr): ...
    def parts(self):
        """DEPRECATED: Assuming the content-type is multipart/mixed, will return the parts as an async iterator.
        This is deprecated and will be removed in a later release.

        :rtype: Iterator
        :return: The parts of the response
        :raises ValueError: If the content is not multipart/mixed
        """

class _HttpResponseBaseImpl(_HttpResponseBase, _HttpResponseBackcompatMixinBase):
    """Base Implementation class for azure.core.rest.HttpRespone and azure.core.rest.AsyncHttpResponse

    Since the rest responses are abstract base classes, we need to implement them for each of our transport
    responses. This is the base implementation class shared by HttpResponseImpl and AsyncHttpResponseImpl.
    The transport responses will be built on top of HttpResponseImpl and AsyncHttpResponseImpl

    :keyword request: The request that led to the response
    :type request: ~azure.core.rest.HttpRequest
    :keyword any internal_response: The response we get directly from the transport. For example, for our requests
     transport, this will be a requests.Response.
    :keyword optional[int] block_size: The block size we are using in our transport
    :keyword int status_code: The status code of the response
    :keyword str reason: The HTTP reason
    :keyword str content_type: The content type of the response
    :keyword MutableMapping[str, str] headers: The response headers
    :keyword Callable stream_download_generator: The stream download generator that we use to stream the response.
    """
    def __init__(self, **kwargs) -> None: ...
    @property
    def request(self) -> _HttpRequest:
        """The request that resulted in this response.

        :rtype: ~azure.core.rest.HttpRequest
        :return: The request that resulted in this response.
        """
    @property
    def url(self) -> str:
        """The URL that resulted in this response.

        :rtype: str
        :return: The URL that resulted in this response.
        """
    @property
    def is_closed(self) -> bool:
        """Whether the network connection has been closed yet.

        :rtype: bool
        :return: Whether the network connection has been closed yet.
        """
    @property
    def is_stream_consumed(self) -> bool:
        """Whether the stream has been consumed.

        :rtype: bool
        :return: Whether the stream has been consumed.
        """
    @property
    def status_code(self) -> int:
        """The status code of this response.

        :rtype: int
        :return: The status code of this response.
        """
    @property
    def headers(self) -> MutableMapping[str, str]:
        """The response headers.

        :rtype: MutableMapping[str, str]
        :return: The response headers.
        """
    @property
    def content_type(self) -> str | None:
        """The content type of the response.

        :rtype: optional[str]
        :return: The content type of the response.
        """
    @property
    def reason(self) -> str:
        """The reason phrase for this response.

        :rtype: str
        :return: The reason phrase for this response.
        """
    @property
    def encoding(self) -> str | None:
        """Returns the response encoding.

        :return: The response encoding. We either return the encoding set by the user,
         or try extracting the encoding from the response's content type. If all fails,
         we return `None`.
        :rtype: optional[str]
        """
    @encoding.setter
    def encoding(self, value: str) -> None:
        """Sets the response encoding.

        :param str value: Sets the response encoding.
        """
    def text(self, encoding: str | None = None) -> str:
        """Returns the response body as a string

        :param optional[str] encoding: The encoding you want to decode the text with. Can
         also be set independently through our encoding property
        :return: The response's content decoded as a string.
        :rtype: str
        """
    def json(self) -> Any:
        """Returns the whole body as a json object.

        :return: The JSON deserialized response body
        :rtype: any
        :raises json.decoder.JSONDecodeError or ValueError (in python 2.7) if object is not JSON decodable:
        """
    def raise_for_status(self) -> None:
        """Raises an HttpResponseError if the response has an error status code.

        If response is good, does nothing.
        """
    @property
    def content(self) -> bytes:
        """Return the response's content in bytes.

        :return: The response's content in bytes.
        :rtype: bytes
        """

class HttpResponseImpl(_HttpResponseBaseImpl, _HttpResponse, HttpResponseBackcompatMixin):
    """HttpResponseImpl built on top of our HttpResponse protocol class.

    Since ~azure.core.rest.HttpResponse is an abstract base class, we need to
    implement HttpResponse for each of our transports. This is an implementation
    that each of the sync transport responses can be built on.

    :keyword request: The request that led to the response
    :type request: ~azure.core.rest.HttpRequest
    :keyword any internal_response: The response we get directly from the transport. For example, for our requests
     transport, this will be a requests.Response.
    :keyword optional[int] block_size: The block size we are using in our transport
    :keyword int status_code: The status code of the response
    :keyword str reason: The HTTP reason
    :keyword str content_type: The content type of the response
    :keyword MutableMapping[str, str] headers: The response headers
    :keyword Callable stream_download_generator: The stream download generator that we use to stream the response.
    """
    def __enter__(self) -> HttpResponseImpl: ...
    def close(self) -> None: ...
    def __exit__(self, *args) -> None: ...
    def read(self) -> bytes:
        """Read the response's bytes.

        :return: The response's bytes
        :rtype: bytes
        """
    def iter_bytes(self, **kwargs) -> Iterator[bytes]:
        """Iterates over the response's bytes. Will decompress in the process.

        :return: An iterator of bytes from the response
        :rtype: Iterator[str]
        """
    def iter_raw(self, **kwargs) -> Iterator[bytes]:
        """Iterates over the response's bytes. Will not decompress in the process.

        :return: An iterator of bytes from the response
        :rtype: Iterator[str]
        """

class _RestHttpClientTransportResponseBackcompatBaseMixin(_HttpResponseBackcompatMixinBase):
    def body(self): ...

class _RestHttpClientTransportResponseBase(_HttpResponseBaseImpl, _RestHttpClientTransportResponseBackcompatBaseMixin):
    def __init__(self, **kwargs) -> None: ...

class RestHttpClientTransportResponse(_RestHttpClientTransportResponseBase, HttpResponseImpl):
    """Create a Rest HTTPResponse from an http.client response."""
    def iter_bytes(self, **kwargs) -> None: ...
    def iter_raw(self, **kwargs) -> None: ...
    def read(self): ...
