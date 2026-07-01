from tensorflow.python.data.ops import dataset_ops as dataset_ops
from tensorflow.python.framework import dtypes as dtypes, tensor_spec as tensor_spec
from tensorflow.python.ops import gen_dataset_ops as gen_dataset_ops

class _SparseTensorSliceDataset(dataset_ops.DatasetSource):
    """A `Dataset` that splits a rank-N `tf.sparse.SparseTensor` into its rows."""
    def __init__(self, sparse_tensor) -> None:
        """See `Dataset.from_sparse_tensor_slices()` for details."""
    @property
    def element_spec(self): ...
