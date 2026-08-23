from ..pipeline import PipelineContext as PipelineContext, PipelineRequest as PipelineRequest, PipelineResponse as PipelineResponse
from ..pipeline.policies import SansIOHTTPPolicy as SansIOHTTPPolicy
from typing import AsyncIterator, Generic, Type, TypeVar

HttpResponseType = TypeVar('HttpResponseType')

class _PartGenerator(AsyncIterator[HttpResponseType], Generic[HttpResponseType]):
    """Until parts is a real async iterator, wrap the sync call.

    :param response: The response to parse
    :type response: ~azure.core.pipeline.transport.AsyncHttpResponse
    :param default_http_response_type: The default HTTP response type to use
    :type default_http_response_type: any
    """
    def __init__(self, response, default_http_response_type: Type[HttpResponseType]) -> None: ...
    async def __anext__(self) -> HttpResponseType: ...
