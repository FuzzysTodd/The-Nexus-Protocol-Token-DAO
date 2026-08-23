from _typeshed import Incomplete
from tensorflow.python.data.ops import dataset_ops as dataset_ops
from tensorflow.python.data.util import convert as convert
from tensorflow.python.framework import dtypes as dtypes, sparse_tensor as sparse_tensor, tensor_shape as tensor_shape

class _DenseToSparseBatchDataset(dataset_ops.UnaryDataset):
    """A `Dataset` that batches ragged dense elements into `tf.sparse.SparseTensor`s."""
    def __init__(self, input_dataset, batch_size, row_shape, name: Incomplete | None = None) -> None:
        """See `Dataset.dense_to_sparse_batch()` for more details."""
    @property
    def element_spec(self): ...
