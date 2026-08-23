from _typeshed import Incomplete
from jax import api_util as api_util, lax as lax, tree_util as tree_util
from jax._src import ad_util as ad_util, state as state
from jax._src.util import merge_lists as merge_lists, partition_list as partition_list, safe_map as safe_map, safe_zip as safe_zip, split_list as split_list, tuple_insert as tuple_insert, weakref_lru_cache as weakref_lru_cache
from jax.interpreters import ad as ad, batching as batching, xla as xla
from typing import Any, Callable, Dict, Sequence

map: Incomplete
unsafe_map: Incomplete
zip: Incomplete
unsafe_zip: Incomplete
Grid: Incomplete
BlockSpec: Incomplete
GridSpec: Incomplete
BlockMapping: Incomplete
GridMapping: Incomplete
NoBlockSpec: Incomplete
no_block_spec: Incomplete
pallas_call_p: Incomplete

def pallas_call(f: Callable[..., None], out_shape: Any, *, grid_spec: GridSpec | None = None, debug: bool = False, grid: Grid | None = None, in_specs: Sequence[BlockSpec | NoBlockSpec] | NoBlockSpec = ..., out_specs: BlockSpec | NoBlockSpec | Sequence[BlockSpec | NoBlockSpec] = ..., input_output_aliases: Dict[int, int] = {}, interpret: bool = False, name: str | None = None, **compiler_params: Any): ...
