from _typeshed import Incomplete
from keras import backend as backend
from keras.engine import base_layer as base_layer
from keras.utils import tf_utils as tf_utils

class GaussianNoise(base_layer.BaseRandomLayer):
    """Apply additive zero-centered Gaussian noise.

    This is useful to mitigate overfitting
    (you could see it as a form of random data augmentation).
    Gaussian Noise (GS) is a natural choice as corruption process
    for real valued inputs.

    As it is a regularization layer, it is only active at training time.

    Args:
      stddev: Float, standard deviation of the noise distribution.
      seed: Integer, optional random seed to enable deterministic behavior.

    Call arguments:
      inputs: Input tensor (of any rank).
      training: Python boolean indicating whether the layer should behave in
        training mode (adding noise) or in inference mode (doing nothing).

    Input shape:
      Arbitrary. Use the keyword argument `input_shape`
      (tuple of integers, does not include the samples axis)
      when using this layer as the first layer in a model.

    Output shape:
      Same shape as input.
    """
    supports_masking: bool
    stddev: Incomplete
    seed: Incomplete
    def __init__(self, stddev, seed: Incomplete | None = None, **kwargs) -> None: ...
    def call(self, inputs, training: Incomplete | None = None): ...
    def get_config(self): ...
    def compute_output_shape(self, input_shape): ...
