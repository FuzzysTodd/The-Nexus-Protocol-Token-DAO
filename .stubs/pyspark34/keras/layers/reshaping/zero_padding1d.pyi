from _typeshed import Incomplete
from keras import backend as backend
from keras.engine.base_layer import Layer as Layer
from keras.engine.input_spec import InputSpec as InputSpec
from keras.utils import conv_utils as conv_utils

class ZeroPadding1D(Layer):
    """Zero-padding layer for 1D input (e.g. temporal sequence).

    Examples:

    >>> input_shape = (2, 2, 3)
    >>> x = np.arange(np.prod(input_shape)).reshape(input_shape)
    >>> print(x)
    [[[ 0  1  2]
      [ 3  4  5]]
     [[ 6  7  8]
      [ 9 10 11]]]
    >>> y = tf.keras.layers.ZeroPadding1D(padding=2)(x)
    >>> print(y)
    tf.Tensor(
      [[[ 0  0  0]
        [ 0  0  0]
        [ 0  1  2]
        [ 3  4  5]
        [ 0  0  0]
        [ 0  0  0]]
       [[ 0  0  0]
        [ 0  0  0]
        [ 6  7  8]
        [ 9 10 11]
        [ 0  0  0]
        [ 0  0  0]]], shape=(2, 6, 3), dtype=int64)

    Args:
        padding: Int, or tuple of int (length 2), or dictionary.
            - If int:
            How many zeros to add at the beginning and end of
            the padding dimension (axis 1).
            - If tuple of int (length 2):
            How many zeros to add at the beginning and the end of
            the padding dimension (`(left_pad, right_pad)`).

    Input shape:
        3D tensor with shape `(batch_size, axis_to_pad, features)`

    Output shape:
        3D tensor with shape `(batch_size, padded_axis, features)`
    """
    padding: Incomplete
    input_spec: Incomplete
    def __init__(self, padding: int = 1, **kwargs) -> None: ...
    def compute_output_shape(self, input_shape): ...
    def call(self, inputs): ...
    def get_config(self): ...
