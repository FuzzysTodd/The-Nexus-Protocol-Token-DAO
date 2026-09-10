import enum
from _typeshed import Incomplete
from tensorflow.python.data.ops import dataset_ops as dataset_ops
from tensorflow.python.distribute import collective_util as collective_util, device_util as device_util, distribution_strategy_context as distribution_strategy_context, numpy_dataset as numpy_dataset, reduce_util as reduce_util, values as values
from tensorflow.python.eager import def_function as def_function, monitoring as monitoring
from tensorflow.python.framework import constant_op as constant_op, dtypes as dtypes, indexed_slices as indexed_slices, ops as ops, tensor_shape as tensor_shape, tensor_util as tensor_util
from tensorflow.python.ops import array_ops as array_ops, control_flow_ops as control_flow_ops, custom_gradient as custom_gradient, math_ops as math_ops, resource_variable_ops as resource_variable_ops, summary_ops_v2 as summary_ops_v2, variable_scope as variable_scope
from tensorflow.python.ops.losses import losses_impl as losses_impl
from tensorflow.python.platform import tf_logging as tf_logging
from tensorflow.python.util import deprecation as deprecation, nest as nest, tf_contextlib as tf_contextlib
from tensorflow.python.util.deprecation import deprecated as deprecated
from tensorflow.python.util.tf_export import tf_export as tf_export
from tensorflow.tools.docs import doc_controls as doc_controls
from typing import NamedTuple

def get_update_replica_id():
    """Get the current device if in a `tf.distribute.Strategy.update()` call."""

class UpdateContext:
    """Context manager when you are in `update()` or `update_non_slot()`."""
    def __init__(self, replica_id) -> None: ...
    def __enter__(self) -> None: ...
    def __exit__(self, exception_type: type[BaseException] | None, exception_value: BaseException | None, traceback: types.TracebackType | None) -> None: ...

def get_loss_reduction():
    """`tf.distribute.ReduceOp` corresponding to the last loss reduction.

  This is used to decide whether loss should be scaled in optimizer (used only
  for estimator + v1 optimizer use case).

  Returns:
    `tf.distribute.ReduceOp` corresponding to the last loss reduction for
    estimator and v1 optimizer use case. `tf.distribute.ReduceOp.SUM` otherwise.
  """
def require_replica_context(replica_ctx) -> None:
    """Verify in `replica_ctx` replica context."""

class _CurrentDistributionContext:
    """Context manager setting the current `tf.distribute.Strategy`.

  Also: overrides the variable creator and optionally the current device.
  """
    def __init__(self, strategy, var_creator_scope, var_scope: Incomplete | None = None, resource_creator_scope: Incomplete | None = None, default_device: Incomplete | None = None) -> None: ...
    def __enter__(self): ...
    def __exit__(self, exception_type: type[BaseException] | None, exception_value: BaseException | None, traceback: types.TracebackType | None): ...

class InputReplicationMode(enum.Enum):
    """Replication mode for input function.

  * `PER_WORKER`: The input function will be called on each worker
    independently, creating as many input pipelines as number of workers.
    Replicas will dequeue from the local Dataset on their worker.
    `tf.distribute.Strategy` doesn't manage any state sharing between such
    separate input pipelines.
  * `PER_REPLICA`: The input function will be called on each replica separately.
    `tf.distribute.Strategy` doesn't manage any state sharing between such
    separate input pipelines.
  """
    PER_WORKER: str
    PER_REPLICA: str

class InputContext:
    """A class wrapping information needed by an input function.

  This is a context class that is passed to the user's input function and
  contains information about the compute replicas and input pipelines. The
  number of compute replicas (in sync training) helps compute the local batch
  size from the desired global batch size for each replica. The input pipeline
  information can be used to return a different subset of the input in each
  replica (for e.g. shard the input pipeline, use a different input
  source etc).
  """
    def __init__(self, num_input_pipelines: int = 1, input_pipeline_id: int = 0, num_replicas_in_sync: int = 1) -> None:
        """Initializes an InputContext object.

    Args:
      num_input_pipelines: the number of input pipelines in a cluster.
      input_pipeline_id: the current input pipeline id, should be an int in
        [0,`num_input_pipelines`).
      num_replicas_in_sync: the number of replicas that are in sync.
    """
    @property
    def num_replicas_in_sync(self):
        """Returns the number of compute replicas in sync."""
    @property
    def input_pipeline_id(self):
        """Returns the input pipeline ID."""
    @property
    def num_input_pipelines(self):
        """Returns the number of input pipelines."""
    def get_per_replica_batch_size(self, global_batch_size):
        """Returns the per-replica batch size.

    Args:
      global_batch_size: the global batch size which should be divisible by
        `num_replicas_in_sync`.

    Returns:
      the per-replica batch size.

    Raises:
      ValueError: if `global_batch_size` not divisible by
        `num_replicas_in_sync`.
    """

class ValueContext:
    '''A class wrapping information needed by a distribute function.

  This is a context class that is passed to the `value_fn` in
  `strategy.experimental_distribute_values_from_function` and contains
  information about the compute replicas. The `num_replicas_in_sync` and
  `replica_id` can be used to customize the value on each replica.

  Example usage:

  1.  Directly constructed.

      >>> def value_fn(context):
      ...   return context.replica_id_in_sync_group/context.num_replicas_in_sync
      >>> context = tf.distribute.experimental.ValueContext(
      ...   replica_id_in_sync_group=2, num_replicas_in_sync=4)
      >>> per_replica_value = value_fn(context)
      >>> per_replica_value
      0.5

  2.  Passed in by `experimental_distribute_values_from_function`.  {: value=2}

      >>> strategy = tf.distribute.MirroredStrategy(["GPU:0", "GPU:1"])
      >>> def value_fn(value_context):
      ...   return value_context.num_replicas_in_sync
      >>> distributed_values = (
      ...      strategy.experimental_distribute_values_from_function(
      ...        value_fn))
      >>> local_result = strategy.experimental_local_results(distributed_values)
      >>> local_result
      (2, 2)

  '''
    def __init__(self, replica_id_in_sync_group: int = 0, num_replicas_in_sync: int = 1) -> None:
        """Initializes an ValueContext object.

    Args:
      replica_id_in_sync_group: the current replica_id, should be an int in
        [0,`num_replicas_in_sync`).
      num_replicas_in_sync: the number of replicas that are in sync.
    """
    @property
    def num_replicas_in_sync(self):
        """Returns the number of compute replicas in sync."""
    @property
    def replica_id_in_sync_group(self):
        """Returns the replica ID."""

class RunOptions(NamedTuple('RunOptions', [('experimental_enable_dynamic_batch_size', Incomplete), ('experimental_bucketizing_dynamic_shape', Incomplete), ('experimental_xla_options', Incomplete)])):
    """Run options for `strategy.run`.

  This can be used to hold some strategy specific configs.

  Attributes:
    experimental_enable_dynamic_batch_size: Boolean. Only applies to
      TPUStrategy. Default to True. If True, TPUStrategy will enable dynamic
      padder to support dynamic batch size for the inputs. Otherwise only static
      shape inputs are allowed.
    experimental_bucketizing_dynamic_shape: Boolean. Only applies to
      TPUStrategy. Default to False. If True, TPUStrategy will automatic
      bucketize inputs passed into `run` if the input shape is
      dynamic. This is a performance optimization to reduce XLA recompilation,
      which should not have impact on correctness.
    experimental_xla_options: A `tf.tpu.XLAOptions` instance. Only applies to
      TPUStrategy. Controls the XLA compiling options on TPUs. Default to None.
  """
    def __new__(cls, experimental_enable_dynamic_batch_size: bool = True, experimental_bucketizing_dynamic_shape: bool = False, experimental_xla_options: Incomplete | None = None): ...

class InputOptions(NamedTuple('InputOptions', [('experimental_fetch_to_device', Incomplete), ('experimental_replication_mode', Incomplete), ('experimental_place_dataset_on_device', Incomplete), ('experimental_per_replica_buffer_size', Incomplete)])):
    """Run options for `experimental_distribute_dataset(s_from_function)`.

  This can be used to hold some strategy specific configs.

  ```python
  # Setup TPUStrategy
  resolver = tf.distribute.cluster_resolver.TPUClusterResolver(tpu='')
  tf.config.experimental_connect_to_cluster(resolver)
  tf.tpu.experimental.initialize_tpu_system(resolver)
  strategy = tf.distribute.TPUStrategy(resolver)

  dataset = tf.data.Dataset.range(16)
  distributed_dataset_on_host = (
      strategy.experimental_distribute_dataset(
          dataset,
          tf.distribute.InputOptions(
              experimental_replication_mode=
              experimental_replication_mode.PER_WORKER,
              experimental_place_dataset_on_device=False,
              experimental_per_replica_buffer_size=1)))
  ```

  Attributes:
    experimental_fetch_to_device: Boolean. If True, dataset
      elements will be prefetched to accelerator device memory. When False,
      dataset elements are prefetched to host device memory. Must be False when
      using TPUEmbedding API. experimental_fetch_to_device can only be used
      with experimental_replication_mode=PER_WORKER. Default behavior is same as
      setting it to True.
    experimental_replication_mode: Replication mode for the input function.
      Currently, the InputReplicationMode.PER_REPLICA is only supported with
      tf.distribute.MirroredStrategy.
      experimental_distribute_datasets_from_function.
      The default value is InputReplicationMode.PER_WORKER.
    experimental_place_dataset_on_device: Boolean. Default to False. When True,
      dataset will be placed on the device, otherwise it will remain on the
      host. experimental_place_dataset_on_device=True can only be used with
      experimental_replication_mode=PER_REPLICA
    experimental_per_replica_buffer_size: Integer. Default to 1. Indicates the
      prefetch buffer size in the replica device memory. Users can set it
      to 0 to completely disable prefetching behavior, or a number greater than
      1 to enable larger buffer size. Note that this option is still
      valid with `experimental_fetch_to_device=False`.
  """
    def __new__(cls, experimental_fetch_to_device: Incomplete | None = None, experimental_replication_mode=..., experimental_place_dataset_on_device: bool = False, experimental_per_replica_buffer_size: int = 1): ...

