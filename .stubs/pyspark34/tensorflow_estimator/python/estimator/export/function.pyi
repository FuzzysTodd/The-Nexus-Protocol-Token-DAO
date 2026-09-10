import tensorflow as tf
from _typeshed import Incomplete
from tensorflow.python.eager import function, wrap_function
from tensorflow_estimator.python.estimator.mode_keys import ModeKeys as ModeKeys

class ModelFunction(tf.compat.v2.__internal__.tracking.AutoTrackable):
    """A checkpointable ModelFunction object.

  This object stores a global mapping of variables and functions for each mode.
  """
    def __init__(self, config: Incomplete | None = None, params: Incomplete | None = None) -> None: ...
    @staticmethod
    def from_function(model_fn, all_modes: Incomplete | None = None, config: Incomplete | None = None, params: Incomplete | None = None):
        """Creates a new ModelFunction object from a model function."""
    @property
    def variables(self): ...
    def add_mode(self, fn, mode, input_signature: Incomplete | None = None) -> None: ...
    def train(self, features, labels): ...
    def evaluate(self, features, labels): ...
    def predict(self, features): ...
    def call(self, mode, features, labels: Incomplete | None = None): ...

class EstimatorSpecFunction(tf.compat.v2.__internal__.function.Function):
    """Wraps graph functions defined for a function returning an EstimatorSpec.

  Instances of this class are revivable when attached to a checkpointable
  object.
  """
    def __init__(self, fn, mode, config: Incomplete | None = None, params: Incomplete | None = None, variable_holder: Incomplete | None = None, **kwargs) -> None:
        """Initializes an EstimatorSpecFunction.

    Args:
      fn: Python model function.
      mode: String mode to run the function.
      config: RunConfig that is passed to the `config` arg in the function.
      params: object that is passed to the `params` argument in the function.
      variable_holder: Optional `wrap_function.VariableHolder` object.
      **kwargs: Optional keyword arguments to pass to tf.function (e.g.
        input_signature).
    """

class _EstimatorSpecFunction(function.Function):
    """Wraps graph functions defined for a function returning an EstimatorSpec.

  This object handles creation of the graph functions.
  """
    def __init__(self, python_function, name, variable_holder: Incomplete | None = None, **kwargs) -> None: ...

class _EstimatorWrappedGraph(wrap_function.WrappedGraph):
    """WrappedGraph that handles global step creation and wraps estimator fns."""
    def __init__(self, *args, **kwargs) -> None: ...
    @property
    def global_step(self): ...
    @property
    def model_fn(self): ...
    @property
    def estimator_spec(self): ...
    def wrap_model_fn(self, model_fn, mode, args: Incomplete | None = None, kwargs: Incomplete | None = None, signature: Incomplete | None = None):
        """Wraps a model function, and stores the returned estimator spec."""
    def wrap_input_receiver_fn(self, input_receiver_fn):
        """Converts an input receiver function to one or more concrete functions.

    Input receiver functions are python functions with no arguments.
    Placeholders are created within the function and used to receive inputs to
    the model.

    The function (or multiple functions) generated depends on the InputReceiver
    object returned by `input_receiver_fn`.

    Generally, the returned function will have inputs and outputs:
      input_receiver(**receiver_tensors) --> features

    or (if the InputReceiver returns labels):
      input_receiver(**receiver_tensors) --> features, labels

    __Alternate Receiver Tensors__

    The InputReceiver may have alternate receiver tensors, in which case
    additional concrete functions are generated. Example:
      InputReceiver.receiver_tensors_alternatives = {
        'alt_input_1': Tensor,
        'alt_input_2': {
          'tensor_1': Tensor,
          'tensor_2': Tensor
        }
      }

    This will generate concrete functions:
      input_receiver_alt_input_1(input) --> features
      input_receiver_alt_input_2(tensor_1, tensor_2) --> features

    Args:
      input_receiver_fn: a no-argument function that returns an `InputReceiver`
        object.

    Returns:
      A list of tuples of (concrete function, receiver name). The name of the
      default input receiver is `None`.
    """
