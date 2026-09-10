from ..config import OpenAIAPIType as OpenAIAPIType, OpenAIConfig as OpenAIConfig, RouteConfig as RouteConfig
from ..schemas import chat as chat, completions as completions, embeddings as embeddings
from .base import BaseProvider as BaseProvider
from .utils import rename_payload_keys as rename_payload_keys, send_request as send_request
from _typeshed import Incomplete
from mlflow.exceptions import MlflowException as MlflowException
from mlflow.utils.uri import append_to_uri_path as append_to_uri_path, append_to_uri_query_params as append_to_uri_query_params

class OpenAIProvider(BaseProvider):
    openai_config: Incomplete
    def __init__(self, config: RouteConfig) -> None: ...
    async def chat(self, payload: chat.RequestPayload) -> chat.ResponsePayload: ...
    async def completions(self, payload: completions.RequestPayload) -> completions.ResponsePayload: ...
    async def embeddings(self, payload: embeddings.RequestPayload) -> embeddings.ResponsePayload: ...
