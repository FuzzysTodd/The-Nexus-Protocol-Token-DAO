import abc
from ..utils._utils import case_insensitive_dict as case_insensitive_dict
from ._helpers import FilesType as FilesType, HttpRequestBackcompatMixin as HttpRequestBackcompatMixin, ParamsType as ParamsType, set_content_body as set_content_body, set_json_body as set_json_body, set_multipart_body as set_multipart_body, set_urlencoded_body as set_urlencoded_body
from _typeshed import Incomplete
from typing import Any, AsyncContextManager, AsyncIterable, AsyncIterator, Dict, Iterable, Iterator, MutableMapping

ContentType = str | bytes | Iterable[bytes] | AsyncIterable[bytes]

class HttpRequest(HttpRequestBackcompatMixin):
    """An HTTP request.

    It should be passed to your client's `send_request` method.

    >>> from azure.core.rest import HttpRequest
    >>> request = HttpRequest('GET', 'http://www.example.com')
    <HttpRequest [GET], url: 'http://www.example.com'>
    >>> response = client.send_request(request)
    <HttpResponse: 200 OK>

    :param str method: HTTP method (GET, HEAD, etc.)
    :param str url: The url for your request
    :keyword mapping params: Query parameters to be mapped into your URL. Your input
     should be a mapping of query name to query value(s).
    :keyword mapping headers: HTTP headers you want in your request. Your input should
     be a mapping of header name to header value.
    :keyword any json: A JSON serializable object. We handle JSON-serialization for your
     object, so use this for more complicated data structures than `data`.
    :keyword content: Content you want in your request body. Think of it as the kwarg you should input
     if your data doesn't fit into `json`, `data`, or `files`. Accepts a bytes type, or a generator
     that yields bytes.
    :paramtype content: str or bytes or iterable[bytes] or asynciterable[bytes]
    :keyword dict data: Form data you want in your request body. Use for form-encoded data, i.e.
     HTML forms.
    :keyword mapping files: Files you want to in your request body. Use for uploading files with
     multipart encoding. Your input should be a mapping of file name to file content.
     Use the `data` kwarg in addition if you want to include non-file data files as part of your request.
    :ivar str url: The URL this request is against.
    :ivar str method: The method type of this request.
    :ivar mapping headers: The HTTP headers you passed in to your request
    :ivar any content: The content passed in for the request
    """
    url: Incomplete
    method: Incomplete
    headers: Incomplete
    def __init__(self, method: str, url: str, *, params: ParamsType | None = None, headers: MutableMapping[str, str] | None = None, json: Any = None, content: ContentType | None = None, data: Dict[str, Any] | None = None, files: FilesType | None = None, **kwargs: Any) -> None: ...
    @property
    def content(self) -> Any:
        """Get's the request's content

        :return: The request's content
        :rtype: any
        """
    def __deepcopy__(self, memo: Dict[int, Any] | None = None) -> HttpRequest: ...

class _HttpResponseBase(abc.ABC, metaclass=abc.ABCMeta):
    """Base abstract base class for HttpResponses."""
    @property
    @abc.abstractmethod
    def request(self) -> HttpRequest:
        """The request that resulted in this response.

        :rtype: ~azure.core.rest.HttpRequest
        :return: The request that resulted in this response.
        """
    @property
    @abc.abstractmethod
    def status_code(self) -> int:
        """The status code of this response.

        :rtype: int
        :return: The status code of this response.
        """
    @property
    @abc.abstractmethod
    def headers(self) -> MutableMapping[str, str]:
        """The response headers. Must be case-insensitive.

        :rtype: MutableMapping[str, str]
        :return: The response headers. Must be case-insensitive.
        """
    @property
    @abc.abstractmethod
    def reason(self) -> str:
        """The reason phrase for this response.

        :rtype: str
        :return: The reason phrase for this response.
        """
    @property
    @abc.abstractmethod
    def content_type(self) -> str | None:
        """The content type of the response.

        :rtype: str
        :return: The content type of the response.
        """
    @property
    @abc.abstractmethod
    def is_closed(self) -> bool:
        """Whether the network connection has been closed yet.

        :rtype: bool
        :return: Whether the network connection has been closed yet.
        """
    @property
    @abc.abstractmethod
    def is_stream_consumed(self) -> bool:
        """Whether the stream has been consumed.

        :rtype: bool
        :return: Whether the stream has been consumed.
        """
    @property
    @abc.abstractmethod
    def encoding(self) -> str | None:
        """Returns the response encoding.

        :return: The response encoding. We either return the encoding set by the user,
         or try extracting the encoding from the response's content type. If all fails,
         we return `None`.
        :rtype: optional[str]
        """
    @encoding.setter
    def encoding(self, value: str | None) -> None:
        """Sets the response encoding.

        :param optional[str] value: The encoding to set
        """
    @property
    @abc.abstractmethod
    def url(self) -> str:
        """The URL that resulted in this response.

        :rtype: str
        :return: The URL that resulted in this response.
        """
    @property
    @abc.abstractmethod
    def content(self) -> bytes:
        """Return the response's content in bytes.

        :rtype: bytes
        :return: The response's content in bytes.
        """
    @abc.abstractmethod
    def text(self, encoding: str | None = None) -> str:
        """Returns the response body as a string.

        :param optional[str] encoding: The encoding you want to decode the text with. Can
         also be set independently through our encoding property
        :return: The response's content decoded as a string.
        :rtype: str
        """
    @abc.abstractmethod
    def json(self) -> Any:
        """Returns the whole body as a json object.

        :return: The JSON deserialized response body
        :rtype: any
        :raises json.decoder.JSONDecodeError or ValueError (in python 2.7) if object is not JSON decodable:
        """
    @abc.abstractmethod
    def raise_for_status(self) -> None:
        """Raises an HttpResponseError if the response has an error status code.

        If response is good, does nothing.

        :raises ~azure.core.HttpResponseError if the object has an error status code.:
        """

