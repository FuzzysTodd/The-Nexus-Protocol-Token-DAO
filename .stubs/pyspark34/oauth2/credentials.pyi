from _typeshed import Incomplete
from google.auth import credentials

class Credentials(credentials.ReadOnlyScoped, credentials.CredentialsWithQuotaProject):
    """Credentials using OAuth 2.0 access and refresh tokens.

    The credentials are considered immutable. If you want to modify the
    quota project, use :meth:`with_quota_project` or ::

        credentials = credentials.with_quota_project('myproject-123')

    Reauth is disabled by default. To enable reauth, set the
    `enable_reauth_refresh` parameter to True in the constructor. Note that
    reauth feature is intended for gcloud to use only.
    If reauth is enabled, `pyu2f` dependency has to be installed in order to use security
    key reauth feature. Dependency can be installed via `pip install pyu2f` or `pip install
    google-auth[reauth]`.
    """
    token: Incomplete
    expiry: Incomplete
    def __init__(self, token, refresh_token: Incomplete | None = None, id_token: Incomplete | None = None, token_uri: Incomplete | None = None, client_id: Incomplete | None = None, client_secret: Incomplete | None = None, scopes: Incomplete | None = None, default_scopes: Incomplete | None = None, quota_project_id: Incomplete | None = None, expiry: Incomplete | None = None, rapt_token: Incomplete | None = None, refresh_handler: Incomplete | None = None, enable_reauth_refresh: bool = False, granted_scopes: Incomplete | None = None, trust_boundary: Incomplete | None = None) -> None:
        """
        Args:
            token (Optional(str)): The OAuth 2.0 access token. Can be None
                if refresh information is provided.
            refresh_token (str): The OAuth 2.0 refresh token. If specified,
                credentials can be refreshed.
            id_token (str): The Open ID Connect ID Token.
            token_uri (str): The OAuth 2.0 authorization server's token
                endpoint URI. Must be specified for refresh, can be left as
                None if the token can not be refreshed.
            client_id (str): The OAuth 2.0 client ID. Must be specified for
                refresh, can be left as None if the token can not be refreshed.
            client_secret(str): The OAuth 2.0 client secret. Must be specified
                for refresh, can be left as None if the token can not be
                refreshed.
            scopes (Sequence[str]): The scopes used to obtain authorization.
                This parameter is used by :meth:`has_scopes`. OAuth 2.0
                credentials can not request additional scopes after
                authorization. The scopes must be derivable from the refresh
                token if refresh information is provided (e.g. The refresh
                token scopes are a superset of this or contain a wild card
                scope like 'https://www.googleapis.com/auth/any-api').
            default_scopes (Sequence[str]): Default scopes passed by a
                Google client library. Use 'scopes' for user-defined scopes.
            quota_project_id (Optional[str]): The project ID used for quota and billing.
                This project may be different from the project used to
                create the credentials.
            rapt_token (Optional[str]): The reauth Proof Token.
            refresh_handler (Optional[Callable[[google.auth.transport.Request, Sequence[str]], [str, datetime]]]):
                A callable which takes in the HTTP request callable and the list of
                OAuth scopes and when called returns an access token string for the
                requested scopes and its expiry datetime. This is useful when no
                refresh tokens are provided and tokens are obtained by calling
                some external process on demand. It is particularly useful for
                retrieving downscoped tokens from a token broker.
            enable_reauth_refresh (Optional[bool]): Whether reauth refresh flow
                should be used. This flag is for gcloud to use only.
            granted_scopes (Optional[Sequence[str]]): The scopes that were consented/granted by the user.
                This could be different from the requested scopes and it could be empty if granted
                and requested scopes were same.
        """
    @property
    def refresh_token(self):
        """Optional[str]: The OAuth 2.0 refresh token."""
    @property
    def scopes(self):
        """Optional[str]: The OAuth 2.0 permission scopes."""
    @property
    def granted_scopes(self):
        """Optional[Sequence[str]]: The OAuth 2.0 permission scopes that were granted by the user."""
    @property
    def token_uri(self):
        """Optional[str]: The OAuth 2.0 authorization server's token endpoint
        URI."""
    @property
    def id_token(self):
        """Optional[str]: The Open ID Connect ID Token.

        Depending on the authorization server and the scopes requested, this
        may be populated when credentials are obtained and updated when
        :meth:`refresh` is called. This token is a JWT. It can be verified
        and decoded using :func:`google.oauth2.id_token.verify_oauth2_token`.
        """
    @property
    def client_id(self):
        """Optional[str]: The OAuth 2.0 client ID."""
    @property
    def client_secret(self):
        """Optional[str]: The OAuth 2.0 client secret."""
    @property
    def requires_scopes(self):
        """False: OAuth 2.0 credentials have their scopes set when
        the initial token is requested and can not be changed."""
    @property
    def rapt_token(self):
        """Optional[str]: The reauth Proof Token."""
    @property
    def refresh_handler(self):
        """Returns the refresh handler if available.

        Returns:
           Optional[Callable[[google.auth.transport.Request, Sequence[str]], [str, datetime]]]:
               The current refresh handler.
        """
    @refresh_handler.setter
    def refresh_handler(self, value) -> None:
        """Updates the current refresh handler.

        Args:
            value (Optional[Callable[[google.auth.transport.Request, Sequence[str]], [str, datetime]]]):
                The updated value of the refresh handler.

        Raises:
            TypeError: If the value is not a callable or None.
        """
    def with_quota_project(self, quota_project_id): ...
    def with_token_uri(self, token_uri): ...
    def refresh(self, request) -> None: ...
    @classmethod
    def from_authorized_user_info(cls, info, scopes: Incomplete | None = None):
        """Creates a Credentials instance from parsed authorized user info.

        Args:
            info (Mapping[str, str]): The authorized user info in Google
                format.
            scopes (Sequence[str]): Optional list of scopes to include in the
                credentials.

        Returns:
            google.oauth2.credentials.Credentials: The constructed
                credentials.

        Raises:
            ValueError: If the info is not in the expected format.
        """
    @classmethod
    def from_authorized_user_file(cls, filename, scopes: Incomplete | None = None):
        """Creates a Credentials instance from an authorized user json file.

        Args:
            filename (str): The path to the authorized user json file.
            scopes (Sequence[str]): Optional list of scopes to include in the
                credentials.

        Returns:
            google.oauth2.credentials.Credentials: The constructed
                credentials.

        Raises:
            ValueError: If the file is not in the expected format.
        """
    def to_json(self, strip: Incomplete | None = None):
        """Utility function that creates a JSON representation of a Credentials
        object.

        Args:
            strip (Sequence[str]): Optional list of members to exclude from the
                                   generated JSON.

        Returns:
            str: A JSON representation of this instance. When converted into
            a dictionary, it can be passed to from_authorized_user_info()
            to create a new credential instance.
        """

class UserAccessTokenCredentials(credentials.CredentialsWithQuotaProject):
    """Access token credentials for user account.

    Obtain the access token for a given user account or the current active
    user account with the ``gcloud auth print-access-token`` command.

    Args:
        account (Optional[str]): Account to get the access token for. If not
            specified, the current active account will be used.
        quota_project_id (Optional[str]): The project ID used for quota
            and billing.
    """
    def __init__(self, account: Incomplete | None = None, quota_project_id: Incomplete | None = None) -> None: ...
    def with_account(self, account):
        """Create a new instance with the given account.

        Args:
            account (str): Account to get the access token for.

        Returns:
            google.oauth2.credentials.UserAccessTokenCredentials: The created
                credentials with the given account.
        """
    def with_quota_project(self, quota_project_id): ...
    token: Incomplete
    def refresh(self, request) -> None:
        """Refreshes the access token.

        Args:
            request (google.auth.transport.Request): This argument is required
                by the base class interface but not used in this implementation,
                so just set it to `None`.

        Raises:
            google.auth.exceptions.UserAccessTokenError: If the access token
                refresh failed.
        """
    def before_request(self, request, method, url, headers) -> None: ...
