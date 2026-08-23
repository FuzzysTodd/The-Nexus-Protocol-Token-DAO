from _typeshed import Incomplete
from keras.engine.base_layer import Layer as Layer
from keras.engine.input_spec import InputSpec as InputSpec
from keras.utils import conv_utils as conv_utils

class Cropping1D(Layer):
    """Cropping layer for 1D input (e.g. temporal sequence).

    It crops along the time dimension (axis 1).

    Examples:

    >>> input_shape = (2, 3, 2)
    >>> x = np.arange(np.prod(input_shape)).reshape(input_shape)
    >>> print(x)
    [[[ 0  1]
      [ 2  3]
      [ 4  5]]
     [[ 6  7]
      [ 8  9]
      [10 11]]]
    >>> y = tf.keras.layers.Cropping1D(cropping=1)(x)
    >>> print(y)
    tf.Tensor(
      [[[2 3]]
       [[8 9]]], shape=(2, 1, 2), dtype=int64)

    Args:
      cropping: Int or tuple of int (length 2)
        How many units should be trimmed off at the beginning and end of
        the cropping dimension (axis 1).
        If a single int is provided, the same value will be used for both.

    Input shape:
      3D tensor with shape `(batch_size, axis_to_crop, features)`

    Output shape:
      3D tensor with shape `(batch_size, cropped_axis, features)`
    """
    cropping: Incomplete
    input_spec: Incomplete
    def __init__(self, cropping=(1, 1), **kwargs) -> None: ...
    def compute_output_shape(self, input_shape): ...
    def call(self, inputs): ...
    def get_config(self): ...
