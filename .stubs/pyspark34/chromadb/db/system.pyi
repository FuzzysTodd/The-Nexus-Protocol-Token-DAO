import abc
from abc import abstractmethod
from chromadb.config import Component as Component
from chromadb.types import Collection as Collection, OptionalArgument as OptionalArgument, Segment as Segment, SegmentScope as SegmentScope, Unspecified as Unspecified, UpdateMetadata as UpdateMetadata
from typing import Sequence
from uuid import UUID

class SysDB(Component, metaclass=abc.ABCMeta):
    """Data interface for Chroma's System database"""
    @abstractmethod
    def create_segment(self, segment: Segment) -> None:
        """Create a new segment in the System database. Raises DuplicateError if the ID
        already exists."""
    @abstractmethod
    def delete_segment(self, id: UUID) -> None:
        """Create a new segment in the System database."""
    @abstractmethod
    def get_segments(self, id: UUID | None = None, type: str | None = None, scope: SegmentScope | None = None, topic: str | None = None, collection: UUID | None = None) -> Sequence[Segment]:
        """Find segments by id, type, scope, topic or collection."""
    @abstractmethod
    def update_segment(self, id: UUID, topic: OptionalArgument[str | None] = ..., collection: OptionalArgument[UUID | None] = ..., metadata: OptionalArgument[UpdateMetadata | None] = ...) -> None:
        """Update a segment. Unspecified fields will be left unchanged. For the
        metadata, keys with None values will be removed and keys not present in the
        UpdateMetadata dict will be left unchanged."""
    @abstractmethod
    def create_collection(self, collection: Collection) -> None:
        """Create a new topic"""
    @abstractmethod
    def delete_collection(self, id: UUID) -> None:
        """Delete a topic and all associated segments from the SysDB"""
    @abstractmethod
    def get_collections(self, id: UUID | None = None, topic: str | None = None, name: str | None = None) -> Sequence[Collection]:
        """Find collections by id, topic or name"""
    @abstractmethod
    def update_collection(self, id: UUID, topic: OptionalArgument[str] = ..., name: OptionalArgument[str] = ..., dimension: OptionalArgument[int | None] = ..., metadata: OptionalArgument[UpdateMetadata | None] = ...) -> None:
        """Update a collection. Unspecified fields will be left unchanged. For metadata,
        keys with None values will be removed and keys not present in the UpdateMetadata
        dict will be left unchanged."""
