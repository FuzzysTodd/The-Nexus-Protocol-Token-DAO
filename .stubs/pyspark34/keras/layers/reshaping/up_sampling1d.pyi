from _typeshed import Incomplete
from keras import backend as backend
from keras.engine.base_layer import Layer as Layer
from keras.engine.input_spec import InputSpec as InputSpec

class UpSampling1D(Layer):
    """Upsampling layer for 1D inputs.

    Repeats each temporal step `size` times along the time axis.

    Examples:

    >>> input_shape = (2, 2, 3)
    >>> x = np.arange(np.prod(input_shape)).reshape(input_shape)
    >>> print(x)
    [[[ 0  1  2]
      [ 3  4  5]]
     [[ 6  7  8]
      [ 9 10 11]]]
    >>> y = tf.keras.layers.UpSampling1D(size=2)(x)
    >>> print(y)
    tf.Tensor(
      [[[ 0  1  2]
        [ 0  1  2]
        [ 3  4  5]
        [ 3  4  5]]
       [[ 6  7  8]
        [ 6  7  8]
        [ 9 10 11]
        [ 9 10 11]]], shape=(2, 4, 3), dtype=int64)

    Args:
      size: Integer. Upsampling factor.

    Input shape:
      3D tensor with shape: `(batch_size, steps, features)`.

    Output shape:
      3D tensor with shape: `(batch_size, upsampled_steps, features)`.
    """
    size: Incomplete
    input_spec: Incomplete
    def __init__(self, size: int = 2, **kwargs) -> None: ...
    def compute_output_shape(self, input_shape): ...
    def call(self, inputs): ...
    def get_config(self): ...
