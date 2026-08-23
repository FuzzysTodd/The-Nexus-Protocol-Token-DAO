from _typeshed import Incomplete
from tensorflow.python import tf2 as tf2
from tensorflow.python.keras.engine import base_layer as base_layer, input_layer as input_layer, input_spec as input_spec
from tensorflow.python.keras.layers import advanced_activations as advanced_activations, convolutional as convolutional, convolutional_recurrent as convolutional_recurrent, core as core, cudnn_recurrent as cudnn_recurrent, dense_attention as dense_attention, embeddings as embeddings, merge as merge, pooling as pooling, recurrent as recurrent, recurrent_v2 as recurrent_v2, rnn_cell_wrapper_v2 as rnn_cell_wrapper_v2
from tensorflow.python.keras.utils import generic_utils as generic_utils
from tensorflow.python.util.tf_export import keras_export as keras_export

ALL_MODULES: Incomplete
ALL_V2_MODULES: Incomplete
LOCAL: Incomplete

def populate_deserializable_objects():
    """Populates dict ALL_OBJECTS with every built-in layer.
  """
def serialize(layer): ...
def deserialize(config, custom_objects: Incomplete | None = None):
    """Instantiates a layer from a config dictionary.

  Args:
      config: dict of the form {'class_name': str, 'config': dict}
      custom_objects: dict mapping class names (or function names)
          of custom (non-Keras) objects to class/functions

  Returns:
      Layer instance (may be Model, Sequential, Network, Layer...)
  """
