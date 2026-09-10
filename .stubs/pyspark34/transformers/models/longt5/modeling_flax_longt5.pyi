import flax.linen as nn
import jax
import jax.numpy as jnp
import numpy as np
from ...modeling_flax_outputs import FlaxBaseModelOutput as FlaxBaseModelOutput, FlaxBaseModelOutputWithPastAndCrossAttentions as FlaxBaseModelOutputWithPastAndCrossAttentions, FlaxCausalLMOutputWithCrossAttentions as FlaxCausalLMOutputWithCrossAttentions, FlaxSeq2SeqLMOutput as FlaxSeq2SeqLMOutput, FlaxSeq2SeqModelOutput as FlaxSeq2SeqModelOutput
from ...modeling_flax_utils import ACT2FN as ACT2FN, FlaxPreTrainedModel as FlaxPreTrainedModel, append_call_sample_docstring as append_call_sample_docstring, append_replace_return_docstrings as append_replace_return_docstrings, overwrite_call_docstring as overwrite_call_docstring
from ...utils import add_start_docstrings as add_start_docstrings, add_start_docstrings_to_model_forward as add_start_docstrings_to_model_forward, logging as logging, replace_return_docstrings as replace_return_docstrings
from .configuration_longt5 import LongT5Config as LongT5Config
from _typeshed import Incomplete
from flax.core.frozen_dict import FrozenDict as FrozenDict
from jax.random import PRNGKey as PRNGKey
from typing import Any, Callable, Optional, Tuple

logger: Incomplete
remat: Incomplete

def shift_tokens_right(input_ids: np.array, pad_token_id: int, decoder_start_token_id: int) -> np.ndarray:
    """
    Shift input ids one token to the right.
    """

class FlaxLongT5LayerNorm(nn.Module):
    hidden_size: int
    dtype: jnp.dtype
    eps: float
    weight_init: Callable[..., np.ndarray]
    weight: Incomplete
    def setup(self) -> None: ...
    def __call__(self, hidden_states):
        """
        Construct a layernorm module in the LongT5 style; No bias and no subtraction of mean.
        """

class FlaxLongT5DenseActDense(nn.Module):
    config: LongT5Config
    dtype: jnp.dtype
    wi: Incomplete
    wo: Incomplete
    dropout: Incomplete
    act: Incomplete
    def setup(self) -> None: ...
    def __call__(self, hidden_states, deterministic: bool = True): ...

class FlaxLongT5DenseGatedActDense(nn.Module):
    config: LongT5Config
    dtype: jnp.dtype
    wi_0: Incomplete
    wi_1: Incomplete
    wo: Incomplete
    dropout: Incomplete
    act: Incomplete
    def setup(self) -> None: ...
    def __call__(self, hidden_states, deterministic): ...

class FlaxLongT5LayerFF(nn.Module):
    config: LongT5Config
    dtype: jnp.dtype
    DenseReluDense: Incomplete
    layer_norm: Incomplete
    dropout: Incomplete
    def setup(self) -> None: ...
    def __call__(self, hidden_states, deterministic: bool = True): ...

class FlaxLongT5Attention(nn.Module):
    config: LongT5Config
    has_relative_attention_bias: bool
    causal: bool
    dtype: jnp.dtype
    relative_attention_num_buckets: Incomplete
    relative_attention_max_distance: Incomplete
    d_model: Incomplete
    key_value_proj_dim: Incomplete
    n_heads: Incomplete
    dropout: Incomplete
    inner_dim: Incomplete
    q: Incomplete
    k: Incomplete
    v: Incomplete
    o: Incomplete
    relative_attention_bias: Incomplete
    def setup(self) -> None: ...
    def compute_bias(self, query_length, key_length):
        """Compute binned relative position bias"""
    def __call__(self, hidden_states, attention_mask: Incomplete | None = None, key_value_states: Incomplete | None = None, position_bias: Incomplete | None = None, use_cache: bool = False, output_attentions: bool = False, deterministic: bool = True, init_cache: bool = False):
        """
        Self-attention (if key_value_states is None) or attention over source sentence (provided by key_value_states).
        """

class FlaxLongT5LocalAttention(nn.Module):
    config: LongT5Config
    has_relative_attention_bias: bool
    dtype: jnp.dtype
    relative_attention_num_buckets: Incomplete
    relative_attention_max_distance: Incomplete
    d_model: Incomplete
    key_value_proj_dim: Incomplete
    n_heads: Incomplete
    local_radius: Incomplete
    block_len: Incomplete
    dropout: Incomplete
    inner_dim: Incomplete
    q: Incomplete
    k: Incomplete
    v: Incomplete
    o: Incomplete
    relative_attention_bias: Incomplete
    def setup(self) -> None: ...
    def compute_bias(self, block_length: int):
        """Compute binned relative position bias"""
    def __call__(self, hidden_states, attention_mask: Incomplete | None = None, key_value_states: Incomplete | None = None, position_bias: Incomplete | None = None, output_attentions: bool = False, deterministic: bool = True):
        """
        Self-attention (if key_value_states is None) or attention over source sentence (provided by key_value_states).
        """

