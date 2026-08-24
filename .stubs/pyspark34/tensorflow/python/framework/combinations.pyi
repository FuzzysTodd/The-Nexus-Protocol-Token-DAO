from _typeshed import Incomplete
from tensorflow.python import tf2 as tf2
from tensorflow.python.eager import context as context
from tensorflow.python.framework import ops as ops, test_combinations as test_combinations
from tensorflow.python.util.tf_export import tf_export as tf_export

class EagerGraphCombination(test_combinations.TestCombination):
    '''Run the test in Graph or Eager mode.

  The optional `mode` parameter controls the test\'s execution mode.  Its
  accepted values are "graph" or "eager" literals.
  '''
    def context_managers(self, kwargs): ...
    def parameter_modifiers(self): ...

class TFVersionCombination(test_combinations.TestCombination):
    """Control the execution of the test in TF1.x and TF2.

  If TF2 is enabled then a test with TF1 test is going to be skipped and vice
  versa.

  Test targets continuously run in TF2 thanks to the tensorflow.v2 TAP target.
  A test can be run in TF2 with bazel by passing --test_env=TF2_BEHAVIOR=1.
  """
    def should_execute_combination(self, kwargs): ...
    def parameter_modifiers(self): ...

generate: Incomplete
combine = test_combinations.combine
times = test_combinations.times
NamedObject = test_combinations.NamedObject
