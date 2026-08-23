from _typeshed import Incomplete
from enum import Enum
from typing import Dict, List, Mapping, Sequence
from typing_extensions import TypeVar, TypedDict
from uuid import UUID

Metadata = Mapping[str, str | int | float | bool]
UpdateMetadata = Mapping[str, int | float | str | bool | None]
NamespacedName = str

class ScalarEncoding(Enum):
    FLOAT32: str
    INT32: str

class SegmentScope(Enum):
    VECTOR: str
    METADATA: str

class Collection(TypedDict):
    id: UUID
    name: str
    topic: str
    metadata: Metadata | None
    dimension: int | None

class Segment(TypedDict):
    id: UUID
    type: NamespacedName
    scope: SegmentScope
    topic: str | None
    collection: UUID | None
    metadata: Metadata | None
SeqId = int

class Operation(Enum):
    ADD: str
    UPDATE: str
    UPSERT: str
    DELETE: str
Vector = Sequence[float] | Sequence[int]

class VectorEmbeddingRecord(TypedDict):
    id: str
    seq_id: SeqId
    embedding: Vector

class MetadataEmbeddingRecord(TypedDict):
    id: str
    seq_id: SeqId
    metadata: Metadata | None

class EmbeddingRecord(TypedDict):
    id: str
    seq_id: SeqId
    embedding: Vector | None
    encoding: ScalarEncoding | None
    metadata: UpdateMetadata | None
    operation: Operation

class SubmitEmbeddingRecord(TypedDict):
    id: str
    embedding: Vector | None
    encoding: ScalarEncoding | None
    metadata: UpdateMetadata | None
    operation: Operation

class VectorQuery(TypedDict):
    """A KNN/ANN query"""
    vectors: Sequence[Vector]
    k: int
    allowed_ids: Sequence[str] | None
    include_embeddings: bool
    options: Dict[str, str | int | float | bool] | None

class VectorQueryResult(TypedDict):
    """A KNN/ANN query result"""
    id: str
    seq_id: SeqId
    distance: float
    embedding: Vector | None
LiteralValue = str | int | float | bool
LogicalOperator: Incomplete
WhereOperator: Incomplete
InclusionExclusionOperator: Incomplete
OperatorExpression = Dict[WhereOperator | LogicalOperator, LiteralValue] | Dict[InclusionExclusionOperator, List[LiteralValue]]
Where: Incomplete
WhereDocumentOperator: Incomplete
WhereDocument: Incomplete

class Unspecified:
    """A sentinel value used to indicate that a value should not be updated"""
    def __new__(cls) -> Unspecified: ...
T = TypeVar('T')
OptionalArgument = T | Unspecified
