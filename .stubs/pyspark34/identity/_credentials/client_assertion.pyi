from .._internal import AadClient as AadClient
from .._internal.get_token_mixin import GetTokenMixin as GetTokenMixin
from azure.core.credentials import AccessToken as AccessToken
from typing import Any, Callable

class ClientAssertionCredential(GetTokenMixin):
    '''Authenticates a service principal with a JWT assertion.

    This credential is for advanced scenarios. :class:`~azure.identity.CertificateCredential` has a more
    convenient API for the most common assertion scenario, authenticating a service principal with a certificate.

    :param str tenant_id: ID of the principal\'s tenant. Also called its "directory" ID.
    :param str client_id: The principal\'s client ID
    :param func: A callable that returns a string assertion. The credential will call this every time it
        acquires a new token.
    :paramtype func: Callable[[], str]

    :keyword str authority: Authority of an Azure Active Directory endpoint, for example
        "login.microsoftonline.com", the authority for Azure Public Cloud (which is the default).
        :class:`~azure.identity.AzureAuthorityHosts` defines authorities for other clouds.
    :keyword List[str] additionally_allowed_tenants: Specifies tenants in addition to the specified "tenant_id"
        for which the credential may acquire tokens. Add the wildcard value "*" to allow the credential to
        acquire tokens for any tenant the application can access.

    .. admonition:: Example:

        .. literalinclude:: ../samples/credential_creation_code_snippets.py
            :start-after: [START create_client_assertion_credential]
            :end-before: [END create_client_assertion_credential]
            :language: python
            :dedent: 4
            :caption: Create a ClientAssertionCredential.
    '''
    def __init__(self, tenant_id: str, client_id: str, func: Callable[[], str], **kwargs: Any) -> None: ...
    def __enter__(self): ...
    def __exit__(self, *args) -> None: ...
    def close(self) -> None: ...
