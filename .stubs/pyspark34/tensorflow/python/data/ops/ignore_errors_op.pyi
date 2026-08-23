from _typeshed import Incomplete
from tensorflow.python.data.ops import dataset_ops as dataset_ops
from tensorflow.python.ops import gen_experimental_dataset_ops as gen_experimental_dataset_ops

class _IgnoreErrorsDataset(dataset_ops.UnaryUnchangedStructureDataset):
    """A `Dataset` that drops erroneous elements from its input."""
    def __init__(self, input_dataset, log_warning, name: Incomplete | None = None) -> None:
        """See `Dataset.ignore_errors` for details."""
