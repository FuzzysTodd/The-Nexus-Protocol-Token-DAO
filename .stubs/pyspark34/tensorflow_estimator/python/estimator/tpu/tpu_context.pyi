import tensorflow as tf
from _typeshed import Incomplete
from collections.abc import Generator
from tensorflow_estimator.python.estimator.tpu import tpu_config as tpu_config

class TPUContext:
    """A context that holds the current configuration of the TPU computation.

  TPUContext was designed for getting TPU context information when calling
  input_fn. It can be called in model_fn as well.

  User is not expected to construct the instance from constructor. The only
  legitimate way to get the instance is either in `input_fn`:

  ```
  def input_fn(params):
    batch_size = params['batch_size']
    context = params['context']
    # ...
  ```

  or in `model_fn`

  ```
  def model_fn(params):
    batch_size = params['batch_size']
    context = params['context']
    # ...
  ```

  Most of the fields of TPUContext are useful for both `input_fn` and
  `model_fn`. Exceptions are:

  1. `input_fn` only:

    current_input_fn_deployment
    current_host

  2. `model_fn` only:

    device_assignment

  """
    def __init__(self, internal_ctx, input_device: Incomplete | None = None, invocation_index: Incomplete | None = None, call_from_input_fn: bool = True, host_id: Incomplete | None = None) -> None: ...
    def current_input_fn_deployment(self):
        """The configuration of the current input_fn invocation.

    The configuration depends on `TPUConfig.per_host_input_for_training`. See
    `TPUConfig` for details.

    Only set in params dict of input_fn

    Returns:
      A tuple of
        1. Device spec string: String, is the current CPU host where the
           input_fn is invoked.
        2. Current invocation index: Int, 0-based index of the input_fn
           invocation. See next item for details.
        3. Total invocation count: Int, the total number of times to invoke the
           input_fn on all CPU hosts. Each invocation will be passed with a new
           `TPUContext` instance with current invocation index set properly.
        4. Total number of replicas consumed by current_invocation: Int, the
           number of replicas fed by the data returned by current input_fn. For
           example, for per_core input pipeline deployment
           and non-model-parallelism, total invocation count is equal to
           the number of cores in the system and num replicas consumed by
           current invocation is 1. For per-host v2 input pipeline deployment,
           total invocation count is equal to the number of hosts in the system
           and num replicas consumed by current invocation is equal to number of
           replicas per host.

    Raises:
      RuntimeError: If this method is not be called from input_fn.
    """
    @property
    def num_replicas(self):
        """The total number of replicas.

    For non-model-parallelism, num_replicas should be the total num of TPU
    cores in the system.

    Returns:
      The number of replicas.
    """
    @property
    def num_hosts(self):
        """The number of hosts for the TPU system."""
    @property
    def current_host(self):
        """The current host index for the TPU system.

    Returns:
      The host index (int).

    Raises:
      RuntimeError: If this method is not be called from input_fn.
    """
    @property
    def num_of_replicas_per_host(self):
        """The number of replicas for each host."""
    @property
    def device_assignment(self):
        """Returns device_assignment object.

    Raises:
      RuntimeError: If this method is not be called from model_fn.
    """
    def device_for_replica(self, replica_id):
        """Returns the tuple of (CPU device and device ordinal) for replica.

    This should be used for full replicate for non-model-parallelism.

    Args:
       replica_id: Int, the replica index.

    Returns:
       A tuple of device spec for CPU device and int device ordinal.
    """
    @property
    def tpu_host_placement_function(self):
        """Returns the TPU host place function.

    The place function takes host_id as the input and returns the TF device
    for the correspoding host.
    """

