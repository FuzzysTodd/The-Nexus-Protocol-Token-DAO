import abc
from . import PollingMethod
from .. import PipelineClient
from .._enum_meta import CaseInsensitiveEnumMeta
from ..pipeline import PipelineResponse
from ..pipeline.transport import AsyncHttpResponse as LegacyAsyncHttpResponse, HttpRequest as LegacyHttpRequest, HttpResponse as LegacyHttpResponse
from ..rest import AsyncHttpResponse, HttpRequest, HttpResponse
from enum import Enum
from typing import Any, Callable, Dict, Generic, Sequence, Tuple, TypeVar

__all__ = ['BadResponse', 'BadStatus', 'OperationFailed', 'LongRunningOperation', 'OperationResourcePolling', 'LocationPolling', 'StatusCheckPolling', 'LROBasePolling']

HttpRequestType = LegacyHttpRequest | HttpRequest
HttpResponseType = LegacyHttpResponse | HttpResponse
AllHttpResponseType = LegacyHttpResponse | HttpResponse | LegacyAsyncHttpResponse | AsyncHttpResponse
LegacyPipelineResponseType = PipelineResponse[LegacyHttpRequest, LegacyHttpResponse]
NewPipelineResponseType = PipelineResponse[HttpRequest, HttpResponse]
PipelineResponseType = PipelineResponse[HttpRequestType, HttpResponseType]
HttpRequestTypeVar = TypeVar('HttpRequestTypeVar', bound=HttpRequestType)
HttpResponseTypeVar = TypeVar('HttpResponseTypeVar', bound=HttpResponseType)
AllHttpResponseTypeVar = TypeVar('AllHttpResponseTypeVar', bound=AllHttpResponseType)
ABC = abc.ABC
PollingReturnType_co = TypeVar('PollingReturnType_co', covariant=True)
PipelineClientType = TypeVar('PipelineClientType')
HTTPResponseType_co = TypeVar('HTTPResponseType_co', covariant=True)
HTTPRequestType_co = TypeVar('HTTPRequestType_co', covariant=True)

class BadStatus(Exception): ...
class BadResponse(Exception): ...
class OperationFailed(Exception): ...

class LongRunningOperation(ABC, Generic[HTTPRequestType_co, HTTPResponseType_co], metaclass=abc.ABCMeta):
    """Protocol to implement for a long running operation algorithm."""
    @abc.abstractmethod
    def can_poll(self, pipeline_response: PipelineResponse[HTTPRequestType_co, HTTPResponseType_co]) -> bool:
        """Answer if this polling method could be used.

        :param pipeline_response: Initial REST call response.
        :type pipeline_response: ~azure.core.pipeline.PipelineResponse
        :return: True if this polling method could be used, False otherwise.
        :rtype: bool
        """
    @abc.abstractmethod
    def get_polling_url(self) -> str:
        """Return the polling URL.

        :return: The polling URL.
        :rtype: str
        """
    @abc.abstractmethod
    def set_initial_status(self, pipeline_response: PipelineResponse[HTTPRequestType_co, HTTPResponseType_co]) -> str:
        """Process first response after initiating long running operation.

        :param pipeline_response: Initial REST call response.
        :type pipeline_response: ~azure.core.pipeline.PipelineResponse
        :return: The initial status.
        :rtype: str
        """
    @abc.abstractmethod
    def get_status(self, pipeline_response: PipelineResponse[HTTPRequestType_co, HTTPResponseType_co]) -> str:
        """Return the status string extracted from this response.

        :param pipeline_response: The response object.
        :type pipeline_response: ~azure.core.pipeline.PipelineResponse
        :return: The status string.
        :rtype: str
        """
    @abc.abstractmethod
    def get_final_get_url(self, pipeline_response: PipelineResponse[HTTPRequestType_co, HTTPResponseType_co]) -> str | None:
        """If a final GET is needed, returns the URL.

        :param pipeline_response: Success REST call response.
        :type pipeline_response: ~azure.core.pipeline.PipelineResponse
        :return: The URL to the final GET, or None if no final GET is needed.
        :rtype: str or None
        """

