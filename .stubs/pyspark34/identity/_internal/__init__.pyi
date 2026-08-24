from .aad_client import AadClient as AadClient
from .aad_client_base import AadClientBase as AadClientBase
from .aadclient_certificate import AadClientCertificate as AadClientCertificate
from .auth_code_redirect_handler import AuthCodeRedirectServer as AuthCodeRedirectServer
from .decorators import wrap_exceptions as wrap_exceptions
from .interactive import InteractiveCredential as InteractiveCredential
from .utils import get_default_authority as get_default_authority, normalize_authority as normalize_authority, resolve_tenant as resolve_tenant, validate_scope as validate_scope, validate_tenant_id as validate_tenant_id, within_credential_chain as within_credential_chain, within_dac as within_dac

__all__ = ['_scopes_to_resource', 'AadClient', 'AadClientBase', 'AuthCodeRedirectServer', 'AadClientCertificate', 'get_default_authority', 'InteractiveCredential', 'normalize_authority', 'resolve_tenant', 'validate_scope', 'within_credential_chain', 'within_dac', 'wrap_exceptions', 'validate_tenant_id']

def _scopes_to_resource(*scopes) -> str:
    """Convert a AADv2 scope to an AADv1 resource.

    :param str scopes: scope to convert
    :return: the first scope, converted to an AADv1 resource
    :rtype: str
    :raises: ValueError if scopes is empty or contains more than one scope
    """
