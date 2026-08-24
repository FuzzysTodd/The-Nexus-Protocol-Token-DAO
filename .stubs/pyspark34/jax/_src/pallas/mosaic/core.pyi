import dataclasses
import enum
import functools
import jax.numpy as jnp
from _typeshed import Incomplete
from collections.abc import Sequence
from jax._src import core as jax_core, state as state, tree_util as tree_util, util as util
from jax._src.pallas import core as pallas_core
from typing import Any

map: Incomplete
unsafe_map: Incomplete
zip: Incomplete
unsafe_zip: Incomplete
partial = functools.partial
Grid: Incomplete
BlockSpec: Incomplete
GridMapping: Incomplete
NoBlockSpec: Incomplete
no_block_spec: Incomplete
split_list: Incomplete

class TPUMemorySpace(enum.Enum):
    ANY: str
    VMEM: str
    SMEM: str
    CMEM: str
    def __call__(self, shape: tuple[int, ...], dtype: jnp.dtype): ...

class SemaphoreType(enum.Enum):
    REGULAR: str
    DMA: str
    BARRIER: str
    def get_aval(self) -> AbstractSemaphore: ...

class AbstractMemoryRef(state.AbstractRef):
    inner_aval: Incomplete
    memory_space: Incomplete
    def __init__(self, inner_aval: jax_core.AbstractValue, memory_space: TPUMemorySpace) -> None: ...
    def at_least_vspace(self): ...
    def __eq__(self, other): ...
    def __hash__(self): ...

@dataclasses.dataclass(frozen=True)
class AbstractSemaphore(jax_core.AbstractValue):
    sem_type: SemaphoreType
    def __init__(self, sem_type) -> None: ...

@dataclasses.dataclass(frozen=True)
class MemoryRef:
    """Like jax.ShapeDtypeStruct but with memory spaces."""
    shape: tuple[int, ...]
    dtype: jnp.dtype
    memory_space: TPUMemorySpace = ...
    def get_aval(self) -> AbstractMemoryRef: ...
    def __init__(self, shape, dtype, memory_space) -> None: ...

@dataclasses.dataclass(init=False, unsafe_hash=True)
class PrefetchScalarGridSpec(pallas_core.GridSpec):
    grid: Grid
    num_scalar_prefetch: int
    in_specs: tuple[BlockSpec | NoBlockSpec, ...]
    out_specs: tuple[BlockSpec | NoBlockSpec, ...]
    in_specs_tree: Any
    out_specs_tree: Any
    def __init__(self, num_scalar_prefetch: int, grid: Grid | None = None, in_specs: BlockSpec | Sequence[BlockSpec | NoBlockSpec] | NoBlockSpec = ..., out_specs: BlockSpec | Sequence[BlockSpec | NoBlockSpec] | NoBlockSpec = ...) -> None: ...
    def get_grid_mapping(self, in_avals, in_tree, out_avals, out_tree) -> tuple[tuple[jax_core.AbstractValue, ...], GridMapping]: ...
