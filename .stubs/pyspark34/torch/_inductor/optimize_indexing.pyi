import sympy
import torch
from .ir import FloorDiv as FloorDiv, InterpreterShim as InterpreterShim, LoopBody as LoopBody, ModularIndexing as ModularIndexing
from .utils import sympy_subs as sympy_subs
from .virtualized import V as V
from _typeshed import Incomplete
from collections.abc import Generator
from torch.utils._sympy.value_ranges import ValueRangeAnalysis as ValueRangeAnalysis, ValueRanges as ValueRanges
from typing import Dict, Iterable

log: Incomplete

def dominated_nodes(initial_queue: torch.fx.Node | Iterable[torch.fx.Node], skip_filter: Incomplete | None = None):
    """Returns the set of nodes whose values depend on those within initial_queue"""
def val_expressable_in_32_bits(val): ...
def range_expressable_in_32_bits(range): ...

class OptimizeIndexing:
    """
    Performs Value Range Analysis on LoopBody's fx graph to reduce precision of
    intermediaries from int64 to int32. This is an important optimization for indexing
    kernels such as Upsample and Interpolate.
    """
    loop_body: Incomplete
    indices_range: Incomplete
    indexing_exprs: Incomplete
    replacement_vals: Incomplete
    interp_env: Incomplete
    submodules: Incomplete
    index_indirect_dependecies: Incomplete
    all_graphs: Incomplete
    tensor_values_set: Incomplete
    def __init__(self, loop_body: LoopBody, indices_ranges: Dict[sympy.Symbol, int], indexing_exprs: Dict[str, sympy.Expr]) -> None: ...
    def run(self) -> None:
        """Compute Value Ranges and try reduce precision of 'to_dtype' nodes to int32 where possible"""
    def try_to_reduce_precision(self, node): ...
    @property
    def all_nodes(self) -> Generator[Incomplete, None, None]: ...
    def swap_submodules(self, submodules): ...
    def masked_subblock(self, subblock, env, mask, value): ...
    def set_indirect(self, var, new_var): ...
    def replace_indirect(self, old, new) -> None:
        """Swap in a variable used in indirect indexing"""
    def get_index(self, name): ...

def indexing_dtype_strength_reduction(loop_body: LoopBody):
    """
    Performs Value Range Analysis on LoopBody's fx graph to reduce precision of
    intermediaries from int64 to int32
    """
