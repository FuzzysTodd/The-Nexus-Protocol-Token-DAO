import typing as ty
from _typeshed import Incomplete
from abc import ABC, ABCMeta, abstractmethod
from http.cookies import SimpleCookie
from jupyter_server import DEFAULT_EVENTS_SCHEMA_PATH as DEFAULT_EVENTS_SCHEMA_PATH, JUPYTER_SERVER_EVENTS_URI as JUPYTER_SERVER_EVENTS_URI
from tornado.httpclient import HTTPResponse as HTTPResponse
from traitlets.config import LoggingConfigurable, SingletonConfigurable

ERROR_STATUS: str
SUCCESS_STATUS: str
STATUS_KEY: str
STATUS_CODE_KEY: str
MESSAGE_KEY: str

class GatewayTokenRenewerMeta(ABCMeta, Incomplete):
    """The metaclass necessary for proper ABC behavior in a Configurable."""

class GatewayTokenRenewerBase(ABC, LoggingConfigurable, metaclass=GatewayTokenRenewerMeta):
    """
    Abstract base class for refreshing tokens used between this server and a Gateway
    server.  Implementations requiring additional configuration can extend their class
    with appropriate configuration values or convey those values via appropriate
    environment variables relative to the implementation.
    """
    @abstractmethod
    def get_token(self, auth_header_key: str, auth_scheme: str | None, auth_token: str, **kwargs: ty.Any) -> str:
        """
        Given the current authorization header key, scheme, and token, this method returns
        a (potentially renewed) token for use against the Gateway server.
        """

class NoOpTokenRenewer(GatewayTokenRenewerBase):
    """NoOpTokenRenewer is the default value to the GatewayClient trait
    `gateway_token_renewer` and merely returns the provided token.
    """
    def get_token(self, auth_header_key: str, auth_scheme: str | None, auth_token: str, **kwargs: ty.Any) -> str:
        """This implementation simply returns the current authorization token."""

class GatewayClient(SingletonConfigurable):
    """This class manages the configuration.  It's its own singleton class so
    that we can share these values across all objects.  It also contains some
    options.
    helper methods to build request arguments out of the various config
    """
    event_schema_id: Incomplete
    event_logger: Incomplete
    def emit(self, data) -> None:
        """Emit event using the core event schema from Jupyter Server's Gateway Client."""
    url: Incomplete
    url_env: str
    ws_url: Incomplete
    ws_url_env: str
    kernels_endpoint_default_value: str
    kernels_endpoint_env: str
    kernels_endpoint: Incomplete
    kernelspecs_endpoint_default_value: str
    kernelspecs_endpoint_env: str
    kernelspecs_endpoint: Incomplete
    kernelspecs_resource_endpoint_default_value: str
    kernelspecs_resource_endpoint_env: str
    kernelspecs_resource_endpoint: Incomplete
    connect_timeout_default_value: float
    connect_timeout_env: str
    connect_timeout: Incomplete
    request_timeout_default_value: float
    request_timeout_env: str
    request_timeout: Incomplete
    client_key: Incomplete
    client_key_env: str
    client_cert: Incomplete
    client_cert_env: str
    ca_certs: Incomplete
    ca_certs_env: str
    http_user: Incomplete
    http_user_env: str
    http_pwd: Incomplete
    http_pwd_env: str
    headers_default_value: str
    headers_env: str
    headers: Incomplete
    auth_header_key_default_value: str
    auth_header_key: Incomplete
    auth_header_key_env: str
    auth_token_default_value: str
    auth_token: Incomplete
    auth_token_env: str
    auth_scheme_default_value: str
    auth_scheme: Incomplete
    auth_scheme_env: str
    validate_cert_default_value: bool
    validate_cert_env: str
    validate_cert: Incomplete
    allowed_envs_default_value: str
    allowed_envs_env: str
    allowed_envs: Incomplete
    env_whitelist: Incomplete
    gateway_retry_interval_default_value: float
    gateway_retry_interval_env: str
    gateway_retry_interval: Incomplete
    gateway_retry_interval_max_default_value: float
    gateway_retry_interval_max_env: str
    gateway_retry_interval_max: Incomplete
    gateway_retry_max_default_value: int
    gateway_retry_max_env: str
    gateway_retry_max: Incomplete
    gateway_token_renewer_class_default_value: str
    gateway_token_renewer_class_env: str
    gateway_token_renewer_class: Incomplete
    launch_timeout_pad_default_value: float
    launch_timeout_pad_env: str
    launch_timeout_pad: Incomplete
    accept_cookies_value: bool
    accept_cookies_env: str
    accept_cookies: Incomplete
    @property
    def gateway_enabled(self): ...
    KERNEL_LAUNCH_TIMEOUT: Incomplete
    gateway_token_renewer: GatewayTokenRenewerBase
    def __init__(self, **kwargs) -> None:
        """Initialize a gateway client."""
    def init_connection_args(self) -> None:
        """Initialize arguments used on every request.  Since these are primarily static values,
        we'll perform this operation once.
        """
    def load_connection_args(self, **kwargs):
        """Merges the static args relative to the connection, with the given keyword arguments.  If statics
        have yet to be initialized, we'll do that here.

        """
    def update_cookies(self, cookie: SimpleCookie) -> None:
        """Update cookies from existing requests for load balancers"""

class RetryableHTTPClient:
    """
    Inspired by urllib.util.Retry (https://urllib3.readthedocs.io/en/stable/reference/urllib3.util.html),
    this class is initialized with desired retry characteristics, uses a recursive method `fetch()` against an instance
    of `AsyncHTTPClient` which tracks the current retry count across applicable request retries.
    """
    MAX_RETRIES_DEFAULT: int
    MAX_RETRIES_CAP: int
    max_retries: int
    retried_methods: ty.Set[str]
    retried_errors: ty.Set[int]
    retried_exceptions: ty.Set[type]
    backoff_factor: float
    retry_count: int
    client: Incomplete
    def __init__(self) -> None:
        """Initialize the retryable http client."""
    async def fetch(self, endpoint: str, **kwargs: ty.Any) -> HTTPResponse:
        """
        Retryable AsyncHTTPClient.fetch() method.  When the request fails, this method will
        recurse up to max_retries times if the condition deserves a retry.
        """

async def gateway_request(endpoint: str, **kwargs: ty.Any) -> HTTPResponse:
    """Make an async request to kernel gateway endpoint, returns a response"""
