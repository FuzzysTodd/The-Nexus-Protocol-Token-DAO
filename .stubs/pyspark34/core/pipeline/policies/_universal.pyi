import logging
from ...rest import HttpRequest as HttpRequest
from ...rest._rest_py3 import _HttpResponseBase as SansIOHttpResponse
from ..transport import HttpRequest as LegacyHttpRequest
from ..transport._base import _HttpResponseBase as LegacySansIOHttpResponse
from ._base import SansIOHTTPPolicy as SansIOHTTPPolicy
from _typeshed import Incomplete
from azure.core.pipeline import PipelineRequest as PipelineRequest, PipelineResponse
from typing import Any, AnyStr, Dict, IO, Mapping, Set

HTTPRequestType = LegacyHttpRequest | HttpRequest
HTTPResponseType = LegacySansIOHttpResponse | SansIOHttpResponse
PipelineResponseType = PipelineResponse[HTTPRequestType, HTTPResponseType]

class HeadersPolicy(SansIOHTTPPolicy[HTTPRequestType, HTTPResponseType]):
    """A simple policy that sends the given headers with the request.

    This will overwrite any headers already defined in the request. Headers can be
    configured up front, where any custom headers will be applied to all outgoing
    operations, and additional headers can also be added dynamically per operation.

    :param dict base_headers: Headers to send with the request.

    .. admonition:: Example:

        .. literalinclude:: ../samples/test_example_sansio.py
            :start-after: [START headers_policy]
            :end-before: [END headers_policy]
            :language: python
            :dedent: 4
            :caption: Configuring a headers policy.
    """
    def __init__(self, base_headers: Dict[str, str] | None = None, **kwargs: Any) -> None: ...
    @property
    def headers(self) -> Dict[str, str]:
        """The current headers collection.

        :rtype: dict[str, str]
        :return: The current headers collection.
        """
    def add_header(self, key: str, value: str) -> None:
        """Add a header to the configuration to be applied to all requests.

        :param str key: The header.
        :param str value: The header's value.
        """
    def on_request(self, request: PipelineRequest[HTTPRequestType]) -> None:
        """Updates with the given headers before sending the request to the next policy.

        :param request: The PipelineRequest object
        :type request: ~azure.core.pipeline.PipelineRequest
        """

class _Unset: ...

class RequestIdPolicy(SansIOHTTPPolicy[HTTPRequestType, HTTPResponseType]):
    '''A simple policy that sets the given request id in the header.

    This will overwrite request id that is already defined in the request. Request id can be
    configured up front, where the request id will be applied to all outgoing
    operations, and additional request id can also be set dynamically per operation.

    :keyword str request_id: The request id to be added into header.
    :keyword bool auto_request_id: Auto generates a unique request ID per call if true which is by default.
    :keyword str request_id_header_name: Header name to use. Default is "x-ms-client-request-id".

    .. admonition:: Example:

        .. literalinclude:: ../samples/test_example_sansio.py
            :start-after: [START request_id_policy]
            :end-before: [END request_id_policy]
            :language: python
            :dedent: 4
            :caption: Configuring a request id policy.
    '''
    def __init__(self, *, request_id: str | Any = ..., auto_request_id: bool = True, request_id_header_name: str = 'x-ms-client-request-id', **kwargs: Any) -> None: ...
    def set_request_id(self, value: str) -> None:
        """Add the request id to the configuration to be applied to all requests.

        :param str value: The request id value.
        """
    def on_request(self, request: PipelineRequest[HTTPRequestType]) -> None:
        """Updates with the given request id before sending the request to the next policy.

        :param request: The PipelineRequest object
        :type request: ~azure.core.pipeline.PipelineRequest
        """

