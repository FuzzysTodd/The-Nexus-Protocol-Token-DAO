from _typeshed import Incomplete
from google.auth import credentials

class Credentials(credentials.Signing, credentials.Scoped, credentials.CredentialsWithQuotaProject, credentials.CredentialsWithTokenUri):
    """Service account credentials

    Usually, you'll create these credentials with one of the helper
    constructors. To create credentials using a Google service account
    private key JSON file::

        credentials = service_account.Credentials.from_service_account_file(
            'service-account.json')

    Or if you already have the service account file loaded::

        service_account_info = json.load(open('service_account.json'))
        credentials = service_account.Credentials.from_service_account_info(
            service_account_info)

    Both helper methods pass on arguments to the constructor, so you can
    specify additional scopes and a subject if necessary::

        credentials = service_account.Credentials.from_service_account_file(
            'service-account.json',
            scopes=['email'],
            subject='user@example.com')

    The credentials are considered immutable. If you want to modify the scopes
    or the subject used for delegation, use :meth:`with_scopes` or
    :meth:`with_subject`::

        scoped_credentials = credentials.with_scopes(['email'])
        delegated_credentials = credentials.with_subject(subject)

    To add a quota project, use :meth:`with_quota_project`::

        credentials = credentials.with_quota_project('myproject-123')
    """
    def __init__(self, signer, service_account_email, token_uri, scopes: Incomplete | None = None, default_scopes: Incomplete | None = None, subject: Incomplete | None = None, project_id: Incomplete | None = None, quota_project_id: Incomplete | None = None, additional_claims: Incomplete | None = None, always_use_jwt_access: bool = False, universe_domain=..., trust_boundary: Incomplete | None = None) -> None:
        """
        Args:
            signer (google.auth.crypt.Signer): The signer used to sign JWTs.
            service_account_email (str): The service account's email.
            scopes (Sequence[str]): User-defined scopes to request during the
                authorization grant.
            default_scopes (Sequence[str]): Default scopes passed by a
                Google client library. Use 'scopes' for user-defined scopes.
            token_uri (str): The OAuth 2.0 Token URI.
            subject (str): For domain-wide delegation, the email address of the
                user to for which to request delegated access.
            project_id  (str): Project ID associated with the service account
                credential.
            quota_project_id (Optional[str]): The project ID used for quota and
                billing.
            additional_claims (Mapping[str, str]): Any additional claims for
                the JWT assertion used in the authorization grant.
            always_use_jwt_access (Optional[bool]): Whether self signed JWT should
                be always used.
            universe_domain (str): The universe domain. The default
                universe domain is googleapis.com. For default value self
                signed jwt is used for token refresh.
            trust_boundary (str): String representation of trust boundary meta.

        .. note:: Typically one of the helper constructors
            :meth:`from_service_account_file` or
            :meth:`from_service_account_info` are used instead of calling the
            constructor directly.
        """
    @classmethod
    def from_service_account_info(cls, info, **kwargs):
        """Creates a Credentials instance from parsed service account info.

        Args:
            info (Mapping[str, str]): The service account info in Google
                format.
            kwargs: Additional arguments to pass to the constructor.

        Returns:
            google.auth.service_account.Credentials: The constructed
                credentials.

        Raises:
            ValueError: If the info is not in the expected format.
        """
    @classmethod
    def from_service_account_file(cls, filename, **kwargs):
        """Creates a Credentials instance from a service account json file.

        Args:
            filename (str): The path to the service account json file.
            kwargs: Additional arguments to pass to the constructor.

        Returns:
            google.auth.service_account.Credentials: The constructed
                credentials.
        """
    @property
    def service_account_email(self):
        """The service account email."""
    @property
    def project_id(self):
        """Project ID associated with this credential."""
    @property
    def requires_scopes(self):
        """Checks if the credentials requires scopes.

        Returns:
            bool: True if there are no scopes set otherwise False.
        """
    def with_scopes(self, scopes, default_scopes: Incomplete | None = None): ...
    def with_always_use_jwt_access(self, always_use_jwt_access):
        """Create a copy of these credentials with the specified always_use_jwt_access value.

        Args:
            always_use_jwt_access (bool): Whether always use self signed JWT or not.

        Returns:
            google.auth.service_account.Credentials: A new credentials
                instance.
        Raises:
            google.auth.exceptions.InvalidValue: If the universe domain is not
                default and always_use_jwt_access is False.
        """
    def with_subject(self, subject):
        """Create a copy of these credentials with the specified subject.

        Args:
            subject (str): The subject claim.

        Returns:
            google.auth.service_account.Credentials: A new credentials
                instance.
        """
    def with_claims(self, additional_claims):
        """Returns a copy of these credentials with modified claims.

        Args:
            additional_claims (Mapping[str, str]): Any additional claims for
                the JWT payload. This will be merged with the current
                additional claims.

        Returns:
            google.auth.service_account.Credentials: A new credentials
                instance.
        """
    def with_quota_project(self, quota_project_id): ...
    def with_token_uri(self, token_uri): ...
    token: Incomplete
    expiry: Incomplete
    def refresh(self, request) -> None: ...
    def sign_bytes(self, message): ...
    @property
    def signer(self): ...
    @property
    def signer_email(self): ...

