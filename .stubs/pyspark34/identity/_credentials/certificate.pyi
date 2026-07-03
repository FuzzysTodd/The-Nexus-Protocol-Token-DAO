from .._internal import validate_tenant_id as validate_tenant_id
from .._internal.client_credential_base import ClientCredentialBase as ClientCredentialBase
from typing import Any, Dict, NamedTuple

class CertificateCredential(ClientCredentialBase):
    '''Authenticates as a service principal using a certificate.

    The certificate must have an RSA private key, because this credential signs assertions using RS256. See
    `Azure Active Directory documentation
    <https://docs.microsoft.com/azure/active-directory/develop/active-directory-certificate-credentials#register-your-certificate-with-microsoft-identity-platform>`_
    for more information on configuring certificate authentication.

    :param str tenant_id: ID of the service principal\'s tenant. Also called its "directory" ID.
    :param str client_id: The service principal\'s client ID
    :param str certificate_path: Optional path to a certificate file in PEM or PKCS12 format, including the private
        key. If not provided, **certificate_data** is required.

    :keyword str authority: Authority of an Azure Active Directory endpoint, for example "login.microsoftonline.com",
        the authority for Azure Public Cloud (which is the default). :class:`~azure.identity.AzureAuthorityHosts`
        defines authorities for other clouds.
    :keyword bytes certificate_data: The bytes of a certificate in PEM or PKCS12 format, including the private key
    :keyword password: The certificate\'s password. If a unicode string, it will be encoded as UTF-8. If the certificate
        requires a different encoding, pass appropriately encoded bytes instead.
    :paramtype password: str or bytes
    :keyword bool send_certificate_chain: If True, the credential will send the public certificate chain in the x5c
        header of each token request\'s JWT. This is required for Subject Name/Issuer (SNI) authentication. Defaults to
        False.
    :keyword cache_persistence_options: Configuration for persistent token caching. If unspecified, the credential
        will cache tokens in memory.
    :paramtype cache_persistence_options: ~azure.identity.TokenCachePersistenceOptions
    :keyword bool disable_instance_discovery: Determines whether or not instance discovery is performed when attempting
        to authenticate. Setting this to true will completely disable both instance discovery and authority validation.
        This functionality is intended for use in scenarios where the metadata endpoint cannot be reached, such as in
        private clouds or Azure Stack. The process of instance discovery entails retrieving authority metadata from
        https://login.microsoft.com/ to validate the authority. By setting this to **True**, the validation of the
        authority is disabled. As a result, it is crucial to ensure that the configured authority host is valid and
        trustworthy.
    :keyword List[str] additionally_allowed_tenants: Specifies tenants in addition to the specified "tenant_id"
        for which the credential may acquire tokens. Add the wildcard value "*" to allow the credential to
        acquire tokens for any tenant the application can access.

    .. admonition:: Example:

        .. literalinclude:: ../samples/credential_creation_code_snippets.py
            :start-after: [START create_certificate_credential]
            :end-before: [END create_certificate_credential]
            :language: python
            :dedent: 4
            :caption: Create a CertificateCredential.
    '''
    def __init__(self, tenant_id: str, client_id: str, certificate_path: str | None = None, **kwargs: Any) -> None: ...

def extract_cert_chain(pem_bytes: bytes) -> bytes:
    """Extract a certificate chain from a PEM file's bytes, removing line breaks.

    :param bytes pem_bytes: The PEM file's bytes
    :return: The certificate chain
    :rtype: bytes
    """

class _Cert(NamedTuple):
    pem_bytes: bytes
    private_key: 'Any'
    fingerprint: bytes

def load_pem_certificate(certificate_data: bytes, password: bytes | None = None) -> _Cert: ...
def load_pkcs12_certificate(certificate_data: bytes, password: bytes | None = None) -> _Cert: ...
def get_client_credential(certificate_path: str | None = None, password: bytes | str | None = None, certificate_data: bytes | None = None, send_certificate_chain: bool = False, **_: Any) -> Dict:
    """Load a certificate from a filesystem path or bytes, return it as a dict suitable for msal.ClientApplication.

    :param str certificate_path: Path to a PEM or PKCS12 certificate file.
    :param bytes password: The certificate's password, if any.
    :param bytes certificate_data: The PEM or PKCS12 certificate's bytes.
    :param bool send_certificate_chain: Whether to send the certificate chain. Defaults to False.

    :return: The certificate as a dict
    :rtype: dict
    """
