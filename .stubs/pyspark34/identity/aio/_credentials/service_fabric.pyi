from .._internal.managed_identity_base import AsyncManagedIdentityBase as AsyncManagedIdentityBase
from .._internal.managed_identity_client import AsyncManagedIdentityClient as AsyncManagedIdentityClient
from typing import Any

class ServiceFabricCredential(AsyncManagedIdentityBase):
    def get_client(self, **kwargs: Any) -> AsyncManagedIdentityClient | None: ...
    def get_unavailable_message(self) -> str: ...
