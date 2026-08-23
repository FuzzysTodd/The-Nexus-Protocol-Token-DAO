from tensorflow.python.data.ops import dataset_ops as dataset_ops
from tensorflow.python.framework import dtypes as dtypes, ops as ops, tensor_spec as tensor_spec
from tensorflow.python.ops import gen_dataset_ops as gen_dataset_ops

class _RangeDataset(dataset_ops.DatasetSource):
    """A `Dataset` of a step separated range of values."""
    def __init__(self, *args, **kwargs) -> None:
        """See `Dataset.range()` for details."""
    @property
    def element_spec(self): ...
