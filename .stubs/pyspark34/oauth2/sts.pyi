from _typeshed import Incomplete
from google.oauth2 import utils

class Client(utils.OAuthClientAuthHandler):
    """Implements the OAuth 2.0 token exchange spec based on
    https://tools.ietf.org/html/rfc8693.
    """
    def __init__(self, token_exchange_endpoint, client_authentication: Incomplete | None = None) -> None:
        """Initializes an STS client instance.

        Args:
            token_exchange_endpoint (str): The token exchange endpoint.
            client_authentication (Optional(google.oauth2.oauth2_utils.ClientAuthentication)):
                The optional OAuth client authentication credentials if available.
        """
    def exchange_token(self, request, grant_type, subject_token, subject_token_type, resource: Incomplete | None = None, audience: Incomplete | None = None, scopes: Incomplete | None = None, requested_token_type: Incomplete | None = None, actor_token: Incomplete | None = None, actor_token_type: Incomplete | None = None, additional_options: Incomplete | None = None, additional_headers: Incomplete | None = None):
        """Exchanges the provided token for another type of token based on the
        rfc8693 spec.

        Args:
            request (google.auth.transport.Request): A callable used to make
                HTTP requests.
            grant_type (str): The OAuth 2.0 token exchange grant type.
            subject_token (str): The OAuth 2.0 token exchange subject token.
            subject_token_type (str): The OAuth 2.0 token exchange subject token type.
            resource (Optional[str]): The optional OAuth 2.0 token exchange resource field.
            audience (Optional[str]): The optional OAuth 2.0 token exchange audience field.
            scopes (Optional[Sequence[str]]): The optional list of scopes to use.
            requested_token_type (Optional[str]): The optional OAuth 2.0 token exchange requested
                token type.
            actor_token (Optional[str]): The optional OAuth 2.0 token exchange actor token.
            actor_token_type (Optional[str]): The optional OAuth 2.0 token exchange actor token type.
            additional_options (Optional[Mapping[str, str]]): The optional additional
                non-standard Google specific options.
            additional_headers (Optional[Mapping[str, str]]): The optional additional
                headers to pass to the token exchange endpoint.

        Returns:
            Mapping[str, str]: The token exchange JSON-decoded response data containing
                the requested token and its expiration time.

        Raises:
            google.auth.exceptions.OAuthError: If the token endpoint returned
                an error.
        """
    def refresh_token(self, request, refresh_token):
        """Exchanges a refresh token for an access token based on the
        RFC6749 spec.

        Args:
            request (google.auth.transport.Request): A callable used to make
                HTTP requests.
            subject_token (str): The OAuth 2.0 refresh token.
        """