class StrategyBase:
    '''A state & compute distribution policy on a list of devices.

  See [the guide](https://www.tensorflow.org/guide/distributed_training)
  for overview and examples. See `tf.distribute.StrategyExtended` and
  [`tf.distribute`](https://www.tensorflow.org/api_docs/python/tf/distribute)
  for a glossary of concepts mentioned on this page such as "per-replica",
  _replica_, and _reduce_.

  In short:

  * To use it with Keras `compile`/`fit`,
    [please
    read](https://www.tensorflow.org/guide/distributed_training#using_tfdistributestrategy_with_keras).
  * You may pass descendant of `tf.distribute.Strategy` to
    `tf.estimator.RunConfig` to specify how a `tf.estimator.Estimator`
    should distribute its computation. See
    [guide](https://www.tensorflow.org/guide/distributed_training#using_tfdistributestrategy_with_estimator_limited_support).
  * Otherwise, use `tf.distribute.Strategy.scope` to specify that a
    strategy should be used when building an executing your model.
    (This puts you in the "cross-replica context" for this strategy, which
    means the strategy is put in control of things like variable placement.)
  * If you are writing a custom training loop, you will need to call a few more
    methods,
    [see the
    guide](https://www.tensorflow.org/guide/distributed_training#using_tfdistributestrategy_with_custom_training_loops):

      * Start by creating a `tf.data.Dataset` normally.
      * Use `tf.distribute.Strategy.experimental_distribute_dataset` to convert
        a `tf.data.Dataset` to something that produces "per-replica" values.
        If you want to manually specify how the dataset should be partitioned
        across replicas, use
        `tf.distribute.Strategy.distribute_datasets_from_function`
        instead.
      * Use `tf.distribute.Strategy.run` to run a function
        once per replica, taking values that may be "per-replica" (e.g.
        from a `tf.distribute.DistributedDataset` object) and returning
        "per-replica" values.
        This function is executed in "replica context", which means each
        operation is performed separately on each replica.
      * Finally use a method (such as `tf.distribute.Strategy.reduce`) to
        convert the resulting "per-replica" values into ordinary `Tensor`s.

  A custom training loop can be as simple as:

  ```
  with my_strategy.scope():
    @tf.function
    def distribute_train_epoch(dataset):
      def replica_fn(input):
        # process input and return result
        return result

      total_result = 0
      for x in dataset:
        per_replica_result = my_strategy.run(replica_fn, args=(x,))
        total_result += my_strategy.reduce(tf.distribute.ReduceOp.SUM,
                                           per_replica_result, axis=None)
      return total_result

    dist_dataset = my_strategy.experimental_distribute_dataset(dataset)
    for _ in range(EPOCHS):
      train_result = distribute_train_epoch(dist_dataset)
  ```

  This takes an ordinary `dataset` and `replica_fn` and runs it
  distributed using a particular `tf.distribute.Strategy` named
  `my_strategy` above. Any variables created in `replica_fn` are created
  using `my_strategy`\'s policy, and library functions called by
  `replica_fn` can use the `get_replica_context()` API to implement
  distributed-specific behavior.

  You can use the `reduce` API to aggregate results across replicas and use
  this as a return value from one iteration over a
  `tf.distribute.DistributedDataset`. Or
  you can use `tf.keras.metrics` (such as loss, accuracy, etc.) to
  accumulate metrics across steps in a given epoch.

  See the
  [custom training loop
  tutorial](https://www.tensorflow.org/tutorials/distribute/custom_training)
  for a more detailed example.

  Note: `tf.distribute.Strategy` currently does not support TensorFlow\'s
  partitioned variables (where a single variable is split across multiple
  devices) at this time.
  '''
    def __init__(self, extended) -> None: ...
    @property
    def extended(self):
        """`tf.distribute.StrategyExtended` with additional methods."""
    def scope(self):
        '''Context manager to make the strategy current and distribute variables.

    This method returns a context manager, and is used as follows:

    >>> strategy = tf.distribute.MirroredStrategy(["GPU:0", "GPU:1"])
    >>> # Variable created inside scope:
    >>> with strategy.scope():
    ...   mirrored_variable = tf.Variable(1.)
    >>> mirrored_variable
    MirroredVariable:{
      0: <tf.Variable \'Variable:0\' shape=() dtype=float32, numpy=1.0>,
      1: <tf.Variable \'Variable/replica_1:0\' shape=() dtype=float32, numpy=1.0>
    }
    >>> # Variable created outside scope:
    >>> regular_variable = tf.Variable(1.)
    >>> regular_variable
    <tf.Variable \'Variable:0\' shape=() dtype=float32, numpy=1.0>

    _What happens when Strategy.scope is entered?_

    * `strategy` is installed in the global context as the "current" strategy.
      Inside this scope, `tf.distribute.get_strategy()` will now return this
      strategy. Outside this scope, it returns the default no-op strategy.
    * Entering the scope also enters the "cross-replica context". See
      `tf.distribute.StrategyExtended` for an explanation on cross-replica and
      replica contexts.
    * Variable creation inside `scope` is intercepted by the strategy. Each
      strategy defines how it wants to affect the variable creation. Sync
      strategies like `MirroredStrategy`, `TPUStrategy` and
      `MultiWorkerMiroredStrategy` create variables replicated on each replica,
      whereas `ParameterServerStrategy` creates variables on the parameter
      servers. This is done using a custom `tf.variable_creator_scope`.
    * In some strategies, a default device scope may also be entered: in
      `MultiWorkerMiroredStrategy`, a default device scope of "/CPU:0" is
      entered on each worker.

    Note: Entering a scope does not automatically distribute a computation, except
      in the case of high level training framework like keras `model.fit`. If
      you\'re not using `model.fit`, you
      need to use `strategy.run` API to explicitly distribute that computation.
      See an example in the [custom training loop tutorial](https://www.tensorflow.org/tutorials/distribute/custom_training).


    _What should be in scope and what should be outside?_

    There are a number of requirements on what needs to happen inside the scope.
    However, in places where we have information about which strategy is in use,
    we often enter the scope for the user, so they don\'t have to do it
    explicitly (i.e. calling those either inside or outside the scope is OK).

    * Anything that creates variables that should be distributed variables
      must be called in a `strategy.scope`. This can be accomplished either by
      directly calling the variable creating function within the scope context,
      or by relying on another API like `strategy.run` or `keras.Model.fit` to
      automatically enter it for you. Any variable that is created outside scope
      will not be distributed and may have performance implications. Some common
      objects that create variables in TF are Models, Optimizers, Metrics. Such
      objects should always be initialized in the scope, and any functions
      that may lazily create variables (e.g., `Model.__call__()`, tracing a
      `tf.function`, etc.) should similarly be called within scope. Another
      source of variable creation can be a checkpoint restore - when variables
      are created lazily. Note that any variable created inside a strategy
      captures the strategy information. So reading and writing to these
      variables outside the `strategy.scope` can also work seamlessly, without
      the user having to enter the scope.
    * Some strategy APIs (such as `strategy.run` and `strategy.reduce`) which
      require to be in a strategy\'s scope, enter the scope automatically, which
      means when using those APIs you don\'t need to explicitly enter the scope
      yourself.
    * When a `tf.keras.Model` is created inside a `strategy.scope`, the Model
      object captures the scope information. When high level training framework
      methods such as `model.compile`, `model.fit`, etc. are then called, the
      captured scope will be automatically entered, and the associated strategy
      will be used to distribute the training etc. See a detailed example in
      [distributed keras tutorial](https://www.tensorflow.org/tutorials/distribute/keras).
      WARNING: Simply calling `model(..)` does not automatically enter the
      captured scope -- only high level training framework APIs support this
      behavior: `model.compile`, `model.fit`, `model.evaluate`, `model.predict`
      and `model.save` can all be called inside or outside the scope.
    * The following can be either inside or outside the scope:
        * Creating the input datasets
        * Defining `tf.function`s that represent your training step
        * Saving APIs such as `tf.saved_model.save`. Loading creates variables,
          so that should go inside the scope if you want to train the model in a
          distributed way.
        * Checkpoint saving. As mentioned above - `checkpoint.restore` may
          sometimes need to be inside scope if it creates variables.

    Returns:
      A context manager.
    '''
    def colocate_vars_with(self, colocate_with_variable):
        """DEPRECATED: use extended.colocate_vars_with() instead."""
    def make_dataset_iterator(self, dataset):
        """DEPRECATED TF 1.x ONLY."""
    def make_input_fn_iterator(self, input_fn, replication_mode=...):
        """DEPRECATED TF 1.x ONLY."""
    def experimental_run(self, fn, input_iterator: Incomplete | None = None):
        """DEPRECATED TF 1.x ONLY."""
    def experimental_distribute_dataset(self, dataset, options: Incomplete | None = None):
        '''Creates `tf.distribute.DistributedDataset` from `tf.data.Dataset`.

    The returned `tf.distribute.DistributedDataset` can be iterated over
    similar to regular datasets.
    NOTE: The user cannot add any more transformations to a
    `tf.distribute.DistributedDataset`. You can only create an iterator or
    examine the `tf.TypeSpec` of the data generated by it. See API docs of
    `tf.distribute.DistributedDataset` to learn more.

    The following is an example:

    >>> global_batch_size = 2
    >>> # Passing the devices is optional.
    ... strategy = tf.distribute.MirroredStrategy(devices=["GPU:0", "GPU:1"])
    >>> # Create a dataset
    ... dataset = tf.data.Dataset.range(4).batch(global_batch_size)
    >>> # Distribute that dataset
    ... dist_dataset = strategy.experimental_distribute_dataset(dataset)
    >>> @tf.function
    ... def replica_fn(input):
    ...   return input*2
    >>> result = []
    >>> # Iterate over the `tf.distribute.DistributedDataset`
    ... for x in dist_dataset:
    ...   # process dataset elements
    ...   result.append(strategy.run(replica_fn, args=(x,)))
    >>> print(result)
    [PerReplica:{
      0: <tf.Tensor: shape=(1,), dtype=int64, numpy=array([0])>,
      1: <tf.Tensor: shape=(1,), dtype=int64, numpy=array([2])>
    }, PerReplica:{
      0: <tf.Tensor: shape=(1,), dtype=int64, numpy=array([4])>,
      1: <tf.Tensor: shape=(1,), dtype=int64, numpy=array([6])>
    }]


    Three key actions happening under the hood of this method are batching,
    sharding, and prefetching.

    In the code snippet above, `dataset` is batched by `global_batch_size`, and
    calling `experimental_distribute_dataset` on it rebatches `dataset` to a
    new batch size that is equal to the global batch size divided by the number
    of replicas in sync. We iterate through it using a Pythonic for loop.
    `x` is a `tf.distribute.DistributedValues` containing data for all replicas,
    and each replica gets data of the new batch size.
    `tf.distribute.Strategy.run` will take care of feeding the right per-replica
    data in `x` to the right `replica_fn` executed on each replica.

    Sharding contains autosharding across multiple workers and within every
    worker. First, in multi-worker distributed training (i.e. when you use
    `tf.distribute.experimental.MultiWorkerMirroredStrategy`
    or `tf.distribute.TPUStrategy`), autosharding a dataset over a set of
    workers means that each worker is assigned a subset of the entire dataset
    (if the right `tf.data.experimental.AutoShardPolicy` is set). This is to
    ensure that at each step, a global batch size of non-overlapping dataset
    elements will be processed by each worker. Autosharding has a couple of
    different options that can be specified using
    `tf.data.experimental.DistributeOptions`. Then, sharding within each worker
    means the method will split the data among all the worker devices (if more
    than one a present). This will happen regardless of multi-worker
    autosharding.

    Note: for autosharding across multiple workers, the default mode is
    `tf.data.experimental.AutoShardPolicy.AUTO`. This mode
    will attempt to shard the input dataset by files if the dataset is
    being created out of reader datasets (e.g. `tf.data.TFRecordDataset`,
    `tf.data.TextLineDataset`, etc.) or otherwise shard the dataset by data,
    where each of the workers will read the entire dataset and only process the
    shard assigned to it. However, if you have less than one input file per
    worker, we suggest that you disable dataset autosharding across workers by
    setting the `tf.data.experimental.DistributeOptions.auto_shard_policy` to be
    `tf.data.experimental.AutoShardPolicy.OFF`.

    By default, this method adds a prefetch transformation at the end of the
    user provided `tf.data.Dataset` instance. The argument to the prefetch
    transformation which is `buffer_size` is equal to the number of replicas in
    sync.

    If the above batch splitting and dataset sharding logic is undesirable,
    please use
    `tf.distribute.Strategy.distribute_datasets_from_function`
    instead, which does not do any automatic batching or sharding for you.

    Note: If you are using TPUStrategy, the order in which the data is processed
    by the workers when using
    `tf.distribute.Strategy.experimental_distribute_dataset` or
    `tf.distribute.Strategy.distribute_datasets_from_function` is
    not guaranteed. This is typically required if you are using
    `tf.distribute` to scale prediction. You can however insert an index for
    each element in the batch and order outputs accordingly. Refer to [this
    snippet](https://www.tensorflow.org/tutorials/distribute/input#caveats)
    for an example of how to order outputs.

    Note: Stateful dataset transformations are currently not supported with
    `tf.distribute.experimental_distribute_dataset` or
    `tf.distribute.distribute_datasets_from_function`. Any stateful
    ops that the dataset may have are currently ignored. For example, if your
    dataset has a `map_fn` that uses `tf.random.uniform` to rotate an image,
    then you have a dataset graph that depends on state (i.e the random seed) on
    the local machine where the python process is being executed.

    For a tutorial on more usage and properties of this method, refer to the
    [tutorial on distributed input](https://www.tensorflow.org/tutorials/distribute/input#tfdistributestrategyexperimental_distribute_dataset).
    If you are interested in last partial batch handling, read [this section](https://www.tensorflow.org/tutorials/distribute/input#partial_batches).

    Args:
      dataset: `tf.data.Dataset` that will be sharded across all replicas using
        the rules stated above.
      options: `tf.distribute.InputOptions` used to control options on how this
        dataset is distributed.

    Returns:
      A `tf.distribute.DistributedDataset`.
    '''
    def distribute_datasets_from_function(self, dataset_fn, options: Incomplete | None = None):
        """Distributes `tf.data.Dataset` instances created by calls to `dataset_fn`.

    The argument `dataset_fn` that users pass in is an input function that has a
    `tf.distribute.InputContext` argument and returns a `tf.data.Dataset`
    instance. It is expected that the returned dataset from `dataset_fn` is
    already batched by per-replica batch size (i.e. global batch size divided by
    the number of replicas in sync) and sharded.
    `tf.distribute.Strategy.distribute_datasets_from_function` does
    not batch or shard the `tf.data.Dataset` instance
    returned from the input function. `dataset_fn` will be called on the CPU
    device of each of the workers and each generates a dataset where every
    replica on that worker will dequeue one batch of inputs (i.e. if a worker
    has two replicas, two batches will be dequeued from the `Dataset` every
    step).

    This method can be used for several purposes. First, it allows you to
    specify your own batching and sharding logic. (In contrast,
    `tf.distribute.experimental_distribute_dataset` does batching and sharding
    for you.) For example, where
    `experimental_distribute_dataset` is unable to shard the input files, this
    method might be used to manually shard the dataset (avoiding the slow
    fallback behavior in `experimental_distribute_dataset`). In cases where the
    dataset is infinite, this sharding can be done by creating dataset replicas
    that differ only in their random seed.

    The `dataset_fn` should take an `tf.distribute.InputContext` instance where
    information about batching and input replication can be accessed.

    You can use `element_spec` property of the
    `tf.distribute.DistributedDataset` returned by this API to query the
    `tf.TypeSpec` of the elements returned by the iterator. This can be used to
    set the `input_signature` property of a `tf.function`. Follow
    `tf.distribute.DistributedDataset.element_spec` to see an example.

    IMPORTANT: The `tf.data.Dataset` returned by `dataset_fn` should have a
    per-replica batch size, unlike `experimental_distribute_dataset`, which uses
    the global batch size. This may be computed using
    `input_context.get_per_replica_batch_size`.

    Note: If you are using TPUStrategy, the order in which the data is processed
    by the workers when using
    `tf.distribute.Strategy.experimental_distribute_dataset` or
    `tf.distribute.Strategy.distribute_datasets_from_function` is
    not guaranteed. This is typically required if you are using
    `tf.distribute` to scale prediction. You can however insert an index for
    each element in the batch and order outputs accordingly. Refer to [this
    snippet](https://www.tensorflow.org/tutorials/distribute/input#caveats)
    for an example of how to order outputs.

    Note: Stateful dataset transformations are currently not supported with
    `tf.distribute.experimental_distribute_dataset` or
    `tf.distribute.distribute_datasets_from_function`. Any stateful
    ops that the dataset may have are currently ignored. For example, if your
    dataset has a `map_fn` that uses `tf.random.uniform` to rotate an image,
    then you have a dataset graph that depends on state (i.e the random seed) on
    the local machine where the python process is being executed.

    For a tutorial on more usage and properties of this method, refer to the
    [tutorial on distributed input](https://www.tensorflow.org/tutorials/distribute/input#tfdistributestrategyexperimental_distribute_datasets_from_function)).
    If you are interested in last partial batch handling, read [this section](https://www.tensorflow.org/tutorials/distribute/input#partial_batches).

    Args:
      dataset_fn: A function taking a `tf.distribute.InputContext` instance and
        returning a `tf.data.Dataset`.
      options: `tf.distribute.InputOptions` used to control options on how this
        dataset is distributed.

    Returns:
      A `tf.distribute.DistributedDataset`.
    """
    def experimental_distribute_datasets_from_function(self, dataset_fn, options: Incomplete | None = None): ...
    def run(self, fn, args=(), kwargs: Incomplete | None = None, options: Incomplete | None = None):
        '''Invokes `fn` on each replica, with the given arguments.

    This method is the primary way to distribute your computation with a
    tf.distribute object. It invokes `fn` on each replica. If `args` or `kwargs`
    have `tf.distribute.DistributedValues`, such as those produced by a
    `tf.distribute.DistributedDataset` from
    `tf.distribute.Strategy.experimental_distribute_dataset` or
    `tf.distribute.Strategy.distribute_datasets_from_function`,
    when `fn` is executed on a particular replica, it will be executed with the
    component of `tf.distribute.DistributedValues` that correspond to that
    replica.

    `fn` is invoked under a replica context. `fn` may call
    `tf.distribute.get_replica_context()` to access members such as
    `all_reduce`. Please see the module-level docstring of tf.distribute for the
    concept of replica context.

    All arguments in `args` or `kwargs` can be a nested structure of tensors,
    e.g. a list of tensors, in which case `args` and `kwargs` will be passed to
    the `fn` invoked on each replica. Or `args` or `kwargs` can be
    `tf.distribute.DistributedValues` containing tensors or composite tensors,
    i.e. `tf.compat.v1.TensorInfo.CompositeTensor`, in which case each `fn` call
    will get the component of a `tf.distribute.DistributedValues` corresponding
    to its replica. Note that arbitrary Python values that are not of the types
    above are not supported.

    IMPORTANT: Depending on the implementation of `tf.distribute.Strategy` and
    whether eager execution is enabled, `fn` may be called one or more times. If
    `fn` is annotated with `tf.function` or `tf.distribute.Strategy.run` is
    called inside a `tf.function` (eager execution is disabled inside a
    `tf.function` by default), `fn` is called once per replica to generate a
    Tensorflow graph, which will then be reused for execution with new inputs.
    Otherwise, if eager execution is enabled, `fn` will be called once per
    replica every step just like regular python code.

    Example usage:

    1.  Constant tensor input.

        >>> strategy = tf.distribute.MirroredStrategy(["GPU:0", "GPU:1"])
        >>> tensor_input = tf.constant(3.0)
        >>> @tf.function
        ... def replica_fn(input):
        ...   return input*2.0
        >>> result = strategy.run(replica_fn, args=(tensor_input,))
        >>> result
        PerReplica:{
          0: <tf.Tensor: shape=(), dtype=float32, numpy=6.0>,
          1: <tf.Tensor: shape=(), dtype=float32, numpy=6.0>
        }

    2.  DistributedValues input.  {: value=2}

        >>> strategy = tf.distribute.MirroredStrategy(["GPU:0", "GPU:1"])
        >>> @tf.function
        ... def run():
        ...   def value_fn(value_context):
        ...     return value_context.num_replicas_in_sync
        ...   distributed_values = (
        ...     strategy.experimental_distribute_values_from_function(
        ...       value_fn))
        ...   def replica_fn2(input):
        ...     return input*2
        ...   return strategy.run(replica_fn2, args=(distributed_values,))
        >>> result = run()
        >>> result
        <tf.Tensor: shape=(), dtype=int32, numpy=4>

    3.  Use `tf.distribute.ReplicaContext` to allreduce values. {: value=3}

        >>> strategy = tf.distribute.MirroredStrategy(["gpu:0", "gpu:1"])
        >>> @tf.function
        ... def run():
        ...    def value_fn(value_context):
        ...      return tf.constant(value_context.replica_id_in_sync_group)
        ...    distributed_values = (
        ...        strategy.experimental_distribute_values_from_function(
        ...            value_fn))
        ...    def replica_fn(input):
        ...      return tf.distribute.get_replica_context().all_reduce(
        ...          "sum", input)
        ...    return strategy.run(replica_fn, args=(distributed_values,))
        >>> result = run()
        >>> result
        PerReplica:{
          0: <tf.Tensor: shape=(), dtype=int32, numpy=1>,
          1: <tf.Tensor: shape=(), dtype=int32, numpy=1>
        }

    Args:
      fn: The function to run on each replica.
      args: Optional positional arguments to `fn`. Its element can be a tensor,
        a nested structure of tensors or a `tf.distribute.DistributedValues`.
      kwargs: Optional keyword arguments to `fn`. Its element can be a tensor,
        a nested structure of tensors or a `tf.distribute.DistributedValues`.
      options: An optional instance of `tf.distribute.RunOptions` specifying
        the options to run `fn`.

    Returns:
      Merged return value of `fn` across replicas. The structure of the return
      value is the same as the return value from `fn`. Each element in the
      structure can either be `tf.distribute.DistributedValues`, `Tensor`
      objects, or `Tensor`s (for example, if running on a single replica).
    '''
    def reduce(self, reduce_op, value, axis):
        '''Reduce `value` across replicas and return result on current device.

    >>> strategy = tf.distribute.MirroredStrategy(["GPU:0", "GPU:1"])
    >>> def step_fn():
    ...   i = tf.distribute.get_replica_context().replica_id_in_sync_group
    ...   return tf.identity(i)
    >>>
    >>> per_replica_result = strategy.run(step_fn)
    >>> total = strategy.reduce("SUM", per_replica_result, axis=None)
    >>> total
    <tf.Tensor: shape=(), dtype=int32, numpy=1>

    To see how this would look with multiple replicas, consider the same
    example with MirroredStrategy with 2 GPUs:

    ```python
    strategy = tf.distribute.MirroredStrategy(devices=["GPU:0", "GPU:1"])
    def step_fn():
      i = tf.distribute.get_replica_context().replica_id_in_sync_group
      return tf.identity(i)

    per_replica_result = strategy.run(step_fn)
    # Check devices on which per replica result is:
    strategy.experimental_local_results(per_replica_result)[0].device
    # /job:localhost/replica:0/task:0/device:GPU:0
    strategy.experimental_local_results(per_replica_result)[1].device
    # /job:localhost/replica:0/task:0/device:GPU:1

    total = strategy.reduce("SUM", per_replica_result, axis=None)
    # Check device on which reduced result is:
    total.device
    # /job:localhost/replica:0/task:0/device:CPU:0

    ```

    This API is typically used for aggregating the results returned from
    different replicas, for reporting etc. For example, loss computed from
    different replicas can be averaged using this API before printing.

    Note: The result is copied to the "current" device - which would typically
    be the CPU of the worker on which the program is running. For `TPUStrategy`,
    it is the first TPU host. For multi client `MultiWorkerMirroredStrategy`,
    this is CPU of each worker.

    There are a number of different tf.distribute APIs for reducing values
    across replicas:
    * `tf.distribute.ReplicaContext.all_reduce`: This differs from
    `Strategy.reduce` in that it is for replica context and does
    not copy the results to the host device. `all_reduce` should be typically
    used for reductions inside the training step such as gradients.
    * `tf.distribute.StrategyExtended.reduce_to` and
    `tf.distribute.StrategyExtended.batch_reduce_to`: These APIs are more
    advanced versions of `Strategy.reduce` as they allow customizing the
    destination of the result. They are also called in cross replica context.

    _What should axis be?_

    Given a per-replica value returned by `run`, say a
    per-example loss, the batch will be divided across all the replicas.  This
    function allows you to aggregate across replicas and optionally also across
    batch elements by specifying the axis parameter accordingly.

    For example, if you have a global batch size of 8 and 2
    replicas, values for examples `[0, 1, 2, 3]` will be on replica 0 and
    `[4, 5, 6, 7]` will be on replica 1. With `axis=None`, `reduce` will
    aggregate only across replicas, returning `[0+4, 1+5, 2+6, 3+7]`.
    This is useful when each replica is computing a scalar or some other value
    that doesn\'t have a "batch" dimension (like a gradient or loss).
    ```
    strategy.reduce("sum", per_replica_result, axis=None)
    ```

    Sometimes, you will want to aggregate across both the global batch _and_
    all replicas. You can get this behavior by specifying the batch
    dimension as the `axis`, typically `axis=0`. In this case it would return a
    scalar `0+1+2+3+4+5+6+7`.
    ```
    strategy.reduce("sum", per_replica_result, axis=0)
    ```

    If there is a last partial batch, you will need to specify an axis so
    that the resulting shape is consistent across replicas. So if the last
    batch has size 6 and it is divided into [0, 1, 2, 3] and [4, 5], you
    would get a shape mismatch unless you specify `axis=0`. If you specify
    `tf.distribute.ReduceOp.MEAN`, using `axis=0` will use the correct
    denominator of 6. Contrast this with computing `reduce_mean` to get a
    scalar value on each replica and this function to average those means,
    which will weigh some values `1/8` and others `1/4`.

    Args:
      reduce_op: a `tf.distribute.ReduceOp` value specifying how values should
        be combined. Allows using string representation of the enum such as
        "SUM", "MEAN".
      value: a `tf.distribute.DistributedValues` instance, e.g. returned by
        `Strategy.run`, to be combined into a single tensor. It can also be a
        regular tensor when used with `OneDeviceStrategy` or default strategy.
      axis: specifies the dimension to reduce along within each
        replica\'s tensor. Should typically be set to the batch dimension, or
        `None` to only reduce across replicas (e.g. if the tensor has no batch
        dimension).

    Returns:
      A `Tensor`.
    '''
    def unwrap(self, value):
        """Returns the list of all local per-replica values contained in `value`.

    DEPRECATED: Please use `experimental_local_results` instead.

    Note: This only returns values on the workers initiated by this client.
    When using a `tf.distribute.Strategy` like
    `tf.distribute.experimental.MultiWorkerMirroredStrategy`, each worker
    will be its own client, and this function will only return values
    computed on that worker.

    Args:
      value: A value returned by `experimental_run()`,
        `extended.call_for_each_replica()`, or a variable created in `scope`.

    Returns:
      A tuple of values contained in `value`. If `value` represents a single
      value, this returns `(value,).`
    """
    def experimental_local_results(self, value):
        """Returns the list of all local per-replica values contained in `value`.

    Note: This only returns values on the worker initiated by this client.
    When using a `tf.distribute.Strategy` like
    `tf.distribute.experimental.MultiWorkerMirroredStrategy`, each worker
    will be its own client, and this function will only return values
    computed on that worker.

    Args:
      value: A value returned by `experimental_run()`, `run(), or a variable
      created in `scope`.

    Returns:
      A tuple of values contained in `value` where ith element corresponds to
      ith replica. If `value` represents a single value, this returns
      `(value,).`
    """
    def group(self, value, name: Incomplete | None = None):
        """Shortcut for `tf.group(self.experimental_local_results(value))`."""
    @property
    def num_replicas_in_sync(self):
        """Returns number of replicas over which gradients are aggregated."""
    def configure(self, session_config: Incomplete | None = None, cluster_spec: Incomplete | None = None, task_type: Incomplete | None = None, task_id: Incomplete | None = None):
        """DEPRECATED: use `update_config_proto` instead.

    Configures the strategy class.

    DEPRECATED: This method's functionality has been split into the strategy
    constructor and `update_config_proto`. In the future, we will allow passing
    cluster and config_proto to the constructor to configure the strategy. And
    `update_config_proto` can be used to update the config_proto based on the
    specific strategy.
    """
    def update_config_proto(self, config_proto):
        """DEPRECATED TF 1.x ONLY."""
    def __deepcopy__(self, memo): ...
    def __copy__(self) -> None: ...
    @property
    def cluster_resolver(self):
        '''Returns the cluster resolver associated with this strategy.

    In general, when using a multi-worker `tf.distribute` strategy such as
    `tf.distribute.experimental.MultiWorkerMirroredStrategy` or
    `tf.distribute.TPUStrategy()`, there is a
    `tf.distribute.cluster_resolver.ClusterResolver` associated with the
    strategy used, and such an instance is returned by this property.

    Strategies that intend to have an associated
    `tf.distribute.cluster_resolver.ClusterResolver` must set the
    relevant attribute, or override this property; otherwise, `None` is returned
    by default. Those strategies should also provide information regarding what
    is returned by this property.

    Single-worker strategies usually do not have a
    `tf.distribute.cluster_resolver.ClusterResolver`, and in those cases this
    property will return `None`.

    The `tf.distribute.cluster_resolver.ClusterResolver` may be useful when the
    user needs to access information such as the cluster spec, task type or task
    id. For example,

    ```python

    os.environ[\'TF_CONFIG\'] = json.dumps({
      \'cluster\': {
          \'worker\': ["localhost:12345", "localhost:23456"],
          \'ps\': ["localhost:34567"]
      },
      \'task\': {\'type\': \'worker\', \'index\': 0}
    })

    # This implicitly uses TF_CONFIG for the cluster and current task info.
    strategy = tf.distribute.experimental.MultiWorkerMirroredStrategy()

    ...

    if strategy.cluster_resolver.task_type == \'worker\':
      # Perform something that\'s only applicable on workers. Since we set this
      # as a worker above, this block will run on this particular instance.
    elif strategy.cluster_resolver.task_type == \'ps\':
      # Perform something that\'s only applicable on parameter servers. Since we
      # set this as a worker above, this block will not run on this particular
      # instance.
    ```

    For more information, please see
    `tf.distribute.cluster_resolver.ClusterResolver`\'s API docstring.

    Returns:
      The cluster resolver associated with this strategy. Returns `None` if a
      cluster resolver is not applicable or available in this strategy.
    '''

