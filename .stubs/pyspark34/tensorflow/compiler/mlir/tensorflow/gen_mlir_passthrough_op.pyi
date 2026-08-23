from _typeshed import Incomplete
from tensorflow.python.util.deprecation import deprecated_endpoints as deprecated_endpoints
from tensorflow.python.util.tf_export import tf_export as tf_export

def mlir_passthrough_op(inputs, mlir_module, Toutputs, name: Incomplete | None = None):
    """TODO: add doc.

  Args:
    inputs: A list of `Tensor` objects.
    mlir_module: A `string`.
    Toutputs: A list of `tf.DTypes`.
    name: A name for the operation (optional).

  Returns:
    A list of `Tensor` objects of type `Toutputs`.
  """

MlirPassthroughOp: Incomplete

def mlir_passthrough_op_eager_fallback(inputs, mlir_module, Toutputs, name, ctx): ...
