from _typeshed import Incomplete
from tensorflow.python.client import session as session
from tensorflow.python.distribute import collective_all_reduce_strategy as collective_all_reduce_strategy, distribute_lib as distribute_lib, multi_process_runner as multi_process_runner, multi_worker_test_base as multi_worker_test_base
from tensorflow.python.eager import context as context, def_function as def_function
from tensorflow.python.framework import config as config, ops as ops, test_combinations as combinations_lib, test_util as test_util
from tensorflow.python.platform import flags as flags
from tensorflow.python.util import tf_decorator as tf_decorator, tf_inspect as tf_inspect
from tensorflow.python.util.tf_export import tf_export as tf_export
from typing import NamedTuple

class DistributionParameter(combinations_lib.ParameterModifier):
    """Transforms arguments of type `NamedDistribution`.

  Convert all arguments of type `NamedDistribution` to the value of their
  `strategy` property.
  """
    def modified_arguments(self, kwargs, requested_parameters): ...

class ClusterParameters(combinations_lib.ParameterModifier):
    """Adds cluster parameters if a `NamedDistribution` has it.

  It needs to be before DistributionParameter.
  """
    def modified_arguments(self, kwargs, requested_parameters): ...

class DistributionCombination(combinations_lib.TestCombination):
    """Sets up distribution strategy for tests."""
    def should_execute_combination(self, kwargs): ...
    def parameter_modifiers(self): ...

class ClusterCombination(combinations_lib.TestCombination):
    """Sets up multi worker tests."""
    def parameter_modifiers(self): ...

class GPUCombination(combinations_lib.TestCombination):
    '''Enable tests to request GPU hardware and skip non-GPU combinations.

  This class expects test_combinations to be generated with `NamedDistribution`
  wrapping instances of `tf.distribute.Strategy`.

  Optionally, the `required_gpus` argument is supported.  GPU hardware is
  required, if its value is `True` or > 0.

  Attributes:
    GPU_TEST: The environment is considered to have GPU hardware available if
              the name of the program contains "test_gpu" or "test_xla_gpu".
  '''
    GPU_TEST: bool
    def should_execute_combination(self, kwargs): ...
    def parameter_modifiers(self): ...

class TPUCombination(combinations_lib.TestCombination):
    '''Allow to request TPU hardware and skip non-TPU combinations.

  This class expects test_combinations to be generated with `NamedDistribution`
  wrapping instances of `tf.distribute.Strategy`.

  Optionally, the `required_tpus` parameter is supported.  TPU hardware is
  required, if its argument is `True` or > 0.

  Optionally, the `use_cloud_tpu` parameter is supported. If TPU hardware is
  required by `required_tpus`, it specifically must be a Cloud TPU (specified
  with `--tpu`) if `use_cloud_tpu` is `True`.

  Attributes:
    TPU_TEST: The environment is considered to have TPU hardware available if
              the name of the program contains "test_tpu".
  '''
    TPU_TEST: bool
    def should_execute_combination(self, kwargs): ...
    def parameter_modifiers(self): ...

class NamedDistribution:
    """Wraps a `tf.distribute.Strategy` and adds a name for test titles."""
    required_gpus: Incomplete
    required_physical_gpus: Incomplete
    required_tpu: Incomplete
    use_cloud_tpu: Incomplete
    has_chief: Incomplete
    num_workers: Incomplete
    num_ps: Incomplete
    share_gpu: Incomplete
    no_xla: Incomplete
    def __init__(self, name, distribution_fn, required_gpus: Incomplete | None = None, required_physical_gpus: int = 0, required_tpu: bool = False, use_cloud_tpu: bool = False, has_chief: bool = False, num_workers: int = 1, num_ps: int = 0, share_gpu: bool = True, pool_runner_fn: Incomplete | None = None, no_xla: bool = False) -> None:
        """Initialize NamedDistribution.

    Args:
      name: Name that will be a part of the name of the test case.
      distribution_fn: A callable that creates a `tf.distribute.Strategy`.
      required_gpus: The number of GPUs that the strategy requires. Only one of
      `required_gpus` and `required_physical_gpus` should be set.
      required_physical_gpus: Number of physical GPUs required. Only one of
      `required_gpus` and `required_physical_gpus` should be set.
      required_tpu: Whether the strategy requires TPU.
      use_cloud_tpu: Whether the strategy requires cloud TPU.
      has_chief: Whether the strategy requires a chief worker.
      num_workers: The number of workers that the strategy requires.
      num_ps: The number of parameter servers.
      share_gpu: Whether to share GPUs among workers.
      pool_runner_fn: An optional callable that returns a MultiProcessPoolRunner
        to run the test.
      no_xla: Whether to skip in XLA tests.
    """
    @property
    def runner(self): ...
    @property
    def strategy(self): ...

tf_function: Incomplete
no_tf_function: Incomplete

def concat(*combined):
    """Concats combinations."""
def generate(combinations, test_combinations=()):
    """Distributed adapter of `tf.__internal__.test.combinations.generate`.

  All tests with distributed strategy should use this one instead of
  `tf.__internal__.test.combinations.generate`. This function has support of
  strategy combinations, GPU/TPU and multi worker support.

  See `tf.__internal__.test.combinations.generate` for usage.
  """
combine = combinations_lib.combine
times = combinations_lib.times
NamedObject = combinations_lib.NamedObject

def in_main_process():
    """Whether it's in the main test process.

  This is normally used to prepare the test environment which should only happen
  in the main process.

  Returns:
    A boolean.
  """

class TestEnvironment:
    """Holds the test environment information.

  Tests should modify the attributes of the instance returned by `env()` in the
  main process if needed, and it will be passed to the worker processes each
  time a test case is run.
  """
    tf_data_service_dispatcher: Incomplete
    total_phsyical_gpus: Incomplete
    def __init__(self) -> None: ...
    def __setattr__(self, name, value) -> None: ...

def env():
    """Returns the object holds the test environment information.

  Tests should modify this in the main process if needed, and it will be passed
  to the worker processes each time a test case is run.

  Returns:
    a TestEnvironment object.
  """

class _TestResult(NamedTuple):
    status: Incomplete
    message: Incomplete
