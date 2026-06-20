from ... import CredentialUnavailableError as CredentialUnavailableError
from ..._credentials.azure_powershell import get_command_line as get_command_line, get_safe_working_dir as get_safe_working_dir, parse_token as parse_token, raise_for_error as raise_for_error
from ..._internal import resolve_tenant as resolve_tenant, validate_scope as validate_scope, validate_tenant_id as validate_tenant_id
from .._internal import AsyncContextManager as AsyncContextManager
from .._internal.decorators import log_get_token_async as log_get_token_async
from _typeshed import Incomplete
from azure.core.credentials import AccessToken as AccessToken
from typing import Any, List

class AzurePowerShellCredential(AsyncContextManager):
    '''Authenticates by requesting a token from Azure PowerShell.

    This requires previously logging in to Azure via "Connect-AzAccount", and will use the currently logged in identity.

    :keyword str tenant_id: Optional tenant to include in the token request.
    :keyword List[str] additionally_allowed_tenants: Specifies tenants in addition to the specified "tenant_id"
        for which the credential may acquire tokens. Add the wildcard value "*" to allow the credential to
        acquire tokens for any tenant the application can access.
    :keyword int process_timeout: Seconds to wait for the Azure PowerShell process to respond. Defaults to 10 seconds.

    .. admonition:: Example:

        .. literalinclude:: ../samples/credential_creation_code_snippets.py
            :start-after: [START create_azure_power_shell_credential_async]
            :end-before: [END create_azure_power_shell_credential_async]
            :language: python
            :dedent: 4
            :caption: Create an AzurePowerShellCredential.
    '''
    tenant_id: Incomplete
    def __init__(self, *, tenant_id: str = '', additionally_allowed_tenants: List[str] | None = None, process_timeout: int = 10) -> None: ...
    async def get_token(self, *scopes: str, claims: str | None = None, tenant_id: str | None = None, **kwargs: Any) -> AccessToken:
        """Request an access token for `scopes`.

        This method is called automatically by Azure SDK clients. Applications calling this method directly must
        also handle token caching because this credential doesn't cache the tokens it acquires.

        :param str scopes: desired scope for the access token. This credential allows only one scope per request.
            For more information about scopes, see
            https://learn.microsoft.com/azure/active-directory/develop/scopes-oidc.
        :keyword str claims: not used by this credential; any value provided will be ignored.
        :keyword str tenant_id: optional tenant to include in the token request.

        :return: An access token with the desired scopes.
        :rtype: ~azure.core.credentials.AccessToken
        :raises ~azure.identity.CredentialUnavailableError: the credential was unable to invoke Azure PowerShell, or
          no account is authenticated
        :raises ~azure.core.exceptions.ClientAuthenticationError: the credential invoked Azure PowerShell but didn't
          receive an access token
        """
    async def close(self) -> None:
        """Calling this method is unnecessary"""

async def run_command_line(command_line: List[str], timeout: int) -> str: ...
async def start_process(command_line): ...
