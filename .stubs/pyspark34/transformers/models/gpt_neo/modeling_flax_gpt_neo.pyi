import flax.linen as nn
import jax
import jax.numpy as jnp
from ...modeling_flax_outputs import FlaxBaseModelOutput as FlaxBaseModelOutput, FlaxCausalLMOutput as FlaxCausalLMOutput
from ...modeling_flax_utils import ACT2FN as ACT2FN, FlaxPreTrainedModel as FlaxPreTrainedModel, append_call_sample_docstring as append_call_sample_docstring
from ...utils import add_start_docstrings as add_start_docstrings, add_start_docstrings_to_model_forward as add_start_docstrings_to_model_forward, logging as logging
from .configuration_gpt_neo import GPTNeoConfig as GPTNeoConfig
from _typeshed import Incomplete
from flax.core.frozen_dict import FrozenDict as FrozenDict
from typing import Optional, Tuple

logger: Incomplete
GPT_NEO_START_DOCSTRING: str
GPT_NEO_INPUTS_DOCSTRING: str

class FlaxGPTNeoSelfAttention(nn.Module):
    config: GPTNeoConfig
    attention_type: str
    dtype: jnp.dtype
    embed_dim: Incomplete
    num_heads: Incomplete
    head_dim: Incomplete
    attn_dropout: Incomplete
    resid_dropout: Incomplete
    out_proj: Incomplete
    causal_mask: Incomplete
    def setup(self) -> None: ...
    def __call__(self, hidden_states, attention_mask: Incomplete | None = None, deterministic: bool = True, init_cache: bool = False, output_attentions: bool = False): ...

class FlaxGPTNeoAttention(nn.Module):
    config: GPTNeoConfig
    layer_id: int
    dtype: jnp.dtype
    attention: Incomplete
    def setup(self) -> None: ...
    def __call__(self, hidden_states, attention_mask: Incomplete | None = None, deterministic: bool = True, init_cache: bool = False, output_attentions: bool = False): ...

class FlaxGPTNeoMLP(nn.Module):
    config: GPTNeoConfig
    intermediate_size: int
    dtype: jnp.dtype
    c_fc: Incomplete
    c_proj: Incomplete
    act: Incomplete
    dropout: Incomplete
    def setup(self) -> None: ...
    def __call__(self, hidden_states, deterministic: bool = True): ...

class FlaxGPTNeoBlock(nn.Module):
    config: GPTNeoConfig
    layer_id: int
    dtype: jnp.dtype
    ln_1: Incomplete
    attn: Incomplete
    ln_2: Incomplete
    mlp: Incomplete
    def setup(self) -> None: ...
    def __call__(self, hidden_states, attention_mask: Incomplete | None = None, deterministic: bool = True, init_cache: bool = False, output_attentions: bool = False): ...

class FlaxGPTNeoPreTrainedModel(FlaxPreTrainedModel):
    """
    An abstract class to handle weights initialization and a simple interface for downloading and loading pretrained
    models.
    """
    config_class = GPTNeoConfig
    base_model_prefix: str
    module_class: nn.Module
    def __init__(self, config: GPTNeoConfig, input_shape: Tuple = (1, 1), seed: int = 0, dtype: jnp.dtype = ..., _do_init: bool = True, **kwargs) -> None: ...
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
    def __call__(self, input_ids, attention_mask: Incomplete | None = None, position_ids: Incomplete | None = None, params: dict = None, past_key_values: dict = None, dropout_rng: jax.random.PRNGKey = None, train: bool = False, output_attentions: Optional[bool] = None, output_hidden_states: Optional[bool] = None, return_dict: Optional[bool] = None): ...

class FlaxGPTNeoBlockCollection(nn.Module):
    config: GPTNeoConfig
    dtype: jnp.dtype
    blocks: Incomplete
    def setup(self) -> None: ...
    def __call__(self, hidden_states, attention_mask: Incomplete | None = None, deterministic: bool = True, init_cache: bool = False, output_attentions: bool = False, output_hidden_states: bool = False, return_dict: bool = True): ...

class FlaxGPTNeoModule(nn.Module):
    config: GPTNeoConfig
    dtype: jnp.dtype
    embed_dim: Incomplete
    wte: Incomplete
    wpe: Incomplete
    dropout: Incomplete
    h: Incomplete
    ln_f: Incomplete
    def setup(self) -> None: ...
    def __call__(self, input_ids, attention_mask, position_ids, deterministic: bool = True, init_cache: bool = False, output_attentions: bool = False, output_hidden_states: bool = False, return_dict: bool = True): ...

class FlaxGPTNeoModel(FlaxGPTNeoPreTrainedModel):
    module_class = FlaxGPTNeoModule

class FlaxGPTNeoForCausalLMModule(nn.Module):
    config: GPTNeoConfig
    dtype: jnp.dtype
    transformer: Incomplete
    lm_head: Incomplete
    def setup(self) -> None: ...
    def __call__(self, input_ids, attention_mask, position_ids, deterministic: bool = True, init_cache: bool = False, output_attentions: bool = False, output_hidden_states: bool = False, return_dict: bool = True): ...

class FlaxGPTNeoForCausalLM(FlaxGPTNeoPreTrainedModel):
    module_class = FlaxGPTNeoForCausalLMModule
    def prepare_inputs_for_generation(self, input_ids, max_length, attention_mask: Optional[jnp.DeviceArray] = None): ...
    def update_inputs_for_generation(self, model_outputs, model_kwargs): ...
