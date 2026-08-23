from . import AsyncHTTPPolicy as AsyncHTTPPolicy
from ._redirect import RedirectPolicyBase as RedirectPolicyBase, domain_changed as domain_changed
from ._utils import get_domain as get_domain
from azure.core.pipeline import PipelineRequest as PipelineRequest, PipelineResponse as PipelineResponse
from azure.core.pipeline.transport import AsyncHttpResponse as LegacyAsyncHttpResponse, HttpRequest as LegacyHttpRequest
from azure.core.rest import AsyncHttpResponse, HttpRequest
from typing import TypeVar

AsyncHTTPResponseType = TypeVar('AsyncHTTPResponseType', AsyncHttpResponse, LegacyAsyncHttpResponse)
HTTPRequestType = TypeVar('HTTPRequestType', HttpRequest, LegacyHttpRequest)

class AsyncRedirectPolicy(RedirectPolicyBase, AsyncHTTPPolicy[HTTPRequestType, AsyncHTTPResponseType]):
    """An async redirect policy.

    An async redirect policy in the pipeline can be configured directly or per operation.

    :keyword bool permit_redirects: Whether the client allows redirects. Defaults to True.
    :keyword int redirect_max: The maximum allowed redirects. Defaults to 30.

    .. admonition:: Example:

        .. literalinclude:: ../samples/test_example_async.py
            :start-after: [START async_redirect_policy]
            :end-before: [END async_redirect_policy]
            :language: python
            :dedent: 4
            :caption: Configuring an async redirect policy.
    """
    async def send(self, request: PipelineRequest[HTTPRequestType]) -> PipelineResponse[HTTPRequestType, AsyncHTTPResponseType]:
        """Sends the PipelineRequest object to the next policy.
        Uses redirect settings to send the request to redirect endpoint if necessary.

        :param request: The PipelineRequest object
        :type request: ~azure.core.pipeline.PipelineRequest
        :return: Returns the PipelineResponse or raises error if maximum redirects exceeded.
        :rtype: ~azure.core.pipeline.PipelineResponse
        :raises: ~azure.core.exceptions.TooManyRedirectsError if maximum redirects exceeded.
        """
