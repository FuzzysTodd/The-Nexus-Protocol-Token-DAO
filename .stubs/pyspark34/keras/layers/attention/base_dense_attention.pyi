from _typeshed import Incomplete
from keras import backend as backend
from keras.engine import base_layer as base_layer
from keras.utils import control_flow_util as control_flow_util

class BaseDenseAttention(base_layer.BaseRandomLayer):
    """Base Attention class for Dense networks.

    This class is suitable for Dense or CNN networks, and not for RNN networks.

    Implementations of attention mechanisms should inherit from this class, and
    reuse the `apply_attention_scores()` method.

    Args:
      dropout: Float between 0 and 1. Fraction of the units to drop for the
        attention scores.

    Call Args:
      inputs: List of the following tensors:
        * query: Query `Tensor` of shape `[batch_size, Tq, dim]`.
        * value: Value `Tensor` of shape `[batch_size, Tv, dim]`.
        * key: Optional key `Tensor` of shape `[batch_size, Tv, dim]`. If not
          given, will use `value` for both `key` and `value`, which is the most
          common case.
      mask: List of the following tensors:
        * query_mask: A boolean mask `Tensor` of shape `[batch_size, Tq]`. If
          given, the output will be zero at the positions where `mask==False`.
        * value_mask: A boolean mask `Tensor` of shape `[batch_size, Tv]`. If
          given, will apply the mask such that values at positions where
          `mask==False` do not contribute to the result.
      training: Python boolean indicating whether the layer should behave in
        training mode (adding dropout) or in inference mode (no dropout).
      return_attention_scores: bool, if `True`, returns the attention scores
        (after masking and softmax) as an additional output argument.

    Output:

      Attention outputs of shape `[batch_size, Tq, dim]`.
      [Optional] Attention scores after masking and softmax with shape
        `[batch_size, Tq, Tv]`.
    """
    causal: Incomplete
    dropout: Incomplete
    supports_masking: bool
    def __init__(self, dropout: float = 0.0, **kwargs) -> None: ...
    built: bool
    def build(self, input_shape) -> None: ...
    def call(self, inputs, mask: Incomplete | None = None, training: Incomplete | None = None, return_attention_scores: bool = False, use_causal_mask: bool = False): ...
    def compute_mask(self, inputs, mask: Incomplete | None = None): ...
    def compute_output_shape(self, input_shape): ...
    def get_config(self): ...
