from _typeshed import Incomplete
from tensorflow_estimator.python.estimator import run_config as run_config_lib
from tensorflow_estimator.python.estimator.estimator_export import estimator_export as estimator_export
from typing import NamedTuple

class InputPipelineConfig:
    """Please see the definition of these values in TPUConfig.

  @compatibility(TF2)
  TPU Estimator manages its own TensorFlow graph and session, so it is not
  compatible with TF2 behaviors. We recommend that you migrate to the newer
  `tf.distribute.TPUStrategy`. See the
  [TPU guide](https://www.tensorflow.org/guide/tpu) for details.
  @end_compatibility
  """
    PER_SHARD_V1: int
    PER_HOST_V1: int
    PER_HOST_V2: int
    BROADCAST: int
    SLICED: int

class TPUConfig(NamedTuple('TPUConfig', [('iterations_per_loop', Incomplete), ('num_shards', Incomplete), ('num_cores_per_replica', Incomplete), ('per_host_input_for_training', Incomplete), ('tpu_job_name', Incomplete), ('initial_infeed_sleep_secs', Incomplete), ('input_partition_dims', Incomplete), ('eval_training_input_configuration', Incomplete), ('experimental_host_call_every_n_steps', Incomplete), ('experimental_allow_per_host_v2_parallel_get_next', Incomplete), ('experimental_feed_hook', Incomplete)])):
    """TPU related configuration required by `TPUEstimator`.

  Args:
    iterations_per_loop: This is the number of train steps running in TPU system
      before returning to CPU host for each `Session.run`. This means global
      step is increased `iterations_per_loop` times in one `Session.run`. It is
      recommended to be set as number of global steps for next checkpoint. Note
      that in evaluation don't use this value, instead we run total eval `steps`
      on TPU for a single `Session.run`.
      [Experimental]: `iterations_per_loop` can be specified as a time interval.
        To specify N seconds in one `Session.run`, one can specify it as `Ns`
        and substitute the N with the N with the number of desired seconds.
        Alternatively, the unit of time can also be specified in minutes or
        hours, e.g. `3600s` or `60m` or `1h`.
    num_shards: (Deprecated, ignored by TPUEstimator). The number of model
      replicas in the system. For non-model-parallelism case, this number equals
      the total number of TPU cores. For model-parallelism, the total number of
      TPU cores equals num_cores_per_replica * num_shards.
    num_cores_per_replica: Defaults to `None`, which disables model parallelism.
      An integer which describes the number of TPU cores per model replica. This
      is required by model-parallelism which enables partitioning the model to
      multiple cores. Currently num_cores_per_replica must be 1, 2, 4, or 8.
    per_host_input_for_training: If `True`, for `PER_HOST_V1`, the `input_fn` is
      invoked once on each host, and the number of hosts must be smaller or
      equal to the number of replicas. For PER_HOST_V2, the `input_fn` is
      invoked once for each host (if the number of hosts is less than the number
      of replicas) or replica (if the number of replicas is less than the number
      of hosts. With the per-core input pipeline configuration, it is invoked
      once for each core. With a global batch size `train_batch_size` in
      `TPUEstimator` constructor, the batch size for each shard is
      `train_batch_size` // #hosts in the `True` or `PER_HOST_V1` mode. In
      `PER_HOST_V2` mode, it is `train_batch_size` // #cores. In `BROADCAST`
      mode, `input_fn` is only invoked once on host 0 and the tensors are
      broadcasted to all other replicas. The batch size equals to
      `train_batch_size`. With the per-core input pipeline configuration, the
      shard batch size is also `train_batch_size` // #cores.
      Note: per_host_input_for_training==PER_SHARD_V1 only supports mode.TRAIN.
    tpu_job_name: The name of the TPU job. Typically, this name is auto-inferred
      within TPUEstimator, however when using ClusterSpec propagation in more
      esoteric cluster configurations, you may need to specify the job name as a
      string.
    initial_infeed_sleep_secs: The number of seconds the infeed thread should
      wait before enqueueing the first batch. This helps avoid timeouts for
      models that require a long compilation time.
    input_partition_dims: A nested list to describe the partition dims for all
      the tensors from input_fn(). The structure of input_partition_dims must
      match the structure of `features` and `labels` from input_fn(). The total
      number of partitions must match
      `num_cores_per_replica`. For example, if input_fn() returns two tensors:
        images with shape [N, H, W, C] and labels [N]. input_partition_dims =
        [[1, 2, 2, 1], None] will split the images to 4 pieces and feed into 4
        TPU cores. labels tensor are directly broadcasted to all the TPU cores
        since the partition dims is `None`.
      Current limitations: This feature is only supported with the PER_HOST_V2
        input mode.
    eval_training_input_configuration: If `SLICED`, `input_fn` is only invoked
      once on host 0 and the tensors are broadcasted to all other replicas.
      Unlike per_host_input_for_training=BROADCAST, each replica will only get a
      slice of the data instead of a whole copy. If `PER_HOST_V1`, the behaviour
      is determined by per_host_input_for_training.
    experimental_host_call_every_n_steps: Within a training loop, this argument
      sets how often host calls are performed during training. Host calls will
      be evaluated every n steps within a training loop where n is the value of
      this argument.
    experimental_allow_per_host_v2_parallel_get_next: When enabled, allows
      concurrent execution of dataset get next calls when using PER_HOST_V2
      input. May result in a performance increase for models with a small step
      time, but as a consequence TPUEstimator may non-deterministically
      distribute batches to different cores, rather than guaranteeing round
      robin behavior.
    experimental_feed_hook: This is a class which user can provide to the TPU
      estimator to override the default TPUInfeedOutfeedSessionHook implementation
      and add customized implementatioin to handle infeed outfeed logic. If
      given class is None, TPU estimator uses default TPUInfeedOutfeedSessionHook
      implementation in tpu_estimator.py. If not None, TPU estimator uses this
      customized tpu infeed outfeed session hook class rather to override the
      default one.

  Raises:
      ValueError: If `num_cores_per_replica` is not 1, 2, 4, 8, ..., 128.

  @compatibility(TF2)
  TPU Estimator manages its own TensorFlow graph and session, so it is not
  compatible with TF2 behaviors. We recommend that you migrate to the newer
  `tf.distribute.TPUStrategy`. See the
  [TPU guide](https://www.tensorflow.org/guide/tpu) for details.
  @end_compatibility
  """
    def __new__(cls, iterations_per_loop: int = 2, num_shards: Incomplete | None = None, num_cores_per_replica: Incomplete | None = None, per_host_input_for_training: bool = True, tpu_job_name: Incomplete | None = None, initial_infeed_sleep_secs: Incomplete | None = None, input_partition_dims: Incomplete | None = None, eval_training_input_configuration=..., experimental_host_call_every_n_steps: int = 1, experimental_allow_per_host_v2_parallel_get_next: bool = False, experimental_feed_hook: Incomplete | None = None): ...

class RunConfig(run_config_lib.RunConfig):
    """RunConfig with TPU support."""
    def __init__(self, tpu_config: Incomplete | None = None, evaluation_master: Incomplete | None = None, master: Incomplete | None = None, cluster: Incomplete | None = None, **kwargs) -> None:
        """Constructs a RunConfig.

    Args:
      tpu_config: the TPUConfig that specifies TPU-specific configuration.
      evaluation_master: a string. The address of the master to use for eval.
        Defaults to master if not set.
      master: a string. The address of the master to use for training.
      cluster: a ClusterResolver
      **kwargs: keyword config parameters.

    Raises:
      ValueError: if cluster is not None and the provided session_config has a
        cluster_def already.

    @compatibility(TF2)
    TPU Estimator manages its own TensorFlow graph and session, so it is not
    compatible with TF2 behaviors. We recommend that you migrate to the newer
    `tf.distribute.TPUStrategy`. See the
    [TPU guide](https://www.tensorflow.org/guide/tpu) for details.
    @end_compatibility
    """
    @property
    def evaluation_master(self): ...
    @property
    def master(self): ...
    @property
    def tpu_config(self): ...
    @property
    def cluster(self): ...
    def replace(self, **kwargs): ...
