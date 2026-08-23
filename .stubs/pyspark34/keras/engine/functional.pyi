from _typeshed import Incomplete
from keras import backend as backend
from keras.engine import base_layer as base_layer, base_layer_utils as base_layer_utils, functional_utils as functional_utils, input_spec as input_spec, training as training_lib, training_utils as training_utils
from keras.saving.legacy import serialization as serialization
from keras.saving.legacy.saved_model import json_utils as json_utils, network_serialization as network_serialization
from keras.utils import generic_utils as generic_utils, tf_inspect as tf_inspect, tf_utils as tf_utils

class Functional(training_lib.Model):
    """A `Functional` model is a `Model` defined as a directed graph of layers.

    Three types of `Model` exist: subclassed `Model`, `Functional` model,
    and `Sequential` (a special case of `Functional`).
    In general, more Keras features are supported with `Functional`
    than with subclassed `Model`s, specifically:

    - Model cloning (`keras.models.clone`)
    - Serialization (`model.get_config()/from_config`, `model.to_json()`
    - Whole-model saving (`model.save()`)

    A `Functional` model can be instantiated by passing two arguments to
    `__init__`. The first argument is the `keras.Input` Tensors that represent
    the inputs to the model. The second argument specifies the output
    tensors that represent the outputs of this model. Both arguments can be a
    nested structure of tensors.

    Example:

    ```
    inputs = {'x1': keras.Input(shape=(10,)), 'x2': keras.Input(shape=(1,))}
    t = keras.layers.Dense(1, activation='relu')(inputs['x1'])
    outputs = keras.layers.Add()([t, inputs['x2'])
    model = keras.Model(inputs, outputs)
    ```

    A `Functional` model constructed using the Functional API can also include
    raw TensorFlow functions, with the exception of functions that create
    Variables or assign ops.

    Example:

    ```python
    inputs = keras.Input(shape=(10,))
    x = keras.layers.Dense(1)(inputs)
    outputs = tf.nn.relu(x)
    model = keras.Model(inputs, outputs)
    ```

    A new `Functional` model can also be created by using the
    intermediate tensors. This enables you to quickly extract sub-components
    of the model.

    Example:

    ```python
    inputs = keras.Input(shape=(None, None, 3))
    processed = keras.layers.RandomCrop(width=32, height=32)(inputs)
    conv = keras.layers.Conv2D(filters=2, kernel_size=3)(processed)
    pooling = keras.layers.GlobalAveragePooling2D()(conv)
    feature = keras.layers.Dense(10)(pooling)

    full_model = keras.Model(inputs, feature)
    backbone = keras.Model(processed, conv)
    activations = keras.Model(conv, feature)
    ```

    Note that the `backbone` and `activations` models are not
    created with `keras.Input` objects, but with the tensors that are originated
    from `keras.Input` objects. Under the hood, the layers and weights will
    be shared across these models, so that user can train the `full_model`, and
    use `backbone` or `activations` to do feature extraction.
    The inputs and outputs of the model can be nested structures of tensors as
    well, and the created models are standard `Functional` model that support
    all the existing API.

    Args:
      inputs: List of input tensors (must be created via `tf.keras.Input()` or
        originated from `tf.keras.Input()`).
      outputs: List of output tensors.
      name: String, optional. Name of the model.
      trainable: Boolean, optional. If the model's variables should be
        trainable.
    """
    def __init__(self, inputs, outputs, name: Incomplete | None = None, trainable: bool = True, **kwargs) -> None: ...
    @property
    def input(self):
        """Retrieves the input tensor(s) of a layer.

        Only applicable if the layer has exactly one input,
        i.e. if it is connected to one incoming layer.

        Returns:
            Input tensor or list of input tensors.

        Raises:
          RuntimeError: If called in Eager mode.
          AttributeError: If no inbound nodes are found.
        """
    @property
    def input_shape(self):
        """Retrieves the input shape(s) of a layer.

        Only applicable if the layer has exactly one input,
        i.e. if it is connected to one incoming layer, or if all inputs
        have the same shape.

        Returns:
            Input shape, as an integer shape tuple
            (or list of shape tuples, one tuple per input tensor).

        Raises:
            AttributeError: if the layer has no defined input_shape.
            RuntimeError: if called in Eager mode.
        """
    @property
    def input_spec(self): ...
    @input_spec.setter
    def input_spec(self, value) -> None: ...
    @property
    def output(self):
        """Retrieves the output tensor(s) of a layer.

        Only applicable if the layer has exactly one output,
        i.e. if it is connected to one incoming layer.

        Returns:
          Output tensor or list of output tensors.

        Raises:
          AttributeError: if the layer is connected to more than one incoming
            layers.
          RuntimeError: if called in Eager mode.
        """
    @property
    def output_shape(self):
        """Retrieves the output shape(s) of a layer.

        Only applicable if the layer has one output,
        or if all outputs have the same shape.

        Returns:
            Output shape, as an integer shape tuple
            (or list of shape tuples, one tuple per output tensor).

        Raises:
            AttributeError: if the layer has no defined output shape.
            RuntimeError: if called in Eager mode.
        """
    def compute_mask(self, inputs, mask): ...
    def call(self, inputs, training: Incomplete | None = None, mask: Incomplete | None = None):
        """Calls the model on new inputs.

        In this case `call` just reapplies
        all ops in the graph to the new inputs
        (e.g. build a new computational graph from the provided inputs).

        Args:
            inputs: A tensor or list of tensors.
            training: Boolean or boolean scalar tensor, indicating whether to
                run the `Network` in training mode or inference mode.
            mask: A mask or list of masks. A mask can be
                either a tensor or None (no mask).

        Returns:
            A tensor if there is a single output, or
            a list of tensors if there are more than one outputs.
        """
    def compute_output_shape(self, input_shape): ...
    def get_config(self): ...
    def get_weight_paths(self): ...

