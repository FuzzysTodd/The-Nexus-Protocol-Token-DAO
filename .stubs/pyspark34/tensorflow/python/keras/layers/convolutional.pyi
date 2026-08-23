from _typeshed import Incomplete
from tensorflow.python.eager import context as context
from tensorflow.python.framework import tensor_shape as tensor_shape
from tensorflow.python.keras import activations as activations, backend as backend, constraints as constraints, initializers as initializers, regularizers as regularizers
from tensorflow.python.keras.engine.base_layer import Layer as Layer
from tensorflow.python.keras.engine.input_spec import InputSpec as InputSpec
from tensorflow.python.keras.layers.pooling import AveragePooling1D as AveragePooling1D, AveragePooling2D as AveragePooling2D, AveragePooling3D as AveragePooling3D, MaxPooling1D as MaxPooling1D, MaxPooling2D as MaxPooling2D, MaxPooling3D as MaxPooling3D
from tensorflow.python.keras.utils import conv_utils as conv_utils, tf_utils as tf_utils
from tensorflow.python.ops import array_ops as array_ops, nn as nn, nn_ops as nn_ops
from tensorflow.python.util.tf_export import keras_export as keras_export

class Conv(Layer):
    '''Abstract N-D convolution layer (private, used as implementation base).

  This layer creates a convolution kernel that is convolved
  (actually cross-correlated) with the layer input to produce a tensor of
  outputs. If `use_bias` is True (and a `bias_initializer` is provided),
  a bias vector is created and added to the outputs. Finally, if
  `activation` is not `None`, it is applied to the outputs as well.

  Note: layer attributes cannot be modified after the layer has been called
  once (except the `trainable` attribute).

  Args:
    rank: An integer, the rank of the convolution, e.g. "2" for 2D convolution.
    filters: Integer, the dimensionality of the output space (i.e. the number
      of filters in the convolution). Could be "None", eg in the case of
      depth wise convolution.
    kernel_size: An integer or tuple/list of n integers, specifying the
      length of the convolution window.
    strides: An integer or tuple/list of n integers,
      specifying the stride length of the convolution.
      Specifying any stride value != 1 is incompatible with specifying
      any `dilation_rate` value != 1.
    padding: One of `"valid"`,  `"same"`, or `"causal"` (case-insensitive).
      `"valid"` means no padding. `"same"` results in padding with zeros
      evenly to the left/right or up/down of the input such that output has the
      same height/width dimension as the input. `"causal"` results in causal
      (dilated) convolutions, e.g. `output[t]` does not depend on `input[t+1:]`.
    data_format: A string, one of `channels_last` (default) or `channels_first`.
      The ordering of the dimensions in the inputs.
      `channels_last` corresponds to inputs with shape
      `(batch_size, ..., channels)` while `channels_first` corresponds to
      inputs with shape `(batch_size, channels, ...)`.
      Note: `channels_first` is only available on GPUs.
    dilation_rate: An integer or tuple/list of n integers, specifying
      the dilation rate to use for dilated convolution.
      Currently, specifying any `dilation_rate` value != 1 is
      incompatible with specifying any `strides` value != 1.
    groups: A positive integer specifying the number of groups in which the
      input is split along the channel axis. Each group is convolved
      separately with `filters / groups` filters. The output is the
      concatenation of all the `groups` results along the channel axis.
      Input channels and `filters` must both be divisible by `groups`.
    activation: Activation function to use.
      If you don\'t specify anything, no activation is applied.
    use_bias: Boolean, whether the layer uses a bias.
    kernel_initializer: An initializer for the convolution kernel. If None, the 
      default initializer (glorot_uniform) will be used. 
    bias_initializer: An initializer for the bias vector. If None, the default
      initializer (zeros) will be used.
    kernel_regularizer: Optional regularizer for the convolution kernel.
    bias_regularizer: Optional regularizer for the bias vector.
    activity_regularizer: Optional regularizer function for the output.
    kernel_constraint: Optional projection function to be applied to the
        kernel after being updated by an `Optimizer` (e.g. used to implement
        norm constraints or value constraints for layer weights). The function
        must take as input the unprojected variable and must return the
        projected variable (which must have the same shape). Constraints are
        not safe to use when doing asynchronous distributed training.
    bias_constraint: Optional projection function to be applied to the
        bias after being updated by an `Optimizer`.
  '''
    rank: Incomplete
    filters: Incomplete
    groups: Incomplete
    kernel_size: Incomplete
    strides: Incomplete
    padding: Incomplete
    data_format: Incomplete
    dilation_rate: Incomplete
    activation: Incomplete
    use_bias: Incomplete
    kernel_initializer: Incomplete
    bias_initializer: Incomplete
    kernel_regularizer: Incomplete
    bias_regularizer: Incomplete
    kernel_constraint: Incomplete
    bias_constraint: Incomplete
    input_spec: Incomplete
    def __init__(self, rank, filters, kernel_size, strides: int = 1, padding: str = 'valid', data_format: Incomplete | None = None, dilation_rate: int = 1, groups: int = 1, activation: Incomplete | None = None, use_bias: bool = True, kernel_initializer: str = 'glorot_uniform', bias_initializer: str = 'zeros', kernel_regularizer: Incomplete | None = None, bias_regularizer: Incomplete | None = None, activity_regularizer: Incomplete | None = None, kernel_constraint: Incomplete | None = None, bias_constraint: Incomplete | None = None, trainable: bool = True, name: Incomplete | None = None, conv_op: Incomplete | None = None, **kwargs) -> None: ...
    kernel: Incomplete
    bias: Incomplete
    built: bool
    def build(self, input_shape) -> None: ...
    def call(self, inputs): ...
    def compute_output_shape(self, input_shape): ...
    def get_config(self): ...

