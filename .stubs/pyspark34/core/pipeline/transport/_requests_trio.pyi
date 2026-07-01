from ...rest import AsyncHttpResponse as RestAsyncHttpResponse, HttpRequest as RestHttpRequest
from ._base import HttpRequest as HttpRequest
from ._base_async import AsyncHttpResponse as AsyncHttpResponse
from ._base_requests_async import RequestsAsyncTransportBase as RequestsAsyncTransportBase
from ._requests_basic import AzureErrorUnion as AzureErrorUnion, RequestsTransportResponse as RequestsTransportResponse
from _typeshed import Incomplete
from azure.core.pipeline import Pipeline as Pipeline
from collections.abc import AsyncIterator
from types import TracebackType
from typing import Any, AsyncIterator as AsyncIteratorType, Type, overload

class TrioStreamDownloadGenerator(AsyncIterator):
    """Generator for streaming response data.

    :param pipeline: The pipeline object
    :type pipeline: ~azure.core.pipeline.AsyncPipeline
    :param response: The response object.
    :type response: ~azure.core.pipeline.transport.AsyncHttpResponse
    :keyword bool decompress: If True which is default, will attempt to decode the body based
        on the *content-encoding* header.
    """
    pipeline: Incomplete
    request: Incomplete
    response: Incomplete
    block_size: Incomplete
    iter_content_func: Incomplete
    content_length: Incomplete
    def __init__(self, pipeline: Pipeline, response: AsyncHttpResponse, **kwargs) -> None: ...
    def __len__(self) -> int: ...
    async def __anext__(self): ...

class TrioRequestsTransportResponse(AsyncHttpResponse, RequestsTransportResponse):
    """Asynchronous streaming of data from the response."""
    def stream_download(self, pipeline, **kwargs) -> AsyncIteratorType[bytes]:
        """Generator for streaming response data.

        :param pipeline: The pipeline object
        :type pipeline: ~azure.core.pipeline.AsyncPipeline
        :rtype: AsyncIterator[bytes]
        :return: An async iterator of bytes chunks
        """

class TrioRequestsTransport(RequestsAsyncTransportBase):
    """Identical implementation as the synchronous RequestsTransport wrapped in a class with
    asynchronous methods. Uses the third party trio event loop.

    .. admonition:: Example:

        .. literalinclude:: ../samples/test_example_async.py
            :start-after: [START trio]
            :end-before: [END trio]
            :language: python
            :dedent: 4
            :caption: Asynchronous transport with trio.
    """
    async def __aenter__(self): ...
    async def __aexit__(self, exc_type: Type[BaseException] | None = None, exc_value: BaseException | None = None, traceback: TracebackType | None = None) -> None: ...
    async def sleep(self, duration) -> None: ...
    @overload
    async def send(self, request: HttpRequest, **kwargs: Any) -> AsyncHttpResponse:
        """Send the request using this HTTP sender.

        :param request: The HttpRequest
        :type request: ~azure.core.pipeline.transport.HttpRequest
        :return: The AsyncHttpResponse
        :rtype: ~azure.core.pipeline.transport.AsyncHttpResponse

        :keyword requests.Session session: will override the driver session and use yours.
         Should NOT be done unless really required. Anything else is sent straight to requests.
        :keyword dict proxies: will define the proxy to use. Proxy is a dict (protocol, url)
        """
    @overload
    async def send(self, request: RestHttpRequest, **kwargs: Any) -> RestAsyncHttpResponse:
        """Send an `azure.core.rest` request using this HTTP sender.

        :param request: The HttpRequest
        :type request: ~azure.core.rest.HttpRequest
        :return: The AsyncHttpResponse
        :rtype: ~azure.core.rest.AsyncHttpResponse

        :keyword requests.Session session: will override the driver session and use yours.
         Should NOT be done unless really required. Anything else is sent straight to requests.
        :keyword dict proxies: will define the proxy to use. Proxy is a dict (protocol, url)
        """
