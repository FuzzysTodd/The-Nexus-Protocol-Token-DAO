from _typeshed import Incomplete
from tensorflow.python.data.ops import dataset_ops as dataset_ops, structured_function as structured_function
from tensorflow.python.ops import gen_dataset_ops as gen_dataset_ops

class _FlatMapDataset(dataset_ops.UnaryDataset):
    """A `Dataset` that maps a function over its input and flattens the result."""
    def __init__(self, input_dataset, map_func, name: Incomplete | None = None) -> None: ...
    @property
    def element_spec(self): ...
