import enum
from _typeshed import Incomplete
from tensorflow.core.framework import dataset_options_pb2 as dataset_options_pb2, model_pb2 as model_pb2
from tensorflow.python.data.util import options as options_lib
from tensorflow.python.util import deprecation as deprecation
from tensorflow.python.util.tf_export import tf_export as tf_export

class AutotuneAlgorithm(enum.Enum):
    """Represents the type of autotuning algorithm to use.

  DEFAULT: The default behavior is implementation specific and may change over
  time.

  HILL_CLIMB: In each optimization step, this algorithm chooses the optimial
  parameter and increases its value by 1.

  GRADIENT_DESCENT: In each optimization step, this algorithm updates the
  parameter values in the optimal direction.

  MAX_PARALLELISM: Similar to HILL_CLIMB but uses a relaxed stopping condition,
  allowing the optimization to oversubscribe the CPU.

  STAGE_BASED: In each optimization step, this algorithm chooses the worst
  bottleneck parameter and increases its value by 1.
  """
    DEFAULT: int
    HILL_CLIMB: int
    GRADIENT_DESCENT: int
    MAX_PARALLELISM: int
    STAGE_BASED: int

class AutoShardPolicy(enum.IntEnum):
    """Represents the type of auto-sharding to use.

  OFF: No sharding will be performed.

  AUTO: Attempts FILE-based sharding, falling back to DATA-based sharding.

  FILE: Shards by input files (i.e. each worker will get a set of files to
  process). When this option is selected, make sure that there is at least as
  many files as workers. If there are fewer input files than workers, a runtime
  error will be raised.

  DATA: Shards by elements produced by the dataset. Each worker will process the
  whole dataset and discard the portion that is not for itself. Note that for
  this mode to correctly partitions the dataset elements, the dataset needs to
  produce elements in a deterministic order.

  HINT: Looks for the presence of `shard(SHARD_HINT, ...)` which is treated as a
  placeholder to replace with `shard(num_workers, worker_index)`.
  """
    OFF: int
    AUTO: int
    FILE: int
    DATA: int
    HINT: int

class ExternalStatePolicy(enum.Enum):
    """Represents how to handle external state during serialization.

  See the `tf.data.Options.experimental_external_state_policy` documentation
  for more information.
  """
    WARN: int
    IGNORE: int
    FAIL: int

class AutotuneOptions(options_lib.OptionsBase):
    """Represents options for autotuning dataset performance.

  ```python
  options = tf.data.Options()
  options.autotune.enabled = False
  dataset = dataset.with_options(options)
  ```
  """
    enabled: Incomplete
    cpu_budget: Incomplete
    ram_budget: Incomplete
    autotune_algorithm: Incomplete

class DistributeOptions(options_lib.OptionsBase):
    """Represents options for distributed data processing.

  You can set the distribution options of a dataset through the
  `experimental_distribute` property of `tf.data.Options`; the property is
  an instance of `tf.data.experimental.DistributeOptions`.

  ```python
  options = tf.data.Options()
  options.experimental_distribute.auto_shard_policy = tf.data.experimental.AutoShardPolicy.OFF
  dataset = dataset.with_options(options)
  ```
  """
    auto_shard_policy: Incomplete
    num_devices: Incomplete

class OptimizationOptions(options_lib.OptionsBase):
    """Represents options for dataset optimizations.

  You can set the optimization options of a dataset through the
  `experimental_optimization` property of `tf.data.Options`; the property is
  an instance of `tf.data.experimental.OptimizationOptions`.

  ```python
  options = tf.data.Options()
  options.experimental_optimization.noop_elimination = True
  options.experimental_optimization.apply_default_optimizations = False
  dataset = dataset.with_options(options)
  ```
  """
    apply_default_optimizations: Incomplete
    filter_fusion: Incomplete
    filter_parallelization: Incomplete
    inject_prefetch: Incomplete
    map_and_batch_fusion: Incomplete
    map_and_filter_fusion: Incomplete
    map_fusion: Incomplete
    map_parallelization: Incomplete
    noop_elimination: Incomplete
    parallel_batch: Incomplete
    shuffle_and_repeat_fusion: Incomplete

class ThreadingOptions(options_lib.OptionsBase):
    """Represents options for dataset threading.

  You can set the threading options of a dataset through the
  `experimental_threading` property of `tf.data.Options`; the property is
  an instance of `tf.data.ThreadingOptions`.

  ```python
  options = tf.data.Options()
  options.threading.private_threadpool_size = 10
  dataset = dataset.with_options(options)
  ```
  """
    max_intra_op_parallelism: Incomplete
    private_threadpool_size: Incomplete

class Options(options_lib.OptionsBase):
    """Represents options for `tf.data.Dataset`.

  A `tf.data.Options` object can be, for instance, used to control which static
  optimizations to apply to the input pipeline graph or whether to use
  performance modeling to dynamically tune the parallelism of operations such as
  `tf.data.Dataset.map` or `tf.data.Dataset.interleave`.

  The options are set for the entire dataset and are carried over to datasets
  created through tf.data transformations.

  The options can be set by constructing an `Options` object and using the
  `tf.data.Dataset.with_options(options)` transformation, which returns a
  dataset with the options set.

  >>> dataset = tf.data.Dataset.range(42)
  >>> options = tf.data.Options()
  >>> options.deterministic = False
  >>> dataset = dataset.with_options(options)
  >>> print(dataset.options().deterministic)
  False

  Note: A known limitation of the `tf.data.Options` implementation is that the
  options are not preserved across tf.function boundaries. In particular, to
  set options for a dataset that is iterated within a tf.function, the options
  need to be set within the same tf.function.
  """
    autotune: Incomplete
    deterministic: Incomplete
    experimental_deterministic: Incomplete
    experimental_distribute: Incomplete
    experimental_external_state_policy: Incomplete
    experimental_optimization: Incomplete
    experimental_slack: Incomplete
    experimental_symbolic_checkpoint: Incomplete
    experimental_threading: Incomplete
    threading: Incomplete
    def __getattribute__(self, name): ...
    def __setattr__(self, name, value) -> None: ...
    def merge(self, options):
        """Merges itself with the given `tf.data.Options`.

    If this object and the `options` to merge set an option differently, a
    warning is generated and this object's value is updated with the `options`
    object's value.

    Args:
      options: The `tf.data.Options` to merge with.

    Returns:
      New `tf.data.Options` object which is the result of merging self with
      the input `tf.data.Options`.
    """
