from .transport import HttpTransport as HttpTransport
from azure.core.pipeline import PipelineRequest, PipelineResponse
from azure.core.pipeline.policies import HTTPPolicy, SansIOHTTPPolicy
from typing import Any, ContextManager, Dict, Generic, Iterable, TypeVar

HTTPResponseType = TypeVar('HTTPResponseType')
HTTPRequestType = TypeVar('HTTPRequestType')

def cleanup_kwargs_for_transport(kwargs: Dict[str, str]) -> None:
    '''Remove kwargs that are not meant for the transport layer.
    :param kwargs: The keyword arguments.
    :type kwargs: dict

    "insecure_domain_change" is used to indicate that a redirect
      has occurred to a different domain. This tells the SensitiveHeaderCleanupPolicy
      to clean up sensitive headers. We need to remove it before sending the request
      to the transport layer. This code is needed to handle the case that the
      SensitiveHeaderCleanupPolicy is not added into the pipeline and "insecure_domain_change" is not popped.
    "enable_cae" is added to the `get_token` method of the `TokenCredential` protocol.
    '''

class _SansIOHTTPPolicyRunner(HTTPPolicy[HTTPRequestType, HTTPResponseType]):
    """Sync implementation of the SansIO policy.

    Modifies the request and sends to the next policy in the chain.

    :param policy: A SansIO policy.
    :type policy: ~azure.core.pipeline.policies.SansIOHTTPPolicy
    """
    def __init__(self, policy: SansIOHTTPPolicy[HTTPRequestType, HTTPResponseType]) -> None: ...
    def send(self, request: PipelineRequest[HTTPRequestType]) -> PipelineResponse[HTTPRequestType, HTTPResponseType]:
        """Modifies the request and sends to the next policy in the chain.

        :param request: The PipelineRequest object.
        :type request: ~azure.core.pipeline.PipelineRequest
        :return: The PipelineResponse object.
        :rtype: ~azure.core.pipeline.PipelineResponse
        """

class _TransportRunner(HTTPPolicy[HTTPRequestType, HTTPResponseType]):
    """Transport runner.

    Uses specified HTTP transport type to send request and returns response.

    :param sender: The Http Transport instance.
    :type sender: ~azure.core.pipeline.transport.HttpTransport
    """
    def __init__(self, sender: HttpTransport[HTTPRequestType, HTTPResponseType]) -> None: ...
    def send(self, request: PipelineRequest[HTTPRequestType]) -> PipelineResponse[HTTPRequestType, HTTPResponseType]:
        """HTTP transport send method.

        :param request: The PipelineRequest object.
        :type request: ~azure.core.pipeline.PipelineRequest
        :return: The PipelineResponse object.
        :rtype: ~azure.core.pipeline.PipelineResponse
        """

class Pipeline(ContextManager['Pipeline'], Generic[HTTPRequestType, HTTPResponseType]):
    """A pipeline implementation.

    This is implemented as a context manager, that will activate the context
    of the HTTP sender. The transport is the last node in the pipeline.

    :param transport: The Http Transport instance
    :type transport: ~azure.core.pipeline.transport.HttpTransport
    :param list policies: List of configured policies.

    .. admonition:: Example:

        .. literalinclude:: ../samples/test_example_sync.py
            :start-after: [START build_pipeline]
            :end-before: [END build_pipeline]
            :language: python
            :dedent: 4
            :caption: Builds the pipeline for synchronous transport.
    """
    def __init__(self, transport: HttpTransport[HTTPRequestType, HTTPResponseType], policies: Iterable[HTTPPolicy[HTTPRequestType, HTTPResponseType] | SansIOHTTPPolicy[HTTPRequestType, HTTPResponseType]] | None = None) -> None: ...
    def __enter__(self) -> Pipeline[HTTPRequestType, HTTPResponseType]: ...
    def __exit__(self, *exc_details: Any) -> None: ...
    def run(self, request: HTTPRequestType, **kwargs: Any) -> PipelineResponse[HTTPRequestType, HTTPResponseType]:
        """Runs the HTTP Request through the chained policies.

        :param request: The HTTP request object.
        :type request: ~azure.core.pipeline.transport.HttpRequest
        :return: The PipelineResponse object
        :rtype: ~azure.core.pipeline.PipelineResponse
        """
