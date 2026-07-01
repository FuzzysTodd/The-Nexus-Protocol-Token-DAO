from _typeshed import Incomplete
from tensorflow.python.util import tf_inspect as tf_inspect
from tensorflow.python.util.tf_export import tf_export as tf_export

class TestCombination:
    """Customize the behavior of `generate()` and the tests that it executes.

  Here is sequence of steps for executing a test combination:
    1. The test combination is evaluated for whether it should be executed in
       the given environment by calling `should_execute_combination`.
    2. If the test combination is going to be executed, then the arguments for
       all combined parameters are validated.  Some arguments can be handled in
       a special way.  This is achieved by implementing that logic in
       `ParameterModifier` instances that returned from `parameter_modifiers`.
    3. Before executing the test, `context_managers` are installed
       around it.
  """
    def should_execute_combination(self, kwargs):
        """Indicates whether the combination of test arguments should be executed.

    If the environment doesn't satisfy the dependencies of the test
    combination, then it can be skipped.

    Args:
      kwargs:  Arguments that are passed to the test combination.

    Returns:
      A tuple boolean and an optional string.  The boolean False indicates
    that the test should be skipped.  The string would indicate a textual
    description of the reason.  If the test is going to be executed, then
    this method returns `None` instead of the string.
    """
    def parameter_modifiers(self):
        """Returns `ParameterModifier` instances that customize the arguments."""
    def context_managers(self, kwargs):
        """Return context managers for running the test combination.

    The test combination will run under all context managers that all
    `TestCombination` instances return.

    Args:
      kwargs:  Arguments and their values that are passed to the test
        combination.

    Returns:
      A list of instantiated context managers.
    """

class ParameterModifier:
    """Customizes the behavior of a particular parameter.

  Users should override `modified_arguments()` to modify the parameter they
  want, eg: change the value of certain parameter or filter it from the params
  passed to the test case.

  See the sample usage below, it will change any negative parameters to zero
  before it gets passed to test case.
  ```
  class NonNegativeParameterModifier(ParameterModifier):

    def modified_arguments(self, kwargs, requested_parameters):
      updates = {}
      for name, value in kwargs.items():
        if value < 0:
          updates[name] = 0
      return updates
  ```
  """
    DO_NOT_PASS_TO_THE_TEST: Incomplete
    def __init__(self, parameter_name: Incomplete | None = None) -> None:
        """Construct a parameter modifier that may be specific to a parameter.

    Args:
      parameter_name:  A `ParameterModifier` instance may operate on a class of
        parameters or on a parameter with a particular name.  Only
        `ParameterModifier` instances that are of a unique type or were
        initialized with a unique `parameter_name` will be executed.
        See `__eq__` and `__hash__`.
    """
    def modified_arguments(self, kwargs, requested_parameters):
        """Replace user-provided arguments before they are passed to a test.

    This makes it possible to adjust user-provided arguments before passing
    them to the test method.

    Args:
      kwargs:  The combined arguments for the test.
      requested_parameters: The set of parameters that are defined in the
        signature of the test method.

    Returns:
      A dictionary with updates to `kwargs`.  Keys with values set to
      `ParameterModifier.DO_NOT_PASS_TO_THE_TEST` are going to be deleted and
      not passed to the test.
    """
    def __eq__(self, other):
        """Compare `ParameterModifier` by type and `parameter_name`."""
    def __ne__(self, other): ...
    def __hash__(self):
        """Compare `ParameterModifier` by type or `parameter_name`."""

class OptionalParameter(ParameterModifier):
    '''A parameter that is optional in `combine()` and in the test signature.

  `OptionalParameter` is usually used with `TestCombination` in the
  `parameter_modifiers()`. It allows `TestCombination` to skip certain
  parameters when passing them to `combine()`, since the `TestCombination` might
  consume the param and create some context based on the value it gets.

  See the sample usage below:

  ```
  class EagerGraphCombination(TestCombination):

    def context_managers(self, kwargs):
      mode = kwargs.pop("mode", None)
      if mode is None:
        return []
      elif mode == "eager":
        return [context.eager_mode()]
      elif mode == "graph":
        return [ops.Graph().as_default(), context.graph_mode()]
      else:
        raise ValueError(
            "\'mode\' has to be either \'eager\' or \'graph\', got {}".format(mode))

    def parameter_modifiers(self):
      return [test_combinations.OptionalParameter("mode")]
  ```

  When the test case is generated, the param "mode" will not be passed to the
  test method, since it is consumed by the `EagerGraphCombination`.
  '''
    def modified_arguments(self, kwargs, requested_parameters): ...

def generate(combinations, test_combinations=()):
    """A decorator for generating combinations of a test method or a test class.

  Parameters of the test method must match by name to get the corresponding
  value of the combination.  Tests must accept all parameters that are passed
  other than the ones that are `OptionalParameter`.

  Args:
    combinations: a list of dictionaries created using combine() and times().
    test_combinations: a tuple of `TestCombination` instances that customize
      the execution of generated tests.

  Returns:
    a decorator that will cause the test method or the test class to be run
    under the specified conditions.

  Raises:
    ValueError: if any parameters were not accepted by the test method
  """
def combine(**kwargs):
    """Generate combinations based on its keyword arguments.

  Two sets of returned combinations can be concatenated using +.  Their product
  can be computed using `times()`.

  Args:
    **kwargs: keyword arguments of form `option=[possibilities, ...]`
         or `option=the_only_possibility`.

  Returns:
    a list of dictionaries for each combination. Keys in the dictionaries are
    the keyword argument names.  Each key has one value - one of the
    corresponding keyword argument values.
  """
def times(*combined):
    """Generate a product of N sets of combinations.

  times(combine(a=[1,2]), combine(b=[3,4])) == combine(a=[1,2], b=[3,4])

  Args:
    *combined: N lists of dictionaries that specify combinations.

  Returns:
    a list of dictionaries for each combination.

  Raises:
    ValueError: if some of the inputs have overlapping keys.
  """

class NamedObject:
    """A class that translates an object into a good test name."""
    def __init__(self, name, obj) -> None: ...
    def __getattr__(self, name): ...
    def __call__(self, *args, **kwargs): ...
    def __iter__(self): ...
