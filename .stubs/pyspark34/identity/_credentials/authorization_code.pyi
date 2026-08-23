from .._internal.aad_client import AadClient as AadClient
from .._internal.get_token_mixin import GetTokenMixin as GetTokenMixin
from azure.core.credentials import AccessToken as AccessToken
from typing import Any

class AuthorizationCodeCredential(GetTokenMixin):
    '''Authenticates by redeeming an authorization code previously obtained from Azure Active Directory.

    See `Azure Active Directory documentation
    <https://docs.microsoft.com/azure/active-directory/develop/v2-oauth2-auth-code-flow>`_ for more information
    about the authentication flow.

    :param str tenant_id: ID of the application\'s Azure Active Directory tenant. Also called its "directory" ID.
    :param str client_id: The application\'s client ID
    :param str authorization_code: The authorization code from the user\'s log-in
    :param str redirect_uri: The application\'s redirect URI. Must match the URI used to request the authorization code.

    :keyword str authority: Authority of an Azure Active Directory endpoint, for example "login.microsoftonline.com",
        the authority for Azure Public Cloud (which is the default). :class:`~azure.identity.AzureAuthorityHosts`
        defines authorities for other clouds.
    :keyword str client_secret: One of the application\'s client secrets. Required only for web apps and web APIs.
    :keyword List[str] additionally_allowed_tenants: Specifies tenants in addition to the specified "tenant_id"
        for which the credential may acquire tokens. Add the wildcard value "*" to allow the credential to
        acquire tokens for any tenant the application can access.

    .. admonition:: Example:

        .. literalinclude:: ../samples/credential_creation_code_snippets.py
            :start-after: [START create_authorization_code_credential]
            :end-before: [END create_authorization_code_credential]
            :language: python
            :dedent: 4
            :caption: Create an AuthorizationCodeCredential.
    '''
    def __init__(self, tenant_id: str, client_id: str, authorization_code: str, redirect_uri: str, **kwargs: Any) -> None: ...
    def __enter__(self): ...
    def __exit__(self, *args) -> None: ...
    def close(self) -> None:
        """Close the credential's transport session."""
    def get_token(self, *scopes: str, claims: str | None = None, tenant_id: str | None = None, **kwargs: Any) -> AccessToken:
        """Request an access token for `scopes`.

        This method is called automatically by Azure SDK clients.

        The first time this method is called, the credential will redeem its authorization code. On subsequent calls
        the credential will return a cached access token or redeem a refresh token, if it acquired a refresh token upon
        redeeming the authorization code.

        :param str scopes: desired scopes for the access token. This method requires at least one scope.
            For more information about scopes, see
            https://learn.microsoft.com/azure/active-directory/develop/scopes-oidc.
        :keyword str claims: additional claims required in the token, such as those returned in a resource provider's
            claims challenge following an authorization failure.
        :keyword str tenant_id: optional tenant to include in the token request.

        :return: An access token with the desired scopes.
        :rtype: ~azure.core.credentials.AccessToken
        :raises ~azure.core.exceptions.ClientAuthenticationError: authentication failed. The error's ``message``
          attribute gives a reason. Any error response from Azure Active Directory is available as the error's
          ``response`` attribute.
        """
