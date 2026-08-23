from _typeshed import Incomplete
from google.auth import credentials, crypt

class Signer(crypt.Signer):
    """Signs messages using the App Engine App Identity service.

    This can be used in place of :class:`google.auth.crypt.Signer` when
    running in the App Engine standard environment.
    """
    @property
    def key_id(self) -> None:
        """Optional[str]: The key ID used to identify this private key.

        .. warning::
           This is always ``None``. The key ID used by App Engine can not
           be reliably determined ahead of time.
        """
    def sign(self, message): ...

def get_project_id():
    """Gets the project ID for the current App Engine application.

    Returns:
        str: The project ID

    Raises:
        google.auth.exceptions.OSError: If the App Engine APIs are unavailable.
    """

class Credentials(credentials.Scoped, credentials.Signing, credentials.CredentialsWithQuotaProject):
    """App Engine standard environment credentials.

    These credentials use the App Engine App Identity API to obtain access
    tokens.
    """
    def __init__(self, scopes: Incomplete | None = None, default_scopes: Incomplete | None = None, service_account_id: Incomplete | None = None, quota_project_id: Incomplete | None = None) -> None:
        """
        Args:
            scopes (Sequence[str]): Scopes to request from the App Identity
                API.
            default_scopes (Sequence[str]): Default scopes passed by a
                Google client library. Use 'scopes' for user-defined scopes.
            service_account_id (str): The service account ID passed into
                :func:`google.appengine.api.app_identity.get_access_token`.
                If not specified, the default application service account
                ID will be used.
            quota_project_id (Optional[str]): The project ID used for quota
                and billing.

        Raises:
            google.auth.exceptions.OSError: If the App Engine APIs are unavailable.
        """
    def refresh(self, request) -> None: ...
    @property
    def service_account_email(self):
        """The service account email."""
    @property
    def requires_scopes(self):
        """Checks if the credentials requires scopes.

        Returns:
            bool: True if there are no scopes set otherwise False.
        """
    def with_scopes(self, scopes, default_scopes: Incomplete | None = None): ...
    def with_quota_project(self, quota_project_id): ...
    def sign_bytes(self, message): ...
    @property
    def signer_email(self): ...
    @property
    def signer(self): ...
