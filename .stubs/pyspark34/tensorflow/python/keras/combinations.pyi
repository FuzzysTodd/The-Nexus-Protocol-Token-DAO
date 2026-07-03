from _typeshed import Incomplete
from tensorflow.python import tf2 as tf2
from tensorflow.python.framework import combinations as combinations, test_combinations as test_combinations
from tensorflow.python.keras import testing_utils as testing_utils

KERAS_MODEL_TYPES: Incomplete

def keras_mode_combinations(mode: Incomplete | None = None, run_eagerly: Incomplete | None = None):
    """Returns the default test combinations for tf.keras tests.

  Note that if tf2 is enabled, then v1 session test will be skipped.

  Args:
    mode: List of modes to run the tests. The valid options are 'graph' and
      'eager'. Default to ['graph', 'eager'] if not specified. If a empty list
      is provide, then the test will run under the context based on tf's
      version, eg graph for v1 and eager for v2.
    run_eagerly: List of `run_eagerly` value to be run with the tests.
      Default to [True, False] if not specified. Note that for `graph` mode,
      run_eagerly value will only be False.

  Returns:
    A list contains all the combinations to be used to generate test cases.
  """
def keras_model_type_combinations(): ...

class KerasModeCombination(test_combinations.TestCombination):
    """Combination for Keras test mode.

  It by default includes v1_session, v2_eager and v2_tf_function.
  """
    def context_managers(self, kwargs): ...
    def parameter_modifiers(self): ...

class KerasModelTypeCombination(test_combinations.TestCombination):
    """Combination for Keras model types when doing model test.

  It by default includes 'functional', 'subclass', 'sequential'.

  Various methods in `testing_utils` to get models will auto-generate a model
  of the currently active Keras model type. This allows unittests to confirm
  the equivalence between different Keras models.
  """
    def context_managers(self, kwargs): ...
    def parameter_modifiers(self): ...

generate: Incomplete
combine = test_combinations.combine
times = test_combinations.times
NamedObject = test_combinations.NamedObject
