from ..._credentials.certificate import get_client_credential as get_client_credential
from ..._internal import AadClientCertificate as AadClientCertificate, validate_tenant_id as validate_tenant_id
from .._internal import AadClient as AadClient, AsyncContextManager as AsyncContextManager
from .._internal.get_token_mixin import GetTokenMixin as GetTokenMixin
from azure.core.credentials import AccessToken as AccessToken
from typing import Any

class OnBehalfOfCredential(AsyncContextManager, GetTokenMixin):
    '''Authenticates a service principal via the on-behalf-of flow.

    This flow is typically used by middle-tier services that authorize requests to other services with a delegated
    user identity. Because this is not an interactive authentication flow, an application using it must have admin
    consent for any delegated permissions before requesting tokens for them. See `Azure Active Directory documentation
    <https://docs.microsoft.com/azure/active-directory/develop/v2-oauth2-on-behalf-of-flow>`_ for a more detailed
    description of the on-behalf-of flow.

    :param str tenant_id: ID of the service principal\'s tenant. Also called its "directory" ID.
    :param str client_id: The service principal\'s client ID
    :keyword str client_secret: Optional. A client secret to authenticate the service principal.
        Either **client_secret** or **client_certificate** must be provided.
    :keyword bytes client_certificate: Optional. The bytes of a certificate in PEM or PKCS12 format including
        the private key to authenticate the service principal. Either **client_secret** or **client_certificate** must
        be provided.
    :keyword str user_assertion: Required. The access token the credential will use as the user assertion when
        requesting on-behalf-of tokens

    :keyword str authority: Authority of an Azure Active Directory endpoint, for example "login.microsoftonline.com",
        the authority for Azure Public Cloud (which is the default). :class:`~azure.identity.AzureAuthorityHosts`
        defines authorities for other clouds.
    :keyword password: A certificate password. Used only when **client_certificate** is provided. If this value
        is a unicode string, it will be encoded as UTF-8. If the certificate requires a different encoding, pass
        appropriately encoded bytes instead.
    :paramtype password: str or bytes
    :keyword List[str] additionally_allowed_tenants: Specifies tenants in addition to the specified "tenant_id"
        for which the credential may acquire tokens. Add the wildcard value "*" to allow the credential to
        acquire tokens for any tenant the application can access.

    .. admonition:: Example:

        .. literalinclude:: ../samples/credential_creation_code_snippets.py
            :start-after: [START create_on_behalf_of_credential_async]
            :end-before: [END create_on_behalf_of_credential_async]
            :language: python
            :dedent: 4
            :caption: Create an OnBehalfOfCredential.
    '''
    def __init__(self, tenant_id: str, client_id: str, *, client_certificate: bytes | None = None, client_secret: str | None = None, user_assertion: str, **kwargs: Any) -> None: ...
    async def __aenter__(self): ...
    async def close(self) -> None: ...
