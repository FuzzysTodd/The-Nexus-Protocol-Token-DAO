from _typeshed import Incomplete
from collections.abc import Generator
from tensorflow.python.compiler.xla.experimental import xla_sharding as xla_sharding
from tensorflow.python.distribute import device_util as device_util, distribute_lib as distribute_lib, distribute_utils as distribute_utils, input_lib as input_lib, input_util as input_util, numpy_dataset as numpy_dataset, reduce_util as reduce_util, tpu_replicated_variable as tpu_replicated_variable, tpu_util as tpu_util, tpu_values as tpu_values, values as values
from tensorflow.python.distribute.cluster_resolver import TPUClusterResolver as TPUClusterResolver
from tensorflow.python.eager import context as context, def_function as def_function, function as function
from tensorflow.python.framework import constant_op as constant_op, device_spec as device_spec, dtypes as dtypes, indexed_slices as indexed_slices, ops as ops, sparse_tensor as sparse_tensor, tensor_shape as tensor_shape, tensor_util as tensor_util
from tensorflow.python.ops import array_ops as array_ops, control_flow_ops as control_flow_ops, math_ops as math_ops, resource_variable_ops as resource_variable_ops
from tensorflow.python.ops.ragged import ragged_tensor as ragged_tensor
from tensorflow.python.tpu import tpu as tpu, tpu_hardware_feature as tpu_hardware_feature, tpu_strategy_util as tpu_strategy_util, training_loop as training_loop
from tensorflow.python.tpu.ops import tpu_ops as tpu_ops
from tensorflow.python.util import deprecation as deprecation, nest as nest, tf_inspect as tf_inspect
from tensorflow.python.util.tf_export import tf_export as tf_export

def maybe_init_scope() -> Generator[None, None, None]: ...
def validate_run_function(fn) -> None:
    """Validate the function passed into strategy.run."""

