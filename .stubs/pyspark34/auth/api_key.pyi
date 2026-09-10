from _typeshed import Incomplete
from google.auth import credentials

class Credentials(credentials.Credentials):
    """API key credentials.
    These credentials use API key to provide authorization to applications.
    """
    token: Incomplete
    def __init__(self, token) -> None:
        """
        Args:
            token (str): API key string
        Raises:
            ValueError: If the provided API key is not a non-empty string.
        """
    @property
    def expired(self): ...
    @property
    def valid(self): ...
    def refresh(self, request) -> None: ...
    def apply(self, headers, token: Incomplete | None = None) -> None:
        """Apply the API key token to the x-goog-api-key header.
        Args:
            headers (Mapping): The HTTP request headers.
            token (Optional[str]): If specified, overrides the current access
                token.
        """
    def before_request(self, request, method, url, headers) -> None:
        """Performs credential-specific before request logic.
        Refreshes the credentials if necessary, then calls :meth:`apply` to
        apply the token to the x-goog-api-key header.
        Args:
            request (google.auth.transport.Request): The object used to make
                HTTP requests.
            method (str): The request's HTTP method or the RPC method being
                invoked.
            url (str): The request's URI or the RPC service's URI.
            headers (Mapping): The request's headers.
        """
