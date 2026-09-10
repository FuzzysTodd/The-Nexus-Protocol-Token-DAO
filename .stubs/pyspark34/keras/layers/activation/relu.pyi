from _typeshed import Incomplete
from keras import backend as backend
from keras.engine.base_layer import Layer as Layer
from keras.utils import tf_utils as tf_utils

class ReLU(Layer):
    """Rectified Linear Unit activation function.

    With default values, it returns element-wise `max(x, 0)`.

    Otherwise, it follows:

    ```
      f(x) = max_value if x >= max_value
      f(x) = x if threshold <= x < max_value
      f(x) = negative_slope * (x - threshold) otherwise
    ```

    Usage:

    >>> layer = tf.keras.layers.ReLU()
    >>> output = layer([-3.0, -1.0, 0.0, 2.0])
    >>> list(output.numpy())
    [0.0, 0.0, 0.0, 2.0]
    >>> layer = tf.keras.layers.ReLU(max_value=1.0)
    >>> output = layer([-3.0, -1.0, 0.0, 2.0])
    >>> list(output.numpy())
    [0.0, 0.0, 0.0, 1.0]
    >>> layer = tf.keras.layers.ReLU(negative_slope=1.0)
    >>> output = layer([-3.0, -1.0, 0.0, 2.0])
    >>> list(output.numpy())
    [-3.0, -1.0, 0.0, 2.0]
    >>> layer = tf.keras.layers.ReLU(threshold=1.5)
    >>> output = layer([-3.0, -1.0, 1.0, 2.0])
    >>> list(output.numpy())
    [0.0, 0.0, 0.0, 2.0]

    Input shape:
      Arbitrary. Use the keyword argument `input_shape`
      (tuple of integers, does not include the batch axis)
      when using this layer as the first layer in a model.

    Output shape:
      Same shape as the input.

    Args:
      max_value: Float >= 0. Maximum activation value. Default to None, which
        means unlimited.
      negative_slope: Float >= 0. Negative slope coefficient. Default to 0.
      threshold: Float >= 0. Threshold value for thresholded activation. Default
        to 0.
    """
    supports_masking: bool
    max_value: Incomplete
    negative_slope: Incomplete
    threshold: Incomplete
    def __init__(self, max_value: Incomplete | None = None, negative_slope: float = 0.0, threshold: float = 0.0, **kwargs) -> None: ...
    def call(self, inputs): ...
    def get_config(self): ...
    def compute_output_shape(self, input_shape): ...
