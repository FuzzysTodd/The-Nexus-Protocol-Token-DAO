from _typeshed import Incomplete
from fastapi import FastAPI, Request as Request
from mlflow.exceptions import MlflowException as MlflowException
from mlflow.gateway.config import GatewayConfig as GatewayConfig, Route as Route, RouteConfig as RouteConfig, RouteType as RouteType
from mlflow.gateway.constants import MLFLOW_GATEWAY_CRUD_ROUTE_BASE as MLFLOW_GATEWAY_CRUD_ROUTE_BASE, MLFLOW_GATEWAY_HEALTH_ENDPOINT as MLFLOW_GATEWAY_HEALTH_ENDPOINT, MLFLOW_GATEWAY_ROUTE_BASE as MLFLOW_GATEWAY_ROUTE_BASE, MLFLOW_GATEWAY_SEARCH_ROUTES_PAGE_SIZE as MLFLOW_GATEWAY_SEARCH_ROUTES_PAGE_SIZE, MLFLOW_QUERY_SUFFIX as MLFLOW_QUERY_SUFFIX
from mlflow.gateway.providers import get_provider as get_provider
from mlflow.gateway.schemas import chat as chat, completions as completions, embeddings as embeddings
from mlflow.gateway.utils import SearchRoutesToken as SearchRoutesToken
from mlflow.version import VERSION as VERSION
from pathlib import Path
from pydantic import BaseModel
from typing import Any, List

MLFLOW_GATEWAY_CONFIG: str

class GatewayAPI(FastAPI):
    dynamic_routes: Incomplete
    def __init__(self, config: GatewayConfig, *args: Any, **kwargs: Any) -> None: ...
    def set_dynamic_routes(self, config: GatewayConfig) -> None: ...
    def get_dynamic_route(self, route_name: str) -> Route | None: ...

class HealthResponse(BaseModel):
    status: str

class SearchRoutesResponse(BaseModel):
    routes: List[Route]
    next_page_token: str | None
    class Config:
        schema_extra: Incomplete

def create_app_from_config(config: GatewayConfig) -> GatewayAPI:
    """
    Create the GatewayAPI app from the gateway configuration.
    """
def create_app_from_path(config_path: str | Path) -> GatewayAPI:
    """
    Load the path and generate the GatewayAPI app instance.
    """
def create_app_from_env() -> GatewayAPI:
    """
    Load the path from the environment variable and generate the GatewayAPI app instance.
    """
