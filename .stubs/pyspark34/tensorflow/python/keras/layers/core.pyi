from _typeshed import Incomplete
from tensorflow.python.eager import backprop as backprop, context as context
from tensorflow.python.framework import constant_op as constant_op, dtypes as dtypes, ops as ops, sparse_tensor as sparse_tensor, tensor_shape as tensor_shape
from tensorflow.python.keras import activations as activations, constraints as constraints, initializers as initializers, regularizers as regularizers
from tensorflow.python.keras.engine import keras_tensor as keras_tensor
from tensorflow.python.keras.engine.base_layer import Layer as Layer
from tensorflow.python.keras.engine.input_spec import InputSpec as InputSpec
from tensorflow.python.keras.utils import control_flow_util as control_flow_util, conv_utils as conv_utils, generic_utils as generic_utils, tf_inspect as tf_inspect, tf_utils as tf_utils
from tensorflow.python.ops import array_ops as array_ops, embedding_ops as embedding_ops, gen_math_ops as gen_math_ops, math_ops as math_ops, nn as nn, nn_ops as nn_ops, sparse_ops as sparse_ops, standard_ops as standard_ops, variable_scope as variable_scope
from tensorflow.python.ops.ragged import ragged_getitem as ragged_getitem, ragged_tensor as ragged_tensor
from tensorflow.python.platform import tf_logging as tf_logging
from tensorflow.python.util import dispatch as dispatch, nest as nest, tf_decorator as tf_decorator
from tensorflow.python.util.tf_export import get_canonical_name_for_symbol as get_canonical_name_for_symbol, get_symbol_from_name as get_symbol_from_name, keras_export as keras_export

class Masking(Layer):
    """Masks a sequence by using a mask value to skip timesteps.

  For each timestep in the input tensor (dimension #1 in the tensor),
  if all values in the input tensor at that timestep
  are equal to `mask_value`, then the timestep will be masked (skipped)
  in all downstream layers (as long as they support masking).

  If any downstream layer does not support masking yet receives such
  an input mask, an exception will be raised.

  Example:

  Consider a Numpy data array `x` of shape `(samples, timesteps, features)`,
  to be fed to an LSTM layer. You want to mask timestep #3 and #5 because you
  lack data for these timesteps. You can:

  - Set `x[:, 3, :] = 0.` and `x[:, 5, :] = 0.`
  - Insert a `Masking` layer with `mask_value=0.` before the LSTM layer:

  ```python
  samples, timesteps, features = 32, 10, 8
  inputs = np.random.random([samples, timesteps, features]).astype(np.float32)
  inputs[:, 3, :] = 0.
  inputs[:, 5, :] = 0.

  model = tf.keras.models.Sequential()
  model.add(tf.keras.layers.Masking(mask_value=0.,
                                    input_shape=(timesteps, features)))
  model.add(tf.keras.layers.LSTM(32))

  output = model(inputs)
  # The time step 3 and 5 will be skipped from LSTM calculation.
  ```

  See [the masking and padding guide](
    https://www.tensorflow.org/guide/keras/masking_and_padding)
  for more details.
  """
    supports_masking: bool
    mask_value: Incomplete
    def __init__(self, mask_value: float = 0.0, **kwargs) -> None: ...
    def compute_mask(self, inputs, mask: Incomplete | None = None): ...
    def call(self, inputs): ...
    def compute_output_shape(self, input_shape): ...
    def get_config(self): ...

