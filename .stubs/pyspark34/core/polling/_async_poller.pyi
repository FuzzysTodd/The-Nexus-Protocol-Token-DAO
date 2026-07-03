from ..exceptions import AzureError as AzureError
from ._poller import _SansIONoPolling
from typing import Any, Awaitable, Callable, Generator, Generic, Tuple, TypeVar

PollingReturnType_co = TypeVar('PollingReturnType_co', covariant=True)
DeserializationCallbackType = Any

class AsyncPollingMethod(Generic[PollingReturnType_co]):
    """ABC class for polling method."""
    def initialize(self, client: Any, initial_response: Any, deserialization_callback: DeserializationCallbackType) -> None: ...
    async def run(self) -> None: ...
    def status(self) -> str: ...
    def finished(self) -> bool: ...
    def resource(self) -> PollingReturnType_co: ...
    def get_continuation_token(self) -> str: ...
    @classmethod
    def from_continuation_token(cls, continuation_token: str, **kwargs: Any) -> Tuple[Any, Any, DeserializationCallbackType]: ...

class AsyncNoPolling(_SansIONoPolling[PollingReturnType_co], AsyncPollingMethod[PollingReturnType_co]):
    """An empty async poller that returns the deserialized initial response."""
    async def run(self) -> None:
        '''Empty run, no polling.
        Just override initial run to add "async"
        '''

async def async_poller(client: Any, initial_response: Any, deserialization_callback: Callable[[Any], PollingReturnType_co], polling_method: AsyncPollingMethod[PollingReturnType_co]) -> PollingReturnType_co:
    '''Async Poller for long running operations.

    .. deprecated:: 1.5.0
       Use :class:`AsyncLROPoller` instead.

    :param client: A pipeline service client.
    :type client: ~azure.core.PipelineClient
    :param initial_response: The initial call response
    :type initial_response: ~azure.core.pipeline.PipelineResponse
    :param deserialization_callback: A callback that takes a Response and return a deserialized object.
                                     If a subclass of Model is given, this passes "deserialize" as callback.
    :type deserialization_callback: callable or msrest.serialization.Model
    :param polling_method: The polling strategy to adopt
    :type polling_method: ~azure.core.polling.PollingMethod
    :return: The final resource at the end of the polling.
    :rtype: any or None
    '''

class AsyncLROPoller(Awaitable[PollingReturnType_co], Generic[PollingReturnType_co]):
    '''Async poller for long running operations.

    :param client: A pipeline service client
    :type client: ~azure.core.PipelineClient
    :param initial_response: The initial call response
    :type initial_response: ~azure.core.pipeline.PipelineResponse
    :param deserialization_callback: A callback that takes a Response and return a deserialized object.
                                     If a subclass of Model is given, this passes "deserialize" as callback.
    :type deserialization_callback: callable or msrest.serialization.Model
    :param polling_method: The polling strategy to adopt
    :type polling_method: ~azure.core.polling.AsyncPollingMethod
    '''
    def __init__(self, client: Any, initial_response: Any, deserialization_callback: Callable[[Any], PollingReturnType_co], polling_method: AsyncPollingMethod[PollingReturnType_co]) -> None: ...
    def polling_method(self) -> AsyncPollingMethod[PollingReturnType_co]:
        """Return the polling method associated to this poller.

        :return: The polling method associated to this poller.
        :rtype: ~azure.core.polling.AsyncPollingMethod
        """
    def continuation_token(self) -> str:
        """Return a continuation token that allows to restart the poller later.

        :returns: An opaque continuation token
        :rtype: str
        """
    @classmethod
    def from_continuation_token(cls, polling_method: AsyncPollingMethod[PollingReturnType_co], continuation_token: str, **kwargs: Any) -> AsyncLROPoller[PollingReturnType_co]: ...
    def status(self) -> str:
        """Returns the current status string.

        :returns: The current status string
        :rtype: str
        """
    async def result(self) -> PollingReturnType_co:
        """Return the result of the long running operation.

        :returns: The deserialized resource of the long running operation, if one is available.
        :rtype: any or None
        :raises ~azure.core.exceptions.HttpResponseError: Server problem with the query.
        """
    def __await__(self) -> Generator[Any, None, PollingReturnType_co]: ...
    async def wait(self) -> None:
        """Wait on the long running operation.

        :raises ~azure.core.exceptions.HttpResponseError: Server problem with the query.
        """
    def done(self) -> bool:
        """Check status of the long running operation.

        :returns: 'True' if the process has completed, else 'False'.
        :rtype: bool
        """
