from _typeshed import Incomplete
from tensorflow.core.protobuf import snapshot_pb2 as snapshot_pb2
from tensorflow.python.eager import context as context
from tensorflow.python.ops import gen_experimental_dataset_ops as gen_experimental_dataset_ops
from tensorflow.python.util import lazy_loader as lazy_loader

nested_structure_coder: Incomplete

def distributed_save(dataset, directory, dispatcher_address, compression: str = 'AUTO'):
    '''Initiates the process of distributedly saving a dataset to disk.

  Args:
    dataset: The `tf.data.Dataset` to save.
    directory: A string indicating the directory to which to save `dataset`.
    dispatcher_address: A string indicating the address of the dispatcher for
      the tf.data service instance used to save `dataset`.
    compression: (Optional.) A string indicating whether and how to compress the
      `dataset` materialization.  If `"AUTO"`, the tf.data runtime decides which
      algorithm to use.  If `"GZIP"` or `"SNAPPY"`, that specific algorithm is
      used.  If `None`, the `dataset` materialization is not compressed.

  Returns:
    `None`.

  Raises:
    ValueError: If not in eager mode.
  '''
