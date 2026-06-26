from _typeshed import Incomplete
from tensorflow.python.data.ops import dataset_ops as dataset_ops
from tensorflow.python.framework import dtypes as dtypes, ops as ops
from tensorflow.python.ops import gen_dataset_ops as gen_dataset_ops

class _SkipDataset(dataset_ops.UnaryUnchangedStructureDataset):
    """A `Dataset` skipping the first `count` elements from its input."""
    def __init__(self, input_dataset, count, name: Incomplete | None = None) -> None:
        """See `Dataset.skip()` for details."""