class TPUStrategyV2(distribute_lib.Strategy):
    """Synchronous training on TPUs and TPU Pods.

  To construct a TPUStrategy object, you need to run the
  initialization code as below:

  >>> resolver = tf.distribute.cluster_resolver.TPUClusterResolver(tpu='')
  >>> tf.config.experimental_connect_to_cluster(resolver)
  >>> tf.tpu.experimental.initialize_tpu_system(resolver)
  >>> strategy = tf.distribute.TPUStrategy(resolver)

  While using distribution strategies, the variables created within the
  strategy's scope will be replicated across all the replicas and can be kept in
  sync using all-reduce algorithms.

  To run TF2 programs on TPUs, you can either use `.compile` and
  `.fit` APIs in `tf.keras` with TPUStrategy, or write your own customized
  training loop by calling `strategy.run` directly. Note that
  TPUStrategy doesn't support pure eager execution, so please make sure the
  function passed into `strategy.run` is a `tf.function` or
  `strategy.run` is called inside a `tf.function` if eager
  behavior is enabled. See more details in https://www.tensorflow.org/guide/tpu.

  `distribute_datasets_from_function` and
  `experimental_distribute_dataset` APIs can be used to distribute the dataset
  across the TPU workers when writing your own training loop. If you are using
  `fit` and `compile` methods available in `tf.keras.Model`, then Keras will
  handle the distribution for you.

  An example of writing customized training loop on TPUs:

  >>> with strategy.scope():
  ...   model = tf.keras.Sequential([
  ...     tf.keras.layers.Dense(2, input_shape=(5,)),
  ...   ])
  ...   optimizer = tf.keras.optimizers.SGD(learning_rate=0.1)

  >>> def dataset_fn(ctx):
  ...   x = np.random.random((2, 5)).astype(np.float32)
  ...   y = np.random.randint(2, size=(2, 1))
  ...   dataset = tf.data.Dataset.from_tensor_slices((x, y))
  ...   return dataset.repeat().batch(1, drop_remainder=True)
  >>> dist_dataset = strategy.distribute_datasets_from_function(
  ...     dataset_fn)
  >>> iterator = iter(dist_dataset)

  >>> @tf.function()
  ... def train_step(iterator):
  ...
  ...   def step_fn(inputs):
  ...     features, labels = inputs
  ...     with tf.GradientTape() as tape:
  ...       logits = model(features, training=True)
  ...       loss = tf.keras.losses.sparse_categorical_crossentropy(
  ...           labels, logits)
  ...
  ...     grads = tape.gradient(loss, model.trainable_variables)
  ...     optimizer.apply_gradients(zip(grads, model.trainable_variables))
  ...
  ...   strategy.run(step_fn, args=(next(iterator),))

  >>> train_step(iterator)

  For the advanced use cases like model parallelism, you can set
  `experimental_device_assignment` argument when creating TPUStrategy to specify
  number of replicas and number of logical devices. Below is an example to
  initialize TPU system with 2 logical devices and 1 replica.

  >>> resolver = tf.distribute.cluster_resolver.TPUClusterResolver(tpu='')
  >>> tf.config.experimental_connect_to_cluster(resolver)
  >>> topology = tf.tpu.experimental.initialize_tpu_system(resolver)
  >>> device_assignment = tf.tpu.experimental.DeviceAssignment.build(
  ...     topology,
  ...     computation_shape=[1, 1, 1, 2],
  ...     num_replicas=1)
  >>> strategy = tf.distribute.TPUStrategy(
  ...     resolver, experimental_device_assignment=device_assignment)

  Then you can run a `tf.add` operation only on logical device 0.

  >>> @tf.function()
  ... def step_fn(inputs):
  ...   features, _ = inputs
  ...   output = tf.add(features, features)
  ...
  ...   # Add operation will be executed on logical device 0.
  ...   output = strategy.experimental_assign_to_logical_device(output, 0)
  ...   return output
  >>> dist_dataset = strategy.distribute_datasets_from_function(
  ...     dataset_fn)
  >>> iterator = iter(dist_dataset)
  >>> strategy.run(step_fn, args=(next(iterator),))

  `experimental_spmd_xla_partitioning` enables the experimental XLA SPMD feature
  for model parallelism. This flag can reduce the compilation time and HBM
  requirements. When running in this mode, every input tensor must either be
  partitioned (via `strategy.experimental_split_to_logical_devices`) or fully
  replicated (via `strategy.experimental_replicate_to_logical_devices`) to all
  logical devices. And calling `strategy.experimental_assign_to_logical_device`
  will result in a ValueError in this mode.
  """
    def __init__(self, tpu_cluster_resolver: Incomplete | None = None, experimental_device_assignment: Incomplete | None = None, experimental_spmd_xla_partitioning: bool = False) -> None:
        """Synchronous training in TPU donuts or Pods.

    Args:
      tpu_cluster_resolver: A
        `tf.distribute.cluster_resolver.TPUClusterResolver` instance, which
        provides information about the TPU cluster. If None, it will assume
        running on a local TPU worker.
      experimental_device_assignment: Optional
        `tf.tpu.experimental.DeviceAssignment` to specify the placement of
        replicas on the TPU cluster.
      experimental_spmd_xla_partitioning: If True, enable the SPMD (Single
        Program Multiple Data) mode in XLA compiler. This flag only affects the
        performance of XLA compilation and the HBM requirement of the compiled
        TPU program. Ceveat: if this flag is True, calling
        `tf.distribute.TPUStrategy.experimental_assign_to_logical_device` will
        result in a ValueError.
    """
    def run(self, fn, args=(), kwargs: Incomplete | None = None, options: Incomplete | None = None):
        """Run the computation defined by `fn` on each TPU replica.

    Executes ops specified by `fn` on each replica. If `args` or `kwargs` have
    `tf.distribute.DistributedValues`, such as those produced by a
    `tf.distribute.DistributedDataset` from
    `tf.distribute.Strategy.experimental_distribute_dataset` or
    `tf.distribute.Strategy.distribute_datasets_from_function`,
    when `fn` is executed on a particular replica, it will be executed with the
    component of `tf.distribute.DistributedValues` that correspond to that
    replica.

    `fn` may call `tf.distribute.get_replica_context()` to access members such
    as `all_reduce`.

    All arguments in `args` or `kwargs` should either be nest of tensors or
    `tf.distribute.DistributedValues` containing tensors or composite tensors.

    Example usage:

    >>> resolver = tf.distribute.cluster_resolver.TPUClusterResolver(tpu='')
    >>> tf.config.experimental_connect_to_cluster(resolver)
    >>> tf.tpu.experimental.initialize_tpu_system(resolver)
    >>> strategy = tf.distribute.TPUStrategy(resolver)
    >>> @tf.function
    ... def run():
    ...   def value_fn(value_context):
    ...     return value_context.num_replicas_in_sync
    ...   distributed_values = (
    ...       strategy.experimental_distribute_values_from_function(value_fn))
    ...   def replica_fn(input):
    ...     return input * 2
    ...   return strategy.run(replica_fn, args=(distributed_values,))
    >>> result = run()

    Args:
      fn: The function to run. The output must be a `tf.nest` of `Tensor`s.
      args: (Optional) Positional arguments to `fn`.
      kwargs: (Optional) Keyword arguments to `fn`.
      options: (Optional) An instance of `tf.distribute.RunOptions` specifying
        the options to run `fn`.

    Returns:
      Merged return value of `fn` across replicas. The structure of the return
      value is the same as the return value from `fn`. Each element in the
      structure can either be `tf.distribute.DistributedValues`, `Tensor`
      objects, or `Tensor`s (for example, if running on a single replica).
    """
    @property
    def cluster_resolver(self):
        """Returns the cluster resolver associated with this strategy.

    `tf.distribute.TPUStrategy` provides the associated
    `tf.distribute.cluster_resolver.ClusterResolver`. If the user provides one
    in `__init__`, that instance is returned; if the user does not, a default
    `tf.distribute.cluster_resolver.TPUClusterResolver` is provided.
    """
    def experimental_assign_to_logical_device(self, tensor, logical_device_id):
        """Adds annotation that `tensor` will be assigned to a logical device.

    This adds an annotation to `tensor` specifying that operations on
    `tensor` will be invoked on logical core device id `logical_device_id`.
    When model parallelism is used, the default behavior is that all ops
    are placed on zero-th logical device.

    ```python

    # Initializing TPU system with 2 logical devices and 4 replicas.
    resolver = tf.distribute.cluster_resolver.TPUClusterResolver(tpu='')
    tf.config.experimental_connect_to_cluster(resolver)
    topology = tf.tpu.experimental.initialize_tpu_system(resolver)
    device_assignment = tf.tpu.experimental.DeviceAssignment.build(
        topology,
        computation_shape=[1, 1, 1, 2],
        num_replicas=4)
    strategy = tf.distribute.TPUStrategy(
        resolver, experimental_device_assignment=device_assignment)
    iterator = iter(inputs)

    @tf.function()
    def step_fn(inputs):
      output = tf.add(inputs, inputs)

      # Add operation will be executed on logical device 0.
      output = strategy.experimental_assign_to_logical_device(output, 0)
      return output

    strategy.run(step_fn, args=(next(iterator),))
    ```

    Args:
      tensor: Input tensor to annotate.
      logical_device_id: Id of the logical core to which the tensor will be
        assigned.

    Raises:
      ValueError: The logical device id presented is not consistent with total
      number of partitions specified by the device assignment or the TPUStrategy
      is constructed with `experimental_spmd_xla_partitioning=True`.

    Returns:
      Annotated tensor with identical value as `tensor`.
    """
    def experimental_split_to_logical_devices(self, tensor, partition_dimensions):
        """Adds annotation that `tensor` will be split across logical devices.

    This adds an annotation to tensor `tensor` specifying that operations on
    `tensor` will be split among multiple logical devices. Tensor `tensor` will
    be split across dimensions specified by `partition_dimensions`.
    The dimensions of `tensor` must be divisible by corresponding value in
    `partition_dimensions`.

    For example, for system with 8 logical devices, if `tensor` is an image
    tensor with shape (batch_size, width, height, channel) and
    `partition_dimensions` is [1, 2, 4, 1], then `tensor` will be split
    2 in width dimension and 4 way in height dimension and the split
    tensor values will be fed into 8 logical devices.

    ```python
    # Initializing TPU system with 8 logical devices and 1 replica.
    resolver = tf.distribute.cluster_resolver.TPUClusterResolver(tpu='')
    tf.config.experimental_connect_to_cluster(resolver)
    topology = tf.tpu.experimental.initialize_tpu_system(resolver)
    device_assignment = tf.tpu.experimental.DeviceAssignment.build(
        topology,
        computation_shape=[1, 2, 2, 2],
        num_replicas=1)
    # Construct the TPUStrategy. Since we are going to split the image across
    # logical devices, here we set `experimental_spmd_xla_partitioning=True`
    # so that the partitioning can be compiled in SPMD mode, which usually
    # results in faster compilation and smaller HBM requirement if the size of
    # input and activation tensors are much bigger than that of the model
    # parameters. Note that this flag is suggested but not a hard requirement
    # for `experimental_split_to_logical_devices`.
    strategy = tf.distribute.TPUStrategy(
        resolver, experimental_device_assignment=device_assignment,
        experimental_spmd_xla_partitioning=True)

    iterator = iter(inputs)

    @tf.function()
    def step_fn(inputs):
      inputs = strategy.experimental_split_to_logical_devices(
        inputs, [1, 2, 4, 1])

      # model() function will be executed on 8 logical devices with `inputs`
      # split 2 * 4  ways.
      output = model(inputs)
      return output

    strategy.run(step_fn, args=(next(iterator),))
    ```
    Args:
      tensor: Input tensor to annotate.
      partition_dimensions: An unnested list of integers with the size equal to
        rank of `tensor` specifying how `tensor` will be partitioned. The
        product of all elements in `partition_dimensions` must be equal to the
        total number of logical devices per replica.

    Raises:
      ValueError: 1) If the size of partition_dimensions does not equal to rank
        of `tensor` or 2) if product of elements of `partition_dimensions` does
        not match the number of logical devices per replica defined by the
        implementing DistributionStrategy's device specification or
        3) if a known size of `tensor` is not divisible by corresponding
        value in `partition_dimensions`.

    Returns:
      Annotated tensor with identical value as `tensor`.
    """
    def experimental_replicate_to_logical_devices(self, tensor):
        """Adds annotation that `tensor` will be replicated to all logical devices.

    This adds an annotation to tensor `tensor` specifying that operations on
    `tensor` will be invoked on all logical devices.

    ```python
    # Initializing TPU system with 2 logical devices and 4 replicas.
    resolver = tf.distribute.cluster_resolver.TPUClusterResolver(tpu='')
    tf.config.experimental_connect_to_cluster(resolver)
    topology = tf.tpu.experimental.initialize_tpu_system(resolver)
    device_assignment = tf.tpu.experimental.DeviceAssignment.build(
        topology,
        computation_shape=[1, 1, 1, 2],
        num_replicas=4)
    strategy = tf.distribute.TPUStrategy(
        resolver, experimental_device_assignment=device_assignment)

    iterator = iter(inputs)

    @tf.function()
    def step_fn(inputs):
      images, labels = inputs
      images = strategy.experimental_split_to_logical_devices(
        inputs, [1, 2, 4, 1])

      # model() function will be executed on 8 logical devices with `inputs`
      # split 2 * 4  ways.
      output = model(inputs)

      # For loss calculation, all logical devices share the same logits
      # and labels.
      labels = strategy.experimental_replicate_to_logical_devices(labels)
      output = strategy.experimental_replicate_to_logical_devices(output)
      loss = loss_fn(labels, output)

      return loss

    strategy.run(step_fn, args=(next(iterator),))
    ```
    Args:
      tensor: Input tensor to annotate.

    Returns:
      Annotated tensor with identical value as `tensor`.
    """

