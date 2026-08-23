from . import HttpRequest as HttpRequest
from ...rest import HttpRequest as RestHttpRequest, HttpResponse as RestHttpResponse
from ._base import HttpResponse as HttpResponse, HttpTransport as HttpTransport, _HttpResponseBase
from ._bigger_block_size_http_adapters import BiggerBlockSizeHTTPAdapter as BiggerBlockSizeHTTPAdapter
from _typeshed import Incomplete
from azure.core.exceptions import HttpResponseError, IncompleteReadError, ServiceRequestError, ServiceResponseError
from typing import Iterator, TypeVar, overload

AzureErrorUnion = ServiceRequestError | ServiceResponseError | IncompleteReadError | HttpResponseError
PipelineType = TypeVar('PipelineType')

class _RequestsTransportResponseBase(_HttpResponseBase):
    """Base class for accessing response data.

    :param HttpRequest request: The request.
    :param requests_response: The object returned from the HTTP library.
    :type requests_response: requests.Response
    :param int block_size: Size in bytes.
    """
    status_code: Incomplete
    headers: Incomplete
    reason: Incomplete
    content_type: Incomplete
    def __init__(self, request, requests_response, block_size: Incomplete | None = None) -> None: ...
    def body(self): ...
    def text(self, encoding: str | None = None) -> str:
        """Return the whole body as a string.

        If encoding is not provided, mostly rely on requests auto-detection, except
        for BOM, that requests ignores. If we see a UTF8 BOM, we assumes UTF8 unlike requests.

        :param str encoding: The encoding to apply.
        :rtype: str
        :return: The body as text.
        """

class StreamDownloadGenerator:
    """Generator for streaming response data.

    :param pipeline: The pipeline object
    :type pipeline: ~azure.core.pipeline.Pipeline
    :param response: The response object.
    :type response: ~azure.core.pipeline.transport.HttpResponse
    :keyword bool decompress: If True which is default, will attempt to decode the body based
        on the *content-encoding* header.
    """
    pipeline: Incomplete
    request: Incomplete
    response: Incomplete
    block_size: Incomplete
    iter_content_func: Incomplete
    content_length: Incomplete
    def __init__(self, pipeline, response, **kwargs) -> None: ...
    def __len__(self) -> int: ...
    def __iter__(self): ...
    def __next__(self): ...
    next = __next__

class RequestsTransportResponse(HttpResponse, _RequestsTransportResponseBase):
    """Streaming of data from the response."""
    def stream_download(self, pipeline: PipelineType, **kwargs) -> Iterator[bytes]:
        """Generator for streaming request body data.

        :param pipeline: The pipeline object
        :type pipeline: ~azure.core.pipeline.Pipeline
        :rtype: iterator[bytes]
        :return: The stream of data
        """

class RequestsTransport(HttpTransport):
    '''Implements a basic requests HTTP sender.

    Since requests team recommends to use one session per requests, you should
    not consider this class as thread-safe, since it will use one Session
    per instance.

    In this simple implementation:
    - You provide the configured session if you want to, or a basic session is created.
    - All kwargs received by "send" are sent to session.request directly

    :keyword requests.Session session: Request session to use instead of the default one.
    :keyword bool session_owner: Decide if the session provided by user is owned by this transport. Default to True.
    :keyword bool use_env_settings: Uses proxy settings from environment. Defaults to True.

    .. admonition:: Example:

        .. literalinclude:: ../samples/test_example_sync.py
            :start-after: [START requests]
            :end-before: [END requests]
            :language: python
            :dedent: 4
            :caption: Synchronous transport with Requests.
    '''
    session: Incomplete
    connection_config: Incomplete
    def __init__(self, **kwargs) -> None: ...
    def __enter__(self) -> RequestsTransport: ...
    def __exit__(self, *args) -> None: ...
    def open(self) -> None: ...
    def close(self) -> None: ...
    @overload
    def send(self, request: HttpRequest, **kwargs) -> HttpResponse:
        """Send a rest request and get back a rest response.

        :param request: The request object to be sent.
        :type request: ~azure.core.pipeline.transport.HttpRequest
        :return: An HTTPResponse object.
        :rtype: ~azure.core.pipeline.transport.HttpResponse

        :keyword requests.Session session: will override the driver session and use yours.
         Should NOT be done unless really required. Anything else is sent straight to requests.
        :keyword dict proxies: will define the proxy to use. Proxy is a dict (protocol, url)
        """
    @overload
    def send(self, request: RestHttpRequest, **kwargs) -> RestHttpResponse:
        """Send an `azure.core.rest` request and get back a rest response.

        :param request: The request object to be sent.
        :type request: ~azure.core.rest.HttpRequest
        :return: An HTTPResponse object.
        :rtype: ~azure.core.rest.HttpResponse

        :keyword requests.Session session: will override the driver session and use yours.
         Should NOT be done unless really required. Anything else is sent straight to requests.
        :keyword dict proxies: will define the proxy to use. Proxy is a dict (protocol, url)
        """
