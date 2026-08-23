from _typeshed import Incomplete
from tensorflow.core.framework import tensor_pb2 as tensor_pb2
from tensorflow.python import pywrap_tfe as pywrap_tfe
from tensorflow.python.eager import core as core
from tensorflow.python.framework import dtypes as dtypes, ops as ops, tensor_shape as tensor_shape
from tensorflow.python.util import compat as compat

def quick_execute(op_name, num_outputs, inputs, attrs, ctx, name: Incomplete | None = None):
    """Execute a TensorFlow operation.

  Args:
    op_name: Name of the TensorFlow operation (see REGISTER_OP in C++ code) to
      execute.
    num_outputs: The number of outputs of the operation to fetch. (Explicitly
      provided instead of being inferred for performance reasons).
    inputs: A list of inputs to the operation. Each entry should be a Tensor, or
      a value which can be passed to the Tensor constructor to create one.
    attrs: A tuple with alternating string attr names and attr values for this
      operation.
    ctx: The value of context.context().
    name: Customized name for the operation.

  Returns:
    List of output Tensor objects. The list is empty if there are no outputs

  Raises:
    An exception on error.
  """
def execute_with_cancellation(op_name, num_outputs, inputs, attrs, ctx, cancellation_manager, name: Incomplete | None = None):
    """Execute a TensorFlow operation.

  Args:
    op_name: Name of the TensorFlow operation (see REGISTER_OP in C++ code) to
      execute.
    num_outputs: The number of outputs of the operation to fetch. (Explicitly
      provided instead of being inferred for performance reasons).
    inputs: A list of inputs to the operation. Each entry should be a Tensor, or
      a value which can be passed to the Tensor constructor to create one.
    attrs: A tuple with alternating string attr names and attr values for this
      operation.
    ctx: The value of context.context().
    cancellation_manager: a `CancellationManager` object that can be used to
      cancel the operation.
    name: Customized name for the operation.

  Returns:
    List of output Tensor objects. The list is empty if there are no outputs

  Raises:
    An exception on error.
  """
def execute_with_callbacks(op_name, num_outputs, inputs, attrs, ctx, name: Incomplete | None = None):
    """Monkey-patch to execute to enable execution callbacks."""
execute = quick_execute

def must_record_gradient():
    """Import backprop if you want gradients recorded."""
def record_gradient(unused_op_name, unused_inputs, unused_attrs, unused_outputs) -> None:
    """Import backprop if you want gradients recorded."""
def make_float(v, arg_name): ...
def make_int(v, arg_name): ...
def make_str(v, arg_name): ...
def make_bool(v, arg_name): ...
def make_type(v, arg_name): ...
def make_shape(v, arg_name):
    """Convert v into a list."""
def make_tensor(v, arg_name):
    """Ensure v is a TensorProto."""
def args_to_matching_eager(l, ctx, allowed_dtypes, default_dtype: Incomplete | None = None):
    """Convert sequence `l` to eager same-type Tensors."""
def convert_to_mixed_eager_tensors(values, ctx): ...
def args_to_mixed_eager_tensors(lists, ctx):
    """Converts a list of same-length lists of values to eager tensors."""