class UserAgentPolicy(SansIOHTTPPolicy[HTTPRequestType, HTTPResponseType]):
    """User-Agent Policy. Allows custom values to be added to the User-Agent header.

    :param str base_user_agent: Sets the base user agent value.

    :keyword bool user_agent_overwrite: Overwrites User-Agent when True. Defaults to False.
    :keyword bool user_agent_use_env: Gets user-agent from environment. Defaults to True.
    :keyword str user_agent: If specified, this will be added in front of the user agent string.
    :keyword str sdk_moniker: If specified, the user agent string will be
        azsdk-python-[sdk_moniker] Python/[python_version] ([platform_version])

    .. admonition:: Example:

        .. literalinclude:: ../samples/test_example_sansio.py
            :start-after: [START user_agent_policy]
            :end-before: [END user_agent_policy]
            :language: python
            :dedent: 4
            :caption: Configuring a user agent policy.
    """
    overwrite: Incomplete
    use_env: Incomplete
    def __init__(self, base_user_agent: str | None = None, **kwargs: Any) -> None: ...
    @property
    def user_agent(self) -> str:
        """The current user agent value.

        :return: The current user agent value.
        :rtype: str
        """
    def add_user_agent(self, value: str) -> None:
        """Add value to current user agent with a space.
        :param str value: value to add to user agent.
        """
    def on_request(self, request: PipelineRequest[HTTPRequestType]) -> None:
        """Modifies the User-Agent header before the request is sent.

        :param request: The PipelineRequest object
        :type request: ~azure.core.pipeline.PipelineRequest
        """

class NetworkTraceLoggingPolicy(SansIOHTTPPolicy[HTTPRequestType, HTTPResponseType]):
    '''The logging policy in the pipeline is used to output HTTP network trace to the configured logger.

    This accepts both global configuration, and per-request level with "enable_http_logger"

    :param bool logging_enable: Use to enable per operation. Defaults to False.

    .. admonition:: Example:

        .. literalinclude:: ../samples/test_example_sansio.py
            :start-after: [START network_trace_logging_policy]
            :end-before: [END network_trace_logging_policy]
            :language: python
            :dedent: 4
            :caption: Configuring a network trace logging policy.
    '''
    enable_http_logger: Incomplete
    def __init__(self, logging_enable: bool = False, **kwargs: Any) -> None: ...
    def on_request(self, request: PipelineRequest[HTTPRequestType]) -> None:
        """Logs HTTP request to the DEBUG logger.

        :param request: The PipelineRequest object.
        :type request: ~azure.core.pipeline.PipelineRequest
        """
    def on_response(self, request: PipelineRequest[HTTPRequestType], response: PipelineResponse[HTTPRequestType, HTTPResponseType]) -> None:
        """Logs HTTP response to the DEBUG logger.

        :param request: The PipelineRequest object.
        :type request: ~azure.core.pipeline.PipelineRequest
        :param response: The PipelineResponse object.
        :type response: ~azure.core.pipeline.PipelineResponse
        """

class _HiddenClassProperties(type):
    @property
    def DEFAULT_HEADERS_WHITELIST(cls) -> Set[str]: ...
    @DEFAULT_HEADERS_WHITELIST.setter
    def DEFAULT_HEADERS_WHITELIST(cls, value: Set[str]) -> None: ...

class HttpLoggingPolicy(SansIOHTTPPolicy[HTTPRequestType, HTTPResponseType], metaclass=_HiddenClassProperties):
    """The Pipeline policy that handles logging of HTTP requests and responses.

    :param logger: The logger to use for logging. Default to azure.core.pipeline.policies.http_logging_policy.
    :type logger: logging.Logger
    """
    DEFAULT_HEADERS_ALLOWLIST: Set[str]
    REDACTED_PLACEHOLDER: str
    MULTI_RECORD_LOG: str
    logger: Incomplete
    allowed_query_params: Incomplete
    allowed_header_names: Incomplete
    def __init__(self, logger: logging.Logger | None = None, **kwargs: Any) -> None: ...
    def on_request(self, request: PipelineRequest[HTTPRequestType]) -> None:
        """Logs HTTP method, url and headers.
        :param request: The PipelineRequest object.
        :type request: ~azure.core.pipeline.PipelineRequest
        """
    def on_response(self, request: PipelineRequest[HTTPRequestType], response: PipelineResponse[HTTPRequestType, HTTPResponseType]) -> None: ...

