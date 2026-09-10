import abc
from _typeshed import Incomplete
from abc import ABC
from dataclasses import dataclass
from requests.adapters import Retry
from requests.sessions import Session
from sempy._utils._log import log_rest_request as log_rest_request, log_rest_response as log_rest_response, log_retry as log_retry
from sempy.fabric._token_provider import SynapseTokenProvider as SynapseTokenProvider, TokenProvider as TokenProvider
from sempy.fabric.exceptions import FabricHTTPException as FabricHTTPException

class RetryWithLogging(Retry):
    def increment(self, *args, **kwargs): ...

class SessionWithLogging(Session):
    def prepare_request(self, *args, **kwargs): ...

@dataclass
class OperationStatus:
    status: str
    retry_after: int
    percent_complete: int

class OperationStart:
    operation_id: str
    retry_after: int
    def __init__(self, response) -> None: ...

class BaseRestClient(ABC, metaclass=abc.ABCMeta):
    """
    REST client to access Fabric and PowerBI endpoints. Authentication tokens are automatically acquired from the execution environment.

    ***Experimental***: This class is experimental and may change in future versions.

    Parameters
    ----------
    token_provider : TokenProvider, default=None
        Implementation of TokenProvider that can provide auth token
        for access to the PowerBI workspace. Will attempt to acquire token
        from its execution environment if not provided.
    """
    http: Incomplete
    token_provider: Incomplete
    default_base_url: Incomplete
    def __init__(self, token_provider: TokenProvider | None = None) -> None: ...
    def request(self, method: str, path_or_url: str, *args, **kwargs):
        """
        Request to the Fabric and PowerBI REST API.

        Parameters
        ----------
        method : str
            HTTP method.
        path_or_url : str
            The path or the url to the resource.
        *args : list
            Arguments passed to the request method.
        **kwargs : dict
            Arguments passed to the request method.

        Returns
        -------
        requests.Response
            The response from the REST API.
        """
    def get(self, path_or_url: str, *args, **kwargs):
        """
        GET request to the Fabric and PowerBI REST API.

        Parameters
        ----------
        path_or_url : str
            The relative path to the resource or the full url.
            If it's relative, the base URL is automatically prepended.
        *args : list
            Arguments passed to the request method.
        **kwargs : dict
            Arguments passed to the request method.

        Returns
        -------
        requests.Response
            The response from the REST API.
        """
    def post(self, path_or_url: str, *args, **kwargs):
        """
        POST request to the Fabric and PowerBI REST API.

        Parameters
        ----------
        path_or_url : str
            The relative path to the resource or the full url.
            If it's relative, the base URL is automatically prepended.
        *args : list
            Arguments passed to the request method.
        **kwargs : dict
            Arguments passed to the request method.

        Returns
        -------
        requests.Response
            The response from the REST API.
        """
    def delete(self, path_or_url: str, *args, **kwargs):
        """
        DELETE request to the Fabric and PowerBI REST API.

        Parameters
        ----------
        path_or_url : str
            The relative path to the resource or the full url.
            If it's relative, the base URL is automatically prepended.
        *args : list
            Arguments passed to the request method.
        **kwargs : dict
            Arguments passed to the request method.

        Returns
        -------
        requests.Response
            The response from the REST API.
        """
    def head(self, path_or_url: str, *args, **kwargs):
        """
        HEAD request to the Fabric and PowerBI REST API.

        Parameters
        ----------
        path_or_url : str
            The relative path to the resource or the full url.
            If it's relative, the base URL is automatically prepended.
        *args : list
            Arguments passed to the request method.
        **kwargs : dict
            Arguments passed to the request method.

        Returns
        -------
        requests.Response
            The response from the REST API.
        """
    def patch(self, path_or_url: str, *args, **kwargs):
        """
        PATCH request to the Fabric and PowerBI REST API.

        Parameters
        ----------
        path_or_url : str
            The relative path to the resource or the full url.
            If it's relative, the base URL is automatically prepended.
        *args : list
            Arguments passed to the request method.
        **kwargs : dict
            Arguments passed to the request method.

        Returns
        -------
        requests.Response
            The response from the REST API.
        """
    def put(self, path_or_url: str, *args, **kwargs):
        """
        PUT request to the Fabric and PowerBI REST API.

        Parameters
        ----------
        path_or_url : str
            The relative path to the resource or the full url.
            If it's relative, the base URL is automatically prepended.
        *args : list
            Arguments passed to the request method.
        **kwargs : dict
            Arguments passed to the request method.

        Returns
        -------
        requests.Response
            The response from the REST API.
        """

class FabricRestClient(BaseRestClient):
    """
    REST client to access Fabric REST endpoints. Authentication tokens are automatically acquired from the execution environment.

    All methods (get, post, ...) have an additional parameter `lro_wait` that can be set to True to wait for the long-running-operation to complete.
    ***Experimental***: This class is experimental and may change in future versions.

    Parameters
    ----------
    token_provider : TokenProvider, default=None
        Implementation of TokenProvider that can provide auth token
        for access to the PowerBI workspace. Will attempt to acquire token
        from its execution environment if not provided.
    """
    def __init__(self, token_provider: TokenProvider | None = None) -> None: ...
    def request(self, method: str, path_or_url: str, lro_wait: bool | None = False, lro_max_attempts: int = 10, lro_operation_name: str | None = None, *args, **kwargs):
        """
        Request to the Fabric REST API.

        Parameters
        ----------
        method : str
            HTTP method.
        path_or_url : str
            The path or the url to the resource.
        lro_wait : bool, default=False
            If True, waits for the long-running-operation to complete.
        lro_max_attempts : int, default=10
            The maximum number of attempts to wait for the long-running-operation to complete.
        lro_operation_name : str, default=None
            The name of the operation to wait for displayed via TQDM.
        *args : list
            Arguments passed to the request method.
        **kwargs : dict
            Arguments passed to the request method.

        Returns
        -------
        requests.Response
            The response from the REST API.
        """
    def get_paged(self, path_or_url: str, headers: dict | None = None, *args, **kwargs) -> list:
        """
        GET request to the Fabric REST API that handles pagination.

        Parameters
        ----------
        path_or_url : str
            The relative path to the resource or the full url.
            If it's relative, the base URL is automatically prepended.
        headers : dict, default=None
            Headers to be included in the request.
        *args : list
            Arguments passed to the request method.
        **kwargs : dict
            Arguments passed to the request method.

        Returns
        -------
        list
            The list of rows from the response.
        """

class PowerBIRestClient(BaseRestClient):
    """
    REST client to access PowerBI REST endpoints. Authentication tokens are automatically acquired from the execution environment.

    ***Experimental***: This class is experimental and may change in future versions.

    Parameters
    ----------
    token_provider : TokenProvider, default=None
        Implementation of TokenProvider that can provide auth token
        for access to the PowerBI workspace. Will attempt to acquire token
        from its execution environment if not provided.
    """
    def __init__(self, token_provider: TokenProvider | None = None) -> None: ...
