from _typeshed import Incomplete
from tensorflow.python.framework import dtypes as dtypes
from tensorflow.python.keras import backend as backend, constraints as constraints, initializers as initializers, regularizers as regularizers
from tensorflow.python.keras.engine.base_layer import Layer as Layer
from tensorflow.python.keras.engine.input_spec import InputSpec as InputSpec
from tensorflow.python.keras.utils import tf_utils as tf_utils
from tensorflow.python.ops import math_ops as math_ops
from tensorflow.python.util.tf_export import keras_export as keras_export

def get_globals(): ...

class LeakyReLU(Layer):
    """Leaky version of a Rectified Linear Unit.

  It allows a small gradient when the unit is not active:

  ```
    f(x) = alpha * x if x < 0
    f(x) = x if x >= 0
  ```

  Usage:

  >>> layer = tf.keras.layers.LeakyReLU()
  >>> output = layer([-3.0, -1.0, 0.0, 2.0])
  >>> list(output.numpy())
  [-0.9, -0.3, 0.0, 2.0]
  >>> layer = tf.keras.layers.LeakyReLU(alpha=0.1)
  >>> output = layer([-3.0, -1.0, 0.0, 2.0])
  >>> list(output.numpy())
  [-0.3, -0.1, 0.0, 2.0]

  Input shape:
    Arbitrary. Use the keyword argument `input_shape`
    (tuple of integers, does not include the batch axis)
    when using this layer as the first layer in a model.

  Output shape:
    Same shape as the input.

  Args:
    alpha: Float >= 0. Negative slope coefficient. Default to 0.3.

  """
    supports_masking: bool
    alpha: Incomplete
    def __init__(self, alpha: float = 0.3, **kwargs) -> None: ...
    def call(self, inputs): ...
    def get_config(self): ...
    def compute_output_shape(self, input_shape): ...

class PReLU(Layer):
    """Parametric Rectified Linear Unit.

  It follows:

  ```
    f(x) = alpha * x for x < 0
    f(x) = x for x >= 0
  ```

  where `alpha` is a learned array with the same shape as x.

  Input shape:
    Arbitrary. Use the keyword argument `input_shape`
    (tuple of integers, does not include the samples axis)
    when using this layer as the first layer in a model.

  Output shape:
    Same shape as the input.

  Args:
    alpha_initializer: Initializer function for the weights.
    alpha_regularizer: Regularizer for the weights.
    alpha_constraint: Constraint for the weights.
    shared_axes: The axes along which to share learnable
      parameters for the activation function.
      For example, if the incoming feature maps
      are from a 2D convolution
      with output shape `(batch, height, width, channels)`,
      and you wish to share parameters across space
      so that each filter only has one set of parameters,
      set `shared_axes=[1, 2]`.
  """
    supports_masking: bool
    alpha_initializer: Incomplete
    alpha_regularizer: Incomplete
    alpha_constraint: Incomplete
    shared_axes: Incomplete
    def __init__(self, alpha_initializer: str = 'zeros', alpha_regularizer: Incomplete | None = None, alpha_constraint: Incomplete | None = None, shared_axes: Incomplete | None = None, **kwargs) -> None: ...
    alpha: Incomplete
    input_spec: Incomplete
    built: bool
    def build(self, input_shape) -> None: ...
    def call(self, inputs): ...
    def get_config(self): ...
    def compute_output_shape(self, input_shape): ...

class ELU(Layer):
    """Exponential Linear Unit.

  It follows:

  ```
    f(x) =  alpha * (exp(x) - 1.) for x < 0
    f(x) = x for x >= 0
  ```

  Input shape:
    Arbitrary. Use the keyword argument `input_shape`
    (tuple of integers, does not include the samples axis)
    when using this layer as the first layer in a model.

  Output shape:
    Same shape as the input.

  Args:
    alpha: Scale for the negative factor.
  """
    supports_masking: bool
    alpha: Incomplete
    def __init__(self, alpha: float = 1.0, **kwargs) -> None: ...
    def call(self, inputs): ...
    def get_config(self): ...
    def compute_output_shape(self, input_shape): ...

