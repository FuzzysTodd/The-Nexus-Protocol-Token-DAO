from _typeshed import Incomplete
from typing import Any, NamedTuple
from typing_extensions import Protocol

__all__ = ['AzureKeyCredential', 'AzureSasCredential', 'AccessToken', 'AzureNamedKeyCredential', 'TokenCredential']

class AccessToken(NamedTuple):
    """Represents an OAuth access token."""
    token: str
    expires_on: int

class TokenCredential(Protocol):
    """Protocol for classes able to provide OAuth tokens."""
    def get_token(self, *scopes: str, claims: str | None = None, tenant_id: str | None = None, **kwargs: Any) -> AccessToken:
        """Request an access token for `scopes`.

        :param str scopes: The type of access needed.

        :keyword str claims: Additional claims required in the token, such as those returned in a resource
            provider's claims challenge following an authorization failure.
        :keyword str tenant_id: Optional tenant to include in the token request.
        :keyword bool enable_cae: Indicates whether to enable Continuous Access Evaluation (CAE) for the requested
            token. Defaults to False.

        :rtype: AccessToken
        :return: An AccessToken instance containing the token string and its expiration time in Unix time.
        """

class AzureNamedKey(NamedTuple):
    name: Incomplete
    key: Incomplete

class AzureKeyCredential:
    """Credential type used for authenticating to an Azure service.
    It provides the ability to update the key without creating a new client.

    :param str key: The key used to authenticate to an Azure service
    :raises: TypeError
    """
    def __init__(self, key: str) -> None: ...
    @property
    def key(self) -> str:
        """The value of the configured key.

        :rtype: str
        :return: The value of the configured key.
        """
    def update(self, key: str) -> None:
        """Update the key.

        This can be used when you've regenerated your service key and want
        to update long-lived clients.

        :param str key: The key used to authenticate to an Azure service
        :raises: ValueError or TypeError
        """

class AzureSasCredential:
    """Credential type used for authenticating to an Azure service.
    It provides the ability to update the shared access signature without creating a new client.

    :param str signature: The shared access signature used to authenticate to an Azure service
    :raises: TypeError
    """
    def __init__(self, signature: str) -> None: ...
    @property
    def signature(self) -> str:
        """The value of the configured shared access signature.

        :rtype: str
        :return: The value of the configured shared access signature.
        """
    def update(self, signature: str) -> None:
        """Update the shared access signature.

        This can be used when you've regenerated your shared access signature and want
        to update long-lived clients.

        :param str signature: The shared access signature used to authenticate to an Azure service
        :raises: ValueError or TypeError
        """

class AzureNamedKeyCredential:
    """Credential type used for working with any service needing a named key that follows patterns
    established by the other credential types.

    :param str name: The name of the credential used to authenticate to an Azure service.
    :param str key: The key used to authenticate to an Azure service.
    :raises: TypeError
    """
    def __init__(self, name: str, key: str) -> None: ...
    @property
    def named_key(self) -> AzureNamedKey:
        """The value of the configured name.

        :rtype: AzureNamedKey
        :return: The value of the configured name.
        """
    def update(self, name: str, key: str) -> None:
        """Update the named key credential.

        Both name and key must be provided in order to update the named key credential.
        Individual attributes cannot be updated.

        :param str name: The name of the credential used to authenticate to an Azure service.
        :param str key: The key used to authenticate to an Azure service.
        """
