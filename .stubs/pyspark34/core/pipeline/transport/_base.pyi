import abc
from ...utils._pipeline_transport_rest_shared import BytesIOSocket as BytesIOSocket
from ...utils._utils import case_insensitive_dict as case_insensitive_dict
from _typeshed import Incomplete
from azure.core.pipeline import Pipeline as Pipeline
from typing import Any, ContextManager, Dict, Generic, Iterator, Mapping, TypeVar

HTTPResponseType = TypeVar('HTTPResponseType')
HTTPRequestType = TypeVar('HTTPRequestType')
DataType = bytes | str | Dict[str, str | int]
binary_type = str

class HttpTransport(ContextManager['HttpTransport'], abc.ABC, Generic[HTTPRequestType, HTTPResponseType], metaclass=abc.ABCMeta):
    """An http sender ABC."""
    @abc.abstractmethod
    def send(self, request: HTTPRequestType, **kwargs: Any) -> HTTPResponseType:
        """Send the request using this HTTP sender.

        :param request: The pipeline request object
        :type request: ~azure.core.transport.HTTPRequest
        :return: The pipeline response object.
        :rtype: ~azure.core.pipeline.transport.HttpResponse
        """
    @abc.abstractmethod
    def open(self) -> None:
        """Assign new session if one does not already exist."""
    @abc.abstractmethod
    def close(self) -> None:
        """Close the session if it is not externally owned."""
    def sleep(self, duration: float) -> None:
        """Sleep for the specified duration.

        You should always ask the transport to sleep, and not call directly
        the stdlib. This is mostly important in async, as the transport
        may not use asyncio but other implementations like trio and they have their own
        way to sleep, but to keep design
        consistent, it's cleaner to always ask the transport to sleep and let the transport
        implementor decide how to do it.

        :param float duration: The number of seconds to sleep.
        """

class HttpRequest:
    '''Represents an HTTP request.

    URL can be given without query parameters, to be added later using "format_parameters".

    :param str method: HTTP method (GET, HEAD, etc.)
    :param str url: At least complete scheme/host/path
    :param dict[str,str] headers: HTTP headers
    :param files: Dictionary of ``\'name\': file-like-objects`` (or ``{\'name\': file-tuple}``) for multipart
        encoding upload. ``file-tuple`` can be a 2-tuple ``(\'filename\', fileobj)``, 3-tuple
        ``(\'filename\', fileobj, \'content_type\')`` or a 4-tuple
        ``(\'filename\', fileobj, \'content_type\', custom_headers)``, where ``\'content_type\'`` is a string
        defining the content type of the given file and ``custom_headers``
        a dict-like object containing additional headers to add for the file.
    :type files: dict[str, tuple[str, IO, str, dict]] or dict[str, IO]
    :param data: Body to be sent.
    :type data: bytes or dict (for form)
    '''
    method: Incomplete
    url: Incomplete
    headers: Incomplete
    files: Incomplete
    data: Incomplete
    multipart_mixed_info: Incomplete
    def __init__(self, method: str, url: str, headers: Mapping[str, str] | None = None, files: Any | None = None, data: DataType | None = None) -> None: ...
    def __deepcopy__(self, memo: Dict[int, Any] | None = None) -> HttpRequest: ...
    @property
    def query(self) -> Dict[str, str]:
        """The query parameters of the request as a dict.

        :rtype: dict[str, str]
        :return: The query parameters of the request as a dict.
        """
    @property
    def body(self) -> DataType | None:
        """Alias to data.

        :rtype: bytes or str or dict or None
        :return: The body of the request.
        """
    @body.setter
    def body(self, value: DataType | None) -> None: ...
    def format_parameters(self, params: Dict[str, str]) -> None:
        """Format parameters into a valid query string.
        It's assumed all parameters have already been quoted as
        valid URL strings.

        :param dict params: A dictionary of parameters.
        """
    def set_streamed_data_body(self, data: Any) -> None:
        """Set a streamable data body.

        :param data: The request field data.
        :type data: stream or generator or asyncgenerator
        """
    def set_text_body(self, data: str) -> None:
        """Set a text as body of the request.

        :param data: A text to send as body.
        :type data: str
        """
    def set_xml_body(self, data: Any) -> None:
        """Set an XML element tree as the body of the request.

        :param data: The request field data.
        :type data: XML node
        """
    def set_json_body(self, data: Any) -> None:
        """Set a JSON-friendly object as the body of the request.

        :param data: A JSON serializable object
        :type data: dict
        """
    def set_formdata_body(self, data: Dict[str, str] | None = None) -> None:
        """Set form-encoded data as the body of the request.

        :param data: The request field data.
        :type data: dict
        """
    def set_bytes_body(self, data: bytes) -> None:
        """Set generic bytes as the body of the request.

        Will set content-length.

        :param data: The request field data.
        :type data: bytes
        """
    def set_multipart_mixed(self, *requests: HttpRequest, **kwargs: Any) -> None:
        """Set the part of a multipart/mixed.

        Only supported args for now are HttpRequest objects.

        boundary is optional, and one will be generated if you don't provide one.
        Note that no verification are made on the boundary, this is considered advanced
        enough so you know how to respect RFC1341 7.2.1 and provide a correct boundary.

        Any additional kwargs will be passed into the pipeline context for per-request policy
        configuration.

        :param requests: The requests to add to the multipart/mixed
        :type requests: ~azure.core.pipeline.transport.HttpRequest
        :keyword list[SansIOHTTPPolicy] policies: SansIOPolicy to apply at preparation time
        :keyword str boundary: Optional boundary
        """
    def prepare_multipart_body(self, content_index: int = 0) -> int:
        '''Will prepare the body of this request according to the multipart information.

        This call assumes the on_request policies have been applied already in their
        correct context (sync/async)

        Does nothing if "set_multipart_mixed" was never called.

        :param int content_index: The current index of parts within the batch message.
        :returns: The updated index after all parts in this request have been added.
        :rtype: int
        '''
    def serialize(self) -> bytes:
        """Serialize this request using application/http spec.

        :rtype: bytes
        :return: The requests serialized as HTTP low-level message in bytes.
        """

