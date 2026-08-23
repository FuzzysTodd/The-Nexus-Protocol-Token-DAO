from .._constants import EnvironmentVariables as EnvironmentVariables, KnownAuthorities as KnownAuthorities
from _typeshed import Incomplete
from typing import List

within_credential_chain: Incomplete
within_dac: Incomplete
VALID_TENANT_ID_CHARACTERS: Incomplete
VALID_SCOPE_CHARACTERS: Incomplete

def normalize_authority(authority: str) -> str:
    """Ensure authority uses https, strip trailing spaces and /.

    :param str authority: authority to normalize
    :return: normalized authority
    :rtype: str
    :raises: ValueError if authority is not a valid https URL
    """
def get_default_authority() -> str: ...
def validate_scope(scope: str) -> None:
    """Raise ValueError if scope is empty or contains a character invalid for a scope

    :param str scope: scope to validate
    :raises: ValueError if scope is empty or contains a character invalid for a scope.
    """
def validate_tenant_id(tenant_id: str) -> None:
    """Raise ValueError if tenant_id is empty or contains a character invalid for a tenant ID.

    :param str tenant_id: tenant ID to validate
    :raises: ValueError if tenant_id is empty or contains a character invalid for a tenant ID.
    """
def resolve_tenant(default_tenant: str, tenant_id: str | None = None, *, additionally_allowed_tenants: List[str] = [], **_) -> str:
    """Returns the correct tenant for a token request given a credential's configuration.

    :param str default_tenant: The tenant ID configured on the credential.
    :param str tenant_id: The tenant ID requested by the user.
    :keyword list[str] additionally_allowed_tenants: The list of additionally allowed tenants.
    :return: The tenant ID to use for the token request.
    :rtype: str
    :raises: ~azure.core.exceptions.ClientAuthenticationError
    """
