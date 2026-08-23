from .. import CredentialUnavailableError as CredentialUnavailableError
from .._constants import DEVELOPER_SIGN_ON_CLIENT_ID as DEVELOPER_SIGN_ON_CLIENT_ID
from .._internal import AadClient as AadClient, AadClientBase as AadClientBase
from .._internal.decorators import log_get_token as log_get_token
from .._internal.shared_token_cache import NO_TOKEN as NO_TOKEN, SharedTokenCacheBase as SharedTokenCacheBase
from .silent import SilentAuthenticationCredential as SilentAuthenticationCredential
from azure.core.credentials import AccessToken as AccessToken, TokenCredential as TokenCredential
from typing import Any

class SharedTokenCacheCredential:
    """Authenticates using tokens in the local cache shared between Microsoft applications.

    :param str username: Username (typically an email address) of the user to authenticate as. This is used when the
        local cache contains tokens for multiple identities.

    :keyword str authority: Authority of an Azure Active Directory endpoint, for example 'login.microsoftonline.com',
        the authority for Azure Public Cloud (which is the default). :class:`~azure.identity.AzureAuthorityHosts`
        defines authorities for other clouds.
    :keyword str tenant_id: an Azure Active Directory tenant ID. Used to select an account when the cache contains
        tokens for multiple identities.
    :keyword AuthenticationRecord authentication_record: an authentication record returned by a user credential such as
        :class:`DeviceCodeCredential` or :class:`InteractiveBrowserCredential`
    :keyword cache_persistence_options: configuration for persistent token caching. If not provided, the credential
        will use the persistent cache shared by Microsoft development applications
    :paramtype cache_persistence_options: ~azure.identity.TokenCachePersistenceOptions
    """
    def __init__(self, username: str | None = None, **kwargs: Any) -> None: ...
    def __enter__(self): ...
    def __exit__(self, *args) -> None: ...
    def close(self) -> None:
        """Close the credential's transport session."""
    def get_token(self, *scopes: str, claims: str | None = None, tenant_id: str | None = None, **kwargs: Any) -> AccessToken:
        """Get an access token for `scopes` from the shared cache.

        If no access token is cached, attempt to acquire one using a cached refresh token.

        This method is called automatically by Azure SDK clients.

        :param str scopes: desired scopes for the access token. This method requires at least one scope.
            For more information about scopes, see
            https://learn.microsoft.com/azure/active-directory/develop/scopes-oidc.
        :keyword str claims: additional claims required in the token, such as those returned in a resource provider's
            claims challenge following an authorization failure
        :keyword str tenant_id: not used by this credential; any value provided will be ignored.
        :keyword bool enable_cae: indicates whether to enable Continuous Access Evaluation (CAE) for the requested
            token. Defaults to False.

        :return: An access token with the desired scopes.
        :rtype: ~azure.core.credentials.AccessToken
        :raises ~azure.identity.CredentialUnavailableError: the cache is unavailable or contains insufficient user
            information
        :raises ~azure.core.exceptions.ClientAuthenticationError: authentication failed. The error's ``message``
            attribute gives a reason.
        """
    @staticmethod
    def supported() -> bool:
        """Whether the shared token cache is supported on the current platform.

        :return: True if the shared token cache is supported on the current platform, otherwise False.
        :rtype: bool
        """

class _SharedTokenCacheCredential(SharedTokenCacheBase):
    """The original SharedTokenCacheCredential, which doesn't use msal.ClientApplication"""
    def __enter__(self): ...
    def __exit__(self, *args) -> None: ...
    def get_token(self, *scopes: str, claims: str | None = None, tenant_id: str | None = None, **kwargs: Any) -> AccessToken: ...
