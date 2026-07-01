from ._base_async import AsyncHTTPPolicy as AsyncHTTPPolicy
from ._retry import RetryPolicyBase as RetryPolicyBase
from azure.core.pipeline import PipelineRequest as PipelineRequest, PipelineResponse as PipelineResponse
from azure.core.pipeline.transport import AsyncHttpResponse as LegacyAsyncHttpResponse, AsyncHttpTransport, HttpRequest as LegacyHttpRequest
from azure.core.rest import AsyncHttpResponse, HttpRequest
from typing import Any, Dict, TypeVar

AsyncHTTPResponseType = TypeVar('AsyncHTTPResponseType', AsyncHttpResponse, LegacyAsyncHttpResponse)
HTTPRequestType = TypeVar('HTTPRequestType', HttpRequest, LegacyHttpRequest)

class AsyncRetryPolicy(RetryPolicyBase, AsyncHTTPPolicy[HTTPRequestType, AsyncHTTPResponseType]):
    """Async flavor of the retry policy.

    The async retry policy in the pipeline can be configured directly, or tweaked on a per-call basis.

    :keyword int retry_total: Total number of retries to allow. Takes precedence over other counts.
     Default value is 10.

    :keyword int retry_connect: How many connection-related errors to retry on.
     These are errors raised before the request is sent to the remote server,
     which we assume has not triggered the server to process the request. Default value is 3.

    :keyword int retry_read: How many times to retry on read errors.
     These errors are raised after the request was sent to the server, so the
     request may have side-effects. Default value is 3.

    :keyword int retry_status: How many times to retry on bad status codes. Default value is 3.

    :keyword float retry_backoff_factor: A backoff factor to apply between attempts after the second try
     (most errors are resolved immediately by a second try without a delay).
     Retry policy will sleep for: `{backoff factor} * (2 ** ({number of total retries} - 1))`
     seconds. If the backoff_factor is 0.1, then the retry will sleep
     for [0.0s, 0.2s, 0.4s, ...] between retries. The default value is 0.8.

    :keyword int retry_backoff_max: The maximum back off time. Default value is 120 seconds (2 minutes).

    .. admonition:: Example:

        .. literalinclude:: ../samples/test_example_async.py
            :start-after: [START async_retry_policy]
            :end-before: [END async_retry_policy]
            :language: python
            :dedent: 4
            :caption: Configuring an async retry policy.
    """
    async def sleep(self, settings: Dict[str, Any], transport: AsyncHttpTransport[HTTPRequestType, AsyncHTTPResponseType], response: PipelineResponse[HTTPRequestType, AsyncHTTPResponseType] | None = None) -> None:
        """Sleep between retry attempts.

        This method will respect a server's ``Retry-After`` response header
        and sleep the duration of the time requested. If that is not present, it
        will use an exponential backoff. By default, the backoff factor is 0 and
        this method will return immediately.

        :param dict settings: The retry settings.
        :param transport: The HTTP transport type.
        :type transport: ~azure.core.pipeline.transport.AsyncHttpTransport
        :param response: The PipelineResponse object.
        :type response: ~azure.core.pipeline.PipelineResponse
        """
    async def send(self, request: PipelineRequest[HTTPRequestType]) -> PipelineResponse[HTTPRequestType, AsyncHTTPResponseType]:
        """Uses the configured retry policy to send the request to the next policy in the pipeline.

        :param request: The PipelineRequest object
        :type request: ~azure.core.pipeline.PipelineRequest
        :return: Returns the PipelineResponse or raises error if maximum retries exceeded.
        :rtype: ~azure.core.pipeline.PipelineResponse
        :raise: ~azure.core.exceptions.AzureError if maximum retries exceeded.
        :raise: ~azure.core.exceptions.ClientAuthenticationError if authentication fails
        """
