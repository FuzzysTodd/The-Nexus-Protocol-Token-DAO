from _typeshed import Incomplete
from tensorflow.python.data.ops import dataset_ops as dataset_ops, structured_function as structured_function
from tensorflow.python.framework import dtypes as dtypes, ops as ops, tensor_spec as tensor_spec

class _GroupByWindowDataset(dataset_ops.UnaryDataset):
    """A `Dataset` that groups its input and performs a windowed reduction."""
    def __init__(self, input_dataset, key_func, reduce_func, window_size_func, name: Incomplete | None = None) -> None:
        """See `group_by_window()` for details."""
    @property
    def element_spec(self): ...
