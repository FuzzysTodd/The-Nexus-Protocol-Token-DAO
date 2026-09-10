import abc
from _typeshed import Incomplete
from azure.core.pipeline import PipelineRequest as PipelineRequest, PipelineResponse as PipelineResponse
from typing import Any, Awaitable, Dict, Generic, TypeVar

HTTPResponseType = TypeVar('HTTPResponseType')
HTTPRequestType = TypeVar('HTTPRequestType')

class HTTPPolicy(abc.ABC, Generic[HTTPRequestType, HTTPResponseType], metaclass=abc.ABCMeta):
    """An HTTP policy ABC.

    Use with a synchronous pipeline.
    """
    next: HTTPPolicy[HTTPRequestType, HTTPResponseType]
    @abc.abstractmethod
    def send(self, request: PipelineRequest[HTTPRequestType]) -> PipelineResponse[HTTPRequestType, HTTPResponseType]:
        """Abstract send method for a synchronous pipeline. Mutates the request.

        Context content is dependent on the HttpTransport.

        :param request: The pipeline request object
        :type request: ~azure.core.pipeline.PipelineRequest
        :return: The pipeline response object.
        :rtype: ~azure.core.pipeline.PipelineResponse
        """

class SansIOHTTPPolicy(Generic[HTTPRequestType, HTTPResponseType]):
    """Represents a sans I/O policy.

    SansIOHTTPPolicy is a base class for policies that only modify or
    mutate a request based on the HTTP specification, and do not depend
    on the specifics of any particular transport. SansIOHTTPPolicy
    subclasses will function in either a Pipeline or an AsyncPipeline,
    and can act either before the request is done, or after.
    You can optionally make these methods coroutines (or return awaitable objects)
    but they will then be tied to AsyncPipeline usage.
    """
    def on_request(self, request: PipelineRequest[HTTPRequestType]) -> None | Awaitable[None]:
        """Is executed before sending the request from next policy.

        :param request: Request to be modified before sent from next policy.
        :type request: ~azure.core.pipeline.PipelineRequest
        """
    def on_response(self, request: PipelineRequest[HTTPRequestType], response: PipelineResponse[HTTPRequestType, HTTPResponseType]) -> None | Awaitable[None]:
        """Is executed after the request comes back from the policy.

        :param request: Request to be modified after returning from the policy.
        :type request: ~azure.core.pipeline.PipelineRequest
        :param response: Pipeline response object
        :type response: ~azure.core.pipeline.PipelineResponse
        """
    def on_exception(self, request: PipelineRequest[HTTPRequestType]) -> None:
        """Is executed if an exception is raised while executing the next policy.

        This method is executed inside the exception handler.

        :param request: The Pipeline request object
        :type request: ~azure.core.pipeline.PipelineRequest

        .. admonition:: Example:

            .. literalinclude:: ../samples/test_example_sansio.py
                :start-after: [START on_exception]
                :end-before: [END on_exception]
                :language: python
                :dedent: 4
        """

class RequestHistory(Generic[HTTPRequestType, HTTPResponseType]):
    """A container for an attempted request and the applicable response.

    This is used to document requests/responses that resulted in redirected/retried requests.

    :param http_request: The request.
    :type http_request: ~azure.core.pipeline.transport.HttpRequest
    :param http_response: The HTTP response.
    :type http_response: ~azure.core.pipeline.transport.HttpResponse
    :param Exception error: An error encountered during the request, or None if the response was received successfully.
    :param dict context: The pipeline context.
    """
    http_request: Incomplete
    http_response: Incomplete
    error: Incomplete
    context: Incomplete
    def __init__(self, http_request: HTTPRequestType, http_response: HTTPResponseType | None = None, error: Exception | None = None, context: Dict[str, Any] | None = None) -> None: ...
