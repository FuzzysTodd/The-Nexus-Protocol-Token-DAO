import abc
from _typeshed import Incomplete
from google.auth import credentials

class Credentials(credentials.Scoped, credentials.CredentialsWithQuotaProject, credentials.CredentialsWithTokenUri, metaclass=abc.ABCMeta):
    """Base class for all external account credentials.

    This is used to instantiate Credentials for exchanging external account
    credentials for Google access token and authorizing requests to Google APIs.
    The base class implements the common logic for exchanging external account
    credentials for Google access tokens.
    """
    def __init__(self, audience, subject_token_type, token_url, credential_source, service_account_impersonation_url: Incomplete | None = None, service_account_impersonation_options: Incomplete | None = None, client_id: Incomplete | None = None, client_secret: Incomplete | None = None, token_info_url: Incomplete | None = None, quota_project_id: Incomplete | None = None, scopes: Incomplete | None = None, default_scopes: Incomplete | None = None, workforce_pool_user_project: Incomplete | None = None, universe_domain=..., trust_boundary: Incomplete | None = None) -> None:
        """Instantiates an external account credentials object.

        Args:
            audience (str): The STS audience field.
            subject_token_type (str): The subject token type.
            token_url (str): The STS endpoint URL.
            credential_source (Mapping): The credential source dictionary.
            service_account_impersonation_url (Optional[str]): The optional service account
                impersonation generateAccessToken URL.
            client_id (Optional[str]): The optional client ID.
            client_secret (Optional[str]): The optional client secret.
            token_info_url (str): The optional STS endpoint URL for token introspection.
            quota_project_id (Optional[str]): The optional quota project ID.
            scopes (Optional[Sequence[str]]): Optional scopes to request during the
                authorization grant.
            default_scopes (Optional[Sequence[str]]): Default scopes passed by a
                Google client library. Use 'scopes' for user-defined scopes.
            workforce_pool_user_project (Optona[str]): The optional workforce pool user
                project number when the credential corresponds to a workforce pool and not
                a workload identity pool. The underlying principal must still have
                serviceusage.services.use IAM permission to use the project for
                billing/quota.
            universe_domain (str): The universe domain. The default universe
                domain is googleapis.com.
            trust_boundary (str): String representation of trust boundary meta.
        Raises:
            google.auth.exceptions.RefreshError: If the generateAccessToken
                endpoint returned an error.
        """
    @property
    def info(self):
        '''Generates the dictionary representation of the current credentials.

        Returns:
            Mapping: The dictionary representation of the credentials. This is the
                reverse of "from_info" defined on the subclasses of this class. It is
                useful for serializing the current credentials so it can deserialized
                later.
        '''
    @property
    def service_account_email(self):
        """Returns the service account email if service account impersonation is used.

        Returns:
            Optional[str]: The service account email if impersonation is used. Otherwise
                None is returned.
        """
    @property
    def is_user(self):
        """Returns whether the credentials represent a user (True) or workload (False).
        Workloads behave similarly to service accounts. Currently workloads will use
        service account impersonation but will eventually not require impersonation.
        As a result, this property is more reliable than the service account email
        property in determining if the credentials represent a user or workload.

        Returns:
            bool: True if the credentials represent a user. False if they represent a
                workload.
        """
    @property
    def is_workforce_pool(self):
        """Returns whether the credentials represent a workforce pool (True) or
        workload (False) based on the credentials' audience.

        This will also return True for impersonated workforce pool credentials.

        Returns:
            bool: True if the credentials represent a workforce pool. False if they
                represent a workload.
        """
    @property
    def requires_scopes(self):
        """Checks if the credentials requires scopes.

        Returns:
            bool: True if there are no scopes set otherwise False.
        """
    @property
    def project_number(self):
        """Optional[str]: The project number corresponding to the workload identity pool."""
    @property
    def token_info_url(self):
        """Optional[str]: The STS token introspection endpoint."""
    def with_scopes(self, scopes, default_scopes: Incomplete | None = None): ...
    @abc.abstractmethod
    def retrieve_subject_token(self, request):
        """Retrieves the subject token using the credential_source object.

        Args:
            request (google.auth.transport.Request): A callable used to make
                HTTP requests.
        Returns:
            str: The retrieved subject token.
        """
    def get_project_id(self, request):
        """Retrieves the project ID corresponding to the workload identity or workforce pool.
        For workforce pool credentials, it returns the project ID corresponding to
        the workforce_pool_user_project.

        When not determinable, None is returned.

        This is introduced to support the current pattern of using the Auth library:

            credentials, project_id = google.auth.default()

        The resource may not have permission (resourcemanager.projects.get) to
        call this API or the required scopes may not be selected:
        https://cloud.google.com/resource-manager/reference/rest/v1/projects/get#authorization-scopes

        Args:
            request (google.auth.transport.Request): A callable used to make
                HTTP requests.
        Returns:
            Optional[str]: The project ID corresponding to the workload identity pool
                or workforce pool if determinable.
        """
    token: Incomplete
    expiry: Incomplete
    def refresh(self, request) -> None: ...
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
            google.auth.identity_pool.Credentials: The constructed
                credentials.

        Raises:
            InvalidValue: For invalid parameters.
        """
    @classmethod
    def from_file(cls, filename, **kwargs):
        """Creates a Credentials instance from an external account json file.

        Args:
            filename (str): The path to the external account json file.
            kwargs: Additional arguments to pass to the constructor.

        Returns:
            google.auth.identity_pool.Credentials: The constructed
                credentials.
        """