class Conv1D(Conv):
    '''1D convolution layer (e.g. temporal convolution).

  This layer creates a convolution kernel that is convolved
  with the layer input over a single spatial (or temporal) dimension
  to produce a tensor of outputs.
  If `use_bias` is True, a bias vector is created and added to the outputs.
  Finally, if `activation` is not `None`,
  it is applied to the outputs as well.

  When using this layer as the first layer in a model,
  provide an `input_shape` argument
  (tuple of integers or `None`, e.g.
  `(10, 128)` for sequences of 10 vectors of 128-dimensional vectors,
  or `(None, 128)` for variable-length sequences of 128-dimensional vectors.

  Examples:

  >>> # The inputs are 128-length vectors with 10 timesteps, and the batch size
  >>> # is 4.
  >>> input_shape = (4, 10, 128)
  >>> x = tf.random.normal(input_shape)
  >>> y = tf.keras.layers.Conv1D(
  ... 32, 3, activation=\'relu\',input_shape=input_shape[1:])(x)
  >>> print(y.shape)
  (4, 8, 32)

  >>> # With extended batch shape [4, 7] (e.g. weather data where batch
  >>> # dimensions correspond to spatial location and the third dimension
  >>> # corresponds to time.)
  >>> input_shape = (4, 7, 10, 128)
  >>> x = tf.random.normal(input_shape)
  >>> y = tf.keras.layers.Conv1D(
  ... 32, 3, activation=\'relu\', input_shape=input_shape[2:])(x)
  >>> print(y.shape)
  (4, 7, 8, 32)

  Args:
    filters: Integer, the dimensionality of the output space
      (i.e. the number of output filters in the convolution).
    kernel_size: An integer or tuple/list of a single integer,
      specifying the length of the 1D convolution window.
    strides: An integer or tuple/list of a single integer,
      specifying the stride length of the convolution.
      Specifying any stride value != 1 is incompatible with specifying
      any `dilation_rate` value != 1.
    padding: One of `"valid"`, `"same"` or `"causal"` (case-insensitive).
      `"valid"` means no padding. `"same"` results in padding with zeros evenly
      to the left/right or up/down of the input such that output has the same
      height/width dimension as the input.
      `"causal"` results in causal (dilated) convolutions, e.g. `output[t]`
      does not depend on `input[t+1:]`. Useful when modeling temporal data
      where the model should not violate the temporal order.
      See [WaveNet: A Generative Model for Raw Audio, section
        2.1](https://arxiv.org/abs/1609.03499).
    data_format: A string,
      one of `channels_last` (default) or `channels_first`.
    dilation_rate: an integer or tuple/list of a single integer, specifying
      the dilation rate to use for dilated convolution.
      Currently, specifying any `dilation_rate` value != 1 is
      incompatible with specifying any `strides` value != 1.
    groups: A positive integer specifying the number of groups in which the
      input is split along the channel axis. Each group is convolved
      separately with `filters / groups` filters. The output is the
      concatenation of all the `groups` results along the channel axis.
      Input channels and `filters` must both be divisible by `groups`.
    activation: Activation function to use.
      If you don\'t specify anything, no activation is applied (
      see `keras.activations`).
    use_bias: Boolean, whether the layer uses a bias vector.
    kernel_initializer: Initializer for the `kernel` weights matrix (
      see `keras.initializers`). Defaults to \'glorot_uniform\'.
    bias_initializer: Initializer for the bias vector (
      see `keras.initializers`). Defaults to \'zeros\'.
    kernel_regularizer: Regularizer function applied to
      the `kernel` weights matrix (see `keras.regularizers`).
    bias_regularizer: Regularizer function applied to the bias vector (
      see `keras.regularizers`).
    activity_regularizer: Regularizer function applied to
      the output of the layer (its "activation") (
      see `keras.regularizers`).
    kernel_constraint: Constraint function applied to the kernel matrix (
      see `keras.constraints`).
    bias_constraint: Constraint function applied to the bias vector (
      see `keras.constraints`).

  Input shape:
    3+D tensor with shape: `batch_shape + (steps, input_dim)`

  Output shape:
    3+D tensor with shape: `batch_shape + (new_steps, filters)`
      `steps` value might have changed due to padding or strides.

  Returns:
    A tensor of rank 3 representing
    `activation(conv1d(inputs, kernel) + bias)`.

  Raises:
    ValueError: when both `strides > 1` and `dilation_rate > 1`.
  '''
    def __init__(self, filters, kernel_size, strides: int = 1, padding: str = 'valid', data_format: str = 'channels_last', dilation_rate: int = 1, groups: int = 1, activation: Incomplete | None = None, use_bias: bool = True, kernel_initializer: str = 'glorot_uniform', bias_initializer: str = 'zeros', kernel_regularizer: Incomplete | None = None, bias_regularizer: Incomplete | None = None, activity_regularizer: Incomplete | None = None, kernel_constraint: Incomplete | None = None, bias_constraint: Incomplete | None = None, **kwargs) -> None: ...

class Conv2D(Conv):
    '''2D convolution layer (e.g. spatial convolution over images).

  This layer creates a convolution kernel that is convolved
  with the layer input to produce a tensor of
  outputs. If `use_bias` is True,
  a bias vector is created and added to the outputs. Finally, if
  `activation` is not `None`, it is applied to the outputs as well.

  When using this layer as the first layer in a model,
  provide the keyword argument `input_shape`
  (tuple of integers or `None`, does not include the sample axis),
  e.g. `input_shape=(128, 128, 3)` for 128x128 RGB pictures
  in `data_format="channels_last"`. You can use `None` when
  a dimension has variable size.

  Examples:

  >>> # The inputs are 28x28 RGB images with `channels_last` and the batch
  >>> # size is 4.
  >>> input_shape = (4, 28, 28, 3)
  >>> x = tf.random.normal(input_shape)
  >>> y = tf.keras.layers.Conv2D(
  ... 2, 3, activation=\'relu\', input_shape=input_shape[1:])(x)
  >>> print(y.shape)
  (4, 26, 26, 2)

  >>> # With `dilation_rate` as 2.
  >>> input_shape = (4, 28, 28, 3)
  >>> x = tf.random.normal(input_shape)
  >>> y = tf.keras.layers.Conv2D(
  ... 2, 3, activation=\'relu\', dilation_rate=2, input_shape=input_shape[1:])(x)
  >>> print(y.shape)
  (4, 24, 24, 2)

  >>> # With `padding` as "same".
  >>> input_shape = (4, 28, 28, 3)
  >>> x = tf.random.normal(input_shape)
  >>> y = tf.keras.layers.Conv2D(
  ... 2, 3, activation=\'relu\', padding="same", input_shape=input_shape[1:])(x)
  >>> print(y.shape)
  (4, 28, 28, 2)

  >>> # With extended batch shape [4, 7]:
  >>> input_shape = (4, 7, 28, 28, 3)
  >>> x = tf.random.normal(input_shape)
  >>> y = tf.keras.layers.Conv2D(
  ... 2, 3, activation=\'relu\', input_shape=input_shape[2:])(x)
  >>> print(y.shape)
  (4, 7, 26, 26, 2)


  Args:
    filters: Integer, the dimensionality of the output space (i.e. the number of
      output filters in the convolution).
    kernel_size: An integer or tuple/list of 2 integers, specifying the height
      and width of the 2D convolution window. Can be a single integer to specify
      the same value for all spatial dimensions.
    strides: An integer or tuple/list of 2 integers, specifying the strides of
      the convolution along the height and width. Can be a single integer to
      specify the same value for all spatial dimensions. Specifying any stride
      value != 1 is incompatible with specifying any `dilation_rate` value != 1.
    padding: one of `"valid"` or `"same"` (case-insensitive).
      `"valid"` means no padding. `"same"` results in padding with zeros evenly
      to the left/right or up/down of the input such that output has the same
      height/width dimension as the input.
    data_format: A string, one of `channels_last` (default) or `channels_first`.
      The ordering of the dimensions in the inputs. `channels_last` corresponds
      to inputs with shape `(batch_size, height, width, channels)` while
      `channels_first` corresponds to inputs with shape `(batch_size, channels,
      height, width)`. It defaults to the `image_data_format` value found in
      your Keras config file at `~/.keras/keras.json`. If you never set it, then
      it will be `channels_last`.
    dilation_rate: an integer or tuple/list of 2 integers, specifying the
      dilation rate to use for dilated convolution. Can be a single integer to
      specify the same value for all spatial dimensions. Currently, specifying
      any `dilation_rate` value != 1 is incompatible with specifying any stride
      value != 1.
    groups: A positive integer specifying the number of groups in which the
      input is split along the channel axis. Each group is convolved separately
      with `filters / groups` filters. The output is the concatenation of all
      the `groups` results along the channel axis. Input channels and `filters`
      must both be divisible by `groups`.
    activation: Activation function to use. If you don\'t specify anything, no
      activation is applied (see `keras.activations`).
    use_bias: Boolean, whether the layer uses a bias vector.
    kernel_initializer: Initializer for the `kernel` weights matrix (see
      `keras.initializers`). Defaults to \'glorot_uniform\'.
    bias_initializer: Initializer for the bias vector (see
      `keras.initializers`). Defaults to \'zeros\'.
    kernel_regularizer: Regularizer function applied to the `kernel` weights
      matrix (see `keras.regularizers`). 
    bias_regularizer: Regularizer function applied to the bias vector (see
      `keras.regularizers`). 
    activity_regularizer: Regularizer function applied to the output of the
      layer (its "activation") (see `keras.regularizers`).
    kernel_constraint: Constraint function applied to the kernel matrix (see
      `keras.constraints`).
    bias_constraint: Constraint function applied to the bias vector (see
      `keras.constraints`).
  Input shape:
    4+D tensor with shape: `batch_shape + (channels, rows, cols)` if
      `data_format=\'channels_first\'`
    or 4+D tensor with shape: `batch_shape + (rows, cols, channels)` if
      `data_format=\'channels_last\'`.
  Output shape:
    4+D tensor with shape: `batch_shape + (filters, new_rows, new_cols)` if
    `data_format=\'channels_first\'` or 4+D tensor with shape: `batch_shape +
      (new_rows, new_cols, filters)` if `data_format=\'channels_last\'`.  `rows`
      and `cols` values might have changed due to padding.

  Returns:
    A tensor of rank 4+ representing
    `activation(conv2d(inputs, kernel) + bias)`.

  Raises:
    ValueError: if `padding` is `"causal"`.
    ValueError: when both `strides > 1` and `dilation_rate > 1`.
  '''
    def __init__(self, filters, kernel_size, strides=(1, 1), padding: str = 'valid', data_format: Incomplete | None = None, dilation_rate=(1, 1), groups: int = 1, activation: Incomplete | None = None, use_bias: bool = True, kernel_initializer: str = 'glorot_uniform', bias_initializer: str = 'zeros', kernel_regularizer: Incomplete | None = None, bias_regularizer: Incomplete | None = None, activity_regularizer: Incomplete | None = None, kernel_constraint: Incomplete | None = None, bias_constraint: Incomplete | None = None, **kwargs) -> None: ...

