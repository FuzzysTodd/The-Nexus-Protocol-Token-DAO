import dataclasses
import functools
from _typeshed import Incomplete
from jax import core as jax_core, lax as lax, tree_util as tree_util
from jax._src import custom_derivatives as custom_derivatives, debugging as debugging, mesh as mesh_lib, pjit as pjit, source_info_util as source_info_util, state as state
from jax._src.interpreters import mlir as mlir
from jax._src.lax.control_flow import for_loop as for_loop
from jax._src.lib.mlir import ir as ir
from jax._src.lib.mlir.dialects import arith as arith, func as func, math as math, memref as memref, scf as scf, vector as vector
from jax._src.pallas import core as core, indexing as indexing, primitives as primitives
from jax._src.util import safe_map as safe_map, safe_zip as safe_zip, split_list as split_list, unzip2 as unzip2
from jax.experimental.mosaic.dialects import tpu as tpu
from typing import Any, Callable, Sequence

NDIndexer: Incomplete
TPUMemorySpace: Incomplete
VMEM: Incomplete
SMEM: Incomplete
partial = functools.partial
map: Incomplete
unsafe_map: Incomplete
zip: Incomplete
unsafe_zip: Incomplete

@dataclasses.dataclass
class MeshContext:
    logical_to_mesh: ir.Value
    axis_names: tuple[str, ...]
    mesh_strides: tuple[int, ...]
    def __init__(self, logical_to_mesh, axis_names, mesh_strides) -> None: ...

@dataclasses.dataclass
class LoweringContext:
    ir_context: ir.Context
    grid_mapping: core.GridMapping | None
    grid_indices: Sequence[ir.Value] | None
    block_shapes: list[tuple[int | core.Mapped, ...]]
    name_stack: source_info_util.NameStack
    mesh_context: MeshContext | None
    replace = dataclasses.replace
    def __init__(self, ir_context, grid_mapping, grid_indices, block_shapes, name_stack, mesh_context) -> None: ...

@dataclasses.dataclass
class LoweringRuleContext:
    lowering_context: LoweringContext
    avals_in: Sequence[jax_core.AbstractValue]
    avals_out: Sequence[jax_core.AbstractValue]
    block_shapes: list[tuple[int | core.Mapped, ...]] | None
    replace = dataclasses.replace
    def __init__(self, lowering_context, avals_in, avals_out, block_shapes) -> None: ...

def aval_to_ir_type(aval, shape: Incomplete | None = None, memory_space: TPUMemorySpace | None = None): ...
def ir_constant(x, mlir_type: Incomplete | None = None): ...

lowering_rules: Incomplete
skip_mlir_conversions: Incomplete

def lower_jaxpr_to_module(ctx: ir.Context, grid_mapping: core.GridMapping, jaxpr: jax_core.Jaxpr, dimension_semantics: tuple[str | None, ...] | None, mesh: mesh_lib.Mesh | None = None) -> ir.Module: ...
def lower_jaxpr_to_transform_func(ctx: ir.Context, jaxpr: jax_core.Jaxpr, memspaces: Sequence[Any], *, name: str) -> func.FuncOp: ...
def lower_fun(fun: Callable, *, multiple_results: bool) -> Callable: ...
def lower_jaxpr_to_func(ctx: ir.Context, jaxpr: jax_core.Jaxpr, *, grid_mapping: core.GridMapping | None, name: str, mesh_info: Any) -> func.FuncOp: ...

class LoweringException(Exception): ...

def jaxpr_subcomp(ctx: LoweringContext, jaxpr: jax_core.Jaxpr, *args: ir.Value) -> Sequence[ir.Value]: ...