class _HttpResponseBase:
    '''Represent a HTTP response.

    No body is defined here on purpose, since async pipeline
    will provide async ways to access the body
    Full in-memory using "body" as bytes.

    :param request: The request.
    :type request: ~azure.core.pipeline.transport.HttpRequest
    :param internal_response: The object returned from the HTTP library.
    :type internal_response: any
    :param int block_size: Defaults to 4096 bytes.
    '''
    request: Incomplete
    internal_response: Incomplete
    status_code: Incomplete
    headers: Incomplete
    reason: Incomplete
    content_type: Incomplete
    block_size: Incomplete
    def __init__(self, request: HttpRequest, internal_response: Any, block_size: int | None = None) -> None: ...
    def body(self) -> bytes:
        """Return the whole body as bytes in memory.

        Sync implementer should load the body in memory if they can.
        Async implementer should rely on async load_body to have been called first.

        :rtype: bytes
        :return: The whole body as bytes in memory.
        """
    def text(self, encoding: str | None = None) -> str:
        '''Return the whole body as a string.

        .. seealso:: ~body()

        :param str encoding: The encoding to apply. If None, use "utf-8" with BOM parsing (utf-8-sig).
         Implementation can be smarter if they want (using headers or chardet).
        :rtype: str
        :return: The whole body as a string.
        '''
    def raise_for_status(self) -> None:
        """Raises an HttpResponseError if the response has an error status code.
        If response is good, does nothing.
        """

class HttpResponse(_HttpResponseBase):
    def stream_download(self, pipeline: Pipeline[HttpRequest, 'HttpResponse'], **kwargs: Any) -> Iterator[bytes]:
        """Generator for streaming request body data.

        Should be implemented by sub-classes if streaming download
        is supported.

        :param pipeline: The pipeline object
        :type pipeline: ~azure.core.pipeline.Pipeline
        :rtype: iterator[bytes]
        :return: The generator of bytes connected to the socket
        """
    def parts(self) -> Iterator['HttpResponse']:
        """Assuming the content-type is multipart/mixed, will return the parts as an iterator.

        :rtype: iterator[HttpResponse]
        :return: The iterator of HttpResponse if request was multipart/mixed
        :raises ValueError: If the content is not multipart/mixed
        """

class _HttpClientTransportResponse(_HttpResponseBase):
    '''Create a HTTPResponse from an http.client response.

    Body will NOT be read by the constructor. Call "body()" to load the body in memory if necessary.

    :param HttpRequest request: The request.
    :param httpclient_response: The object returned from an HTTP(S)Connection from http.client
    :type httpclient_response: http.client.HTTPResponse
    '''
    status_code: Incomplete
    headers: Incomplete
    reason: Incomplete
    content_type: Incomplete
    data: Incomplete
    def __init__(self, request, httpclient_response) -> None: ...
    def body(self): ...

class HttpClientTransportResponse(_HttpClientTransportResponse, HttpResponse):
    '''Create a HTTPResponse from an http.client response.

    Body will NOT be read by the constructor. Call "body()" to load the body in memory if necessary.
    '''

