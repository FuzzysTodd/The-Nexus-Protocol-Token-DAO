from _typeshed import Incomplete
from tensorflow.python.data.ops import dataset_ops as dataset_ops
from tensorflow.python.data.util import nest as nest, structure as structure
from tensorflow.python.framework import constant_op as constant_op, dtypes as dtypes, ops as ops, smart_cond as smart_cond, tensor_shape as tensor_shape, tensor_spec as tensor_spec, tensor_util as tensor_util
from tensorflow.python.ops import gen_dataset_ops as gen_dataset_ops

class _PaddedBatchDataset(dataset_ops.UnaryDataset):
    """A `Dataset` that batches and pads contiguous elements from its input."""
    def __init__(self, input_dataset, batch_size, padded_shapes, padding_values, drop_remainder, name: Incomplete | None = None) -> None:
        """See `Dataset.batch()` for details."""
    @property
    def element_spec(self): ...
