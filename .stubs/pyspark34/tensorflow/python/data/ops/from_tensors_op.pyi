from _typeshed import Incomplete
from tensorflow.python.data.ops import dataset_ops as dataset_ops
from tensorflow.python.data.util import structure as structure
from tensorflow.python.ops import gen_dataset_ops as gen_dataset_ops

class _TensorDataset(dataset_ops.DatasetSource):
    """A `Dataset` with a single element."""
    def __init__(self, element, name: Incomplete | None = None) -> None:
        """See `tf.data.Dataset.from_tensors` for details."""
    @property
    def element_spec(self): ...
