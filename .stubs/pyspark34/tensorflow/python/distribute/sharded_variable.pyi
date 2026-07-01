from _typeshed import Incomplete
from tensorflow.python.framework import composite_tensor as composite_tensor, constant_op as constant_op, dtypes as dtypes, ops as ops, tensor_conversion_registry as tensor_conversion_registry, tensor_shape as tensor_shape, type_spec as type_spec
from tensorflow.python.ops import array_ops as array_ops, data_flow_ops as data_flow_ops, embedding_ops as embedding_ops, math_ops as math_ops, partitioned_variables as partitioned_variables, resource_variable_ops as resource_variable_ops
from tensorflow.python.saved_model import save_context as save_context
from tensorflow.python.trackable import base as trackable
from tensorflow.python.training.saving import saveable_object_util as saveable_object_util
from tensorflow.python.util import dispatch as dispatch
from tensorflow.python.util.tf_export import tf_export as tf_export

class Partitioner:
    """Partitioner base class: all partitiners inherit from this class.

  Partitioners should implement a `__call__` method with the following
  signature:

  ```python
  def __call__(self, shape, dtype, axis=0):
    # Partitions the given `shape` and returns the partition results.
    # See docstring of `__call__` method for the format of partition results.
  ```
  """
    def __call__(self, shape, dtype, axis: int = 0) -> None:
        """Partitions the given `shape` and returns the partition results.

    Examples of a partitioner that allocates a fixed number of shards:

    ```python
    partitioner = FixedShardsPartitioner(num_shards=2)
    partitions = partitioner(tf.TensorShape([10, 3], tf.float32), axis=0)
    print(partitions) # [2, 0]
    ```

    Args:
      shape: a `tf.TensorShape`, the shape to partition.
      dtype: a `tf.dtypes.Dtype` indicating the type of the partition value.
      axis: The axis to partition along.  Default: outermost axis.

    Returns:
      A list of integers representing the number of partitions on each axis,
      where i-th value correponds to i-th axis.
    """

class FixedShardsPartitioner(Partitioner):
    """Partitioner that allocates a fixed number of shards.

  Examples:

  >>> # standalone usage:
  >>> partitioner = FixedShardsPartitioner(num_shards=2)
  >>> partitions = partitioner(tf.TensorShape([10, 3]), tf.float32)
  >>> [2, 1]
  >>>
  >>> # use in ParameterServerStrategy
  >>> # strategy = tf.distribute.experimental.ParameterServerStrategy(
  >>> #   cluster_resolver=cluster_resolver, variable_partitioner=partitioner)

  """
    def __init__(self, num_shards) -> None:
        """Creates a new `FixedShardsPartitioner`.

    Args:
      num_shards: `int`, number of shards to partition.
    """
    def __call__(self, shape, dtype, axis: int = 0): ...

class MinSizePartitioner(Partitioner):
    """Partitioner that allocates a minimum size per shard.

  This partitioner ensures each shard has at least `min_shard_bytes`, and tries
  to allocate as many shards as possible, i.e., keeping shard size as small as
  possible. The maximum number of such shards (upper bound) is given by
  `max_shards`.

  Examples:

  >>> partitioner = MinSizePartitioner(min_shard_bytes=4, max_shards=2)
  >>> partitions = partitioner(tf.TensorShape([6, 1]), tf.float32)
  >>> [2, 1]
  >>> partitioner = MinSizePartitioner(min_shard_bytes=4, max_shards=10)
  >>> partitions = partitioner(tf.TensorShape([6, 1]), tf.float32)
  >>> [6, 1]
  >>>
  >>> # use in ParameterServerStrategy
  >>> # strategy = tf.distribute.experimental.ParameterServerStrategy(
  >>> #   cluster_resolver=cluster_resolver, variable_partitioner=partitioner)
  """
    def __init__(self, min_shard_bytes=..., max_shards: int = 1, bytes_per_string: int = 16) -> None:
        """Creates a new `MinSizePartitioner`.

    Args:
      min_shard_bytes: Minimum bytes of each shard. Defaults to 256K.
      max_shards: Upper bound on the number of shards. Defaults to 1.
      bytes_per_string: If the partition value is of type string, this provides
        an estimate of how large each string is.
    """
    def __call__(self, shape, dtype, axis: int = 0): ...