class HttpResponse(_HttpResponseBase, metaclass=abc.ABCMeta):
    """Abstract base class for HTTP responses.

    Use this abstract base class to create your own transport responses.

    Responses implementing this ABC are returned from your client's `send_request` method
    if you pass in an :class:`~azure.core.rest.HttpRequest`

    >>> from azure.core.rest import HttpRequest
    >>> request = HttpRequest('GET', 'http://www.example.com')
    <HttpRequest [GET], url: 'http://www.example.com'>
    >>> response = client.send_request(request)
    <HttpResponse: 200 OK>
    """
    @abc.abstractmethod
    def __enter__(self) -> HttpResponse: ...
    @abc.abstractmethod
    def __exit__(self, *args: Any) -> None: ...
    @abc.abstractmethod
    def close(self) -> None: ...
    @abc.abstractmethod
    def read(self) -> bytes:
        """Read the response's bytes.

        :return: The read in bytes
        :rtype: bytes
        """
    @abc.abstractmethod
    def iter_raw(self, **kwargs: Any) -> Iterator[bytes]:
        """Iterates over the response's bytes. Will not decompress in the process.

        :return: An iterator of bytes from the response
        :rtype: Iterator[str]
        """
    @abc.abstractmethod
    def iter_bytes(self, **kwargs: Any) -> Iterator[bytes]:
        """Iterates over the response's bytes. Will decompress in the process.

        :return: An iterator of bytes from the response
        :rtype: Iterator[str]
        """

class AsyncHttpResponse(_HttpResponseBase, AsyncContextManager['AsyncHttpResponse'], metaclass=abc.ABCMeta):
    """Abstract base class for Async HTTP responses.

    Use this abstract base class to create your own transport responses.

    Responses implementing this ABC are returned from your async client's `send_request`
    method if you pass in an :class:`~azure.core.rest.HttpRequest`

    >>> from azure.core.rest import HttpRequest
    >>> request = HttpRequest('GET', 'http://www.example.com')
    <HttpRequest [GET], url: 'http://www.example.com'>
    >>> response = await client.send_request(request)
    <AsyncHttpResponse: 200 OK>
    """
    @abc.abstractmethod
    async def read(self) -> bytes:
        """Read the response's bytes into memory.

        :return: The response's bytes
        :rtype: bytes
        """
    @abc.abstractmethod
    async def iter_raw(self, **kwargs: Any) -> AsyncIterator[bytes]:
        """Asynchronously iterates over the response's bytes. Will not decompress in the process.

        :return: An async iterator of bytes from the response
        :rtype: AsyncIterator[bytes]
        """
    @abc.abstractmethod
    async def iter_bytes(self, **kwargs: Any) -> AsyncIterator[bytes]:
        """Asynchronously iterates over the response's bytes. Will decompress in the process.

        :return: An async iterator of bytes from the response
        :rtype: AsyncIterator[bytes]
        """
    @abc.abstractmethod
    async def close(self) -> None: ...