class Conv3D(Conv):
    '''3D convolution layer (e.g. spatial convolution over volumes).

  This layer creates a convolution kernel that is convolved
  with the layer input to produce a tensor of
  outputs. If `use_bias` is True,
  a bias vector is created and added to the outputs. Finally, if
  `activation` is not `None`, it is applied to the outputs as well.

  When using this layer as the first layer in a model,
  provide the keyword argument `input_shape`
  (tuple of integers or `None`, does not include the sample axis),
  e.g. `input_shape=(128, 128, 128, 1)` for 128x128x128 volumes
  with a single channel,
  in `data_format="channels_last"`.

  Examples:

  >>> # The inputs are 28x28x28 volumes with a single channel, and the
  >>> # batch size is 4
  >>> input_shape =(4, 28, 28, 28, 1)
  >>> x = tf.random.normal(input_shape)
  >>> y = tf.keras.layers.Conv3D(
  ... 2, 3, activation=\'relu\', input_shape=input_shape[1:])(x)
  >>> print(y.shape)
  (4, 26, 26, 26, 2)

  >>> # With extended batch shape [4, 7], e.g. a batch of 4 videos of 3D frames,
  >>> # with 7 frames per video.
  >>> input_shape = (4, 7, 28, 28, 28, 1)
  >>> x = tf.random.normal(input_shape)
  >>> y = tf.keras.layers.Conv3D(
  ... 2, 3, activation=\'relu\', input_shape=input_shape[2:])(x)
  >>> print(y.shape)
  (4, 7, 26, 26, 26, 2)

  Args:
    filters: Integer, the dimensionality of the output space (i.e. the number of
      output filters in the convolution).
    kernel_size: An integer or tuple/list of 3 integers, specifying the depth,
      height and width of the 3D convolution window. Can be a single integer to
      specify the same value for all spatial dimensions.
    strides: An integer or tuple/list of 3 integers, specifying the strides of
      the convolution along each spatial dimension. Can be a single integer to
      specify the same value for all spatial dimensions. Specifying any stride
      value != 1 is incompatible with specifying any `dilation_rate` value != 1.
    padding: one of `"valid"` or `"same"` (case-insensitive).
      `"valid"` means no padding. `"same"` results in padding with zeros evenly
      to the left/right or up/down of the input such that output has the same
      height/width dimension as the input.
    data_format: A string, one of `channels_last` (default) or `channels_first`.
      The ordering of the dimensions in the inputs. `channels_last` corresponds
      to inputs with shape `batch_shape + (spatial_dim1, spatial_dim2,
      spatial_dim3, channels)` while `channels_first` corresponds to inputs with
      shape `batch_shape + (channels, spatial_dim1, spatial_dim2,
      spatial_dim3)`. It defaults to the `image_data_format` value found in your
      Keras config file at `~/.keras/keras.json`. If you never set it, then it
      will be "channels_last".
    dilation_rate: an integer or tuple/list of 3 integers, specifying the
      dilation rate to use for dilated convolution. Can be a single integer to
      specify the same value for all spatial dimensions. Currently, specifying
      any `dilation_rate` value != 1 is incompatible with specifying any stride
      value != 1.
    groups: A positive integer specifying the number of groups in which the
      input is split along the channel axis. Each group is convolved separately
      with `filters / groups` filters. The output is the concatenation of all
      the `groups` results along the channel axis. Input channels and `filters`
      must both be divisible by `groups`.
    activation: Activation function to use. If you don\'t specify anything, no
      activation is applied (see `keras.activations`).
    use_bias: Boolean, whether the layer uses a bias vector.
    kernel_initializer: Initializer for the `kernel` weights matrix (see
      `keras.initializers`). Defaults to \'glorot_uniform\'.
    bias_initializer: Initializer for the bias vector (see
      `keras.initializers`). Defaults to \'zeros\'.
    kernel_regularizer: Regularizer function applied to the `kernel` weights
      matrix (see `keras.regularizers`).
    bias_regularizer: Regularizer function applied to the bias vector (see
      `keras.regularizers`).
    activity_regularizer: Regularizer function applied to the output of the
      layer (its "activation") (see `keras.regularizers`).
    kernel_constraint: Constraint function applied to the kernel matrix (see
      `keras.constraints`).
    bias_constraint: Constraint function applied to the bias vector (see
      `keras.constraints`).
  Input shape:
    5+D tensor with shape: `batch_shape + (channels, conv_dim1, conv_dim2,
      conv_dim3)` if data_format=\'channels_first\'
    or 5+D tensor with shape: `batch_shape + (conv_dim1, conv_dim2, conv_dim3,
      channels)` if data_format=\'channels_last\'.
  Output shape:
    5+D tensor with shape: `batch_shape + (filters, new_conv_dim1,
      new_conv_dim2, new_conv_dim3)` if data_format=\'channels_first\'
    or 5+D tensor with shape: `batch_shape + (new_conv_dim1, new_conv_dim2,
      new_conv_dim3, filters)` if data_format=\'channels_last\'. `new_conv_dim1`,
      `new_conv_dim2` and `new_conv_dim3` values might have changed due to
      padding.

  Returns:
    A tensor of rank 5+ representing
    `activation(conv3d(inputs, kernel) + bias)`.

  Raises:
    ValueError: if `padding` is "causal".
    ValueError: when both `strides > 1` and `dilation_rate > 1`.
  '''
    def __init__(self, filters, kernel_size, strides=(1, 1, 1), padding: str = 'valid', data_format: Incomplete | None = None, dilation_rate=(1, 1, 1), groups: int = 1, activation: Incomplete | None = None, use_bias: bool = True, kernel_initializer: str = 'glorot_uniform', bias_initializer: str = 'zeros', kernel_regularizer: Incomplete | None = None, bias_regularizer: Incomplete | None = None, activity_regularizer: Incomplete | None = None, kernel_constraint: Incomplete | None = None, bias_constraint: Incomplete | None = None, **kwargs) -> None: ...

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
      `"valid"` means no padding. `"same"` results in padding with zeros evenly
      to the left/right or up/down of the input such that output has the same
      height/width dimension as the input.
    output_padding: An integer specifying the amount of padding along
      the time dimension of the output tensor.
      The amount of output padding must be lower than the stride.
      If set to `None` (default), the output shape is inferred.
    data_format: A string, one of `channels_last` (default) or `channels_first`.
      The ordering of the dimensions in the inputs.
      `channels_last` corresponds to inputs with shape
      `(batch_size, length, channels)` while `channels_first` corresponds to
      inputs with shape `(batch_size, channels, length)`.
    dilation_rate: an integer, specifying
      the dilation rate to use for dilated convolution.
      Currently, specifying a `dilation_rate` value != 1 is
      incompatible with specifying a stride value != 1.
      Also dilation rate larger than 1 is not currently supported.
    activation: Activation function to use.
      If you don\'t specify anything, no activation is applied (
      see `keras.activations`).
    use_bias: Boolean, whether the layer uses a bias vector.
    kernel_initializer: Initializer for the `kernel` weights matrix (
      see `keras.initializers`). Defaults to \'glorot_uniform\'.
    bias_initializer: Initializer for the bias vector (
      see `keras.initializers`). Defaults to \'zeros\'.
    kernel_regularizer: Regularizer function applied to
      the `kernel` weights matrix (see `keras.regularizers`).
    bias_regularizer: Regularizer function applied to the bias vector (
      see `keras.regularizers`).
    activity_regularizer: Regularizer function applied to
      the output of the layer (its "activation") (see `keras.regularizers`).
    kernel_constraint: Constraint function applied to the kernel matrix (
      see `keras.constraints`).
    bias_constraint: Constraint function applied to the bias vector (
      see `keras.constraints`).

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

