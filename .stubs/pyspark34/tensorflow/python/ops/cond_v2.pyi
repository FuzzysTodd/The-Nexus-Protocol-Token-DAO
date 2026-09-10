from _typeshed import Incomplete
from tensorflow.core.framework import types_pb2 as types_pb2
from tensorflow.python.eager import backprop_util as backprop_util
from tensorflow.python.framework import auto_control_deps as auto_control_deps, constant_op as constant_op, dtypes as dtypes, errors_impl as errors_impl, indexed_slices as indexed_slices, ops as ops, tensor_shape as tensor_shape, tensor_util as tensor_util, type_spec as type_spec
from tensorflow.python.ops import array_ops as array_ops, control_flow_util as control_flow_util, control_flow_util_v2 as util, default_gradient as default_gradient, gen_functional_ops as gen_functional_ops, gen_optional_ops as gen_optional_ops, gradients_util as gradients_util, handle_data_util as handle_data_util, math_ops as math_ops
from tensorflow.python.util import nest as nest

def cond_v2(pred, true_fn, false_fn, name: str = 'cond'):
    """Like tf.cond, except emits a single If op."""
def get_func_graphs(op):
    """Returns `FuncGraph`s for the input op branches.

  Args:
    op: The If or Case Operation.

  Returns:
    A tuple of the `FuncGraph`s of the then_branch and else_branch (all branches
    for Case).
  """
def verify_captures(op_type, branch_graphs) -> None:
    """Verify that a branch's tensor is not accessed in another branch fn."""

class _CondGradFuncGraph(util.CondBranchFuncGraph):
    """FuncGraph for the gradient function of the branch of an If op.

  Handles wrapping and unwrapping intermediate values that are captured by the
  gradient computation in optionals.

  Attributes:
    op_needs_rewrite: True if any intermediates were captured, meaning the
      forward If op needs to be written to output the wrapped intermediates.
  """
    op_needs_rewrite: bool
    def __init__(self, name, forward_graph) -> None: ...
    @property
    def wrapped_intermediates(self):
        """The optional-wrapped intermediates captured from the forward graph."""
    @property
    def xla_intermediates(self):
        """Raw intermediates captured from the forward graph if XLA is enabled."""

def indexed_case(branch_index, branch_fns, name: str = 'indexed_case', lower_using_switch_merge: Incomplete | None = None):
    """Like conv_v2, except emits a Case op instead of an If."""
