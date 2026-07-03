from _typeshed import Incomplete

CLIENT_ID: str
AUTHORITY_STR: str
DEFAULT_SCOPES: Incomplete
AUTH: Incomplete

class AuthenticationResult:
    def __init__(self) -> None:
        """ Create an instance of AuthenticationResult

        Returns:
            object: AuthenticationResult object. The authentication result object should be passed only to trusted code in your notebook.
        """
    def get_access_token(self, force_refresh: bool = False):
        """ Returns the access token

        Returns:
            string: access token
        """

class DeviceCodeLoginAuthentication(AuthenticationResult):
    def __init__(self, tenant_id: Incomplete | None = None) -> None:
        """ Initiate a Device Flow Auth instance

        Args:
            tenant_id (string): Optional.
                Id of Power BI tenant where your report resides.

        Returns:
            object: Device flow object. The device flow object should be passed only to trusted code in your notebook.
        """

class InteractiveLoginAuthentication(AuthenticationResult):
    def __init__(self, tenant_id: Incomplete | None = None) -> None:
        """Acquire token interactively i.e. via a local browser

        Args:
            tenant_id (string): Optional.
                Id of Power BI tenant where your report resides.

        Returns:
            object: Interactive authentication object. The interactive authentication object should be passed only to trusted code in your notebook.
        """

def CheckGlobalAuth() -> None: ...
