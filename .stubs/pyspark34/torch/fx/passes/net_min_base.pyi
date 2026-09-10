import torch.fx
from .tools_common import Names, NodeSet, TensorOrTensors, Tensors
from _typeshed import Incomplete
from dataclasses import dataclass
from typing import Callable, List, Tuple

__all__ = ['FxNetMinimizerBadModuleError', 'FxNetMinimizerRunFuncError', 'FxNetMinimizerResultMismatchError']

class FxNetMinimizerBadModuleError(Exception):
    """
    Raised if failed to split out a minimize module
    """
class FxNetMinimizerRunFuncError(Exception):
    """
    Raised if error occurs during run_a or run_b functions
    """
class FxNetMinimizerResultMismatchError(Exception):
    """
    Raised if comparing function thinks the results are mismatching.
    """

@dataclass
class _MinimizerSettingBase:
    '''
    Args:
    `accumulate_error`: Instead of using a\'s input for both converted module to verify
    , use the previous outputs of each converted module as input to accumulate the
    errors.

    `traverse_method`: "sequential" or "binary" or "accumulate"
    Determine the way of traverse the nodes in FX module.

    `find_all`: Minimizer will go through the entire model and return all problematic nodes.

    `return_intermediate`: If true, when using `run_nodes()` function to run the
    model, intermediate results of all the ops will be returned as output.
    '''
    accumulate_error: bool = ...
    traverse_method: str = ...
    find_all: bool = ...
    return_intermediate: bool = ...
    def __init__(self, accumulate_error, traverse_method, find_all, return_intermediate) -> None: ...

class _MinimizerBase:
    """
    This class is used to automatically find problematic nodes in a model. It takes a FX
    graphmodule and generate some submodules while traverse the graph. Then two functions
    `run_a` and `run_b` will be used to run the same submodule and a function `compare_fn`
    will be used to compare the results.

    Currently we provides two ways to traverse the graph and generate submodules.
        1. Sequential traversal: this will traverse the graph node by node and generate
           one submodule with one sigle node.
        2. Binary searching: this will do a binary search style traversal on the graph.

    For internal Users, a guide can be found here https://fb.quip.com/HDtuAgiKGfkP.
    """
    module: Incomplete
    sample_input: Incomplete
    compare_fn: Incomplete
    settings: Incomplete
    a_outputs: Incomplete
    b_outputs: Incomplete
    results: Incomplete
    reports: Incomplete
    iteration: int
    fusions: Incomplete
    def __init__(self, module: torch.fx.GraphModule, sample_input: Tensors, compare_fn: Callable[[TensorOrTensors, TensorOrTensors, Names], Tuple[float, bool]], settings: _MinimizerSettingBase) -> None: ...
    def run_a(self, mod: torch.fx.GraphModule, inputs: Tensors) -> TensorOrTensors:
        """
        Run `mod` with `inputs` and generate output. The output will be compared with
        output of run_b().
        """
    def run_b(self, mod: torch.fx.GraphModule, inputs: Tensors) -> TensorOrTensors:
        """
        Run `mod` with `inputs` and generate output. The output will be compared with
        output of run_a().
        """
    def run_nodes(self, start: str | None = None, end: str | None = None):
        """
        Run part of the model from `start` node to `end` node. If `start` is None
        then we start from the beginning of the model. If `end` is None then we
        stop at the end of the model.

        Args:
            start: The name of the node which is the first node of the submodule
                we want to run. If set to None, then we'll start with the first
                node of the model.
            end: The name of the node which is the last node of the submodule we
                want to run. If set to None, we'll end with the last node of the
                model.
        """
    def print_report(self, report: List[str]): ...
    def print_reports(self) -> None: ...
    def minimize(self, start: str | None = None, end: str | None = None) -> NodeSet:
        """
        Minimizing the model from node with name `start` to node with name `end` base
        on self.settings. Find culprits that causes FxNetMinimizerRunFuncError or
        FxNetMinimizerResultMismatchError errors.

        Args:
            start: The name of the node where we want to start minimizing. If set
                to None, then we'll start with the first node of the model.
            end: The name of the node where we want to terminate minimizing. If
                set to None, we'll end with the last node of the model.

        Returns:
            nodes: A list of nodes that causes FxNetMinimizerRunFuncError or
                FxNetMinimizerResultMismatchError errors during minimizing.
        """
