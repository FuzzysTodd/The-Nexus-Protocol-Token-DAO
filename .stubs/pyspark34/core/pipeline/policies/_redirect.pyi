from ._base import HTTPPolicy as HTTPPolicy, RequestHistory as RequestHistory
from ._utils import get_domain as get_domain
from _typeshed import Incomplete
from azure.core.pipeline import PipelineRequest as PipelineRequest, PipelineResponse as PipelineResponse
from azure.core.pipeline.transport import AsyncHttpResponse as LegacyAsyncHttpResponse, HttpRequest as LegacyHttpRequest, HttpResponse as LegacyHttpResponse
from azure.core.rest import AsyncHttpResponse, HttpRequest, HttpResponse
from typing import Any, Dict, TypeVar
from typing_extensions import Literal

HTTPResponseType = TypeVar('HTTPResponseType', HttpResponse, LegacyHttpResponse)
AllHttpResponseType = TypeVar('AllHttpResponseType', HttpResponse, LegacyHttpResponse, AsyncHttpResponse, LegacyAsyncHttpResponse)
HTTPRequestType = TypeVar('HTTPRequestType', HttpRequest, LegacyHttpRequest)
ClsRedirectPolicy = TypeVar('ClsRedirectPolicy', bound='RedirectPolicyBase')

def domain_changed(original_domain: str | None, url: str) -> bool:
    """Checks if the domain has changed.
    :param str original_domain: The original domain.
    :param str url: The new url.
    :rtype: bool
    :return: Whether the domain has changed.
    """

class RedirectPolicyBase:
    REDIRECT_STATUSES: Incomplete
    REDIRECT_HEADERS_BLACKLIST: Incomplete
    allow: Incomplete
    max_redirects: Incomplete
    def __init__(self, **kwargs: Any) -> None: ...
    @classmethod
    def no_redirects(cls) -> ClsRedirectPolicy:
        """Disable redirects.

        :return: A redirect policy with redirects disabled.
        :rtype: ~azure.core.pipeline.policies.RedirectPolicy or ~azure.core.pipeline.policies.AsyncRedirectPolicy
        """
    def configure_redirects(self, options: Dict[str, Any]) -> Dict[str, Any]:
        """Configures the redirect settings.

        :param options: Keyword arguments from context.
        :type options: dict
        :return: A dict containing redirect settings and a history of redirects.
        :rtype: dict
        """
    def get_redirect_location(self, response: PipelineResponse[Any, AllHttpResponseType]) -> str | None | Literal[False]:
        """Checks for redirect status code and gets redirect location.

        :param response: The PipelineResponse object
        :type response: ~azure.core.pipeline.PipelineResponse
        :return: Truthy redirect location string if we got a redirect status
         code and valid location. ``None`` if redirect status and no
         location. ``False`` if not a redirect status code.
        :rtype: str or bool or None
        """
    def increment(self, settings: Dict[str, Any], response: PipelineResponse[Any, AllHttpResponseType], redirect_location: str) -> bool:
        """Increment the redirect attempts for this request.

        :param dict settings: The redirect settings
        :param response: A pipeline response object.
        :type response: ~azure.core.pipeline.PipelineResponse
        :param str redirect_location: The redirected endpoint.
        :return: Whether further redirect attempts are remaining.
         False if exhausted; True if more redirect attempts available.
        :rtype: bool
        """

class RedirectPolicy(RedirectPolicyBase, HTTPPolicy[HTTPRequestType, HTTPResponseType]):
    """A redirect policy.

    A redirect policy in the pipeline can be configured directly or per operation.

    :keyword bool permit_redirects: Whether the client allows redirects. Defaults to True.
    :keyword int redirect_max: The maximum allowed redirects. Defaults to 30.

    .. admonition:: Example:

        .. literalinclude:: ../samples/test_example_sync.py
            :start-after: [START redirect_policy]
            :end-before: [END redirect_policy]
            :language: python
            :dedent: 4
            :caption: Configuring a redirect policy.
    """
    def send(self, request: PipelineRequest[HTTPRequestType]) -> PipelineResponse[HTTPRequestType, HTTPResponseType]:
        """Sends the PipelineRequest object to the next policy.
        Uses redirect settings to send request to redirect endpoint if necessary.

        :param request: The PipelineRequest object
        :type request: ~azure.core.pipeline.PipelineRequest
        :return: Returns the PipelineResponse or raises error if maximum redirects exceeded.
        :rtype: ~azure.core.pipeline.PipelineResponse
        :raises: ~azure.core.exceptions.TooManyRedirectsError if maximum redirects exceeded.
        """
