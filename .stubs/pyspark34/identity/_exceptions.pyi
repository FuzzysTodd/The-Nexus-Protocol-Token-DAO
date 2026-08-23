from azure.core.exceptions import ClientAuthenticationError
from typing import Any, Iterable

class CredentialUnavailableError(ClientAuthenticationError):
    """The credential did not attempt to authenticate because required data or state is unavailable."""

class AuthenticationRequiredError(CredentialUnavailableError):
    '''Interactive authentication is required to acquire a token.

    This error is raised only by interactive user credentials configured not to automatically prompt for user
    interaction as needed. Its properties provide additional information that may be required to authenticate. The
    control_interactive_prompts sample demonstrates handling this error by calling a credential\'s "authenticate"
    method.

    :param str scopes: Scopes requested during the failed authentication
    :param str message: An error message explaining the reason for the exception.
    :param str claims: Additional claims required in the next authentication.
    '''
    def __init__(self, scopes: Iterable[str], message: str | None = None, claims: str | None = None, **kwargs: Any) -> None: ...
    @property
    def scopes(self) -> Iterable[str]:
        """Scopes requested during the failed authentication.

        :rtype: ~typing.Iterable[str]
        """
    @property
    def claims(self) -> str | None:
        """Additional claims required in the next authentication.

        :rtype: str or None
        """
