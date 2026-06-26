from _typeshed import Incomplete
from tensorflow.python.data.ops import dataset_ops as dataset_ops, structured_function as structured_function
from tensorflow.python.data.util import nest as nest
from tensorflow.python.framework import dtypes as dtypes, ops as ops, tensor_spec as tensor_spec
from tensorflow.python.ops.ragged import ragged_tensor as ragged_tensor

class _DenseToRaggedDataset(dataset_ops.UnaryDataset):
    """A `Dataset` that encodes dense inputs as ragged (w/ ragged_rank=0).

  In particular:

  * Any tf.Tensor elements with rank>0 are encoded as ragged tensors with
    ragged_rank=0.  This allows tensors with varying shape to be batched
    together.
  * Any other elements are left as-is.
  """
    def __init__(self, input_dataset, row_splits_dtype, name: Incomplete | None = None) -> None:
        """Constructs a new _DenseToRaggedDataset.

    Args:
      input_dataset: The dataset whose tf.Tensor elements should be made ragged.
      row_splits_dtype: The dtype that should be used for the `row_splits` of
        any new ragged tensors.  Existing `tf.RaggedTensor` elements do *not*
        have their row_splits dtype changed.
      name: (Optional.) A string indicating a name for the `tf.data` operation.
    """
    @property
    def element_spec(self): ...
