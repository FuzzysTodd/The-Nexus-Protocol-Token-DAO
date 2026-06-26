from _typeshed import Incomplete
from keras import backend as backend, constraints as constraints, initializers as initializers, regularizers as regularizers
from keras.engine.base_layer import Layer as Layer
from keras.engine.input_spec import InputSpec as InputSpec
from keras.utils import tf_utils as tf_utils

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
