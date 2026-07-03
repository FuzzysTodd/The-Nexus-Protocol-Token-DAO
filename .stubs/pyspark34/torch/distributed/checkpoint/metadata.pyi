import torch
from dataclasses import dataclass
from torch.distributed._shard.sharded_tensor.metadata import TensorProperties
from typing import Any, Dict, List, Sequence

__all__ = ['ChunkStorageMetadata', 'TensorStorageMetadata', 'BytesStorageMetadata', 'Metadata', 'MetadataIndex']

@dataclass
class ChunkStorageMetadata:
    """
    Each chunk is expected to have the same properties of the TensorStorageMetadata that includes it.
    """
    offsets: torch.Size
    sizes: torch.Size
    def __init__(self, offsets, sizes) -> None: ...

@dataclass
class TensorStorageMetadata:
    properties: TensorProperties
    size: torch.Size
    chunks: List[ChunkStorageMetadata]
    def __init__(self, properties, size, chunks) -> None: ...

@dataclass
class BytesStorageMetadata: ...
STORAGE_TYPES = TensorStorageMetadata | BytesStorageMetadata
STATE_DICT_TYPE = Dict[str, Any]

@dataclass
class Metadata:
    state_dict_metadata: Dict[str, STORAGE_TYPES]
    planner_data: Any = ...
    storage_data: Any = ...
    def __init__(self, state_dict_metadata, planner_data, storage_data) -> None: ...

@dataclass(frozen=True)
class MetadataIndex:
    """
    This class represents a lookup key for items in a state dict or Metadata.
    """
    fqn: str
    offset: torch.Size | None = ...
    index: int | None = ...
    def __init__(self, fqn: str, offset: Sequence[int] | None = None, index: int | None = None) -> None: ...
