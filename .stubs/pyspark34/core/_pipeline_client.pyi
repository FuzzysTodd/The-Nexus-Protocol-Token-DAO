from .configuration import Configuration as Configuration
from .pipeline import Pipeline as Pipeline
from .pipeline.policies import ContentDecodePolicy as ContentDecodePolicy, DistributedTracingPolicy as DistributedTracingPolicy, HttpLoggingPolicy as HttpLoggingPolicy, RequestIdPolicy as RequestIdPolicy, RetryPolicy as RetryPolicy, SensitiveHeaderCleanupPolicy as SensitiveHeaderCleanupPolicy
from .pipeline.transport import HttpTransport as HttpTransport
from .pipeline.transport._base import PipelineClientBase as PipelineClientBase
from typing import Any, Generic, TypeVar

HTTPResponseType = TypeVar('HTTPResponseType')
HTTPRequestType = TypeVar('HTTPRequestType')

class PipelineClient(PipelineClientBase, Generic[HTTPRequestType, HTTPResponseType]):
    """Service client core methods.

    Builds a Pipeline client.

    :param str base_url: URL for the request.
    :keyword ~azure.core.configuration.Configuration config: If omitted, the standard configuration is used.
    :keyword Pipeline pipeline: If omitted, a Pipeline object is created and returned.
    :keyword list[HTTPPolicy] policies: If omitted, the standard policies of the configuration object is used.
    :keyword per_call_policies: If specified, the policies will be added into the policy list before RetryPolicy
    :paramtype per_call_policies: Union[HTTPPolicy, SansIOHTTPPolicy, list[HTTPPolicy], list[SansIOHTTPPolicy]]
    :keyword per_retry_policies: If specified, the policies will be added into the policy list after RetryPolicy
    :paramtype per_retry_policies: Union[HTTPPolicy, SansIOHTTPPolicy, list[HTTPPolicy], list[SansIOHTTPPolicy]]
    :keyword HttpTransport transport: If omitted, RequestsTransport is used for synchronous transport.
    :return: A pipeline object.
    :rtype: ~azure.core.pipeline.Pipeline

    .. admonition:: Example:

        .. literalinclude:: ../samples/test_example_sync.py
            :start-after: [START build_pipeline_client]
            :end-before: [END build_pipeline_client]
            :language: python
            :dedent: 4
            :caption: Builds the pipeline client.
    """
    def __init__(self, base_url: str, *, pipeline: Pipeline[HTTPRequestType, HTTPResponseType] | None = None, config: Configuration[HTTPRequestType, HTTPResponseType] | None = None, **kwargs: Any) -> None: ...
    def __enter__(self) -> PipelineClient[HTTPRequestType, HTTPResponseType]: ...
    def __exit__(self, *exc_details: Any) -> None: ...
    def close(self) -> None: ...
    def send_request(self, request: HTTPRequestType, **kwargs: Any) -> HTTPResponseType:
        """Method that runs the network request through the client's chained policies.

        >>> from azure.core.rest import HttpRequest
        >>> request = HttpRequest('GET', 'http://www.example.com')
        <HttpRequest [GET], url: 'http://www.example.com'>
        >>> response = client.send_request(request)
        <HttpResponse: 200 OK>

        :param request: The network request you want to make. Required.
        :type request: ~azure.core.rest.HttpRequest
        :keyword bool stream: Whether the response payload will be streamed. Defaults to False.
        :return: The response of your network call. Does not do error handling on your response.
        :rtype: ~azure.core.rest.HttpResponse
        """