class IDTokenCredentials(credentials.Signing, credentials.CredentialsWithQuotaProject, credentials.CredentialsWithTokenUri):
    """Open ID Connect ID Token-based service account credentials.

    These credentials are largely similar to :class:`.Credentials`, but instead
    of using an OAuth 2.0 Access Token as the bearer token, they use an Open
    ID Connect ID Token as the bearer token. These credentials are useful when
    communicating to services that require ID Tokens and can not accept access
    tokens.

    Usually, you'll create these credentials with one of the helper
    constructors. To create credentials using a Google service account
    private key JSON file::

        credentials = (
            service_account.IDTokenCredentials.from_service_account_file(
                'service-account.json'))


    Or if you already have the service account file loaded::

        service_account_info = json.load(open('service_account.json'))
        credentials = (
            service_account.IDTokenCredentials.from_service_account_info(
                service_account_info))


    Both helper methods pass on arguments to the constructor, so you can
    specify additional scopes and a subject if necessary::

        credentials = (
            service_account.IDTokenCredentials.from_service_account_file(
                'service-account.json',
                scopes=['email'],
                subject='user@example.com'))


    The credentials are considered immutable. If you want to modify the scopes
    or the subject used for delegation, use :meth:`with_scopes` or
    :meth:`with_subject`::

        scoped_credentials = credentials.with_scopes(['email'])
        delegated_credentials = credentials.with_subject(subject)

    """
    def __init__(self, signer, service_account_email, token_uri, target_audience, additional_claims: Incomplete | None = None, quota_project_id: Incomplete | None = None, universe_domain=...) -> None:
        """
        Args:
            signer (google.auth.crypt.Signer): The signer used to sign JWTs.
            service_account_email (str): The service account's email.
            token_uri (str): The OAuth 2.0 Token URI.
            target_audience (str): The intended audience for these credentials,
                used when requesting the ID Token. The ID Token's ``aud`` claim
                will be set to this string.
            additional_claims (Mapping[str, str]): Any additional claims for
                the JWT assertion used in the authorization grant.
            quota_project_id (Optional[str]): The project ID used for quota and billing.
            universe_domain (str): The universe domain. The default
                universe domain is googleapis.com. For default value IAM ID
                token endponint is used for token refresh. Note that
                iam.serviceAccountTokenCreator role is required to use the IAM
                endpoint.
        .. note:: Typically one of the helper constructors
            :meth:`from_service_account_file` or
            :meth:`from_service_account_info` are used instead of calling the
            constructor directly.
        """
    @classmethod
    def from_service_account_info(cls, info, **kwargs):
        """Creates a credentials instance from parsed service account info.

        Args:
            info (Mapping[str, str]): The service account info in Google
                format.
            kwargs: Additional arguments to pass to the constructor.

        Returns:
            google.auth.service_account.IDTokenCredentials: The constructed
                credentials.

        Raises:
            ValueError: If the info is not in the expected format.
        """
    @classmethod
    def from_service_account_file(cls, filename, **kwargs):
        """Creates a credentials instance from a service account json file.

        Args:
            filename (str): The path to the service account json file.
            kwargs: Additional arguments to pass to the constructor.

        Returns:
            google.auth.service_account.IDTokenCredentials: The constructed
                credentials.
        """
    def with_target_audience(self, target_audience):
        """Create a copy of these credentials with the specified target
        audience.

        Args:
            target_audience (str): The intended audience for these credentials,
            used when requesting the ID Token.

        Returns:
            google.auth.service_account.IDTokenCredentials: A new credentials
                instance.
        """
    def with_quota_project(self, quota_project_id): ...
    def with_token_uri(self, token_uri): ...
    token: Incomplete
    expiry: Incomplete
    def refresh(self, request) -> None: ...
    @property
    def service_account_email(self):
        """The service account email."""
    def sign_bytes(self, message): ...
    @property
    def signer(self): ...
    @property
    def signer_email(self): ...
