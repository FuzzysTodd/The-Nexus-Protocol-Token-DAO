from _typeshed import Incomplete
from tensorflow.python.checkpoint import checkpoint_management as checkpoint_management
from tensorflow.python.data.ops import dataset_ops as dataset_ops, structured_function as structured_function
from tensorflow.python.data.util import structure as structure
from tensorflow.python.eager import context as context
from tensorflow.python.framework import dtypes as dtypes, ops as ops
from tensorflow.python.platform import gfile as gfile
from tensorflow.python.util import lazy_loader as lazy_loader

nested_structure_coder: Incomplete

class _SaveDataset(dataset_ops.UnaryDataset):
    '''"A dataset that loads previously saved dataset.'''
    def __init__(self, dataset, path, shard_func, compression) -> None: ...
    @property
    def element_spec(self): ...

def set_save_dataset_attributes(dataset, shard_func, path):
    """Sets parameters for SaveDatasetOp and SaveDatasetV2Op."""
