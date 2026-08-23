from _typeshed import Incomplete
from tensorflow.python.framework import constant_op as constant_op, dtypes as dtypes, ops as ops
from tensorflow.python.ops import array_ops as array_ops, math_ops as math_ops, random_ops as random_ops
from tensorflow.python.ops.ragged import dynamic_ragged_shape as dynamic_ragged_shape, ragged_tensor as ragged_tensor
from tensorflow.python.ops.ragged.row_partition import RowPartition as RowPartition
from tensorflow.python.ops.structured.structured_tensor import StructuredTensor as StructuredTensor
from tensorflow.python.util import deprecation as deprecation, dispatch as dispatch

def shape_v2(input: StructuredTensor, out_type=..., name: Incomplete | None = None) -> dynamic_ragged_shape.DynamicRaggedShape:
    """Returns a DynamicRaggedShape containing the shape of the input."""
def shape_v1(input: StructuredTensor, name: Incomplete | None = None, out_type=...) -> dynamic_ragged_shape.DynamicRaggedShape:
    """Returns a DynamicRaggedShape containing the shape of the input."""
def expand_dims(input, axis: Incomplete | None = None, name: Incomplete | None = None, dim: Incomplete | None = None):
    '''Creates a StructuredTensor with a length 1 axis inserted at index `axis`.

  This is an implementation of tf.expand_dims for StructuredTensor. Note
  that the `axis` must be less than or equal to rank.

  >>> st = StructuredTensor.from_pyval([[{"x": 1}, {"x": 2}], [{"x": 3}]])
  >>> tf.expand_dims(st, 0).to_pyval()
  [[[{\'x\': 1}, {\'x\': 2}], [{\'x\': 3}]]]
  >>> tf.expand_dims(st, 1).to_pyval()
  [[[{\'x\': 1}, {\'x\': 2}]], [[{\'x\': 3}]]]
  >>> tf.expand_dims(st, 2).to_pyval()
  [[[{\'x\': 1}], [{\'x\': 2}]], [[{\'x\': 3}]]]
  >>> tf.expand_dims(st, -1).to_pyval()  # -1 is the same as 2
  [[[{\'x\': 1}], [{\'x\': 2}]], [[{\'x\': 3}]]]

  Args:
    input: the original StructuredTensor.
    axis: the axis to insert the dimension: `-(rank + 1) <= axis <= rank`
    name: the name of the op.
    dim: deprecated: use axis.

  Returns:
    a new structured tensor with larger rank.

  Raises:
    an error if `axis < -(rank + 1)` or `rank < axis`.
  '''
def expand_dims_v2(input, axis, name: Incomplete | None = None):
    '''Creates a StructuredTensor with a length 1 axis inserted at index `axis`.

  This is an implementation of tf.expand_dims for StructuredTensor. Note
  that the `axis` must be less than or equal to rank.

  >>> st = StructuredTensor.from_pyval([[{"x": 1}, {"x": 2}], [{"x": 3}]])
  >>> tf.expand_dims(st, 0).to_pyval()
  [[[{\'x\': 1}, {\'x\': 2}], [{\'x\': 3}]]]
  >>> tf.expand_dims(st, 1).to_pyval()
  [[[{\'x\': 1}, {\'x\': 2}]], [[{\'x\': 3}]]]
  >>> tf.expand_dims(st, 2).to_pyval()
  [[[{\'x\': 1}], [{\'x\': 2}]], [[{\'x\': 3}]]]
  >>> tf.expand_dims(st, -1).to_pyval()  # -1 is the same as 2
  [[[{\'x\': 1}], [{\'x\': 2}]], [[{\'x\': 3}]]]

  Args:
    input: the original StructuredTensor.
    axis: the axis to insert the dimension: `-(rank + 1) <= axis <= rank`
    name: the name of the op.

  Returns:
    a new structured tensor with larger rank.

  Raises:
    an error if `axis < -(rank + 1)` or `rank < axis`.
  '''
def gather(params, indices, validate_indices: Incomplete | None = None, name: Incomplete | None = None, axis: Incomplete | None = None, batch_dims: int = 0):
    """tf.gather for structured tensors.

  Does not support (yet) checks on illegal axis values, et cetera.

  Indices must be a ragged or dense tensor.
  Args:
    params: a structured tensor to be gathered
    indices: a ragged tensor or tensor to gather by.
    validate_indices: whether to validate the indices
    name: the name of the op(s).
    axis: the axis in params to gather on.
    batch_dims: the number of batch dimensions.

  Returns:
    the params reorganized according to indices.
  """
def concat(values, axis, name: str = 'concat'):
    """tf.concat for structured tensors.

  Does not support (yet) checks on illegal axis values, et cetera.

  Args:
    values: a sequence of StructuredTensors.
    axis: an axis to concatenate upon.
    name: the name of the op(s).

  Returns:
    the params reorganized according to indices.
  """
def random_shuffle(value, seed: Incomplete | None = None, name: Incomplete | None = None):
    """Shuffle a structured tensor on the zeroth axis.

  Args:
    value: a structured tensor of rank at least one.
    seed: the seed for shuffling.
    name: the name for shuffle.

  Returns:
    The shuffled structured tensor.
  """
def size_v2(input, out_type=..., name: Incomplete | None = None):
    """Returns the size of a tensor."""
def size(input, name: Incomplete | None = None, out_type=...):
    """Returns the size of a tensor."""
def zeros_like(tensor, dtype: Incomplete | None = None, name: Incomplete | None = None, optimize: bool = True):
    """Implementation of zeros_like for StructuredTensor for TF v1."""
def zeros_like_v2(input, dtype: Incomplete | None = None, name: Incomplete | None = None):
    '''Replace every object with a zero.

  Example:
  >>> st = StructuredTensor.from_pyval([{"x":[3]}, {"x":[4,5]}])
  >>> tf.zeros_like(st)
  <tf.Tensor: shape=(2,), dtype=int32, numpy=array([0.0, 0.0], dtype=float32)>
  >>> st = StructuredTensor.from_pyval([[{"x":[3]}], [{"x":[4,5]}, {"x":[]}]])
  >>> tf.zeros_like(st, dtype=tf.int32)
  <tf.RaggedTensor [[0], [0, 0]]>

  Args:
    input: a structured tensor.
    dtype: the dtype of the resulting zeros. (default is tf.float32)
    name: a name for the op.
  Returns:
    a tensor of zeros of the same shape.
  '''
def ones_like(tensor, dtype: Incomplete | None = None, name: Incomplete | None = None, optimize: bool = True):
    """Implementation of zeros_like for StructuredTensor for TF v1."""
def ones_like_v2(input, dtype: Incomplete | None = None, name: Incomplete | None = None):
    '''Replace every object with a zero.

  Example:
  >>> st = StructuredTensor.from_pyval([{"x":[3]}, {"x":[4,5]}])
  >>> tf.ones_like(st)
  <tf.Tensor: shape=(2,), dtype=int32, numpy=array([1.0, 1.0], dtype=float32)>
  >>> st = StructuredTensor.from_pyval([[{"x":[3]}], [{"x":[4,5]}, {"x":[]}]])
  >>> tf.ones_like(st, dtype=tf.int32)
  <tf.RaggedTensor [[1], [1, 1]]>

  Args:
    input: a structured tensor.
    dtype: the dtype of the resulting zeros. (default is tf.float32)
    name: a name for the op.
  Returns:
    a tensor of zeros of the same shape.
  '''
def rank(input, name: Incomplete | None = None):
    """Returns the rank of a tensor."""
def empty_st_op_like_zeros(leaf_op): ...
