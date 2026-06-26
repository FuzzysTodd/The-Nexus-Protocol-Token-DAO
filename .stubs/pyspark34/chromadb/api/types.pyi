from chromadb.types import LiteralValue, LogicalOperator, Metadata as Metadata, OperatorExpression, UpdateMetadata, Vector, Where as Where, WhereDocument as WhereDocument, WhereDocumentOperator, WhereOperator
from typing import Any, Dict, List, TypeVar
from typing_extensions import Protocol, TypedDict

__all__ = ['Metadata', 'Where', 'WhereDocument', 'UpdateCollectionMetadata']

ID = str
IDs = List[ID]
Embedding = Vector
Embeddings = List[Embedding]
Metadatas = List[Metadata]
CollectionMetadata = Dict[str, Any]
UpdateCollectionMetadata = UpdateMetadata
Document = str
Documents = List[Document]
Parameter = TypeVar('Parameter', Embedding, Document, Metadata, ID)
T = TypeVar('T')
OneOrMany = T | List[T]
LiteralValue = LiteralValue
LogicalOperator = LogicalOperator
WhereOperator = WhereOperator
OperatorExpression = OperatorExpression
Where = Where
WhereDocumentOperator = WhereDocumentOperator

class GetResult(TypedDict):
    ids: List[ID]
    embeddings: List[Embedding] | None
    documents: List[Document] | None
    metadatas: List[Metadata] | None

class QueryResult(TypedDict):
    ids: List[IDs]
    embeddings: List[List[Embedding]] | None
    documents: List[List[Document]] | None
    metadatas: List[List[Metadata]] | None
    distances: List[List[float]] | None

class IndexMetadata(TypedDict):
    dimensionality: int
    curr_elements: int
    total_elements_added: int
    time_created: float

class EmbeddingFunction(Protocol):
    def __call__(self, texts: Documents) -> Embeddings: ...