class Strategy(StrategyBase):
    __doc__: Incomplete
    def experimental_distribute_values_from_function(self, value_fn):
        '''Generates `tf.distribute.DistributedValues` from `value_fn`.

    This function is to generate `tf.distribute.DistributedValues` to pass
    into `run`, `reduce`, or other methods that take
    distributed values when not using datasets.

    Args:
      value_fn: The function to run to generate values. It is called for
        each replica with `tf.distribute.ValueContext` as the sole argument. It
        must return a Tensor or a type that can be converted to a Tensor.
    Returns:
      A `tf.distribute.DistributedValues` containing a value for each replica.

    Example usage:

    1.  Return constant value per replica:

        >>> strategy = tf.distribute.MirroredStrategy(["GPU:0", "GPU:1"])
        >>> def value_fn(ctx):
        ...   return tf.constant(1.)
        >>> distributed_values = (
        ...     strategy.experimental_distribute_values_from_function(
        ...        value_fn))
        >>> local_result = strategy.experimental_local_results(
        ...     distributed_values)
        >>> local_result
        (<tf.Tensor: shape=(), dtype=float32, numpy=1.0>,
        <tf.Tensor: shape=(), dtype=float32, numpy=1.0>)

    2.  Distribute values in array based on replica_id: {: value=2}

        >>> strategy = tf.distribute.MirroredStrategy(["GPU:0", "GPU:1"])
        >>> array_value = np.array([3., 2., 1.])
        >>> def value_fn(ctx):
        ...   return array_value[ctx.replica_id_in_sync_group]
        >>> distributed_values = (
        ...     strategy.experimental_distribute_values_from_function(
        ...         value_fn))
        >>> local_result = strategy.experimental_local_results(
        ...     distributed_values)
        >>> local_result
        (3.0, 2.0)

    3.  Specify values using num_replicas_in_sync:  {: value=3}

        >>> strategy = tf.distribute.MirroredStrategy(["GPU:0", "GPU:1"])
        >>> def value_fn(ctx):
        ...   return ctx.num_replicas_in_sync
        >>> distributed_values = (
        ...     strategy.experimental_distribute_values_from_function(
        ...         value_fn))
        >>> local_result = strategy.experimental_local_results(
        ...     distributed_values)
        >>> local_result
        (2, 2)

    4.  Place values on devices and distribute: {: value=4}

        ```
        strategy = tf.distribute.TPUStrategy()
        worker_devices = strategy.extended.worker_devices
        multiple_values = []
        for i in range(strategy.num_replicas_in_sync):
          with tf.device(worker_devices[i]):
            multiple_values.append(tf.constant(1.0))

        def value_fn(ctx):
          return multiple_values[ctx.replica_id_in_sync_group]

        distributed_values = strategy.
          experimental_distribute_values_from_function(
          value_fn)
        ```

    '''
    def gather(self, value, axis):
        '''Gather `value` across replicas along `axis` to the current device.

    Given a `tf.distribute.DistributedValues` or `tf.Tensor`-like
    object `value`, this API gathers and concatenates `value` across replicas
    along the `axis`-th dimension. The result is copied to the "current" device,
    which would typically be the CPU of the worker on which the program is
    running. For `tf.distribute.TPUStrategy`, it is the first TPU host. For
    multi-client `tf.distribute.MultiWorkerMirroredStrategy`, this is the CPU of
    each worker.

    This API can only be called in the cross-replica context. For a counterpart
    in the replica context, see `tf.distribute.ReplicaContext.all_gather`.

    Note: For all strategies except `tf.distribute.TPUStrategy`, the input
    `value` on different replicas must have the same rank, and their shapes must
    be the same in all dimensions except the `axis`-th dimension. In other
    words, their shapes cannot be different in a dimension `d` where `d` does
    not equal to the `axis` argument. For example, given a
    `tf.distribute.DistributedValues` with component tensors of shape
    `(1, 2, 3)` and `(1, 3, 3)` on two replicas, you can call
    `gather(..., axis=1, ...)` on it, but not `gather(..., axis=0, ...)` or
    `gather(..., axis=2, ...)`. However, for `tf.distribute.TPUStrategy.gather`,
    all tensors must have exactly the same rank and same shape.

    Note: Given a `tf.distribute.DistributedValues` `value`, its component
    tensors must have a non-zero rank. Otherwise, consider using
    `tf.expand_dims` before gathering them.

    >>> strategy = tf.distribute.MirroredStrategy(["GPU:0", "GPU:1"])
    >>> # A DistributedValues with component tensor of shape (2, 1) on each replica
    ... distributed_values = strategy.experimental_distribute_values_from_function(lambda _: tf.identity(tf.constant([[1], [2]])))
    >>> @tf.function
    ... def run():
    ...   return strategy.gather(distributed_values, axis=0)
    >>> run()
    <tf.Tensor: shape=(4, 1), dtype=int32, numpy=
    array([[1],
           [2],
           [1],
           [2]], dtype=int32)>


    Consider the following example for more combinations:

    >>> strategy = tf.distribute.MirroredStrategy(["GPU:0", "GPU:1", "GPU:2", "GPU:3"])
    >>> single_tensor = tf.reshape(tf.range(6), shape=(1,2,3))
    >>> distributed_values = strategy.experimental_distribute_values_from_function(lambda _: tf.identity(single_tensor))
    >>> @tf.function
    ... def run(axis):
    ...   return strategy.gather(distributed_values, axis=axis)
    >>> axis=0
    >>> run(axis)
    <tf.Tensor: shape=(4, 2, 3), dtype=int32, numpy=
    array([[[0, 1, 2],
            [3, 4, 5]],
           [[0, 1, 2],
            [3, 4, 5]],
           [[0, 1, 2],
            [3, 4, 5]],
           [[0, 1, 2],
            [3, 4, 5]]], dtype=int32)>
    >>> axis=1
    >>> run(axis)
    <tf.Tensor: shape=(1, 8, 3), dtype=int32, numpy=
    array([[[0, 1, 2],
            [3, 4, 5],
            [0, 1, 2],
            [3, 4, 5],
            [0, 1, 2],
            [3, 4, 5],
            [0, 1, 2],
            [3, 4, 5]]], dtype=int32)>
    >>> axis=2
    >>> run(axis)
    <tf.Tensor: shape=(1, 2, 12), dtype=int32, numpy=
    array([[[0, 1, 2, 0, 1, 2, 0, 1, 2, 0, 1, 2],
            [3, 4, 5, 3, 4, 5, 3, 4, 5, 3, 4, 5]]], dtype=int32)>


    Args:
      value: a `tf.distribute.DistributedValues` instance, e.g. returned by
        `Strategy.run`, to be combined into a single tensor. It can also be a
        regular tensor when used with `tf.distribute.OneDeviceStrategy` or the
        default strategy. The tensors that constitute the DistributedValues
        can only be dense tensors with non-zero rank, NOT a `tf.IndexedSlices`.
      axis: 0-D int32 Tensor. Dimension along which to gather. Must be in the
        range [0, rank(value)).

    Returns:
       A `Tensor` that\'s the concatenation of `value` across replicas along
       `axis` dimension.
    '''