class TPUStrategy(distribute_lib.Strategy):
    """Synchronous training on TPUs and TPU Pods.

  To construct a TPUStrategy object, you need to run the
  initialization code as below:

  >>> resolver = tf.distribute.cluster_resolver.TPUClusterResolver(tpu='')
  >>> tf.config.experimental_connect_to_cluster(resolver)
  >>> tf.tpu.experimental.initialize_tpu_system(resolver)
  >>> strategy = tf.distribute.experimental.TPUStrategy(resolver)

  While using distribution strategies, the variables created within the
  strategy's scope will be replicated across all the replicas and can be kept in
  sync using all-reduce algorithms.

  To run TF2 programs on TPUs, you can either use `.compile` and
  `.fit` APIs in `tf.keras` with TPUStrategy, or write your own customized
  training loop by calling `strategy.run` directly. Note that
  TPUStrategy doesn't support pure eager execution, so please make sure the
  function passed into `strategy.run` is a `tf.function` or
  `strategy.run` is called inside a `tf.function` if eager
  behavior is enabled.
  """
    def __init__(self, tpu_cluster_resolver: Incomplete | None = None, device_assignment: Incomplete | None = None) -> None:
        """Synchronous training in TPU donuts or Pods.

    Args:
      tpu_cluster_resolver: A tf.distribute.cluster_resolver.TPUClusterResolver,
        which provides information about the TPU cluster.
      device_assignment: Optional `tf.tpu.experimental.DeviceAssignment` to
        specify the placement of replicas on the TPU cluster.
    """
    def run(self, fn, args=(), kwargs: Incomplete | None = None, options: Incomplete | None = None):
        """See base class."""
    @property
    def cluster_resolver(self):
        """Returns the cluster resolver associated with this strategy.

    `tf.distribute.experimental.TPUStrategy` provides the
    associated `tf.distribute.cluster_resolver.ClusterResolver`. If the user
    provides one in `__init__`, that instance is returned; if the user does
    not, a default
    `tf.distribute.cluster_resolver.TPUClusterResolver` is provided.
    """

