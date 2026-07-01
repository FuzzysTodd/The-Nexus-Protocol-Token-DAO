import abc
from .._constants import AZURE_VSCODE_CLIENT_ID as AZURE_VSCODE_CLIENT_ID, AzureAuthorityHosts as AzureAuthorityHosts, EnvironmentVariables as EnvironmentVariables
from .._exceptions import CredentialUnavailableError as CredentialUnavailableError
from .._internal import normalize_authority as normalize_authority, validate_tenant_id as validate_tenant_id, within_dac as within_dac
from .._internal.aad_client import AadClient as AadClient, AadClientBase as AadClientBase
from .._internal.decorators import log_get_token as log_get_token
from .._internal.get_token_mixin import GetTokenMixin as GetTokenMixin
from .._internal.linux_vscode_adapter import get_refresh_token as get_refresh_token, get_user_settings as get_user_settings
from azure.core.credentials import AccessToken as AccessToken
from typing import Any

class _VSCodeCredentialBase(abc.ABC, metaclass=abc.ABCMeta):
    def __init__(self, **kwargs: Any) -> None: ...

class VisualStudioCodeCredential(_VSCodeCredentialBase, GetTokenMixin):
    '''Authenticates as the Azure user signed in to Visual Studio Code via the \'Azure Account\' extension.

    It\'s a `known issue <https://github.com/Azure/azure-sdk-for-python/issues/23249>`_ that this credential doesn\'t
    work with `Azure Account extension <https://marketplace.visualstudio.com/items?itemName=ms-vscode.azure-account>`_
    versions newer than **0.9.11**. A long-term fix to this problem is in progress. In the meantime, consider
    authenticating with :class:`AzureCliCredential`.

    :keyword str authority: Authority of an Azure Active Directory endpoint, for example "login.microsoftonline.com".
        This argument is required for a custom cloud and usually unnecessary otherwise. Defaults to the authority
        matching the "Azure: Cloud" setting in VS Code\'s user settings or, when that setting has no value, the
        authority for Azure Public Cloud.
    :keyword str tenant_id: ID of the tenant the credential should authenticate in. Defaults to the "Azure: Tenant"
        setting in VS Code\'s user settings or, when that setting has no value, the "organizations" tenant, which
        supports only Azure Active Directory work or school accounts.
    :keyword List[str] additionally_allowed_tenants: Specifies tenants in addition to the specified "tenant_id"
        for which the credential may acquire tokens. Add the wildcard value "*" to allow the credential to
        acquire tokens for any tenant the application can access.
    '''
    def __enter__(self): ...
    def __exit__(self, *args) -> None: ...
    def close(self) -> None:
        """Close the credential's transport session."""
    def get_token(self, *scopes: str, claims: str | None = None, tenant_id: str | None = None, **kwargs: Any) -> AccessToken:
        """Request an access token for `scopes` as the user currently signed in to Visual Studio Code.

        This method is called automatically by Azure SDK clients.

        :param str scopes: desired scopes for the access token. This method requires at least one scope.
            For more information about scopes, see
            https://learn.microsoft.com/azure/active-directory/develop/scopes-oidc.
        :keyword str claims: additional claims required in the token, such as those returned in a resource provider's
            claims challenge following an authorization failure.
        :keyword str tenant_id: optional tenant to include in the token request.

        :return: An access token with the desired scopes.
        :rtype: ~azure.core.credentials.AccessToken
        :raises ~azure.identity.CredentialUnavailableError: the credential cannot retrieve user details from Visual
          Studio Code
        """
