from _typeshed import Incomplete
from keras import backend as backend
from keras.engine.base_layer import Layer as Layer
from keras.utils import tf_utils as tf_utils

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
