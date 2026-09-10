from _typeshed import Incomplete
from keras.engine.base_layer import Layer as Layer
from keras.engine.input_spec import InputSpec as InputSpec
from keras.utils import conv_utils as conv_utils

class Cropping3D(Layer):
    '''Cropping layer for 3D data (e.g. spatial or spatio-temporal).

      Examples:

    >>> input_shape = (2, 28, 28, 10, 3)
    >>> x = np.arange(np.prod(input_shape)).reshape(input_shape)
    >>> y = tf.keras.layers.Cropping3D(cropping=(2, 4, 2))(x)
    >>> print(y.shape)
    (2, 24, 20, 6, 3)

    Args:
      cropping: Int, or tuple of 3 ints, or tuple of 3 tuples of 2 ints.
        - If int: the same symmetric cropping
          is applied to depth, height, and width.
        - If tuple of 3 ints: interpreted as two different
          symmetric cropping values for depth, height, and width:
          `(symmetric_dim1_crop, symmetric_dim2_crop, symmetric_dim3_crop)`.
        - If tuple of 3 tuples of 2 ints: interpreted as
          `((left_dim1_crop, right_dim1_crop), (left_dim2_crop,
            right_dim2_crop), (left_dim3_crop, right_dim3_crop))`
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
        `(batch_size, first_axis_to_crop, second_axis_to_crop,
        third_axis_to_crop, depth)`
      - If `data_format` is `"channels_first"`:
        `(batch_size, depth, first_axis_to_crop, second_axis_to_crop,
          third_axis_to_crop)`

    Output shape:
      5D tensor with shape:
      - If `data_format` is `"channels_last"`:
        `(batch_size, first_cropped_axis, second_cropped_axis,
        third_cropped_axis, depth)`
      - If `data_format` is `"channels_first"`:
        `(batch_size, depth, first_cropped_axis, second_cropped_axis,
          third_cropped_axis)`
    '''
    data_format: Incomplete
    cropping: Incomplete
    input_spec: Incomplete
    def __init__(self, cropping=((1, 1), (1, 1), (1, 1)), data_format: Incomplete | None = None, **kwargs) -> None: ...
    def compute_output_shape(self, input_shape): ...
    def call(self, inputs): ...
    def get_config(self): ...
