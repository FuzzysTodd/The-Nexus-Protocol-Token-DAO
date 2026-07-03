from _typeshed import Incomplete
from keras import activations as activations, constraints as constraints, initializers as initializers, regularizers as regularizers
from keras.dtensor import utils as utils
from keras.engine.input_spec import InputSpec as InputSpec
from keras.layers.convolutional.conv1d import Conv1D as Conv1D
from keras.utils import conv_utils as conv_utils

class Conv1DTranspose(Conv1D):
    '''Transposed convolution layer (sometimes called Deconvolution).

    The need for transposed convolutions generally arises
    from the desire to use a transformation going in the opposite direction
    of a normal convolution, i.e., from something that has the shape of the
    output of some convolution to something that has the shape of its input
    while maintaining a connectivity pattern that is compatible with
    said convolution.

    When using this layer as the first layer in a model,
    provide the keyword argument `input_shape`
    (tuple of integers or `None`, does not include the sample axis),
    e.g. `input_shape=(128, 3)` for data with 128 time steps and 3 channels.

    Args:
      filters: Integer, the dimensionality of the output space
        (i.e. the number of output filters in the convolution).
      kernel_size: An integer length of the 1D convolution window.
      strides: An integer specifying the stride of the convolution along the
        time dimension. Specifying a stride value != 1 is incompatible with
        specifying a `dilation_rate` value != 1. Defaults to 1.
      padding: one of `"valid"` or `"same"` (case-insensitive).
        `"valid"` means no padding. `"same"` results in padding with zeros
        evenly to the left/right or up/down of the input such that output has
        the same height/width dimension as the input.
      output_padding: An integer specifying the amount of padding along
        the time dimension of the output tensor.
        The amount of output padding must be lower than the stride.
        If set to `None` (default), the output shape is inferred.
      data_format: A string, one of `channels_last` (default) or
        `channels_first`.  The ordering of the dimensions in the inputs.
        `channels_last` corresponds to inputs with shape
        `(batch_size, length, channels)` while `channels_first` corresponds to
        inputs with shape `(batch_size, channels, length)`.
      dilation_rate: an integer, specifying
        the dilation rate to use for dilated convolution.
        Currently, specifying a `dilation_rate` value != 1 is
        incompatible with specifying a stride value != 1.
        Also dilation rate larger than 1 is not currently supported.
      activation: Activation function to use.
        If you don\'t specify anything, no activation is applied
        (see `keras.activations`).
      use_bias: Boolean, whether the layer uses a bias vector.
      kernel_initializer: Initializer for the `kernel` weights matrix
        (see `keras.initializers`). Defaults to \'glorot_uniform\'.
      bias_initializer: Initializer for the bias vector
        (see `keras.initializers`). Defaults to \'zeros\'.
      kernel_regularizer: Regularizer function applied to
        the `kernel` weights matrix (see `keras.regularizers`).
      bias_regularizer: Regularizer function applied to the bias vector
        (see `keras.regularizers`).
      activity_regularizer: Regularizer function applied to
        the output of the layer (its "activation") (see `keras.regularizers`).
      kernel_constraint: Constraint function applied to the kernel matrix
        (see `keras.constraints`).
      bias_constraint: Constraint function applied to the bias vector
        (see `keras.constraints`).

    Input shape:
      3D tensor with shape:
      `(batch_size, steps, channels)`

    Output shape:
      3D tensor with shape:
      `(batch_size, new_steps, filters)`
      If `output_padding` is specified:
      ```
      new_timesteps = ((timesteps - 1) * strides + kernel_size -
      2 * padding + output_padding)
      ```

    Returns:
      A tensor of rank 3 representing
      `activation(conv1dtranspose(inputs, kernel) + bias)`.

    Raises:
      ValueError: if `padding` is "causal".
      ValueError: when both `strides` > 1 and `dilation_rate` > 1.

    References:
      - [A guide to convolution arithmetic for deep learning](
        https://arxiv.org/abs/1603.07285v1)
      - [Deconvolutional Networks](
        https://www.matthewzeiler.com/mattzeiler/deconvolutionalnetworks.pdf)
    '''
    output_padding: Incomplete
    def __init__(self, filters, kernel_size, strides: int = 1, padding: str = 'valid', output_padding: Incomplete | None = None, data_format: Incomplete | None = None, dilation_rate: int = 1, activation: Incomplete | None = None, use_bias: bool = True, kernel_initializer: str = 'glorot_uniform', bias_initializer: str = 'zeros', kernel_regularizer: Incomplete | None = None, bias_regularizer: Incomplete | None = None, activity_regularizer: Incomplete | None = None, kernel_constraint: Incomplete | None = None, bias_constraint: Incomplete | None = None, **kwargs) -> None: ...
    input_spec: Incomplete
    kernel: Incomplete
    bias: Incomplete
    built: bool
    def build(self, input_shape) -> None: ...
    def call(self, inputs): ...
    def compute_output_shape(self, input_shape): ...
    def get_config(self): ...
Convolution1DTranspose = Conv1DTranspose
