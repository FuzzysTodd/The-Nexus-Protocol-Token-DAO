from _typeshed import Incomplete
from tensorflow.python.framework import dtypes as dtypes, ops as ops, tensor_shape as tensor_shape, tensor_util as tensor_util
from tensorflow.python.ops import array_ops as array_ops, math_ops as math_ops
from tensorflow.python.ops.ragged import ragged_util as ragged_util
from tensorflow.python.util import dispatch as dispatch
from tensorflow.python.util.tf_export import tf_export as tf_export

def row_splits_to_segment_ids(splits, name: Incomplete | None = None, out_type: Incomplete | None = None):
    """Generates the segmentation corresponding to a RaggedTensor `row_splits`.

  Returns an integer vector `segment_ids`, where `segment_ids[i] == j` if
  `splits[j] <= i < splits[j+1]`.  Example:

  >>> print(tf.ragged.row_splits_to_segment_ids([0, 3, 3, 5, 6, 9]))
   tf.Tensor([0 0 0 2 2 3 4 4 4], shape=(9,), dtype=int64)

  Args:
    splits: A sorted 1-D integer Tensor.  `splits[0]` must be zero.
    name: A name prefix for the returned tensor (optional).
    out_type: The dtype for the return value.  Defaults to `splits.dtype`,
      or `tf.int64` if `splits` does not have a dtype.

  Returns:
    A sorted 1-D integer Tensor, with `shape=[splits[-1]]`

  Raises:
    ValueError: If `splits` is invalid.
  """
def segment_ids_to_row_splits(segment_ids, num_segments: Incomplete | None = None, out_type: Incomplete | None = None, name: Incomplete | None = None):
    """Generates the RaggedTensor `row_splits` corresponding to a segmentation.

  Returns an integer vector `splits`, where `splits[0] = 0` and
  `splits[i] = splits[i-1] + count(segment_ids==i)`.  Example:

  >>> print(tf.ragged.segment_ids_to_row_splits([0, 0, 0, 2, 2, 3, 4, 4, 4]))
  tf.Tensor([0 3 3 5 6 9], shape=(6,), dtype=int64)

  Args:
    segment_ids: A 1-D integer Tensor.
    num_segments: A scalar integer indicating the number of segments.  Defaults
      to `max(segment_ids) + 1` (or zero if `segment_ids` is empty).
    out_type: The dtype for the return value.  Defaults to `segment_ids.dtype`,
      or `tf.int64` if `segment_ids` does not have a dtype.
    name: A name prefix for the returned tensor (optional).

  Returns:
    A sorted 1-D integer Tensor, with `shape=[num_segments + 1]`.
  """
