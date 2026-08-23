from _typeshed import Incomplete
from keras.engine.base_layer import Layer as Layer
from keras.engine.input_spec import InputSpec as InputSpec
from keras.utils import conv_utils as conv_utils

class Flatten(Layer):
    '''Flattens the input. Does not affect the batch size.

    Note: If inputs are shaped `(batch,)` without a feature axis, then
    flattening adds an extra channel dimension and output shape is `(batch, 1)`.

    Args:
      data_format: A string,
        one of `channels_last` (default) or `channels_first`.
        The ordering of the dimensions in the inputs.
        `channels_last` corresponds to inputs with shape
        `(batch, ..., channels)` while `channels_first` corresponds to
        inputs with shape `(batch, channels, ...)`.
        It defaults to the `image_data_format` value found in your
        Keras config file at `~/.keras/keras.json`.
        If you never set it, then it will be "channels_last".

    Example:

    >>> model = tf.keras.Sequential()
    >>> model.add(tf.keras.layers.Conv2D(64, 3, 3, input_shape=(3, 32, 32)))
    >>> model.output_shape
    (None, 1, 10, 64)

    >>> model.add(Flatten())
    >>> model.output_shape
    (None, 640)

    '''
    data_format: Incomplete
    input_spec: Incomplete
    def __init__(self, data_format: Incomplete | None = None, **kwargs) -> None: ...
    def call(self, inputs): ...
    def compute_output_shape(self, input_shape): ...
    def get_config(self): ...