class FlaxLongT5TransientGlobalAttention(nn.Module):
    config: LongT5Config
    has_relative_attention_bias: bool
    dtype: jnp.dtype
    relative_attention_num_buckets: Incomplete
    relative_attention_max_distance: Incomplete
    d_model: Incomplete
    key_value_proj_dim: Incomplete
    n_heads: Incomplete
    local_radius: Incomplete
    block_len: Incomplete
    global_block_size: Incomplete
    dropout: Incomplete
    inner_dim: Incomplete
    q: Incomplete
    k: Incomplete
    v: Incomplete
    o: Incomplete
    relative_attention_bias: Incomplete
    global_relative_attention_bias: Incomplete
    global_input_layer_norm: Incomplete
    def setup(self) -> None: ...
    def compute_bias(self, block_length: int):
        """Compute binned relative position bias"""
    def compute_side_bias(self, attention_mask: np.ndarray, global_segment_ids: np.ndarray) -> np.ndarray: ...
    def __call__(self, hidden_states, attention_mask: Incomplete | None = None, key_value_states: Incomplete | None = None, position_bias: Incomplete | None = None, output_attentions: bool = False, deterministic: bool = True):
        """
        Self-attention (if key_value_states is None) or attention over source sentence (provided by key_value_states).
        """

class FlaxLongT5LayerLocalSelfAttention(nn.Module):
    """Local self attention used in encoder"""
    config: LongT5Config
    has_relative_attention_bias: bool
    dtype: jnp.dtype
    LocalSelfAttention: Incomplete
    layer_norm: Incomplete
    dropout: Incomplete
    def setup(self) -> None: ...
    def __call__(self, hidden_states, attention_mask: Incomplete | None = None, position_bias: Incomplete | None = None, output_attentions: bool = False, deterministic: bool = True, **kwargs: Any): ...

class FlaxLongT5LayerTransientGlobalSelfAttention(nn.Module):
    """Transient-Global self attention used in encoder"""
    config: LongT5Config
    has_relative_attention_bias: bool
    dtype: jnp.dtype
    TransientGlobalSelfAttention: Incomplete
    layer_norm: Incomplete
    dropout: Incomplete
    def setup(self) -> None: ...
    def __call__(self, hidden_states, attention_mask: Incomplete | None = None, position_bias: Incomplete | None = None, output_attentions: bool = False, deterministic: bool = True, **kwargs: Any): ...

class FlaxLongT5LayerSelfAttention(nn.Module):
    config: LongT5Config
    has_relative_attention_bias: bool
    dtype: jnp.dtype
    SelfAttention: Incomplete
    layer_norm: Incomplete
    dropout: Incomplete
    def setup(self) -> None: ...
    def __call__(self, hidden_states, attention_mask: Incomplete | None = None, position_bias: Incomplete | None = None, output_attentions: bool = False, deterministic: bool = True, init_cache: bool = False): ...

class FlaxLongT5LayerCrossAttention(nn.Module):
    config: LongT5Config
    dtype: jnp.dtype
    EncDecAttention: Incomplete
    layer_norm: Incomplete
    dropout: Incomplete
    def setup(self) -> None: ...
    def __call__(self, hidden_states, key_value_states, attention_mask: Incomplete | None = None, position_bias: Incomplete | None = None, output_attentions: bool = False, deterministic: bool = True): ...

class FlaxLongT5Block(nn.Module):
    config: LongT5Config
    has_relative_attention_bias: bool
    dtype: jnp.dtype
    causal: Incomplete
    layer: Incomplete
    def setup(self) -> None: ...
    def __call__(self, hidden_states, attention_mask: Incomplete | None = None, position_bias: Incomplete | None = None, encoder_hidden_states: Incomplete | None = None, encoder_attention_mask: Incomplete | None = None, encoder_decoder_position_bias: Incomplete | None = None, output_attentions: bool = False, return_dict: bool = True, deterministic: bool = True, init_cache: bool = False): ...

