from _typeshed import Incomplete
from tensorflow.python.data.ops import dataset_ops as dataset_ops, debug_mode as debug_mode
from tensorflow.python.framework import dtypes as dtypes, ops as ops
from tensorflow.python.ops import gen_dataset_ops as gen_dataset_ops

class _PrefetchDataset(dataset_ops.UnaryUnchangedStructureDataset):
    """A `Dataset` that asynchronously prefetches its input."""
    def __init__(self, input_dataset, buffer_size, slack_period: Incomplete | None = None, name: Incomplete | None = None) -> None:
        """See `Dataset.prefetch()` for details."""