class ContentDecodePolicy(SansIOHTTPPolicy[HTTPRequestType, HTTPResponseType]):
    """Policy for decoding unstreamed response content.

    :param response_encoding: The encoding to use if known for this service (will disable auto-detection)
    :type response_encoding: str
    """
    JSON_REGEXP: Incomplete
    CONTEXT_NAME: str
    def __init__(self, response_encoding: str | None = None, **kwargs: Any) -> None: ...
    @classmethod
    def deserialize_from_text(cls, data: AnyStr | IO[AnyStr] | None, mime_type: str | None = None, response: HTTPResponseType | None = None) -> Any:
        """Decode response data according to content-type.

        Accept a stream of data as well, but will be load at once in memory for now.
        If no content-type, will return the string version (not bytes, not stream)

        :param data: The data to deserialize.
        :type data: str or bytes or file-like object
        :param response: The HTTP response.
        :type response: ~azure.core.pipeline.transport.HttpResponse
        :param str mime_type: The mime type. As mime type, charset is not expected.
        :param response: If passed, exception will be annotated with that response
        :type response: any
        :raises ~azure.core.exceptions.DecodeError: If deserialization fails
        :returns: A dict (JSON), XML tree or str, depending of the mime_type
        :rtype: dict[str, Any] or xml.etree.ElementTree.Element or str
        """
    @classmethod
    def deserialize_from_http_generics(cls, response: HTTPResponseType, encoding: str | None = None) -> Any:
        '''Deserialize from HTTP response.

        Headers will tested for "content-type"

        :param response: The HTTP response
        :type response: any
        :param str encoding: The encoding to use if known for this service (will disable auto-detection)
        :raises ~azure.core.exceptions.DecodeError: If deserialization fails
        :returns: A dict (JSON), XML tree or str, depending of the mime_type
        :rtype: dict[str, Any] or xml.etree.ElementTree.Element or str
        '''
    def on_request(self, request: PipelineRequest[HTTPRequestType]) -> None: ...
    def on_response(self, request: PipelineRequest[HTTPRequestType], response: PipelineResponse[HTTPRequestType, HTTPResponseType]) -> None:
        """Extract data from the body of a REST response object.
        This will load the entire payload in memory.
        Will follow Content-Type to parse.
        We assume everything is UTF8 (BOM acceptable).

        :param request: The PipelineRequest object.
        :type request: ~azure.core.pipeline.PipelineRequest
        :param response: The PipelineResponse object.
        :type response: ~azure.core.pipeline.PipelineResponse
        :raises JSONDecodeError: If JSON is requested and parsing is impossible.
        :raises UnicodeDecodeError: If bytes is not UTF8
        :raises xml.etree.ElementTree.ParseError: If bytes is not valid XML
        :raises ~azure.core.exceptions.DecodeError: If deserialization fails
        """

class ProxyPolicy(SansIOHTTPPolicy[HTTPRequestType, HTTPResponseType]):
    """A proxy policy.

    Dictionary mapping protocol or protocol and host to the URL of the proxy
    to be used on each Request.

    :param dict proxies: Maps protocol or protocol and hostname to the URL
     of the proxy.

    .. admonition:: Example:

        .. literalinclude:: ../samples/test_example_sansio.py
            :start-after: [START proxy_policy]
            :end-before: [END proxy_policy]
            :language: python
            :dedent: 4
            :caption: Configuring a proxy policy.
    """
    proxies: Incomplete
    def __init__(self, proxies: Mapping[str, str] | None = None, **kwargs: Any) -> None: ...
    def on_request(self, request: PipelineRequest[HTTPRequestType]) -> None: ...
