from _typeshed import Incomplete
from tensorflow.python import tf2 as tf2
from tensorflow.python.data.ops import dataset_ops as dataset_ops
from tensorflow.python.data.util import random_seed as random_seed
from tensorflow.python.framework import dtypes as dtypes, tensor_spec as tensor_spec
from tensorflow.python.ops import gen_dataset_ops as gen_dataset_ops

class _RandomDataset(dataset_ops.DatasetSource):
    """A `Dataset` of pseudorandom values."""
    def __init__(self, seed: Incomplete | None = None, rerandomize_each_iteration: Incomplete | None = None, name: Incomplete | None = None) -> None:
        """A `Dataset` of pseudorandom values."""
    @property
    def element_spec(self): ...
