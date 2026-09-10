from tensorflow.python.data.ops import dataset_ops as dataset_ops
from tensorflow.python.framework import dtypes as dtypes, ops as ops
from tensorflow.python.ops import gen_dataset_ops as gen_dataset_ops

class _ShardDataset(dataset_ops.UnaryUnchangedStructureDataset):
    """A `Dataset` for sharding its input."""
    def __init__(self, input_dataset, num_shards, index, name) -> None:
        """See `Dataset.shard()` for details."""