class Dropout(Layer):
    """Applies Dropout to the input.

  The Dropout layer randomly sets input units to 0 with a frequency of `rate`
  at each step during training time, which helps prevent overfitting.
  Inputs not set to 0 are scaled up by 1/(1 - rate) such that the sum over
  all inputs is unchanged.

  Note that the Dropout layer only applies when `training` is set to True
  such that no values are dropped during inference. When using `model.fit`,
  `training` will be appropriately set to True automatically, and in other
  contexts, you can set the kwarg explicitly to True when calling the layer.

  (This is in contrast to setting `trainable=False` for a Dropout layer.
  `trainable` does not affect the layer's behavior, as Dropout does
  not have any variables/weights that can be frozen during training.)

  >>> tf.random.set_seed(0)
  >>> layer = tf.keras.layers.Dropout(.2, input_shape=(2,))
  >>> data = np.arange(10).reshape(5, 2).astype(np.float32)
  >>> print(data)
  [[0. 1.]
   [2. 3.]
   [4. 5.]
   [6. 7.]
   [8. 9.]]
  >>> outputs = layer(data, training=True)
  >>> print(outputs)
  tf.Tensor(
  [[ 0.    1.25]
   [ 2.5   3.75]
   [ 5.    6.25]
   [ 7.5   8.75]
   [10.    0.  ]], shape=(5, 2), dtype=float32)

  Args:
    rate: Float between 0 and 1. Fraction of the input units to drop.
    noise_shape: 1D integer tensor representing the shape of the
      binary dropout mask that will be multiplied with the input.
      For instance, if your inputs have shape
      `(batch_size, timesteps, features)` and
      you want the dropout mask to be the same for all timesteps,
      you can use `noise_shape=(batch_size, 1, features)`.
    seed: A Python integer to use as random seed.

  Call arguments:
    inputs: Input tensor (of any rank).
    training: Python boolean indicating whether the layer should behave in
      training mode (adding dropout) or in inference mode (doing nothing).
  """
    rate: Incomplete
    noise_shape: Incomplete
    seed: Incomplete
    supports_masking: bool
    def __init__(self, rate, noise_shape: Incomplete | None = None, seed: Incomplete | None = None, **kwargs) -> None: ...
    def call(self, inputs, training: Incomplete | None = None): ...
    def compute_output_shape(self, input_shape): ...
    def get_config(self): ...

class SpatialDropout1D(Dropout):
    """Spatial 1D version of Dropout.

  This version performs the same function as Dropout, however, it drops
  entire 1D feature maps instead of individual elements. If adjacent frames
  within feature maps are strongly correlated (as is normally the case in
  early convolution layers) then regular dropout will not regularize the
  activations and will otherwise just result in an effective learning rate
  decrease. In this case, SpatialDropout1D will help promote independence
  between feature maps and should be used instead.

  Args:
    rate: Float between 0 and 1. Fraction of the input units to drop.

  Call arguments:
    inputs: A 3D tensor.
    training: Python boolean indicating whether the layer should behave in
      training mode (adding dropout) or in inference mode (doing nothing).

  Input shape:
    3D tensor with shape:
    `(samples, timesteps, channels)`

  Output shape:
    Same as input.

  References:
    - [Efficient Object Localization Using Convolutional
      Networks](https://arxiv.org/abs/1411.4280)
  """
    input_spec: Incomplete
    def __init__(self, rate, **kwargs) -> None: ...

class SpatialDropout2D(Dropout):
    '''Spatial 2D version of Dropout.

  This version performs the same function as Dropout, however, it drops
  entire 2D feature maps instead of individual elements. If adjacent pixels
  within feature maps are strongly correlated (as is normally the case in
  early convolution layers) then regular dropout will not regularize the
  activations and will otherwise just result in an effective learning rate
  decrease. In this case, SpatialDropout2D will help promote independence
  between feature maps and should be used instead.

  Args:
    rate: Float between 0 and 1. Fraction of the input units to drop.
    data_format: \'channels_first\' or \'channels_last\'.
      In \'channels_first\' mode, the channels dimension
      (the depth) is at index 1,
      in \'channels_last\' mode is it at index 3.
      It defaults to the `image_data_format` value found in your
      Keras config file at `~/.keras/keras.json`.
      If you never set it, then it will be "channels_last".

  Call arguments:
    inputs: A 4D tensor.
    training: Python boolean indicating whether the layer should behave in
      training mode (adding dropout) or in inference mode (doing nothing).

  Input shape:
    4D tensor with shape:
    `(samples, channels, rows, cols)` if data_format=\'channels_first\'
    or 4D tensor with shape:
    `(samples, rows, cols, channels)` if data_format=\'channels_last\'.

  Output shape:
    Same as input.

  References:
    - [Efficient Object Localization Using Convolutional
      Networks](https://arxiv.org/abs/1411.4280)
  '''
    data_format: Incomplete
    input_spec: Incomplete
    def __init__(self, rate, data_format: Incomplete | None = None, **kwargs) -> None: ...

