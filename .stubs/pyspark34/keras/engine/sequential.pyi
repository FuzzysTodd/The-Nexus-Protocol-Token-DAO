from _typeshed import Incomplete
from keras.engine import base_layer as base_layer, functional as functional, input_layer as input_layer, training as training, training_utils as training_utils
from keras.saving.legacy import serialization as serialization
from keras.saving.legacy.saved_model import model_serialization as model_serialization
from keras.utils import generic_utils as generic_utils, layer_utils as layer_utils, tf_inspect as tf_inspect, tf_utils as tf_utils, traceback_utils as traceback_utils

SINGLE_LAYER_OUTPUT_ERROR_MSG: str

class Sequential(functional.Functional):
    '''`Sequential` groups a linear stack of layers into a `tf.keras.Model`.

    `Sequential` provides training and inference features on this model.

    Examples:

    ```python
    # Optionally, the first layer can receive an `input_shape` argument:
    model = tf.keras.Sequential()
    model.add(tf.keras.layers.Dense(8, input_shape=(16,)))
    # Afterwards, we do automatic shape inference:
    model.add(tf.keras.layers.Dense(4))

    # This is identical to the following:
    model = tf.keras.Sequential()
    model.add(tf.keras.Input(shape=(16,)))
    model.add(tf.keras.layers.Dense(8))

    # Note that you can also omit the `input_shape` argument.
    # In that case the model doesn\'t have any weights until the first call
    # to a training/evaluation method (since it isn\'t yet built):
    model = tf.keras.Sequential()
    model.add(tf.keras.layers.Dense(8))
    model.add(tf.keras.layers.Dense(4))
    # model.weights not created yet

    # Whereas if you specify the input shape, the model gets built
    # continuously as you are adding layers:
    model = tf.keras.Sequential()
    model.add(tf.keras.layers.Dense(8, input_shape=(16,)))
    model.add(tf.keras.layers.Dense(4))
    len(model.weights)
    # Returns "4"

    # When using the delayed-build pattern (no input shape specified), you can
    # choose to manually build your model by calling
    # `build(batch_input_shape)`:
    model = tf.keras.Sequential()
    model.add(tf.keras.layers.Dense(8))
    model.add(tf.keras.layers.Dense(4))
    model.build((None, 16))
    len(model.weights)
    # Returns "4"

    # Note that when using the delayed-build pattern (no input shape specified),
    # the model gets built the first time you call `fit`, `eval`, or `predict`,
    # or the first time you call the model on some input data.
    model = tf.keras.Sequential()
    model.add(tf.keras.layers.Dense(8))
    model.add(tf.keras.layers.Dense(1))
    model.compile(optimizer=\'sgd\', loss=\'mse\')
    # This builds the model for the first time:
    model.fit(x, y, batch_size=32, epochs=10)
    ```
    '''
    supports_masking: bool
    def __init__(self, layers: Incomplete | None = None, name: Incomplete | None = None) -> None:
        """Creates a `Sequential` model instance.

        Args:
          layers: Optional list of layers to add to the model.
          name: Optional name for the model.
        """
    @property
    def layers(self): ...
    built: bool
    outputs: Incomplete
    inputs: Incomplete
    def add(self, layer) -> None:
        """Adds a layer instance on top of the layer stack.

        Args:
            layer: layer instance.

        Raises:
            TypeError: If `layer` is not a layer instance.
            ValueError: In case the `layer` argument does not
                know its input shape.
            ValueError: In case the `layer` argument has
                multiple output tensors, or is already connected
                somewhere else (forbidden in `Sequential` models).
        """
    def pop(self) -> None:
        """Removes the last layer in the model.

        Raises:
            TypeError: if there are no layers in the model.
        """
    def build(self, input_shape: Incomplete | None = None) -> None: ...
    def call(self, inputs, training: Incomplete | None = None, mask: Incomplete | None = None): ...
    def compute_output_shape(self, input_shape): ...
    def compute_mask(self, inputs, mask): ...
    def get_config(self): ...
    @classmethod
    def from_config(cls, config, custom_objects: Incomplete | None = None): ...
    @property
    def input_spec(self): ...
    @input_spec.setter
    def input_spec(self, value) -> None: ...

def relax_input_shape(shape_1, shape_2): ...
def clear_previously_created_nodes(layer, created_nodes) -> None:
    """Remove nodes from `created_nodes` from the layer's inbound_nodes."""
def track_nodes_created_by_last_call(layer, created_nodes) -> None:
    """Adds to `created_nodes` the nodes created by the last call to `layer`."""
