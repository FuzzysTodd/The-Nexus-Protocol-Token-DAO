from .authentication import StorageHttpChallenge as StorageHttpChallenge
from .constants import DEFAULT_OAUTH_SCOPE as DEFAULT_OAUTH_SCOPE, STORAGE_OAUTH_SCOPE as STORAGE_OAUTH_SCOPE
from .models import LocationMode as LocationMode
from _typeshed import Incomplete
from azure.core.credentials import TokenCredential as TokenCredential
from azure.core.pipeline import PipelineRequest as PipelineRequest, PipelineResponse as PipelineResponse
from azure.core.pipeline.policies import BearerTokenCredentialPolicy, HTTPPolicy, HeadersPolicy, NetworkTraceLoggingPolicy, SansIOHTTPPolicy
from typing import Any

def encode_base64(data): ...
def is_exhausted(settings): ...
def retry_hook(settings, **kwargs) -> None: ...
def is_retry(response, mode): ...
def urljoin(base_url, stub_url): ...

class QueueMessagePolicy(SansIOHTTPPolicy):
    def on_request(self, request) -> None: ...

class StorageHeadersPolicy(HeadersPolicy):
    request_id_header_name: str
    def on_request(self, request: Any) -> None: ...

class StorageHosts(SansIOHTTPPolicy):
    hosts: Incomplete
    def __init__(self, hosts: Incomplete | None = None, **kwargs) -> None: ...
    def on_request(self, request: Any) -> None: ...

class StorageLoggingPolicy(NetworkTraceLoggingPolicy):
    '''A policy that logs HTTP request and response to the DEBUG logger.

    This accepts both global configuration, and per-request level with "enable_http_logger"
    '''
    logging_body: Incomplete
    def __init__(self, logging_enable: bool = False, **kwargs) -> None: ...
    def on_request(self, request: Any) -> None: ...
    def on_response(self, request: PipelineResponse, response: Any) -> None: ...

class StorageRequestHook(SansIOHTTPPolicy):
    def __init__(self, **kwargs) -> None: ...
    def on_request(self, request: Any) -> PipelineResponse: ...

class StorageResponseHook(HTTPPolicy):
    def __init__(self, **kwargs) -> None: ...
    def send(self, request: PipelineRequest) -> PipelineResponse: ...

class StorageContentValidation(SansIOHTTPPolicy):
    """A simple policy that sends the given headers
    with the request.

    This will overwrite any headers already defined in the request.
    """
    header_name: str
    def __init__(self, **kwargs) -> None: ...
    @staticmethod
    def get_content_md5(data): ...
    def on_request(self, request: Any) -> None: ...
    def on_response(self, request, response) -> None: ...

class StorageRetryPolicy(HTTPPolicy):
    """
    The base class for Exponential and Linear retries containing shared code.
    """
    total_retries: Incomplete
    connect_retries: Incomplete
    read_retries: Incomplete
    status_retries: Incomplete
    retry_to_secondary: Incomplete
    def __init__(self, **kwargs) -> None: ...
    def configure_retries(self, request): ...
    def get_backoff_time(self, settings):
        """ Formula for computing the current backoff.
        Should be calculated by child class.

        :param Optional[Dict[str, Any]] settings: The configurable values pertaining to the backoff time.
        :returns: The backoff time.
        :rtype: float
        """
    def sleep(self, settings, transport) -> None: ...
    def increment(self, settings, request, response: Incomplete | None = None, error: Incomplete | None = None):
        '''Increment the retry counters.

        :param Optional[Dict[str, Any]] settings: The configurable values pertaining to the increment operation.
        :param "PipelineRequest" request: A pipeline request object.
        :param "PipelineResponse": A pipeline response object.
        :param error: An error encountered during the request, or
            None if the response was received successfully.
        :paramtype error: Union[ServiceRequestError, ServiceResponseError]
        :returns: Whether the retry attempts are exhausted.
        :rtype: bool
        '''
    def send(self, request): ...

class ExponentialRetry(StorageRetryPolicy):
    """Exponential retry."""
    initial_backoff: Incomplete
    increment_base: Incomplete
    random_jitter_range: Incomplete
    def __init__(self, initial_backoff: int = 15, increment_base: int = 3, retry_total: int = 3, retry_to_secondary: bool = False, random_jitter_range: int = 3, **kwargs) -> None:
        """
        Constructs an Exponential retry object. The initial_backoff is used for
        the first retry. Subsequent retries are retried after initial_backoff +
        increment_power^retry_count seconds.

        :param int initial_backoff:
            The initial backoff interval, in seconds, for the first retry.
        :param int increment_base:
            The base, in seconds, to increment the initial_backoff by after the
            first retry.
        :param int max_attempts:
            The maximum number of retry attempts.
        :param bool retry_to_secondary:
            Whether the request should be retried to secondary, if able. This should
            only be enabled of RA-GRS accounts are used and potentially stale data
            can be handled.
        :param int random_jitter_range:
            A number in seconds which indicates a range to jitter/randomize for the back-off interval.
            For example, a random_jitter_range of 3 results in the back-off interval x to vary between x+3 and x-3.
        """
    def get_backoff_time(self, settings):
        """
        Calculates how long to sleep before retrying.

        :param Optional[Dict[str, Any]] settings: The configurable values pertaining to get backoff time.
        :returns:
            An integer indicating how long to wait before retrying the request,
            or None to indicate no retry should be performed.
        :rtype: int or None
        """

class LinearRetry(StorageRetryPolicy):
    """Linear retry."""
    backoff: Incomplete
    random_jitter_range: Incomplete
    def __init__(self, backoff: int = 15, retry_total: int = 3, retry_to_secondary: bool = False, random_jitter_range: int = 3, **kwargs) -> None:
        """
        Constructs a Linear retry object.

        :param int backoff:
            The backoff interval, in seconds, between retries.
        :param int max_attempts:
            The maximum number of retry attempts.
        :param bool retry_to_secondary:
            Whether the request should be retried to secondary, if able. This should
            only be enabled of RA-GRS accounts are used and potentially stale data
            can be handled.
        :param int random_jitter_range:
            A number in seconds which indicates a range to jitter/randomize for the back-off interval.
            For example, a random_jitter_range of 3 results in the back-off interval x to vary between x+3 and x-3.
        """
    def get_backoff_time(self, settings):
        """
        Calculates how long to sleep before retrying.

        :param Optional[Dict[str, Any]] settings: The configurable values pertaining to the backoff time.
        :returns:
            An integer indicating how long to wait before retrying the request,
            or None to indicate no retry should be performed.
        :rtype: int or None
        """

class StorageBearerTokenCredentialPolicy(BearerTokenCredentialPolicy):
    """ Custom Bearer token credential policy for following Storage Bearer challenges """
    def __init__(self, credential: TokenCredential, **kwargs: Any) -> None: ...
    def on_challenge(self, request: PipelineRequest, response: PipelineResponse) -> bool: ...