class StrategyV1(StrategyBase):
    """A list of devices with a state & compute distribution policy.

  See [the guide](https://www.tensorflow.org/guide/distribute_strategy)
  for overview and examples.

  Note: Not all `tf.distribute.Strategy` implementations currently support
  TensorFlow's partitioned variables (where a single variable is split across
  multiple devices) at this time.
  """
    def make_dataset_iterator(self, dataset):
        """Makes an iterator for input provided via `dataset`.

    DEPRECATED: This method is not available in TF 2.x.

    Data from the given dataset will be distributed evenly across all the
    compute replicas. We will assume that the input dataset is batched by the
    global batch size. With this assumption, we will make a best effort to
    divide each batch across all the replicas (one or more workers).
    If this effort fails, an error will be thrown, and the user should instead
    use `make_input_fn_iterator` which provides more control to the user, and
    does not try to divide a batch across replicas.

    The user could also use `make_input_fn_iterator` if they want to
    customize which input is fed to which replica/worker etc.

    Args:
      dataset: `tf.data.Dataset` that will be distributed evenly across all
        replicas.

    Returns:
      An `tf.distribute.InputIterator` which returns inputs for each step of the
      computation.  User should call `initialize` on the returned iterator.
    """
    def make_input_fn_iterator(self, input_fn, replication_mode=...):
        """Returns an iterator split across replicas created from an input function.

    DEPRECATED: This method is not available in TF 2.x.

    The `input_fn` should take an `tf.distribute.InputContext` object where
    information about batching and input sharding can be accessed:

    ```
    def input_fn(input_context):
      batch_size = input_context.get_per_replica_batch_size(global_batch_size)
      d = tf.data.Dataset.from_tensors([[1.]]).repeat().batch(batch_size)
      return d.shard(input_context.num_input_pipelines,
                     input_context.input_pipeline_id)
    with strategy.scope():
      iterator = strategy.make_input_fn_iterator(input_fn)
      replica_results = strategy.experimental_run(replica_fn, iterator)
    ```

    The `tf.data.Dataset` returned by `input_fn` should have a per-replica
    batch size, which may be computed using
    `input_context.get_per_replica_batch_size`.

    Args:
      input_fn: A function taking a `tf.distribute.InputContext` object and
        returning a `tf.data.Dataset`.
      replication_mode: an enum value of `tf.distribute.InputReplicationMode`.
        Only `PER_WORKER` is supported currently, which means there will be
        a single call to `input_fn` per worker. Replicas will dequeue from the
        local `tf.data.Dataset` on their worker.

    Returns:
      An iterator object that should first be `.initialize()`-ed. It may then
      either be passed to `strategy.experimental_run()` or you can
      `iterator.get_next()` to get the next value to pass to
      `strategy.extended.call_for_each_replica()`.
    """
    def experimental_make_numpy_dataset(self, numpy_input, session: Incomplete | None = None):
        """Makes a tf.data.Dataset for input provided via a numpy array.

    This avoids adding `numpy_input` as a large constant in the graph,
    and copies the data to the machine or machines that will be processing
    the input.

    Note that you will likely need to use
    tf.distribute.Strategy.experimental_distribute_dataset
    with the returned dataset to further distribute it with the strategy.

    Example:
    ```
    numpy_input = np.ones([10], dtype=np.float32)
    dataset = strategy.experimental_make_numpy_dataset(numpy_input)
    dist_dataset = strategy.experimental_distribute_dataset(dataset)
    ```

    Args:
      numpy_input: A nest of NumPy input arrays that will be converted into a
      dataset. Note that lists of Numpy arrays are stacked, as that is normal
      `tf.data.Dataset` behavior.
      session: (TensorFlow v1.x graph execution only) A session used for
        initialization.

    Returns:
      A `tf.data.Dataset` representing `numpy_input`.
    """
    def experimental_run(self, fn, input_iterator: Incomplete | None = None):
        """Runs ops in `fn` on each replica, with inputs from `input_iterator`.

    DEPRECATED: This method is not available in TF 2.x. Please switch
    to using `run` instead.

    When eager execution is enabled, executes ops specified by `fn` on each
    replica. Otherwise, builds a graph to execute the ops on each replica.

    Each replica will take a single, different input from the inputs provided by
    one `get_next` call on the input iterator.

    `fn` may call `tf.distribute.get_replica_context()` to access members such
    as `replica_id_in_sync_group`.

    IMPORTANT: Depending on the `tf.distribute.Strategy` implementation being
    used, and whether eager execution is enabled, `fn` may be called one or more
    times (once for each replica).

    Args:
      fn: The function to run. The inputs to the function must match the outputs
        of `input_iterator.get_next()`. The output must be a `tf.nest` of
        `Tensor`s.
      input_iterator: (Optional) input iterator from which the inputs are taken.

    Returns:
      Merged return value of `fn` across replicas. The structure of the return
      value is the same as the return value from `fn`. Each element in the
      structure can either be `PerReplica` (if the values are unsynchronized),
      `Mirrored` (if the values are kept in sync), or `Tensor` (if running on a
      single replica).
    """
    def reduce(self, reduce_op, value, axis: Incomplete | None = None): ...
    def update_config_proto(self, config_proto):
        """Returns a copy of `config_proto` modified for use with this strategy.

    DEPRECATED: This method is not available in TF 2.x.

    The updated config has something needed to run a strategy, e.g.
    configuration to run collective ops, or device filters to improve
    distributed training performance.

    Args:
      config_proto: a `tf.ConfigProto` object.

    Returns:
      The updated copy of the `config_proto`.
    """

