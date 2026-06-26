from _typeshed import Incomplete
from tensorflow.python.data.ops import dataset_ops as dataset_ops, structured_function as structured_function
from tensorflow.python.framework import dtypes as dtypes, tensor_spec as tensor_spec
from tensorflow.python.ops import gen_dataset_ops as gen_dataset_ops

class _FilterDataset(dataset_ops.UnaryUnchangedStructureDataset):
    """A `Dataset` that filters its input according to a predicate function."""
    def __init__(self, input_dataset, predicate, use_legacy_function: bool = False, name: Incomplete | None = None) -> None:
        """See `Dataset.filter` for details."""