class SpatialDropout3D(Dropout):
    '''Spatial 3D version of Dropout.

  This version performs the same function as Dropout, however, it drops
  entire 3D feature maps instead of individual elements. If adjacent voxels
  within feature maps are strongly correlated (as is normally the case in
  early convolution layers) then regular dropout will not regularize the
  activations and will otherwise just result in an effective learning rate
  decrease. In this case, SpatialDropout3D will help promote independence
  between feature maps and should be used instead.

  Args:
    rate: Float between 0 and 1. Fraction of the input units to drop.
    data_format: \'channels_first\' or \'channels_last\'.
        In \'channels_first\' mode, the channels dimension (the depth)
        is at index 1, in \'channels_last\' mode is it at index 4.
        It defaults to the `image_data_format` value found in your
        Keras config file at `~/.keras/keras.json`.
        If you never set it, then it will be "channels_last".

  Call arguments:
    inputs: A 5D tensor.
    training: Python boolean indicating whether the layer should behave in
      training mode (adding dropout) or in inference mode (doing nothing).

  Input shape:
    5D tensor with shape:
    `(samples, channels, dim1, dim2, dim3)` if data_format=\'channels_first\'
    or 5D tensor with shape:
    `(samples, dim1, dim2, dim3, channels)` if data_format=\'channels_last\'.

  Output shape:
    Same as input.

  References:
    - [Efficient Object Localization Using Convolutional
      Networks](https://arxiv.org/abs/1411.4280)
  '''
    data_format: Incomplete
    input_spec: Incomplete
    def __init__(self, rate, data_format: Incomplete | None = None, **kwargs) -> None: ...

class Activation(Layer):
    '''Applies an activation function to an output.

  Args:
    activation: Activation function, such as `tf.nn.relu`, or string name of
      built-in activation function, such as "relu".

  Usage:

  >>> layer = tf.keras.layers.Activation(\'relu\')
  >>> output = layer([-3.0, -1.0, 0.0, 2.0])
  >>> list(output.numpy())
  [0.0, 0.0, 0.0, 2.0]
  >>> layer = tf.keras.layers.Activation(tf.nn.relu)
  >>> output = layer([-3.0, -1.0, 0.0, 2.0])
  >>> list(output.numpy())
  [0.0, 0.0, 0.0, 2.0]

  Input shape:
    Arbitrary. Use the keyword argument `input_shape`
    (tuple of integers, does not include the batch axis)
    when using this layer as the first layer in a model.

  Output shape:
    Same shape as input.
  '''
    supports_masking: bool
    activation: Incomplete
    def __init__(self, activation, **kwargs) -> None: ...
    def call(self, inputs): ...
    def compute_output_shape(self, input_shape): ...
    def get_config(self): ...