class StrategyExtendedV2:
    '''Additional APIs for algorithms that need to be distribution-aware.

  Note: For most usage of `tf.distribute.Strategy`, there should be no need to
  call these methods, since TensorFlow libraries (such as optimizers) already
  call these methods when needed on your behalf.


  Some common use cases of functions on this page:

  * _Locality_

  `tf.distribute.DistributedValues` can have the same _locality_ as a
  _distributed variable_, which leads to a mirrored value residing on the same
  devices as the variable (as opposed to the compute devices). Such values may
  be passed to a call to `tf.distribute.StrategyExtended.update` to update the
  value of a variable. You may use
  `tf.distribute.StrategyExtended.colocate_vars_with` to give a variable the
  same locality as another variable. You may convert a "PerReplica" value to a
  variable\'s locality by using `tf.distribute.StrategyExtended.reduce_to` or
  `tf.distribute.StrategyExtended.batch_reduce_to`.

  * _How to update a distributed variable_

  A distributed variable is variables created on multiple devices. As discussed
  in the [glossary](https://www.tensorflow.org/api_docs/python/tf/distribute),
  mirrored variable and SyncOnRead variable are two examples. The standard
  pattern for updating distributed variables is to:

  1. In your function passed to `tf.distribute.Strategy.run`,
     compute a list of (update, variable) pairs. For example, the update might
     be a gradient of the loss with respect to the variable.
  2. Switch to cross-replica mode by calling
     `tf.distribute.get_replica_context().merge_call()` with the updates and
     variables as arguments.
  3. Call
     `tf.distribute.StrategyExtended.reduce_to(VariableAggregation.SUM, t, v)`
     (for one variable) or `tf.distribute.StrategyExtended.batch_reduce_to`
     (for a list of variables) to sum the updates.
  4. Call `tf.distribute.StrategyExtended.update(v)` for each variable to update
     its value.

  Steps 2 through 4 are done automatically by class
  `tf.keras.optimizers.Optimizer` if you call its
  `tf.keras.optimizers.Optimizer.apply_gradients` method in a replica context.

  In fact, a higher-level solution to update a distributed variable is by
  calling `assign` on the variable as you would do to a regular `tf.Variable`.
  You can call the method in both _replica context_ and _cross-replica context_.
  For a _mirrored variable_, calling `assign` in _replica context_ requires you
  to specify the `aggregation` type in the variable constructor. In that case,
  the context switching and sync described in steps 2 through 4 are handled for
  you. If you call `assign` on _mirrored variable_ in _cross-replica context_,
  you can only assign a single value or assign values from another mirrored
  variable or a mirrored `tf.distribute.DistributedValues`. For a _SyncOnRead
  variable_, in _replica context_, you can simply call `assign` on it and no
  aggregation happens under the hood. In _cross-replica context_, you can only
  assign a single value to a SyncOnRead variable. One example case is restoring
  from a checkpoint: if the `aggregation` type of the variable is
  `tf.VariableAggregation.SUM`, it is assumed that replica values were added
  before checkpointing, so at the time of restoring, the value is divided by
  the number of replicas and then assigned to each replica; if the `aggregation`
  type is `tf.VariableAggregation.MEAN`, the value is assigned to each replica
  directly.

  '''
    def __init__(self, container_strategy) -> None: ...
    def variable_created_in_scope(self, v):
        '''Tests whether `v` was created while this strategy scope was active.

    Variables created inside the strategy scope are "owned" by it:

    >>> strategy = tf.distribute.MirroredStrategy()
    >>> with strategy.scope():
    ...   v = tf.Variable(1.)
    >>> strategy.extended.variable_created_in_scope(v)
    True

    Variables created outside the strategy are not owned by it:

    >>> strategy = tf.distribute.MirroredStrategy()
    >>> v = tf.Variable(1.)
    >>> strategy.extended.variable_created_in_scope(v)
    False

    Args:
      v: A `tf.Variable` instance.

    Returns:
      True if `v` was created inside the scope, False if not.
    '''
    def colocate_vars_with(self, colocate_with_variable):
        """Scope that controls which devices variables will be created on.

    No operations should be added to the graph inside this scope, it
    should only be used when creating variables (some implementations
    work by changing variable creation, others work by using a
    tf.compat.v1.colocate_with() scope).

    This may only be used inside `self.scope()`.

    Example usage:

    ```
    with strategy.scope():
      var1 = tf.Variable(...)
      with strategy.extended.colocate_vars_with(var1):
        # var2 and var3 will be created on the same device(s) as var1
        var2 = tf.Variable(...)
        var3 = tf.Variable(...)

      def fn(v1, v2, v3):
        # operates on v1 from var1, v2 from var2, and v3 from var3

      # `fn` runs on every device `var1` is on, `var2` and `var3` will be there
      # too.
      strategy.extended.update(var1, fn, args=(var2, var3))
    ```

    Args:
      colocate_with_variable: A variable created in this strategy's `scope()`.
        Variables created while in the returned context manager will be on the
        same set of devices as `colocate_with_variable`.

    Returns:
      A context manager.
    """
    def reduce_to(self, reduce_op, value, destinations, options: Incomplete | None = None):
        '''Combine (via e.g. sum or mean) values across replicas.

    `reduce_to` aggregates `tf.distribute.DistributedValues` and distributed
    variables. It supports both dense values and `tf.IndexedSlices`.

    This API currently can only be called in cross-replica context. Other
    variants to reduce values across replicas are:
    * `tf.distribute.StrategyExtended.batch_reduce_to`: the batch version of
      this API.
    * `tf.distribute.ReplicaContext.all_reduce`: the counterpart of this API
      in replica context. It supports both batched and non-batched all-reduce.
    * `tf.distribute.Strategy.reduce`: a more convenient method to reduce
      to the host in cross-replica context.

    `destinations` specifies where to reduce the value to, e.g. "GPU:0". You can
    also pass in a `Tensor`, and the destinations will be the device of that
    tensor. For all-reduce, pass the same to `value` and `destinations`.

    It can be used in `tf.distribute.ReplicaContext.merge_call` to write code
    that works for all `tf.distribute.Strategy`.

    >>> @tf.function
    ... def step_fn(var):
    ...
    ...   def merge_fn(strategy, value, var):
    ...     # All-reduce the value. Note that `value` here is a
    ...     # `tf.distribute.DistributedValues`.
    ...     reduced = strategy.extended.reduce_to(tf.distribute.ReduceOp.SUM,
    ...         value, destinations=var)
    ...     strategy.extended.update(var, lambda var, value: var.assign(value),
    ...         args=(reduced,))
    ...
    ...   value = tf.identity(1.)
    ...   tf.distribute.get_replica_context().merge_call(merge_fn,
    ...     args=(value, var))
    >>>
    >>> def run(strategy):
    ...   with strategy.scope():
    ...     v = tf.Variable(0.)
    ...     strategy.run(step_fn, args=(v,))
    ...     return v
    >>>
    >>> run(tf.distribute.MirroredStrategy(["GPU:0", "GPU:1"]))
    MirroredVariable:{
      0: <tf.Variable \'Variable:0\' shape=() dtype=float32, numpy=2.0>,
      1: <tf.Variable \'Variable/replica_1:0\' shape=() dtype=float32, numpy=2.0>
    }
    >>> run(tf.distribute.experimental.CentralStorageStrategy(
    ...     compute_devices=["GPU:0", "GPU:1"], parameter_device="CPU:0"))
    <tf.Variable \'Variable:0\' shape=() dtype=float32, numpy=2.0>
    >>> run(tf.distribute.OneDeviceStrategy("GPU:0"))
    <tf.Variable \'Variable:0\' shape=() dtype=float32, numpy=1.0>

    Args:
      reduce_op: a `tf.distribute.ReduceOp` value specifying how values should
        be combined. Allows using string representation of the enum such as
        "SUM", "MEAN".
      value: a `tf.distribute.DistributedValues`, or a `tf.Tensor` like object.
      destinations: a `tf.distribute.DistributedValues`, a `tf.Variable`, a
        `tf.Tensor` alike object, or a device string. It specifies the devices
        to reduce to. To perform an all-reduce, pass the same to `value` and
        `destinations`. Note that if it\'s a `tf.Variable`, the value is reduced
        to the devices of that variable, and this method doesn\'t update the
        variable.
      options: a `tf.distribute.experimental.CommunicationOptions`. Options to
        perform collective operations. This overrides the default options if the
        `tf.distribute.Strategy` takes one in the constructor. See
        `tf.distribute.experimental.CommunicationOptions` for details of the
        options.

    Returns:
      A tensor or value reduced to `destinations`.
    '''
    def batch_reduce_to(self, reduce_op, value_destination_pairs, options: Incomplete | None = None):
        '''Combine multiple `reduce_to` calls into one for faster execution.

    Similar to `reduce_to`, but accepts a list of (value, destinations) pairs.
    It\'s more efficient than reduce each value separately.

    This API currently can only be called in cross-replica context. Other
    variants to reduce values across replicas are:
    * `tf.distribute.StrategyExtended.reduce_to`: the non-batch version of
      this API.
    * `tf.distribute.ReplicaContext.all_reduce`: the counterpart of this API
      in replica context. It supports both batched and non-batched all-reduce.
    * `tf.distribute.Strategy.reduce`: a more convenient method to reduce
      to the host in cross-replica context.

    See `reduce_to` for more information.

    >>> @tf.function
    ... def step_fn(var):
    ...
    ...   def merge_fn(strategy, value, var):
    ...     # All-reduce the value. Note that `value` here is a
    ...     # `tf.distribute.DistributedValues`.
    ...     reduced = strategy.extended.batch_reduce_to(
    ...         tf.distribute.ReduceOp.SUM, [(value, var)])[0]
    ...     strategy.extended.update(var, lambda var, value: var.assign(value),
    ...         args=(reduced,))
    ...
    ...   value = tf.identity(1.)
    ...   tf.distribute.get_replica_context().merge_call(merge_fn,
    ...     args=(value, var))
    >>>
    >>> def run(strategy):
    ...   with strategy.scope():
    ...     v = tf.Variable(0.)
    ...     strategy.run(step_fn, args=(v,))
    ...     return v
    >>>
    >>> run(tf.distribute.MirroredStrategy(["GPU:0", "GPU:1"]))
    MirroredVariable:{
      0: <tf.Variable \'Variable:0\' shape=() dtype=float32, numpy=2.0>,
      1: <tf.Variable \'Variable/replica_1:0\' shape=() dtype=float32, numpy=2.0>
    }
    >>> run(tf.distribute.experimental.CentralStorageStrategy(
    ...     compute_devices=["GPU:0", "GPU:1"], parameter_device="CPU:0"))
    <tf.Variable \'Variable:0\' shape=() dtype=float32, numpy=2.0>
    >>> run(tf.distribute.OneDeviceStrategy("GPU:0"))
    <tf.Variable \'Variable:0\' shape=() dtype=float32, numpy=1.0>

    Args:
      reduce_op: a `tf.distribute.ReduceOp` value specifying how values should
        be combined. Allows using string representation of the enum such as
        "SUM", "MEAN".
      value_destination_pairs: a sequence of (value, destinations) pairs. See
        `tf.distribute.Strategy.reduce_to` for descriptions.
      options: a `tf.distribute.experimental.CommunicationOptions`. Options to
        perform collective operations. This overrides the default options if the
        `tf.distribute.Strategy` takes one in the constructor. See
        `tf.distribute.experimental.CommunicationOptions` for details of the
        options.

    Returns:
      A list of reduced values, one per pair in `value_destination_pairs`.
    '''
    def update(self, var, fn, args=(), kwargs: Incomplete | None = None, group: bool = True):
        '''Run `fn` to update `var` using inputs mirrored to the same devices.

    `tf.distribute.StrategyExtended.update` takes a distributed variable `var`
    to be updated, an update function `fn`, and `args` and `kwargs` for `fn`. It
    applies `fn` to each component variable of `var` and passes corresponding
    values from `args` and `kwargs`. Neither `args` nor `kwargs` may contain
    per-replica values. If they contain mirrored values, they will be unwrapped
    before calling `fn`. For example, `fn` can be `assign_add` and `args` can be
    a mirrored DistributedValues where each component contains the value to be
    added to this mirrored variable `var`. Calling `update` will call
    `assign_add` on each component variable of `var` with the corresponding
    tensor value on that device.

    Example usage:

    ```python
    strategy = tf.distribute.MirroredStrategy([\'GPU:0\', \'GPU:1\']) # With 2
    devices
    with strategy.scope():
      v = tf.Variable(5.0, aggregation=tf.VariableAggregation.SUM)
    def update_fn(v):
      return v.assign(1.0)
    result = strategy.extended.update(v, update_fn)
    # result is
    # Mirrored:{
    #  0: tf.Tensor(1.0, shape=(), dtype=float32),
    #  1: tf.Tensor(1.0, shape=(), dtype=float32)
    # }
    ```

    If `var` is mirrored across multiple devices, then this method implements
    logic as following:

    ```python
    results = {}
    for device, v in var:
      with tf.device(device):
        # args and kwargs will be unwrapped if they are mirrored.
        results[device] = fn(v, *args, **kwargs)
    return merged(results)
    ```

    Otherwise, this method returns `fn(var, *args, **kwargs)` colocated with
    `var`.

    Args:
      var: Variable, possibly mirrored to multiple devices, to operate on.
      fn: Function to call. Should take the variable as the first argument.
      args: Tuple or list. Additional positional arguments to pass to `fn()`.
      kwargs: Dict with keyword arguments to pass to `fn()`.
      group: Boolean. Defaults to True. If False, the return value will be
        unwrapped.

    Returns:
      By default, the merged return value of `fn` across all replicas.  The
      merged result has dependencies to make sure that if it is evaluated at
      all, the side effects (updates) will happen on every replica. If instead
      "group=False" is specified, this function will return a nest of lists
      where each list has an element per replica, and the caller is responsible
      for ensuring all elements are executed.
    '''
    def value_container(self, value) -> None:
        """Returns the container that this per-replica `value` belongs to.

    Args:
      value: A value returned by `run()` or a variable created in `scope()`.

    Returns:
      A container that `value` belongs to.
      If value does not belong to any container (including the case of
      container having been destroyed), returns the value itself.
      `value in experimental_local_results(value_container(value))` will
      always be true.
    """
    @property
    def experimental_require_static_shapes(self):
        """Returns `True` if static shape is required; `False` otherwise."""
    @property
    def worker_devices(self) -> None:
        """Returns the tuple of all devices used to for compute replica execution.
    """
    @property
    def parameter_devices(self) -> None:
        """Returns the tuple of all devices used to place variables."""

