from _typeshed import Incomplete
from google.auth import credentials

class Credentials(credentials.Scoped, credentials.CredentialsWithQuotaProject, credentials.Signing):
    """This module defines impersonated credentials which are essentially
    impersonated identities.

    Impersonated Credentials allows credentials issued to a user or
    service account to impersonate another. The target service account must
    grant the originating credential principal the
    `Service Account Token Creator`_ IAM role:

    For more information about Token Creator IAM role and
    IAMCredentials API, see
    `Creating Short-Lived Service Account Credentials`_.

    .. _Service Account Token Creator:
        https://cloud.google.com/iam/docs/service-accounts#the_service_account_token_creator_role

    .. _Creating Short-Lived Service Account Credentials:
        https://cloud.google.com/iam/docs/creating-short-lived-service-account-credentials

    Usage:

    First grant source_credentials the `Service Account Token Creator`
    role on the target account to impersonate.   In this example, the
    service account represented by svc_account.json has the
    token creator role on
    `impersonated-account@_project_.iam.gserviceaccount.com`.

    Enable the IAMCredentials API on the source project:
    `gcloud services enable iamcredentials.googleapis.com`.

    Initialize a source credential which does not have access to
    list bucket::

        from google.oauth2 import service_account

        target_scopes = [
            'https://www.googleapis.com/auth/devstorage.read_only']

        source_credentials = (
            service_account.Credentials.from_service_account_file(
                '/path/to/svc_account.json',
                scopes=target_scopes))

    Now use the source credentials to acquire credentials to impersonate
    another service account::

        from google.auth import impersonated_credentials

        target_credentials = impersonated_credentials.Credentials(
          source_credentials=source_credentials,
          target_principal='impersonated-account@_project_.iam.gserviceaccount.com',
          target_scopes = target_scopes,
          lifetime=500)

    Resource access is granted::

        client = storage.Client(credentials=target_credentials)
        buckets = client.list_buckets(project='your_project')
        for bucket in buckets:
          print(bucket.name)
    """
    token: Incomplete
    expiry: Incomplete
    def __init__(self, source_credentials, target_principal, target_scopes, delegates: Incomplete | None = None, lifetime=..., quota_project_id: Incomplete | None = None, iam_endpoint_override: Incomplete | None = None) -> None:
        '''
        Args:
            source_credentials (google.auth.Credentials): The source credential
                used as to acquire the impersonated credentials.
            target_principal (str): The service account to impersonate.
            target_scopes (Sequence[str]): Scopes to request during the
                authorization grant.
            delegates (Sequence[str]): The chained list of delegates required
                to grant the final access_token.  If set, the sequence of
                identities must have "Service Account Token Creator" capability
                granted to the prceeding identity.  For example, if set to
                [serviceAccountB, serviceAccountC], the source_credential
                must have the Token Creator role on serviceAccountB.
                serviceAccountB must have the Token Creator on
                serviceAccountC.
                Finally, C must have Token Creator on target_principal.
                If left unset, source_credential must have that role on
                target_principal.
            lifetime (int): Number of seconds the delegated credential should
                be valid for (upto 3600).
            quota_project_id (Optional[str]): The project ID used for quota and billing.
                This project may be different from the project used to
                create the credentials.
            iam_endpoint_override (Optiona[str]): The full IAM endpoint override
                with the target_principal embedded. This is useful when supporting
                impersonation with regional endpoints.
        '''
    def refresh(self, request) -> None: ...
    def sign_bytes(self, message): ...
    @property
    def signer_email(self): ...
    @property
    def service_account_email(self): ...
    @property
    def signer(self): ...
    @property
    def requires_scopes(self): ...
    def with_quota_project(self, quota_project_id): ...
    def with_scopes(self, scopes, default_scopes: Incomplete | None = None): ...

class IDTokenCredentials(credentials.CredentialsWithQuotaProject):
    """Open ID Connect ID Token-based service account credentials.

    """
    def __init__(self, target_credentials, target_audience: Incomplete | None = None, include_email: bool = False, quota_project_id: Incomplete | None = None) -> None:
        """
        Args:
            target_credentials (google.auth.Credentials): The target
                credential used as to acquire the id tokens for.
            target_audience (string): Audience to issue the token for.
            include_email (bool): Include email in IdToken
            quota_project_id (Optional[str]):  The project ID used for
                quota and billing.
        """
    def from_credentials(self, target_credentials, target_audience: Incomplete | None = None): ...
    def with_target_audience(self, target_audience): ...
    def with_include_email(self, include_email): ...
    def with_quota_project(self, quota_project_id): ...
    token: Incomplete
    expiry: Incomplete
    def refresh(self, request) -> None: ...
