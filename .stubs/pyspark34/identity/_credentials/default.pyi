from .._constants import EnvironmentVariables as EnvironmentVariables
from .._internal import get_default_authority as get_default_authority, normalize_authority as normalize_authority, within_dac as within_dac
from .azd_cli import AzureDeveloperCliCredential as AzureDeveloperCliCredential
from .azure_cli import AzureCliCredential as AzureCliCredential
from .azure_powershell import AzurePowerShellCredential as AzurePowerShellCredential
from .browser import InteractiveBrowserCredential as InteractiveBrowserCredential
from .chained import ChainedTokenCredential as ChainedTokenCredential
from .environment import EnvironmentCredential as EnvironmentCredential
from .managed_identity import ManagedIdentityCredential as ManagedIdentityCredential
from .shared_cache import SharedTokenCacheCredential as SharedTokenCacheCredential
from .vscode import VisualStudioCodeCredential as VisualStudioCodeCredential
from .workload_identity import WorkloadIdentityCredential as WorkloadIdentityCredential
from azure.core.credentials import AccessToken as AccessToken, TokenCredential as TokenCredential
from typing import Any

class DefaultAzureCredential(ChainedTokenCredential):
    '''A default credential capable of handling most Azure SDK authentication scenarios.

    The identity it uses depends on the environment. When an access token is needed, it requests one using these
    identities in turn, stopping when one provides a token:

    1. A service principal configured by environment variables. See :class:`~azure.identity.EnvironmentCredential` for
       more details.
    2. WorkloadIdentityCredential if environment variable configuration is set by the Azure workload
       identity webhook.
    3. An Azure managed identity. See :class:`~azure.identity.ManagedIdentityCredential` for more details.
    4. On Windows only: a user who has signed in with a Microsoft application, such as Visual Studio. If multiple
       identities are in the cache, then the value of  the environment variable ``AZURE_USERNAME`` is used to select
       which identity to use. See :class:`~azure.identity.SharedTokenCacheCredential` for more details.
    5. The identity currently logged in to the Azure CLI.
    6. The identity currently logged in to Azure PowerShell.
    7. The identity currently logged in to the Azure Developer CLI.

    This default behavior is configurable with keyword arguments.

    :keyword str authority: Authority of an Azure Active Directory endpoint, for example \'login.microsoftonline.com\',
        the authority for Azure Public Cloud (which is the default). :class:`~azure.identity.AzureAuthorityHosts`
        defines authorities for other clouds. Managed identities ignore this because they reside in a single cloud.
    :keyword bool exclude_workload_identity_credential: Whether to exclude the workload identity from the credential.
        Defaults to **False**.
    :keyword bool exclude_developer_cli_credential: Whether to exclude the Azure Developer CLI
        from the credential. Defaults to **False**.
    :keyword bool exclude_cli_credential: Whether to exclude the Azure CLI from the credential. Defaults to **False**.
    :keyword bool exclude_environment_credential: Whether to exclude a service principal configured by environment
        variables from the credential. Defaults to **False**.
    :keyword bool exclude_managed_identity_credential: Whether to exclude managed identity from the credential.
        Defaults to **False**.
    :keyword bool exclude_powershell_credential: Whether to exclude Azure PowerShell. Defaults to **False**.
    :keyword bool exclude_visual_studio_code_credential: Whether to exclude stored credential from VS Code.
        Defaults to **True**.
    :keyword bool exclude_shared_token_cache_credential: Whether to exclude the shared token cache. Defaults to
        **False**.
    :keyword bool exclude_interactive_browser_credential: Whether to exclude interactive browser authentication (see
        :class:`~azure.identity.InteractiveBrowserCredential`). Defaults to **True**.
    :keyword str interactive_browser_tenant_id: Tenant ID to use when authenticating a user through
        :class:`~azure.identity.InteractiveBrowserCredential`. Defaults to the value of environment variable
        AZURE_TENANT_ID, if any. If unspecified, users will authenticate in their home tenants.
    :keyword str managed_identity_client_id: The client ID of a user-assigned managed identity. Defaults to the value
        of the environment variable AZURE_CLIENT_ID, if any. If not specified, a system-assigned identity will be used.
    :keyword str workload_identity_client_id: The client ID of an identity assigned to the pod. Defaults to the value
        of the environment variable AZURE_CLIENT_ID, if any. If not specified, the pod\'s default identity will be used.
    :keyword str workload_identity_tenant_id: Preferred tenant for :class:`~azure.identity.WorkloadIdentityCredential`.
        Defaults to the value of environment variable AZURE_TENANT_ID, if any.
    :keyword str interactive_browser_client_id: The client ID to be used in interactive browser credential. If not
        specified, users will authenticate to an Azure development application.
    :keyword str shared_cache_username: Preferred username for :class:`~azure.identity.SharedTokenCacheCredential`.
        Defaults to the value of environment variable AZURE_USERNAME, if any.
    :keyword str shared_cache_tenant_id: Preferred tenant for :class:`~azure.identity.SharedTokenCacheCredential`.
        Defaults to the value of environment variable AZURE_TENANT_ID, if any.
    :keyword str visual_studio_code_tenant_id: Tenant ID to use when authenticating with
        :class:`~azure.identity.VisualStudioCodeCredential`. Defaults to the "Azure: Tenant" setting in VS Code\'s user
        settings or, when that setting has no value, the "organizations" tenant, which supports only Azure Active
        Directory work or school accounts.
    :keyword int process_timeout: The timeout in seconds to use for developer credentials that run
        subprocesses (e.g. AzureCliCredential, AzurePowerShellCredential). Defaults to **10** seconds.

    .. admonition:: Example:

        .. literalinclude:: ../samples/credential_creation_code_snippets.py
            :start-after: [START create_default_credential]
            :end-before: [END create_default_credential]
            :language: python
            :dedent: 4
            :caption: Create a DefaultAzureCredential.
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
