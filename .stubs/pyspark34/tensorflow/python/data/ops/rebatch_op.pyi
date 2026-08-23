from _typeshed import Incomplete
from tensorflow.python.data.ops import dataset_ops as dataset_ops
from tensorflow.python.data.util import nest as nest
from tensorflow.python.framework import dtypes as dtypes, ops as ops, tensor_shape as tensor_shape, tensor_util as tensor_util

class _RebatchDataset(dataset_ops.UnaryDataset):
    """A `Dataset` that rebatches elements from its input into new batch sizes.

  `_RebatchDataset(input_dataset, batch_sizes)` is functionally equivalent to
  `input_dataset.unbatch().batch(N)`, where the value of N cycles through the
  `batch_sizes` input list. The elements produced by this dataset have the same
  rank as the elements of the input dataset.
  """
    def __init__(self, input_dataset, batch_sizes, drop_remainder: bool = False, name: Incomplete | None = None) -> None:
        """See `Dataset.rebatch` for details."""
    @property
    def element_spec(self): ...
