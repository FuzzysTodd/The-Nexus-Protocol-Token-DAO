from ._base import SansIOHTTPPolicy as SansIOHTTPPolicy
from _typeshed import Incomplete
from azure.core.pipeline import PipelineRequest as PipelineRequest
from azure.core.pipeline.transport import HttpRequest as LegacyHttpRequest, HttpResponse as LegacyHttpResponse
from azure.core.rest import HttpRequest, HttpResponse
from typing import Any, List, TypeVar

HTTPResponseType = TypeVar('HTTPResponseType', HttpResponse, LegacyHttpResponse)
HTTPRequestType = TypeVar('HTTPRequestType', HttpRequest, LegacyHttpRequest)

class SensitiveHeaderCleanupPolicy(SansIOHTTPPolicy[HTTPRequestType, HTTPResponseType]):
    """A simple policy that cleans up sensitive headers

    :keyword list[str] blocked_redirect_headers: The headers to clean up when redirecting to another domain.
    :keyword bool disable_redirect_cleanup: Opt out cleaning up sensitive headers when redirecting to another domain.
    """
    DEFAULT_SENSITIVE_HEADERS: Incomplete
    def __init__(self, *, blocked_redirect_headers: List[str] | None = None, disable_redirect_cleanup: bool = False, **kwargs: Any) -> None: ...
    def on_request(self, request: PipelineRequest[HTTPRequestType]) -> None:
        """This is executed before sending the request to the next policy.

        :param request: The PipelineRequest object.
        :type request: ~azure.core.pipeline.PipelineRequest
        """