class Reshape(Layer):
    """Layer that reshapes inputs into the given shape.

  Input shape:
    Arbitrary, although all dimensions in the input shape must be known/fixed.
    Use the keyword argument `input_shape` (tuple of integers, does not include
    the samples/batch size axis) when using this layer as the first layer
    in a model.

  Output shape:
    `(batch_size,) + target_shape`

  Example:

  >>> # as first layer in a Sequential model
  >>> model = tf.keras.Sequential()
  >>> model.add(tf.keras.layers.Reshape((3, 4), input_shape=(12,)))
  >>> # model.output_shape == (None, 3, 4), `None` is the batch size.
  >>> model.output_shape
  (None, 3, 4)

  >>> # as intermediate layer in a Sequential model
  >>> model.add(tf.keras.layers.Reshape((6, 2)))
  >>> model.output_shape
  (None, 6, 2)

  >>> # also supports shape inference using `-1` as dimension
  >>> model.add(tf.keras.layers.Reshape((-1, 2, 2)))
  >>> model.output_shape
  (None, 3, 2, 2)
  """
    target_shape: Incomplete
    def __init__(self, target_shape, **kwargs) -> None:
        """Creates a `tf.keras.layers.Reshape`  layer instance.

    Args:
      target_shape: Target shape. Tuple of integers, does not include the
        samples dimension (batch size).
      **kwargs: Any additional layer keyword arguments.
    """
    def compute_output_shape(self, input_shape): ...
    def call(self, inputs): ...
    def get_config(self): ...

class Permute(Layer):
    """Permutes the dimensions of the input according to a given pattern.

  Useful e.g. connecting RNNs and convnets.

  Example:

  ```python
  model = Sequential()
  model.add(Permute((2, 1), input_shape=(10, 64)))
  # now: model.output_shape == (None, 64, 10)
  # note: `None` is the batch dimension
  ```

  Args:
    dims: Tuple of integers. Permutation pattern does not include the
      samples dimension. Indexing starts at 1.
      For instance, `(2, 1)` permutes the first and second dimensions
      of the input.

  Input shape:
    Arbitrary. Use the keyword argument `input_shape`
    (tuple of integers, does not include the samples axis)
    when using this layer as the first layer in a model.

  Output shape:
    Same as the input shape, but with the dimensions re-ordered according
    to the specified pattern.
  """
    dims: Incomplete
    input_spec: Incomplete
    def __init__(self, dims, **kwargs) -> None: ...
    def compute_output_shape(self, input_shape): ...
    def call(self, inputs): ...
    def get_config(self): ...

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

class RepeatVector(Layer):
    """Repeats the input n times.

  Example:

  ```python
  model = Sequential()
  model.add(Dense(32, input_dim=32))
  # now: model.output_shape == (None, 32)
  # note: `None` is the batch dimension

  model.add(RepeatVector(3))
  # now: model.output_shape == (None, 3, 32)
  ```

  Args:
    n: Integer, repetition factor.

  Input shape:
    2D tensor of shape `(num_samples, features)`.

  Output shape:
    3D tensor of shape `(num_samples, n, features)`.
  """
    n: Incomplete
    input_spec: Incomplete
    def __init__(self, n, **kwargs) -> None: ...
    def compute_output_shape(self, input_shape): ...
    def call(self, inputs): ...
    def get_config(self): ...

