import torch
import torch.fx as fx
import torch.nn as nn
from _typeshed import Incomplete
from torch.fx.node import Argument as Argument, Target as Target
from torch.fx.passes.shape_prop import ShapeProp as ShapeProp
from torch.nn.utils.fusion import fuse_conv_bn_eval as fuse_conv_bn_eval
from typing import Any, Dict, Iterable, List, Type

def matches_module_pattern(pattern: Iterable[Type], node: fx.Node, modules: Dict[str, Any]): ...
def replace_node_module(node: fx.Node, modules: Dict[str, Any], new_module: torch.nn.Module): ...
def fuse(model: torch.nn.Module, inplace: bool = False) -> torch.nn.Module:
    """
    Fuses convolution/BN layers for inference purposes. Will deepcopy your
    model by default, but can modify the model inplace as well.
    """
def remove_dropout(model: nn.Module) -> nn.Module:
    """
    Removes all dropout layers from the module.
    """
def extract_subgraph(orig_module: nn.Module, nodes: List[fx.Node], inputs: List[fx.Node], outputs: List[fx.Node]):
    """
    Given lists of nodes from an existing graph that represent a subgraph, returns a submodule that executes that subgraph.
    """

mkldnn_supported: Incomplete
mkldnn_supported_unknown: Incomplete
mkldnn_map: Incomplete

def modules_to_mkldnn(nodes: List[fx.Node], modules: Dict[str, nn.Module]):
    """
    For each node, if it's a module that can be preconverted into MKLDNN,
    then we do so and create a mapping to allow us to convert from the MKLDNN
    version of the module to the original.
    """
def reset_modules(nodes: List[fx.Node], modules: Dict[str, nn.Module], old_modules: Dict[nn.Module, nn.Module]):
    """
    Maps each module that's been changed with `modules_to_mkldnn` back to its
    original.
    """

class MklSubgraph:
    fx_graph: Incomplete
    nodes: Incomplete
    start_nodes: Incomplete
    end_nodes: Incomplete
    def __init__(self, fx_graph: fx.Graph) -> None: ...

def gen_mkl_autotuner(example_inputs, iters: int = 10, warmup: int = 1):
    """
    This generates a heuristic that can be passed into `optimize_for_inference` that
    determines whether a subgraph should be run in MKL by running it with the example_inputs.

    Example usage:
        heuristic = gen_mkl_autotuner(example_inputs, iters=10)
        fast_model = optimization.optimize_for_inference(model, heuristic)
    """
def use_mkl_length(graph: MklSubgraph) -> bool:
    """
    This is a heuristic that can be passed into `optimize_for_inference` that
    determines whether a subgraph should be run in MKL by checking if there
    are more than 2 nodes in it
    """

class UnionFind:
    parent: Incomplete
    size: Incomplete
    def __init__(self, n) -> None: ...
    def make_set(self, v: int): ...
    def find(self, v: int) -> int: ...
    def join(self, a: int, b: int): ...

def optimize_for_inference(model: torch.nn.Module, pass_config: Dict[str, Any] | None = None, tracer: Type[fx.Tracer] = ...) -> torch.nn.Module:
    """
    Performs a set of optimization passes to optimize a model for the
    purposes of inference. Specifically, the passes that are run are:
    1. Conv/BN fusion
    2. Dropout removal
    3. MKL layout optimizations

    The third optimization takes a function `use_mkl_heuristic` that's used
    to determine whether a subgraph should be explicity run in MKL layout.

    Note: As FX does not currently handle aliasing, this pass currently
    assumes nothing aliases. If that isn't true, use at your own risk.
    """
