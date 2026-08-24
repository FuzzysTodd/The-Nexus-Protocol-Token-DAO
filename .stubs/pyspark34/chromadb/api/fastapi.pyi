import requests
from _typeshed import Incomplete
from chromadb.api import API as API
from chromadb.api.models.Collection import Collection as Collection
from chromadb.api.types import CollectionMetadata as CollectionMetadata, Documents as Documents, EmbeddingFunction as EmbeddingFunction, Embeddings as Embeddings, GetResult as GetResult, IDs as IDs, Include as Include, Metadatas as Metadatas, QueryResult as QueryResult, Where as Where, WhereDocument as WhereDocument, validate_batch as validate_batch
from chromadb.auth import ClientAuthProvider as ClientAuthProvider
from chromadb.auth.providers import RequestsClientAuthProtocolAdapter as RequestsClientAuthProtocolAdapter
from chromadb.auth.registry import resolve_provider as resolve_provider
from chromadb.config import Settings as Settings, System as System
from chromadb.telemetry import Telemetry as Telemetry
from typing import Sequence

logger: Incomplete

class FastAPI(API):
    @staticmethod
    def resolve_url(chroma_server_host: str, chroma_server_ssl_enabled: bool | None = False, default_api_path: str | None = '', chroma_server_http_port: int | None = 8000) -> str: ...
    def __init__(self, system: System) -> None: ...
    def heartbeat(self) -> int:
        """Returns the current server time in nanoseconds to check if the server is alive"""
    def list_collections(self) -> Sequence[Collection]:
        """Returns a list of all collections"""
    def create_collection(self, name: str, metadata: CollectionMetadata | None = None, embedding_function: EmbeddingFunction | None = ..., get_or_create: bool = False) -> Collection:
        """Creates a collection"""
    def get_collection(self, name: str, embedding_function: EmbeddingFunction | None = ...) -> Collection:
        """Returns a collection"""
    def get_or_create_collection(self, name: str, metadata: CollectionMetadata | None = None, embedding_function: EmbeddingFunction | None = ...) -> Collection: ...
    def delete_collection(self, name: str) -> None:
        """Deletes a collection"""
    def reset(self) -> bool:
        """Resets the database"""
    def get_version(self) -> str:
        """Returns the version of the server"""
    def get_settings(self) -> Settings:
        """Returns the settings of the client"""
    @property
    def max_batch_size(self) -> int: ...

def raise_chroma_error(resp: requests.Response) -> None:
    """Raises an error if the response is not ok, using a ChromaError if possible"""
