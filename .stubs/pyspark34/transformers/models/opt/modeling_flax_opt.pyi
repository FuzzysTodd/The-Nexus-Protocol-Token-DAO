import flax.linen as nn
import jax
import jax.numpy as jnp
from ...modeling_flax_outputs import FlaxBaseModelOutput as FlaxBaseModelOutput, FlaxMaskedLMOutput as FlaxMaskedLMOutput
from ...modeling_flax_utils import ACT2FN as ACT2FN, FlaxPreTrainedModel as FlaxPreTrainedModel, append_call_sample_docstring as append_call_sample_docstring
from ...utils import add_start_docstrings as add_start_docstrings, logging as logging
from .configuration_opt import OPTConfig as OPTConfig
from _typeshed import Incomplete
from flax.core.frozen_dict import FrozenDict as FrozenDict
from jax.random import PRNGKey as PRNGKey
from typing import Optional, Tuple

logger: Incomplete
OPT_START_DOCSTRING: str
OPT_INPUTS_DOCSTRING: str

class FlaxOPTAttention(nn.Module):
    config: OPTConfig
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

class FlaxOPTDecoderLayer(nn.Module):
    config: OPTConfig
    dtype: jnp.dtype
    embed_dim: Incomplete
    self_attn: Incomplete
    do_layer_norm_before: Incomplete
    dropout_layer: Incomplete
    activation_fn: Incomplete
    self_attn_layer_norm: Incomplete
    fc1: Incomplete
    fc2: Incomplete
    final_layer_norm: Incomplete
    def setup(self) -> None: ...
    def __call__(self, hidden_states: jnp.ndarray, attention_mask: jnp.ndarray, init_cache: bool = False, output_attentions: bool = True, deterministic: bool = True) -> Tuple[jnp.ndarray]: ...

class FlaxOPTDecoderLayerCollection(nn.Module):
    config: OPTConfig
    dtype: jnp.dtype
    layers: Incomplete
    layerdrop: Incomplete
    def setup(self) -> None: ...
    def __call__(self, hidden_states, attention_mask, deterministic: bool = True, init_cache: bool = False, output_attentions: bool = False, output_hidden_states: bool = False): ...

class FlaxOPTLearnedPositionalEmbedding(nn.Embed):
    """
    This module learns positional embeddings up to a fixed maximum size.
    """
    offset: int
    embedding: Incomplete
    def setup(self) -> None: ...
    def __call__(self, positions):
        """`input_ids_shape` is expected to be [bsz x seqlen]."""

class FlaxOPTDecoder(nn.Module):
    config: OPTConfig
    dtype: jnp.dtype
    offset: int
    dropout_layer: Incomplete
    padding_idx: Incomplete
    max_target_positions: Incomplete
    embed_tokens: Incomplete
    embed_positions: Incomplete
    project_in: Incomplete
    project_out: Incomplete
    final_layer_norm: Incomplete
    layers: Incomplete
    def setup(self) -> None: ...
    def __call__(self, input_ids, attention_mask, position_ids, init_cache: bool = False, output_attentions: bool = False, output_hidden_states: bool = False, return_dict: bool = True, deterministic: bool = True): ...

class FlaxOPTPreTrainedModel(FlaxPreTrainedModel):
    config_class = OPTConfig
    base_model_prefix: str
    module_class: nn.Module
    def __init__(self, config: OPTConfig, input_shape: Tuple[int] = (1, 1), seed: int = 0, dtype: jnp.dtype = ..., _do_init: bool = True, **kwargs) -> None: ...
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
    def __call__(self, input_ids: jnp.ndarray, attention_mask: Optional[jnp.ndarray] = None, position_ids: Optional[jnp.ndarray] = None, params: dict = None, past_key_values: dict = None, output_attentions: Optional[bool] = None, output_hidden_states: Optional[bool] = None, return_dict: Optional[bool] = None, dropout_rng: PRNGKey = None, deterministic: bool = True): ...

class FlaxOPTModule(nn.Module):
    config: OPTConfig
    dtype: jnp.dtype
    decoder: Incomplete
    def setup(self) -> None: ...
    def __call__(self, input_ids, attention_mask, position_ids, output_attentions: bool = False, output_hidden_states: bool = False, return_dict: bool = True, deterministic: bool = True, init_cache: bool = False): ...

class FlaxOPTModel(FlaxOPTPreTrainedModel):
    config: OPTConfig
    dtype: jnp.dtype
    module_class = FlaxOPTModule

class FlaxOPTForCausalLMModule(nn.Module):
    config: OPTConfig
    dtype: jnp.dtype
    model: Incomplete
    lm_head: Incomplete
    def setup(self) -> None: ...
    def __call__(self, input_ids, attention_mask, position_ids, init_cache: bool = False, output_attentions: bool = False, output_hidden_states: bool = False, return_dict: bool = True, deterministic: bool = True): ...

class FlaxOPTForCausalLM(FlaxOPTPreTrainedModel):
    module_class = FlaxOPTForCausalLMModule
    def prepare_inputs_for_generation(self, input_ids, max_length, attention_mask: Optional[jnp.DeviceArray] = None): ...
    def update_inputs_for_generation(self, model_outputs, model_kwargs): ...
