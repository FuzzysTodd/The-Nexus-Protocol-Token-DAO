from tensorflow.python.data.ops import dataset_ops as dataset_ops
from tensorflow.python.data.util import nest as nest

class _DirectedInterleaveDataset(dataset_ops.DatasetV2):
    """A substitute for `Dataset.interleave()` on a fixed list of datasets."""
    def __init__(self, selector_input, data_inputs, stop_on_empty_dataset: bool = False) -> None: ...
    @property
    def element_spec(self): ...
