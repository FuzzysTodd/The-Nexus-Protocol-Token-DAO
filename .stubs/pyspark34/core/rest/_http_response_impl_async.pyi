from ._http_response_impl import _HttpResponseBackcompatMixinBase, _HttpResponseBaseImpl, _RestHttpClientTransportResponseBase
from ._rest_py3 import AsyncHttpResponse as _AsyncHttpResponse
from types import TracebackType
from typing import Any, AsyncIterator, Type

class AsyncHttpResponseBackcompatMixin(_HttpResponseBackcompatMixinBase):
    """Backcompat mixin for async responses"""
    def __getattr__(self, attr): ...
    def parts(self):
        """DEPRECATED: Assuming the content-type is multipart/mixed, will return the parts as an async iterator.
        This is deprecated and will be removed in a later release.
        :rtype: AsyncIterator
        :return: The parts of the response
        :raises ValueError: If the content is not multipart/mixed
        """

class AsyncHttpResponseImpl(_HttpResponseBaseImpl, _AsyncHttpResponse, AsyncHttpResponseBackcompatMixin):
    """AsyncHttpResponseImpl built on top of our HttpResponse protocol class.

    Since ~azure.core.rest.AsyncHttpResponse is an abstract base class, we need to
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
    async def read(self) -> bytes:
        """Read the response's bytes into memory.

        :return: The response's bytes
        :rtype: bytes
        """
    async def iter_raw(self, **kwargs: Any) -> AsyncIterator[bytes]:
        """Asynchronously iterates over the response's bytes. Will not decompress in the process
        :return: An async iterator of bytes from the response
        :rtype: AsyncIterator[bytes]
        """
    async def iter_bytes(self, **kwargs: Any) -> AsyncIterator[bytes]:
        """Asynchronously iterates over the response's bytes. Will decompress in the process
        :return: An async iterator of bytes from the response
        :rtype: AsyncIterator[bytes]
        """
    async def close(self) -> None:
        """Close the response.

        :return: None
        :rtype: None
        """
    async def __aexit__(self, exc_type: Type[BaseException] | None = None, exc_value: BaseException | None = None, traceback: TracebackType | None = None) -> None: ...

class RestAsyncHttpClientTransportResponse(_RestHttpClientTransportResponseBase, AsyncHttpResponseImpl):
    """Create a Rest HTTPResponse from an http.client response."""
    async def iter_bytes(self, **kwargs) -> None: ...
    async def iter_raw(self, **kwargs) -> None: ...
    async def read(self): ...
