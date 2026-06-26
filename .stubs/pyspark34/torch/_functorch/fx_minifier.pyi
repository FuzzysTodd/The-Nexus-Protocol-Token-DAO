import torch
import torch.fx as fx
from .compile_utils import get_outputs as get_outputs, get_placeholders as get_placeholders
from dataclasses import dataclass
from typing import Callable, List

class ConcreteProp(torch.fx.Interpreter):
    def run_node(self, n): ...
    def propagate(self, *args): ...

def dump_state(fx_g, inps) -> None: ...

@dataclass
class ReproState:
    graph: fx.Graph
    inps: List[torch.Tensor]
    def __init__(self, graph, inps) -> None: ...

def minifier(fail_f: fx.GraphModule, inps, module_fails, dump_state: Callable = ...):
    """
    Minimizes a FX graph with given inputs, such that the resulting FX graph still returns True for module_fails.

    Does 2 main strategies:
    1. Truncates suffix: Removes some suffix from the graph and sets a new output.
    2. Delta Debugging: Tries replacing half of the graph with inputs. If fails,
        tries replacing quarter of the graph, etc.

    >>> # xdoctest: +SKIP(failing)
    >>> failing_function = fx.symbolic_trace(f)
    >>> minimize(failing_function, [torch.randn(5)], lambda fx_g, inps: fx_g(*inps))

    note: module_fails returns True if it fails.
    """
