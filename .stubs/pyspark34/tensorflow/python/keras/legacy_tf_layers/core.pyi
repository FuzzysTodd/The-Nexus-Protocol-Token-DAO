from _typeshed import Incomplete
from tensorflow.python.keras import layers as keras_layers
from tensorflow.python.keras.legacy_tf_layers import base as base
from tensorflow.python.ops import init_ops as init_ops
from tensorflow.python.util.tf_export import keras_export as keras_export, tf_export as tf_export

class Dense(keras_layers.Dense, base.Layer):
    """Densely-connected layer class.

  This layer implements the operation:
  `outputs = activation(inputs * kernel + bias)`
  Where `activation` is the activation function passed as the `activation`
  argument (if not `None`), `kernel` is a weights matrix created by the layer,
  and `bias` is a bias vector created by the layer
  (only if `use_bias` is `True`).

  Args:
    units: Integer or Long, dimensionality of the output space.
    activation: Activation function (callable). Set it to None to maintain a
      linear activation.
    use_bias: Boolean, whether the layer uses a bias.
    kernel_initializer: Initializer function for the weight matrix.
      If `None` (default), weights are initialized using the default
      initializer used by `tf.compat.v1.get_variable`.
    bias_initializer: Initializer function for the bias.
    kernel_regularizer: Regularizer function for the weight matrix.
    bias_regularizer: Regularizer function for the bias.
    activity_regularizer: Regularizer function for the output.
    kernel_constraint: An optional projection function to be applied to the
        kernel after being updated by an `Optimizer` (e.g. used to implement
        norm constraints or value constraints for layer weights). The function
        must take as input the unprojected variable and must return the
        projected variable (which must have the same shape). Constraints are
        not safe to use when doing asynchronous distributed training.
    bias_constraint: An optional projection function to be applied to the
        bias after being updated by an `Optimizer`.
    trainable: Boolean, if `True` also add variables to the graph collection
      `GraphKeys.TRAINABLE_VARIABLES` (see `tf.Variable`).
    name: String, the name of the layer. Layers with the same name will
      share weights, but to avoid mistakes we require reuse=True in such cases.
    _reuse: Boolean, whether to reuse the weights of a previous layer
      by the same name.

  Properties:
    units: Python integer, dimensionality of the output space.
    activation: Activation function (callable).
    use_bias: Boolean, whether the layer uses a bias.
    kernel_initializer: Initializer instance (or name) for the kernel matrix.
    bias_initializer: Initializer instance (or name) for the bias.
    kernel_regularizer: Regularizer instance for the kernel matrix (callable)
    bias_regularizer: Regularizer instance for the bias (callable).
    activity_regularizer: Regularizer instance for the output (callable)
    kernel_constraint: Constraint function for the kernel matrix.
    bias_constraint: Constraint function for the bias.
    kernel: Weight matrix (TensorFlow variable or tensor).
    bias: Bias vector, if applicable (TensorFlow variable or tensor).
  """
    def __init__(self, units, activation: Incomplete | None = None, use_bias: bool = True, kernel_initializer: Incomplete | None = None, bias_initializer=..., kernel_regularizer: Incomplete | None = None, bias_regularizer: Incomplete | None = None, activity_regularizer: Incomplete | None = None, kernel_constraint: Incomplete | None = None, bias_constraint: Incomplete | None = None, trainable: bool = True, name: Incomplete | None = None, **kwargs) -> None: ...

def dense(inputs, units, activation: Incomplete | None = None, use_bias: bool = True, kernel_initializer: Incomplete | None = None, bias_initializer=..., kernel_regularizer: Incomplete | None = None, bias_regularizer: Incomplete | None = None, activity_regularizer: Incomplete | None = None, kernel_constraint: Incomplete | None = None, bias_constraint: Incomplete | None = None, trainable: bool = True, name: Incomplete | None = None, reuse: Incomplete | None = None):
    """Functional interface for the densely-connected layer.

  This layer implements the operation:
  `outputs = activation(inputs * kernel + bias)`
  where `activation` is the activation function passed as the `activation`
  argument (if not `None`), `kernel` is a weights matrix created by the layer,
  and `bias` is a bias vector created by the layer
  (only if `use_bias` is `True`).

  Args:
    inputs: Tensor input.
    units: Integer or Long, dimensionality of the output space.
    activation: Activation function (callable). Set it to None to maintain a
      linear activation.
    use_bias: Boolean, whether the layer uses a bias.
    kernel_initializer: Initializer function for the weight matrix.
      If `None` (default), weights are initialized using the default
      initializer used by `tf.compat.v1.get_variable`.
    bias_initializer: Initializer function for the bias.
    kernel_regularizer: Regularizer function for the weight matrix.
    bias_regularizer: Regularizer function for the bias.
    activity_regularizer: Regularizer function for the output.
    kernel_constraint: An optional projection function to be applied to the
        kernel after being updated by an `Optimizer` (e.g. used to implement
        norm constraints or value constraints for layer weights). The function
        must take as input the unprojected variable and must return the
        projected variable (which must have the same shape). Constraints are
        not safe to use when doing asynchronous distributed training.
    bias_constraint: An optional projection function to be applied to the
        bias after being updated by an `Optimizer`.
    trainable: Boolean, if `True` also add variables to the graph collection
      `GraphKeys.TRAINABLE_VARIABLES` (see `tf.Variable`).
    name: String, the name of the layer.
    reuse: Boolean, whether to reuse the weights of a previous layer
      by the same name.

  Returns:
    Output tensor the same shape as `inputs` except the last dimension is of
    size `units`.

  Raises:
    ValueError: if eager execution is enabled.
  """

