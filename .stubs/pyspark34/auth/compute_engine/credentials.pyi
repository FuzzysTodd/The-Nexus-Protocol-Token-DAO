from _typeshed import Incomplete
from google.auth import credentials

class Credentials(credentials.Scoped, credentials.CredentialsWithQuotaProject):
    """Compute Engine Credentials.

    These credentials use the Google Compute Engine metadata server to obtain
    OAuth 2.0 access tokens associated with the instance's service account,
    and are also used for Cloud Run, Flex and App Engine (except for the Python
    2.7 runtime, which is supported only on older versions of this library).

    For more information about Compute Engine authentication, including how
    to configure scopes, see the `Compute Engine authentication
    documentation`_.

    .. note:: On Compute Engine the metadata server ignores requested scopes.
        On Cloud Run, Flex and App Engine the server honours requested scopes.

    .. _Compute Engine authentication documentation:
        https://cloud.google.com/compute/docs/authentication#using
    """
    def __init__(self, service_account_email: str = 'default', quota_project_id: Incomplete | None = None, scopes: Incomplete | None = None, default_scopes: Incomplete | None = None) -> None:
        """
        Args:
            service_account_email (str): The service account email to use, or
                'default'. A Compute Engine instance may have multiple service
                accounts.
            quota_project_id (Optional[str]): The project ID used for quota and
                billing.
            scopes (Optional[Sequence[str]]): The list of scopes for the credentials.
            default_scopes (Optional[Sequence[str]]): Default scopes passed by a
                Google client library. Use 'scopes' for user-defined scopes.
        """
    def refresh(self, request) -> None:
        """Refresh the access token and scopes.

        Args:
            request (google.auth.transport.Request): The object used to make
                HTTP requests.

        Raises:
            google.auth.exceptions.RefreshError: If the Compute Engine metadata
                service can't be reached if if the instance has not
                credentials.
        """
    @property
    def service_account_email(self):
        """The service account email.

        .. note:: This is not guaranteed to be set until :meth:`refresh` has been
            called.
        """
    @property
    def requires_scopes(self): ...
    def with_quota_project(self, quota_project_id): ...
    def with_scopes(self, scopes, default_scopes: Incomplete | None = None): ...

class IDTokenCredentials(credentials.CredentialsWithQuotaProject, credentials.Signing, credentials.CredentialsWithTokenUri):
    """Open ID Connect ID Token-based service account credentials.

    These credentials relies on the default service account of a GCE instance.

    ID token can be requested from `GCE metadata server identity endpoint`_, IAM
    token endpoint or other token endpoints you specify. If metadata server
    identity endpoint is not used, the GCE instance must have been started with
    a service account that has access to the IAM Cloud API.

    .. _GCE metadata server identity endpoint:
        https://cloud.google.com/compute/docs/instances/verifying-instance-identity
    """
    def __init__(self, request, target_audience, token_uri: Incomplete | None = None, additional_claims: Incomplete | None = None, service_account_email: Incomplete | None = None, signer: Incomplete | None = None, use_metadata_identity_endpoint: bool = False, quota_project_id: Incomplete | None = None) -> None:
        """
        Args:
            request (google.auth.transport.Request): The object used to make
                HTTP requests.
            target_audience (str): The intended audience for these credentials,
                used when requesting the ID Token. The ID Token's ``aud`` claim
                will be set to this string.
            token_uri (str): The OAuth 2.0 Token URI.
            additional_claims (Mapping[str, str]): Any additional claims for
                the JWT assertion used in the authorization grant.
            service_account_email (str): Optional explicit service account to
                use to sign JWT tokens.
                By default, this is the default GCE service account.
            signer (google.auth.crypt.Signer): The signer used to sign JWTs.
                In case the signer is specified, the request argument will be
                ignored.
            use_metadata_identity_endpoint (bool): Whether to use GCE metadata
                identity endpoint. For backward compatibility the default value
                is False. If set to True, ``token_uri``, ``additional_claims``,
                ``service_account_email``, ``signer`` argument should not be set;
                otherwise ValueError will be raised.
            quota_project_id (Optional[str]): The project ID used for quota and
                billing.

        Raises:
            ValueError:
                If ``use_metadata_identity_endpoint`` is set to True, and one of
                ``token_uri``, ``additional_claims``, ``service_account_email``,
                 ``signer`` arguments is set.
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
    def refresh(self, request) -> None:
        """Refreshes the ID token.

        Args:
            request (google.auth.transport.Request): The object used to make
                HTTP requests.

        Raises:
            google.auth.exceptions.RefreshError: If the credentials could
                not be refreshed.
            ValueError: If extracting expiry from the obtained ID token fails.
        """
    @property
    def signer(self): ...
    def sign_bytes(self, message):
        """Signs the given message.

        Args:
            message (bytes): The message to sign.

        Returns:
            bytes: The message's cryptographic signature.

        Raises:
            ValueError:
                Signer is not available if metadata identity endpoint is used.
        """
    @property
    def service_account_email(self):
        """The service account email."""
    @property
    def signer_email(self): ...
