from _typeshed import Incomplete
from tensorflow.python.data.ops import dataset_ops as dataset_ops, debug_mode as debug_mode, structured_function as structured_function
from tensorflow.python.framework import dtypes as dtypes, ops as ops
from tensorflow.python.ops import gen_dataset_ops as gen_dataset_ops

class _MapDataset(dataset_ops.UnaryDataset):
    """A `Dataset` that maps a function over elements in its input."""
    def __init__(self, input_dataset, map_func, use_inter_op_parallelism: bool = True, preserve_cardinality: bool = True, use_legacy_function: bool = False, name: Incomplete | None = None) -> None: ...
    @property
    def element_spec(self): ...

class _ParallelMapDataset(dataset_ops.UnaryDataset):
    """A `Dataset` that maps a function over elements in its input in parallel."""
    def __init__(self, input_dataset, map_func, num_parallel_calls, deterministic, use_inter_op_parallelism: bool = True, preserve_cardinality: bool = False, use_legacy_function: bool = False, name: Incomplete | None = None) -> None:
        """See `Dataset.map()` for details."""
    @property
    def element_spec(self): ...
