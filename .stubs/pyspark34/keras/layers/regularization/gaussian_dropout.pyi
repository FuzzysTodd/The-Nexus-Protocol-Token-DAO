from _typeshed import Incomplete
from keras import backend as backend
from keras.engine import base_layer as base_layer
from keras.utils import tf_utils as tf_utils

class GaussianDropout(base_layer.BaseRandomLayer):
    """Apply multiplicative 1-centered Gaussian noise.

    As it is a regularization layer, it is only active at training time.

    Args:
      rate: Float, drop probability (as with `Dropout`).
        The multiplicative noise will have
        standard deviation `sqrt(rate / (1 - rate))`.
      seed: Integer, optional random seed to enable deterministic behavior.

    Call arguments:
      inputs: Input tensor (of any rank).
      training: Python boolean indicating whether the layer should behave in
        training mode (adding dropout) or in inference mode (doing nothing).

    Input shape:
      Arbitrary. Use the keyword argument `input_shape`
      (tuple of integers, does not include the samples axis)
      when using this layer as the first layer in a model.

    Output shape:
      Same shape as input.
    """
    supports_masking: bool
    rate: Incomplete
    seed: Incomplete
    def __init__(self, rate, seed: Incomplete | None = None, **kwargs) -> None: ...
    def call(self, inputs, training: Incomplete | None = None): ...
    def get_config(self): ...
    def compute_output_shape(self, input_shape): ...
