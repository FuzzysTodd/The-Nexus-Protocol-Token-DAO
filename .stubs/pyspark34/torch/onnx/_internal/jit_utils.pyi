import dataclasses
import torch
from torch import _C
from torch.onnx._globals import GLOBALS as GLOBALS
from torch.onnx._internal import registration as registration
from typing import Any, Dict, Tuple

@dataclasses.dataclass
class GraphContext:
    """Extra context for symbolic functions with all methods from torch.Graph.

    NOTE: This class is not meant for external consumption. Please do not depend on
    it outside of torch.onnx as the interface may evolve.

    Attributes:
        graph: The _C.Graph being constructed.
        block: The current _C.Block being constructed.
        opset: The opset version.
        original_node: Current node that is being converted from.
        params_dict: Mapping from graph initializer name to IValue.
        env: Mapping from Torch domain graph Value to ONNX domain graph Value.
    """
    graph: _C.Graph
    block: _C.Block
    opset: int
    original_node: _C.Node
    params_dict: Dict[str, '_C.IValue']
    env: Dict[_C.Value, _C.Value]
    def __getattr__(self, name: str) -> Any: ...
    def op(self, opname: str, *raw_args: torch.Tensor | _C.Value, outputs: int = 1, **kwargs):
        '''Creates an ONNX operator "opname", taking "raw_args" as inputs and "kwargs" as attributes.

        The set of operators and the inputs/attributes they take
        is documented at https://github.com/onnx/onnx/blob/master/docs/Operators.md

        Args:
            opname: The ONNX operator name, e.g., `Abs` or `Add`, or an operator qualified
                with a namespace, e.g., `aten::add`.
            raw_args: The inputs to the operator; usually provided
                as arguments to the `symbolic` definition.
            outputs: The number of outputs this operator returns.
                By default an operator is assumed to return a single output.
                If `outputs` is greater than one, this functions returns a tuple
                of output `Value`, representing each output of the ONNX operator
                in order.
            kwargs: The attributes of the ONNX operator, whose keys are named
                according to the following convention: `alpha_f` indicates
                the `alpha` attribute with type `f`.  The valid type specifiers are
                `f` (float), `i` (int), `s` (string) or `t` (Tensor).  An attribute
                specified with type float accepts either a single float, or a
                list of floats (e.g., you would say `dims_i` for a `dims` attribute
                that takes a list of integers).

        Returns:
            The value representing the single output of this operator (see the `outputs`
            keyword argument for multi-return nodes).
        '''
    def aten_op(self, operator: str, *args, overload_name: str = '', **kwargs):
        """Generates an ONNX ATen op node.

        This function is for backward compatibility with the old symbolic functions.
        """
    at = aten_op
    def onnxscript_op(self, onnx_fn, *raw_args: torch.Tensor | _C.Value, outputs: int = 1, **kwargs):
        '''Creates an ONNX operator from onnx-script function, taking "raw_args" as inputs and "kwargs" as attributes.

        onnx-script repository: https://github.com/microsoft/onnx-script

        Args:
            onnx_fn: ONNXFunction from onnx-script; An example can be found at
                https://github.com/microsoft/onnx-script#example
            raw_args: The inputs to the operator; usually provided
                as arguments to the `symbolic` definition.
            outputs: The number of outputs this operator returns.
                By default an operator is assumed to return a single output.
                If `outputs` is greater than one, this functions returns a tuple
                of output `Value`, representing each output of the ONNX operator
                in order.
            kwargs: The attributes of the ONNX operator, whose keys are named
                according to the following convention: `alpha_f` indicates
                the `alpha` attribute with type `f`.  The valid type specifiers are
                `f` (float), `i` (int), `s` (string) or `t` (Tensor).  An attribute
                specified with type float accepts either a single float, or a
                list of floats (e.g., you would say `dims_i` for a `dims` attribute
                that takes a list of integers).

        Returns:
            The value representing the single output of this operator (see the `outputs`
            keyword argument for multi-return nodes).
        '''
    def __init__(self, graph, block, opset, original_node, params_dict, env) -> None: ...

def add_op_with_blocks(graph_context: GraphContext, opname: str, *inputs: _C.Value, outputs: int = 1, n_blocks: int = 1, **attributes) -> Tuple[Any, Tuple[GraphContext, ...], _C.Node]:
    '''Creates an ONNX operator "opname", taking inputs and attributes.

    Args:
        graph_context: The context for the current graph.
        opname: The ONNX operator name, e.g., `Abs` or `Add`, or an operator qualified
            with a namespace, e.g., `aten::add`.
        inputs: The inputs to the operator.
        outputs: The number of outputs this operator returns.
            By default an operator is assumed to return a single output.
            If `outputs` is greater than one, this functions returns a tuple
            of output `Value`, representing each output of the ONNX operator
            in order.
        n_blocks: The number of sub-blocks to create in the node.
        attributes: The attributes of the ONNX operator.

    Returns:
        A tuple of (output_values, new_contexts, node) where:
            output_values: ONe or more output value of this operator
                (see the `outputs` keyword argument for multi-return nodes).
            new_contexts: A tuple of new graph contexts for each sub-block.
            node: The node representing the operator.
    '''
def get_device_from_value(value: _C.Value) -> torch.device | None: ...
def parse_node_kind(kind: str) -> Tuple[str, str]:
    """Parse node kind into domain and Op name."""
def is_aten(domain: str) -> bool:
    """Check if the domain is official."""
def is_prim(domain: str) -> bool:
    """Check if the domain is official."""
def is_onnx(domain: str) -> bool:
    """Check if the domain is official."""
