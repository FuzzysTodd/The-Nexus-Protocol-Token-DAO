from .authentication import StorageHttpChallenge as StorageHttpChallenge
from .constants import DEFAULT_OAUTH_SCOPE as DEFAULT_OAUTH_SCOPE, STORAGE_OAUTH_SCOPE as STORAGE_OAUTH_SCOPE
from .policies import StorageRetryPolicy as StorageRetryPolicy, is_retry as is_retry
from _typeshed import Incomplete
from azure.core.credentials_async import AsyncTokenCredential as AsyncTokenCredential
from azure.core.pipeline import PipelineRequest as PipelineRequest, PipelineResponse as PipelineResponse
from azure.core.pipeline.policies import AsyncBearerTokenCredentialPolicy, AsyncHTTPPolicy
from typing import Any

async def retry_hook(settings, **kwargs) -> None: ...

class AsyncStorageResponseHook(AsyncHTTPPolicy):
    def __init__(self, **kwargs) -> None: ...
    async def send(self, request: PipelineRequest) -> PipelineResponse: ...

class AsyncStorageRetryPolicy(StorageRetryPolicy):
    """
    The base class for Exponential and Linear retries containing shared code.
    """
    async def sleep(self, settings, transport) -> None: ...
    async def send(self, request): ...

class ExponentialRetry(AsyncStorageRetryPolicy):
    """Exponential retry."""
    initial_backoff: Incomplete
    increment_base: Incomplete
    random_jitter_range: Incomplete
    def __init__(self, initial_backoff: int = 15, increment_base: int = 3, retry_total: int = 3, retry_to_secondary: bool = False, random_jitter_range: int = 3, **kwargs) -> None:
        """
        Constructs an Exponential retry object. The initial_backoff is used for
        the first retry. Subsequent retries are retried after initial_backoff +
        increment_power^retry_count seconds. For example, by default the first retry
        occurs after 15 seconds, the second after (15+3^1) = 18 seconds, and the
        third after (15+3^2) = 24 seconds.

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

        :return:
            An integer indicating how long to wait before retrying the request,
            or None to indicate no retry should be performed.
        :rtype: int or None
        """

class LinearRetry(AsyncStorageRetryPolicy):
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

        :return:
            An integer indicating how long to wait before retrying the request,
            or None to indicate no retry should be performed.
        :rtype: int or None
        """

class AsyncStorageBearerTokenCredentialPolicy(AsyncBearerTokenCredentialPolicy):
    """ Custom Bearer token credential policy for following Storage Bearer challenges """
    def __init__(self, credential: AsyncTokenCredential, **kwargs: Any) -> None: ...
    async def on_challenge(self, request: PipelineRequest, response: PipelineResponse) -> bool: ...
