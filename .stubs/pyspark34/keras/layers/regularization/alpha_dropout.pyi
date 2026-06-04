from _typeshed import Incomplete
from keras import backend as backend
from keras.engine import base_layer as base_layer
from keras.utils import tf_utils as tf_utils

class AlphaDropout(base_layer.BaseRandomLayer):
    """Applies Alpha Dropout to the input.

    Alpha Dropout is a `Dropout` that keeps mean and variance of inputs
    to their original values, in order to ensure the self-normalizing property
    even after this dropout.
    Alpha Dropout fits well to Scaled Exponential Linear Units
    by randomly setting activations to the negative saturation value.

    Args:
      rate: float, drop probability (as with `Dropout`).
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
    rate: Incomplete
    noise_shape: Incomplete
    seed: Incomplete
    supports_masking: bool
    def __init__(self, rate, noise_shape: Incomplete | None = None, seed: Incomplete | None = None, **kwargs) -> None: ...
    def call(self, inputs, training: Incomplete | None = None): ...
    def get_config(self): ...
    def compute_output_shape(self, input_shape): ...
