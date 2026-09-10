import flax.linen as nn
import jax
import jax.numpy as jnp
from ...modeling_flax_outputs import FlaxBaseModelOutputWithPastAndCrossAttentions as FlaxBaseModelOutputWithPastAndCrossAttentions, FlaxCausalLMOutputWithCrossAttentions as FlaxCausalLMOutputWithCrossAttentions
from ...modeling_flax_utils import ACT2FN as ACT2FN, FlaxPreTrainedModel as FlaxPreTrainedModel, append_call_sample_docstring as append_call_sample_docstring
from ...utils import add_start_docstrings as add_start_docstrings, add_start_docstrings_to_model_forward as add_start_docstrings_to_model_forward, logging as logging
from .configuration_gpt2 import GPT2Config as GPT2Config
from _typeshed import Incomplete
from flax.core.frozen_dict import FrozenDict as FrozenDict
from typing import Any, Optional, Tuple

logger: Incomplete
GPT2_START_DOCSTRING: str
GPT2_INPUTS_DOCSTRING: str

class FlaxConv1D(nn.Module):
    features: int
    use_bias: bool
    dtype: Any
    precision: Any
    def __call__(self, inputs): ...

class FlaxGPT2Attention(nn.Module):
    config: GPT2Config
    dtype: jnp.dtype
    causal: bool
    is_cross_attention: bool
    embed_dim: Incomplete
    num_heads: Incomplete
    head_dim: Incomplete
    c_attn: Incomplete
    q_attn: Incomplete
    c_proj: Incomplete
    resid_dropout: Incomplete
    causal_mask: Incomplete
    def setup(self) -> None: ...
    def __call__(self, hidden_states, key_value_states: Optional[jnp.ndarray] = None, attention_mask: Incomplete | None = None, deterministic: bool = True, init_cache: bool = False, output_attentions: bool = False): ...

class FlaxGPT2MLP(nn.Module):
    config: GPT2Config
    intermediate_size: int
    dtype: jnp.dtype
    c_fc: Incomplete
    c_proj: Incomplete
    act: Incomplete
    dropout: Incomplete
    def setup(self) -> None: ...
    def __call__(self, hidden_states, deterministic: bool = True): ...

class FlaxGPT2Block(nn.Module):
    config: GPT2Config
    dtype: jnp.dtype
    ln_1: Incomplete
    attn: Incomplete
    ln_2: Incomplete
    crossattention: Incomplete
    ln_cross_attn: Incomplete
    mlp: Incomplete
    def setup(self) -> None: ...
    def __call__(self, hidden_states, attention_mask: Incomplete | None = None, encoder_hidden_states: Optional[jnp.ndarray] = None, encoder_attention_mask: Optional[jnp.ndarray] = None, deterministic: bool = True, init_cache: bool = False, output_attentions: bool = False): ...

class FlaxGPT2PreTrainedModel(FlaxPreTrainedModel):
    """
    An abstract class to handle weights initialization and a simple interface for downloading and loading pretrained
    models.
    """
    config_class = GPT2Config
    base_model_prefix: str
    module_class: nn.Module
    def __init__(self, config: GPT2Config, input_shape: Tuple = (1, 1), seed: int = 0, dtype: jnp.dtype = ..., _do_init: bool = True, **kwargs) -> None: ...
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
    def __call__(self, input_ids, attention_mask: Incomplete | None = None, position_ids: Incomplete | None = None, encoder_hidden_states: Optional[jnp.ndarray] = None, encoder_attention_mask: Optional[jnp.ndarray] = None, params: dict = None, past_key_values: dict = None, dropout_rng: jax.random.PRNGKey = None, train: bool = False, output_attentions: Optional[bool] = None, output_hidden_states: Optional[bool] = None, return_dict: Optional[bool] = None): ...

class FlaxGPT2BlockCollection(nn.Module):
    config: GPT2Config
    dtype: jnp.dtype
    blocks: Incomplete
    def setup(self) -> None: ...
    def __call__(self, hidden_states, attention_mask: Incomplete | None = None, encoder_hidden_states: Optional[jnp.ndarray] = None, encoder_attention_mask: Optional[jnp.ndarray] = None, deterministic: bool = True, init_cache: bool = False, output_attentions: bool = False, output_hidden_states: bool = False, return_dict: bool = True): ...

class FlaxGPT2Module(nn.Module):
    config: GPT2Config
    dtype: jnp.dtype
    embed_dim: Incomplete
    wte: Incomplete
    wpe: Incomplete
    dropout: Incomplete
    h: Incomplete
    ln_f: Incomplete
    def setup(self) -> None: ...
    def __call__(self, input_ids, attention_mask, position_ids, encoder_hidden_states: Optional[jnp.ndarray] = None, encoder_attention_mask: Optional[jnp.ndarray] = None, deterministic: bool = True, init_cache: bool = False, output_attentions: bool = False, output_hidden_states: bool = False, return_dict: bool = True): ...

class FlaxGPT2Model(FlaxGPT2PreTrainedModel):
    module_class = FlaxGPT2Module

class FlaxGPT2LMHeadModule(nn.Module):
    config: GPT2Config
    dtype: jnp.dtype
    transformer: Incomplete
    lm_head: Incomplete
    def setup(self) -> None: ...
    def __call__(self, input_ids, attention_mask, position_ids, encoder_hidden_states: Optional[jnp.ndarray] = None, encoder_attention_mask: Optional[jnp.ndarray] = None, deterministic: bool = True, init_cache: bool = False, output_attentions: bool = False, output_hidden_states: bool = False, return_dict: bool = True): ...

class FlaxGPT2LMHeadModel(FlaxGPT2PreTrainedModel):
    module_class = FlaxGPT2LMHeadModule
    def prepare_inputs_for_generation(self, input_ids, max_length, attention_mask: Optional[jnp.DeviceArray] = None): ...
    def update_inputs_for_generation(self, model_outputs, model_kwargs): ...
