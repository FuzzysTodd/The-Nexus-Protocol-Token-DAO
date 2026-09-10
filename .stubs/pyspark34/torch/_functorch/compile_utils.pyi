import torch
from _typeshed import Incomplete
from torch.utils._pytree import tree_flatten as tree_flatten

aten: Incomplete

def get_aten_target(node): ...

rand_ops: Incomplete

def fx_graph_cse(fx_g: torch.fx.graph.Graph): ...
def strip_overloads(gm) -> None:
    """
    Modifies the target of graph nodes in :attr:`gm` to strip overloads.

    Args:
        gm(fx.GraphModule): The input Fx graph module to be modified
    """
def get_placeholders(graph): ...
def get_outputs(graph): ...
