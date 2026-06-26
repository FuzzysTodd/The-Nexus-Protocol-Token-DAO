from .pipeline.policies import AsyncHTTPPolicy as AsyncHTTPPolicy, HTTPPolicy as HTTPPolicy, SansIOHTTPPolicy as SansIOHTTPPolicy
from _typeshed import Incomplete
from typing import Any, Generic, TypeVar

HTTPResponseType = TypeVar('HTTPResponseType')
HTTPRequestType = TypeVar('HTTPRequestType')
AnyPolicy = HTTPPolicy[HTTPRequestType, HTTPResponseType] | AsyncHTTPPolicy[HTTPRequestType, HTTPResponseType] | SansIOHTTPPolicy[HTTPRequestType, HTTPResponseType]

class Configuration(Generic[HTTPRequestType, HTTPResponseType]):
    """Provides the home for all of the configurable policies in the pipeline.

    A new Configuration object provides no default policies and does not specify in what
    order the policies will be added to the pipeline. The SDK developer must specify each
    of the policy defaults as required by the service and use the policies in the
    Configuration to construct the pipeline correctly, as well as inserting any
    unexposed/non-configurable policies.

    :ivar headers_policy: Provides parameters for custom or additional headers to be sent with the request.
    :ivar proxy_policy: Provides configuration parameters for proxy.
    :ivar redirect_policy: Provides configuration parameters for redirects.
    :ivar retry_policy: Provides configuration parameters for retries in the pipeline.
    :ivar custom_hook_policy: Provides configuration parameters for a custom hook.
    :ivar logging_policy: Provides configuration parameters for logging.
    :ivar http_logging_policy: Provides configuration parameters for HTTP specific logging.
    :ivar user_agent_policy: Provides configuration parameters to append custom values to the
     User-Agent header.
    :ivar authentication_policy: Provides configuration parameters for adding a bearer token Authorization
     header to requests.
    :ivar request_id_policy: Provides configuration parameters for adding a request id to requests.
    :keyword polling_interval: Polling interval while doing LRO operations, if Retry-After is not set.

    .. admonition:: Example:

        .. literalinclude:: ../samples/test_example_config.py
            :start-after: [START configuration]
            :end-before: [END configuration]
            :language: python
            :caption: Creates the service configuration and adds policies.
    """
    headers_policy: Incomplete
    proxy_policy: Incomplete
    redirect_policy: Incomplete
    retry_policy: Incomplete
    custom_hook_policy: Incomplete
    logging_policy: Incomplete
    http_logging_policy: Incomplete
    user_agent_policy: Incomplete
    authentication_policy: Incomplete
    request_id_policy: Incomplete
    polling_interval: Incomplete
    def __init__(self, **kwargs: Any) -> None: ...

class ConnectionConfiguration:
    """HTTP transport connection configuration settings.

    Common properties that can be configured on all transports. Found in the
    Configuration object.

    :keyword float connection_timeout: A single float in seconds for the connection timeout. Defaults to 300 seconds.
    :keyword float read_timeout: A single float in seconds for the read timeout. Defaults to 300 seconds.
    :keyword connection_verify: SSL certificate verification. Enabled by default. Set to False to disable,
     alternatively can be set to the path to a CA_BUNDLE file or directory with certificates of trusted CAs.
    :paramtype connection_verify: bool or str
    :keyword str connection_cert: Client-side certificates. You can specify a local cert to use as client side
     certificate, as a single file (containing the private key and the certificate) or as a tuple of both files' paths.
    :keyword int connection_data_block_size: The block size of data sent over the connection. Defaults to 4096 bytes.

    .. admonition:: Example:

        .. literalinclude:: ../samples/test_example_config.py
            :start-after: [START connection_configuration]
            :end-before: [END connection_configuration]
            :language: python
            :dedent: 4
            :caption: Configuring transport connection settings.
    """
    timeout: Incomplete
    read_timeout: Incomplete
    verify: Incomplete
    cert: Incomplete
    data_block_size: Incomplete
    def __init__(self, *, connection_timeout: float = 300, read_timeout: float = 300, connection_verify: bool | str = True, connection_cert: str | None = None, connection_data_block_size: int = 4096, **kwargs: Any) -> None: ...
