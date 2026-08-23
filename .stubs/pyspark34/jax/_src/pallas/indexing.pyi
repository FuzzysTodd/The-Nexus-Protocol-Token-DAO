import dataclasses
import jax
from _typeshed import Incomplete
from jax import tree_util as tree_util
from jax._src.interpreters import mlir as mlir
from jax._src.util import merge_lists as merge_lists, partition_list as partition_list
from typing import Any, Tuple

broadcast_to_p: Incomplete

def broadcast_to(a: jax.Array, shape: Tuple[int, ...]) -> jax.Array: ...

@dataclasses.dataclass
class Slice:
    """Represents a slice with a dynamic start index and a fixed size."""
    start: Any
    size: int
    def tree_flatten(self): ...
    @classmethod
    def tree_unflatten(cls, data, xs): ...
    @classmethod
    def from_slice(cls, slc: slice, size: int) -> Slice: ...
    def __init__(self, start, size) -> None: ...

def dslice(start: int | jax.Array | None, size: int | None = None) -> slice | Slice:
    """Constructs a `Slice` from a start and a size."""
ds = dslice

@dataclasses.dataclass
class NDIndexer:
    indices: Tuple[int | Slice | jax.Array, ...]
    shape: Tuple[int, ...]
    int_indexer_shape: Tuple[int, ...]
    def __post_init__(self) -> None: ...
    def tree_flatten(self): ...
    @classmethod
    def tree_unflatten(cls, data, flat_idx): ...
    @classmethod
    def from_indices_shape(cls, indices, shape) -> NDIndexer: ...
    def get_indexer_shape(self) -> Tuple[int, ...]: ...
    def __init__(self, indices, shape, int_indexer_shape) -> None: ...