class Lambda(Layer):
    """Wraps arbitrary expressions as a `Layer` object.

  The `Lambda` layer exists so that arbitrary expressions can be used
  as a `Layer` when constructing `Sequential`
  and Functional API models. `Lambda` layers are best suited for simple
  operations or quick experimentation. For more advanced use cases, follow
  [this guide](https://www.tensorflow.org/guide/keras/custom_layers_and_models)
  for subclassing `tf.keras.layers.Layer`.

  WARNING: `tf.keras.layers.Lambda` layers have (de)serialization limitations!

  The main reason to subclass `tf.keras.layers.Layer` instead of using a
  `Lambda` layer is saving and inspecting a Model. `Lambda` layers
  are saved by serializing the Python bytecode, which is fundamentally
  non-portable. They should only be loaded in the same environment where
  they were saved. Subclassed layers can be saved in a more portable way
  by overriding their `get_config` method. Models that rely on
  subclassed Layers are also often easier to visualize and reason about.

  Examples:

  ```python
  # add a x -> x^2 layer
  model.add(Lambda(lambda x: x ** 2))
  ```
  ```python
  # add a layer that returns the concatenation
  # of the positive part of the input and
  # the opposite of the negative part

  def antirectifier(x):
      x -= K.mean(x, axis=1, keepdims=True)
      x = K.l2_normalize(x, axis=1)
      pos = K.relu(x)
      neg = K.relu(-x)
      return K.concatenate([pos, neg], axis=1)

  model.add(Lambda(antirectifier))
  ```

  Variables:
    While it is possible to use Variables with Lambda layers, this practice is
    discouraged as it can easily lead to bugs. For instance, consider the
    following layer:

    ```python
      scale = tf.Variable(1.)
      scale_layer = tf.keras.layers.Lambda(lambda x: x * scale)
    ```

    Because scale_layer does not directly track the `scale` variable, it will
    not appear in `scale_layer.trainable_weights` and will therefore not be
    trained if `scale_layer` is used in a Model.

    A better pattern is to write a subclassed Layer:

    ```python
      class ScaleLayer(tf.keras.layers.Layer):
        def __init__(self):
          super(ScaleLayer, self).__init__()
          self.scale = tf.Variable(1.)

        def call(self, inputs):
          return inputs * self.scale
    ```

    In general, Lambda layers can be convenient for simple stateless
    computation, but anything more complex should use a subclass Layer instead.

  Args:
    function: The function to be evaluated. Takes input tensor as first
      argument.
    output_shape: Expected output shape from function. This argument can be
      inferred if not explicitly provided. Can be a tuple or function. If a
      tuple, it only specifies the first dimension onward;
      sample dimension is assumed either the same as the input: `output_shape =
        (input_shape[0], ) + output_shape` or, the input is `None` and
      the sample dimension is also `None`: `output_shape = (None, ) +
        output_shape` If a function, it specifies the entire shape as a function
        of the
      input shape: `output_shape = f(input_shape)`
    mask: Either None (indicating no masking) or a callable with the same
      signature as the `compute_mask` layer method, or a tensor that will be
      returned as output mask regardless of what the input is.
    arguments: Optional dictionary of keyword arguments to be passed to the
      function.

  Input shape:
    Arbitrary. Use the keyword argument input_shape (tuple of
    integers, does not include the samples axis) when using this layer as the
    first layer in a model.

  Output shape:
    Specified by `output_shape` argument
  """
    arguments: Incomplete
    function: Incomplete
    supports_masking: bool
    mask: Incomplete
    def __init__(self, function, output_shape: Incomplete | None = None, mask: Incomplete | None = None, arguments: Incomplete | None = None, **kwargs) -> None: ...
    def compute_output_shape(self, input_shape): ...
    def call(self, inputs, mask: Incomplete | None = None, training: Incomplete | None = None): ...
    def compute_mask(self, inputs, mask: Incomplete | None = None): ...
    def get_config(self): ...
    @classmethod
    def from_config(cls, config, custom_objects: Incomplete | None = None): ...

