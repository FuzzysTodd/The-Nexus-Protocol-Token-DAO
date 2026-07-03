import torch
import torch.fx as fx
from . import config as config
from .compile_utils import fx_graph_cse as fx_graph_cse, get_aten_target as get_aten_target
from _typeshed import Incomplete
from torch.fx.experimental.proxy_tensor import is_sym_node as is_sym_node, py_sym_types as py_sym_types
from torch.fx.experimental.symbolic_shapes import hint_int as hint_int
from torch.fx.passes import graph_drawer as graph_drawer
from typing import Tuple

AOT_PARTITIONER_DEBUG: Incomplete

class InvalidNodeBase: ...

InvalidNode: Incomplete

def default_partition(joint_module: fx.GraphModule, _joint_inputs, *, num_fwd_outputs) -> Tuple[fx.GraphModule, fx.GraphModule]:
    """
    Partitions the :attr:`joint_module` in a manner that closely resembles the
    behavior observed in the original ``.forward()`` and ``.backward()`` of the
    callable, i.e., the resulting forward graph contains those operators that
    are executed in the original ``.forward()`` callable passed to
    :func:`aot_function`.

    The default partitioner collects the operators that are between the forward
    inputs and the forward outputs. This helps in finding the tensors which have
    to be stashed for the backward pass. These stashed tensors become the output
    of the generated forward graph. The remaining operators are then placed in
    the backward graph.

    .. warning::
        This API is experimental and likely to change.

    Args:
        joint_module(fx.GraphModule): The joint forward and backward graph. This
            is the result of AOT Autograd tracing.

    Returns:
        Returns the generated forward and backward Fx graph modules.
    """
def pointwise_ops(): ...
def min_cut_rematerialization_partition(joint_module: fx.GraphModule, _joint_inputs, compiler: str = 'nvfuser', recomputable_ops: Incomplete | None = None, *, num_fwd_outputs) -> Tuple[fx.GraphModule, fx.GraphModule]:
    """
    Partitions the joint graph such that the backward recomputes the forward.
    Recomputing helps in trading off memory bandwidth with computation.

    To create the fwd and bwd graph, we copy the joint graph, manually set the
    outputs to just original forward or backward outputs. And then we run the
    resulting graphs through dead code elimintation.

    .. warning::
        This API is experimental and likely to change.

    Args:
        joint_module(fx.GraphModule): The joint forward and backward graph. This
            is the result of AOT Autograd tracing.
        _joint_inputs: The inputs to the joint graph. This is unused.
        compiler: This option determines the default set of recomputable ops.
            Currently, there are two options: ``nvfuser`` and ``inductor``.
        recomputable_ops: This is an optional set of recomputable ops. If this
            is not None, then this set of ops will be used instead of the
            default set of ops.
        num_fwd_outputs: The number of outputs from the forward graph.

    Returns:
        Returns the generated forward and backward Fx graph modules.
    """
def draw_graph(traced: torch.fx.GraphModule, fname: str, figname: str = 'fx_graph', clear_meta: bool = True): ...
def draw_joint_graph(graph, joint_inputs, file_name: str = 'full_graph.png'): ...
