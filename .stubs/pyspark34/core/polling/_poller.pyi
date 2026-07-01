from typing import Any, Callable, Generic, Tuple, TypeVar

PollingReturnType_co = TypeVar('PollingReturnType_co', covariant=True)
DeserializationCallbackType = Any

class PollingMethod(Generic[PollingReturnType_co]):
    """ABC class for polling method."""
    def initialize(self, client: Any, initial_response: Any, deserialization_callback: DeserializationCallbackType) -> None: ...
    def run(self) -> None: ...
    def status(self) -> str: ...
    def finished(self) -> bool: ...
    def resource(self) -> PollingReturnType_co: ...
    def get_continuation_token(self) -> str: ...
    @classmethod
    def from_continuation_token(cls, continuation_token: str, **kwargs: Any) -> Tuple[Any, Any, DeserializationCallbackType]: ...

class _SansIONoPolling(Generic[PollingReturnType_co]):
    def __init__(self) -> None: ...
    def initialize(self, _: Any, initial_response: Any, deserialization_callback: Callable[[Any], PollingReturnType_co]) -> None: ...
    def status(self) -> str:
        """Return the current status.

        :rtype: str
        :return: The current status
        """
    def finished(self) -> bool:
        """Is this polling finished?

        :rtype: bool
        :return: Whether this polling is finished
        """
    def resource(self) -> PollingReturnType_co: ...
    def get_continuation_token(self) -> str: ...
    @classmethod
    def from_continuation_token(cls, continuation_token: str, **kwargs: Any) -> Tuple[Any, Any, Callable[[Any], PollingReturnType_co]]: ...

class NoPolling(_SansIONoPolling[PollingReturnType_co], PollingMethod[PollingReturnType_co]):
    """An empty poller that returns the deserialized initial response."""
    def run(self) -> None:
        """Empty run, no polling."""

class LROPoller(Generic[PollingReturnType_co]):
    '''Poller for long running operations.

    :param client: A pipeline service client
    :type client: ~azure.core.PipelineClient
    :param initial_response: The initial call response
    :type initial_response: ~azure.core.pipeline.PipelineResponse
    :param deserialization_callback: A callback that takes a Response and return a deserialized object.
                                     If a subclass of Model is given, this passes "deserialize" as callback.
    :type deserialization_callback: callable or msrest.serialization.Model
    :param polling_method: The polling strategy to adopt
    :type polling_method: ~azure.core.polling.PollingMethod
    '''
    def __init__(self, client: Any, initial_response: Any, deserialization_callback: Callable[[Any], PollingReturnType_co], polling_method: PollingMethod[PollingReturnType_co]) -> None: ...
    def polling_method(self) -> PollingMethod[PollingReturnType_co]:
        """Return the polling method associated to this poller.

        :return: The polling method
        :rtype: ~azure.core.polling.PollingMethod
        """
    def continuation_token(self) -> str:
        """Return a continuation token that allows to restart the poller later.

        :returns: An opaque continuation token
        :rtype: str
        """
    @classmethod
    def from_continuation_token(cls, polling_method: PollingMethod[PollingReturnType_co], continuation_token: str, **kwargs: Any) -> LROPoller[PollingReturnType_co]: ...
    def status(self) -> str:
        """Returns the current status string.

        :returns: The current status string
        :rtype: str
        """
    def result(self, timeout: float | None = None) -> PollingReturnType_co:
        """Return the result of the long running operation, or
        the result available after the specified timeout.

        :param float timeout: Period of time to wait before getting back control.
        :returns: The deserialized resource of the long running operation, if one is available.
        :rtype: any or None
        :raises ~azure.core.exceptions.HttpResponseError: Server problem with the query.
        """
    def wait(self, timeout: float | None = None) -> None:
        '''Wait on the long running operation for a specified length
        of time. You can check if this call as ended with timeout with the
        "done()" method.

        :param float timeout: Period of time to wait for the long running
         operation to complete (in seconds).
        :raises ~azure.core.exceptions.HttpResponseError: Server problem with the query.
        '''
    def done(self) -> bool:
        """Check status of the long running operation.

        :returns: 'True' if the process has completed, else 'False'.
        :rtype: bool
        """
    def add_done_callback(self, func: Callable) -> None:
        """Add callback function to be run once the long running operation
        has completed - regardless of the status of the operation.

        :param callable func: Callback function that takes at least one
         argument, a completed LongRunningOperation.
        """
    def remove_done_callback(self, func: Callable) -> None:
        """Remove a callback from the long running operation.

        :param callable func: The function to be removed from the callbacks.
        :raises ValueError: if the long running operation has already completed.
        """
