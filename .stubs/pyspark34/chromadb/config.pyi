from _typeshed import Incomplete
from abc import ABC
from chromadb.is_thin_client import is_thin_client as is_thin_client
from overrides import EnforceOverrides
from pydantic.v1 import BaseSettings
from typing import Any, Dict, Iterable, List, Set, Type, TypeVar
from typing_extensions import Literal

in_pydantic_v2: bool
is_thin_client: bool
logger: Incomplete
LEGACY_ERROR: str

class Settings(BaseSettings):
    environment: str
    chroma_db_impl: str | None
    chroma_api_impl: str
    chroma_telemetry_impl: str
    chroma_sysdb_impl: str
    chroma_producer_impl: str
    chroma_consumer_impl: str
    chroma_segment_manager_impl: str
    tenant_id: str
    topic_namespace: str
    is_persistent: bool
    persist_directory: str
    chroma_server_host: str | None
    chroma_server_headers: Dict[str, str] | None
    chroma_server_http_port: str | None
    chroma_server_ssl_enabled: bool | None
    chroma_server_api_default_path: str | None
    chroma_server_grpc_port: str | None
    chroma_server_cors_allow_origins: List[str]
    pulsar_broker_url: str | None
    pulsar_admin_port: str | None
    pulsar_broker_port: str | None
    chroma_server_auth_provider: str | None
    def chroma_server_auth_provider_non_empty(cls, v: str) -> str | None: ...
    chroma_server_auth_configuration_provider: str | None
    chroma_server_auth_configuration_file: str | None
    chroma_server_auth_credentials_provider: str | None
    chroma_server_auth_credentials_file: str | None
    chroma_server_auth_credentials: str | None
    def chroma_server_auth_credentials_file_non_empty_file_exists(cls, v: str) -> str | None: ...
    chroma_client_auth_provider: str | None
    chroma_server_auth_ignore_paths: Dict[str, List[str]]
    chroma_client_auth_credentials_provider: str | None
    chroma_client_auth_protocol_adapter: str | None
    chroma_client_auth_credentials_file: str | None
    chroma_client_auth_credentials: str | None
    chroma_client_auth_token_transport_header: str | None
    chroma_server_auth_token_transport_header: str | None
    anonymized_telemetry: bool
    allow_reset: bool
    migrations: Literal['none', 'validate', 'apply']
    def require(self, key: str) -> Any:
        """Return the value of a required config key, or raise an exception if it is not
        set"""
    def __getitem__(self, key: str) -> Any: ...
    class Config:
        env_file: str
        env_file_encoding: str
T = TypeVar('T', bound='Component')

class Component(ABC, EnforceOverrides):
    def __init__(self, system: System) -> None: ...
    def require(self, type: Type[T]) -> T:
        """Get a Component instance of the given type, and register as a dependency of
        that instance."""
    def dependencies(self) -> Set['Component']:
        """Return the full set of components this component depends on."""
    def stop(self) -> None:
        """Idempotently stop this component's execution and free all associated
        resources."""
    def start(self) -> None:
        """Idempotently start this component's execution"""
    def reset_state(self) -> None:
        """Reset this component's state to its initial blank state. Only intended to be
        called from tests."""

class System(Component):
    settings: Settings
    def __init__(self, settings: Settings) -> None: ...
    def instance(self, type: Type[T]) -> T:
        """Return an instance of the component type specified. If the system is running,
        the component will be started as well."""
    def components(self) -> Iterable[Component]:
        """Return the full set of all components and their dependencies in dependency
        order."""
    def start(self) -> None: ...
    def stop(self) -> None: ...
    def reset_state(self) -> None:
        """Reset the state of this system and all constituents in reverse dependency order"""
C = TypeVar('C')

def get_class(fqn: str, type: Type[C]) -> Type[C]:
    """Given a fully qualifed class name, import the module and return the class"""
def get_fqn(cls) -> str:
    """Given a class, return its fully qualified name"""