class Conv2DTranspose(Conv2D):
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
  e.g. `input_shape=(128, 128, 3)` for 128x128 RGB pictures
  in `data_format="channels_last"`.

  Args:
    filters: Integer, the dimensionality of the output space
      (i.e. the number of output filters in the convolution).
    kernel_size: An integer or tuple/list of 2 integers, specifying the
      height and width of the 2D convolution window.
      Can be a single integer to specify the same value for
      all spatial dimensions.
    strides: An integer or tuple/list of 2 integers,
      specifying the strides of the convolution along the height and width.
      Can be a single integer to specify the same value for
      all spatial dimensions.
      Specifying any stride value != 1 is incompatible with specifying
      any `dilation_rate` value != 1.
    padding: one of `"valid"` or `"same"` (case-insensitive).
      `"valid"` means no padding. `"same"` results in padding with zeros evenly
      to the left/right or up/down of the input such that output has the same
      height/width dimension as the input.
    output_padding: An integer or tuple/list of 2 integers,
      specifying the amount of padding along the height and width
      of the output tensor.
      Can be a single integer to specify the same value for all
      spatial dimensions.
      The amount of output padding along a given dimension must be
      lower than the stride along that same dimension.
      If set to `None` (default), the output shape is inferred.
    data_format: A string,
      one of `channels_last` (default) or `channels_first`.
      The ordering of the dimensions in the inputs.
      `channels_last` corresponds to inputs with shape
      `(batch_size, height, width, channels)` while `channels_first`
      corresponds to inputs with shape
      `(batch_size, channels, height, width)`.
      It defaults to the `image_data_format` value found in your
      Keras config file at `~/.keras/keras.json`.
      If you never set it, then it will be "channels_last".
    dilation_rate: an integer or tuple/list of 2 integers, specifying
      the dilation rate to use for dilated convolution.
      Can be a single integer to specify the same value for
      all spatial dimensions.
      Currently, specifying any `dilation_rate` value != 1 is
      incompatible with specifying any stride value != 1.
    activation: Activation function to use.
      If you don\'t specify anything, no activation is applied (
      see `keras.activations`).
    use_bias: Boolean, whether the layer uses a bias vector.
    kernel_initializer: Initializer for the `kernel` weights matrix (
      see `keras.initializers`). Defaults to \'glorot_uniform\'.
    bias_initializer: Initializer for the bias vector (
      see `keras.initializers`). Defaults to \'zeros\'.
    kernel_regularizer: Regularizer function applied to
      the `kernel` weights matrix (see `keras.regularizers`).
    bias_regularizer: Regularizer function applied to the bias vector (
      see `keras.regularizers`).
    activity_regularizer: Regularizer function applied to
      the output of the layer (its "activation") (see `keras.regularizers`).
    kernel_constraint: Constraint function applied to the kernel matrix (
      see `keras.constraints`).
    bias_constraint: Constraint function applied to the bias vector (
      see `keras.constraints`).

  Input shape:
    4D tensor with shape:
    `(batch_size, channels, rows, cols)` if data_format=\'channels_first\'
    or 4D tensor with shape:
    `(batch_size, rows, cols, channels)` if data_format=\'channels_last\'.

  Output shape:
    4D tensor with shape:
    `(batch_size, filters, new_rows, new_cols)` if data_format=\'channels_first\'
    or 4D tensor with shape:
    `(batch_size, new_rows, new_cols, filters)` if data_format=\'channels_last\'.
    `rows` and `cols` values might have changed due to padding.
    If `output_padding` is specified:
    ```
    new_rows = ((rows - 1) * strides[0] + kernel_size[0] - 2 * padding[0] +
    output_padding[0])
    new_cols = ((cols - 1) * strides[1] + kernel_size[1] - 2 * padding[1] +
    output_padding[1])
    ```

  Returns:
    A tensor of rank 4 representing
    `activation(conv2dtranspose(inputs, kernel) + bias)`.

  Raises:
    ValueError: if `padding` is "causal".
    ValueError: when both `strides` > 1 and `dilation_rate` > 1.

  References:
    - [A guide to convolution arithmetic for deep
      learning](https://arxiv.org/abs/1603.07285v1)
    - [Deconvolutional
      Networks](https://www.matthewzeiler.com/mattzeiler/deconvolutionalnetworks.pdf)
  '''
    output_padding: Incomplete
    def __init__(self, filters, kernel_size, strides=(1, 1), padding: str = 'valid', output_padding: Incomplete | None = None, data_format: Incomplete | None = None, dilation_rate=(1, 1), activation: Incomplete | None = None, use_bias: bool = True, kernel_initializer: str = 'glorot_uniform', bias_initializer: str = 'zeros', kernel_regularizer: Incomplete | None = None, bias_regularizer: Incomplete | None = None, activity_regularizer: Incomplete | None = None, kernel_constraint: Incomplete | None = None, bias_constraint: Incomplete | None = None, **kwargs) -> None: ...
    input_spec: Incomplete
    kernel: Incomplete
    bias: Incomplete
    built: bool
    def build(self, input_shape) -> None: ...
    def call(self, inputs): ...
    def compute_output_shape(self, input_shape): ...
    def get_config(self): ...

class Conv3DTranspose(Conv3D):
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
  e.g. `input_shape=(128, 128, 128, 3)` for a 128x128x128 volume with 3 channels
  if `data_format="channels_last"`.

  Args:
    filters: Integer, the dimensionality of the output space
      (i.e. the number of output filters in the convolution).
    kernel_size: An integer or tuple/list of 3 integers, specifying the
      depth, height and width of the 3D convolution window.
      Can be a single integer to specify the same value for
      all spatial dimensions.
    strides: An integer or tuple/list of 3 integers,
      specifying the strides of the convolution along the depth, height
        and width.
      Can be a single integer to specify the same value for
      all spatial dimensions.
      Specifying any stride value != 1 is incompatible with specifying
      any `dilation_rate` value != 1.
    padding: one of `"valid"` or `"same"` (case-insensitive).
      `"valid"` means no padding. `"same"` results in padding with zeros evenly
      to the left/right or up/down of the input such that output has the same
      height/width dimension as the input.
    output_padding: An integer or tuple/list of 3 integers,
      specifying the amount of padding along the depth, height, and
      width.
      Can be a single integer to specify the same value for all
      spatial dimensions.
      The amount of output padding along a given dimension must be
      lower than the stride along that same dimension.
      If set to `None` (default), the output shape is inferred.
    data_format: A string,
      one of `channels_last` (default) or `channels_first`.
      The ordering of the dimensions in the inputs.
      `channels_last` corresponds to inputs with shape
      `(batch_size, depth, height, width, channels)` while `channels_first`
      corresponds to inputs with shape
      `(batch_size, channels, depth, height, width)`.
      It defaults to the `image_data_format` value found in your
      Keras config file at `~/.keras/keras.json`.
      If you never set it, then it will be "channels_last".
    dilation_rate: an integer or tuple/list of 3 integers, specifying
      the dilation rate to use for dilated convolution.
      Can be a single integer to specify the same value for
      all spatial dimensions.
      Currently, specifying any `dilation_rate` value != 1 is
      incompatible with specifying any stride value != 1.
    activation: Activation function to use.
      If you don\'t specify anything, no activation is applied (
      see `keras.activations`).
    use_bias: Boolean, whether the layer uses a bias vector.
    kernel_initializer: Initializer for the `kernel` weights matrix (
      see `keras.initializers`). Defaults to \'glorot_uniform\'.
    bias_initializer: Initializer for the bias vector (
      see `keras.initializers`). Defaults to \'zeros\'.
    kernel_regularizer: Regularizer function applied to
      the `kernel` weights matrix (
      see `keras.regularizers`).
    bias_regularizer: Regularizer function applied to the bias vector (
      see `keras.regularizers`).
    activity_regularizer: Regularizer function applied to
      the output of the layer (its "activation") (
      see `keras.regularizers`).
    kernel_constraint: Constraint function applied to the kernel matrix (
      see `keras.constraints`).
    bias_constraint: Constraint function applied to the bias vector (
      see `keras.constraints`).

  Input shape:
    5D tensor with shape:
    `(batch_size, channels, depth, rows, cols)` if data_format=\'channels_first\'
    or 5D tensor with shape:
    `(batch_size, depth, rows, cols, channels)` if data_format=\'channels_last\'.

  Output shape:
    5D tensor with shape:
    `(batch_size, filters, new_depth, new_rows, new_cols)` if
      data_format=\'channels_first\'
    or 5D tensor with shape:
    `(batch_size, new_depth, new_rows, new_cols, filters)` if
      data_format=\'channels_last\'.
    `depth` and `rows` and `cols` values might have changed due to padding.
    If `output_padding` is specified::
    ```
    new_depth = ((depth - 1) * strides[0] + kernel_size[0] - 2 * padding[0] +
    output_padding[0])
    new_rows = ((rows - 1) * strides[1] + kernel_size[1] - 2 * padding[1] +
    output_padding[1])
    new_cols = ((cols - 1) * strides[2] + kernel_size[2] - 2 * padding[2] +
    output_padding[2])
    ```

  Returns:
    A tensor of rank 5 representing
    `activation(conv3dtranspose(inputs, kernel) + bias)`.

  Raises:
    ValueError: if `padding` is "causal".
    ValueError: when both `strides` > 1 and `dilation_rate` > 1.

  References:
    - [A guide to convolution arithmetic for deep
      learning](https://arxiv.org/abs/1603.07285v1)
    - [Deconvolutional
      Networks](https://www.matthewzeiler.com/mattzeiler/deconvolutionalnetworks.pdf)
  '''
    output_padding: Incomplete
    def __init__(self, filters, kernel_size, strides=(1, 1, 1), padding: str = 'valid', output_padding: Incomplete | None = None, data_format: Incomplete | None = None, dilation_rate=(1, 1, 1), activation: Incomplete | None = None, use_bias: bool = True, kernel_initializer: str = 'glorot_uniform', bias_initializer: str = 'zeros', kernel_regularizer: Incomplete | None = None, bias_regularizer: Incomplete | None = None, activity_regularizer: Incomplete | None = None, kernel_constraint: Incomplete | None = None, bias_constraint: Incomplete | None = None, **kwargs) -> None: ...
    input_spec: Incomplete
    kernel: Incomplete
    bias: Incomplete
    built: bool
    def build(self, input_shape) -> None: ...
    def call(self, inputs): ...
    def compute_output_shape(self, input_shape): ...
    def get_config(self): ...

class SeparableConv(Conv):
    '''Abstract base layer for separable nD convolution.

  This layer performs a depthwise convolution that acts separately on
  channels, followed by a pointwise convolution that mixes channels.
  If `use_bias` is True and a bias initializer is provided,
  it adds a bias vector to the output.
  It then optionally applies an activation function to produce the final output.

  Args:
    rank: An integer, the rank of the convolution, e.g. "2" for 2D convolution.
    filters: Integer, the dimensionality of the output space (i.e. the number
      of filters in the convolution).
    kernel_size: A tuple or list of integers specifying the spatial
      dimensions of the filters. Can be a single integer to specify the same
      value for all spatial dimensions.
    strides: A tuple or list of integers specifying the strides
      of the convolution. Can be a single integer to specify the same value for
      all spatial dimensions.
      Specifying any `stride` value != 1 is incompatible with specifying
      any `dilation_rate` value != 1.
    padding: One of `"valid"` or `"same"` (case-insensitive).
      `"valid"` means no padding. `"same"` results in padding with zeros evenly
      to the left/right or up/down of the input such that output has the same
      height/width dimension as the input.
    data_format: A string, one of `channels_last` (default) or `channels_first`.
      The ordering of the dimensions in the inputs.
      `channels_last` corresponds to inputs with shape
      `(batch_size, ..., channels)` while `channels_first` corresponds to
      inputs with shape `(batch_size, channels, ...)`.
    dilation_rate: An integer or tuple/list of 2 integers, specifying
      the dilation rate to use for dilated convolution.
      Can be a single integer to specify the same value for
      all spatial dimensions.
      Currently, specifying any `dilation_rate` value != 1 is
      incompatible with specifying any stride value != 1.
    depth_multiplier: The number of depthwise convolution output channels for
      each input channel. The total number of depthwise convolution output
      channels will be equal to `num_filters_in * depth_multiplier`.
    activation: Activation function to use.
      If you don\'t specify anything, no activation is applied (
      see `keras.activations`).
    use_bias: Boolean, whether the layer uses a bias.
    depthwise_initializer: An initializer for the depthwise convolution kernel (
      see `keras.initializers`). If None, then the default initializer (
      \'glorot_uniform\') will be used.
    pointwise_initializer: An initializer for the pointwise convolution kernel (
      see `keras.initializers`). If None, then the default initializer 
      (\'glorot_uniform\') will be used.
    bias_initializer: An initializer for the bias vector. If None, the default
      initializer (\'zeros\') will be used (see `keras.initializers`).
    depthwise_regularizer: Optional regularizer for the depthwise
      convolution kernel.
    pointwise_regularizer: Optional regularizer for the pointwise
      convolution kernel.
    bias_regularizer: Optional regularizer for the bias vector.
    activity_regularizer: Optional regularizer function for the output.
    depthwise_constraint: Optional projection function to be applied to the
      depthwise kernel after being updated by an `Optimizer` (e.g. used for
      norm constraints or value constraints for layer weights). The function
      must take as input the unprojected variable and must return the
      projected variable (which must have the same shape). Constraints are
      not safe to use when doing asynchronous distributed training.
    pointwise_constraint: Optional projection function to be applied to the
      pointwise kernel after being updated by an `Optimizer`.
    bias_constraint: Optional projection function to be applied to the
      bias after being updated by an `Optimizer`.
    trainable: Boolean, if `True` the weights of this layer will be marked as
      trainable (and listed in `layer.trainable_weights`).
  '''
    depth_multiplier: Incomplete
    depthwise_initializer: Incomplete
    pointwise_initializer: Incomplete
    depthwise_regularizer: Incomplete
    pointwise_regularizer: Incomplete
    depthwise_constraint: Incomplete
    pointwise_constraint: Incomplete
    def __init__(self, rank, filters, kernel_size, strides: int = 1, padding: str = 'valid', data_format: Incomplete | None = None, dilation_rate: int = 1, depth_multiplier: int = 1, activation: Incomplete | None = None, use_bias: bool = True, depthwise_initializer: str = 'glorot_uniform', pointwise_initializer: str = 'glorot_uniform', bias_initializer: str = 'zeros', depthwise_regularizer: Incomplete | None = None, pointwise_regularizer: Incomplete | None = None, bias_regularizer: Incomplete | None = None, activity_regularizer: Incomplete | None = None, depthwise_constraint: Incomplete | None = None, pointwise_constraint: Incomplete | None = None, bias_constraint: Incomplete | None = None, trainable: bool = True, name: Incomplete | None = None, **kwargs) -> None: ...
    input_spec: Incomplete
    depthwise_kernel: Incomplete
    pointwise_kernel: Incomplete
    bias: Incomplete
    built: bool
    def build(self, input_shape) -> None: ...
    def call(self, inputs) -> None: ...
    def get_config(self): ...

class SeparableConv1D(SeparableConv):
    '''Depthwise separable 1D convolution.

  This layer performs a depthwise convolution that acts separately on
  channels, followed by a pointwise convolution that mixes channels.
  If `use_bias` is True and a bias initializer is provided,
  it adds a bias vector to the output.
  It then optionally applies an activation function to produce the final output.

  Args:
    filters: Integer, the dimensionality of the output space (i.e. the number
      of filters in the convolution).
    kernel_size: A single integer specifying the spatial
      dimensions of the filters.
    strides: A single integer specifying the strides
      of the convolution.
      Specifying any `stride` value != 1 is incompatible with specifying
      any `dilation_rate` value != 1.
    padding: One of `"valid"`, `"same"`, or `"causal"` (case-insensitive).
      `"valid"` means no padding. `"same"` results in padding with zeros evenly
      to the left/right or up/down of the input such that output has the same
      height/width dimension as the input. `"causal"` results in causal
      (dilated) convolutions, e.g. `output[t]` does not depend on `input[t+1:]`.
    data_format: A string, one of `channels_last` (default) or `channels_first`.
      The ordering of the dimensions in the inputs.
      `channels_last` corresponds to inputs with shape
      `(batch_size, length, channels)` while `channels_first` corresponds to
      inputs with shape `(batch_size, channels, length)`.
    dilation_rate: A single integer, specifying
      the dilation rate to use for dilated convolution.
      Currently, specifying any `dilation_rate` value != 1 is
      incompatible with specifying any stride value != 1.
    depth_multiplier: The number of depthwise convolution output channels for
      each input channel. The total number of depthwise convolution output
      channels will be equal to `num_filters_in * depth_multiplier`.
    activation: Activation function to use.
      If you don\'t specify anything, no activation is applied (
      see `keras.activations`).
    use_bias: Boolean, whether the layer uses a bias.
    depthwise_initializer: An initializer for the depthwise convolution kernel (
      see `keras.initializers`). If None, then the default initializer (
      \'glorot_uniform\') will be used.
    pointwise_initializer: An initializer for the pointwise convolution kernel (
      see `keras.initializers`). If None, then the default initializer 
      (\'glorot_uniform\') will be used.
    bias_initializer: An initializer for the bias vector. If None, the default
      initializer (\'zeros\') will be used (see `keras.initializers`).
    depthwise_regularizer: Optional regularizer for the depthwise
      convolution kernel (see `keras.regularizers`).
    pointwise_regularizer: Optional regularizer for the pointwise
      convolution kernel (see `keras.regularizers`).
    bias_regularizer: Optional regularizer for the bias vector (
      see `keras.regularizers`).
    activity_regularizer: Optional regularizer function for the output (
      see `keras.regularizers`).
    depthwise_constraint: Optional projection function to be applied to the
      depthwise kernel after being updated by an `Optimizer` (e.g. used for
      norm constraints or value constraints for layer weights). The function
      must take as input the unprojected variable and must return the
      projected variable (which must have the same shape). Constraints are
      not safe to use when doing asynchronous distributed training (
      see `keras.constraints`).
    pointwise_constraint: Optional projection function to be applied to the
      pointwise kernel after being updated by an `Optimizer` (
      see `keras.constraints`).
    bias_constraint: Optional projection function to be applied to the
      bias after being updated by an `Optimizer` (
      see `keras.constraints`).
    trainable: Boolean, if `True` the weights of this layer will be marked as
      trainable (and listed in `layer.trainable_weights`).

  Input shape:
    3D tensor with shape:
    `(batch_size, channels, steps)` if data_format=\'channels_first\'
    or 5D tensor with shape:
    `(batch_size, steps, channels)` if data_format=\'channels_last\'.

  Output shape:
    3D tensor with shape:
    `(batch_size, filters, new_steps)` if data_format=\'channels_first\'
    or 3D tensor with shape:
    `(batch_size,  new_steps, filters)` if data_format=\'channels_last\'.
    `new_steps` value might have changed due to padding or strides.

  Returns:
    A tensor of rank 3 representing
    `activation(separableconv1d(inputs, kernel) + bias)`.

  Raises:
    ValueError: when both `strides` > 1 and `dilation_rate` > 1.
  '''
    def __init__(self, filters, kernel_size, strides: int = 1, padding: str = 'valid', data_format: Incomplete | None = None, dilation_rate: int = 1, depth_multiplier: int = 1, activation: Incomplete | None = None, use_bias: bool = True, depthwise_initializer: str = 'glorot_uniform', pointwise_initializer: str = 'glorot_uniform', bias_initializer: str = 'zeros', depthwise_regularizer: Incomplete | None = None, pointwise_regularizer: Incomplete | None = None, bias_regularizer: Incomplete | None = None, activity_regularizer: Incomplete | None = None, depthwise_constraint: Incomplete | None = None, pointwise_constraint: Incomplete | None = None, bias_constraint: Incomplete | None = None, **kwargs) -> None: ...
    def call(self, inputs): ...

class SeparableConv2D(SeparableConv):
    '''Depthwise separable 2D convolution.

  Separable convolutions consist of first performing
  a depthwise spatial convolution
  (which acts on each input channel separately)
  followed by a pointwise convolution which mixes the resulting
  output channels. The `depth_multiplier` argument controls how many
  output channels are generated per input channel in the depthwise step.

  Intuitively, separable convolutions can be understood as
  a way to factorize a convolution kernel into two smaller kernels,
  or as an extreme version of an Inception block.

  Args:
    filters: Integer, the dimensionality of the output space
      (i.e. the number of output filters in the convolution).
    kernel_size: An integer or tuple/list of 2 integers, specifying the
      height and width of the 2D convolution window.
      Can be a single integer to specify the same value for
      all spatial dimensions.
    strides: An integer or tuple/list of 2 integers,
      specifying the strides of the convolution along the height and width.
      Can be a single integer to specify the same value for
      all spatial dimensions. Current implementation only supports equal 
      length strides in the row and column dimensions.
      Specifying any stride value != 1 is incompatible with specifying
      any `dilation_rate` value != 1.
    padding: one of `"valid"` or `"same"` (case-insensitive).
      `"valid"` means no padding. `"same"` results in padding with zeros evenly
      to the left/right or up/down of the input such that output has the same
      height/width dimension as the input.
    data_format: A string,
      one of `channels_last` (default) or `channels_first`.
      The ordering of the dimensions in the inputs.
      `channels_last` corresponds to inputs with shape
      `(batch_size, height, width, channels)` while `channels_first`
      corresponds to inputs with shape
      `(batch_size, channels, height, width)`.
      It defaults to the `image_data_format` value found in your
      Keras config file at `~/.keras/keras.json`.
      If you never set it, then it will be "channels_last".
    dilation_rate: An integer or tuple/list of 2 integers, specifying
      the dilation rate to use for dilated convolution.
      Currently, specifying any `dilation_rate` value != 1 is
      incompatible with specifying any `strides` value != 1.
    depth_multiplier: The number of depthwise convolution output channels
      for each input channel.
      The total number of depthwise convolution output
      channels will be equal to `filters_in * depth_multiplier`.
    activation: Activation function to use.
      If you don\'t specify anything, no activation is applied (
      see `keras.activations`).
    use_bias: Boolean, whether the layer uses a bias vector.
    depthwise_initializer: An initializer for the depthwise convolution kernel (
      see `keras.initializers`). If None, then the default initializer (
      \'glorot_uniform\') will be used.
    pointwise_initializer: An initializer for the pointwise convolution kernel (
      see `keras.initializers`). If None, then the default initializer 
      (\'glorot_uniform\') will be used.
    bias_initializer: An initializer for the bias vector. If None, the default
      initializer (\'zeros\') will be used (see `keras.initializers`).
    depthwise_regularizer: Regularizer function applied to
      the depthwise kernel matrix (see `keras.regularizers`).
    pointwise_regularizer: Regularizer function applied to
      the pointwise kernel matrix (see `keras.regularizers`).
    bias_regularizer: Regularizer function applied to the bias vector (
      see `keras.regularizers`).
    activity_regularizer: Regularizer function applied to
      the output of the layer (its "activation") (
      see `keras.regularizers`).
    depthwise_constraint: Constraint function applied to
      the depthwise kernel matrix (
      see `keras.constraints`).
    pointwise_constraint: Constraint function applied to
      the pointwise kernel matrix (
      see `keras.constraints`).
    bias_constraint: Constraint function applied to the bias vector (
      see `keras.constraints`).

  Input shape:
    4D tensor with shape:
    `(batch_size, channels, rows, cols)` if data_format=\'channels_first\'
    or 4D tensor with shape:
    `(batch_size, rows, cols, channels)` if data_format=\'channels_last\'.

  Output shape:
    4D tensor with shape:
    `(batch_size, filters, new_rows, new_cols)` if data_format=\'channels_first\'
    or 4D tensor with shape:
    `(batch_size, new_rows, new_cols, filters)` if data_format=\'channels_last\'.
    `rows` and `cols` values might have changed due to padding.

  Returns:
    A tensor of rank 4 representing
    `activation(separableconv2d(inputs, kernel) + bias)`.

  Raises:
    ValueError: if `padding` is "causal".
    ValueError: when both `strides` > 1 and `dilation_rate` > 1.
  '''
    def __init__(self, filters, kernel_size, strides=(1, 1), padding: str = 'valid', data_format: Incomplete | None = None, dilation_rate=(1, 1), depth_multiplier: int = 1, activation: Incomplete | None = None, use_bias: bool = True, depthwise_initializer: str = 'glorot_uniform', pointwise_initializer: str = 'glorot_uniform', bias_initializer: str = 'zeros', depthwise_regularizer: Incomplete | None = None, pointwise_regularizer: Incomplete | None = None, bias_regularizer: Incomplete | None = None, activity_regularizer: Incomplete | None = None, depthwise_constraint: Incomplete | None = None, pointwise_constraint: Incomplete | None = None, bias_constraint: Incomplete | None = None, **kwargs) -> None: ...
    def call(self, inputs): ...

class DepthwiseConv2D(Conv2D):
    '''Depthwise 2D convolution.

  Depthwise convolution is a type of convolution in which a single convolutional
  filter is apply to each input channel (i.e. in a depthwise way).
  You can understand depthwise convolution as being
  the first step in a depthwise separable convolution.

  It is implemented via the following steps:

  - Split the input into individual channels.
  - Convolve each input with the layer\'s kernel (called a depthwise kernel).
  - Stack the convolved outputs together (along the channels axis).

  Unlike a regular 2D convolution, depthwise convolution does not mix
  information across different input channels.

  The `depth_multiplier` argument controls how many
  output channels are generated per input channel in the depthwise step.

  Args:
    kernel_size: An integer or tuple/list of 2 integers, specifying the
      height and width of the 2D convolution window.
      Can be a single integer to specify the same value for
      all spatial dimensions.
    strides: An integer or tuple/list of 2 integers,
      specifying the strides of the convolution along the height and width.
      Can be a single integer to specify the same value for
      all spatial dimensions.
      Specifying any stride value != 1 is incompatible with specifying
      any `dilation_rate` value != 1.
    padding: one of `\'valid\'` or `\'same\'` (case-insensitive).
      `"valid"` means no padding. `"same"` results in padding with zeros evenly
      to the left/right or up/down of the input such that output has the same
      height/width dimension as the input.
    depth_multiplier: The number of depthwise convolution output channels
      for each input channel.
      The total number of depthwise convolution output
      channels will be equal to `filters_in * depth_multiplier`.
    data_format: A string,
      one of `channels_last` (default) or `channels_first`.
      The ordering of the dimensions in the inputs.
      `channels_last` corresponds to inputs with shape
      `(batch_size, height, width, channels)` while `channels_first`
      corresponds to inputs with shape
      `(batch_size, channels, height, width)`.
      It defaults to the `image_data_format` value found in your
      Keras config file at `~/.keras/keras.json`.
      If you never set it, then it will be \'channels_last\'.
    dilation_rate: An integer or tuple/list of 2 integers, specifying
      the dilation rate to use for dilated convolution.
      Currently, specifying any `dilation_rate` value != 1 is
      incompatible with specifying any `strides` value != 1.
    activation: Activation function to use.
      If you don\'t specify anything, no activation is applied (
      see `keras.activations`).
    use_bias: Boolean, whether the layer uses a bias vector.
    depthwise_initializer: Initializer for the depthwise kernel matrix (
      see `keras.initializers`). If None, the default initializer (
      \'glorot_uniform\') will be used.
    bias_initializer: Initializer for the bias vector (
      see `keras.initializers`). If None, the default initializer (
      \'zeros\') will bs used.
    depthwise_regularizer: Regularizer function applied to
      the depthwise kernel matrix (see `keras.regularizers`).
    bias_regularizer: Regularizer function applied to the bias vector (
      see `keras.regularizers`).
    activity_regularizer: Regularizer function applied to
      the output of the layer (its \'activation\') (
      see `keras.regularizers`).
    depthwise_constraint: Constraint function applied to
      the depthwise kernel matrix (
      see `keras.constraints`).
    bias_constraint: Constraint function applied to the bias vector (
      see `keras.constraints`).

  Input shape:
    4D tensor with shape:
    `[batch_size, channels, rows, cols]` if data_format=\'channels_first\'
    or 4D tensor with shape:
    `[batch_size, rows, cols, channels]` if data_format=\'channels_last\'.

  Output shape:
    4D tensor with shape:
    `[batch_size, channels * depth_multiplier, new_rows, new_cols]` if
    data_format=\'channels_first\' or 4D tensor with shape:
    `[batch_size, new_rows, new_cols, channels * depth_multiplier]` if
    data_format=\'channels_last\'. `rows` and `cols` values might have
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
    def __init__(self, kernel_size, strides=(1, 1), padding: str = 'valid', depth_multiplier: int = 1, data_format: Incomplete | None = None, dilation_rate=(1, 1), activation: Incomplete | None = None, use_bias: bool = True, depthwise_initializer: str = 'glorot_uniform', bias_initializer: str = 'zeros', depthwise_regularizer: Incomplete | None = None, bias_regularizer: Incomplete | None = None, activity_regularizer: Incomplete | None = None, depthwise_constraint: Incomplete | None = None, bias_constraint: Incomplete | None = None, **kwargs) -> None: ...
    depthwise_kernel: Incomplete
    bias: Incomplete
    input_spec: Incomplete
    built: bool
    def build(self, input_shape) -> None: ...
    def call(self, inputs): ...
    def compute_output_shape(self, input_shape): ...
    def get_config(self): ...

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

class UpSampling2D(Layer):
    '''Upsampling layer for 2D inputs.

  Repeats the rows and columns of the data
  by `size[0]` and `size[1]` respectively.

  Examples:

  >>> input_shape = (2, 2, 1, 3)
  >>> x = np.arange(np.prod(input_shape)).reshape(input_shape)
  >>> print(x)
  [[[[ 0  1  2]]
    [[ 3  4  5]]]
   [[[ 6  7  8]]
    [[ 9 10 11]]]]
  >>> y = tf.keras.layers.UpSampling2D(size=(1, 2))(x)
  >>> print(y)
  tf.Tensor(
    [[[[ 0  1  2]
       [ 0  1  2]]
      [[ 3  4  5]
       [ 3  4  5]]]
     [[[ 6  7  8]
       [ 6  7  8]]
      [[ 9 10 11]
       [ 9 10 11]]]], shape=(2, 2, 2, 3), dtype=int64)

  Args:
    size: Int, or tuple of 2 integers.
      The upsampling factors for rows and columns.
    data_format: A string,
      one of `channels_last` (default) or `channels_first`.
      The ordering of the dimensions in the inputs.
      `channels_last` corresponds to inputs with shape
      `(batch_size, height, width, channels)` while `channels_first`
      corresponds to inputs with shape
      `(batch_size, channels, height, width)`.
      It defaults to the `image_data_format` value found in your
      Keras config file at `~/.keras/keras.json`.
      If you never set it, then it will be "channels_last".
    interpolation: A string, one of `nearest` or `bilinear`.

  Input shape:
    4D tensor with shape:
    - If `data_format` is `"channels_last"`:
        `(batch_size, rows, cols, channels)`
    - If `data_format` is `"channels_first"`:
        `(batch_size, channels, rows, cols)`

  Output shape:
    4D tensor with shape:
    - If `data_format` is `"channels_last"`:
        `(batch_size, upsampled_rows, upsampled_cols, channels)`
    - If `data_format` is `"channels_first"`:
        `(batch_size, channels, upsampled_rows, upsampled_cols)`
  '''
    data_format: Incomplete
    size: Incomplete
    interpolation: Incomplete
    input_spec: Incomplete
    def __init__(self, size=(2, 2), data_format: Incomplete | None = None, interpolation: str = 'nearest', **kwargs) -> None: ...
    def compute_output_shape(self, input_shape): ...
    def call(self, inputs): ...
    def get_config(self): ...

class UpSampling3D(Layer):
    '''Upsampling layer for 3D inputs.

  Repeats the 1st, 2nd and 3rd dimensions
  of the data by `size[0]`, `size[1]` and `size[2]` respectively.

  Examples:

  >>> input_shape = (2, 1, 2, 1, 3)
  >>> x = tf.constant(1, shape=input_shape)
  >>> y = tf.keras.layers.UpSampling3D(size=2)(x)
  >>> print(y.shape)
  (2, 2, 4, 2, 3)

  Args:
    size: Int, or tuple of 3 integers.
      The upsampling factors for dim1, dim2 and dim3.
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
        `(batch_size, dim1, dim2, dim3, channels)`
    - If `data_format` is `"channels_first"`:
        `(batch_size, channels, dim1, dim2, dim3)`

  Output shape:
    5D tensor with shape:
    - If `data_format` is `"channels_last"`:
        `(batch_size, upsampled_dim1, upsampled_dim2, upsampled_dim3, channels)`
    - If `data_format` is `"channels_first"`:
        `(batch_size, channels, upsampled_dim1, upsampled_dim2, upsampled_dim3)`
  '''
    data_format: Incomplete
    size: Incomplete
    input_spec: Incomplete
    def __init__(self, size=(2, 2, 2), data_format: Incomplete | None = None, **kwargs) -> None: ...
    def compute_output_shape(self, input_shape): ...
    def call(self, inputs): ...
    def get_config(self): ...

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

class ZeroPadding2D(Layer):
    '''Zero-padding layer for 2D input (e.g. picture).

  This layer can add rows and columns of zeros
  at the top, bottom, left and right side of an image tensor.

  Examples:

  >>> input_shape = (1, 1, 2, 2)
  >>> x = np.arange(np.prod(input_shape)).reshape(input_shape)
  >>> print(x)
  [[[[0 1]
     [2 3]]]]
  >>> y = tf.keras.layers.ZeroPadding2D(padding=1)(x)
  >>> print(y)
  tf.Tensor(
    [[[[0 0]
       [0 0]
       [0 0]
       [0 0]]
      [[0 0]
       [0 1]
       [2 3]
       [0 0]]
      [[0 0]
       [0 0]
       [0 0]
       [0 0]]]], shape=(1, 3, 4, 2), dtype=int64)

  Args:
    padding: Int, or tuple of 2 ints, or tuple of 2 tuples of 2 ints.
      - If int: the same symmetric padding
        is applied to height and width.
      - If tuple of 2 ints:
        interpreted as two different
        symmetric padding values for height and width:
        `(symmetric_height_pad, symmetric_width_pad)`.
      - If tuple of 2 tuples of 2 ints:
        interpreted as
        `((top_pad, bottom_pad), (left_pad, right_pad))`
    data_format: A string,
      one of `channels_last` (default) or `channels_first`.
      The ordering of the dimensions in the inputs.
      `channels_last` corresponds to inputs with shape
      `(batch_size, height, width, channels)` while `channels_first`
      corresponds to inputs with shape
      `(batch_size, channels, height, width)`.
      It defaults to the `image_data_format` value found in your
      Keras config file at `~/.keras/keras.json`.
      If you never set it, then it will be "channels_last".

  Input shape:
    4D tensor with shape:
    - If `data_format` is `"channels_last"`:
        `(batch_size, rows, cols, channels)`
    - If `data_format` is `"channels_first"`:
        `(batch_size, channels, rows, cols)`

  Output shape:
    4D tensor with shape:
    - If `data_format` is `"channels_last"`:
        `(batch_size, padded_rows, padded_cols, channels)`
    - If `data_format` is `"channels_first"`:
        `(batch_size, channels, padded_rows, padded_cols)`
  '''
    data_format: Incomplete
    padding: Incomplete
    input_spec: Incomplete
    def __init__(self, padding=(1, 1), data_format: Incomplete | None = None, **kwargs) -> None: ...
    def compute_output_shape(self, input_shape): ...
    def call(self, inputs): ...
    def get_config(self): ...

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
        `(batch_size, first_axis_to_pad, second_axis_to_pad, third_axis_to_pad,
          depth)`
    - If `data_format` is `"channels_first"`:
        `(batch_size, depth, first_axis_to_pad, second_axis_to_pad,
          third_axis_to_pad)`

  Output shape:
    5D tensor with shape:
    - If `data_format` is `"channels_last"`:
        `(batch_size, first_padded_axis, second_padded_axis, third_axis_to_pad,
          depth)`
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

class Cropping2D(Layer):
    '''Cropping layer for 2D input (e.g. picture).

  It crops along spatial dimensions, i.e. height and width.

  Examples:

  >>> input_shape = (2, 28, 28, 3)
  >>> x = np.arange(np.prod(input_shape)).reshape(input_shape)
  >>> y = tf.keras.layers.Cropping2D(cropping=((2, 2), (4, 4)))(x)
  >>> print(y.shape)
  (2, 24, 20, 3)

  Args:
    cropping: Int, or tuple of 2 ints, or tuple of 2 tuples of 2 ints.
      - If int: the same symmetric cropping
        is applied to height and width.
      - If tuple of 2 ints:
        interpreted as two different
        symmetric cropping values for height and width:
        `(symmetric_height_crop, symmetric_width_crop)`.
      - If tuple of 2 tuples of 2 ints:
        interpreted as
        `((top_crop, bottom_crop), (left_crop, right_crop))`
    data_format: A string,
      one of `channels_last` (default) or `channels_first`.
      The ordering of the dimensions in the inputs.
      `channels_last` corresponds to inputs with shape
      `(batch_size, height, width, channels)` while `channels_first`
      corresponds to inputs with shape
      `(batch_size, channels, height, width)`.
      It defaults to the `image_data_format` value found in your
      Keras config file at `~/.keras/keras.json`.
      If you never set it, then it will be "channels_last".

  Input shape:
    4D tensor with shape:
    - If `data_format` is `"channels_last"`:
      `(batch_size, rows, cols, channels)`
    - If `data_format` is `"channels_first"`:
      `(batch_size, channels, rows, cols)`

  Output shape:
    4D tensor with shape:
    - If `data_format` is `"channels_last"`:
      `(batch_size, cropped_rows, cropped_cols, channels)`
    - If `data_format` is `"channels_first"`:
      `(batch_size, channels, cropped_rows, cropped_cols)`
  '''
    data_format: Incomplete
    cropping: Incomplete
    input_spec: Incomplete
    def __init__(self, cropping=((0, 0), (0, 0)), data_format: Incomplete | None = None, **kwargs) -> None: ...
    def compute_output_shape(self, input_shape): ...
    def call(self, inputs): ...
    def get_config(self): ...

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
      `(batch_size, first_axis_to_crop, second_axis_to_crop, third_axis_to_crop,
        depth)`
    - If `data_format` is `"channels_first"`:
      `(batch_size, depth, first_axis_to_crop, second_axis_to_crop,
        third_axis_to_crop)`

  Output shape:
    5D tensor with shape:
    - If `data_format` is `"channels_last"`:
      `(batch_size, first_cropped_axis, second_cropped_axis, third_cropped_axis,
        depth)`
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
Convolution1D = Conv1D
Convolution2D = Conv2D
Convolution3D = Conv3D
SeparableConvolution1D = SeparableConv1D
SeparableConvolution2D = SeparableConv2D
Convolution2DTranspose = Conv2DTranspose
Convolution3DTranspose = Conv3DTranspose
Deconvolution2D = Conv2DTranspose
Deconv2D = Conv2DTranspose
Deconvolution3D = Conv3DTranspose
Deconv3D = Conv3DTranspose