class StrategyExtendedV1(StrategyExtendedV2):
    __doc__: Incomplete
    def experimental_make_numpy_dataset(self, numpy_input, session: Incomplete | None = None):
        """Makes a dataset for input provided via a numpy array.

    This avoids adding `numpy_input` as a large constant in the graph,
    and copies the data to the machine or machines that will be processing
    the input.

    Args:
      numpy_input: A nest of NumPy input arrays that will be distributed evenly
        across all replicas. Note that lists of Numpy arrays are stacked, as
        that is normal `tf.data.Dataset` behavior.
      session: (TensorFlow v1.x graph execution only) A session used for
        initialization.

    Returns:
      A `tf.data.Dataset` representing `numpy_input`.
    """
    def broadcast_to(self, tensor, destinations):
        """Mirror a tensor on one device to all worker devices.

    Args:
      tensor: A Tensor value to broadcast.
      destinations: A mirrored variable or device string specifying the
        destination devices to copy `tensor` to.

    Returns:
      A value mirrored to `destinations` devices.
    """
    def experimental_run_steps_on_iterator(self, fn, iterator, iterations: int = 1, initial_loop_values: Incomplete | None = None):
        """DEPRECATED: please use `run` instead.

    Run `fn` with input from `iterator` for `iterations` times.

    This method can be used to run a step function for training a number of
    times using input from a dataset.

    Args:
      fn: function to run using this distribution strategy. The function must
        have the following signature: `def fn(context, inputs)`. `context` is an
          instance of `MultiStepContext` that will be passed when `fn` is run.
          `context` can be used to specify the outputs to be returned from `fn`
          by calling `context.set_last_step_output`. It can also be used to
          capture non tensor outputs by `context.set_non_tensor_output`. See
          `MultiStepContext` documentation for more information. `inputs` will
          have same type/structure as `iterator.get_next()`. Typically, `fn`
          will use `call_for_each_replica` method of the strategy to distribute
          the computation over multiple replicas.
      iterator: Iterator of a dataset that represents the input for `fn`. The
        caller is responsible for initializing the iterator as needed.
      iterations: (Optional) Number of iterations that `fn` should be run.
        Defaults to 1.
      initial_loop_values: (Optional) Initial values to be passed into the
        loop that runs `fn`. Defaults to `None`. # TODO(priyag): Remove
          initial_loop_values argument when we have a mechanism to infer the
          outputs of `fn`.

    Returns:
      Returns the `MultiStepContext` object which has the following properties,
      among other things:
        - run_op: An op that runs `fn` `iterations` times.
        - last_step_outputs: A dictionary containing tensors set using
        `context.set_last_step_output`. Evaluating this returns the value of
        the tensors after the last iteration.
        - non_tensor_outputs: A dictionary containing anything that was set by
          `fn` by calling `context.set_non_tensor_output`.
    """
    def call_for_each_replica(self, fn, args=(), kwargs: Incomplete | None = None):
        '''Run `fn` once per replica.

    `fn` may call `tf.get_replica_context()` to access methods such as
    `replica_id_in_sync_group` and `merge_call()`.

    `merge_call()` is used to communicate between the replicas and
    re-enter the cross-replica context. All replicas pause their execution
    having encountered a `merge_call()` call. After that the
    `merge_fn`-function is executed. Its results are then unwrapped and
    given back to each replica call. After that execution resumes until
    `fn` is complete or encounters another `merge_call()`.  Example:

    ```python
    # Called once in "cross-replica" context.
    def merge_fn(distribution, three_plus_replica_id):
      # sum the values across replicas
      return sum(distribution.experimental_local_results(three_plus_replica_id))

    # Called once per replica in `distribution`, in a "replica" context.
    def fn(three):
      replica_ctx = tf.get_replica_context()
      v = three + replica_ctx.replica_id_in_sync_group
      # Computes the sum of the `v` values across all replicas.
      s = replica_ctx.merge_call(merge_fn, args=(v,))
      return s + v

    with distribution.scope():
      # in "cross-replica" context
      ...
      merged_results = distribution.run(fn, args=[3])
      # merged_results has the values from every replica execution of `fn`.
      # This statement prints a list:
      print(distribution.experimental_local_results(merged_results))
    ```

    Args:
      fn: function to run (will be run once per replica).
      args: Tuple or list with positional arguments for `fn`.
      kwargs: Dict with keyword arguments for `fn`.

    Returns:
      Merged return value of `fn` across all replicas.
    '''
    def read_var(self, v) -> None:
        """Reads the value of a variable.

    Returns the aggregate value of a replica-local variable, or the
    (read-only) value of any other variable.

    Args:
      v: A variable allocated within the scope of this `tf.distribute.Strategy`.

    Returns:
      A tensor representing the value of `v`, aggregated across replicas if
      necessary.
    """
    def update_non_slot(self, colocate_with, fn, args=(), kwargs: Incomplete | None = None, group: bool = True):
        """Runs `fn(*args, **kwargs)` on `colocate_with` devices.

    Used to update non-slot variables.

    DEPRECATED: TF 1.x ONLY.

    Args:
      colocate_with: Devices returned by `non_slot_devices()`.
      fn: Function to execute.
      args: Tuple or list. Positional arguments to pass to `fn()`.
      kwargs: Dict with keyword arguments to pass to `fn()`.
      group: Boolean. Defaults to True. If False, the return value will be
        unwrapped.

    Returns:
      Return value of `fn`, possibly merged across devices.
    """
    def non_slot_devices(self, var_list) -> None:
        """Device(s) for non-slot variables.

    DEPRECATED: TF 1.x ONLY.

    This method returns non-slot devices where non-slot variables are placed.
    Users can create non-slot variables on these devices by using a block:

    ```python
    with tf.distribute.StrategyExtended.colocate_vars_with(tf.distribute.StrategyExtended.non_slot_devices(...)):
      ...
    ```

    Args:
      var_list: The list of variables being optimized, needed with the
        default `tf.distribute.Strategy`.
    Returns:
      A sequence of devices for non-slot variables.
    """
    @property
    def experimental_between_graph(self) -> None:
        """Whether the strategy uses between-graph replication or not.

      This is expected to return a constant value that will not be changed
      throughout its life cycle.
    """
    @property
    def experimental_should_init(self) -> None:
        """Whether initialization is needed."""
    @property
    def should_checkpoint(self) -> None:
        """Whether checkpointing is needed."""
    @property
    def should_save_summary(self) -> None:
        """Whether saving summaries is needed."""

