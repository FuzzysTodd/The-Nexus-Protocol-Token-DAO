from _typeshed import Incomplete
from tensorflow.python.data.ops import dataset_ops as dataset_ops, debug_mode as debug_mode, structured_function as structured_function
from tensorflow.python.framework import dtypes as dtypes, ops as ops
from tensorflow.python.ops import gen_dataset_ops as gen_dataset_ops

class _InterleaveDataset(dataset_ops.UnaryDataset):
    """A `Dataset` that interleaves the result of transformed inputs."""
    def __init__(self, input_dataset, map_func, cycle_length, block_length, name: Incomplete | None = None) -> None:
        """See `Dataset.interleave()` for details."""
    @property
    def element_spec(self): ...

class _ParallelInterleaveDataset(dataset_ops.UnaryDataset):
    """A `Dataset` that maps a function over its input and interleaves the result.
  """
    def __init__(self, input_dataset, map_func, cycle_length, block_length, num_parallel_calls, buffer_output_elements=..., prefetch_input_elements=..., deterministic: Incomplete | None = None, name: Incomplete | None = None) -> None:
        """See `Dataset.interleave()` for details."""
    @property
    def element_spec(self): ...