class FlaxLongT5LayerCollection(nn.Module):
    config: LongT5Config
    has_relative_attention_bias: bool
    dtype: jnp.dtype
    layer: Incomplete
    def setup(self) -> None: ...
    def __call__(self, hidden_states, attention_mask: Incomplete | None = None, position_bias: Incomplete | None = None, encoder_hidden_states: Incomplete | None = None, encoder_attention_mask: Incomplete | None = None, encoder_decoder_position_bias: Incomplete | None = None, output_attentions: bool = False, deterministic: bool = True, init_cache: bool = False): ...

class FlaxLongT5BlockCollection(nn.Module):
    config: LongT5Config
    dtype: jnp.dtype
    gradient_checkpointing: bool
    causal: Incomplete
    blocks: Incomplete
    def setup(self) -> None: ...
    def __call__(self, hidden_states: Incomplete | None = None, attention_mask: Incomplete | None = None, encoder_hidden_states: Incomplete | None = None, encoder_attention_mask: Incomplete | None = None, output_attentions: bool = False, output_hidden_states: bool = False, deterministic: bool = True, init_cache: bool = False): ...

class FlaxLongT5Stack(nn.Module):
    config: LongT5Config
    embed_tokens: nn.Embed
    dtype: jnp.dtype
    gradient_checkpointing: bool
    causal: Incomplete
    block: Incomplete
    final_layer_norm: Incomplete
    dropout: Incomplete
    def setup(self) -> None: ...
    def __call__(self, input_ids: Incomplete | None = None, attention_mask: Incomplete | None = None, encoder_hidden_states: Incomplete | None = None, encoder_attention_mask: Incomplete | None = None, output_attentions: bool = False, output_hidden_states: bool = False, return_dict: bool = True, deterministic: bool = True, init_cache: bool = False): ...

LONGT5_ENCODE_INPUTS_DOCSTRING: str
LONGT5_DECODE_INPUTS_DOCSTRING: str
LONGT5_INPUTS_DOCSTRING: str

class FlaxLongT5PreTrainedModel(FlaxPreTrainedModel):
    """
    An abstract class to handle weights initialization and a simple interface for downloading and loading pretrained
    models.
    """
    config_class = LongT5Config
    base_model_prefix: str
    module_class: nn.Module
    def __init__(self, config: LongT5Config, input_shape: Tuple[int] = (1, 1), seed: int = 0, dtype: jnp.dtype = ..., _do_init: bool = True, **kwargs) -> None: ...
    def enable_gradient_checkpointing(self) -> None: ...
    def init_weights(self, rng: jax.random.PRNGKey, input_shape: Tuple, params: FrozenDict = None) -> FrozenDict: ...
    def __call__(self, input_ids: jnp.ndarray, attention_mask: Optional[jnp.ndarray] = None, decoder_input_ids: jnp.ndarray = None, decoder_attention_mask: Optional[jnp.ndarray] = None, output_attentions: Optional[bool] = None, output_hidden_states: Optional[bool] = None, return_dict: Optional[bool] = None, train: bool = False, params: dict = None, dropout_rng: PRNGKey = None): ...
    def init_cache(self, batch_size, max_length, encoder_outputs):
        """
        Args:
            batch_size (`int`):
                batch_size used for fast auto-regressive decoding. Defines the batch size of the initialized cache.
            max_length (`int`):
                maximum possible length for auto-regressive decoding. Defines the sequence length of the initialized
                cache.
            encoder_outputs (`Union[FlaxBaseModelOutput, tuple(tuple(jnp.ndarray)]`):
                `encoder_outputs` consists of (`last_hidden_state`, *optional*: `hidden_states`, *optional*:
                `attentions`). `last_hidden_state` of shape `(batch_size, sequence_length, hidden_size)`, *optional*)
                is a sequence of hidden-states at the output of the last layer of the encoder. Used in the
                cross-attention of the decoder.
        """
    def encode(self, input_ids: jnp.ndarray, attention_mask: Optional[jnp.ndarray] = None, output_attentions: Optional[bool] = None, output_hidden_states: Optional[bool] = None, return_dict: Optional[bool] = None, train: bool = False, params: dict = None, dropout_rng: PRNGKey = None):
        '''
        Returns:

        Example:

        ```python
        >>> from transformers import AutoTokenizer, FlaxLongT5ForConditionalGeneration

        >>> tokenizer = AutoTokenizer.from_pretrained("t5-base")
        >>> model = FlaxLongT5ForConditionalGeneration.from_pretrained("google/long-t5-local-base")

        >>> text = "My friends are cool but they eat too many carbs."
        >>> inputs = tokenizer(text, return_tensors="np")
        >>> encoder_outputs = model.encode(**inputs)
        ```'''
    def decode(self, decoder_input_ids, encoder_outputs, encoder_attention_mask: Optional[jnp.ndarray] = None, decoder_attention_mask: Optional[jnp.ndarray] = None, past_key_values: dict = None, output_attentions: Optional[bool] = None, output_hidden_states: Optional[bool] = None, return_dict: Optional[bool] = None, train: bool = False, params: dict = None, dropout_rng: PRNGKey = None):
        '''
        Returns:

        Example:

        ```python
        >>> from transformers import AutoTokenizer, FlaxLongT5ForConditionalGeneration
        >>> import jax.numpy as jnp

        >>> tokenizer = AutoTokenizer.from_pretrained("t5-base")
        >>> model = FlaxLongT5ForConditionalGeneration.from_pretrained("google/long-t5-local-base")

        >>> text = "My friends are cool but they eat too many carbs."
        >>> inputs = tokenizer(text, return_tensors="np")
        >>> encoder_outputs = model.encode(**inputs)

        >>> decoder_start_token_id = model.config.decoder_start_token_id
        >>> decoder_input_ids = jnp.ones((inputs.input_ids.shape[0], 1), dtype="i4") * decoder_start_token_id

        >>> outputs = model.decode(decoder_input_ids, encoder_outputs)
        >>> logits = outputs.logits
        ```'''

