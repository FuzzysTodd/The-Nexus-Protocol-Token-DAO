from _typeshed import Incomplete
from tensorflow.python.data.ops import dataset_ops as dataset_ops
from tensorflow.python.data.util import nest as nest
from tensorflow.python.framework import tensor_shape as tensor_shape

class _UnbatchDataset(dataset_ops.UnaryDataset):
    """A dataset that splits the elements of its input into multiple elements."""
    def __init__(self, input_dataset, name: Incomplete | None = None) -> None:
        """See `unbatch()` for more details."""
    @property
    def element_spec(self): ...
