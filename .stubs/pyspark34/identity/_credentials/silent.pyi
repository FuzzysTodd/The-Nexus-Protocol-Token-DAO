from .. import AuthenticationRecord as AuthenticationRecord, CredentialUnavailableError as CredentialUnavailableError
from .._internal import resolve_tenant as resolve_tenant, validate_tenant_id as validate_tenant_id, within_dac as within_dac
from .._internal.decorators import wrap_exceptions as wrap_exceptions
from .._internal.msal_client import MsalClient as MsalClient
from .._internal.shared_token_cache import NO_TOKEN as NO_TOKEN
from .._persistent_cache import TokenCachePersistenceOptions as TokenCachePersistenceOptions
from azure.core.credentials import AccessToken
from msal import TokenCache as TokenCache
from typing import Any

class SilentAuthenticationCredential:
    """Internal class for authenticating from the default shared cache given an AuthenticationRecord.

    :param authentication_record: an AuthenticationRecord from which to authenticate
    :type authentication_record: ~azure.identity.AuthenticationRecord
    :keyword str tenant_id: tenant ID of the application the credential is authenticating for. Defaults to the tenant
    """
    def __init__(self, authentication_record: AuthenticationRecord, *, tenant_id: str | None = None, **kwargs) -> None: ...
    def __enter__(self): ...
    def __exit__(self, *args) -> None: ...
    def get_token(self, *scopes: str, claims: str | None = None, tenant_id: str | None = None, **kwargs: Any) -> AccessToken: ...