class TPUStrategyV1(distribute_lib.StrategyV1):
    """TPU distribution strategy implementation."""
    def __init__(self, tpu_cluster_resolver: Incomplete | None = None, steps_per_run: Incomplete | None = None, device_assignment: Incomplete | None = None) -> None:
        """Initializes the TPUStrategy object.

    Args:
      tpu_cluster_resolver: A tf.distribute.cluster_resolver.TPUClusterResolver,
          which provides information about the TPU cluster.
      steps_per_run: Number of steps to run on device before returning to the
          host. Note that this can have side-effects on performance, hooks,
          metrics, summaries etc.
          This parameter is only used when Distribution Strategy is used with
          estimator or keras.
      device_assignment: Optional `tf.tpu.experimental.DeviceAssignment` to
          specify the placement of replicas on the TPU cluster. Currently only
          supports the usecase of using a single core within a TPU cluster.
    """
    @property
    def steps_per_run(self):
        """DEPRECATED: use .extended.steps_per_run instead."""
    def run(self, fn, args=(), kwargs: Incomplete | None = None, options: Incomplete | None = None):
        '''Run `fn` on each replica, with the given arguments.

    Executes ops specified by `fn` on each replica. If `args` or `kwargs` have
    "per-replica" values, such as those produced by a "distributed `Dataset`",
    when `fn` is executed on a particular replica, it will be executed with the
    component of those "per-replica" values that correspond to that replica.

    `fn` may call `tf.distribute.get_replica_context()` to access members such
    as `all_reduce`.

    All arguments in `args` or `kwargs` should either be nest of tensors or
    per-replica objects containing tensors or composite tensors.

    Users can pass strategy specific options to `options` argument. An example
    to enable bucketizing dynamic shapes in `TPUStrategy.run`
    is:

    >>> resolver = tf.distribute.cluster_resolver.TPUClusterResolver(tpu=\'\')
    >>> tf.config.experimental_connect_to_cluster(resolver)
    >>> tf.tpu.experimental.initialize_tpu_system(resolver)
    >>> strategy = tf.distribute.experimental.TPUStrategy(resolver)

    >>> options = tf.distribute.RunOptions(
    ...     experimental_bucketizing_dynamic_shape=True)

    >>> dataset = tf.data.Dataset.range(
    ...    strategy.num_replicas_in_sync, output_type=dtypes.float32).batch(
    ...        strategy.num_replicas_in_sync, drop_remainder=True)
    >>> input_iterator = iter(strategy.experimental_distribute_dataset(dataset))

    >>> @tf.function()
    ... def step_fn(inputs):
    ...  output = tf.reduce_sum(inputs)
    ...  return output

    >>> strategy.run(step_fn, args=(next(input_iterator),), options=options)

    Args:
      fn: The function to run. The output must be a `tf.nest` of `Tensor`s.
      args: (Optional) Positional arguments to `fn`.
      kwargs: (Optional) Keyword arguments to `fn`.
      options: (Optional) An instance of `tf.distribute.RunOptions` specifying
        the options to run `fn`.

    Returns:
      Merged return value of `fn` across replicas. The structure of the return
      value is the same as the return value from `fn`. Each element in the
      structure can either be "per-replica" `Tensor` objects or `Tensor`s
      (for example, if running on a single replica).
    '''

