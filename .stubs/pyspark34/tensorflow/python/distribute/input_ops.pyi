from _typeshed import Incomplete
from tensorflow.python.data.experimental.ops import distribute as distribute
from tensorflow.python.data.ops import dataset_ops as dataset_ops
from tensorflow.python.data.ops.options import AutoShardPolicy as AutoShardPolicy
from tensorflow.python.data.util import traverse as traverse
from tensorflow.python.framework import op_def_registry as op_def_registry, ops as ops

def auto_shard_dataset(dataset, num_shards, index, num_replicas_in_sync: Incomplete | None = None):
    """Shard the input pipeline by sharding the underlying list of files.

  Args:
    dataset: A `tf.data.Dataset` instance, typically the result of a bunch of
      dataset transformations.
    num_shards: A `tf.int64` scalar `tf.Tensor`, representing the number of
        shards operating in parallel. Same usage as in `tf.data.Dataset.shard`.
    index: A `tf.int64` scalar `tf.Tensor`, representing the worker index.
      Same usage as in `tf.data.Dataset.shard`.
    num_replicas_in_sync: An integer representing the total number of replicas
      across all workers. This is used in the rewrite when sharding by data.

  Returns:
    A modified `Dataset` obtained by updating the pipeline sharded by the
    files. The input dataset will be returned if we cannot automatically
    determine a good way to shard the input dataset.
  """
