from ._base import cleanup_kwargs_for_transport as cleanup_kwargs_for_transport
from .transport import AsyncHttpTransport as AsyncHttpTransport
from azure.core.pipeline import PipelineRequest, PipelineResponse
from azure.core.pipeline.policies import AsyncHTTPPolicy, SansIOHTTPPolicy
from types import TracebackType
from typing import Any, Generic, Iterable, Type, TypeVar
from typing_extensions import AsyncContextManager

AsyncHTTPResponseType = TypeVar('AsyncHTTPResponseType')
HTTPRequestType = TypeVar('HTTPRequestType')

class _SansIOAsyncHTTPPolicyRunner(AsyncHTTPPolicy[HTTPRequestType, AsyncHTTPResponseType]):
    """Async implementation of the SansIO policy.

    Modifies the request and sends to the next policy in the chain.

    :param policy: A SansIO policy.
    :type policy: ~azure.core.pipeline.policies.SansIOHTTPPolicy
    """
    def __init__(self, policy: SansIOHTTPPolicy[HTTPRequestType, AsyncHTTPResponseType]) -> None: ...
    async def send(self, request: PipelineRequest[HTTPRequestType]) -> PipelineResponse[HTTPRequestType, AsyncHTTPResponseType]:
        """Modifies the request and sends to the next policy in the chain.

        :param request: The PipelineRequest object.
        :type request: ~azure.core.pipeline.PipelineRequest
        :return: The PipelineResponse object.
        :rtype: ~azure.core.pipeline.PipelineResponse
        """

class _AsyncTransportRunner(AsyncHTTPPolicy[HTTPRequestType, AsyncHTTPResponseType]):
    """Async Transport runner.

    Uses specified HTTP transport type to send request and returns response.

    :param sender: The async Http Transport instance.
    :type sender: ~azure.core.pipeline.transport.AsyncHttpTransport
    """
    def __init__(self, sender: AsyncHttpTransport[HTTPRequestType, AsyncHTTPResponseType]) -> None: ...
    async def send(self, request: PipelineRequest[HTTPRequestType]) -> PipelineResponse[HTTPRequestType, AsyncHTTPResponseType]:
        """Async HTTP transport send method.

        :param request: The PipelineRequest object.
        :type request: ~azure.core.pipeline.PipelineRequest
        :return: The PipelineResponse object.
        :rtype: ~azure.core.pipeline.PipelineResponse
        """

class AsyncPipeline(AsyncContextManager['AsyncPipeline'], Generic[HTTPRequestType, AsyncHTTPResponseType]):
    """Async pipeline implementation.

    This is implemented as a context manager, that will activate the context
    of the HTTP sender.

    :param transport: The async Http Transport instance.
    :type transport: ~azure.core.pipeline.transport.AsyncHttpTransport
    :param list policies: List of configured policies.

    .. admonition:: Example:

        .. literalinclude:: ../samples/test_example_async.py
            :start-after: [START build_async_pipeline]
            :end-before: [END build_async_pipeline]
            :language: python
            :dedent: 4
            :caption: Builds the async pipeline for asynchronous transport.
    """
    def __init__(self, transport: AsyncHttpTransport[HTTPRequestType, AsyncHTTPResponseType], policies: Iterable[AsyncHTTPPolicy[HTTPRequestType, AsyncHTTPResponseType] | SansIOHTTPPolicy[HTTPRequestType, AsyncHTTPResponseType]] | None = None) -> None: ...
    async def __aenter__(self) -> AsyncPipeline[HTTPRequestType, AsyncHTTPResponseType]: ...
    async def __aexit__(self, exc_type: Type[BaseException] | None = None, exc_value: BaseException | None = None, traceback: TracebackType | None = None) -> None: ...
    async def run(self, request: HTTPRequestType, **kwargs: Any) -> PipelineResponse[HTTPRequestType, AsyncHTTPResponseType]:
        """Runs the HTTP Request through the chained policies.

        :param request: The HTTP request object.
        :type request: ~azure.core.pipeline.transport.HttpRequest
        :return: The PipelineResponse object.
        :rtype: ~azure.core.pipeline.PipelineResponse
        """
