from _typeshed import Incomplete
from tensorflow.python.framework import constant_op as constant_op, dtypes as dtypes, ops as ops
from tensorflow.python.ops import array_ops as array_ops, control_flow_ops as control_flow_ops, math_ops as math_ops
from tensorflow.python.ops.ragged import ragged_tensor as ragged_tensor
from tensorflow.python.ops.ragged.ragged_tensor import RaggedTensor as RaggedTensor
from tensorflow.python.util import deprecation as deprecation, dispatch as dispatch

def squeeze(input: ragged_tensor.Ragged, axis: Incomplete | None = None, name: Incomplete | None = None):
    """Ragged compatible squeeze.

  If `input` is a `tf.Tensor`, then this calls `tf.squeeze`.

  If `input` is a `tf.RaggedTensor`, then this operation takes `O(N)` time,
  where `N` is the number of elements in the squeezed dimensions.

  Args:
    input: A potentially ragged tensor. The input to squeeze.
    axis: An optional list of ints. Defaults to `None`. If the `input` is
      ragged, it only squeezes the dimensions listed. It fails if `input` is
      ragged and axis is []. If `input` is not ragged it calls tf.squeeze. Note
      that it is an error to squeeze a dimension that is not 1. It must be in
      the range of [-rank(input), rank(input)).
   name: A name for the operation (optional).

  Returns:
    A potentially ragged tensor. Contains the same data as input,
    but has one or more dimensions of size 1 removed.
  """
