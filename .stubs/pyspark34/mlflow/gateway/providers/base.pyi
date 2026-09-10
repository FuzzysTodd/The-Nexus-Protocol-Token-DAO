from ..config import RouteConfig as RouteConfig
from ..schemas import chat as chat, completions as completions, embeddings as embeddings
from _typeshed import Incomplete
from abc import ABC
from typing import Tuple

class BaseProvider(ABC):
    """
    Base class for MLflow Gateway providers.
    """
    NAME: str
    SUPPORTED_ROUTE_TYPES: Tuple[str, ...]
    config: Incomplete
    def __init__(self, config: RouteConfig) -> None: ...
    async def chat(self, payload: chat.RequestPayload) -> chat.ResponsePayload: ...
    async def completions(self, payload: completions.RequestPayload) -> completions.ResponsePayload: ...
    async def embeddings(self, payload: embeddings.RequestPayload) -> embeddings.ResponsePayload: ...
    @staticmethod
    def check_for_model_field(payload) -> None: ...
