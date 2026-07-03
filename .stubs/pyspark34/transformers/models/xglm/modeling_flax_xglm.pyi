import flax.linen as nn
import jax
import jax.numpy as jnp
from ...modeling_flax_outputs import FlaxBaseModelOutputWithPastAndCrossAttentions as FlaxBaseModelOutputWithPastAndCrossAttentions, FlaxCausalLMOutputWithCrossAttentions as FlaxCausalLMOutputWithCrossAttentions
from ...modeling_flax_utils import ACT2FN as ACT2FN, FlaxPreTrainedModel as FlaxPreTrainedModel, append_call_sample_docstring as append_call_sample_docstring
from ...utils import add_start_docstrings as add_start_docstrings, add_start_docstrings_to_model_forward as add_start_docstrings_to_model_forward, logging as logging
from .configuration_xglm import XGLMConfig as XGLMConfig
from _typeshed import Incomplete
from flax.core.frozen_dict import FrozenDict as FrozenDict
from jax.random import PRNGKey as PRNGKey
from typing import Optional, Tuple

logger: Incomplete
XGLM_START_DOCSTRING: str
XGLM_INPUTS_DOCSTRING: str

def create_sinusoidal_positions(n_pos, dim, padding_idx: int = 1): ...
def shift_tokens_right(input_ids: jnp.ndarray, pad_token_id: int, decoder_start_token_id: int) -> jnp.ndarray:
    """
    Shift input ids one token to the right.
    """

class FlaxXGLMAttention(nn.Module):
    config: XGLMConfig
    embed_dim: int
    num_heads: int
    dropout: float
    causal: bool
    bias: bool
    dtype: jnp.dtype
    head_dim: Incomplete
    out_proj: Incomplete
    dropout_layer: Incomplete
    causal_mask: Incomplete
    def setup(self) -> None: ...
    def __call__(self, hidden_states: jnp.ndarray, key_value_states: Optional[jnp.ndarray] = None, attention_mask: Optional[jnp.ndarray] = None, init_cache: bool = False, deterministic: bool = True) -> Tuple[jnp.ndarray]:
        """Input shape: Batch x Time x Channel"""

class FlaxXGLMDecoderLayer(nn.Module):
    config: XGLMConfig
    dtype: jnp.dtype
    embed_dim: Incomplete
    self_attn: Incomplete
    self_attn_layer_norm: Incomplete
    dropout_layer: Incomplete
    activation_fn: Incomplete
    activation_dropout_layer: Incomplete
    encoder_attn: Incomplete
    encoder_attn_layer_norm: Incomplete
    fc1: Incomplete
    fc2: Incomplete
    final_layer_norm: Incomplete
    def setup(self) -> None: ...
    def __call__(self, hidden_states: jnp.ndarray, attention_mask: jnp.ndarray, encoder_hidden_states: Optional[jnp.ndarray] = None, encoder_attention_mask: Optional[jnp.ndarray] = None, init_cache: bool = False, output_attentions: bool = True, deterministic: bool = True) -> Tuple[jnp.ndarray]: ...

class FlaxXGLMDecoderLayerCollection(nn.Module):
    config: XGLMConfig
    dtype: jnp.dtype
    layers: Incomplete
    layerdrop: Incomplete
    def setup(self) -> None: ...
    def __call__(self, hidden_states, attention_mask, encoder_hidden_states: Optional[jnp.ndarray] = None, encoder_attention_mask: Optional[jnp.ndarray] = None, deterministic: bool = True, init_cache: bool = False, output_attentions: bool = False, output_hidden_states: bool = False, return_dict: bool = True): ...

class FlaxXGLMModule(nn.Module):
    config: XGLMConfig
    dtype: jnp.dtype
    dropout_layer: Incomplete
    padding_idx: Incomplete
    max_target_positions: Incomplete
    embed_scale: Incomplete
    embed_tokens: Incomplete
    offset: int
    embed_positions: Incomplete
    layers: Incomplete
    layer_norm: Incomplete
    def setup(self) -> None: ...
    def __call__(self, input_ids, attention_mask, position_ids, encoder_hidden_states: Optional[jnp.ndarray] = None, encoder_attention_mask: Optional[jnp.ndarray] = None, init_cache: bool = False, output_attentions: bool = False, output_hidden_states: bool = False, return_dict: bool = True, deterministic: bool = True): ...

class FlaxXGLMPreTrainedModel(FlaxPreTrainedModel):
    config_class = XGLMConfig
    base_model_prefix: str
    module_class: nn.Module
    def __init__(self, config: XGLMConfig, input_shape: Tuple[int] = (1, 1), seed: int = 0, dtype: jnp.dtype = ..., _do_init: bool = True, **kwargs) -> None: ...
    def init_weights(self, rng: jax.random.PRNGKey, input_shape: Tuple, params: FrozenDict = None) -> FrozenDict: ...
    def init_cache(self, batch_size, max_length):
        """
        Args:
            batch_size (`int`):
                batch_size used for fast auto-regressive decoding. Defines the batch size of the initialized cache.
            max_length (`int`):
                maximum possible length for auto-regressive decoding. Defines the sequence length of the initialized
                cache.
        """
    def __call__(self, input_ids: jnp.ndarray, attention_mask: Optional[jnp.ndarray] = None, position_ids: Optional[jnp.ndarray] = None, encoder_hidden_states: Optional[jnp.ndarray] = None, encoder_attention_mask: Optional[jnp.ndarray] = None, output_attentions: Optional[bool] = None, output_hidden_states: Optional[bool] = None, return_dict: Optional[bool] = None, train: bool = False, params: dict = None, past_key_values: dict = None, dropout_rng: PRNGKey = None): ...

class FlaxXGLMModel(FlaxXGLMPreTrainedModel):
    module_class = FlaxXGLMModule

class FlaxXGLMForCausalLMModule(nn.Module):
    config: XGLMConfig
    dtype: jnp.dtype
    model: Incomplete
    lm_head: Incomplete
    def setup(self) -> None: ...
    def __call__(self, input_ids, attention_mask, position_ids, encoder_hidden_states: Optional[jnp.ndarray] = None, encoder_attention_mask: Optional[jnp.ndarray] = None, init_cache: bool = False, output_attentions: bool = False, output_hidden_states: bool = False, return_dict: bool = True, deterministic: bool = True): ...

class FlaxXGLMForCausalLM(FlaxXGLMPreTrainedModel):
    module_class = FlaxXGLMForCausalLMModule
    def prepare_inputs_for_generation(self, input_ids, max_length, attention_mask: Optional[jnp.DeviceArray] = None): ...
    def update_inputs_for_generation(self, model_outputs, model_kwargs): ...
