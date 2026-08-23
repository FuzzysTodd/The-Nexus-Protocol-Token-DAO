from ..config import MlflowModelServingConfig as MlflowModelServingConfig, RouteConfig as RouteConfig
from ..constants import MLFLOW_SERVING_RESPONSE_KEY as MLFLOW_SERVING_RESPONSE_KEY
from ..schemas import chat as chat, completions as completions, embeddings as embeddings
from .base import BaseProvider as BaseProvider
from .utils import send_request as send_request
from _typeshed import Incomplete
from pydantic import BaseModel, StrictStr as StrictStr
from typing import List

class ServingTextResponse(BaseModel):
    predictions: List[StrictStr]
    def extract_candidates(cls, predictions): ...

class EmbeddingsResponse(BaseModel):
    predictions: List[List[float]]
    def validate_predictions(cls, predictions): ...

class MlflowModelServingProvider(BaseProvider):
    mlflow_config: Incomplete
    headers: Incomplete
    def __init__(self, config: RouteConfig) -> None: ...
    async def completions(self, payload: completions.RequestPayload) -> completions.ResponsePayload: ...
    async def chat(self, payload: chat.RequestPayload) -> chat.ResponsePayload: ...
    async def embeddings(self, payload: embeddings.RequestPayload) -> embeddings.ResponsePayload: ...
