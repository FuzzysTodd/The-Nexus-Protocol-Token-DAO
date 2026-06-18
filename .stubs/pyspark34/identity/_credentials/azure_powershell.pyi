import subprocess
from .. import CredentialUnavailableError as CredentialUnavailableError
from .._internal import resolve_tenant as resolve_tenant, validate_scope as validate_scope, validate_tenant_id as validate_tenant_id, within_dac as within_dac
from .._internal.decorators import log_get_token as log_get_token
from .azure_cli import get_safe_working_dir as get_safe_working_dir
from _typeshed import Incomplete
from azure.core.credentials import AccessToken
from typing import Any, List, Tuple

AZ_ACCOUNT_NOT_INSTALLED: str
BLOCKED_BY_EXECUTION_POLICY: str
NO_AZ_ACCOUNT_MODULE: str
POWERSHELL_NOT_INSTALLED: str
RUN_CONNECT_AZ_ACCOUNT: str
SCRIPT: str

class AzurePowerShellCredential:
    '''Authenticates by requesting a token from Azure PowerShell.

    This requires previously logging in to Azure via "Connect-AzAccount", and will use the currently logged in identity.

    :keyword str tenant_id: Optional tenant to include in the token request.
    :keyword List[str] additionally_allowed_tenants: Specifies tenants in addition to the specified "tenant_id"
        for which the credential may acquire tokens. Add the wildcard value "*" to allow the credential to
        acquire tokens for any tenant the application can access.
    :keyword int process_timeout: Seconds to wait for the Azure PowerShell process to respond. Defaults to 10 seconds.

    .. admonition:: Example:

        .. literalinclude:: ../samples/credential_creation_code_snippets.py
            :start-after: [START create_azure_power_shell_credential]
            :end-before: [END create_azure_power_shell_credential]
            :language: python
            :dedent: 4
            :caption: Create an AzurePowerShellCredential.
    '''
    tenant_id: Incomplete
    def __init__(self, *, tenant_id: str = '', additionally_allowed_tenants: List[str] | None = None, process_timeout: int = 10) -> None: ...
    def __enter__(self): ...
    def __exit__(self, *args) -> None: ...
    def close(self) -> None:
        """Calling this method is unnecessary."""
    def get_token(self, *scopes: str, claims: str | None = None, tenant_id: str | None = None, **kwargs: Any) -> AccessToken:
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

def run_command_line(command_line: List[str], timeout: int) -> str: ...
def start_process(args: List[str]) -> subprocess.Popen: ...
def parse_token(output: str) -> AccessToken: ...
def get_command_line(scopes: Tuple[str, ...], tenant_id: str) -> List[str]: ...
def raise_for_error(return_code: int, stdout: str, stderr: str) -> None: ...
