from ..._internal.managed_identity_client import ManagedIdentityClientBase as ManagedIdentityClientBase
from ..._internal.pipeline import build_async_pipeline as build_async_pipeline
from .._internal import AsyncContextManager as AsyncContextManager
from azure.core.credentials import AccessToken as AccessToken
from azure.core.pipeline import AsyncPipeline as AsyncPipeline

class AsyncManagedIdentityClient(AsyncContextManager, ManagedIdentityClientBase):
    async def __aenter__(self): ...
    async def close(self) -> None: ...
    async def request_token(self, *scopes: str, **kwargs) -> AccessToken: ...
