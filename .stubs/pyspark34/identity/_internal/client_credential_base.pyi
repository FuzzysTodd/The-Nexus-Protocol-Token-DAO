from . import wrap_exceptions as wrap_exceptions
from .get_token_mixin import GetTokenMixin as GetTokenMixin
from .msal_credentials import MsalCredential as MsalCredential

class ClientCredentialBase(MsalCredential, GetTokenMixin):
    """Base class for credentials authenticating a service principal with a certificate or secret"""
