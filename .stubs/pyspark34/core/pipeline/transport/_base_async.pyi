import abc
from .._base_async import AsyncPipeline as AsyncPipeline
from ._base import HttpRequest as HttpRequest, _HttpClientTransportResponse, _HttpResponseBase
from collections.abc import AsyncIterator
from types import TracebackType
from typing import Any, AsyncContextManager, AsyncIterator as AsyncIteratorType, Generic, Type, TypeVar

AsyncHTTPResponseType = TypeVar('AsyncHTTPResponseType')
HTTPResponseType = TypeVar('HTTPResponseType')
HTTPRequestType = TypeVar('HTTPRequestType')

class _ResponseStopIteration(Exception): ...

class AsyncHttpResponse(_HttpResponseBase, AsyncContextManager['AsyncHttpResponse']):
    """An AsyncHttpResponse ABC.

    Allows for the asynchronous streaming of data from the response.
    """
    def stream_download(self, pipeline: AsyncPipeline[HttpRequest, 'AsyncHttpResponse'], **kwargs: Any) -> AsyncIteratorType[bytes]:
        """Generator for streaming response body data.

        Should be implemented by sub-classes if streaming download
        is supported. Will return an asynchronous generator.

        :param pipeline: The pipeline object
        :type pipeline: azure.core.pipeline.Pipeline
        :keyword bool decompress: If True which is default, will attempt to decode the body based
            on the *content-encoding* header.
        :return: An async iterator of bytes
        :rtype: AsyncIterator[bytes]
        """
    def parts(self) -> AsyncIterator['AsyncHttpResponse']:
        """Assuming the content-type is multipart/mixed, will return the parts as an async iterator.

        :return: An async iterator of the parts
        :rtype: AsyncIterator
        :raises ValueError: If the content is not multipart/mixed
        """
    async def __aexit__(self, exc_type: Type[BaseException] | None = None, exc_value: BaseException | None = None, traceback: TracebackType | None = None) -> None: ...

class AsyncHttpClientTransportResponse(_HttpClientTransportResponse, AsyncHttpResponse):
    '''Create a HTTPResponse from an http.client response.

    Body will NOT be read by the constructor. Call "body()" to load the body in memory if necessary.

    :param HttpRequest request: The request.
    :param httpclient_response: The object returned from an HTTP(S)Connection from http.client
    '''

class AsyncHttpTransport(AsyncContextManager['AsyncHttpTransport'], abc.ABC, Generic[HTTPRequestType, AsyncHTTPResponseType], metaclass=abc.ABCMeta):
    """An http sender ABC."""
    @abc.abstractmethod
    async def send(self, request: HTTPRequestType, **kwargs: Any) -> AsyncHTTPResponseType:
        """Send the request using this HTTP sender.

        :param request: The request object. Exact type can be inferred from the pipeline.
        :type request: any
        :return: The response object. Exact type can be inferred from the pipeline.
        :rtype: any
        """
    @abc.abstractmethod
    async def open(self) -> None:
        """Assign new session if one does not already exist."""
    @abc.abstractmethod
    async def close(self) -> None:
        """Close the session if it is not externally owned."""
    async def sleep(self, duration: float) -> None:
        '''Sleep for the specified duration.

        You should always ask the transport to sleep, and not call directly
        the stdlib. This is mostly important in async, as the transport
        may not use asyncio but other implementation like trio and they their own
        way to sleep, but to keep design
        consistent, it\'s cleaner to always ask the transport to sleep and let the transport
        implementor decide how to do it.
        By default, this method will use "asyncio", and don\'t need to be overridden
        if your transport does too.

        :param float duration: The number of seconds to sleep.
        '''
