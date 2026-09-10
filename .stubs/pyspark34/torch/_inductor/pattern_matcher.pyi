import dataclasses
import inspect
import torch
import torch.fx
from . import config as config, ir as ir
from .virtualized import V as V
from _typeshed import Incomplete
from torch._dynamo.utils import counters as counters
from torch.fx.immutable_collections import immutable_dict as immutable_dict, immutable_list as immutable_list
from typing import Any, Callable, List

log: Incomplete
aten: Incomplete
Constant = Any
NodeOrConstant = Constant | torch.fx.Node

class Match:
    """
    Represents a successfully matched pattern.
    """
    pattern: Incomplete
    args: Incomplete
    kwargs: Incomplete
    nodes: Incomplete
    targets: Incomplete
    def __init__(self, pattern, args: Incomplete | None = None, kwargs: Incomplete | None = None) -> None: ...
    def extend(self, other) -> None: ...
    def bundle(self): ...
    def erase_nodes(self, graph: torch.fx.Graph): ...

class FailedMatch(RuntimeError):
    def __bool__(self) -> bool: ...

class MatchContext:
    """
    State needed while running PatternExpr._match().
    """
    outputs: Incomplete
    pattern_to_node: Incomplete
    def __init__(self, outputs: List['PatternExpr']) -> None: ...
    def match(self, pattern, node):
        """wrapper to check reused nodes in patterns"""

class PatternExpr:
    """
    Base class for types of patterns
    """
    def match(self, node: torch.fx.Node) -> Match | FailedMatch: ...

class Arg(PatternExpr):
    """
    Capture an arg which will become an input to the handler.  Args are
    passed in depth first order.
    """

class KeywordArg(PatternExpr):
    """
    Capture a kwarg which will become an input to the handler.
    """
    name: Incomplete
    def __init__(self, name) -> None: ...

class CallFunction(PatternExpr):
    """
    Matches a call_function node in the FX graps: `fns[i](*args, **kwargs)`
    """
    fns: Incomplete
    fns_set: Incomplete
    args: Incomplete
    kwargs: Incomplete
    users: Incomplete
    flatten: Incomplete
    flat_args_kwargs: Incomplete
    def __init__(self, fns, *args, _users: int = 1, **kwargs) -> None: ...
    @staticmethod
    def simple_flatten(args, kwargs): ...
    @staticmethod
    def pytree_flatten(args, kwargs): ...

class ListOf(PatternExpr):
    """
    Matches a repeated pattern
    """
    pattern: Incomplete
    def __init__(self, pattern) -> None: ...

pass_patterns: Incomplete

@dataclasses.dataclass
class PatternEntry:
    pattern: PatternExpr
    extra_check: Callable[[Match], bool]
    def apply(self, match: Match, graph: torch.fx.Graph, node: torch.fx.Node): ...
    def register(self, pass_number, target) -> None: ...
    def __init__(self, pattern, extra_check) -> None: ...

@dataclasses.dataclass
class LoweringPatternEntry(PatternEntry):
    handler: Any
    def apply(self, match: Match, graph: torch.fx.Graph, node: torch.fx.Node): ...
    def __init__(self, pattern, extra_check, handler) -> None: ...

@dataclasses.dataclass
class ReplacementPatternEntry(PatternEntry):
    replacement_graph: torch.fx.GraphModule
    signature: inspect.Signature
    propagate: bool = ...
    def apply(self, match: Match, graph: torch.fx.Graph, node: torch.fx.Node): ...
    def __init__(self, pattern, extra_check, replacement_graph, signature, propagate) -> None: ...

def register_replacement_pattern(pattern, extra_check=..., pass_number: int = 1):
    """
    Register an aten to aten replacement pattern
    """
def register_lowering_pattern(pattern, extra_check=..., pass_number: int = 1):
    """
    Register an aten to inductor IR replacement pattern
    """
register_pattern = register_lowering_pattern

def replace_matched_patterns(graph: torch.fx.Graph): ...
def reorder_for_locality(graph: torch.fx.Graph): ...
def fx_passes(gm: torch.fx.GraphModule): ...
def mm_plus_mm(match: Match, mat1, mat2, mat3, mat4): ...
def cat_mm(match, inputs, dim): ...
def cat_addmm(match, inputs, dim): ...
def cat_tuned_op(match, inputs, dim, *, op, shape_of):
    """
    Memory planning to remove cat.  We can't use the stock memory
    planner since autotuning matmauls needs to know the output layout.
    """
def cat_slice_cat(match, cat_input, size, dim: int = 1):
    """
    This is an example of a more complex pattern where cat_1 is used
    multiple times inside the pattern.  We fold 2 calls to cat into one.

    Matches:
        cat_1: f32[1024, 4077] = torch.ops.aten.cat.default([add_26, primals_217], 1)
        slice_1: f32[1024, 4077] = torch.ops.aten.slice.Tensor(cat_1, 0, 0, 9223372036854775807)
        slice_2: f32[1024, 19] = torch.ops.aten.slice.Tensor(slice_1, 1, 0, 19)
        cat_2: f32[1024, 4096] = torch.ops.aten.cat.default([cat_1, slice_2], 1)


    Rewrite to:
        slice_2 = torch.ops.aten.slice.Tensor(add_26, 1, 0, 19)
        cat_2 = torch.ops.aten.cat.default([add_26, primals_217, slice2], 1)
    """
def addmm(mat1, mat2, added): ...
