import requests
from . import __version__ as __version__
from .exceptions import DatalakeBadOffsetException as DatalakeBadOffsetException, DatalakeRESTException as DatalakeRESTException, FileNotFoundError as FileNotFoundError, PermissionError as PermissionError
from .retry import ExponentialRetryPolicy as ExponentialRetryPolicy, retry_decorator_for_auth as retry_decorator_for_auth
from _typeshed import Incomplete

enforce_no_py_open_ssl: Incomplete
logger: Incomplete
default_client: Incomplete
default_store: Incomplete
default_adls_suffix: Incomplete
DEFAULT_RESOURCE_ENDPOINT: str
MAX_CONTENT_LENGTH: Incomplete
MAX_POOL_CONNECTIONS: int

def auth(tenant_id: Incomplete | None = None, username: Incomplete | None = None, password: Incomplete | None = None, client_id=..., client_secret: Incomplete | None = None, resource=..., require_2fa: bool = False, authority: Incomplete | None = None, retry_policy: Incomplete | None = None, **kwargs):
    ''' User/password authentication

    Parameters
    ----------

    tenant_id: str
        associated with the user\'s subscription, or "common"
    username: str
        active directory user
    password: str
        sign-in password
    client_id: str
        the service principal client
    client_secret: str
        the secret associated with the client_id
    resource: str
        resource for auth (e.g., https://datalake.azure.net/)
    require_2fa: bool
        indicates this authentication attempt requires two-factor authentication
    authority: string
        The full URI of the authentication authority to authenticate against (such as https://login.microsoftonline.com/)
    kwargs: key/values
        Other parameters, for future use

    Returns
    -------
    :type DataLakeCredential :mod: `A DataLakeCredential object`
    '''

class DataLakeCredential:
    token: Incomplete
    def __init__(self, token) -> None: ...
    def signed_session(self) -> requests.Session:
        """Create requests session with any required auth headers applied.

        :rtype: requests.Session
        """
    def refresh_token(self, authority: Incomplete | None = None) -> None:
        """ Refresh an expired authorization token

        Parameters
        ----------
        authority: string
            The full URI of the authentication authority to authenticate against (such as https://login.microsoftonline.com/)
        """

class DatalakeRESTInterface:
    """ Call factory for webHDFS endpoints on ADLS

    Parameters
    ----------
    store_name: str
        The name of the Data Lake Store account to execute operations against.
    token: dict
        from `auth()` or `refresh_token()` or other ADAL source
    url_suffix: str (None)
        Domain to send REST requests to. The end-point URL is constructed
        using this and the store_name. If None, use default.
    api_version: str (2018-09-01)
        The API version to target with requests. Changing this value will
        change the behavior of the requests, and can cause unexpected behavior or
        breaking changes. Changes to this value should be undergone with caution.
    req_timeout_s: float(60)
        This is the timeout for each requests library call.
    kwargs: optional arguments to auth
        See ``auth()``. Includes, e.g., username, password, tenant; will pull
        values from environment variables if not provided.
    """
    ends: Incomplete
    local: Incomplete
    token: Incomplete
    api_version: Incomplete
    head: Incomplete
    url: Incomplete
    webhdfs: str
    extended_operations: str
    user_agent: Incomplete
    req_timeout_s: Incomplete
    def __init__(self, store_name=..., token: Incomplete | None = None, url_suffix=..., api_version: str = '2018-09-01', req_timeout_s: int = 60, **kwargs) -> None: ...
    @property
    def session(self): ...
    def log_response_and_raise(self, response, exception, level=...) -> None: ...
    def call(self, op, path: str = '', is_extended: bool = False, expected_error_code: Incomplete | None = None, retry_policy: Incomplete | None = None, headers={}, **kwargs):
        """ Execute a REST call

        Parameters
        ----------
        op: str
            webHDFS operation to perform, one of `DatalakeRESTInterface.ends`
        path: str
            filepath on the remote system
        is_extended: bool (False)
            Indicates if the API call comes from the webhdfs extensions path or the basic webhdfs path.
            By default, all requests target the official webhdfs path. A small subset of custom convenience
            methods specific to Azure Data Lake Store target the extension path (such as SETEXPIRY).
        expected_error_code: int
            Optionally indicates a specific, expected error code, if any. In the event that this error
            is returned, the exception will be logged to DEBUG instead of ERROR stream. The exception
            will still be raised, however, as it is expected that the caller will expect to handle it
            and do something different if it is raised.
        kwargs: dict
            other parameters, as defined by the webHDFS standard and
            https://msdn.microsoft.com/en-us/library/mt710547.aspx
        """
    def is_successful_response(self, response, exception): ...
