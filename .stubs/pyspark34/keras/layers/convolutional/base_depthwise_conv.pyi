from _typeshed import Incomplete
from keras import constraints as constraints, initializers as initializers, regularizers as regularizers
from keras.engine.input_spec import InputSpec as InputSpec
from keras.layers.convolutional.base_conv import Conv as Conv

class DepthwiseConv(Conv):
    '''Depthwise convolution.

    Depthwise convolution is a type of convolution in which each input channel
    is convolved with a different kernel (called a depthwise kernel). You can
    understand depthwise convolution as the first step in a depthwise separable
    convolution.

    It is implemented via the following steps:

    - Split the input into individual channels.
    - Convolve each channel with an individual depthwise kernel with
      `depth_multiplier` output channels.
    - Concatenate the convolved outputs along the channels axis.

    Unlike a regular convolution, depthwise convolution does not mix
    information across different input channels.

    The `depth_multiplier` argument determines how many filter are applied to
    one input channel. As such, it controls the amount of output channels that
    are generated per input channel in the depthwise step.

    Args:
      kernel_size: A tuple or list of integers specifying the spatial dimensions
        of the filters. Can be a single integer to specify the same value for
        all spatial dimensions.
      strides: A tuple or list of integers specifying the strides of the
        convolution. Can be a single integer to specify the same value for all
        spatial dimensions. Specifying any `stride` value != 1 is incompatible
        with specifying any `dilation_rate` value != 1.
      padding: One of `"valid"` or `"same"` (case-insensitive). `"valid"` means
        no padding. `"same"` results in padding with zeros evenly to the
        left/right or up/down of the input such that output has the same
        height/width dimension as the input.
      depth_multiplier: The number of depthwise convolution output channels for
        each input channel. The total number of depthwise convolution output
        channels will be equal to `filters_in * depth_multiplier`.
      data_format: A string, one of `channels_last` (default) or
        `channels_first`.  The ordering of the dimensions in the inputs.
        `channels_last` corresponds to inputs with shape `(batch_size, height,
        width, channels)` while `channels_first` corresponds to inputs with
        shape `(batch_size, channels, height, width)`. It defaults to the
        `image_data_format` value found in your Keras config file at
        `~/.keras/keras.json`. If you never set it, then it will be
        \'channels_last\'.
      dilation_rate: An integer or tuple/list of 2 integers, specifying the
        dilation rate to use for dilated convolution. Currently, specifying any
        `dilation_rate` value != 1 is incompatible with specifying any `strides`
        value != 1.
      activation: Activation function to use. If you don\'t specify anything, no
        activation is applied (see `keras.activations`).
      use_bias: Boolean, whether the layer uses a bias vector.
      depthwise_initializer: Initializer for the depthwise kernel matrix (see
        `keras.initializers`). If None, the default initializer
        (\'glorot_uniform\') will be used.
      bias_initializer: Initializer for the bias vector (see
        `keras.initializers`). If None, the default initializer (\'zeros\') will
        be used.
      depthwise_regularizer: Regularizer function applied to the depthwise
        kernel matrix (see `keras.regularizers`).
      bias_regularizer: Regularizer function applied to the bias vector (see
        `keras.regularizers`).
      activity_regularizer: Regularizer function applied to the output of the
        layer (its \'activation\') (see `keras.regularizers`).
      depthwise_constraint: Constraint function applied to the depthwise kernel
        matrix (see `keras.constraints`).
      bias_constraint: Constraint function applied to the bias vector (see
        `keras.constraints`).

    Input shape:
      4D tensor with shape: `[batch_size, channels, rows, cols]` if
        data_format=\'channels_first\'
      or 4D tensor with shape: `[batch_size, rows, cols, channels]` if
        data_format=\'channels_last\'.

    Output shape:
      4D tensor with shape: `[batch_size, channels * depth_multiplier, new_rows,
        new_cols]` if `data_format=\'channels_first\'`
        or 4D tensor with shape: `[batch_size,
        new_rows, new_cols, channels * depth_multiplier]` if
        `data_format=\'channels_last\'`. `rows` and `cols` values might have
        changed due to padding.

    Returns:
      A tensor of rank 4 representing
      `activation(depthwiseconv2d(inputs, kernel) + bias)`.

    Raises:
      ValueError: if `padding` is "causal".
      ValueError: when both `strides` > 1 and `dilation_rate` > 1.
    '''
    depth_multiplier: Incomplete
    depthwise_initializer: Incomplete
    depthwise_regularizer: Incomplete
    depthwise_constraint: Incomplete
    bias_initializer: Incomplete
    def __init__(self, rank, kernel_size, strides: int = 1, padding: str = 'valid', depth_multiplier: int = 1, data_format: Incomplete | None = None, dilation_rate: int = 1, activation: Incomplete | None = None, use_bias: bool = True, depthwise_initializer: str = 'glorot_uniform', bias_initializer: str = 'zeros', depthwise_regularizer: Incomplete | None = None, bias_regularizer: Incomplete | None = None, activity_regularizer: Incomplete | None = None, depthwise_constraint: Incomplete | None = None, bias_constraint: Incomplete | None = None, **kwargs) -> None: ...
    depthwise_kernel: Incomplete
    bias: Incomplete
    input_spec: Incomplete
    built: bool
    def build(self, input_shape) -> None: ...
    def call(self, inputs) -> None: ...
    def get_config(self): ...