class ThresholdedReLU(Layer):
    """Thresholded Rectified Linear Unit.

  It follows:

  ```
    f(x) = x for x > theta
    f(x) = 0 otherwise`
  ```

  Input shape:
    Arbitrary. Use the keyword argument `input_shape`
    (tuple of integers, does not include the samples axis)
    when using this layer as the first layer in a model.

  Output shape:
    Same shape as the input.

  Args:
    theta: Float >= 0. Threshold location of activation.
  """
    supports_masking: bool
    theta: Incomplete
    def __init__(self, theta: float = 1.0, **kwargs) -> None: ...
    def call(self, inputs): ...
    def get_config(self): ...
    def compute_output_shape(self, input_shape): ...

class Softmax(Layer):
    """Softmax activation function.

  Example without mask:

  >>> inp = np.asarray([1., 2., 1.])
  >>> layer = tf.keras.layers.Softmax()
  >>> layer(inp).numpy()
  array([0.21194157, 0.5761169 , 0.21194157], dtype=float32)
  >>> mask = np.asarray([True, False, True], dtype=bool)
  >>> layer(inp, mask).numpy()
  array([0.5, 0. , 0.5], dtype=float32)

  Input shape:
    Arbitrary. Use the keyword argument `input_shape`
    (tuple of integers, does not include the samples axis)
    when using this layer as the first layer in a model.

  Output shape:
    Same shape as the input.

  Args:
    axis: Integer, or list of Integers, axis along which the softmax
      normalization is applied.
  Call arguments:
    inputs: The inputs, or logits to the softmax layer.
    mask: A boolean mask of the same shape as `inputs`. Defaults to `None`. The
      mask specifies 1 to keep and 0 to mask.

  Returns:
    softmaxed output with the same shape as `inputs`.
  """
    supports_masking: bool
    axis: Incomplete
    def __init__(self, axis: int = -1, **kwargs) -> None: ...
    def call(self, inputs, mask: Incomplete | None = None): ...
    def get_config(self): ...
    def compute_output_shape(self, input_shape): ...

class ReLU(Layer):
    """Rectified Linear Unit activation function.

  With default values, it returns element-wise `max(x, 0)`.

  Otherwise, it follows:

  ```
    f(x) = max_value if x >= max_value
    f(x) = x if threshold <= x < max_value
    f(x) = negative_slope * (x - threshold) otherwise
  ```

  Usage:

  >>> layer = tf.keras.layers.ReLU()
  >>> output = layer([-3.0, -1.0, 0.0, 2.0])
  >>> list(output.numpy())
  [0.0, 0.0, 0.0, 2.0]
  >>> layer = tf.keras.layers.ReLU(max_value=1.0)
  >>> output = layer([-3.0, -1.0, 0.0, 2.0])
  >>> list(output.numpy())
  [0.0, 0.0, 0.0, 1.0]
  >>> layer = tf.keras.layers.ReLU(negative_slope=1.0)
  >>> output = layer([-3.0, -1.0, 0.0, 2.0])
  >>> list(output.numpy())
  [-3.0, -1.0, 0.0, 2.0]
  >>> layer = tf.keras.layers.ReLU(threshold=1.5)
  >>> output = layer([-3.0, -1.0, 1.0, 2.0])
  >>> list(output.numpy())
  [0.0, 0.0, 0.0, 2.0]

  Input shape:
    Arbitrary. Use the keyword argument `input_shape`
    (tuple of integers, does not include the batch axis)
    when using this layer as the first layer in a model.

  Output shape:
    Same shape as the input.

  Args:
    max_value: Float >= 0. Maximum activation value. Default to None, which
      means unlimited.
    negative_slope: Float >= 0. Negative slope coefficient. Default to 0.
    threshold: Float >= 0. Threshold value for thresholded activation. Default
      to 0.
  """
    supports_masking: bool
    max_value: Incomplete
    negative_slope: Incomplete
    threshold: Incomplete
    def __init__(self, max_value: Incomplete | None = None, negative_slope: int = 0, threshold: int = 0, **kwargs) -> None: ...
    def call(self, inputs): ...
    def get_config(self): ...
    def compute_output_shape(self, input_shape): ...
