from _typeshed import Incomplete
from keras import backend as backend
from keras.engine.base_layer import Layer as Layer
from keras.utils import tf_utils as tf_utils

class Softmax(Layer):
    """Softmax activation function.

    Example without mask:

    >>> inp = np.asarray([1., 2., 1.])
    >>> layer = tf.keras.layers.Softmax()
    >>> layer(inp).numpy()
    array([0.21194157, 0.5761169 , 0.21194157], dtype=float32)
    >>> mask = np.asarray([True, False, True], dtype=bool)
    >>> layer(inp, mask).numpy()
    array([0.5, 0. , 0.5], dtype=float32)

    Input shape:
      Arbitrary. Use the keyword argument `input_shape`
      (tuple of integers, does not include the samples axis)
      when using this layer as the first layer in a model.

    Output shape:
      Same shape as the input.

    Args:
      axis: Integer, or list of Integers, axis along which the softmax
        normalization is applied.
    Call arguments:
      inputs: The inputs, or logits to the softmax layer.
      mask: A boolean mask of the same shape as `inputs`. Defaults to `None`.
        The mask specifies 1 to keep and 0 to mask.

    Returns:
      softmaxed output with the same shape as `inputs`.
    """
    supports_masking: bool
    axis: Incomplete
    def __init__(self, axis: int = -1, **kwargs) -> None: ...
    def call(self, inputs, mask: Incomplete | None = None): ...
    def get_config(self): ...
    def compute_output_shape(self, input_shape): ...
