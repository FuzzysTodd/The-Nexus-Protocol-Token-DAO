from .. import CredentialUnavailableError as CredentialUnavailableError
from .._constants import EnvironmentVariables as EnvironmentVariables
from .._internal.decorators import log_get_token as log_get_token
from .certificate import CertificateCredential as CertificateCredential
from .client_secret import ClientSecretCredential as ClientSecretCredential
from .user_password import UsernamePasswordCredential as UsernamePasswordCredential
from azure.core.credentials import AccessToken as AccessToken
from typing import Any

EnvironmentCredentialTypes = CertificateCredential | ClientSecretCredential | UsernamePasswordCredential

class EnvironmentCredential:
    '''A credential configured by environment variables.

    This credential is capable of authenticating as a service principal using a client secret or a certificate, or as
    a user with a username and password. Configuration is attempted in this order, using these environment variables:

    Service principal with secret:
      - **AZURE_TENANT_ID**: ID of the service principal\'s tenant. Also called its \'directory\' ID.
      - **AZURE_CLIENT_ID**: the service principal\'s client ID
      - **AZURE_CLIENT_SECRET**: one of the service principal\'s client secrets
      - **AZURE_AUTHORITY_HOST**: authority of an Azure Active Directory endpoint, for example
        "login.microsoftonline.com", the authority for Azure Public Cloud, which is the default
        when no value is given.

    Service principal with certificate:
      - **AZURE_TENANT_ID**: ID of the service principal\'s tenant. Also called its \'directory\' ID.
      - **AZURE_CLIENT_ID**: the service principal\'s client ID
      - **AZURE_CLIENT_CERTIFICATE_PATH**: path to a PEM or PKCS12 certificate file including the private key.
      - **AZURE_CLIENT_CERTIFICATE_PASSWORD**: (optional) password of the certificate file, if any.
      - **AZURE_AUTHORITY_HOST**: authority of an Azure Active Directory endpoint, for example
        "login.microsoftonline.com", the authority for Azure Public Cloud, which is the default
        when no value is given.

    User with username and password:
      - **AZURE_CLIENT_ID**: the application\'s client ID
      - **AZURE_USERNAME**: a username (usually an email address)
      - **AZURE_PASSWORD**: that user\'s password
      - **AZURE_TENANT_ID**: (optional) ID of the service principal\'s tenant. Also called its \'directory\' ID.
        If not provided, defaults to the \'organizations\' tenant, which supports only Azure Active Directory work or
        school accounts.
      - **AZURE_AUTHORITY_HOST**: authority of an Azure Active Directory endpoint, for example
        "login.microsoftonline.com", the authority for Azure Public Cloud, which is the default
        when no value is given.

    .. admonition:: Example:

        .. literalinclude:: ../samples/credential_creation_code_snippets.py
            :start-after: [START create_environment_credential]
            :end-before: [END create_environment_credential]
            :language: python
            :dedent: 4
            :caption: Create an EnvironmentCredential.
    '''
    def __init__(self, **kwargs: Any) -> None: ...
    def __enter__(self): ...
    def __exit__(self, *args) -> None: ...
    def close(self) -> None:
        """Close the credential's transport session."""
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

        :raises ~azure.identity.CredentialUnavailableError: environment variable configuration is incomplete
        """
