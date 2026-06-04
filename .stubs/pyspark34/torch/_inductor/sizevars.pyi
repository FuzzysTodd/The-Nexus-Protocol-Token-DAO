import dataclasses
import sympy
from . import ir as ir
from .codegen.common import IndentedBuffer as IndentedBuffer
from .utils import VarRanges as VarRanges, sympy_subs as sympy_subs, sympy_symbol as sympy_symbol
from .virtualized import V as V
from _typeshed import Incomplete
from sympy import Expr as Expr
from torch.fx.experimental.symbolic_shapes import ShapeEnv as ShapeEnv
from typing import Dict, List, Tuple

log: Incomplete

@dataclasses.dataclass
class ZeroGuard:
    """
    An expression we should check equals zero.
    Guards are currently not checked.  Plan to add this later.
    """
    expr: Expr
    def __init__(self, expr) -> None: ...

@dataclasses.dataclass
class PositiveGuard:
    """
    An expression we should check for > 0
    Guards are currently not checked.  Plan to add this later.
    """
    expr: Expr
    def __init__(self, expr) -> None: ...

class SizeVarAllocator:
    shape_env: Incomplete
    var_to_val: Incomplete
    guards: Incomplete
    replacements: Incomplete
    precomputed_replacements: Incomplete
    inv_precomputed_replacements: Incomplete
    need_seed: bool
    stride_vars: Incomplete
    simplify_with_ranges: Incomplete
    declare: str
    ending: str
    as_strided: str
    def __init__(self, shape_env: Incomplete | None = None) -> None: ...
    def seed(self):
        """
        Seed is a special variable used to hold the rng seed for a graph.

        Note this is only used by the CPU backend, we put seeds in a
        1-element tensor for the CUDA backend.
        """
    def simplify(self, expr: Expr): ...
    def make_simplify_with_ranges_cache(self):
        """
        self._simplify_with_ranges() can be expensive, cache its results
        """
    def make_simplify_loops_cache(self):
        """
        self._simplify_with_ranges() can be expensive, cache its results
        """
    def guard_equals(self, left: Expr, right: Expr) -> Expr: ...
    def maybe_guard_equals(self, left: Expr, right: Expr) -> bool:
        """if left==right, guard on that fact and return true"""
    def maybe_guard_list_equals(self, left: List[Expr], right: List[Expr]) -> bool:
        """if left==right, guard on that fact and return true"""
    def maybe_guard_leq(self, left: Expr, right: Expr) -> bool: ...
    def maybe_guard_lt(self, left: Expr, right: Expr) -> bool: ...
    def guard_leq(self, left: Expr, right: Expr) -> None: ...
    def guard_lt(self, left: Expr, right: Expr) -> None: ...
    def guard_min(self, left: Expr, right: Expr) -> Expr:
        """return the smaller of left and right, and guard on that choice"""
    def guard_max(self, left: Expr, right: Expr) -> Expr:
        """return the larger of left and right, and guard on that choice"""
    def maybe_guard_multiple_of(self, numerator: Expr, denominator: Expr) -> bool:
        """if denominator divides numerator, return True and guard on that fact"""
    def guard_static_shape(self, left: Expr) -> int: ...
    def __getitem__(self, val: int) -> Expr: ...
    def size_hint(self, expr: Expr) -> int: ...
    def size_hints(self, exprs: List[Expr]) -> int: ...
    def make_stride_vars_cache(self): ...
    def offset_var(self, index: Expr, vars: List[sympy.Symbol]) -> Expr:
        """Extract offset part of an indexing expression"""
    def stride_hints(self, index: Expr, vars: List[sympy.Symbol]) -> List[int]: ...
    def stride_order(self, index: Expr, vars: List[sympy.Symbol]) -> List[int]: ...
    def lookup_precomputed_size(self, expr: Expr): ...
    def codegen(self, code: IndentedBuffer, graph_inputs: Dict[str, ir.Buffer]):
        """Assign all symbolic shapes to locals"""
    def codegen_precomputed_sizes(self, code: IndentedBuffer): ...
    def codegen_sizevar(self, x: Expr) -> str: ...
    def codegen_shape_tuple(self, shape: Tuple[Expr, ...]) -> str: ...
    def codegen_benchmark_shape_tuple(self, shape: Tuple[Expr, ...]) -> str: ...

def join_dimensions(expr: Expr) -> Expr: ...

class CppSizeVarAllocator(SizeVarAllocator):
    declare: str
    ending: str
    as_strided: str
    def __init__(self, shape_env: Incomplete | None = None) -> None: ...
    def codegen_shape_tuple(self, shape: Tuple[Expr, ...]) -> str: ...
    def codegen_benchmark_shape_tuple(self, shape: Tuple[Expr, ...]) -> str: ...

class SimplifyIndexing(V.WrapperHandler):
    """
    A wrapper around .virtualize.ops that uses var range information to
    simplify ir.ModularIndexing/ir.FloorDiv.
    """
    name: str
    def __init__(self, inner, var_ranges: VarRanges) -> None: ...
    def load(self, name: str, index: sympy.Expr): ...
    def store(self, name, index, value, mode: Incomplete | None = None): ...
    def reduction(self, name, dtype, src_dtype, reduction_type, index, value): ...
    def index_expr(self, index, dtype): ...
