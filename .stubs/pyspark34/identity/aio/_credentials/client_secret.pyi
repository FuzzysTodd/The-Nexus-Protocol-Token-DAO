from ..._internal import validate_tenant_id as validate_tenant_id
from .._internal import AadClient as AadClient, AsyncContextManager as AsyncContextManager
from .._internal.get_token_mixin import GetTokenMixin as GetTokenMixin
from azure.core.credentials import AccessToken as AccessToken
from typing import Any, TypeVar

T = TypeVar('T', bound='ClientSecretCredential')

class ClientSecretCredential(AsyncContextManager, GetTokenMixin):
    '''Authenticates as a service principal using a client secret.

    :param str tenant_id: ID of the service principal\'s tenant. Also called its \'directory\' ID.
    :param str client_id: The service principal\'s client ID
    :param str client_secret: One of the service principal\'s client secrets

    :keyword str authority: Authority of an Azure Active Directory endpoint, for example \'login.microsoftonline.com\',
          the authority for Azure Public Cloud (which is the default). :class:`~azure.identity.AzureAuthorityHosts`
          defines authorities for other clouds.
    :keyword cache_persistence_options: Configuration for persistent token caching. If unspecified, the credential
          will cache tokens in memory.
    :paramtype cache_persistence_options: ~azure.identity.TokenCachePersistenceOptions
    :keyword List[str] additionally_allowed_tenants: Specifies tenants in addition to the specified "tenant_id"
        for which the credential may acquire tokens. Add the wildcard value "*" to allow the credential to
        acquire tokens for any tenant the application can access.

    .. admonition:: Example:

        .. literalinclude:: ../samples/credential_creation_code_snippets.py
            :start-after: [START create_client_secret_credential_async]
            :end-before: [END create_client_secret_credential_async]
            :language: python
            :dedent: 4
            :caption: Create a ClientSecretCredential.
    '''
    def __init__(self, tenant_id: str, client_id: str, client_secret: str, **kwargs: Any) -> None: ...
    async def __aenter__(self) -> T: ...
    async def close(self) -> None:
        """Close the credential's transport session."""