class _LroOption(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Known LRO options from Swagger."""
    FINAL_STATE_VIA: str

class _FinalStateViaOption(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Possible final-state-via options."""
    AZURE_ASYNC_OPERATION_FINAL_STATE: str
    LOCATION_FINAL_STATE: str
    OPERATION_LOCATION_FINAL_STATE: str

class OperationResourcePolling(LongRunningOperation[HttpRequestTypeVar, AllHttpResponseTypeVar]):
    """Implements a operation resource polling, typically from Operation-Location.

    :param str operation_location_header: Name of the header to return operation format (default 'operation-location')
    :keyword dict[str, any] lro_options: Additional options for LRO. For more information, see
     https://aka.ms/azsdk/autorest/openapi/lro-options
    """
    def __init__(self, operation_location_header: str = 'operation-location', *, lro_options: Dict[str, Any] | None = None) -> None: ...
    def can_poll(self, pipeline_response: PipelineResponse[HttpRequestTypeVar, AllHttpResponseTypeVar]) -> bool:
        """Check if status monitor header (e.g. Operation-Location) is present.

        :param pipeline_response: Initial REST call response.
        :type pipeline_response: ~azure.core.pipeline.PipelineResponse
        :return: True if this polling method could be used, False otherwise.
        :rtype: bool
        """
    def get_polling_url(self) -> str:
        """Return the polling URL.

        Will extract it from the defined header to read (e.g. Operation-Location)

        :return: The polling URL.
        :rtype: str
        """
    def get_final_get_url(self, pipeline_response: PipelineResponse[HttpRequestTypeVar, AllHttpResponseTypeVar]) -> str | None:
        """If a final GET is needed, returns the URL.

        :param pipeline_response: Success REST call response.
        :type pipeline_response: ~azure.core.pipeline.PipelineResponse
        :return: The URL to the final GET, or None if no final GET is needed.
        :rtype: str or None
        """
    def set_initial_status(self, pipeline_response: PipelineResponse[HttpRequestTypeVar, AllHttpResponseTypeVar]) -> str:
        """Process first response after initiating long running operation.

        :param pipeline_response: Initial REST call response.
        :type pipeline_response: ~azure.core.pipeline.PipelineResponse
        :return: The initial status.
        :rtype: str
        """
    def get_status(self, pipeline_response: PipelineResponse[HttpRequestTypeVar, AllHttpResponseTypeVar]) -> str:
        '''Process the latest status update retrieved from an "Operation-Location" header.

        :param pipeline_response: Initial REST call response.
        :type pipeline_response: ~azure.core.pipeline.PipelineResponse
        :return: The status string.
        :rtype: str
        :raises: BadResponse if response has no body, or body does not contain status.
        '''

class LocationPolling(LongRunningOperation[HttpRequestTypeVar, AllHttpResponseTypeVar]):
    """Implements a Location polling."""
    def can_poll(self, pipeline_response: PipelineResponse[HttpRequestTypeVar, AllHttpResponseTypeVar]) -> bool:
        """True if contains a Location header

        :param pipeline_response: Initial REST call response.
        :type pipeline_response: ~azure.core.pipeline.PipelineResponse
        :return: True if this polling method could be used, False otherwise.
        :rtype: bool
        """
    def get_polling_url(self) -> str:
        """Return the Location header value.

        :return: The polling URL.
        :rtype: str
        """
    def get_final_get_url(self, pipeline_response: PipelineResponse[HttpRequestTypeVar, AllHttpResponseTypeVar]) -> str | None:
        """If a final GET is needed, returns the URL.

        Always return None for a Location polling.

        :param pipeline_response: Success REST call response.
        :type pipeline_response: ~azure.core.pipeline.PipelineResponse
        :return: Always None for this implementation.
        :rtype: None
        """
    def set_initial_status(self, pipeline_response: PipelineResponse[HttpRequestTypeVar, AllHttpResponseTypeVar]) -> str:
        """Process first response after initiating long running operation.

        :param pipeline_response: Initial REST call response.
        :type pipeline_response: ~azure.core.pipeline.PipelineResponse
        :return: The initial status.
        :rtype: str
        """
    def get_status(self, pipeline_response: PipelineResponse[HttpRequestTypeVar, AllHttpResponseTypeVar]) -> str:
        """Return the status string extracted from this response.

        For Location polling, it means the status monitor returns 202.

        :param pipeline_response: Initial REST call response.
        :type pipeline_response: ~azure.core.pipeline.PipelineResponse
        :return: The status string.
        :rtype: str
        """

class StatusCheckPolling(LongRunningOperation[HttpRequestTypeVar, AllHttpResponseTypeVar]):
    """Should be the fallback polling, that don't poll but exit successfully
    if not other polling are detected and status code is 2xx.
    """
    def can_poll(self, pipeline_response: PipelineResponse[HttpRequestTypeVar, AllHttpResponseTypeVar]) -> bool:
        """Answer if this polling method could be used.

        For this implementation, always True.

        :param pipeline_response: Initial REST call response.
        :type pipeline_response: ~azure.core.pipeline.PipelineResponse
        :return: True if this polling method could be used, False otherwise.
        :rtype: bool
        """
    def get_polling_url(self) -> str:
        """Return the polling URL.

        This is not implemented for this polling, since we're never supposed to loop.

        :return: The polling URL.
        :rtype: str
        """
    def set_initial_status(self, pipeline_response: PipelineResponse[HttpRequestTypeVar, AllHttpResponseTypeVar]) -> str:
        """Process first response after initiating long running operation.

        Will succeed immediately.

        :param pipeline_response: Initial REST call response.
        :type pipeline_response: ~azure.core.pipeline.PipelineResponse
        :return: The initial status.
        :rtype: str
        """
    def get_status(self, pipeline_response: PipelineResponse[HttpRequestTypeVar, AllHttpResponseTypeVar]) -> str:
        """Return the status string extracted from this response.

        Only possible status is success.

        :param pipeline_response: Initial REST call response.
        :type pipeline_response: ~azure.core.pipeline.PipelineResponse
        :return: The status string.
        :rtype: str
        """
    def get_final_get_url(self, pipeline_response: PipelineResponse[HttpRequestTypeVar, AllHttpResponseTypeVar]) -> str | None:
        """If a final GET is needed, returns the URL.

        :param pipeline_response: Success REST call response.
        :type pipeline_response: ~azure.core.pipeline.PipelineResponse
        :rtype: str
        :return: Always None for this implementation.
        """

class _SansIOLROBasePolling(Generic[PollingReturnType_co, PipelineClientType, HttpRequestTypeVar, AllHttpResponseTypeVar]):
    """A base class that has no opinion on IO, to help mypy be accurate.

    :param float timeout: Default polling internal in absence of Retry-After header, in seconds.
    :param list[LongRunningOperation] lro_algorithms: Ordered list of LRO algorithms to use.
    :param lro_options: Additional options for LRO. For more information, see the algorithm's docstring.
    :type lro_options: dict[str, any]
    :param path_format_arguments: A dictionary of the format arguments to be used to format the URL.
    :type path_format_arguments: dict[str, str]
    """
    def __init__(self, timeout: float = 30, lro_algorithms: Sequence[LongRunningOperation[HttpRequestTypeVar, AllHttpResponseTypeVar]] | None = None, lro_options: Dict[str, Any] | None = None, path_format_arguments: Dict[str, str] | None = None, **operation_config: Any) -> None: ...
    def initialize(self, client: PipelineClientType, initial_response: PipelineResponse[HttpRequestTypeVar, AllHttpResponseTypeVar], deserialization_callback: Callable[[PipelineResponse[HttpRequestTypeVar, AllHttpResponseTypeVar]], PollingReturnType_co]) -> None:
        """Set the initial status of this LRO.

        :param client: The Azure Core Pipeline client used to make request.
        :type client: ~azure.core.pipeline.PipelineClient
        :param initial_response: The initial response for the call.
        :type initial_response: ~azure.core.pipeline.PipelineResponse
        :param deserialization_callback: A callback function to deserialize the final response.
        :type deserialization_callback: callable
        :raises: HttpResponseError if initial status is incorrect LRO state
        """
    def get_continuation_token(self) -> str: ...
    @classmethod
    def from_continuation_token(cls, continuation_token: str, **kwargs: Any) -> Tuple[Any, Any, Callable[[Any], PollingReturnType_co]]: ...
    def status(self) -> str:
        """Return the current status as a string.

        :rtype: str
        :return: The current status.
        """
    def finished(self) -> bool:
        """Is this polling finished?

        :rtype: bool
        :return: True if finished, False otherwise.
        """
    def resource(self) -> PollingReturnType_co:
        """Return the built resource.

        :rtype: any
        :return: The built resource.
        """

class LROBasePolling(_SansIOLROBasePolling[PollingReturnType_co, PipelineClient[HttpRequestTypeVar, HttpResponseTypeVar], HttpRequestTypeVar, HttpResponseTypeVar], PollingMethod[PollingReturnType_co]):
    """A base LRO poller.

    This assumes a basic flow:
    - I analyze the response to decide the polling approach
    - I poll
    - I ask the final resource depending of the polling approach

    If your polling need are more specific, you could implement a PollingMethod directly
    """
    def __getattribute__(self, name: str) -> Any:
        """Find the right method for the job.

        This contains a workaround for azure-mgmt-core 1.0.0 to 1.4.0, where the MRO
        is changing when azure-core was refactored in 1.27.0. The MRO change was causing
        AsyncARMPolling to look-up the wrong methods and find the non-async ones.

        :param str name: The name of the attribute to retrieve.
        :rtype: Any
        :return: The attribute value.
        """
    def run(self) -> None: ...
    def update_status(self) -> None:
        """Update the current status of the LRO."""
    def request_status(self, status_link: str) -> PipelineResponse[HttpRequestTypeVar, HttpResponseTypeVar]:
        """Do a simple GET to this status link.

        This method re-inject 'x-ms-client-request-id'.

        :param str status_link: The URL to poll.
        :rtype: azure.core.pipeline.PipelineResponse
        :return: The response of the status request.
        """
