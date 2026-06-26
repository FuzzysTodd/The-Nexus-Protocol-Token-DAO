from _typeshed import Incomplete
from tensorflow.python.data.ops import dataset_ops as dataset_ops
from tensorflow.python.data.util import nest as nest, structure as structure
from tensorflow.python.framework import dtypes as dtypes, ops as ops
from tensorflow.python.ops import gen_dataset_ops as gen_dataset_ops

class _WindowDataset(dataset_ops.UnaryDataset):
    """A dataset that creates window datasets from the input elements."""
    def __init__(self, input_dataset, size, shift, stride, drop_remainder, name: Incomplete | None = None) -> None:
        """See `window()` for more details."""
    @property
    def element_spec(self): ...
