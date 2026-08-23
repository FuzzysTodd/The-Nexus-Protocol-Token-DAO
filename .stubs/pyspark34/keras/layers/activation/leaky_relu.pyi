from _typeshed import Incomplete
from keras import backend as backend
from keras.engine.base_layer import Layer as Layer
from keras.utils import tf_utils as tf_utils

class LeakyReLU(Layer):
    """Leaky version of a Rectified Linear Unit.

    It allows a small gradient when the unit is not active:

    ```
      f(x) = alpha * x if x < 0
      f(x) = x if x >= 0
    ```

    Usage:

    >>> layer = tf.keras.layers.LeakyReLU()
    >>> output = layer([-3.0, -1.0, 0.0, 2.0])
    >>> list(output.numpy())
    [-0.9, -0.3, 0.0, 2.0]
    >>> layer = tf.keras.layers.LeakyReLU(alpha=0.1)
    >>> output = layer([-3.0, -1.0, 0.0, 2.0])
    >>> list(output.numpy())
    [-0.3, -0.1, 0.0, 2.0]

    Input shape:
      Arbitrary. Use the keyword argument `input_shape`
      (tuple of integers, does not include the batch axis)
      when using this layer as the first layer in a model.

    Output shape:
      Same shape as the input.

    Args:
      alpha: Float >= 0. Negative slope coefficient. Default to 0.3.

    """
    supports_masking: bool
    alpha: Incomplete
    def __init__(self, alpha: float = 0.3, **kwargs) -> None: ...
    def call(self, inputs): ...
    def get_config(self): ...
    def compute_output_shape(self, input_shape): ...
