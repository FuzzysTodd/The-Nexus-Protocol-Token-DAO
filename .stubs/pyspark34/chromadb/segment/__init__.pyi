import abc
from abc import abstractmethod
from chromadb.config import Component as Component, System as System
from chromadb.types import Collection as Collection, Metadata as Metadata, MetadataEmbeddingRecord as MetadataEmbeddingRecord, Operation as Operation, Segment as Segment, SeqId as SeqId, VectorEmbeddingRecord as VectorEmbeddingRecord, VectorQuery as VectorQuery, VectorQueryResult as VectorQueryResult, Where as Where, WhereDocument as WhereDocument
from typing import Sequence, Type, TypeVar
from uuid import UUID

class SegmentImplementation(Component, metaclass=abc.ABCMeta):
    @abstractmethod
    def __init__(self, sytstem: System, segment: Segment): ...
    @abstractmethod
    def count(self) -> int:
        """Get the number of embeddings in this segment"""
    @abstractmethod
    def max_seqid(self) -> SeqId:
        """Get the maximum SeqID currently indexed by this segment"""
    @staticmethod
    def propagate_collection_metadata(metadata: Metadata) -> Metadata | None:
        """Given an arbitrary metadata map (e.g, from a collection), validate it and
        return metadata (if any) that is applicable and should be applied to the
        segment. Validation errors will be reported to the user."""
    @abstractmethod
    def delete(self) -> None:
        """Delete the segment and all its data"""
S = TypeVar('S', bound=SegmentImplementation)

class MetadataReader(SegmentImplementation, metaclass=abc.ABCMeta):
    """Embedding Metadata segment interface"""
    @abstractmethod
    def get_metadata(self, where: Where | None = None, where_document: WhereDocument | None = None, ids: Sequence[str] | None = None, limit: int | None = None, offset: int | None = None) -> Sequence[MetadataEmbeddingRecord]:
        """Query for embedding metadata."""

class VectorReader(SegmentImplementation, metaclass=abc.ABCMeta):
    """Embedding Vector segment interface"""
    @abstractmethod
    def get_vectors(self, ids: Sequence[str] | None = None) -> Sequence[VectorEmbeddingRecord]:
        """Get embeddings from the segment. If no IDs are provided, all embeddings are
        returned."""
    @abstractmethod
    def query_vectors(self, query: VectorQuery) -> Sequence[Sequence[VectorQueryResult]]:
        """Given a vector query, return the top-k nearest neighbors for vector in the
        query."""

class SegmentManager(Component, metaclass=abc.ABCMeta):
    """Interface for a pluggable strategy for creating, retrieving and instantiating
    segments as required"""
    @abstractmethod
    def create_segments(self, collection: Collection) -> Sequence[Segment]:
        """Return the segments required for a new collection. Returns only segment data,
        does not persist to the SysDB"""
    @abstractmethod
    def delete_segments(self, collection_id: UUID) -> Sequence[UUID]:
        """Delete any local state for all the segments associated with a collection, and
        returns a sequence of their IDs. Does not update the SysDB."""
    @abstractmethod
    def get_segment(self, collection_id: UUID, type: Type[S]) -> S:
        """Return the segment that should be used for servicing queries to a collection.
        Implementations should cache appropriately; clients are intended to call this
        method repeatedly rather than storing the result (thereby giving this
        implementation full control over which segment impls are in or out of memory at
        a given time.)"""
    @abstractmethod
    def hint_use_collection(self, collection_id: UUID, hint_type: Operation) -> None:
        """Signal to the segment manager that a collection is about to be used, so that
        it can preload segments as needed. This is only a hint, and implementations are
        free to ignore it."""
