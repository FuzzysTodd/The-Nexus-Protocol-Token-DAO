from _typeshed import Incomplete
from tensorflow.python.data.ops import dataset_ops as dataset_ops, structured_function as structured_function
from tensorflow.python.framework import dtypes as dtypes, tensor_spec as tensor_spec

class _TakeWhileDataset(dataset_ops.UnaryUnchangedStructureDataset):
    """A dataset that stops iteration when `predicate` returns false."""
    def __init__(self, input_dataset, predicate, name: Incomplete | None = None) -> None:
        """See `take_while()` for details."""
