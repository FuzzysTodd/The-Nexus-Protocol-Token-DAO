import requests
from . import version as version
from _typeshed import Incomplete
from databricks_cli.sdk.version import UC_API_VERSION as UC_API_VERSION
from requests.adapters import HTTPAdapter

class TlsV1HttpAdapter(HTTPAdapter):
    """
    A HTTP adapter implementation that specifies the ssl version to be TLS1.
    This avoids problems with openssl versions that
    use SSL3 as a default (which is not supported by the server side).
    """
    poolmanager: Incomplete
    def init_poolmanager(self, connections, maxsize, block: bool = False) -> None: ...

class FallbackNetrcAuth(requests.auth.AuthBase):
    """Force requests to ignore the ``.netrc`` if other authentication 
    methods have been setup. Fallback to ``.netrc`` if not. 

    Use with::

        requests.get(url, auth=FallbackNetrcAuth())
        
        s = requests.Session()
        s.auth = FallbackNetrcAuth()
    """
    def __call__(self, r): ...

class ApiClient:
    """
    A partial Python implementation of dbc rest api
    to be used by different versions of the client.
    """
    session: Incomplete
    url: Incomplete
    default_headers: Incomplete
    verify: Incomplete
    api_version: Incomplete
    jobs_api_version: Incomplete
    def __init__(self, user: Incomplete | None = None, password: Incomplete | None = None, host: Incomplete | None = None, token: Incomplete | None = None, api_version=..., default_headers={}, verify: bool = True, command_name: str = '', jobs_api_version: Incomplete | None = None) -> None: ...
    def close(self) -> None:
        """Close the client"""
    def perform_query(self, method, path, data={}, headers: Incomplete | None = None, files: Incomplete | None = None, version: Incomplete | None = None):
        """set up connection and perform query"""
    def get_url(self, path, version: Incomplete | None = None): ...
