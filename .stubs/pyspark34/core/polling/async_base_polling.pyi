from .. import AsyncPipelineClient
from ..pipeline import PipelineResponse
from ..pipeline.transport import AsyncHttpResponse as LegacyAsyncHttpResponse, HttpRequest as LegacyHttpRequest
from ..rest import AsyncHttpResponse, HttpRequest
from ._async_poller import AsyncPollingMethod
from .base_polling import _SansIOLROBasePolling
from typing import TypeVar

__all__ = ['AsyncLROBasePolling', 'AsyncLROBasePolling']

HttpRequestType = LegacyHttpRequest | HttpRequest
AsyncHttpResponseType = LegacyAsyncHttpResponse | AsyncHttpResponse
HttpRequestTypeVar = TypeVar('HttpRequestTypeVar', bound=HttpRequestType)
AsyncHttpResponseTypeVar = TypeVar('AsyncHttpResponseTypeVar', bound=AsyncHttpResponseType)
PollingReturnType_co = TypeVar('PollingReturnType_co', covariant=True)

class AsyncLROBasePolling(_SansIOLROBasePolling[PollingReturnType_co, AsyncPipelineClient[HttpRequestTypeVar, AsyncHttpResponseTypeVar], HttpRequestTypeVar, AsyncHttpResponseTypeVar], AsyncPollingMethod[PollingReturnType_co]):
    """A base LRO async poller.

    This assumes a basic flow:
    - I analyze the response to decide the polling approach
    - I poll
    - I ask the final resource depending of the polling approach

    If your polling need are more specific, you could implement a PollingMethod directly
    """
    async def run(self) -> None: ...
    async def update_status(self) -> None:
        """Update the current status of the LRO."""
    async def request_status(self, status_link: str) -> PipelineResponse[HttpRequestTypeVar, AsyncHttpResponseTypeVar]:
        """Do a simple GET to this status link.

        This method re-inject 'x-ms-client-request-id'.

        :param str status_link: URL to poll.
        :rtype: azure.core.pipeline.PipelineResponse
        :return: The response of the status request.
        """
