from _typeshed import Incomplete
from keras.engine import base_layer as base_layer, input_layer as input_layer, input_spec as input_spec
from keras.layers import activation as activation, attention as attention, convolutional as convolutional, core as core, locally_connected as locally_connected, merging as merging, pooling as pooling, regularization as regularization, reshaping as reshaping, rnn as rnn
from keras.layers.normalization import batch_normalization as batch_normalization, batch_normalization_v1 as batch_normalization_v1, group_normalization as group_normalization, layer_normalization as layer_normalization, unit_normalization as unit_normalization
from keras.layers.preprocessing import category_encoding as category_encoding, discretization as discretization, hashed_crossing as hashed_crossing, hashing as hashing, image_preprocessing as image_preprocessing, integer_lookup as integer_lookup, string_lookup as string_lookup, text_vectorization as text_vectorization
from keras.layers.rnn import cell_wrappers as cell_wrappers, gru as gru, lstm as lstm
from keras.saving.legacy.saved_model import json_utils as json_utils
from keras.utils import generic_utils as generic_utils

ALL_MODULES: Incomplete
ALL_V2_MODULES: Incomplete
LOCAL: Incomplete

def populate_deserializable_objects():
    """Populates dict ALL_OBJECTS with every built-in layer."""
def serialize(layer, use_legacy_format: bool = False):
    """Serializes a `Layer` object into a JSON-compatible representation.

    Args:
      layer: The `Layer` object to serialize.

    Returns:
      A JSON-serializable dict representing the object's config.

    Example:

    ```python
    from pprint import pprint
    model = tf.keras.models.Sequential()
    model.add(tf.keras.Input(shape=(16,)))
    model.add(tf.keras.layers.Dense(32, activation='relu'))

    pprint(tf.keras.layers.serialize(model))
    # prints the configuration of the model, as a dict.
    """
def deserialize(config, custom_objects: Incomplete | None = None, use_legacy_format: bool = False):
    """Instantiates a layer from a config dictionary.

    Args:
        config: dict of the form {'class_name': str, 'config': dict}
        custom_objects: dict mapping class names (or function names) of custom
          (non-Keras) objects to class/functions

    Returns:
        Layer instance (may be Model, Sequential, Network, Layer...)

    Example:

    ```python
    # Configuration of Dense(32, activation='relu')
    config = {
      'class_name': 'Dense',
      'config': {
        'activation': 'relu',
        'activity_regularizer': None,
        'bias_constraint': None,
        'bias_initializer': {'class_name': 'Zeros', 'config': {}},
        'bias_regularizer': None,
        'dtype': 'float32',
        'kernel_constraint': None,
        'kernel_initializer': {'class_name': 'GlorotUniform',
                               'config': {'seed': None}},
        'kernel_regularizer': None,
        'name': 'dense',
        'trainable': True,
        'units': 32,
        'use_bias': True
      }
    }
    dense_layer = tf.keras.layers.deserialize(config)
    ```
    """
def get_builtin_layer(class_name):
    """Returns class if `class_name` is registered, else returns None."""
def deserialize_from_json(json_string, custom_objects: Incomplete | None = None):
    """Instantiates a layer from a JSON string."""
