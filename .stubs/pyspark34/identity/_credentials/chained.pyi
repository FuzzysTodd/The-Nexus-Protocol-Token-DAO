from .. import CredentialUnavailableError as CredentialUnavailableError
from .._internal import within_credential_chain as within_credential_chain
from _typeshed import Incomplete
from azure.core.credentials import AccessToken as AccessToken, TokenCredential as TokenCredential
from typing import Any

class ChainedTokenCredential:
    """A sequence of credentials that is itself a credential.

    Its :func:`get_token` method calls ``get_token`` on each credential in the sequence, in order, returning the first
    valid token received.

    :param credentials: credential instances to form the chain
    :type credentials: ~azure.core.credentials.TokenCredential

    .. admonition:: Example:

        .. literalinclude:: ../samples/credential_creation_code_snippets.py
            :start-after: [START create_chained_token_credential]
            :end-before: [END create_chained_token_credential]
            :language: python
            :dedent: 4
            :caption: Create a ChainedTokenCredential.
    """
    credentials: Incomplete
    def __init__(self, *credentials: TokenCredential) -> None: ...
    def __enter__(self): ...
    def __exit__(self, *args: Any): ...
    def close(self) -> None:
        """Close the transport session of each credential in the chain."""
    def get_token(self, *scopes: str, claims: str | None = None, tenant_id: str | None = None, **kwargs: Any) -> AccessToken:
        """Request a token from each chained credential, in order, returning the first token received.

        This method is called automatically by Azure SDK clients.

        :param str scopes: desired scopes for the access token. This method requires at least one scope.
            For more information about scopes, see
            https://learn.microsoft.com/azure/active-directory/develop/scopes-oidc.
        :keyword str claims: additional claims required in the token, such as those returned in a resource provider's
            claims challenge following an authorization failure.
        :keyword str tenant_id: optional tenant to include in the token request.

        :return: An access token with the desired scopes.
        :rtype: ~azure.core.credentials.AccessToken
        :raises ~azure.core.exceptions.ClientAuthenticationError: no credential in the chain provided a token
        """