class Dense(Layer):
    '''Just your regular densely-connected NN layer.

  `Dense` implements the operation:
  `output = activation(dot(input, kernel) + bias)`
  where `activation` is the element-wise activation function
  passed as the `activation` argument, `kernel` is a weights matrix
  created by the layer, and `bias` is a bias vector created by the layer
  (only applicable if `use_bias` is `True`). These are all attributes of
  `Dense`.

  Note: If the input to the layer has a rank greater than 2, then `Dense`
  computes the dot product between the `inputs` and the `kernel` along the
  last axis of the `inputs` and axis 0 of the `kernel` (using `tf.tensordot`).
  For example, if input has dimensions `(batch_size, d0, d1)`,
  then we create a `kernel` with shape `(d1, units)`, and the `kernel` operates
  along axis 2 of the `input`, on every sub-tensor of shape `(1, 1, d1)`
  (there are `batch_size * d0` such sub-tensors).
  The output in this case will have shape `(batch_size, d0, units)`.

  Besides, layer attributes cannot be modified after the layer has been called
  once (except the `trainable` attribute).
  When a popular kwarg `input_shape` is passed, then keras will create
  an input layer to insert before the current layer. This can be treated
  equivalent to explicitly defining an `InputLayer`.

  Example:

  >>> # Create a `Sequential` model and add a Dense layer as the first layer.
  >>> model = tf.keras.models.Sequential()
  >>> model.add(tf.keras.Input(shape=(16,)))
  >>> model.add(tf.keras.layers.Dense(32, activation=\'relu\'))
  >>> # Now the model will take as input arrays of shape (None, 16)
  >>> # and output arrays of shape (None, 32).
  >>> # Note that after the first layer, you don\'t need to specify
  >>> # the size of the input anymore:
  >>> model.add(tf.keras.layers.Dense(32))
  >>> model.output_shape
  (None, 32)

  Args:
    units: Positive integer, dimensionality of the output space.
    activation: Activation function to use.
      If you don\'t specify anything, no activation is applied
      (ie. "linear" activation: `a(x) = x`).
    use_bias: Boolean, whether the layer uses a bias vector.
    kernel_initializer: Initializer for the `kernel` weights matrix.
    bias_initializer: Initializer for the bias vector.
    kernel_regularizer: Regularizer function applied to
      the `kernel` weights matrix.
    bias_regularizer: Regularizer function applied to the bias vector.
    activity_regularizer: Regularizer function applied to
      the output of the layer (its "activation").
    kernel_constraint: Constraint function applied to
      the `kernel` weights matrix.
    bias_constraint: Constraint function applied to the bias vector.

  Input shape:
    N-D tensor with shape: `(batch_size, ..., input_dim)`.
    The most common situation would be
    a 2D input with shape `(batch_size, input_dim)`.

  Output shape:
    N-D tensor with shape: `(batch_size, ..., units)`.
    For instance, for a 2D input with shape `(batch_size, input_dim)`,
    the output would have shape `(batch_size, units)`.
  '''
    units: Incomplete
    activation: Incomplete
    use_bias: Incomplete
    kernel_initializer: Incomplete
    bias_initializer: Incomplete
    kernel_regularizer: Incomplete
    bias_regularizer: Incomplete
    kernel_constraint: Incomplete
    bias_constraint: Incomplete
    input_spec: Incomplete
    supports_masking: bool
    def __init__(self, units, activation: Incomplete | None = None, use_bias: bool = True, kernel_initializer: str = 'glorot_uniform', bias_initializer: str = 'zeros', kernel_regularizer: Incomplete | None = None, bias_regularizer: Incomplete | None = None, activity_regularizer: Incomplete | None = None, kernel_constraint: Incomplete | None = None, bias_constraint: Incomplete | None = None, **kwargs) -> None: ...
    kernel: Incomplete
    bias: Incomplete
    built: bool
    def build(self, input_shape) -> None: ...
    def call(self, inputs): ...
    def compute_output_shape(self, input_shape): ...
    def get_config(self): ...

class ActivityRegularization(Layer):
    """Layer that applies an update to the cost function based input activity.

  Args:
    l1: L1 regularization factor (positive float).
    l2: L2 regularization factor (positive float).

  Input shape:
    Arbitrary. Use the keyword argument `input_shape`
    (tuple of integers, does not include the samples axis)
    when using this layer as the first layer in a model.

  Output shape:
    Same shape as input.
  """
    supports_masking: bool
    l1: Incomplete
    l2: Incomplete
    def __init__(self, l1: float = 0.0, l2: float = 0.0, **kwargs) -> None: ...
    def compute_output_shape(self, input_shape): ...
    def get_config(self): ...

