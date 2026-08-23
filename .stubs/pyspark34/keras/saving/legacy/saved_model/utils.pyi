import threading
from _typeshed import Incomplete
from collections.abc import Generator
from keras import backend as backend
from keras.engine import base_layer_utils as base_layer_utils
from keras.utils import control_flow_util as control_flow_util, tf_contextlib as tf_contextlib
from keras.utils.generic_utils import LazyLoader as LazyLoader
from keras.utils.layer_utils import CallFunctionSpec as CallFunctionSpec

training_lib: Incomplete

def use_wrapped_call(layer, call_fn, call_spec, default_training_value: Incomplete | None = None, return_method: bool = False):
    """Creates fn that adds losses returned by call_fn & returns the outputs.

    Args:
      layer: A Keras layer object
      call_fn: tf.function that takes layer inputs (and possibly a training
        arg), and returns a tuple of (outputs, list of losses).
      call_spec: The `CallFunctionSpec` for the layer's call function.
      default_training_value: Default value of the training kwarg. If `None`,
        the default is `tf.keras.backend.learning_phase()`.
      return_method: Whether to return a method bound to the layer.

    Returns:
      function that calls call_fn and returns the outputs. Losses returned by
      call_fn are added to the layer losses.
    """
def layer_uses_training_bool(layer):
    """Returns whether this layer or any of its children uses the training
    arg."""
def list_all_layers(obj): ...
def list_all_layers_and_sublayers(obj): ...
def maybe_add_training_arg(call_spec, wrapped_call, expects_training_arg, default_training_value):
    """Decorate call and optionally adds training argument.

    If a layer expects a training argument, this function ensures that
    'training' is present in the layer args or kwonly args, with the default
    training value.

    Args:
      call_spec: CallFunctionSpec of the layer.
      wrapped_call: Wrapped call function.
      expects_training_arg: Whether to include 'training' argument.
      default_training_value: Default value of the training kwarg to include in
        the arg spec. If `None`, the default is
        `tf.keras.backend.learning_phase()`.

    Returns:
      Tuple of (
        function that calls `wrapped_call` and sets the training arg,
        Argspec of returned function or `None` if the argspec is unchanged)
    """
def set_training_arg_spec(arg_spec, default_training_value):
    """Set `training=DEFAULT` argument in an ArgSpec."""

class SaveOptionsContext(threading.local):
    save_traces: bool
    in_tf_saved_model_scope: bool
    def __init__(self) -> None: ...

def keras_option_scope(save_traces, in_tf_saved_model_scope: bool = True) -> Generator[None, None, None]: ...
def should_save_traces():
    """Whether to trace layer functions-can be disabled in the save_traces
    arg."""
def in_tf_saved_model_scope(): ...
def no_automatic_dependency_tracking_scope(obj) -> Generator[None, None, None]:
    """Context that disables automatic dependency tracking when assigning attrs.

    Objects that inherit from Autotrackable automatically creates dependencies
    to trackable objects through attribute assignments, and wraps data
    structures (lists or dicts) with trackable classes. This scope may be used
    to temporarily disable this behavior. This works similar to the decorator
    `no_automatic_dependency_tracking`.

    Example usage:
    ```
    model = tf.keras.Model()
    model.arr1 = []  # Creates a ListWrapper object
    with no_automatic_dependency_tracking_scope(model):
      model.arr2 = []  # Creates a regular, untracked python list
    ```

    Args:
      obj: A trackable object.

    Yields:
      a scope in which the object doesn't track dependencies.
    """
