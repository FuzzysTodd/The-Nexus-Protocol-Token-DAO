from _typeshed import Incomplete
from tensorflow.core.framework import attr_value_pb2 as attr_value_pb2
from tensorflow.python.eager import backprop_util as backprop_util
from tensorflow.python.framework import constant_op as constant_op, dtypes as dtypes, indexed_slices as indexed_slices, ops as ops, tensor_shape as tensor_shape, tensor_spec as tensor_spec, tensor_util as tensor_util
from tensorflow.python.ops import array_ops as array_ops, control_flow_ops as control_flow_ops, control_flow_util_v2 as util, default_gradient as default_gradient, gen_functional_ops as gen_functional_ops, gen_resource_variable_ops as gen_resource_variable_ops, gradients_util as gradients_util, handle_data_util as handle_data_util, list_ops as list_ops, math_ops as math_ops, tensor_array_ops as tensor_array_ops, while_v2_indexed_slices_rewriter as while_v2_indexed_slices_rewriter
from tensorflow.python.util import compat as compat, nest as nest, object_identity as object_identity, variable_utils as variable_utils
from typing import NamedTuple

glob_stateful_parallelism: bool

def while_loop(cond, body, loop_vars, shape_invariants: Incomplete | None = None, parallel_iterations: int = 10, maximum_iterations: Incomplete | None = None, name: Incomplete | None = None, return_same_structure: bool = True, back_prop: bool = True):
    """Like tf.while_loop, except emits a single While op."""

class OptimizedReductionOpsCacheKey(NamedTuple):
    op_type: Incomplete
    inputs: Incomplete
    dtypes: Incomplete
    input_types: Incomplete
    name: Incomplete
    attrs: Incomplete
    op_def: Incomplete
    compute_device: Incomplete

class _WhileBodyGradFuncGraph(util.WhileBodyFuncGraph):
    '''FuncGraph for the gradient function of the body of a While op.

  Contains the logic for capturing the tensors from the body of the forward
  While op which is as follows:
  1. If the tensor is of resource type (these are not accumulated):
     a. Ensure that the tensor is a loop invariant, i.e., it exists in both loop
        inputs and outputs at the same index.
     b. Lookup the corresponding resource tensor in the forward outer graph and
        try to capture that.
  2. If the tensor is not of resource type:
     a. Create an accumulator for that tensor and output it from the forward
        pass. Note this also requires adding it as an input to the forward pass.
     b. Capture the accumulator from the forward pass in this FuncGraph. This
        will later be resolved to the correct output of the forward While op.
     c. Pop a value from the captured placeholder and use it as the captured
        value for the forward pass tensor.

  This only allows capturing tensors in the forward graph. A ValueError is
  raised if an attempt is made to capture a tensor not in the forward graph.
  To manually capture a tensor that is not in the forward graph, call `capture`
  with `allowlisted=True`.

  Note: The `captures` dict does not contain the forward tensor since it is not
  directly captured. It contains the accumulator corresponding to this forward
  tensor.

  Attributes:
    while_op_needs_rewrite: True if any non-resource intermediates were
      captured, meaning the forward While op needs to be rewritten to output the
      corresponding accumulators.
    extra_inputs: list of EmptyTensorList tensors to be used as initial input to
    the new accumulators in the forward graph. It may also contain external
    captures of the custom gradient function.
    internal_capture_to_output: dict from a tensor_id(captured placeholder) to
      the corresponding tensor that needs to be added to the list of outputs.
      For instance, when capturing an accumulator TensorList this contains the
      TensorList obtained after popping a tensor from the list. Other entries
      in this dict are expected, though not enforced, to be identities.
      This dict is needed because these output tensors need to be added to
      FuncGraph.outputs "after" the tensors returned from the gradient function.
  '''
    extra_inputs: Incomplete
    internal_capture_to_output: Incomplete
    def __init__(self, name, forward_cond_graph, forward_body_graph, maximum_iterations, forward_while_op, body_graph_inputs, body_graph_outputs) -> None: ...
    @property
    def while_op_needs_rewrite(self): ...

class _OperationWithOutputs(ops.Operation):
    """Operation with pre-built `TF_Output`s.

  The C API for creating the extra placeholders for the cond graph returns
  SWIG wrapped TF_Output* pointers which we can use directly for
  `Operation.outputs`. The default constructor for `Operation` does not provide
  a way of specifying pre-built output tensors and always creates them. This is
  a performance overhead. It is not clear if adding that feature to the
  `Operation` API would be generally useful so for now we just have our own
  lightweight `Operation` implementation. Note that this does not extract a
  stacktrace as well since we don't expect this operation to be used.

  TODO(b/143286622): This should not be required once captures are separated
  from regular loop vars.
  """
    def __init__(self, c_op, g) -> None: ...
