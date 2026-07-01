from _typeshed import Incomplete
from tensorflow.python.data.ops import dataset_ops as dataset_ops
from tensorflow.python.framework import constant_op as constant_op, dtypes as dtypes, ops as ops
from tensorflow.python.ops import gen_dataset_ops as gen_dataset_ops

class _RepeatDataset(dataset_ops.UnaryUnchangedStructureDataset):
    """A `Dataset` that repeats its input several times."""
    def __init__(self, input_dataset, count, name: Incomplete | None = None) -> None:
        """See `Dataset.repeat()` for details."""
