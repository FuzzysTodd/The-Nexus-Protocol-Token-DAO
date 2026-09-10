from _typeshed import Incomplete
from tensorflow.python.data.ops import dataset_ops as dataset_ops
from tensorflow.python.data.util import nest as nest
from tensorflow.python.ops import gen_dataset_ops as gen_dataset_ops

class _ZipDataset(dataset_ops.DatasetV2):
    """A `Dataset` that zips its inputs together."""
    def __init__(self, datasets, name: Incomplete | None = None) -> None:
        """See `Dataset.zip()` for details."""
    @property
    def element_spec(self): ...
