from _typeshed import Incomplete
from tensorflow.python.data.ops import dataset_ops as dataset_ops, structured_function as structured_function
from tensorflow.python.eager import context as context
from tensorflow.python.platform import gfile as gfile
from tensorflow.python.util import lazy_loader as lazy_loader

nested_structure_coder: Incomplete

class _LoadDataset(dataset_ops.DatasetSource):
    """A dataset that loads previously saved dataset."""
    def __init__(self, path, element_spec: Incomplete | None = None, compression: Incomplete | None = None, reader_func: Incomplete | None = None) -> None: ...
    @property
    def element_spec(self): ...
