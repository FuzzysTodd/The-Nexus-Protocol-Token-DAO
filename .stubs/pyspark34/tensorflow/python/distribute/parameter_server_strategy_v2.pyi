from _typeshed import Incomplete
from tensorflow.python.distribute import device_util as device_util, distribute_lib as distribute_lib, input_lib as input_lib, input_util as input_util, mirrored_run as mirrored_run, multi_worker_util as multi_worker_util, parameter_server_strategy as parameter_server_strategy, ps_values as ps_values, sharded_variable as sharded_variable, values as values
from tensorflow.python.eager import remote as remote
from tensorflow.python.framework import config as config, ops as ops, tensor_shape as tensor_shape
from tensorflow.python.ops import array_ops as array_ops, resource_variable_ops as resource_variable_ops
from tensorflow.python.training import server_lib as server_lib
from tensorflow.python.util import keras_deps as keras_deps, nest as nest, tf_inspect as tf_inspect
from tensorflow.python.util.lazy_loader import LazyLoader as LazyLoader
from tensorflow.python.util.tf_export import tf_export as tf_export

ALLOWED_TASK_TYPES: Incomplete
cluster_coordinator: Incomplete

class ParameterServerStrategyV2(distribute_lib.Strategy):
    '''An multi-worker tf.distribute strategy with parameter servers.

  Parameter server training is a common data-parallel method to scale up a
  machine learning model on multiple machines. A parameter server training
  cluster consists of workers and parameter servers. Variables are created on
  parameter servers and they are read and updated by workers in each step.
  By default, workers read and update these variables independently without
  synchronizing with each other. Under this configuration, it is known as
  asynchronous training.

  In TensorFlow 2, we recommend an architecture based on central coordination
  for parameter server training. Each worker and parameter server runs a
  `tf.distribute.Server`, and on top of that, a coordinator task is responsible
  for creating resources on workers and parameter servers, dispatching
  functions, and coordinating the training. The coordinator uses a
  `tf.distribute.experimental.coordinator.ClusterCoordinator` to coordinate the
  cluster, and a `tf.distribute.experimental.ParameterServerStrategy` to define
  variables on parameter servers and computation on workers.

  For the training to work, the coordinator dispatches `tf.function`s to be
  executed on remote workers. Upon receiving requests from the coordinator, a
  worker executes the `tf.function` by reading the variables from parameter
  servers, executing the ops, and updating the variables on the parameter
  servers. Each of the worker only processes the requests from the coordinator,
  and communicates with parameter servers, without direct interactions with
  other workers in the cluster.

  As a result, failures of some workers do not prevent the cluster from
  continuing the work, and this allows the cluster to train with instances that
  can be occasionally unavailable (e.g. preemptible or spot instances). The
  coordinator and parameter servers though, must be available at all times for
  the cluster to make progress.

  Note that the coordinator is not one of the training workers. Instead, it
  creates resources such as variables and datasets, dispatches `tf.function`s,
  saves checkpoints and so on. In addition to workers, parameter servers and
  the coordinator, an optional evaluator can be run on the side that
  periodically reads the checkpoints saved by the coordinator and runs
  evaluations against each checkpoint.

  `ParameterServerStrategy` is supported with two training APIs: [Custom
  Training Loop (CTL)]
  (https://www.tensorflow.org/tutorials/distribute/custom_training)
  and [Keras Training API, also known as `Model.fit`]
  (https://www.tensorflow.org/tutorials/distribute/keras). CTL is recommended
  when users prefer to define the details of their training loop, and
  `Model.fit` is recommended when users prefer a high-level abstraction and
  handling of training.

  When using a CTL, `ParameterServerStrategy` has to work in conjunction with a
  `tf.distribute.experimental.coordinator.ClusterCoordinator` object.

  When using `Model.fit`, currently only the
  `tf.keras.utils.experimental.DatasetCreator` input type is supported.

  __Example code for coordinator__

  This section provides code snippets that are intended to be run on (the only)
  one task that is designated as the coordinator. Note that `cluster_resolver`,
  `variable_partitioner`, and `dataset_fn` arguments are explained in the
  following "Cluster setup", "Variable partitioning", and "Dataset preparation"
  sections.

  With a CTL,

  ```python
  # Prepare a strategy to use with the cluster and variable partitioning info.
  strategy = tf.distribute.experimental.ParameterServerStrategy(
      cluster_resolver=...,
      variable_partitioner=...)
  coordinator = tf.distribute.experimental.coordinator.ClusterCoordinator(
      strategy=strategy)

  # Prepare a distribute dataset that will place datasets on the workers.
  distributed_dataset = coordinator.create_per_worker_dataset(dataset_fn=...)

  with strategy.scope():
    model = ...
    optimizer, metrics = ...  # Keras optimizer/metrics are great choices
    checkpoint = tf.train.Checkpoint(model=model, optimizer=optimizer)
    checkpoint_manager = tf.train.CheckpointManager(
        checkpoint, checkpoint_dir, max_to_keep=2)
    # `load_checkpoint` infers initial epoch from `optimizer.iterations`.
    initial_epoch = load_checkpoint(checkpoint_manager) or 0

  @tf.function
  def worker_fn(iterator):

    def replica_fn(inputs):
      batch_data, labels = inputs
      # calculate gradient, applying gradient, metrics update etc.

    strategy.run(replica_fn, args=(next(iterator),))

  for epoch in range(initial_epoch, num_epoch):
    distributed_iterator = iter(distributed_dataset)  # Reset iterator state.
    for step in range(steps_per_epoch):

      # Asynchronously schedule the `worker_fn` to be executed on an arbitrary
      # worker. This call returns immediately.
      coordinator.schedule(worker_fn, args=(distributed_iterator,))

    # `join` blocks until all scheduled `worker_fn`s finish execution. Once it
    # returns, we can read the metrics and save checkpoints as needed.
    coordinator.join()
    logging.info(\'Metric result: %r\', metrics.result())
    train_accuracy.reset_states()
    checkpoint_manager.save()
  ```

  With `Model.fit`,

  ```python
  # Prepare a strategy to use with the cluster and variable partitioning info.
  strategy = tf.distribute.experimental.ParameterServerStrategy(
      cluster_resolver=...,
      variable_partitioner=...)

  # A dataset function takes a `input_context` and returns a `Dataset`
  def dataset_fn(input_context):
    dataset = tf.data.Dataset.from_tensors(...)
    return dataset.repeat().shard(...).batch(...).prefetch(...)

  # With `Model.fit`, a `DatasetCreator` needs to be used.
  input = tf.keras.utils.experimental.DatasetCreator(dataset_fn=...)

  with strategy.scope():
    model = ...  # Make sure the `Model` is created within scope.
  model.compile(optimizer="rmsprop", loss="mse", steps_per_execution=..., ...)

  # Optional callbacks to checkpoint the model, back up the progress, etc.
  callbacks = [tf.keras.callbacks.ModelCheckpoint(...), ...]

  # `steps_per_epoch` is required with `ParameterServerStrategy`.
  model.fit(input, epochs=..., steps_per_epoch=..., callbacks=callbacks)
  ```

  __Example code for worker and parameter servers__

  In addition to the coordinator, there should be tasks designated as
  "worker" or "ps". They should run the following code to start a TensorFlow
  server, waiting for coordinator\'s requests:

  ```python
  # Provide a `tf.distribute.cluster_resolver.ClusterResolver` that serves
  # the cluster information. See below "Cluster setup" section.
  cluster_resolver = ...

  server = tf.distribute.Server(
      cluster_resolver.cluster_spec(),
      job_name=cluster_resolver.task_type,
      task_index=cluster_resolver.task_id,
      protocol="grpc")

  # Blocking the process that starts a server from exiting.
  server.join()
  ```

  __Cluster setup__

  In order for the tasks in the cluster to know other tasks\' addresses,
  a `tf.distribute.cluster_resolver.ClusterResolver` is required to be used
  in coordinator, worker, and ps. The
  `tf.distribute.cluster_resolver.ClusterResolver` is responsible for providing
  the cluster information, as well as the task type and id of the current task.
  See `tf.distribute.cluster_resolver.ClusterResolver` for more information.

  If `TF_CONFIG` environment variable is set, a
  `tf.distribute.cluster_resolver.TFConfigClusterResolver` should be used as
  well.

  Since there are assumptions in
  `tf.distribute.experimental.ParameterServerStrategy` around the naming of the
  task types, "chief", "ps", and "worker" should be used in the
  `tf.distribute.cluster_resolver.ClusterResolver` to refer to the coordinator,
  parameter servers, and workers, respectively.

  The following example demonstrates setting `TF_CONFIG` for the task designated
  as a parameter server (task type "ps") and index 1 (the second task), in a
  cluster with 1 chief, 2 parameter servers, and 3 workers. Note that it needs
  to be set before the use of
  `tf.distribute.cluster_resolver.TFConfigClusterResolver`.

  Example code for cluster setup:
  ```python
  os.environ[\'TF_CONFIG\'] = \'\'\'
  {
    "cluster": {
      "chief": ["chief.example.com:2222"],
      "ps": ["ps0.example.com:2222", "ps1.example.com:2222"],
      "worker": ["worker0.example.com:2222", "worker1.example.com:2222",
                 "worker2.example.com:2222"]
    },
    "task": {
      "type": "ps",
      "index": 1
    }
  }
  \'\'\'
  ```

  If you prefer to run the same binary for all tasks, you will need to let the
  binary branch into different roles at the beginning of the program:
  ```python
  # If coordinator, create a strategy and start the training program.
  if cluster_resolver.task_type == \'chief\':
    strategy = tf.distribute.experimental.ParameterServerStrategy(
        cluster_resolver)
    ...

  # If worker/ps, create a server
  elif cluster_resolver.task_type in ("worker", "ps"):
    server = tf.distribute.Server(...)
    ...
  ```
  Alternatively, you can also start a bunch of TensorFlow servers in advance and
  connect to them later. The coordinator can be in the same cluster or on any
  machine that has connectivity to workers and parameter servers. This is
  covered in our guide and tutorial.

  __Variable creation with `strategy.scope()`__

  `tf.distribute.experimental.ParameterServerStrategy` follows the
  `tf.distribute` API contract where variable creation is expected to be inside
  the context manager returned by `strategy.scope()`, in order to be correctly
  placed on parameter servers in a round-robin manner:

  ```python
  # In this example, we\'re assuming having 3 ps.
  strategy = tf.distribute.experimental.ParameterServerStrategy(
      cluster_resolver=...)
  coordinator = tf.distribute.experimental.coordinator.ClusterCoordinator(
      strategy=strategy)

  # Variables should be created inside scope to be placed on parameter servers.
  # If created outside scope such as `v1` here, it would be placed on the
  # coordinator.
  v1 = tf.Variable(initial_value=0.0)

  with strategy.scope():
    v2 = tf.Variable(initial_value=1.0)
    v3 = tf.Variable(initial_value=2.0)
    v4 = tf.Variable(initial_value=3.0)
    v5 = tf.Variable(initial_value=4.0)

  # v2 through v5 are created in scope and are distributed on parameter servers.
  # Default placement is round-robin but the order should not be relied on.
  assert v2.device == "/job:ps/replica:0/task:0/device:CPU:0"
  assert v3.device == "/job:ps/replica:0/task:1/device:CPU:0"
  assert v4.device == "/job:ps/replica:0/task:2/device:CPU:0"
  assert v5.device == "/job:ps/replica:0/task:0/device:CPU:0"
  ```

  See `distribute.Strategy.scope` for more information.

  __Variable partitioning__

  Having dedicated servers to store variables means being able to divide up, or
  "shard" the variables across the ps. Partitioning large variable among ps is a
  commonly used technique to boost training throughput and mitigate memory
  constraints. It enables parallel computations and updates on different shards
  of a variable, and often yields better load balancing across parameter
  servers. Without sharding, models with large variables (e.g, embeddings) that
  can\'t fit into one machine\'s memory would otherwise be unable to train.

  With `tf.distribute.experimental.ParameterServerStrategy`, if a
  `variable_partitioner` is provided to `__init__` and certain conditions are
  satisfied, the resulting variables created in scope are sharded across the
  parameter servers, in a round-robin fashion. The variable reference returned
  from `tf.Variable` becomes a type that serves as the container of the sharded
  variables. One can access `variables` attribute of this container for the
  actual variable components. If building model with `tf.Module` or Keras,
  the variable components are collected in the `variables` alike attributes.

  It is recommended to use size-based partitioners like
  `tf.distribute.experimental.partitioners.MinSizePartitioner` to avoid
  partitioning small variables, which could have negative impact on model
  training speed.

  ```python
  # Partition the embedding layer into 2 shards.
  variable_partitioner = (
    tf.distribute.experimental.partitioners.MinSizePartitioner(
      min_shard_bytes=(256 << 10),
      max_shards = 2))
  strategy = tf.distribute.experimental.ParameterServerStrategy(
    cluster_resolver=...,
    variable_partitioner = variable_partitioner)
  with strategy.scope():
    embedding = tf.keras.layers.Embedding(input_dim=1024, output_dim=1024)
  assert len(embedding.variables) == 2
  assert isinstance(embedding.variables[0], tf.Variable)
  assert isinstance(embedding.variables[1], tf.Variable)
  assert embedding.variables[0].shape == (512, 1024)
  assert embedding.variables[1].shape == (512, 1024)
  ```

  The sharded variable container can be converted to a `Tensor` via
  `tf.convert_to_tensor`. This means the container can be directly used in most
  Python Ops where such `Tensor` conversion automatically happens. For example,
  in the above code snippet, `x * self.w` would implicitly apply the said tensor
  conversion. Note that such conversion can be expensive, as the variable
  components need to be transferred from multiple parameter servers to where
  the value is used.

  `tf.nn.embedding_lookup` on the other hand doesn\'t apply the tensor
  conversion, and performs parallel lookups on the variable components instead.
  This is crucial to scale up embedding lookups when the embedding table
  variable is large.

  When a partitioned variable is saved to a `SavedModel`, it will be saved as if
  it is one single variable. This improves serving efficiency by eliminating
  a number of Ops that handle the partiton aspects.

  Known limitations of variable partitioning:

  * Number of partitions must not change across Checkpoint saving/loading.

  * After saving partitioned variables to a SavedModel, the SavedModel can\'t be
    loaded via `tf.saved_model.load`.

  * Partition variable doesn\'t directly work with `tf.GradientTape`, please use
    the `variables` attributes to get the actual variable components and use
    them in gradient APIs instead.

  __Dataset preparation__

  With `tf.distribute.experimental.ParameterServerStrategy`, a dataset is
  created in each of the workers to be used for training. This is done by
  creating a `dataset_fn` that takes no argument and returns a
  `tf.data.Dataset`, and passing the `dataset_fn` into
  `tf.distribute.experimental.coordinator.
  ClusterCoordinator.create_per_worker_dataset`. We recommend the dataset to be
  shuffled and repeated to have the examples run through the training as evenly
  as possible.

  ```python
  def dataset_fn():
    filenames = ...
    dataset = tf.data.Dataset.from_tensor_slices(filenames)

    # Dataset is recommended to be shuffled, and repeated.
    return dataset.shuffle(buffer_size=...).repeat().batch(batch_size=...)

  coordinator =
      tf.distribute.experimental.coordinator.ClusterCoordinator(strategy=...)
  distributed_dataset = coordinator.create_per_worker_dataset(dataset_fn)
  ```

  __Limitations__

  * `tf.distribute.experimental.ParameterServerStrategy` in TF2 is experimental,
  and the API is subject to further changes.

  * When using `Model.fit`, `tf.distribute.experimental.ParameterServerStrategy`
  must be used with a `tf.keras.utils.experimental.DatasetCreator`, and
  `steps_per_epoch` must be specified.
  '''
    def __init__(self, cluster_resolver, variable_partitioner: Incomplete | None = None) -> None:
        """Initializes the TF2 parameter server strategy.

    This initializes the `tf.distribute.experimental.ParameterServerStrategy`
    object to be ready for use with
    `tf.distribute.experimental.coordinator.ClusterCoordinator`.

    Args:
      cluster_resolver: a `tf.distribute.cluster_resolver.ClusterResolver`
        object.
      variable_partitioner:
        a `distribute.experimental.partitioners.Partitioner` that specifies
        how to partition variables. If `None`, variables will not be
        partitioned.

        * Predefined partitioners in `tf.distribute.experimental.partitioners`
        can be used for this argument. A commonly used partitioner is
        `MinSizePartitioner(min_shard_bytes = 256 << 10, max_shards = num_ps)`,
        which allocates at least 256K per shard, and each ps gets at most one
        shard.

        * `variable_partitioner` will be called for each variable created under
        strategy `scope` to instruct how the variable should be partitioned.
        Variables that have only one partition along the partitioning axis
        (i.e., no need for partition) will be created as a normal `tf.Variable`.

        * Only the first / outermost axis partitioning is supported.

        * Div partition strategy is used to partition variables. Assuming we
        assign consecutive integer ids along the first axis of a variable, then
        ids are assigned to shards in a contiguous manner, while attempting to
        keep each shard size identical. If the ids do not evenly divide the
        number of shards, each of the first several shards will be assigned one
        more id. For instance, a variable whose first dimension is 13 has 13
        ids, and they are split across 5 shards as:
        `[[0, 1, 2], [3, 4, 5], [6, 7, 8], [9, 10], [11, 12]]`.

        * Variables created under `strategy.extended.colocate_vars_with` will
        not be partitioned.
    """

class ParameterServerStrategyV2Extended(parameter_server_strategy.ParameterServerStrategyExtended):
    """Extended class for ParameterServerStrategyV2.

  Please see `tf.distribute.StrategyExtended` doc for more information.
  """
    def __init__(self, container_strategy, cluster_resolver, variable_partitioner) -> None:
        """Initialization of ParameterServerStrategyV2Extended."""
    @property
    def worker_devices(self): ...
