from _typeshed import Incomplete
from tensorflow.python.data.ops import dataset_ops as dataset_ops
from tensorflow.python.ops import gen_dataset_ops as gen_dataset_ops

class _ConcatenateDataset(dataset_ops.DatasetV2):
    """A `Dataset` that concatenates its input with given dataset."""
    def __init__(self, input_dataset, dataset_to_concatenate, name: Incomplete | None = None) -> None:
        """See `Dataset.concatenate()` for details."""
    @property
    def element_spec(self): ...
