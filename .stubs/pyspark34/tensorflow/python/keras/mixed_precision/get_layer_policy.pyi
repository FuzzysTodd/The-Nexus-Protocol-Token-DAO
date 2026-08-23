from tensorflow.python.keras.engine import base_layer as base_layer
from tensorflow.python.util.tf_export import keras_export as keras_export

def get_layer_policy(layer):
    """Returns the dtype policy of a layer.

  Warning: This function is deprecated. Use
  `tf.keras.layers.Layer.dtype_policy` instead.

  Args:
    layer: A `tf.keras.layers.Layer`.

  Returns:
    The `tf.keras.mixed_precision.Policy` of the layer.
  """
