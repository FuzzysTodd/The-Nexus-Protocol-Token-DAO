from _typeshed import Incomplete
from tensorflow.python import tf2 as tf2
from tensorflow.python.data.ops import dataset_ops as dataset_ops
from tensorflow.python.data.util import random_seed as random_seed
from tensorflow.python.eager import context as context
from tensorflow.python.framework import dtypes as dtypes, ops as ops
from tensorflow.python.ops import gen_dataset_ops as gen_dataset_ops

class _ShuffleDataset(dataset_ops.UnaryUnchangedStructureDataset):
    """A `Dataset` that randomly shuffles the elements of its input."""
    def __init__(self, input_dataset, buffer_size, seed: Incomplete | None = None, reshuffle_each_iteration: Incomplete | None = None, name: Incomplete | None = None) -> None:
        """See `Dataset.shuffle()` for details."""