def connect_ancillary_layers(model, created_layers):
    """Adds layers that are not connected to the outputs to the model."""
def reconstruct_from_config(config, custom_objects: Incomplete | None = None, created_layers: Incomplete | None = None):
    """Reconstructs graph from config object.

    Args:
      config: Dictionary returned from Network.get_config()
      custom_objects: Optional dictionary mapping names (strings) to custom
        classes or functions to be considered during deserialization.
      created_layers: Optional dictionary mapping names to Layer objects. Any
        layer not in this dictionary will be created and added to the dict.
        This function will add new nodes to all layers (excluding InputLayers),
        instead of re-using pre-existing nodes in the layers.

    Returns:
      Tuple of (input tensors, output tensors, dictionary of created layers)
    """
def get_network_config(network, serialize_layer_fn: Incomplete | None = None, config: Incomplete | None = None):
    """Build the config, which consists of the node graph and serialized layers.

    Args:
      network: A Network object.
      serialize_layer_fn: Function used to serialize layers.
      config: A dict to append more config entries into. If None, start with a
          new dict for the config.

    Returns:
      Config dictionary.
    """
def shape_with_no_batch_size(x): ...

class ModuleWrapper(base_layer.Layer):
    """Wrapper for `tf.Module`s to support the Functional and Sequential API."""
    def __init__(self, module, method_name: Incomplete | None = None, **kwargs) -> None:
        """Initializes the wrapper Layer for this module.

        Args:
          module: The `tf.Module` instance to be wrapped.
          method_name: (Optional) str. The name of the method to use as the
            forward pass of the module. If not set, defaults to '__call__' if
            defined, or 'call'.
          **kwargs: Additional keywrod arguments. See `tf.keras.layers.Layer`.

        Raises:
          ValueError: If `method` is not defined on `module`.
        """
    def call(self, *args, **kwargs): ...

def has_functional_like_constructor(cls): ...