class _InternalTPUContext:
    """A context holds immutable states of TPU computation.

  This immutable object holds TPUEstimator config, train/eval batch size, and
  `TPUEstimator.use_tpu`, which is expected to be passed around. It also
  provides utility functions, based on the current state, to determine other
  information commonly required by TPU computation, such as TPU device names,
  TPU hosts, shard batch size, etc.

  if eval_on_tpu is False, then execution of eval on TPU is disabled.
  if eval_on_tpu is True, but use_tpu is False, a warning is issued,
  and TPU execution is disabled for all modes.

  N.B. As `mode` is not immutable state in Estimator, but essential to
  distinguish between TPU training and evaluation, a common usage for
  _InternalTPUContext with `mode` is as follows:
  ```
  with _ctx.with_mode(mode) as ctx:
    if ctx.is_running_on_cpu():
       ...
  ```
  """
    def __init__(self, config, train_batch_size, eval_batch_size, predict_batch_size, use_tpu, eval_on_tpu: bool = True, embedding_config_spec: Incomplete | None = None) -> None: ...
    def with_mode(self, mode) -> Generator[Incomplete, None, None]: ...
    @property
    def mode(self): ...
    @property
    def tensor_core_embedding_columns(self): ...
    @property
    def embedding_config(self):
        """Returns the embedding config based on current mode."""
    @property
    def allow_per_host_v2_parallel_get_next(self): ...
    @property
    def feed_hook(self): ...
    @property
    def model_parallelism_enabled(self): ...
    @property
    def input_partition_dims(self): ...
    @property
    def device_assignment(self): ...
    @property
    def num_of_cores_per_host(self): ...
    @property
    def num_cores(self): ...
    @property
    def num_of_replicas_per_host(self):
        """Return the number of replicas per host."""
    @property
    def num_replicas(self):
        """Compute the total number of replicas."""
    @property
    def num_hosts(self): ...
    @property
    def config(self): ...
    def is_input_sharded_per_core(self):
        """Return true if input_fn is invoked per-core (other than per-host)."""
    def is_input_per_host_with_iterators(self):
        """Return true if input_fn should be run in the per-host v2 config."""
    def is_input_broadcast_with_iterators(self):
        """Return true if input_fn should be run in the full_replicae config."""
    def is_input_slice_broadcast_to_all_cores(self):
        """Return true if input_fn is invoked once and broadcast to other hosts."""
    def is_replica_across_hosts(self):
        """Return true if single replica is across multiple hosts."""
    def is_running_on_cpu(self, is_export_mode: bool = False):
        """Determines whether the input_fn and model_fn should be invoked on CPU.

    This API also validates user provided configuration, such as batch size,
    according the lazy initialized TPU system metadata.

    Args:
      is_export_mode: Indicates whether the current mode is for exporting the
        model, when mode == PREDICT. Only with this bool, we could tell whether
        user is calling the Estimator.predict or Estimator.export_savedmodel,
        which are running on TPU and CPU respectively. Parent class Estimator
        does not distinguish these two.

    Returns:
      bool, whether current input_fn or model_fn should be running on CPU.

    Raises:
      ValueError: any configuration is invalid.
    """
    @property
    def global_batch_size(self): ...
    @property
    def batch_size_for_input_fn(self):
        """Returns the shard batch size for `input_fn`."""
    @property
    def batch_size_for_model_fn(self):
        """Returns the shard batch size for `model_fn`."""
    @property
    def master_job(self):
        """Returns the job name to use to place TPU computations on.

    Returns:
      A string containing the job name, or None if no job should be specified.

    Raises:
      ValueError: If the user needs to specify a tpu_job_name, because we are
        unable to infer the job name automatically, or if the user-specified job
        names are inappropriate.
    """
    @property
    def tpu_host_placement_function(self):
        """Returns the TPU host place function."""
    @property
    def tpu_device_placement_function(self):
        """Returns a TPU device placement Fn."""
    def tpu_ordinal_function(self, host_id):
        """Returns the TPU ordinal fn."""
    def device_for_replica(self, replica_id):
        """Returns the tuple of (CPU device and device ordinal) for replica.

    This should be used for full replicate for non-model-parallelism.

    Args:
       replica_id: Int, the replica index.

    Returns:
       A tuple of device spec for CPU device and int device ordinal.
    """

class _OneCoreTPUContext(_InternalTPUContext):
    """Special _InternalTPUContext for one core usage."""
    def __init__(self, config, train_batch_size, eval_batch_size, predict_batch_size, use_tpu) -> None: ...

class _TPUEstimatorReplicaContext(tf.distribute.ReplicaContext):
    """Internal context for storing replica id.

  This is to set eager.context.Context() so that only summary ops from
  0th replica is executed.
  """
    def __init__(self, replica_id_in_sync) -> None:
        """Creates internal replica context for TPUEstimator.

    Args:
      replica_id_in_sync: Zero indexed integer id of replica that is running the
        TPU compuation.
    """
    def __enter__(self): ...
    def __exit__(self, exception_type: type[BaseException] | None, exception_value: BaseException | None, traceback: types.TracebackType | None) -> None: ...
