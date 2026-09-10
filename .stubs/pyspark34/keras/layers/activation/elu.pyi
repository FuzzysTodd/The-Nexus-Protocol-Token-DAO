from _typeshed import Incomplete
from keras import backend as backend
from keras.engine.base_layer import Layer as Layer
from keras.utils import tf_utils as tf_utils

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
