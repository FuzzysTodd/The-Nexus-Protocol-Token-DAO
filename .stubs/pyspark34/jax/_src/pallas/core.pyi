import dataclasses
import functools
from _typeshed import Incomplete
from collections.abc import Sequence
from jax._src import api_util as api_util, core as jax_core, state as state, tree_util as tree_util, util as util
from typing import Any, Callable, Iterator

partial = functools.partial
Grid = tuple[int, ...]
split_list: Incomplete
map: Incomplete
unsafe_map: Incomplete
zip: Incomplete
unsafe_zip: Incomplete

@dataclasses.dataclass
class GridEnv:
    axis_index: Any
    axis_size: int
    def __init__(self, axis_index, axis_size) -> None: ...

def grid_env(env: tuple[tuple[Any, int], ...]) -> Iterator[None]: ...
def current_grid_env() -> tuple[GridEnv, ...] | None: ...

class Mapped: ...

mapped: Incomplete

@dataclasses.dataclass(init=False, unsafe_hash=True)
class BlockSpec:
    index_map: Callable[..., Any] | None
    block_shape: tuple[int | None, ...] | None
    memory_space: Any
    def __init__(self, index_map: Callable[..., Any] | None = None, block_shape: tuple[int | None, ...] | None = None, memory_space: Any = None) -> None: ...
    def compute_index(self, *args): ...

@dataclasses.dataclass(frozen=True)
class BlockMapping:
    block_shape: tuple[Mapped | int, ...]
    index_map_jaxpr: jax_core.ClosedJaxpr
    memory_space: Any
    def compute_start_indices(self, loop_idx, *args): ...
    replace = dataclasses.replace
    def __init__(self, block_shape, index_map_jaxpr, memory_space) -> None: ...

@dataclasses.dataclass(frozen=True)
class GridMapping:
    grid: tuple[int, ...]
    block_mappings: tuple[BlockMapping | None, ...]
    mapped_dims: tuple[int, ...]
    num_index_operands: int
    replace = dataclasses.replace
    def __init__(self, grid, block_mappings, mapped_dims, num_index_operands) -> None: ...

class NoBlockSpec: ...

no_block_spec: Incomplete

@dataclasses.dataclass(init=False, unsafe_hash=True)
class GridSpec:
    grid: Grid
    in_specs: tuple[BlockSpec | NoBlockSpec, ...]
    out_specs: tuple[BlockSpec | NoBlockSpec, ...]
    in_specs_tree: Any
    out_specs_tree: Any
    def __init__(self, grid: Grid | None = None, in_specs: BlockSpec | Sequence[BlockSpec | NoBlockSpec] | NoBlockSpec = ..., out_specs: BlockSpec | Sequence[BlockSpec | NoBlockSpec] | NoBlockSpec = ...) -> None: ...
    def get_grid_mapping(self, in_avals, in_tree, out_avals, out_tree) -> tuple[tuple[jax_core.AbstractValue, ...], GridMapping]: ...
