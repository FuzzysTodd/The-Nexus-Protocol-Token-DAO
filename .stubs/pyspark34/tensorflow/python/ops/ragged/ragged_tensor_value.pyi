from _typeshed import Incomplete
from tensorflow.python.ops.ragged.row_partition import RowPartition as RowPartition
from tensorflow.python.util import dispatch as dispatch
from tensorflow.python.util.tf_export import tf_export as tf_export

class RaggedTensorValue:
    """Represents the value of a `RaggedTensor`.

  Warning: `RaggedTensorValue` should only be used in graph mode; in
  eager mode, the `tf.RaggedTensor` class contains its value directly.

  See `tf.RaggedTensor` for a description of ragged tensors.
  """
    def __init__(self, values, row_splits) -> None:
        """Creates a `RaggedTensorValue`.

    Args:
      values: A numpy array of any type and shape; or a RaggedTensorValue.
      row_splits: A 1-D int32 or int64 numpy array.
    """
    row_splits: Incomplete
    values: Incomplete
    dtype: Incomplete
    @property
    def flat_values(self):
        """The innermost `values` array for this ragged tensor value."""
    @property
    def nested_row_splits(self):
        """The row_splits for all ragged dimensions in this ragged tensor value."""
    @property
    def ragged_rank(self):
        """The number of ragged dimensions in this ragged tensor value."""
    @property
    def shape(self):
        """A tuple indicating the shape of this RaggedTensorValue."""
    def to_list(self):
        """Returns this ragged tensor value as a nested Python list."""
