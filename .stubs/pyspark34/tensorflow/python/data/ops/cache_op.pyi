from _typeshed import Incomplete
from tensorflow.python import tf2 as tf2
from tensorflow.python.data.ops import dataset_ops as dataset_ops
from tensorflow.python.eager import context as context
from tensorflow.python.framework import dtypes as dtypes, ops as ops
from tensorflow.python.ops import gen_dataset_ops as gen_dataset_ops

class CacheDataset(dataset_ops.UnaryUnchangedStructureDataset):
    """A `Dataset` that caches elements of its input."""
    def __init__(self, input_dataset, filename, name: Incomplete | None = None) -> None:
        """See `Dataset.cache()` for details."""
