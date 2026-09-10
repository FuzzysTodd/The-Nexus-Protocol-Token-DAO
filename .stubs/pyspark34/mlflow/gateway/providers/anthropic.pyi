from ..config import AnthropicConfig as AnthropicConfig, RouteConfig as RouteConfig
from ..constants import MLFLOW_AI_GATEWAY_ANTHROPIC_DEFAULT_MAX_TOKENS as MLFLOW_AI_GATEWAY_ANTHROPIC_DEFAULT_MAX_TOKENS, MLFLOW_AI_GATEWAY_ANTHROPIC_MAXIMUM_MAX_TOKENS as MLFLOW_AI_GATEWAY_ANTHROPIC_MAXIMUM_MAX_TOKENS
from ..schemas import chat as chat, completions as completions, embeddings as embeddings
from .base import BaseProvider as BaseProvider
from .utils import rename_payload_keys as rename_payload_keys, send_request as send_request
from _typeshed import Incomplete

class AnthropicProvider(BaseProvider):
    anthropic_config: Incomplete
    headers: Incomplete
    base_url: str
    def __init__(self, config: RouteConfig) -> None: ...
    async def completions(self, payload: completions.RequestPayload) -> completions.ResponsePayload: ...
    async def chat(self, payload: chat.RequestPayload) -> None: ...
    async def embeddings(self, payload: embeddings.RequestPayload) -> None: ...
