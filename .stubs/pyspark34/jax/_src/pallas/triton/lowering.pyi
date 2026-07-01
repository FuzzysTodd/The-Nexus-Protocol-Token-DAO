import dataclasses
import functools
import jax
import triton.language as tl
from _typeshed import Incomplete
from jax import lax as lax, tree_util as tree_util
from jax._src import ad_checkpoint as ad_checkpoint, ad_util as ad_util, api_util as api_util, core as jax_core, pjit as pjit, state as state, util as util
from jax._src.lax.control_flow import for_loop as for_loop
from jax._src.lib import hlo_helpers as hlo_helpers, version as version
from jax._src.lib.mlir import ir as ir
from jax._src.pallas import indexing as indexing, primitives as primitives
from jax._src.pallas.pallas_call import pallas_call_p as pallas_call_p
from jax._src.state import AbstractRef as AbstractRef, discharge as discharge
from jax._src.util import merge_lists as merge_lists, partition_list as partition_list, split_list as split_list, weakref_lru_cache as weakref_lru_cache
from jax.interpreters import mlir as mlir
from triton._C.libtriton.triton import ir as tl_ir
from typing import Any, Dict, Sequence, Tuple

map: Incomplete
unsafe_map: Incomplete
zip: Incomplete
unsafe_zip: Incomplete
partial = functools.partial
Grid = Tuple[int, ...]
NDIndexer: Incomplete
GridMapping: Incomplete
BlockMapping: Incomplete

@dataclasses.dataclass
class TritonModuleContext:
    name: str
    ir_context: tl_ir.context
    builder: tl_ir.builder
    module: tl_ir.module
    grid_mapping: GridMapping
    program_ids: Sequence[tl.tensor]
    def __init__(self, name, ir_context, builder, module, grid_mapping, program_ids) -> None: ...

@dataclasses.dataclass
class BlockInfo:
    full_shape_dtype: jax.ShapeDtypeStruct
    start_indices: Sequence[Any]
    block_shape: Tuple[int, ...]
    def __init__(self, full_shape_dtype, start_indices, block_shape) -> None: ...

@dataclasses.dataclass
class TritonLoweringRuleContext:
    context: TritonModuleContext
    avals_in: Any
    avals_out: Any
    block_infos: Sequence[BlockInfo | None]
    builder = ...
    def __post_init__(self) -> None: ...
    replace = dataclasses.replace
    def __init__(self, context, avals_in, avals_out, block_infos) -> None: ...

@dataclasses.dataclass
class TritonLoweringResult:
    """Keeps pybind11 objects alive."""
    ir_context: tl_ir.context
    module: tl_ir.module
    builder: tl_ir.builder
    grid: Tuple[int, ...]
    def __init__(self, ir_context, module, builder, grid) -> None: ...

@dataclasses.dataclass
class TritonCompilationResult:
    kernel_name: str
    ttir: str
    ptx: str
    shared_mem_bytes: int
    compute_capability: int
    lowering_result: TritonLoweringResult
    def __init__(self, kernel_name, ttir, ptx, shared_mem_bytes, compute_capability, lowering_result) -> None: ...

class TritonLoweringException(Exception): ...

triton_lowering_rules: Incomplete

def lower_jaxpr_to_triton_module(jaxpr: jax_core.Jaxpr, in_shapes, grid_mapping: GridMapping, name: str) -> tl_ir.module: ...
def lower_jaxpr_to_triton_ir(ctx: TritonModuleContext, jaxpr: jax_core.Jaxpr, block_infos: Sequence[BlockInfo | None] | None, *args) -> Sequence[Any]: ...
def max_lowering_rule(ctx: TritonLoweringRuleContext, a, b): ...
def ge_lowering_rule(ctx: TritonLoweringRuleContext, a, b): ...
def eq_lowering_rule(ctx: TritonLoweringRuleContext, a, b): ...
def ne_lowering_rule(ctx: TritonLoweringRuleContext, a, b): ...
def bitwise_and_lowering_rule(ctx: TritonLoweringRuleContext, a, b): ...
def bitwise_or_lowering_rule(ctx: TritonLoweringRuleContext, a, b): ...
def select_n_lowering_rule(ctx: TritonLoweringRuleContext, pred, a, b): ...
def compile_jaxpr(jaxpr: jax_core.Jaxpr, in_shapes, grid_mapping: GridMapping, name: str, num_warps: int, num_stages: int, debug: bool) -> TritonCompilationResult: ...
def pallas_call_lowering(ctx: mlir.LoweringRuleContext, *in_nodes, jaxpr: jax_core.Jaxpr, name: str, in_shapes: Tuple[jax.ShapeDtypeStruct, ...], out_shapes: Tuple[jax.ShapeDtypeStruct, ...], which_linear: Tuple[bool, ...], interpret: bool, debug: bool, input_output_aliases: Tuple[Tuple[int, int], ...], grid_mapping: GridMapping, triton_params: Dict[str, Any] | None = None, **compiler_params: Any): ...
