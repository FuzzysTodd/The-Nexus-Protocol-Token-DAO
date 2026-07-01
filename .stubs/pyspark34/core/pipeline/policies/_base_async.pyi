import abc
from .. import PipelineRequest as PipelineRequest, PipelineResponse as PipelineResponse
from typing import Generic, TypeVar

AsyncHTTPResponseType = TypeVar('AsyncHTTPResponseType')
HTTPResponseType = TypeVar('HTTPResponseType')
HTTPRequestType = TypeVar('HTTPRequestType')

class AsyncHTTPPolicy(abc.ABC, Generic[HTTPRequestType, AsyncHTTPResponseType], metaclass=abc.ABCMeta):
    """An async HTTP policy ABC.

    Use with an asynchronous pipeline.
    """
    next: AsyncHTTPPolicy[HTTPRequestType, AsyncHTTPResponseType]
    @abc.abstractmethod
    async def send(self, request: PipelineRequest[HTTPRequestType]) -> PipelineResponse[HTTPRequestType, AsyncHTTPResponseType]:
        """Abstract send method for a asynchronous pipeline. Mutates the request.

        Context content is dependent on the HttpTransport.

        :param request: The pipeline request object.
        :type request: ~azure.core.pipeline.PipelineRequest
        :return: The pipeline response object.
        :rtype: ~azure.core.pipeline.PipelineResponse
        """
