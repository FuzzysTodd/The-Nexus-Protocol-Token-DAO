from .._constants import EnvironmentVariables as EnvironmentVariables
from .._internal import get_default_authority as get_default_authority, normalize_authority as normalize_authority
from .chained import ChainedTokenCredential as ChainedTokenCredential
from .environment import EnvironmentCredential as EnvironmentCredential
from .managed_identity import ManagedIdentityCredential as ManagedIdentityCredential
from azure.core.credentials import AccessToken as AccessToken
from typing import Any

class AzureApplicationCredential(ChainedTokenCredential):
    '''A credential for Azure Active Directory applications.

    This credential is designed for applications deployed to Azure (:class:`~azure.identity.DefaultAzureCredential` is
    better suited to local development). It authenticates service principals and managed identities.

    For service principal authentication, set these environment variables to identify a principal:

        - **AZURE_TENANT_ID**: ID of the service principal\'s tenant. Also called its "directory" ID.
        - **AZURE_CLIENT_ID**: the service principal\'s client ID

    And one of these to authenticate that principal:

        - **AZURE_CLIENT_SECRET**: one of the service principal\'s client secrets

        **or**

        - **AZURE_CLIENT_CERTIFICATE_PATH**: path to a PEM-encoded certificate file including the private key. The
          certificate must not be password-protected.

    See `Azure CLI documentation <https://docs.microsoft.com/cli/azure/create-an-azure-service-principal-azure-cli>`_
    for more information about creating and managing service principals.

    When this environment configuration is incomplete, the credential will attempt to authenticate a managed identity.
    See `Azure Active Directory documentation
    <https://docs.microsoft.com/azure/active-directory/managed-identities-azure-resources/overview>`_ for an overview of
    managed identities.

    :keyword str authority: Authority of an Azure Active Directory endpoint, for example "login.microsoftonline.com",
        the authority for Azure Public Cloud, which is the default when no value is given for this keyword argument or
        environment variable AZURE_AUTHORITY_HOST. :class:`~azure.identity.AzureAuthorityHosts` defines authorities for
        other clouds. Authority configuration applies only to service principal authentication.
    :keyword str managed_identity_client_id: The client ID of a user-assigned managed identity. Defaults to the value
        of the environment variable AZURE_CLIENT_ID, if any. If not specified, a system-assigned identity will be used.
    '''
    def __init__(self, **kwargs: Any) -> None: ...
    def get_token(self, *scopes: str, claims: str | None = None, tenant_id: str | None = None, **kwargs: Any) -> AccessToken:
        """Request an access token for `scopes`.

        This method is called automatically by Azure SDK clients.

        :param str scopes: desired scopes for the access token. This method requires at least one scope.
            For more information about scopes, see
            https://learn.microsoft.com/azure/active-directory/develop/scopes-oidc.
        :keyword str claims: additional claims required in the token, such as those returned in a resource provider's
            claims challenge following an authorization failure.
        :keyword str tenant_id: optional tenant to include in the token request.

        :return: An access token with the desired scopes.
        :rtype: ~azure.core.credentials.AccessToken
        :raises ~azure.core.exceptions.ClientAuthenticationError: authentication failed. The exception has a
            `message` attribute listing each authentication attempt and its error message.
        """
