from _typeshed import Incomplete
from keras import constraints as constraints, initializers as initializers, regularizers as regularizers
from keras.layers import InputSpec as InputSpec, Layer as Layer
from keras.utils import tf_utils as tf_utils

class GroupNormalization(Layer):
    """Group normalization layer.

    Group Normalization divides the channels into groups and computes
    within each group the mean and variance for normalization.
    Empirically, its accuracy is more stable than batch norm in a wide
    range of small batch sizes, if learning rate is adjusted linearly
    with batch sizes.

    Relation to Layer Normalization:
    If the number of groups is set to 1, then this operation becomes nearly
    identical to Layer Normalization (see Layer Normalization docs for details).

    Relation to Instance Normalization:
    If the number of groups is set to the input dimension (number of groups is
    equal to number of channels), then this operation becomes identical to
    Instance Normalization.

    Args:
      groups: Integer, the number of groups for Group Normalization. Can be in
        the range [1, N] where N is the input dimension. The input dimension
        must be divisible by the number of groups. Defaults to 32.
      axis: Integer or List/Tuple. The axis or axes to normalize across.
        Typically this is the features axis/axes. The left-out axes are
        typically the batch axis/axes. This argument defaults to `-1`, the last
        dimension in the input.
      epsilon: Small float added to variance to avoid dividing by zero. Defaults
        to 1e-3
      center: If True, add offset of `beta` to normalized tensor. If False,
        `beta` is ignored. Defaults to True.
      scale: If True, multiply by `gamma`. If False, `gamma` is not used.
        Defaults to True. When the next layer is linear (also e.g. `nn.relu`),
        this can be disabled since the scaling will be done by the next layer.
      beta_initializer: Initializer for the beta weight. Defaults to zeros.
      gamma_initializer: Initializer for the gamma weight. Defaults to ones.
      beta_regularizer: Optional regularizer for the beta weight. None by
        default.
      gamma_regularizer: Optional regularizer for the gamma weight. None by
        default.
      beta_constraint: Optional constraint for the beta weight. None by default.
      gamma_constraint: Optional constraint for the gamma weight. None by
        default.  Input shape: Arbitrary. Use the keyword argument `input_shape`
        (tuple of integers, does not include the samples axis) when using this
        layer as the first layer in a model.  Output shape: Same shape as input.
    Reference: - [Yuxin Wu & Kaiming He, 2018](https://arxiv.org/abs/1803.08494)
    """
    supports_masking: bool
    groups: Incomplete
    axis: Incomplete
    epsilon: Incomplete
    center: Incomplete
    scale: Incomplete
    beta_initializer: Incomplete
    gamma_initializer: Incomplete
    beta_regularizer: Incomplete
    gamma_regularizer: Incomplete
    beta_constraint: Incomplete
    gamma_constraint: Incomplete
    def __init__(self, groups: int = 32, axis: int = -1, epsilon: float = 0.001, center: bool = True, scale: bool = True, beta_initializer: str = 'zeros', gamma_initializer: str = 'ones', beta_regularizer: Incomplete | None = None, gamma_regularizer: Incomplete | None = None, beta_constraint: Incomplete | None = None, gamma_constraint: Incomplete | None = None, **kwargs) -> None: ...
    input_spec: Incomplete
    gamma: Incomplete
    beta: Incomplete
    def build(self, input_shape) -> None: ...
    def call(self, inputs): ...
    def compute_output_shape(self, input_shape): ...
    def get_config(self): ...
