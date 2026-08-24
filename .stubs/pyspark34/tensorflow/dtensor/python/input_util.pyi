import dataclasses
from tensorflow.dtensor.python import api as api, config as config, layout as layout_lib
from tensorflow.python.data.experimental.ops import data_service_ops as data_service_ops
from tensorflow.python.data.ops import dataset_ops as dataset_ops, iterator_ops as iterator_ops
from tensorflow.python.framework import constant_op as constant_op, dtypes as dtypes, errors as errors, ops as ops, tensor_spec as tensor_spec
from tensorflow.python.ops import array_ops as array_ops, math_ops as math_ops
from tensorflow.python.util import nest as nest
from tensorflow.python.util.tf_export import tf_export as tf_export
from typing import Any, Optional, Sequence, Tuple

@dataclasses.dataclass
class TFDataServiceConfig:
    """Specifies the tf.data service configuration to use.

  Attributes:
    dispatcher_address: a string specifying the address of the tf.data service
      dispatcher server.
    job_name: a non-empty string identifying the shared job that will be created
      on tf.data service to process this dataset.
  """
    dispatcher_address: str
    job_name: str
    def __init__(self, dispatcher_address, job_name) -> None: ...

class _DTensorIterator(iterator_ops.IteratorBase):
    """An iterator for a tf.data.Dataset distributed using DTensor.

  DTensorIterator encapsulates multiple underlying dataset iterators. It handles
  retrieving the tensors to be placed on each underlying device and then uses
  the 'pack' operation to create and return a DTensor. Thus users need only
  interact with a single DTensorIterator to automatically distribute dataset
  tensors onto devices.
  """
    def __init__(self, datasets: Sequence[Tuple[int, dataset_ops.DatasetV2]], element_spec: tensor_spec.TensorSpec, layouts: Any, num_local_devices_per_replica: int) -> None:
        """Initializes a distributed iterator for DTensor datasets.

    The DTensorIterator uses 'replica IDs' to identify shards of a dataset. Here
    the term 'replica' is used in the data-parallel context where each replica
    receives a partition of the global batch. Depending on the model parallelism
    in the layouts supplied, each device within that replica may receive the
    same partition of the global batch (no model parallelism), or specific
    slices of that partition.

    Args:
      datasets: a dictionary mapping each unique local replica ID to the dataset
        object whose elements will be placed on the devices corresponding to
        that replica.
      element_spec: the underlying dataset's element spec.
      layouts: a structure of DTensor layouts to be applied to the dataset
        values. This can be a single layout or (possibly nested) tuples or
        dictionaries of layouts, and the structure must match the structure of
        the dataset.
      num_local_devices_per_replica: the number of local devices for each
        replica.
    """
    def __next__(self): ...
    def __iter__(self): ...
    @property
    def element_spec(self):
        """The type specification of an element of this iterator.

    A possibly nested structure of `tf.TypeSpec` objects matching the structure
    of an element of this iterator.
    """
    def get_next(self):
        """Returns the next element.

    Returns:
      A possibly nested structure of values matching
      `tf.data.Iterator.element_spec`.

    Raises:
      `tf.errors.OutOfRangeError`: if the end of the underlying iterators has
        been reached.
      RuntimeError: if any of the underlying iterators do not return the
        expected number of items.
    """
    def get_next_as_optional(self) -> None:
        """Returns the next element wrapped in `tf.experimental.Optional`.

    If the iterator has reached the end of the sequence, the returned
    `tf.experimental.Optional` will have no value.

    Returns:
      A `tf.experimental.Optional` object representing the next element.
    """

class DTensorDataset(dataset_ops.UnaryUnchangedStructureDataset):
    """A dataset of DTensors.

  DTensorDataset encapsulates a `tf.data.Dataset` whose elements are
  automatically packed and returned as DTensors based on a given mesh and
  layouts.
  """
    def __init__(self, dataset: dataset_ops.DatasetV2, *, mesh: layout_lib.Mesh, layouts: Any, global_batch_size: int, dataset_already_batched: bool = False, batch_dim: Optional[str] = None, prefetch: Optional[int] = None, tf_data_service_config: Optional[TFDataServiceConfig] = None) -> None:
        """Creates a DTensorDataset.

    DTensorDataset automatically handles distribution of the dataset elements to
    each client's devices. It can be used to create an iterator that returns
    DTensors of the input data on each iteration.

    DTensorDataset works best with unbatched datasets. It takes the mesh and the
    provided layouts to automatically calculate how to batch the input locally
    for each replica.

    If the provided dataset is already batched according to the per-replica
    batch size, then `dataset_already_batched` must be set and DTensorDataset
    will check that the batch size is consistent with the intended
    `global_batch_size` using the layout information. Each replica receives a
    separate slice of the global batch, thus the per-replica batch size can be
    computed as the global batch size divided by the number of model replicas.
    For a DTensor mesh, the number of replicas is equal to the size of the
    mesh's batch dimension.

    TODO(b/223275517): add support for input datasets that are already batched
    to the global batch size.

    Args:
      dataset: a `tf.data.Dataset` object.
      mesh: the DTensor mesh to place the dataset batches on.
      layouts: a structure of DTensor layouts to be applied to the input dataset
        values. This can be a single layout or (possibly nested) tuples or
        dictionaries of layouts, and the structure must match the structure of
        the dataset. Either all or none of the layouts should be sharded on the
        batch dimension; having only a subset of layouts batch sharded will not
        work and raises a ValueError.
      global_batch_size: the desired global batch size.
      dataset_already_batched: must be set only if the dataset is already
        batched to the per-replica batch size. The batched dataset must have
        `drop_remainder=True` set since DTensor requires static shapes for
        slicing the input tensors.
      batch_dim: the mesh dimension on which the input's batch dimension is
        sharded. Set to None if the input layouts do not shard on the batch
        dimension.
      prefetch: number of batches to prefetch using Dataset.prefetch.
      tf_data_service_config: if operating in multi-client mode, this config
        specifies the tf.data service configuration to use.

    Raises:
      ValueError: on any of the following situations,
        1. if the structures and ranks of layouts and the dataset do not match.
        2. if the shapes in the dataset's spec are not fully defined.
        3. if batch_dim is specified and all layouts are not batch-sharded.
        4. if per_replica_batch_size is specified for an already batched Dataset
           but it does not match the expected per-replica size based on the
           provided mesh.
      TypeError: if type of structures of layouts and the dataset do not match.
    """
    def __iter__(self): ...
