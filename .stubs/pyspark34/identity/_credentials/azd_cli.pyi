from .. import CredentialUnavailableError as CredentialUnavailableError
from .._internal import resolve_tenant as resolve_tenant, validate_scope as validate_scope, validate_tenant_id as validate_tenant_id, within_dac as within_dac
from .._internal.decorators import log_get_token as log_get_token
from _typeshed import Incomplete
from azure.core.credentials import AccessToken
from typing import Any, List

CLI_NOT_FOUND: str
COMMAND_LINE: str
EXECUTABLE_NAME: str
NOT_LOGGED_IN: str

class AzureDeveloperCliCredential:
    '''Authenticates by requesting a token from the Azure Developer CLI.

    Azure Developer CLI is a command-line interface tool that allows developers to create, manage, and deploy
    resources in Azure. It\'s built on top of the Azure CLI and provides additional functionality specific
    to Azure developers. It allows users to authenticate as a user and/or a service principal against
    `Azure Active Directory (Azure AD) <"https://learn.microsoft.com/azure/active-directory/fundamentals/">`__.
    The AzureDeveloperCliCredential authenticates in a development environment and acquires a token on behalf of
    the logged-in user or service principal in Azure Developer CLI. It acts as the Azure Developer CLI logged-in user
    or service principal and executes an Azure CLI command underneath to authenticate the application against
    Azure Active Directory.

    To use this credential, the developer needs to authenticate locally in Azure Developer CLI using one of the
    commands below:

      * Run "azd auth login" in Azure Developer CLI to authenticate interactively as a user.
      * Run "azd auth login --client-id \'client_id\' --client-secret \'client_secret\' --tenant-id \'tenant_id\'"
        to authenticate as a service principal.

    You may need to repeat this process after a certain time period, depending on the refresh token validity in your
    organization. Generally, the refresh token validity period is a few weeks to a few months.
    AzureDeveloperCliCredential will prompt you to sign in again.

    :keyword str tenant_id: Optional tenant to include in the token request.
    :keyword List[str] additionally_allowed_tenants: Specifies tenants in addition to the specified "tenant_id"
        for which the credential may acquire tokens. Add the wildcard value "*" to allow the credential to
        acquire tokens for any tenant the application can access.
    :keyword int process_timeout: Seconds to wait for the Azure Developer CLI process to respond. Defaults
        to 10 seconds.

    .. admonition:: Example:

        .. literalinclude:: ../samples/credential_creation_code_snippets.py
            :start-after: [START azure_developer_cli_credential]
            :end-before: [END azure_developer_cli_credential]
            :language: python
            :dedent: 4
            :caption: Create an AzureDeveloperCliCredential.
    '''
    tenant_id: Incomplete
    def __init__(self, *, tenant_id: str = '', additionally_allowed_tenants: List[str] | None = None, process_timeout: int = 10) -> None: ...
    def __enter__(self) -> AzureDeveloperCliCredential: ...
    def __exit__(self, *args: Any) -> None: ...
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

        :raises ~azure.identity.CredentialUnavailableError: the credential was unable to invoke
          the Azure Developer CLI.
        :raises ~azure.core.exceptions.ClientAuthenticationError: the credential invoked
          the Azure Developer CLI but didn't receive an access token.
        """

def parse_token(output: str) -> AccessToken | None:
    '''Parse to an AccessToken.

    In particular, convert the "expiresOn" value to epoch seconds. This value is a naive local datetime as returned by
    datetime.fromtimestamp.

    :param str output: The output of the Azure Developer CLI command.
    :return: An AccessToken or None if the output isn\'t valid.
    :rtype: azure.core.credentials.AccessToken or None
    '''
def get_safe_working_dir() -> str:
    """Invoke 'azd' from a directory controlled by the OS, not the executing program's directory.

    :return: The path to the directory.
    :rtype: str
    :raises ~azure.identity.CredentialUnavailableError: the SYSTEMROOT environment variable is not set.
    """
def sanitize_output(output: str) -> str:
    """Redact tokens from CLI output to prevent error messages revealing them.

    :param str output: The output of the Azure Developer CLI command.
    :return: The output with tokens redacted.
    :rtype: str
    """
