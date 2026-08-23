from _typeshed import Incomplete
from tensorflow.python.data.ops import dataset_ops as dataset_ops
from tensorflow.python.data.util import nest as nest, structure as structure
from tensorflow.python.framework import tensor_shape as tensor_shape
from tensorflow.python.ops import gen_dataset_ops as gen_dataset_ops

class _TensorSliceDataset(dataset_ops.DatasetSource):
    """A `Dataset` of slices from a dataset element."""
    def __init__(self, element, is_files: bool = False, name: Incomplete | None = None) -> None:
        """See `Dataset.from_tensor_slices` for details."""
    @property
    def element_spec(self): ...
