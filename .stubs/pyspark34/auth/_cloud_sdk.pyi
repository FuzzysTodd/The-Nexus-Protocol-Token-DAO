from _typeshed import Incomplete

CLOUD_SDK_CLIENT_ID: str

def get_config_path():
    """Returns the absolute path the the Cloud SDK's configuration directory.

    Returns:
        str: The Cloud SDK config path.
    """
def get_application_default_credentials_path():
    """Gets the path to the application default credentials file.

    The path may or may not exist.

    Returns:
        str: The full path to application default credentials.
    """
def get_project_id():
    """Gets the project ID from the Cloud SDK.

    Returns:
        Optional[str]: The project ID.
    """
def get_auth_access_token(account: Incomplete | None = None):
    """Load user access token with the ``gcloud auth print-access-token`` command.

    Args:
        account (Optional[str]): Account to get the access token for. If not
            specified, the current active account will be used.

    Returns:
        str: The user access token.

    Raises:
        google.auth.exceptions.UserAccessTokenError: if failed to get access
            token from gcloud.
    """
