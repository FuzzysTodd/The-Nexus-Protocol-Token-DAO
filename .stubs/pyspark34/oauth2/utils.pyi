import abc
import enum
from _typeshed import Incomplete

class ClientAuthType(enum.Enum):
    basic: int
    request_body: int

class ClientAuthentication:
    """Defines the client authentication credentials for basic and request-body
    types based on https://tools.ietf.org/html/rfc6749#section-2.3.1.
    """
    client_auth_type: Incomplete
    client_id: Incomplete
    client_secret: Incomplete
    def __init__(self, client_auth_type, client_id, client_secret: Incomplete | None = None) -> None:
        """Instantiates a client authentication object containing the client ID
        and secret credentials for basic and response-body auth.

        Args:
            client_auth_type (google.oauth2.oauth_utils.ClientAuthType): The
                client authentication type.
            client_id (str): The client ID.
            client_secret (Optional[str]): The client secret.
        """

class OAuthClientAuthHandler(metaclass=abc.ABCMeta):
    """Abstract class for handling client authentication in OAuth-based
    operations.
    """
    def __init__(self, client_authentication: Incomplete | None = None) -> None:
        """Instantiates an OAuth client authentication handler.

        Args:
            client_authentication (Optional[google.oauth2.utils.ClientAuthentication]):
                The OAuth client authentication credentials if available.
        """
    def apply_client_authentication_options(self, headers, request_body: Incomplete | None = None, bearer_token: Incomplete | None = None) -> None:
        """Applies client authentication on the OAuth request's headers or POST
        body.

        Args:
            headers (Mapping[str, str]): The HTTP request header.
            request_body (Optional[Mapping[str, str]]): The HTTP request body
                dictionary. For requests that do not support request body, this
                is None and will be ignored.
            bearer_token (Optional[str]): The optional bearer token.
        """

def handle_error_response(response_body) -> None:
    """Translates an error response from an OAuth operation into an
    OAuthError exception.

    Args:
        response_body (str): The decoded response data.

    Raises:
        google.auth.exceptions.OAuthError
    """
