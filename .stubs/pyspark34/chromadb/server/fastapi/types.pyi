from chromadb.api.types import CollectionMetadata as CollectionMetadata, Include as Include
from pydantic import BaseModel
from typing import Any, Dict, List

class AddEmbedding(BaseModel):
    embeddings: List[Any] | None
    metadatas: List[Dict[Any, Any] | None] | None
    documents: List[str | None] | None
    ids: List[str]

class UpdateEmbedding(BaseModel):
    embeddings: List[Any] | None
    metadatas: List[Dict[Any, Any] | None] | None
    documents: List[str | None] | None
    ids: List[str]

class QueryEmbedding(BaseModel):
    where: Dict[Any, Any] | None
    where_document: Dict[Any, Any] | None
    query_embeddings: List[Any]
    n_results: int
    include: Include

class GetEmbedding(BaseModel):
    ids: List[str] | None
    where: Dict[Any, Any] | None
    where_document: Dict[Any, Any] | None
    sort: str | None
    limit: int | None
    offset: int | None
    include: Include

class DeleteEmbedding(BaseModel):
    ids: List[str] | None
    where: Dict[Any, Any] | None
    where_document: Dict[Any, Any] | None

class CreateCollection(BaseModel):
    name: str
    metadata: CollectionMetadata | None
    get_or_create: bool

class UpdateCollection(BaseModel):
    new_name: str | None
    new_metadata: CollectionMetadata | None
