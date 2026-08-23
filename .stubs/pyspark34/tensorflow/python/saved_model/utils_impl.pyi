from _typeshed import Incomplete
from tensorflow.core.framework import types_pb2 as types_pb2
from tensorflow.core.protobuf import meta_graph_pb2 as meta_graph_pb2, struct_pb2 as struct_pb2
from tensorflow.python.eager import context as context
from tensorflow.python.framework import composite_tensor as composite_tensor, dtypes as dtypes, ops as ops, sparse_tensor as sparse_tensor, tensor_shape as tensor_shape
from tensorflow.python.ops import resource_variable_ops as resource_variable_ops
from tensorflow.python.saved_model import nested_structure_coder as nested_structure_coder
from tensorflow.python.util import deprecation as deprecation, nest as nest
from tensorflow.python.util.tf_export import tf_export as tf_export

def build_tensor_info(tensor):
    """Utility function to build TensorInfo proto from a Tensor.

  Args:
    tensor: Tensor or SparseTensor whose name, dtype and shape are used to
        build the TensorInfo. For SparseTensors, the names of the three
        constituent Tensors are used.

  Returns:
    A TensorInfo protocol buffer constructed based on the supplied argument.

  Raises:
    RuntimeError: If eager execution is enabled.

  @compatibility(TF2)
  This API is not compatible with eager execution as `tensor` needs to be a
  graph tensor, and there is no replacement for it in TensorFlow 2.x. To start
  writing programs using TensorFlow 2.x, please refer to the [Effective
  TensorFlow 2](https://www.tensorflow.org/guide/effective_tf2) guide.
  @end_compatibility
  """
def build_tensor_info_internal(tensor):
    """Utility function to build TensorInfo proto from a Tensor."""
def build_tensor_info_from_op(op):
    '''Utility function to build TensorInfo proto from an Op.

  Note that this function should be used with caution. It is strictly restricted
  to TensorFlow internal use-cases only. Please make sure you do need it before
  using it.

  This utility function overloads the TensorInfo proto by setting the name to
  the Op\'s name, dtype to DT_INVALID and tensor_shape as None. One typical usage
  is for the Op of the call site for the defunned function:
  ```python
    @function.defun
    def some_variable_initialization_fn(value_a, value_b):
      a = value_a
      b = value_b

    value_a = constant_op.constant(1, name="a")
    value_b = constant_op.constant(2, name="b")
    op_info = utils.build_op_info(
        some_variable_initialization_fn(value_a, value_b))
  ```

  Args:
    op: An Op whose name is used to build the TensorInfo. The name that points
        to the Op could be fetched at run time in the Loader session.

  Returns:
    A TensorInfo protocol buffer constructed based on the supplied argument.

  Raises:
    RuntimeError: If eager execution is enabled.
  '''
def get_tensor_from_tensor_info(tensor_info, graph: Incomplete | None = None, import_scope: Incomplete | None = None):
    """Returns the Tensor or CompositeTensor described by a TensorInfo proto.

  Args:
    tensor_info: A TensorInfo proto describing a Tensor or SparseTensor or
      CompositeTensor.
    graph: The tf.Graph in which tensors are looked up. If None, the
        current default graph is used.
    import_scope: If not None, names in `tensor_info` are prefixed with this
        string before lookup.

  Returns:
    The Tensor or SparseTensor or CompositeTensor in `graph` described by
    `tensor_info`.

  Raises:
    KeyError: If `tensor_info` does not correspond to a tensor in `graph`.
    ValueError: If `tensor_info` is malformed.
  """
def get_element_from_tensor_info(tensor_info, graph: Incomplete | None = None, import_scope: Incomplete | None = None):
    """Returns the element in the graph described by a TensorInfo proto.

  Args:
    tensor_info: A TensorInfo proto describing an Op or Tensor by name.
    graph: The tf.Graph in which tensors are looked up. If None, the current
      default graph is used.
    import_scope: If not None, names in `tensor_info` are prefixed with this
      string before lookup.

  Returns:
    Op or tensor in `graph` described by `tensor_info`.

  Raises:
    KeyError: If `tensor_info` does not correspond to an op or tensor in `graph`
  """

byte_swappable: Incomplete

def swap_function_tensor_content(meta_graph_def, from_endiness, to_endiness) -> None: ...
def byte_swap_tensor_content(tensor, from_endiness, to_endiness) -> None:
    """Byte swaps."""
