import abc
from _typeshed import Incomplete
from tensorflow_estimator.python.estimator import estimator_lib as estimator_lib
from tensorflow_estimator.python.estimator.canned.timeseries import feature_keys as feature_keys

class PassthroughStateManager:
    """A minimal wrapper for models which do not need state management."""
    def __init__(self) -> None: ...
    def initialize_graph(self, model, input_statistics: Incomplete | None = None) -> None:
        """Adds required operations to the graph."""
    def define_loss(self, model, features, mode):
        '''Wrap "model" with StateManager-specific operations.

    Args:
      model: The model (inheriting from TimeSeriesModel) to manage state for.
      features: A dictionary with the following key/value pairs:
        feature_keys.TrainEvalFeatures.TIMES: A [batch size x window size]
          Tensor with times for each observation.
        feature_keys.TrainEvalFeatures.VALUES: A [batch size x window size x num
          features] Tensor with values for each observation.
      mode: The tf.estimator.ModeKeys mode to use (TRAIN or EVAL).

    Returns:
      A ModelOutputs object.
    Raises:
      ValueError: If start state was specified.
    '''

class _OverridableStateManager(PassthroughStateManager, metaclass=abc.ABCMeta):
    """Base class for state managers which support overriding model state."""
    def define_loss(self, model, features, mode):
        """Switches between explicit start state and managed state."""

class FilteringOnlyStateManager(_OverridableStateManager):
    """State manager for models which use state only for filtering.

  Window-based models (ARModel) do not require state to be fed during training
  (instead requiring a specific window size). Rather than requiring a minimum
  window size for filtering, these models maintain this window in their state,
  and so need state to be fed.
  """
