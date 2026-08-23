from _typeshed import Incomplete
from tensorflow.python import tf2 as tf2
from tensorflow.python.data.ops import dataset_ops as dataset_ops, random_op as random_op
from tensorflow.python.util import deprecation as deprecation
from tensorflow.python.util.tf_export import tf_export as tf_export

class RandomDatasetV2(random_op._RandomDataset):
    """A `Dataset` of pseudorandom values."""

class RandomDatasetV1(dataset_ops.DatasetV1Adapter):
    """A `Dataset` of pseudorandom values."""
    def __init__(self, seed: Incomplete | None = None) -> None: ...
RandomDataset = RandomDatasetV2
RandomDataset = RandomDatasetV1
