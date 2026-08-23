from _typeshed import Incomplete
from tensorflow.core.config import flags as flags
from tensorflow.core.framework import attr_value_pb2 as attr_value_pb2, tensor_pb2 as tensor_pb2, tensor_shape_pb2 as tensor_shape_pb2, types_pb2 as types_pb2
from tensorflow.python.framework import dtypes as dtypes, op_callbacks as op_callbacks, op_def_library_pybind as op_def_library_pybind, op_def_registry as op_def_registry, ops as ops, tensor_shape as tensor_shape
from tensorflow.python.util import compat as compat, tf_contextlib as tf_contextlib

def apply_op(op_type_name, name: Incomplete | None = None, **keywords):
    '''Add a node invoking a registered Op to a graph.

  Example usage:
     # input1 and input2 can be Tensors or anything ops.convert_to_tensor()
     # will convert to a Tensor.
     op_def_library.apply_op("op", input1=input1, input2=input2)
     # Can specify a node name.
     op_def_library.apply_op("op", input1=input1, name="node_name")
     # Must use keyword arguments, with the names specified in the OpDef.
     op_def_library.apply_op("op", input_name=input, attr_name=attr)

  All attrs must either be inferred from an input or specified.
  (If inferred, the attr must not be specified.)  If an attr has a default
  value specified in the Op\'s OpDef, then you may pass None as the value
  of that attr to get the default.

  Args:
    op_type_name: string. Must match the name field of a registered Op.
    name: string. Optional name of the created op.
    **keywords: input Tensor and attr arguments specified by name, and optional
      parameters to pass when constructing the Operation.

  Returns:
    The Tensor(s) representing the output of the operation, or the Operation
    itself if there are no outputs.

  Raises:
    RuntimeError: On some errors.
    TypeError: On some errors.
    ValueError: On some errors.
  '''
def value_to_attr_value(value, attr_type, arg_name):
    """Encodes a Python value as an `AttrValue` proto message.

  Args:
    value: The value to convert.
    attr_type: The value type (string) -- see the AttrValue proto definition for
      valid strings.
    arg_name: Argument name (for error messages).

  Returns:
    An AttrValue proto message that encodes `value`.
  """