class TPUExtended(distribute_lib.StrategyExtendedV1):
    """Implementation of TPUStrategy."""
    steps_per_run: Incomplete
    experimental_enable_get_next_as_optional: bool
    def __init__(self, container_strategy, tpu_cluster_resolver: Incomplete | None = None, steps_per_run: Incomplete | None = None, device_assignment: Incomplete | None = None, use_spmd_for_xla_partitioning: bool = False) -> None: ...
    def experimental_logical_device(self, logical_device_id) -> Generator[None, None, None]:
        """Places variables and ops on the specified logical device."""
    def read_var(self, var): ...
    def value_container(self, value): ...
    @property
    def num_hosts(self): ...
    @property
    def num_replicas_per_host(self): ...
    @property
    def experimental_between_graph(self): ...
    @property
    def experimental_should_init(self): ...
    @property
    def should_checkpoint(self): ...
    @property
    def should_save_summary(self): ...
    @property
    def worker_devices(self): ...
    @property
    def parameter_devices(self): ...
    @property
    def tpu_hardware_feature(self):
        """Return the `tf.tpu.experimental.HardwareFeature` class."""
    def non_slot_devices(self, var_list): ...
    def tpu_run(self, fn, args, kwargs, options: Incomplete | None = None): ...

class _TPUReplicaContext(distribute_lib.ReplicaContext):
    """Replication Context class for TPU Strategy."""
    def __init__(self, strategy, replica_id_in_sync_group: int = 0) -> None: ...
    @property
    def devices(self): ...
    def experimental_logical_device(self, logical_device_id):
        """Places variables and ops on the specified logical device."""
    def all_gather(self, value, axis, experimental_hints: Incomplete | None = None): ...
