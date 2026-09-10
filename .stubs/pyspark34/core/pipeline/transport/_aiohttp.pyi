import aiohttp
from ...rest import AsyncHttpResponse as RestAsyncHttpResponse, HttpRequest as RestHttpRequest
from ...rest._aiohttp import RestAioHttpTransportResponse as RestAioHttpTransportResponse
from ._base import HttpRequest as HttpRequest
from ._base_async import AsyncHttpResponse as AsyncHttpResponse, AsyncHttpTransport as AsyncHttpTransport
from _typeshed import Incomplete
from azure.core.pipeline import AsyncPipeline as AsyncPipeline
from collections.abc import AsyncIterator
from types import TracebackType
from typing import Any, AsyncIterator as AsyncIteratorType, Type, overload

CONTENT_CHUNK_SIZE: Incomplete

class AioHttpTransport(AsyncHttpTransport):
    """AioHttp HTTP sender implementation.

    Fully asynchronous implementation using the aiohttp library.

    :keyword session: The client session.
    :paramtype session: ~aiohttp.ClientSession
    :keyword bool session_owner: Session owner. Defaults True.

    :keyword bool use_env_settings: Uses proxy settings from environment. Defaults to True.

    .. admonition:: Example:

        .. literalinclude:: ../samples/test_example_async.py
            :start-after: [START aiohttp]
            :end-before: [END aiohttp]
            :language: python
            :dedent: 4
            :caption: Asynchronous transport with aiohttp.
    """
    session: Incomplete
    connection_config: Incomplete
    def __init__(self, *, session: aiohttp.ClientSession | None = None, loop: Incomplete | None = None, session_owner: bool = True, **kwargs) -> None: ...
    async def __aenter__(self): ...
    async def __aexit__(self, exc_type: Type[BaseException] | None = None, exc_value: BaseException | None = None, traceback: TracebackType | None = None) -> None: ...
    async def open(self) -> None:
        """Opens the connection."""
    async def close(self) -> None:
        """Closes the connection."""
    @overload
    async def send(self, request: HttpRequest, **config: Any) -> AsyncHttpResponse:
        """Send the request using this HTTP sender.

        Will pre-load the body into memory to be available with a sync method.
        Pass stream=True to avoid this behavior.

        :param request: The HttpRequest object
        :type request: ~azure.core.pipeline.transport.HttpRequest
        :keyword any config: Any keyword arguments
        :return: The AsyncHttpResponse
        :rtype: ~azure.core.pipeline.transport.AsyncHttpResponse

        :keyword bool stream: Defaults to False.
        :keyword dict proxies: dict of proxy to used based on protocol. Proxy is a dict (protocol, url)
        :keyword str proxy: will define the proxy to use all the time
        """
    @overload
    async def send(self, request: RestHttpRequest, **config: Any) -> RestAsyncHttpResponse:
        """Send the `azure.core.rest` request using this HTTP sender.

        Will pre-load the body into memory to be available with a sync method.
        Pass stream=True to avoid this behavior.

        :param request: The HttpRequest object
        :type request: ~azure.core.rest.HttpRequest
        :keyword any config: Any keyword arguments
        :return: The AsyncHttpResponse
        :rtype: ~azure.core.rest.AsyncHttpResponse

        :keyword bool stream: Defaults to False.
        :keyword dict proxies: dict of proxy to used based on protocol. Proxy is a dict (protocol, url)
        :keyword str proxy: will define the proxy to use all the time
        """

class AioHttpStreamDownloadGenerator(AsyncIterator):
    """Streams the response body data.

    :param pipeline: The pipeline object
    :type pipeline: ~azure.core.pipeline.AsyncPipeline
    :param response: The client response object.
    :type response: ~azure.core.rest.AsyncHttpResponse
    :keyword bool decompress: If True which is default, will attempt to decode the body based
        on the *content-encoding* header.
    """
    @overload
    def __init__(self, pipeline: AsyncPipeline[HttpRequest, AsyncHttpResponse], response: AioHttpTransportResponse, *, decompress: bool = True) -> None: ...
    @overload
    def __init__(self, pipeline: AsyncPipeline[RestHttpRequest, RestAsyncHttpResponse], response: RestAioHttpTransportResponse, *, decompress: bool = True) -> None: ...
    def __len__(self) -> int: ...
    async def __anext__(self): ...

class AioHttpTransportResponse(AsyncHttpResponse):
    """Methods for accessing response body data.

    :param request: The HttpRequest object
    :type request: ~azure.core.pipeline.transport.HttpRequest
    :param aiohttp_response: Returned from ClientSession.request().
    :type aiohttp_response: aiohttp.ClientResponse object
    :param block_size: block size of data sent over connection.
    :type block_size: int
    :keyword bool decompress: If True which is default, will attempt to decode the body based
            on the *content-encoding* header.
    """
    status_code: Incomplete
    headers: Incomplete
    reason: Incomplete
    content_type: Incomplete
    def __init__(self, request: HttpRequest, aiohttp_response: aiohttp.ClientResponse, block_size: int | None = None, *, decompress: bool = True) -> None: ...
    def body(self) -> bytes:
        """Return the whole body as bytes in memory.

        :rtype: bytes
        :return: The whole response body.
        """
    def text(self, encoding: str | None = None) -> str:
        """Return the whole body as a string.

        If encoding is not provided, rely on aiohttp auto-detection.

        :param str encoding: The encoding to apply.
        :rtype: str
        :return: The whole response body as a string.
        """
    async def load_body(self) -> None:
        """Load in memory the body, so it could be accessible from sync methods."""
    def stream_download(self, pipeline: AsyncPipeline[HttpRequest, AsyncHttpResponse], **kwargs) -> AsyncIteratorType[bytes]:
        """Generator for streaming response body data.

        :param pipeline: The pipeline object
        :type pipeline: azure.core.pipeline.AsyncPipeline
        :keyword bool decompress: If True which is default, will attempt to decode the body based
            on the *content-encoding* header.
        :rtype: AsyncIterator[bytes]
        :return: An iterator of bytes chunks.
        """
