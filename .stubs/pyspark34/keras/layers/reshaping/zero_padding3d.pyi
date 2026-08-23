from _typeshed import Incomplete
from keras import backend as backend
from keras.engine.base_layer import Layer as Layer
from keras.engine.input_spec import InputSpec as InputSpec
from keras.utils import conv_utils as conv_utils

class ZeroPadding3D(Layer):
    '''Zero-padding layer for 3D data (spatial or spatio-temporal).

    Examples:

    >>> input_shape = (1, 1, 2, 2, 3)
    >>> x = np.arange(np.prod(input_shape)).reshape(input_shape)
    >>> y = tf.keras.layers.ZeroPadding3D(padding=2)(x)
    >>> print(y.shape)
    (1, 5, 6, 6, 3)

    Args:
      padding: Int, or tuple of 3 ints, or tuple of 3 tuples of 2 ints.
        - If int: the same symmetric padding
          is applied to height and width.
        - If tuple of 3 ints:
          interpreted as two different
          symmetric padding values for height and width:
          `(symmetric_dim1_pad, symmetric_dim2_pad, symmetric_dim3_pad)`.
        - If tuple of 3 tuples of 2 ints:
          interpreted as
          `((left_dim1_pad, right_dim1_pad), (left_dim2_pad,
            right_dim2_pad), (left_dim3_pad, right_dim3_pad))`
      data_format: A string,
        one of `channels_last` (default) or `channels_first`.
        The ordering of the dimensions in the inputs.
        `channels_last` corresponds to inputs with shape
        `(batch_size, spatial_dim1, spatial_dim2, spatial_dim3, channels)`
        while `channels_first` corresponds to inputs with shape
        `(batch_size, channels, spatial_dim1, spatial_dim2, spatial_dim3)`.
        It defaults to the `image_data_format` value found in your
        Keras config file at `~/.keras/keras.json`.
        If you never set it, then it will be "channels_last".

    Input shape:
      5D tensor with shape:
      - If `data_format` is `"channels_last"`:
          `(batch_size, first_axis_to_pad, second_axis_to_pad,
          third_axis_to_pad, depth)`
      - If `data_format` is `"channels_first"`:
          `(batch_size, depth, first_axis_to_pad, second_axis_to_pad,
          third_axis_to_pad)`

    Output shape:
      5D tensor with shape:
      - If `data_format` is `"channels_last"`:
          `(batch_size, first_padded_axis, second_padded_axis,
          third_axis_to_pad, depth)`
      - If `data_format` is `"channels_first"`:
          `(batch_size, depth, first_padded_axis, second_padded_axis,
            third_axis_to_pad)`
    '''
    data_format: Incomplete
    padding: Incomplete
    input_spec: Incomplete
    def __init__(self, padding=(1, 1, 1), data_format: Incomplete | None = None, **kwargs) -> None: ...
    def compute_output_shape(self, input_shape): ...
    def call(self, inputs): ...
    def get_config(self): ...
