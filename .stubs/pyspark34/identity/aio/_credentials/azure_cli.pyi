from ... import CredentialUnavailableError as CredentialUnavailableError
from ..._credentials.azure_cli import CLI_NOT_FOUND as CLI_NOT_FOUND, COMMAND_LINE as COMMAND_LINE, EXECUTABLE_NAME as EXECUTABLE_NAME, NOT_LOGGED_IN as NOT_LOGGED_IN, get_safe_working_dir as get_safe_working_dir, parse_token as parse_token, sanitize_output as sanitize_output
from ..._internal import resolve_tenant as resolve_tenant, validate_scope as validate_scope, validate_tenant_id as validate_tenant_id, within_dac as within_dac
from .._internal import AsyncContextManager as AsyncContextManager
from .._internal.decorators import log_get_token_async as log_get_token_async
from _typeshed import Incomplete
from azure.core.credentials import AccessToken as AccessToken
from typing import Any, List

class AzureCliCredential(AsyncContextManager):
    '''Authenticates by requesting a token from the Azure CLI.

    This requires previously logging in to Azure via "az login", and will use the CLI\'s currently logged in identity.

    :keyword str tenant_id: Optional tenant to include in the token request.
    :keyword List[str] additionally_allowed_tenants: Specifies tenants in addition to the specified "tenant_id"
        for which the credential may acquire tokens. Add the wildcard value "*" to allow the credential to
        acquire tokens for any tenant the application can access.
    :keyword int process_timeout: Seconds to wait for the Azure CLI process to respond. Defaults to 10 seconds.

    .. admonition:: Example:

        .. literalinclude:: ../samples/credential_creation_code_snippets.py
            :start-after: [START create_azure_cli_credential_async]
            :end-before: [END create_azure_cli_credential_async]
            :language: python
            :dedent: 4
            :caption: Create an AzureCliCredential.
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
        :raises ~azure.identity.CredentialUnavailableError: the credential was unable to invoke the Azure CLI.
        :raises ~azure.core.exceptions.ClientAuthenticationError: the credential invoked the Azure CLI but didn't
          receive an access token.
        """
    async def close(self) -> None:
        """Calling this method is unnecessary"""
