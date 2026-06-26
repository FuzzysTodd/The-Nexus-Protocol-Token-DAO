from _typeshed import Incomplete
from google.auth import transport

RequestMethods: Incomplete

class _Response(transport.Response):
    """urllib3 transport response adapter.

    Args:
        response (urllib3.response.HTTPResponse): The raw urllib3 response.
    """
    def __init__(self, response) -> None: ...
    @property
    def status(self): ...
    @property
    def headers(self): ...
    @property
    def data(self): ...

class Request(transport.Request):
    """urllib3 request adapter.

    This class is used internally for making requests using various transports
    in a consistent way. If you use :class:`AuthorizedHttp` you do not need
    to construct or use this class directly.

    This class can be useful if you want to manually refresh a
    :class:`~google.auth.credentials.Credentials` instance::

        import google.auth.transport.urllib3
        import urllib3

        http = urllib3.PoolManager()
        request = google.auth.transport.urllib3.Request(http)

        credentials.refresh(request)

    Args:
        http (urllib3.request.RequestMethods): An instance of any urllib3
            class that implements :class:`~urllib3.request.RequestMethods`,
            usually :class:`urllib3.PoolManager`.

    .. automethod:: __call__
    """
    http: Incomplete
    def __init__(self, http) -> None: ...
    def __call__(self, url, method: str = 'GET', body: Incomplete | None = None, headers: Incomplete | None = None, timeout: Incomplete | None = None, **kwargs):
        """Make an HTTP request using urllib3.

        Args:
            url (str): The URI to be requested.
            method (str): The HTTP method to use for the request. Defaults
                to 'GET'.
            body (bytes): The payload / body in HTTP request.
            headers (Mapping[str, str]): Request headers.
            timeout (Optional[int]): The number of seconds to wait for a
                response from the server. If not specified or if None, the
                urllib3 default timeout will be used.
            kwargs: Additional arguments passed throught to the underlying
                urllib3 :meth:`urlopen` method.

        Returns:
            google.auth.transport.Response: The HTTP response.

        Raises:
            google.auth.exceptions.TransportError: If any exception occurred.
        """

class AuthorizedHttp(RequestMethods):
    '''A urllib3 HTTP class with credentials.

    This class is used to perform requests to API endpoints that require
    authorization::

        from google.auth.transport.urllib3 import AuthorizedHttp

        authed_http = AuthorizedHttp(credentials)

        response = authed_http.request(
            \'GET\', \'https://www.googleapis.com/storage/v1/b\')

    This class implements :class:`urllib3.request.RequestMethods` and can be
    used just like any other :class:`urllib3.PoolManager`.

    The underlying :meth:`urlopen` implementation handles adding the
    credentials\' headers to the request and refreshing credentials as needed.

    This class also supports mutual TLS via :meth:`configure_mtls_channel`
    method. In order to use this method, the `GOOGLE_API_USE_CLIENT_CERTIFICATE`
    environment variable must be explicitly set to `true`, otherwise it does
    nothing. Assume the environment is set to `true`, the method behaves in the
    following manner:
    If client_cert_callback is provided, client certificate and private
    key are loaded using the callback; if client_cert_callback is None,
    application default SSL credentials will be used. Exceptions are raised if
    there are problems with the certificate, private key, or the loading process,
    so it should be called within a try/except block.

    First we set the environment variable to `true`, then create an :class:`AuthorizedHttp`
    instance and specify the endpoints::

        regular_endpoint = \'https://pubsub.googleapis.com/v1/projects/{my_project_id}/topics\'
        mtls_endpoint = \'https://pubsub.mtls.googleapis.com/v1/projects/{my_project_id}/topics\'

        authed_http = AuthorizedHttp(credentials)

    Now we can pass a callback to :meth:`configure_mtls_channel`::

        def my_cert_callback():
            # some code to load client cert bytes and private key bytes, both in
            # PEM format.
            some_code_to_load_client_cert_and_key()
            if loaded:
                return cert, key
            raise MyClientCertFailureException()

        # Always call configure_mtls_channel within a try/except block.
        try:
            is_mtls = authed_http.configure_mtls_channel(my_cert_callback)
        except:
            # handle exceptions.

        if is_mtls:
            response = authed_http.request(\'GET\', mtls_endpoint)
        else:
            response = authed_http.request(\'GET\', regular_endpoint)

    You can alternatively use application default SSL credentials like this::

        try:
            is_mtls = authed_http.configure_mtls_channel()
        except:
            # handle exceptions.

    Args:
        credentials (google.auth.credentials.Credentials): The credentials to
            add to the request.
        http (urllib3.PoolManager): The underlying HTTP object to
            use to make requests. If not specified, a
            :class:`urllib3.PoolManager` instance will be constructed with
            sane defaults.
        refresh_status_codes (Sequence[int]): Which HTTP status codes indicate
            that credentials should be refreshed and the request should be
            retried.
        max_refresh_attempts (int): The maximum number of times to attempt to
            refresh the credentials and retry the request.
        default_host (Optional[str]): A host like "pubsub.googleapis.com".
            This is used when a self-signed JWT is created from service
            account credentials.
    '''
    http: Incomplete
    credentials: Incomplete
    def __init__(self, credentials, http: Incomplete | None = None, refresh_status_codes=..., max_refresh_attempts=..., default_host: Incomplete | None = None) -> None: ...
    def configure_mtls_channel(self, client_cert_callback: Incomplete | None = None):
        """Configures mutual TLS channel using the given client_cert_callback or
        application default SSL credentials. The behavior is controlled by
        `GOOGLE_API_USE_CLIENT_CERTIFICATE` environment variable.
        (1) If the environment variable value is `true`, the function returns True
        if the channel is mutual TLS and False otherwise. The `http` provided
        in the constructor will be overwritten.
        (2) If the environment variable is not set or `false`, the function does
        nothing and it always return False.

        Args:
            client_cert_callback (Optional[Callable[[], (bytes, bytes)]]):
                The optional callback returns the client certificate and private
                key bytes both in PEM format.
                If the callback is None, application default SSL credentials
                will be used.

        Returns:
            True if the channel is mutual TLS and False otherwise.

        Raises:
            google.auth.exceptions.MutualTLSChannelError: If mutual TLS channel
                creation failed for any reason.
        """
    def urlopen(self, method, url, body: Incomplete | None = None, headers: Incomplete | None = None, **kwargs):
        """Implementation of urllib3's urlopen."""
    def __enter__(self):
        """Proxy to ``self.http``."""
    def __exit__(self, exc_type: type[BaseException] | None, exc_val: BaseException | None, exc_tb: types.TracebackType | None):
        """Proxy to ``self.http``."""
    def __del__(self) -> None: ...
    @property
    def headers(self):
        """Proxy to ``self.http``."""
    @headers.setter
    def headers(self, value) -> None:
        """Proxy to ``self.http``."""
