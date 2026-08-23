from _typeshed import Incomplete
from keras import backend as backend
from keras.engine.base_layer import Layer as Layer
from keras.utils import tf_utils as tf_utils

class _Merge(Layer):
    """Generic merge layer for elementwise merge functions.

    Used to implement `Sum`, `Average`, etc.
    """
    supports_masking: bool
    def __init__(self, **kwargs) -> None:
        """Initializes a Merge layer.

        Args:
          **kwargs: standard layer keyword arguments.
        """
    def build(self, input_shape) -> None: ...
    def call(self, inputs): ...
    def compute_output_shape(self, input_shape): ...
    def compute_mask(self, inputs, mask: Incomplete | None = None): ...
    def get_config(self): ...