class Dropout(keras_layers.Dropout, base.Layer):
    """Applies Dropout to the input.

  Dropout consists in randomly setting a fraction `rate` of input units to 0
  at each update during training time, which helps prevent overfitting.
  The units that are kept are scaled by `1 / (1 - rate)`, so that their
  sum is unchanged at training time and inference time.

  Args:
    rate: The dropout rate, between 0 and 1. E.g. `rate=0.1` would drop out
      10% of input units.
    noise_shape: 1D tensor of type `int32` representing the shape of the
      binary dropout mask that will be multiplied with the input.
      For instance, if your inputs have shape
      `(batch_size, timesteps, features)`, and you want the dropout mask
      to be the same for all timesteps, you can use
      `noise_shape=[batch_size, 1, features]`.
    seed: A Python integer. Used to create random seeds. See
      `tf.compat.v1.set_random_seed`.
      for behavior.
    name: The name of the layer (string).
  """
    def __init__(self, rate: float = 0.5, noise_shape: Incomplete | None = None, seed: Incomplete | None = None, name: Incomplete | None = None, **kwargs) -> None: ...
    def call(self, inputs, training: bool = False): ...

def dropout(inputs, rate: float = 0.5, noise_shape: Incomplete | None = None, seed: Incomplete | None = None, training: bool = False, name: Incomplete | None = None):
    '''Applies Dropout to the input.

  Dropout consists in randomly setting a fraction `rate` of input units to 0
  at each update during training time, which helps prevent overfitting.
  The units that are kept are scaled by `1 / (1 - rate)`, so that their
  sum is unchanged at training time and inference time.

  Args:
    inputs: Tensor input.
    rate: The dropout rate, between 0 and 1. E.g. "rate=0.1" would drop out
      10% of input units.
    noise_shape: 1D tensor of type `int32` representing the shape of the
      binary dropout mask that will be multiplied with the input.
      For instance, if your inputs have shape
      `(batch_size, timesteps, features)`, and you want the dropout mask
      to be the same for all timesteps, you can use
      `noise_shape=[batch_size, 1, features]`.
    seed: A Python integer. Used to create random seeds. See
      `tf.compat.v1.set_random_seed`
      for behavior.
    training: Either a Python boolean, or a TensorFlow boolean scalar tensor
      (e.g. a placeholder). Whether to return the output in training mode
      (apply dropout) or in inference mode (return the input untouched).
    name: The name of the layer (string).

  Returns:
    Output tensor.

  Raises:
    ValueError: if eager execution is enabled.
  '''

class Flatten(keras_layers.Flatten, base.Layer):
    """Flattens an input tensor while preserving the batch axis (axis 0).

  Args:
    data_format: A string, one of `channels_last` (default) or `channels_first`.
      The ordering of the dimensions in the inputs.
      `channels_last` corresponds to inputs with shape
      `(batch, ..., channels)` while `channels_first` corresponds to
      inputs with shape `(batch, channels, ...)`.

  Examples:

  ```
    x = tf.compat.v1.placeholder(shape=(None, 4, 4), dtype='float32')
    y = Flatten()(x)
    # now `y` has shape `(None, 16)`

    x = tf.compat.v1.placeholder(shape=(None, 3, None), dtype='float32')
    y = Flatten()(x)
    # now `y` has shape `(None, None)`
  ```
  """

def flatten(inputs, name: Incomplete | None = None, data_format: str = 'channels_last'):
    """Flattens an input tensor while preserving the batch axis (axis 0).

  Args:
    inputs: Tensor input.
    name: The name of the layer (string).
    data_format: A string, one of `channels_last` (default) or `channels_first`.
      The ordering of the dimensions in the inputs.
      `channels_last` corresponds to inputs with shape
      `(batch, height, width, channels)` while `channels_first` corresponds to
      inputs with shape `(batch, channels, height, width)`.

  Returns:
    Reshaped tensor.

  Examples:

  ```
    x = tf.compat.v1.placeholder(shape=(None, 4, 4), dtype='float32')
    y = flatten(x)
    # now `y` has shape `(None, 16)`

    x = tf.compat.v1.placeholder(shape=(None, 3, None), dtype='float32')
    y = flatten(x)
    # now `y` has shape `(None, None)`
  ```
  """
FullyConnected = Dense
fully_connected = dense
