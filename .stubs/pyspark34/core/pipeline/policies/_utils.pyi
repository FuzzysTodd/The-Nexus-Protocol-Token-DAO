from .. import PipelineResponse as PipelineResponse
from ...utils._utils import case_insensitive_dict as case_insensitive_dict
from azure.core.pipeline.transport import AsyncHttpResponse as LegacyAsyncHttpResponse, HttpRequest as LegacyHttpRequest, HttpResponse as LegacyHttpResponse
from azure.core.rest import AsyncHttpResponse, HttpRequest, HttpResponse

AllHttpResponseType = HttpResponse | LegacyHttpResponse | AsyncHttpResponse | LegacyAsyncHttpResponse
HTTPRequestType = HttpRequest | LegacyHttpRequest

def parse_retry_after(retry_after: str) -> float:
    """Helper to parse Retry-After and get value in seconds.

    :param str retry_after: Retry-After header
    :rtype: float
    :return: Value of Retry-After in seconds.
    """
def get_retry_after(response: PipelineResponse[HTTPRequestType, AllHttpResponseType]) -> float | None:
    """Get the value of Retry-After in seconds.

    :param response: The PipelineResponse object
    :type response: ~azure.core.pipeline.PipelineResponse
    :return: Value of Retry-After in seconds.
    :rtype: float or None
    """
def get_domain(url: str) -> str:
    """Get the domain of an url.

    :param str url: The url.
    :rtype: str
    :return: The domain of the url.
    """