class ReplicaContextBase:
    """A class with a collection of APIs that can be called in a replica context.

  You can use `tf.distribute.get_replica_context` to get an instance of
  `ReplicaContext`, which can only be called inside the function passed to
  `tf.distribute.Strategy.run`.

  >>> strategy = tf.distribute.MirroredStrategy(['GPU:0', 'GPU:1'])
  >>> def func():
  ...   replica_context = tf.distribute.get_replica_context()
  ...   return replica_context.replica_id_in_sync_group
  >>> strategy.run(func)
  PerReplica:{
    0: <tf.Tensor: shape=(), dtype=int32, numpy=0>,
    1: <tf.Tensor: shape=(), dtype=int32, numpy=1>
  }
  """
    def __init__(self, strategy, replica_id_in_sync_group) -> None:
        """Creates a ReplicaContext.

    Args:
      strategy: A `tf.distribute.Strategy`.
      replica_id_in_sync_group: An integer, a `Tensor` or None. Prefer an
        integer whenever possible to avoid issues with nested `tf.function`. It
        accepts a `Tensor` only to be compatible with `tpu.replicate`.
    """
    def __enter__(self): ...
    def __exit__(self, exception_type: type[BaseException] | None, exception_value: BaseException | None, traceback: types.TracebackType | None) -> None: ...
    def merge_call(self, merge_fn, args=(), kwargs: Incomplete | None = None):
        """Merge args across replicas and run `merge_fn` in a cross-replica context.

    This allows communication and coordination when there are multiple calls
    to the step_fn triggered by a call to `strategy.run(step_fn, ...)`.

    See `tf.distribute.Strategy.run` for an explanation.

    If not inside a distributed scope, this is equivalent to:

    ```
    strategy = tf.distribute.get_strategy()
    with cross-replica-context(strategy):
      return merge_fn(strategy, *args, **kwargs)
    ```

    Args:
      merge_fn: Function that joins arguments from threads that are given as
        PerReplica. It accepts `tf.distribute.Strategy` object as
        the first argument.
      args: List or tuple with positional per-thread arguments for `merge_fn`.
      kwargs: Dict with keyword per-thread arguments for `merge_fn`.

    Returns:
      The return value of `merge_fn`, except for `PerReplica` values which are
      unpacked.
    """
    @property
    def num_replicas_in_sync(self):
        """Returns number of replicas that are kept in sync."""
    @property
    def replica_id_in_sync_group(self):
        """Returns the id of the replica.

    This identifies the replica among all replicas that are kept in sync. The
    value of the replica id can range from 0 to
    `tf.distribute.ReplicaContext.num_replicas_in_sync` - 1.

    NOTE: This is not guaranteed to be the same ID as the XLA replica ID use
    for low-level operations such as collective_permute.

    Returns:
      a `Tensor`.
    """
    @property
    def strategy(self):
        """The current `tf.distribute.Strategy` object."""
    @property
    def devices(self):
        '''Returns the devices this replica is to be executed on, as a tuple of strings.

    NOTE: For `tf.distribute.MirroredStrategy` and
    `tf.distribute.experimental.MultiWorkerMirroredStrategy`, this returns a
    nested
    list of device strings, e.g, [["GPU:0"]].
    '''
    def all_reduce(self, reduce_op, value, options: Incomplete | None = None):
        '''All-reduces `value` across all replicas.

    >>> strategy = tf.distribute.MirroredStrategy(["GPU:0", "GPU:1"])
    >>> def step_fn():
    ...   ctx = tf.distribute.get_replica_context()
    ...   value = tf.identity(1.)
    ...   return ctx.all_reduce(tf.distribute.ReduceOp.SUM, value)
    >>> strategy.experimental_local_results(strategy.run(step_fn))
    (<tf.Tensor: shape=(), dtype=float32, numpy=2.0>,
     <tf.Tensor: shape=(), dtype=float32, numpy=2.0>)

    It supports batched operations. You can pass a list of values and it
    attempts to batch them when possible. You can also specify `options`
    to indicate the desired batching behavior, e.g. batch the values into
    multiple packs so that they can better overlap with computations.

    >>> strategy = tf.distribute.MirroredStrategy(["GPU:0", "GPU:1"])
    >>> def step_fn():
    ...   ctx = tf.distribute.get_replica_context()
    ...   value1 = tf.identity(1.)
    ...   value2 = tf.identity(2.)
    ...   return ctx.all_reduce(tf.distribute.ReduceOp.SUM, [value1, value2])
    >>> strategy.experimental_local_results(strategy.run(step_fn))
    ([<tf.Tensor: shape=(), dtype=float32, numpy=2.0>,
    <tf.Tensor: shape=(), dtype=float32, numpy=4.0>],
    [<tf.Tensor: shape=(), dtype=float32, numpy=2.0>,
    <tf.Tensor: shape=(), dtype=float32, numpy=4.0>])

    Note that all replicas need to participate in the all-reduce, otherwise this
    operation hangs. Note that if there\'re multiple all-reduces, they need to
    execute in the same order on all replicas. Dispatching all-reduce based on
    conditions is usually error-prone.

    Known limitation: if `value` contains `tf.IndexedSlices`, attempting to
    compute gradient w.r.t `value` would result in an error.

    This API currently can only be called in the replica context. Other
    variants to reduce values across replicas are:
    * `tf.distribute.StrategyExtended.reduce_to`: the reduce and all-reduce API
      in the cross-replica context.
    * `tf.distribute.StrategyExtended.batch_reduce_to`: the batched reduce and
      all-reduce API in the cross-replica context.
    * `tf.distribute.Strategy.reduce`: a more convenient method to reduce
      to the host in cross-replica context.

    Args:
      reduce_op: a `tf.distribute.ReduceOp` value specifying how values should
        be combined. Allows using string representation of the enum such as
        "SUM", "MEAN".
      value: a potentially nested structure of `tf.Tensor` or `tf.IndexedSlices` which
        `tf.nest.flatten` accepts. The structure and the shapes of `value` need to be
        same on all replicas.
      options: a `tf.distribute.experimental.CommunicationOptions`. Options to
        perform collective operations. This overrides the default options if the
        `tf.distribute.Strategy` takes one in the constructor. See
        `tf.distribute.experimental.CommunicationOptions` for details of the
        options.

    Returns:
       A nested structure of `tf.Tensor` with the reduced values. The structure
       is the same as `value`.
    '''

