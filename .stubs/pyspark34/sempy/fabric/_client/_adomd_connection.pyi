from _typeshed import Incomplete
from sempy.fabric._token_provider import TokenProvider as TokenProvider, create_on_access_token_expired_callback as create_on_access_token_expired_callback

class AdomdConnection:
    """
    Cached wrapper of Microsoft.AnalysisServices AdomdConnection object, designed to be used with python context manager.

    Parameters
    ----------
    dax_connection_string : str
        Adomd connection string.
    token_provider : TokenProvider
        Dataset client token provider (used for token refresh)
    """
    adomd_connection: Incomplete
    dax_connection_string: Incomplete
    token_provider: Incomplete
    def __init__(self, dax_connection_string: str, token_provider: TokenProvider) -> None: ...
    def __enter__(self):
        """
        Create a new Microsoft.AnalysisServices.AdomdClient.AdomdConnection object, or get from existing cache.
        """
    def __exit__(self, exc_type: type[BaseException] | None, exc_value: BaseException | None, exc_tb: types.TracebackType | None) -> None:
        """
        Handles clearing the cached connection only if an exception is thrown (exception will still be raised).
        """
    def get_or_create_connection(self):
        """
        If connection is not already created, creates a new Microsoft.AnalysisServices.AdomdClient.AdomdConnection object.
        Connection is opened and has token refresh callback.
        """
    def close_and_dispose_connection(self) -> None:
        """
        If a connection is cached, close and dispose of it and reset cache to None.
        """
