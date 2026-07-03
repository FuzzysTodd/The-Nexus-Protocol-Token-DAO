from _typeshed import Incomplete
from google.oauth2 import credentials as oauth2_credentials

class Credentials(oauth2_credentials.Credentials):
    """Credentials using OAuth 2.0 access and refresh tokens.

    The credentials are considered immutable. If you want to modify the
    quota project, use :meth:`with_quota_project` or ::

        credentials = credentials.with_quota_project('myproject-123)
    """
    token: Incomplete
    expiry: Incomplete
    async def refresh(self, request) -> None: ...

class UserAccessTokenCredentials(oauth2_credentials.UserAccessTokenCredentials):
    """Access token credentials for user account.

    Obtain the access token for a given user account or the current active
    user account with the ``gcloud auth print-access-token`` command.

    Args:
        account (Optional[str]): Account to get the access token for. If not
            specified, the current active account will be used.
        quota_project_id (Optional[str]): The project ID used for quota
            and billing.

    """
