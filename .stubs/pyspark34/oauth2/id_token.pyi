from _typeshed import Incomplete

def verify_token(id_token, request, audience: Incomplete | None = None, certs_url=..., clock_skew_in_seconds: int = 0):
    """Verifies an ID token and returns the decoded token.

    Args:
        id_token (Union[str, bytes]): The encoded token.
        request (google.auth.transport.Request): The object used to make
            HTTP requests.
        audience (str or list): The audience or audiences that this token is
            intended for. If None then the audience is not verified.
        certs_url (str): The URL that specifies the certificates to use to
            verify the token. This URL should return JSON in the format of
            ``{'key id': 'x509 certificate'}``.
        clock_skew_in_seconds (int): The clock skew used for `iat` and `exp`
            validation.

    Returns:
        Mapping[str, Any]: The decoded token.
    """
def verify_oauth2_token(id_token, request, audience: Incomplete | None = None, clock_skew_in_seconds: int = 0):
    """Verifies an ID Token issued by Google's OAuth 2.0 authorization server.

    Args:
        id_token (Union[str, bytes]): The encoded token.
        request (google.auth.transport.Request): The object used to make
            HTTP requests.
        audience (str): The audience that this token is intended for. This is
            typically your application's OAuth 2.0 client ID. If None then the
            audience is not verified.
        clock_skew_in_seconds (int): The clock skew used for `iat` and `exp`
            validation.

    Returns:
        Mapping[str, Any]: The decoded token.

    Raises:
        exceptions.GoogleAuthError: If the issuer is invalid.
        ValueError: If token verification fails
    """
def verify_firebase_token(id_token, request, audience: Incomplete | None = None, clock_skew_in_seconds: int = 0):
    """Verifies an ID Token issued by Firebase Authentication.

    Args:
        id_token (Union[str, bytes]): The encoded token.
        request (google.auth.transport.Request): The object used to make
            HTTP requests.
        audience (str): The audience that this token is intended for. This is
            typically your Firebase application ID. If None then the audience
            is not verified.
        clock_skew_in_seconds (int): The clock skew used for `iat` and `exp`
            validation.

    Returns:
        Mapping[str, Any]: The decoded token.
    """
def fetch_id_token_credentials(audience, request: Incomplete | None = None):
    '''Create the ID Token credentials from the current environment.

    This function acquires ID token from the environment in the following order.
    See https://google.aip.dev/auth/4110.

    1. If the environment variable ``GOOGLE_APPLICATION_CREDENTIALS`` is set
       to the path of a valid service account JSON file, then ID token is
       acquired using this service account credentials.
    2. If the application is running in Compute Engine, App Engine or Cloud Run,
       then the ID token are obtained from the metadata server.
    3. If metadata server doesn\'t exist and no valid service account credentials
       are found, :class:`~google.auth.exceptions.DefaultCredentialsError` will
       be raised.

    Example::

        import google.oauth2.id_token
        import google.auth.transport.requests

        request = google.auth.transport.requests.Request()
        target_audience = "https://pubsub.googleapis.com"

        # Create ID token credentials.
        credentials = google.oauth2.id_token.fetch_id_token_credentials(target_audience, request=request)

        # Refresh the credential to obtain an ID token.
        credentials.refresh(request)

        id_token = credentials.token
        id_token_expiry = credentials.expiry

    Args:
        audience (str): The audience that this ID token is intended for.
        request (Optional[google.auth.transport.Request]): A callable used to make
            HTTP requests. A request object will be created if not provided.

    Returns:
        google.auth.credentials.Credentials: The ID token credentials.

    Raises:
        ~google.auth.exceptions.DefaultCredentialsError:
            If metadata server doesn\'t exist and no valid service account
            credentials are found.
    '''
def fetch_id_token(request, audience):
    '''Fetch the ID Token from the current environment.

    This function acquires ID token from the environment in the following order.
    See https://google.aip.dev/auth/4110.

    1. If the environment variable ``GOOGLE_APPLICATION_CREDENTIALS`` is set
       to the path of a valid service account JSON file, then ID token is
       acquired using this service account credentials.
    2. If the application is running in Compute Engine, App Engine or Cloud Run,
       then the ID token are obtained from the metadata server.
    3. If metadata server doesn\'t exist and no valid service account credentials
       are found, :class:`~google.auth.exceptions.DefaultCredentialsError` will
       be raised.

    Example::

        import google.oauth2.id_token
        import google.auth.transport.requests

        request = google.auth.transport.requests.Request()
        target_audience = "https://pubsub.googleapis.com"

        id_token = google.oauth2.id_token.fetch_id_token(request, target_audience)

    Args:
        request (google.auth.transport.Request): A callable used to make
            HTTP requests.
        audience (str): The audience that this ID token is intended for.

    Returns:
        str: The ID token.

    Raises:
        ~google.auth.exceptions.DefaultCredentialsError:
            If metadata server doesn\'t exist and no valid service account
            credentials are found.
    '''
