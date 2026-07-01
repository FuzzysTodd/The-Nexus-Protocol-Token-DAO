from _typeshed import Incomplete
from google.auth import credentials

class Credentials(credentials.CredentialsWithQuotaProject, credentials.ReadOnlyScoped, credentials.CredentialsWithTokenUri):
    """Credentials for External Account Authorized Users.

    This is used to instantiate Credentials for exchanging refresh tokens from
    authorized users for Google access token and authorizing requests to Google
    APIs.

    The credentials are considered immutable. If you want to modify the
    quota project, use `with_quota_project` and if you want to modify the token
    uri, use `with_token_uri`.
    """
    token: Incomplete
    expiry: Incomplete
    def __init__(self, token: Incomplete | None = None, expiry: Incomplete | None = None, refresh_token: Incomplete | None = None, audience: Incomplete | None = None, client_id: Incomplete | None = None, client_secret: Incomplete | None = None, token_url: Incomplete | None = None, token_info_url: Incomplete | None = None, revoke_url: Incomplete | None = None, scopes: Incomplete | None = None, quota_project_id: Incomplete | None = None) -> None:
        """Instantiates a external account authorized user credentials object.

        Args:
        token (str): The OAuth 2.0 access token. Can be None if refresh information
            is provided.
        expiry (datetime.datetime): The optional expiration datetime of the OAuth 2.0 access
            token.
        refresh_token (str): The optional OAuth 2.0 refresh token. If specified,
            credentials can be refreshed.
        audience (str): The optional STS audience which contains the resource name for the workforce
            pool and the provider identifier in that pool.
        client_id (str): The OAuth 2.0 client ID. Must be specified for refresh, can be left as
            None if the token can not be refreshed.
        client_secret (str): The OAuth 2.0 client secret. Must be specified for refresh, can be
            left as None if the token can not be refreshed.
        token_url (str): The optional STS token exchange endpoint for refresh. Must be specified for
            refresh, can be left as None if the token can not be refreshed.
        token_info_url (str): The optional STS endpoint URL for token introspection.
        revoke_url (str): The optional STS endpoint URL for revoking tokens.
        quota_project_id (str): The optional project ID used for quota and billing.
            This project may be different from the project used to
            create the credentials.

        Returns:
            google.auth.external_account_authorized_user.Credentials: The
                constructed credentials.
        """
    @property
    def info(self):
        '''Generates the serializable dictionary representation of the current
        credentials.

        Returns:
            Mapping: The dictionary representation of the credentials. This is the
                reverse of the "from_info" method defined in this class. It is
                useful for serializing the current credentials so it can deserialized
                later.
        '''
    def constructor_args(self): ...
    @property
    def scopes(self):
        """Optional[str]: The OAuth 2.0 permission scopes."""
    @property
    def requires_scopes(self):
        """ False: OAuth 2.0 credentials have their scopes set when
        the initial token is requested and can not be changed."""
    @property
    def client_id(self):
        """Optional[str]: The OAuth 2.0 client ID."""
    @property
    def client_secret(self):
        """Optional[str]: The OAuth 2.0 client secret."""
    @property
    def audience(self):
        """Optional[str]: The STS audience which contains the resource name for the
            workforce pool and the provider identifier in that pool."""
    @property
    def refresh_token(self):
        """Optional[str]: The OAuth 2.0 refresh token."""
    @property
    def token_url(self):
        """Optional[str]: The STS token exchange endpoint for refresh."""
    @property
    def token_info_url(self):
        """Optional[str]: The STS endpoint for token info."""
    @property
    def revoke_url(self):
        """Optional[str]: The STS endpoint for token revocation."""
    @property
    def is_user(self):
        """ True: This credential always represents a user."""
    @property
    def can_refresh(self): ...
    def get_project_id(self, request: Incomplete | None = None) -> None:
        """Retrieves the project ID corresponding to the workload identity or workforce pool.
        For workforce pool credentials, it returns the project ID corresponding to
        the workforce_pool_user_project.

        When not determinable, None is returned.

        Args:
            request (google.auth.transport.requests.Request): Request object.
                Unused here, but passed from _default.default().

        Return:
          str: project ID is not determinable for this credential type so it returns None
        """
    def to_json(self, strip: Incomplete | None = None):
        """Utility function that creates a JSON representation of this
        credential.
        Args:
            strip (Sequence[str]): Optional list of members to exclude from the
                                   generated JSON.
        Returns:
            str: A JSON representation of this instance. When converted into
            a dictionary, it can be passed to from_info()
            to create a new instance.
        """
    def refresh(self, request) -> None:
        """Refreshes the access token.

        Args:
            request (google.auth.transport.Request): The object used to make
                HTTP requests.

        Raises:
            google.auth.exceptions.RefreshError: If the credentials could
                not be refreshed.
        """
    def with_quota_project(self, quota_project_id): ...
    def with_token_uri(self, token_uri): ...
    @classmethod
    def from_info(cls, info, **kwargs):
        """Creates a Credentials instance from parsed external account info.

        Args:
            info (Mapping[str, str]): The external account info in Google
                format.
            kwargs: Additional arguments to pass to the constructor.

        Returns:
            google.auth.external_account_authorized_user.Credentials: The
                constructed credentials.

        Raises:
            ValueError: For invalid parameters.
        """
    @classmethod
    def from_file(cls, filename, **kwargs):
        """Creates a Credentials instance from an external account json file.

        Args:
            filename (str): The path to the external account json file.
            kwargs: Additional arguments to pass to the constructor.

        Returns:
            google.auth.external_account_authorized_user.Credentials: The
                constructed credentials.
        """
