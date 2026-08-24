from _typeshed import Incomplete

RUN_CHALLENGE_RETRY_LIMIT: int

def is_interactive():
    """Check if we are in an interractive environment.

    Override this function with a different logic if you are using this library
    outside a CLI.

    If the rapt token needs refreshing, the user needs to answer the challenges.
    If the user is not in an interractive environment, the challenges can not
    be answered and we just wait for timeout for no reason.

    Returns:
        bool: True if is interactive environment, False otherwise.
    """
def get_rapt_token(request, client_id, client_secret, refresh_token, token_uri, scopes: Incomplete | None = None):
    """Given an http request method and refresh_token, get rapt token.

    Args:
        request (google.auth.transport.Request): A callable used to make
            HTTP requests.
        client_id (str): client id to get access token for reauth scope.
        client_secret (str): client secret for the client_id
        refresh_token (str): refresh token to refresh access token
        token_uri (str): uri to refresh access token
        scopes (Optional(Sequence[str])): scopes required by the client application

    Returns:
        str: The rapt token.
    Raises:
        google.auth.exceptions.RefreshError: If reauth failed.
    """
def refresh_grant(request, token_uri, refresh_token, client_id, client_secret, scopes: Incomplete | None = None, rapt_token: Incomplete | None = None, enable_reauth_refresh: bool = False):
    """Implements the reauthentication flow.

    Args:
        request (google.auth.transport.Request): A callable used to make
            HTTP requests.
        token_uri (str): The OAuth 2.0 authorizations server's token endpoint
            URI.
        refresh_token (str): The refresh token to use to get a new access
            token.
        client_id (str): The OAuth 2.0 application's client ID.
        client_secret (str): The Oauth 2.0 appliaction's client secret.
        scopes (Optional(Sequence[str])): Scopes to request. If present, all
            scopes must be authorized for the refresh token. Useful if refresh
            token has a wild card scope (e.g.
            'https://www.googleapis.com/auth/any-api').
        rapt_token (Optional(str)): The rapt token for reauth.
        enable_reauth_refresh (Optional[bool]): Whether reauth refresh flow
            should be used. The default value is False. This option is for
            gcloud only, other users should use the default value.

    Returns:
        Tuple[str, Optional[str], Optional[datetime], Mapping[str, str], str]: The
            access token, new refresh token, expiration, the additional data
            returned by the token endpoint, and the rapt token.

    Raises:
        google.auth.exceptions.RefreshError: If the token endpoint returned
            an error.
    """
