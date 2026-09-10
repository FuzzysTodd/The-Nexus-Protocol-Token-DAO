from _typeshed import Incomplete
from tensorflow.core.protobuf import composite_tensor_variant_pb2 as composite_tensor_variant_pb2
from tensorflow.python.framework import composite_tensor as composite_tensor, dtypes as dtypes, ops as ops
from tensorflow.python.ops import gen_composite_tensor_ops as gen_composite_tensor_ops
from tensorflow.python.saved_model import nested_structure_coder as nested_structure_coder
from tensorflow.python.util import nest as nest

def composite_tensor_to_variants(value, type_spec: Incomplete | None = None, name: Incomplete | None = None):
    """Encodes `value` as a scalar variant tensor.

  Args:
    value: The `ExtensionType` value to encode.
    type_spec: Information about the value's type that should be included in the
      encoding.
    name: Optional name for the operation.

  Returns:
    A Tensor with shape=`()` and dtype=`tf.variant`.

  Raises:
    ValueError: If `type_spec` is not compatible with `value`.
  """
def composite_tensor_from_variant(encoded, type_spec, name: Incomplete | None = None):
    """Returns the `ExtensionType` value encoded by a variant scalar tensor.

  Args:
    encoded: A Tensor returned by `composite_tensor_to_variants`.
    type_spec: The `TypeSpec` of the original value.  This is used to determine
      the number and types of the component tensors that comprise the decoded
      value.  Must be compatible with the `TypeSpec` serilized in `encoded`.
    name: Optional name for the operation.

  Returns:
    An `ExtensionType` value that is compatible with `TypeSpec`.

  Raises:
    TypeError: If `encoded` is not a Tensor with dtype=variant.
    InvalidArgumentError: If `encoded` is not compatible with `type_spec`.
  """