class TFOpLambda(Layer):
    """Wraps TF API symbols in a `Layer` object.

  It is inserted by the Functional API construction whenever users call
  a supported TF symbol on KerasTensors.

  Like Lambda layers, this layer tries to raise warnings when it detects users
  explicitly use variables in the call. (To let them know
  that the layer will not capture the variables).

  This is useful in the case where users do something like:
  x = keras.Input(...)
  y = tf.Variable(...)
  out = x * tf_variable
  """
    function: Incomplete
    symbol: Incomplete
    call: Incomplete
    def __init__(self, function, **kwargs) -> None: ...
    def get_config(self): ...
    @classmethod
    def from_config(cls, config, custom_objects: Incomplete | None = None): ...

class KerasOpDispatcher(dispatch.GlobalOpDispatcher):
    """A global dispatcher that allows building a functional model with TF Ops."""
    def handle(self, op, args, kwargs):
        """Handle the specified operation with the specified arguments."""

class SlicingOpLambda(TFOpLambda):
    """Wraps TF API symbols in a `Layer` object.

  It is inserted by the Functional API construction whenever users call
  a supported TF symbol on KerasTensors.

  Like Lambda layers, this layer tries to raise warnings when it detects users
  explicitly use variables in the call. (To let them know
  that the layer will not capture the variables).

  This is useful in the case where users do something like:
  x = keras.Input(...)
  y = tf.Variable(...)
  out = x * tf_variable
  """
    call: Incomplete
    def __init__(self, function, **kwargs) -> None: ...

class TFSlicingOpDispatcher(dispatch.OpDispatcher):
    """A global dispatcher that allows building a functional model with TF Ops."""
    op: Incomplete
    def __init__(self, op) -> None: ...
    def handle(self, args, kwargs):
        """Handle the specified operation with the specified arguments."""

class InstanceProperty(Layer):
    """Wraps an instance property access (e.g. `x.foo`) in a Keras Layer.

  This layer takes an attribute name `attr_name` in the constructor and,
  when called on input tensor `obj` returns `obj.attr_name`.

  KerasTensors specialized for specific extension types use it to
  represent instance property accesses on the represented object in the
  case where the property needs to be dynamically accessed as opposed to
  being statically computed from the typespec, e.g.

  x = keras.Input(..., ragged=True)
  out = x.flat_values
  """
    attr_name: Incomplete
    def __init__(self, attr_name, **kwargs) -> None: ...
    def call(self, obj): ...
    def get_config(self): ...
    @classmethod
    def from_config(cls, config, custom_objects: Incomplete | None = None): ...

class InstanceMethod(InstanceProperty):
    """Wraps an instance method access (e.g. `x.foo(arg)` in a Keras Layer.

  This layer takes an attribute name `attr_name` in the constructor and,
  when called on input tensor `obj` with additional arguments `args` and
  `kwargs` returns `obj.attr_name(*args, **kwargs)`.

  KerasTensors specialized for specific extension types use it to
  represent dynamic instance method calls on the represented object, e.g.

  x = keras.Input(..., ragged=True)
  new_values = keras.Input(...)
  out = x.with_values(new_values)
  """
    def call(self, obj, args, kwargs): ...

class ClassMethod(Layer):
    """Wraps a TF API Class's class method  in a `Layer` object.

  It is inserted by the Functional API construction whenever users call
  a supported TF Class's class method on KerasTensors.

  This is useful in the case where users do something like:
  x = keras.Input(...)
  y = keras.Input(...)
  out = tf.RaggedTensor.from_row_splits(x, y)
  """
    cls_ref: Incomplete
    method_name: Incomplete
    cls_symbol: Incomplete
    def __init__(self, cls_ref, method_name, **kwargs) -> None: ...
    def call(self, args, kwargs): ...
    def get_config(self): ...
    @classmethod
    def from_config(cls, config, custom_objects: Incomplete | None = None): ...

class TFClassMethodDispatcher(dispatch.OpDispatcher):
    """A class method dispatcher that allows building a functional model with TF class methods."""
    cls: Incomplete
    method_name: Incomplete
    def __init__(self, cls, method_name) -> None: ...
    def handle(self, args, kwargs):
        """Handle the specified operation with the specified arguments."""
