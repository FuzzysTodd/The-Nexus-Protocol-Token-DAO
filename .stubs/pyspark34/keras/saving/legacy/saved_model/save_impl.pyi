import threading
from _typeshed import Incomplete
from collections.abc import Generator
from keras import backend as backend
from keras.engine import base_layer_utils as base_layer_utils, input_spec as input_spec
from keras.mixed_precision import autocast_variable as autocast_variable
from keras.saving.legacy import saving_utils as saving_utils
from keras.saving.legacy.saved_model import constants as constants, serialized_attributes as serialized_attributes, utils as utils
from keras.utils import layer_utils as layer_utils, tf_contextlib as tf_contextlib, tf_utils as tf_utils, version_utils as version_utils
from keras.utils.generic_utils import LazyLoader as LazyLoader

base_layer: Incomplete
metrics: Incomplete
input_layer: Incomplete
training_lib: Incomplete
sequential_lib: Incomplete

def should_skip_serialization(layer):
    """Skip serializing extra objects and functions if layer inputs aren't
    set."""
def wrap_layer_objects(layer, serialization_cache):
    """Returns extra trackable objects to attach to the serialized layer.

    Args:
      layer: Keras Layer object.
      serialization_cache: Dictionary shared between all objects during
        serialization.

    Returns:
      A dictionary containing all checkpointable objects from a
      SerializedAttributes object. See LayerAttributes and ModelAttributes for
      entire list of objects
    """
def wrap_layer_functions(layer, serialization_cache):
    """Returns dict of wrapped layer call function and losses in tf.functions.

    Args:
      layer: Keras Layer object.
      serialization_cache: Dictionary shared between all objects during
        serialization.

    Returns:
      A dictionary containing all keras tf.functions to serialize. See
      LayerAttributes and ModelAttributes for the list of all attributes.
    """
def default_save_signature(layer): ...

class LayerTracingContext(threading.local):
    enable_call_tracing: bool
    trace_queue: Incomplete
    def __init__(self) -> None: ...

def tracing_scope() -> Generator[None, None, None]:
    """Enables tracing scope."""
def add_trace_to_queue(fn, args, kwargs, training: Incomplete | None = None) -> None: ...
def tracing_enabled():
    """Whether to add extra traces to the queue."""

class LayerCallCollection:
    """Groups wrapped layer call functions.

    This is used to ensure that all layer call functions are traced with the
    same inputs-
      - call
      - call_and_return_conditional_losses
      - call_and_return_all_conditional_losses
    """
    layer: Incomplete
    layer_call_method: Incomplete
    def __init__(self, layer) -> None: ...
    def add_trace(self, *args, **kwargs) -> None:
        """Traces all functions with the same args and kwargs.

        Args:
          *args: Positional args passed to the original function.
          **kwargs: Keyword args passed to the original function.
        """
    def training_arg_was_passed(self, args, kwargs): ...
    def get_training_arg_value(self, args, kwargs): ...
    def get_input_arg_value(self, args, kwargs): ...
    def add_function(self, call_fn, name, match_layer_training_arg):
        """Adds a layer call function to the collection.

        Args:
          call_fn: a python function
          name: Name of call function
          match_layer_training_arg: If True, removes the `training` from the
            function arguments when calling `call_fn`.

        Returns:
          LayerCall (tf.function)
        """
    def trace_with_input_signature(self) -> None:
        """Trace with the layer/models inferred input signature if possible."""

def layer_call_wrapper(call_collection, method, name):
    """Ensures layer losses are kept the same, and runs method in call
    context."""

class LayerCall:
    """Function that triggers traces of other functions in the same
    collection."""
    call_collection: Incomplete
    wrapped_call: Incomplete
    def __init__(self, call_collection, call_fn, name) -> None:
        """Initializes a LayerCall object.

        Args:
          call_collection: a LayerCallCollection, which contains the other layer
            call functions (e.g. call_with_conditional_losses, call). These
            functions should be traced with the same arguments.
          call_fn: A call function.
          name: Name of the call function.
        """
    def __call__(self, *args, **kwargs): ...
    def get_concrete_function(self, *args, **kwargs): ...