class PipelineClientBase:
    """Base class for pipeline clients.

    :param str base_url: URL for the request.
    """
    def __init__(self, base_url: str) -> None: ...
    def format_url(self, url_template: str, **kwargs: Any) -> str:
        """Format request URL with the client base URL, unless the
        supplied URL is already absolute.

        Note that both the base url and the template url can contain query parameters.

        :param str url_template: The request URL to be formatted if necessary.
        :rtype: str
        :return: The formatted URL.
        """
    def get(self, url: str, params: Dict[str, str] | None = None, headers: Dict[str, str] | None = None, content: Any = None, form_content: Dict[str, Any] | None = None) -> HttpRequest:
        """Create a GET request object.

        :param str url: The request URL.
        :param dict params: Request URL parameters.
        :param dict headers: Headers
        :param content: The body content
        :type content: bytes or str or dict
        :param dict form_content: Form content
        :return: An HttpRequest object
        :rtype: ~azure.core.pipeline.transport.HttpRequest
        """
    def put(self, url: str, params: Dict[str, str] | None = None, headers: Dict[str, str] | None = None, content: Any = None, form_content: Dict[str, Any] | None = None, stream_content: Any = None) -> HttpRequest:
        """Create a PUT request object.

        :param str url: The request URL.
        :param dict params: Request URL parameters.
        :param dict headers: Headers
        :param content: The body content
        :type content: bytes or str or dict
        :param dict form_content: Form content
        :param stream_content: The body content as a stream
        :type stream_content: stream or generator or asyncgenerator
        :return: An HttpRequest object
        :rtype: ~azure.core.pipeline.transport.HttpRequest
        """
    def post(self, url: str, params: Dict[str, str] | None = None, headers: Dict[str, str] | None = None, content: Any = None, form_content: Dict[str, Any] | None = None, stream_content: Any = None) -> HttpRequest:
        """Create a POST request object.

        :param str url: The request URL.
        :param dict params: Request URL parameters.
        :param dict headers: Headers
        :param content: The body content
        :type content: bytes or str or dict
        :param dict form_content: Form content
        :param stream_content: The body content as a stream
        :type stream_content: stream or generator or asyncgenerator
        :return: An HttpRequest object
        :rtype: ~azure.core.pipeline.transport.HttpRequest
        """
    def head(self, url: str, params: Dict[str, str] | None = None, headers: Dict[str, str] | None = None, content: Any = None, form_content: Dict[str, Any] | None = None, stream_content: Any = None) -> HttpRequest:
        """Create a HEAD request object.

        :param str url: The request URL.
        :param dict params: Request URL parameters.
        :param dict headers: Headers
        :param content: The body content
        :type content: bytes or str or dict
        :param dict form_content: Form content
        :param stream_content: The body content as a stream
        :type stream_content: stream or generator or asyncgenerator
        :return: An HttpRequest object
        :rtype: ~azure.core.pipeline.transport.HttpRequest
        """
    def patch(self, url: str, params: Dict[str, str] | None = None, headers: Dict[str, str] | None = None, content: Any = None, form_content: Dict[str, Any] | None = None, stream_content: Any = None) -> HttpRequest:
        """Create a PATCH request object.

        :param str url: The request URL.
        :param dict params: Request URL parameters.
        :param dict headers: Headers
        :param content: The body content
        :type content: bytes or str or dict
        :param dict form_content: Form content
        :param stream_content: The body content as a stream
        :type stream_content: stream or generator or asyncgenerator
        :return: An HttpRequest object
        :rtype: ~azure.core.pipeline.transport.HttpRequest
        """
    def delete(self, url: str, params: Dict[str, str] | None = None, headers: Dict[str, str] | None = None, content: Any = None, form_content: Dict[str, Any] | None = None) -> HttpRequest:
        """Create a DELETE request object.

        :param str url: The request URL.
        :param dict params: Request URL parameters.
        :param dict headers: Headers
        :param content: The body content
        :type content: bytes or str or dict
        :param dict form_content: Form content
        :return: An HttpRequest object
        :rtype: ~azure.core.pipeline.transport.HttpRequest
        """
    def merge(self, url: str, params: Dict[str, str] | None = None, headers: Dict[str, str] | None = None, content: Any = None, form_content: Dict[str, Any] | None = None) -> HttpRequest:
        """Create a MERGE request object.

        :param str url: The request URL.
        :param dict params: Request URL parameters.
        :param dict headers: Headers
        :param content: The body content
        :type content: bytes or str or dict
        :param dict form_content: Form content
        :return: An HttpRequest object
        :rtype: ~azure.core.pipeline.transport.HttpRequest
        """
    def options(self, url: str, params: Dict[str, str] | None = None, headers: Dict[str, str] | None = None, **kwargs: Any) -> HttpRequest:
        """Create a OPTIONS request object.

        :param str url: The request URL.
        :param dict params: Request URL parameters.
        :param dict headers: Headers
        :keyword content: The body content
        :type content: bytes or str or dict
        :keyword dict form_content: Form content
        :return: An HttpRequest object
        :rtype: ~azure.core.pipeline.transport.HttpRequest
        """
