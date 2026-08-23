from _typeshed import Incomplete
from tensorflow.python.data.ops import dataset_ops as dataset_ops, debug_mode as debug_mode
from tensorflow.python.data.util import nest as nest
from tensorflow.python.framework import dtypes as dtypes, ops as ops, tensor_util as tensor_util
from tensorflow.python.ops import gen_dataset_ops as gen_dataset_ops

class _BatchDataset(dataset_ops.UnaryDataset):
    """A `Dataset` that batches contiguous elements from its input."""
    def __init__(self, input_dataset, batch_size, drop_remainder, name: Incomplete | None = None) -> None:
        """See `Dataset.batch()` for details."""
    @property
    def element_spec(self): ...

class _ParallelBatchDataset(dataset_ops.UnaryDataset):
    """A `Dataset` that batches contiguous elements from its input in parallel."""
    def __init__(self, input_dataset, batch_size, drop_remainder, num_parallel_calls, deterministic, name: Incomplete | None = None) -> None:
        """See `Dataset.batch()` for details."""
    @property
    def element_spec(self): ...
