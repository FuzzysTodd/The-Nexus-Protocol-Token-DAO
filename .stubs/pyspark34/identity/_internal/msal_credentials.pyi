from .._constants import EnvironmentVariables as EnvironmentVariables
from .msal_client import MsalClient as MsalClient
from .utils import get_default_authority as get_default_authority, normalize_authority as normalize_authority, resolve_tenant as resolve_tenant, validate_tenant_id as validate_tenant_id
from typing import Dict, List

class MsalCredential:
    """Base class for credentials wrapping MSAL applications.

    :param str client_id: the principal's client ID
    :param client_credential: client credential data for the application
    :type client_credential: dict
    """
    def __init__(self, client_id: str, client_credential: str | Dict | None = None, *, additionally_allowed_tenants: List[str] | None = None, authority: str | None = None, disable_instance_discovery: bool | None = None, tenant_id: str | None = None, **kwargs) -> None: ...
    def __enter__(self): ...
    def __exit__(self, *args) -> None: ...
    def close(self) -> None: ...
