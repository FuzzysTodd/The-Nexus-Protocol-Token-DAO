from _typeshed import Incomplete

def session_from_client_config(client_config, scopes, **kwargs):
    """Creates a :class:`requests_oauthlib.OAuth2Session` from client
    configuration loaded from a Google-format client secrets file.

    Args:
        client_config (Mapping[str, Any]): The client
            configuration in the Google `client secrets`_ format.
        scopes (Sequence[str]): The list of scopes to request during the
            flow.
        kwargs: Any additional parameters passed to
            :class:`requests_oauthlib.OAuth2Session`

    Raises:
        ValueError: If the client configuration is not in the correct
            format.

    Returns:
        Tuple[requests_oauthlib.OAuth2Session, Mapping[str, Any]]: The new
            oauthlib session and the validated client configuration.

    .. _client secrets:
        https://github.com/googleapis/google-api-python-client/blob/main/docs/client-secrets.md
    """
def session_from_client_secrets_file(client_secrets_file, scopes, **kwargs):
    """Creates a :class:`requests_oauthlib.OAuth2Session` instance from a
    Google-format client secrets file.

    Args:
        client_secrets_file (str): The path to the `client secrets`_ .json
            file.
        scopes (Sequence[str]): The list of scopes to request during the
            flow.
        kwargs: Any additional parameters passed to
            :class:`requests_oauthlib.OAuth2Session`

    Returns:
        Tuple[requests_oauthlib.OAuth2Session, Mapping[str, Any]]: The new
            oauthlib session and the validated client configuration.

    .. _client secrets:
        https://github.com/googleapis/google-api-python-client/blob/main/docs/client-secrets.md
    """
def credentials_from_session(session, client_config: Incomplete | None = None):
    """Creates :class:`google.oauth2.credentials.Credentials` from a
    :class:`requests_oauthlib.OAuth2Session`.

    :meth:`fetch_token` must be called on the session before before calling
    this. This uses the session's auth token and the provided client
    configuration to create :class:`google.oauth2.credentials.Credentials`.
    This allows you to use the credentials from the session with Google
    API client libraries.

    Args:
        session (requests_oauthlib.OAuth2Session): The OAuth 2.0 session.
        client_config (Mapping[str, Any]): The subset of the client
            configuration to use. For example, if you have a web client
            you would pass in `client_config['web']`.

    Returns:
        google.oauth2.credentials.Credentials: The constructed credentials.

    Raises:
        ValueError: If there is no access token in the session.
    """
