from _typeshed import Incomplete
from tensorflow.python.data.ops import dataset_ops as dataset_ops, structured_function as structured_function
from tensorflow.python.data.util import nest as nest, structure as structure
from tensorflow.python.framework import ops as ops
from tensorflow.python.util.compat import collections_abc as collections_abc

class _ScanDataset(dataset_ops.UnaryDataset):
    """A dataset that scans a function across its input."""
    def __init__(self, input_dataset, initial_state, scan_func, use_default_device: Incomplete | None = None, name: Incomplete | None = None) -> None:
        """See `scan()` for details."""
    @property
    def element_spec(self): ...
