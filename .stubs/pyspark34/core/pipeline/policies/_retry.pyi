from ..._enum_meta import CaseInsensitiveEnumMeta as CaseInsensitiveEnumMeta
from ._base import HTTPPolicy as HTTPPolicy, RequestHistory as RequestHistory
from _typeshed import Incomplete
from azure.core.pipeline import PipelineContext as PipelineContext, PipelineRequest, PipelineResponse
from azure.core.pipeline.transport import AsyncHttpResponse as LegacyAsyncHttpResponse, HttpRequest as LegacyHttpRequest, HttpResponse as LegacyHttpResponse, HttpTransport
from azure.core.rest import AsyncHttpResponse, HttpRequest, HttpResponse
from enum import Enum
from typing import Any, Dict, TypeVar

HTTPResponseType = TypeVar('HTTPResponseType', HttpResponse, LegacyHttpResponse)
AllHttpResponseType = TypeVar('AllHttpResponseType', HttpResponse, LegacyHttpResponse, AsyncHttpResponse, LegacyAsyncHttpResponse)
HTTPRequestType = TypeVar('HTTPRequestType', HttpRequest, LegacyHttpRequest)
ClsRetryPolicy = TypeVar('ClsRetryPolicy', bound='RetryPolicyBase')

class RetryMode(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    Exponential: str
    Fixed: str

class RetryPolicyBase:
    BACKOFF_MAX: int
    total_retries: Incomplete
    connect_retries: Incomplete
    read_retries: Incomplete
    status_retries: Incomplete
    backoff_factor: Incomplete
    backoff_max: Incomplete
    retry_mode: Incomplete
    timeout: Incomplete
    def __init__(self, **kwargs: Any) -> None: ...
    @classmethod
    def no_retries(cls) -> ClsRetryPolicy:
        """Disable retries.

        :return: A retry policy with retries disabled.
        :rtype: ~azure.core.pipeline.policies.RetryPolicy or ~azure.core.pipeline.policies.AsyncRetryPolicy
        """
    def configure_retries(self, options: Dict[str, Any]) -> Dict[str, Any]:
        """Configures the retry settings.

        :param options: keyword arguments from context.
        :type options: dict
        :return: A dict containing settings and history for retries.
        :rtype: dict
        """
    def get_backoff_time(self, settings: Dict[str, Any]) -> float:
        """Returns the current backoff time.

        :param dict settings: The retry settings.
        :return: The current backoff value.
        :rtype: float
        """
    def parse_retry_after(self, retry_after: str) -> float:
        """Helper to parse Retry-After and get value in seconds.

        :param str retry_after: Retry-After header
        :rtype: float
        :return: Value of Retry-After in seconds.
        """
    def get_retry_after(self, response: PipelineResponse[Any, AllHttpResponseType]) -> float | None:
        """Get the value of Retry-After in seconds.

        :param response: The PipelineResponse object
        :type response: ~azure.core.pipeline.PipelineResponse
        :return: Value of Retry-After in seconds.
        :rtype: float or None
        """
    def is_retry(self, settings: Dict[str, Any], response: PipelineResponse[HTTPRequestType, AllHttpResponseType]) -> bool:
        """Checks if method/status code is retryable.

        Based on allowlists and control variables such as the number of
        total retries to allow, whether to respect the Retry-After header,
        whether this header is present, and whether the returned status
        code is on the list of status codes to be retried upon on the
        presence of the aforementioned header.

        The behavior is:
        -\tIf status_code < 400: don't retry
        -\tElse if Retry-After present: retry
        -\tElse: retry based on the safe status code list ([408, 429, 500, 502, 503, 504])


        :param dict settings: The retry settings.
        :param response: The PipelineResponse object
        :type response: ~azure.core.pipeline.PipelineResponse
        :return: True if method/status code is retryable. False if not retryable.
        :rtype: bool
        """
    def is_exhausted(self, settings: Dict[str, Any]) -> bool:
        """Checks if any retries left.

        :param dict settings: the retry settings
        :return: False if have more retries. True if retries exhausted.
        :rtype: bool
        """
    def increment(self, settings: Dict[str, Any], response: PipelineRequest[HTTPRequestType] | PipelineResponse[HTTPRequestType, AllHttpResponseType] | None = None, error: Exception | None = None) -> bool:
        """Increment the retry counters.

        :param settings: The retry settings.
        :type settings: dict
        :param response: A pipeline response object.
        :type response: ~azure.core.pipeline.PipelineResponse
        :param error: An error encountered during the request, or
         None if the response was received successfully.
        :type error: ~azure.core.exceptions.AzureError
        :return: Whether any retry attempt is available
         True if more retry attempts available, False otherwise
        :rtype: bool
        """
    def update_context(self, context: PipelineContext, retry_settings: Dict[str, Any]) -> None:
        """Updates retry history in pipeline context.

        :param context: The pipeline context.
        :type context: ~azure.core.pipeline.PipelineContext
        :param retry_settings: The retry settings.
        :type retry_settings: dict
        """

class RetryPolicy(RetryPolicyBase, HTTPPolicy[HTTPRequestType, HTTPResponseType]):
    """A retry policy.

    The retry policy in the pipeline can be configured directly, or tweaked on a per-call basis.

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
     In fixed mode, retry policy will always sleep for {backoff factor}.
     In 'exponential' mode, retry policy will sleep for: `{backoff factor} * (2 ** ({number of total retries} - 1))`
     seconds. If the backoff_factor is 0.1, then the retry will sleep
     for [0.0s, 0.2s, 0.4s, ...] between retries. The default value is 0.8.

    :keyword int retry_backoff_max: The maximum back off time. Default value is 120 seconds (2 minutes).

    :keyword RetryMode retry_mode: Fixed or exponential delay between attemps, default is exponential.

    :keyword int timeout: Timeout setting for the operation in seconds, default is 604800s (7 days).

    .. admonition:: Example:

        .. literalinclude:: ../samples/test_example_sync.py
            :start-after: [START retry_policy]
            :end-before: [END retry_policy]
            :language: python
            :dedent: 4
            :caption: Configuring a retry policy.
    """
    def sleep(self, settings: Dict[str, Any], transport: HttpTransport[HTTPRequestType, HTTPResponseType], response: PipelineResponse[HTTPRequestType, HTTPResponseType] | None = None) -> None:
        """Sleep between retry attempts.

        This method will respect a server's ``Retry-After`` response header
        and sleep the duration of the time requested. If that is not present, it
        will use an exponential backoff. By default, the backoff factor is 0 and
        this method will return immediately.

        :param dict settings: The retry settings.
        :param transport: The HTTP transport type.
        :type transport: ~azure.core.pipeline.transport.HttpTransport
        :param response: The PipelineResponse object.
        :type response: ~azure.core.pipeline.PipelineResponse
        """
    def send(self, request: PipelineRequest[HTTPRequestType]) -> PipelineResponse[HTTPRequestType, HTTPResponseType]:
        """Sends the PipelineRequest object to the next policy. Uses retry settings if necessary.

        :param request: The PipelineRequest object
        :type request: ~azure.core.pipeline.PipelineRequest
        :return: Returns the PipelineResponse or raises error if maximum retries exceeded.
        :rtype: ~azure.core.pipeline.PipelineResponse
        :raises: ~azure.core.exceptions.AzureError if maximum retries exceeded.
        :raises: ~azure.core.exceptions.ClientAuthenticationError if authentication
        """
