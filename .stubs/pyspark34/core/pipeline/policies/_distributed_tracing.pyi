from azure.core.pipeline import PipelineRequest as PipelineRequest, PipelineResponse as PipelineResponse
from azure.core.pipeline.policies import SansIOHTTPPolicy
from azure.core.pipeline.transport import HttpRequest as LegacyHttpRequest, HttpResponse as LegacyHttpResponse
from azure.core.rest import HttpRequest, HttpResponse
from azure.core.tracing._abstract_span import AbstractSpan as AbstractSpan
from types import TracebackType
from typing import Any, Tuple, Type, TypeVar

HTTPResponseType = TypeVar('HTTPResponseType', HttpResponse, LegacyHttpResponse)
HTTPRequestType = TypeVar('HTTPRequestType', HttpRequest, LegacyHttpRequest)
ExcInfo = Tuple[Type[BaseException], BaseException, TracebackType]
OptExcInfo = ExcInfo | Tuple[None, None, None]

class DistributedTracingPolicy(SansIOHTTPPolicy[HTTPRequestType, HTTPResponseType]):
    """The policy to create spans for Azure calls.

    :keyword network_span_namer: A callable to customize the span name
    :type network_span_namer: callable[[~azure.core.pipeline.transport.HttpRequest], str]
    :keyword tracing_attributes: Attributes to set on all created spans
    :type tracing_attributes: dict[str, str]
    """
    TRACING_CONTEXT: str
    def __init__(self, **kwargs: Any) -> None: ...
    def on_request(self, request: PipelineRequest[HTTPRequestType]) -> None: ...
    def end_span(self, request: PipelineRequest[HTTPRequestType], response: HTTPResponseType | None = None, exc_info: OptExcInfo | None = None) -> None:
        """Ends the span that is tracing the network and updates its status.

        :param request: The PipelineRequest object
        :type request: ~azure.core.pipeline.PipelineRequest
        :param response: The HttpResponse object
        :type response: ~azure.core.rest.HTTPResponse or ~azure.core.pipeline.transport.HttpResponse
        :param exc_info: The exception information
        :type exc_info: tuple
        """
    def on_response(self, request: PipelineRequest[HTTPRequestType], response: PipelineResponse[HTTPRequestType, HTTPResponseType]) -> None: ...
    def on_exception(self, request: PipelineRequest[HTTPRequestType]) -> None: ...
