from _typeshed import Incomplete
from tensorflow.python.data.ops import dataset_ops as dataset_ops
from tensorflow.python.data.util import nest as nest
from tensorflow.python.framework import dtypes as dtypes
from tensorflow.python.ops import gen_experimental_dataset_ops as gen_experimental_dataset_ops

class _UniqueDataset(dataset_ops.UnaryUnchangedStructureDataset):
    """A dataset containing the unique elements of an input dataset."""
    def __init__(self, input_dataset, name: Incomplete | None = None) -> None:
        """See `tf.data.Dataset.unique` for details."""
