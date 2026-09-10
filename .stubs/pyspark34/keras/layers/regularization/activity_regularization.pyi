from _typeshed import Incomplete
from keras import regularizers as regularizers
from keras.engine.base_layer import Layer as Layer

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
