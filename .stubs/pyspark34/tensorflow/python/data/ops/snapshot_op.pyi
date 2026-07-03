from _typeshed import Incomplete
from tensorflow.python.data.ops import dataset_ops as dataset_ops, structured_function as structured_function
from tensorflow.python.framework import dtypes as dtypes, tensor_spec as tensor_spec

class _SnapshotDataset(dataset_ops.UnaryUnchangedStructureDataset):
    """A dataset that allows saving and re-use of already processed data."""
    def __init__(self, input_dataset, path, shard_func, compression: Incomplete | None = None, reader_func: Incomplete | None = None, pending_snapshot_expiry_seconds: Incomplete | None = None, use_legacy_function: bool = False, name: Incomplete | None = None) -> None: ...