LONGT5_START_DOCSTRING: str

class FlaxLongT5Module(nn.Module):
    config: LongT5Config
    dtype: jnp.dtype
    gradient_checkpointing: bool
    shared: Incomplete
    encoder: Incomplete
    decoder: Incomplete
    def setup(self) -> None: ...
    def __call__(self, input_ids: Incomplete | None = None, attention_mask: Incomplete | None = None, decoder_input_ids: Incomplete | None = None, decoder_attention_mask: Incomplete | None = None, encoder_outputs: Incomplete | None = None, output_attentions: Incomplete | None = None, output_hidden_states: Incomplete | None = None, return_dict: Incomplete | None = None, deterministic: bool = True): ...

class FlaxLongT5Model(FlaxLongT5PreTrainedModel):
    module_class = FlaxLongT5Module

FLAX_LONGT5_MODEL_DOCSTRING: str

class FlaxLongT5ForConditionalGenerationModule(nn.Module):
    config: LongT5Config
    dtype: jnp.dtype
    gradient_checkpointing: bool
    model_dim: Incomplete
    shared: Incomplete
    encoder: Incomplete
    decoder: Incomplete
    lm_head: Incomplete
    def setup(self) -> None: ...
    def __call__(self, input_ids: Incomplete | None = None, attention_mask: Incomplete | None = None, decoder_input_ids: Incomplete | None = None, decoder_attention_mask: Incomplete | None = None, encoder_outputs: Incomplete | None = None, output_attentions: Incomplete | None = None, output_hidden_states: Incomplete | None = None, return_dict: Incomplete | None = None, deterministic: bool = True): ...

class FlaxLongT5ForConditionalGeneration(FlaxLongT5PreTrainedModel):
    module_class = FlaxLongT5ForConditionalGenerationModule
    def decode(self, decoder_input_ids, encoder_outputs, encoder_attention_mask: Optional[jnp.ndarray] = None, decoder_attention_mask: Optional[jnp.ndarray] = None, past_key_values: dict = None, output_attentions: Optional[bool] = None, output_hidden_states: Optional[bool] = None, return_dict: Optional[bool] = None, train: bool = False, params: dict = None, dropout_rng: PRNGKey = None):
        '''
        Returns:

        Example:

        ```python
        >>> from transformers import AutoTokenizer, FlaxLongT5ForConditionalGeneration
        >>> import jax.numpy as jnp

        >>> tokenizer = AutoTokenizer.from_pretrained("t5-base")
        >>> model = FlaxLongT5ForConditionalGeneration.from_pretrained("google/long-t5-local-base")

        >>> text = "summarize: My friends are cool but they eat too many carbs."
        >>> inputs = tokenizer(text, return_tensors="np")
        >>> encoder_outputs = model.encode(**inputs)

        >>> decoder_start_token_id = model.config.decoder_start_token_id
        >>> decoder_input_ids = jnp.ones((inputs.input_ids.shape[0], 1), dtype="i4") * decoder_start_token_id

        >>> outputs = model.decode(decoder_input_ids, encoder_outputs)
        >>> logits = outputs.logits
        ```'''
    def prepare_inputs_for_generation(self, decoder_input_ids, max_length, attention_mask: Optional[jnp.DeviceArray] = None, decoder_attention_mask: Optional[jnp.DeviceArray] = None, encoder_outputs: Incomplete | None = None, **kwargs): ...
    def update_inputs_for_generation(self, model_outputs, model_kwargs): ...

FLAX_LONGT5_CONDITIONAL_GENERATION_DOCSTRING: str
