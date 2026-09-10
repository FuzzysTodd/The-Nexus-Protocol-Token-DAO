from ... import CredentialUnavailableError as CredentialUnavailableError
from ..._constants import EnvironmentVariables as EnvironmentVariables
from .._internal import AsyncContextManager as AsyncContextManager
from .._internal.decorators import log_get_token_async as log_get_token_async
from azure.core.credentials import AccessToken as AccessToken
from azure.core.credentials_async import AsyncTokenCredential as AsyncTokenCredential
from typing import Any

class ManagedIdentityCredential(AsyncContextManager):
    '''Authenticates with an Azure managed identity in any hosting environment which supports managed identities.

    This credential defaults to using a system-assigned identity. To configure a user-assigned identity, use one of
    the keyword arguments. See `Azure Active Directory documentation
    <https://docs.microsoft.com/azure/active-directory/managed-identities-azure-resources/overview>`_ for more
    information about configuring managed identity for applications.

    :keyword str client_id: a user-assigned identity\'s client ID or, when using Pod Identity, the client ID of an Azure
        AD app registration. This argument is supported in all hosting environments.
    :keyword identity_config: a mapping ``{parameter_name: value}`` specifying a user-assigned identity by its object
        or resource ID, for example ``{"object_id": "..."}``. Check the documentation for your hosting environment to
        learn what values it expects.
    :paramtype identity_config: Mapping[str, str]

    .. admonition:: Example:

        .. literalinclude:: ../samples/credential_creation_code_snippets.py
            :start-after: [START create_managed_identity_credential_async]
            :end-before: [END create_managed_identity_credential_async]
            :language: python
            :dedent: 4
            :caption: Create a ManagedIdentityCredential.
    '''
    def __init__(self, **kwargs: Any) -> None: ...
    async def __aenter__(self): ...
    async def close(self) -> None:
        """Close the credential's transport session."""
    async def get_token(self, *scopes: str, claims: str | None = None, tenant_id: str | None = None, **kwargs: Any) -> AccessToken:
        """Asynchronously request an access token for `scopes`.

        This method is called automatically by Azure SDK clients.

        :param str scopes: desired scope for the access token. This credential allows only one scope per request.
            For more information about scopes, see
            https://learn.microsoft.com/azure/active-directory/develop/scopes-oidc.
        :keyword str claims: not used by this credential; any value provided will be ignored.
        :keyword str tenant_id: not used by this credential; any value provided will be ignored.

        :return: An access token with the desired scopes.
        :rtype: ~azure.core.credentials.AccessToken
        :raises ~azure.identity.CredentialUnavailableError: managed identity isn't available in the hosting environment
        """
