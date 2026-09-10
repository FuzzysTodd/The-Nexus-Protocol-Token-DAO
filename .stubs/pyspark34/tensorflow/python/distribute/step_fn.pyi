from tensorflow.python.eager import backprop as backprop

class Step:
    """Interface for performing each step of a training algorithm."""
    def __init__(self, distribution) -> None: ...
    @property
    def distribution(self): ...
    def initialize(self): ...
    def __call__(self) -> None:
        """Perform one step of this training algorithm."""

class StandardInputStep(Step):
    """Step with a standard implementation of input handling.

  Args:
    dataset_fn: a function that returns a tf.data Dataset that produces the
      input for the model.
  """
    def __init__(self, dataset_fn, distribution) -> None: ...
    def initialize(self): ...

class StandardSingleLossStep(StandardInputStep):
    """A step function that implements a training step for a feed forward network.

  An instance of this class is intended to be used as a callable:

  ```python
  ...
  step = step_fn.StandardSingleLossStep(
      dataset, loss_fn, optimizer, distribution)

  # Run a single training step on a given DistributionStrategy:
  step(distribution)
  ...
  ```

  Args:
    dataset_fn: a function that returns a tf.data Dataset that produces the
      input for the model.
    loss_fn: a function that takes a context and inputs as arguments. It returns
      the loss for those inputs. `context` is an instance of
      `values.MultiStepContext` that will be passed when `loss_fn` is run.
      `context` can be used to specify the outputs to be returned from
      `loss_fn`, among other things.
    optimizer: an optimizer that implements an update rule.
    distribution: a `DistributionStrategy` object.
  """
    def __init__(self, dataset_fn, loss_fn, optimizer, distribution, iterations_per_step: int = 1) -> None: ...
    def __call__(self): ...
