from .._constants import EnvironmentVariables as EnvironmentVariables
from .._internal.managed_identity_base import ManagedIdentityBase as ManagedIdentityBase
from .._internal.managed_identity_client import ManagedIdentityClient as ManagedIdentityClient
from typing import Any

class AppServiceCredential(ManagedIdentityBase):
    def get_client(self, **kwargs: Any) -> ManagedIdentityClient | None: ...
    def get_unavailable_message(self) -> str: ...
