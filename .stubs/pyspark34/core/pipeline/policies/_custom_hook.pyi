from ._base import SansIOHTTPPolicy as SansIOHTTPPolicy
from azure.core.pipeline import PipelineRequest as PipelineRequest, PipelineResponse as PipelineResponse
from azure.core.pipeline.transport import HttpRequest as LegacyHttpRequest, HttpResponse as LegacyHttpResponse
from azure.core.rest import HttpRequest, HttpResponse
from typing import Any, TypeVar

HTTPResponseType = TypeVar('HTTPResponseType', HttpResponse, LegacyHttpResponse)
HTTPRequestType = TypeVar('HTTPRequestType', HttpRequest, LegacyHttpRequest)

class CustomHookPolicy(SansIOHTTPPolicy[HTTPRequestType, HTTPResponseType]):
    """A simple policy that enable the given callback
    with the response.

    :keyword callback raw_request_hook: Callback function. Will be invoked on request.
    :keyword callback raw_response_hook: Callback function. Will be invoked on response.
    """
    def __init__(self, **kwargs: Any) -> None: ...
    def on_request(self, request: PipelineRequest[HTTPRequestType]) -> None:
        """This is executed before sending the request to the next policy.

        :param request: The PipelineRequest object.
        :type request: ~azure.core.pipeline.PipelineRequest
        """
    def on_response(self, request: PipelineRequest[HTTPRequestType], response: PipelineResponse[HTTPRequestType, HTTPResponseType]) -> None:
        """This is executed after the request comes back from the policy.

        :param request: The PipelineRequest object.
        :type request: ~azure.core.pipeline.PipelineRequest
        :param response: The PipelineResponse object.
        :type response: ~azure.core.pipeline.PipelineResponse
        """
