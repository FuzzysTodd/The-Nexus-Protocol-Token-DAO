from _typeshed import Incomplete
from keras.engine import base_layer as base_layer
from keras.utils import tf_utils as tf_utils

class UnitNormalization(base_layer.Layer):
    """Unit normalization layer.

    Normalize a batch of inputs so that each input in the batch has a L2 norm
    equal to 1 (across the axes specified in `axis`).

    Example:

    >>> data = tf.constant(np.arange(6).reshape(2, 3), dtype=tf.float32)
    >>> normalized_data = tf.keras.layers.UnitNormalization()(data)
    >>> print(tf.reduce_sum(normalized_data[0, :] ** 2).numpy())
    1.0

    Args:
      axis: Integer or list/tuple. The axis or axes to normalize across.
        Typically this is the features axis or axes. The left-out axes are
        typically the batch axis or axes. Defaults to `-1`, the last dimension
        in the input.
    """
    axis: Incomplete
    supports_masking: bool
    def __init__(self, axis: int = -1, **kwargs) -> None: ...
    def build(self, input_shape) -> None: ...
    def call(self, inputs): ...
    def compute_output_shape(self, input_shape): ...
    def get_config(self): ...