class ReplicaContext(ReplicaContextBase):
    __doc__: Incomplete
    def all_gather(self, value, axis, options: Incomplete | None = None):
        '''All-gathers `value` across all replicas along `axis`.

    Note: An `all_gather` method can only be called in replica context. For
    a cross-replica context counterpart, see `tf.distribute.Strategy.gather`.
    All replicas need to participate in the all-gather, otherwise this
    operation hangs. So if `all_gather` is called in any replica, it must be
    called in all replicas.

    Note: If there are multiple `all_gather` calls, they need to be executed in
    the same order on all replicas. Dispatching `all_gather` based on conditions
    is usually error-prone.

    For all strategies except `tf.distribute.TPUStrategy`, the input
    `value` on different replicas must have the same rank, and their shapes must
    be the same in all dimensions except the `axis`-th dimension. In other
    words, their shapes cannot be different in a dimension `d` where `d` does
    not equal to the `axis` argument. For example, given a
    `tf.distribute.DistributedValues` with component tensors of shape
    `(1, 2, 3)` and `(1, 3, 3)` on two replicas, you can call
    `all_gather(..., axis=1, ...)` on it, but not `all_gather(..., axis=0, ...)`
    or `all_gather(..., axis=2, ...)`. However, with
    `tf.distribute.TPUStrategy`, all tensors must have exactly the same rank and
    same shape.

    Note: The input `value` must have a non-zero rank. Otherwise, consider using
    `tf.expand_dims` before gathering them.

    You can pass in a single tensor to all-gather:

    >>> strategy = tf.distribute.MirroredStrategy(["GPU:0", "GPU:1"])
    >>> @tf.function
    ... def gather_value():
    ...   ctx = tf.distribute.get_replica_context()
    ...   local_value = tf.constant([1, 2, 3])
    ...   return ctx.all_gather(local_value, axis=0)
    >>> result = strategy.run(gather_value)
    >>> result
    PerReplica:{
      0: <tf.Tensor: shape=(6,), dtype=int32, numpy=array([1, 2, 3, 1, 2, 3], dtype=int32)>,
      1: <tf.Tensor: shape=(6,), dtype=int32, numpy=array([1, 2, 3, 1, 2, 3], dtype=int32)>
    }
    >>> strategy.experimental_local_results(result)
    (<tf.Tensor: shape=(6,), dtype=int32, numpy=array([1, 2, 3, 1, 2, 3],
    dtype=int32)>,
    <tf.Tensor: shape=(6,), dtype=int32, numpy=array([1, 2, 3, 1, 2, 3],
    dtype=int32)>)


    You can also pass in a nested structure of tensors to all-gather, say, a
    list:

    >>> strategy = tf.distribute.MirroredStrategy(["GPU:0", "GPU:1"])
    >>> @tf.function
    ... def gather_nest():
    ...   ctx = tf.distribute.get_replica_context()
    ...   value_1 = tf.constant([1, 2, 3])
    ...   value_2 = tf.constant([[1, 2], [3, 4]])
    ...   # all_gather a nest of `tf.distribute.DistributedValues`
    ...   return ctx.all_gather([value_1, value_2], axis=0)
    >>> result = strategy.run(gather_nest)
    >>> result
    [PerReplica:{
      0: <tf.Tensor: shape=(6,), dtype=int32, numpy=array([1, 2, 3, 1, 2, 3], dtype=int32)>,
      1: <tf.Tensor: shape=(6,), dtype=int32, numpy=array([1, 2, 3, 1, 2, 3], dtype=int32)>
    }, PerReplica:{
      0: <tf.Tensor: shape=(4, 2), dtype=int32, numpy=
    array([[1, 2],
           [3, 4],
           [1, 2],
           [3, 4]], dtype=int32)>,
      1: <tf.Tensor: shape=(4, 2), dtype=int32, numpy=
    array([[1, 2],
           [3, 4],
           [1, 2],
           [3, 4]], dtype=int32)>
    }]
    >>> strategy.experimental_local_results(result)
    ([<tf.Tensor: shape=(6,), dtype=int32, numpy=array([1, 2, 3, 1, 2, 3], dtype=int32)>,
    <tf.Tensor: shape=(4, 2), dtype=int32, numpy=
    array([[1, 2],
           [3, 4],
           [1, 2],
           [3, 4]], dtype=int32)>],
           [<tf.Tensor: shape=(6,), dtype=int32, numpy=array([1, 2, 3, 1, 2, 3], dtype=int32)>,
           <tf.Tensor: shape=(4, 2), dtype=int32, numpy=
    array([[1, 2],
           [3, 4],
           [1, 2],
           [3, 4]], dtype=int32)>])


    What if you are all-gathering tensors with different shapes on different
    replicas? Consider the following example with two replicas, where you have
    `value` as a nested structure consisting of two items to all-gather, `a` and
    `b`.

    * On Replica 0, `value` is `{\'a\': [0], \'b\': [[0, 1]]}`.
    * On Replica 1, `value` is `{\'a\': [1], \'b\': [[2, 3], [4, 5]]}`.
    * Result for `all_gather` with `axis=0` (on each of the replicas) is:

      ```
      {\'a\': [1, 2], \'b\': [[0, 1], [2, 3], [4, 5]]}
      ```

    Args:
      value: a nested structure of `tf.Tensor` which `tf.nest.flatten` accepts,
        or a `tf.distribute.DistributedValues` instance. The structure of the
        `tf.Tensor` need to be same on all replicas. The underlying tensor
        constructs can only be dense tensors with non-zero rank, NOT
        `tf.IndexedSlices`.
      axis: 0-D int32 Tensor. Dimension along which to gather.
      options: a `tf.distribute.experimental.CommunicationOptions`. Options to
        perform collective operations. This overrides the default options if the
        `tf.distribute.Strategy` takes one in the constructor. See
        `tf.distribute.experimental.CommunicationOptions` for details of the
        options.

    Returns:
       A nested structure of `tf.Tensor` with the gathered values. The structure
       is the same as `value`.
    '''

class ReplicaContextV1(ReplicaContextBase):
    __doc__: Incomplete

class _DefaultDistributionStrategyV1(StrategyV1):
    """Default `tf.distribute.Strategy` if none is explicitly selected."""
    def __init__(self) -> None: ...
    def __deepcopy__(self, memo) -> None: ...

class _DefaultDistributionStrategy(Strategy):
    """Default `tf.distribute.Strategy` if none is explicitly selected."""
    def __init__(self) -> None: ...
    def __deepcopy__(self, memo) -> None: ...

class _DefaultDistributionContext:
    """Context manager setting the default `tf.distribute.Strategy`."""
    def __init__(self, strategy) -> None: ...
    def __enter__(self): ...
    def __exit__(self, exception_type: type[BaseException] | None, exception_value: BaseException | None, traceback: types.TracebackType | None) -> None: ...

class _DefaultDistributionExtended(StrategyExtendedV1):
    """Implementation of _DefaultDistributionStrategy."""
    def __init__(self, container_strategy) -> None: ...
    def colocate_vars_with(self, colocate_with_variable):
        """Does not require `self.scope`."""
    def variable_created_in_scope(self, v): ...
    def read_var(self, replica_local_var): ...
    def value_container(self, value): ...
    @property
    def worker_devices(self) -> None: ...
    @property
    def parameter_devices(self) -> None: ...
    def non_slot_devices(self, var_list): ...
    @property
    def should_checkpoint(self): ...
    @property
    def should_save_summary(self): ...
    class DefaultInputIterator:
        """Default implementation of `InputIterator` for default strategy."""
        def __init__(self, dataset) -> None: ...
        def get_next(self): ...
        def get_next_as_optional(self): ...
        def initialize(self):
            """Initialize underlying iterators.

      Returns:
        A list of any initializer ops that should be run.
      """
        @property
        def initializer(self):
            """Returns a list of ops that initialize the iterator."""

class _DefaultReplicaContext(ReplicaContext):
    """ReplicaContext for _DefaultDistributionStrategy."""
    @property
    def replica_id_in_sync_group(self): ...

distribution_strategy_gauge: Incomplete
distribution_strategy_replica_gauge: Incomplete
distribution_strategy_input_api_counter: Incomplete