class MaxSizePartitioner(Partitioner):
    """Partitioner that keeps shards below `max_shard_bytes`.

  This partitioner ensures each shard has at most `max_shard_bytes`, and tries
  to allocate as few shards as possible, i.e., keeping shard size as large
  as possible.

  If the partitioner hits the `max_shards` limit, then each shard may end up
  larger than `max_shard_bytes`. By default `max_shards` equals `None` and no
  limit on the number of shards is enforced.

  Examples:

  >>> partitioner = MaxSizePartitioner(max_shard_bytes=4)
  >>> partitions = partitioner(tf.TensorShape([6, 1]), tf.float32)
  >>> [6, 1]
  >>> partitioner = MaxSizePartitioner(max_shard_bytes=4, max_shards=2)
  >>> partitions = partitioner(tf.TensorShape([6, 1]), tf.float32)
  >>> [2, 1]
  >>> partitioner = MaxSizePartitioner(max_shard_bytes=1024)
  >>> partitions = partitioner(tf.TensorShape([6, 1]), tf.float32)
  >>> [1, 1]
  >>>
  >>> # use in ParameterServerStrategy
  >>> # strategy = tf.distribute.experimental.ParameterServerStrategy(
  >>> #   cluster_resolver=cluster_resolver, variable_partitioner=partitioner)
  """
    def __init__(self, max_shard_bytes, max_shards: Incomplete | None = None, bytes_per_string: int = 16) -> None:
        """Creates a new `MaxSizePartitioner`.

    Args:
      max_shard_bytes: The maximum size any given shard is allowed to be.
      max_shards: The maximum number of shards in `int` created taking
        precedence over `max_shard_bytes`.
      bytes_per_string: If the partition value is of type string, this provides
        an estimate of how large each string is.
    """
    def __call__(self, shape, dtype, axis: int = 0): ...

class ShardedVariableSpec(type_spec.TypeSpec):
    """Type specification for a `ShardedVariable`."""
    value_type: Incomplete
    def __init__(self, *variable_specs) -> None: ...

class ShardedVariableMixin(trackable.Trackable):
    """Mixin for ShardedVariable."""
    def __init__(self, variables, name: str = 'ShardedVariable') -> None:
        '''Treats `variables` as shards of a larger Variable.


    Example:

    ```
    variables = [
      tf.Variable(..., shape=(10, 100), dtype=tf.float32),
      tf.Variable(..., shape=(15, 100), dtype=tf.float32),
      tf.Variable(..., shape=(5, 100), dtype=tf.float32)
    ]
    sharded_variable = ShardedVariableMixin(variables)
    assert sharded_variable.shape.as_list() == [30, 100]
    ```

    Args:
      variables: A list of `ResourceVariable`s that comprise this sharded
        variable. Variables should not be shared between different
        `ShardedVariableMixin` objects.
      name: String. Name of this container. Defaults to "ShardedVariable".
    '''
    def __iter__(self):
        """Return an iterable for accessing the underlying sharded variables."""
    def __getitem__(self, slice_spec):
        """Extracts the specified region as a Tensor from the sharded variable.

    The API contract is identical to `Tensor.__getitem__`. Assignment to the
    sliced range is not yet supported.

    Args:
      slice_spec: The arguments to __getitem__, specifying the global slicing of
        the sharded variable.

    Returns:
      The appropriate slice of tensor based on `slice_spec`.

    Raises:
      IndexError: If a slice index is out of bound.
      TypeError: If `spec_spec` contains Tensor.
    """
    @property
    def variables(self):
        """The list of `Variable`s that make up the shards of this object."""
    @property
    def name(self):
        """The name of this object. Used for checkpointing."""
    @property
    def dtype(self):
        """The dtype of all `Variable`s in this object."""
    @property
    def shape(self):
        """The overall shape, combining all shards along axis `0`."""
    def assign(self, value, use_locking: Incomplete | None = None, name: Incomplete | None = None, read_value: bool = True): ...
    def assign_add(self, delta, use_locking: bool = False, name: Incomplete | None = None, read_value: bool = True): ...
    def assign_sub(self, delta, use_locking: bool = False, name: Incomplete | None = None, read_value: bool = True): ...
    def scatter_add(self, sparse_delta, use_locking: bool = False, name: Incomplete | None = None):
        """Implements tf.Variable.scatter_add."""
    def scatter_div(self, sparse_delta, use_locking: bool = False, name: Incomplete | None = None):
        """Implements tf.Variable.scatter_div."""
    def scatter_max(self, sparse_delta, use_locking: bool = False, name: Incomplete | None = None):
        """Implements tf.Variable.scatter_max."""
    def scatter_min(self, sparse_delta, use_locking: bool = False, name: Incomplete | None = None):
        """Implements tf.Variable.scatter_min."""
    def scatter_mul(self, sparse_delta, use_locking: bool = False, name: Incomplete | None = None):
        """Implements tf.Variable.scatter_mul."""
    def scatter_sub(self, sparse_delta, use_locking: bool = False, name: Incomplete | None = None):
        """Implements tf.Variable.scatter_sub."""
    def scatter_update(self, sparse_delta, use_locking: bool = False, name: Incomplete | None = None):
        """Implements tf.Variable.scatter_update."""
    def batch_scatter_update(self, sparse_delta, use_locking: bool = False, name: Incomplete | None = None):
        """Implements tf.Variable.batch_scatter_update."""
    def sparse_read(self, indices, name: Incomplete | None = None):
        """Implements tf.Variable.sparse_read."""
    @property
    def is_sharded_variable(self): ...
    def numpy(self):
        """Copies the values in this ShardedVariable to a NumPy array.

    First converts to a single Tensor using the registered conversion function,
    which concatenates the shards, then uses Tensor.numpy() to convert to
    a NumPy array.

    Returns:
      A NumPy array of the same shape and dtype.
    """

