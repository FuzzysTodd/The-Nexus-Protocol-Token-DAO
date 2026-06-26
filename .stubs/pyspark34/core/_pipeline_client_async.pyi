from .configuration import Configuration as Configuration
from .pipeline import AsyncPipeline as AsyncPipeline
from .pipeline.policies import AsyncRetryPolicy as AsyncRetryPolicy, ContentDecodePolicy as ContentDecodePolicy, DistributedTracingPolicy as DistributedTracingPolicy, HttpLoggingPolicy as HttpLoggingPolicy, RequestIdPolicy as RequestIdPolicy, SensitiveHeaderCleanupPolicy as SensitiveHeaderCleanupPolicy
from .pipeline.transport._base import PipelineClientBase as PipelineClientBase
from types import TracebackType
from typing import Any, AsyncContextManager, Awaitable, Generator, Generic, Type, TypeVar

HTTPRequestType = TypeVar('HTTPRequestType')
AsyncHTTPResponseType = TypeVar('AsyncHTTPResponseType', bound='AsyncContextManager')

class _Coroutine(Awaitable[AsyncHTTPResponseType]):
    '''Wrapper to get both context manager and awaitable in place.

    Naming it "_Coroutine" because if you don\'t await it makes the error message easier:
    >>> result = client.send_request(request)
    >>> result.text()
    AttributeError: \'_Coroutine\' object has no attribute \'text\'

    Indeed, the message for calling a coroutine without waiting would be:
    AttributeError: \'coroutine\' object has no attribute \'text\'

    This allows the dev to either use the "async with" syntax, or simply the object directly.
    It\'s also why "send_request" is not declared as async, since it couldn\'t be both easily.

    "wrapped" must be an awaitable object that returns an object implements the async context manager protocol.

    This permits this code to work for both following requests.

    ```python
    from azure.core import AsyncPipelineClient
    from azure.core.rest import HttpRequest

    async def main():

        request = HttpRequest("GET", "https://httpbin.org/user-agent")
        async with AsyncPipelineClient("https://httpbin.org/") as client:
            # Can be used directly
            result = await client.send_request(request)
            print(result.text())

            # Can be used as an async context manager
            async with client.send_request(request) as result:
                print(result.text())
    ```

    :param wrapped: Must be an awaitable the returns an async context manager that supports async "close()"
    :type wrapped: awaitable[AsyncHTTPResponseType]
    '''
    def __init__(self, wrapped: Awaitable[AsyncHTTPResponseType]) -> None: ...
    def __await__(self) -> Generator[Any, None, AsyncHTTPResponseType]: ...
    async def __aenter__(self) -> AsyncHTTPResponseType: ...
    async def __aexit__(self, exc_type: Type[BaseException] | None = None, exc_value: BaseException | None = None, traceback: TracebackType | None = None) -> None: ...

class AsyncPipelineClient(PipelineClientBase, AsyncContextManager['AsyncPipelineClient'], Generic[HTTPRequestType, AsyncHTTPResponseType]):
    """Service client core methods.

    Builds an AsyncPipeline client.

    :param str base_url: URL for the request.
    :keyword ~azure.core.configuration.Configuration config: If omitted, the standard configuration is used.
    :keyword Pipeline pipeline: If omitted, a Pipeline object is created and returned.
    :keyword list[AsyncHTTPPolicy] policies: If omitted, the standard policies of the configuration object is used.
    :keyword per_call_policies: If specified, the policies will be added into the policy list before RetryPolicy
    :paramtype per_call_policies: Union[AsyncHTTPPolicy, SansIOHTTPPolicy,
        list[AsyncHTTPPolicy], list[SansIOHTTPPolicy]]
    :keyword per_retry_policies: If specified, the policies will be added into the policy list after RetryPolicy
    :paramtype per_retry_policies: Union[AsyncHTTPPolicy, SansIOHTTPPolicy,
        list[AsyncHTTPPolicy], list[SansIOHTTPPolicy]]
    :keyword AsyncHttpTransport transport: If omitted, AioHttpTransport is used for asynchronous transport.
    :return: An async pipeline object.
    :rtype: ~azure.core.pipeline.AsyncPipeline

    .. admonition:: Example:

        .. literalinclude:: ../samples/test_example_async.py
            :start-after: [START build_async_pipeline_client]
            :end-before: [END build_async_pipeline_client]
            :language: python
            :dedent: 4
            :caption: Builds the async pipeline client.
    """
    def __init__(self, base_url: str, *, pipeline: AsyncPipeline[HTTPRequestType, AsyncHTTPResponseType] | None = None, config: Configuration[HTTPRequestType, AsyncHTTPResponseType] | None = None, **kwargs: Any) -> None: ...
    async def __aenter__(self) -> AsyncPipelineClient[HTTPRequestType, AsyncHTTPResponseType]: ...
    async def __aexit__(self, exc_type: Type[BaseException] | None = None, exc_value: BaseException | None = None, traceback: TracebackType | None = None) -> None: ...
    async def close(self) -> None: ...
    def send_request(self, request: HTTPRequestType, *, stream: bool = False, **kwargs: Any) -> Awaitable[AsyncHTTPResponseType]:
        """Method that runs the network request through the client's chained policies.

        >>> from azure.core.rest import HttpRequest
        >>> request = HttpRequest('GET', 'http://www.example.com')
        <HttpRequest [GET], url: 'http://www.example.com'>
        >>> response = await client.send_request(request)
        <AsyncHttpResponse: 200 OK>

        :param request: The network request you want to make. Required.
        :type request: ~azure.core.rest.HttpRequest
        :keyword bool stream: Whether the response payload will be streamed. Defaults to False.
        :return: The response of your network call. Does not do error handling on your response.
        :rtype: ~azure.core.rest.AsyncHttpResponse
        """
