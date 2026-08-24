from _typeshed import Incomplete
from enum import Enum
from mlflow.exceptions import MlflowException as MlflowException
from mlflow.gateway.base_models import ConfigModel as ConfigModel, ResponseModel as ResponseModel
from mlflow.gateway.constants import MLFLOW_GATEWAY_ROUTE_BASE as MLFLOW_GATEWAY_ROUTE_BASE, MLFLOW_QUERY_SUFFIX as MLFLOW_QUERY_SUFFIX
from mlflow.gateway.utils import check_configuration_route_name_collisions as check_configuration_route_name_collisions, is_valid_endpoint_name as is_valid_endpoint_name
from typing import Any, Dict, List

class Provider(str, Enum):
    OPENAI: str
    ANTHROPIC: str
    COHERE: str
    MLFLOW_MODEL_SERVING: str
    DATABRICKS_MODEL_SERVING: str
    MOSAICLML: str
    @classmethod
    def values(cls): ...

class RouteType(str, Enum):
    LLM_V1_COMPLETIONS: str
    LLM_V1_CHAT: str
    LLM_V1_EMBEDDINGS: str

class CohereConfig(ConfigModel):
    cohere_api_key: str
    def validate_cohere_api_key(cls, value): ...

class OpenAIAPIType(str, Enum):
    OPENAI: str
    AZURE: str
    AZUREAD: str

class OpenAIConfig(ConfigModel):
    openai_api_key: str
    openai_api_type: OpenAIAPIType
    openai_api_base: str | None
    openai_api_version: str | None
    openai_deployment_name: str | None
    openai_organization: str | None
    def validate_openai_api_key(cls, value): ...
    def validate_field_compatibility(cls, config: Dict[str, Any]): ...

class AnthropicConfig(ConfigModel):
    anthropic_api_key: str
    def validate_anthropic_api_key(cls, value): ...

class MlflowModelServingConfig(ConfigModel):
    model_server_url: str

config_types: Incomplete

class ModelInfo(ResponseModel):
    name: str | None
    provider: Provider

class Model(ConfigModel):
    name: str | None
    provider: str | Provider
    config: CohereConfig | OpenAIConfig | AnthropicConfig | MlflowModelServingConfig | None
    def validate_provider(cls, value): ...
    def validate_config(cls, config, values): ...

class RouteConfig(ConfigModel):
    name: str
    route_type: RouteType
    model: Model
    def validate_endpoint_name(cls, route_name): ...
    def validate_model(cls, model): ...
    def validate_route_type(cls, value): ...
    def to_route(self) -> Route: ...

class Route(ResponseModel):
    name: str
    route_type: RouteType
    model: ModelInfo
    route_url: str
    class Config:
        schema_extra: Incomplete

class GatewayConfig(ConfigModel):
    routes: List[RouteConfig]