class ShardedVariable(ShardedVariableMixin, composite_tensor.CompositeTensor):
    """A container for `Variables` that should be treated as shards.

  Variables that are too large to fit on a single device (e.g., large
  embeddings)
  may need to be sharded over multiple devices. This class maintains a list of
  smaller variables that can be independently stored on separate devices (eg,
  multiple parameter servers), and saves and restores those variables as if they
  were a single larger variable.

  Objects of this class can be saved with a given number of shards and then
  restored from a checkpoint into a different number of shards.

  Objects of this class can be saved to SavedModel format using
  `tf.saved_model.save`. The SavedModel can be used by programs like TF serving
  APIs. It is not yet supported to load the SavedModel with
  `tf.saved_model.load`.

  Since `ShardedVariable` can be saved and then restored to different number of
  shards depending on the restore environments, for example, TF serving APIs
  would restore to one shard for serving efficiency, when using
  `ShardedVariable` in a tf.function, one should generally not assume it has the
  same number of shards across save and load.

  Sharding is only supported along the first dimension.

  >>> class Model(tf.Module):
  ...   def __init__(self):
  ...     self.sharded_variable = ShardedVariable([
  ...       tf.Variable([3.0], dtype=tf.float32),
  ...       tf.Variable([2.0], dtype=tf.float32)
  ...     ])
  ...
  ...   @tf.function(input_signature=[tf.TensorSpec([], dtype=tf.int32)])
  ...   def fn(self, x):
  ...     return tf.nn.embedding_lookup(self.sharded_variable.variables, x)
  ...
  ...   @tf.function(input_signature=[tf.TensorSpec([], dtype=tf.int32)])
  ...   def serve_fn(self, x):
  ...     return tf.nn.embedding_lookup(self.sharded_variable.variables, x)
  >>>
  >>> model = Model()
  >>> model.fn(1).numpy()
  2.0
  >>> tf.saved_model.save(model, export_dir='/tmp/saved_model',
  ...   signatures=model.serve_fn)
  """
    def __tf_experimental_restore_capture__(self, concrete_function, internal_capture) -> None: ...

def embedding_lookup(params, ids, partition_strategy: str = 'mod', name: Incomplete | None = None, validate_indices: bool = True, max_norm: Incomplete | None = None): ...
