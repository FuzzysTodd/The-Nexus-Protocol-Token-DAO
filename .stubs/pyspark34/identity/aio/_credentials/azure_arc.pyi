from ..._constants import EnvironmentVariables as EnvironmentVariables
from .._internal.managed_identity_base import AsyncManagedIdentityBase as AsyncManagedIdentityBase
from .._internal.managed_identity_client import AsyncManagedIdentityClient as AsyncManagedIdentityClient
from azure.core.pipeline import PipelineRequest as PipelineRequest, PipelineResponse as PipelineResponse
from azure.core.pipeline.policies import AsyncHTTPPolicy
from typing import Any

class AzureArcCredential(AsyncManagedIdentityBase):
    def get_client(self, **kwargs: Any) -> AsyncManagedIdentityClient | None: ...
    def get_unavailable_message(self) -> str: ...

class ArcChallengeAuthPolicy(AsyncHTTPPolicy):
    """Policy for handling Azure Arc's challenge authentication"""
    async def send(self, request: PipelineRequest) -> PipelineResponse: ...
