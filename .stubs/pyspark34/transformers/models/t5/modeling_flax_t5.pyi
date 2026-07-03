import flax.linen as nn
import jax
import jax.numpy as jnp
import numpy as np
from ...modeling_flax_outputs import FlaxBaseModelOutput as FlaxBaseModelOutput, FlaxBaseModelOutputWithPastAndCrossAttentions as FlaxBaseModelOutputWithPastAndCrossAttentions, FlaxCausalLMOutputWithCrossAttentions as FlaxCausalLMOutputWithCrossAttentions, FlaxSeq2SeqLMOutput as FlaxSeq2SeqLMOutput, FlaxSeq2SeqModelOutput as FlaxSeq2SeqModelOutput
from ...modeling_flax_utils import ACT2FN as ACT2FN, FlaxPreTrainedModel as FlaxPreTrainedModel, append_call_sample_docstring as append_call_sample_docstring, append_replace_return_docstrings as append_replace_return_docstrings, overwrite_call_docstring as overwrite_call_docstring
from ...utils import add_start_docstrings as add_start_docstrings, add_start_docstrings_to_model_forward as add_start_docstrings_to_model_forward, logging as logging, replace_return_docstrings as replace_return_docstrings
from .configuration_t5 import T5Config as T5Config
from _typeshed import Incomplete
from flax.core.frozen_dict import FrozenDict as FrozenDict
from jax.random import PRNGKey as PRNGKey
from typing import Callable, Optional, Tuple

logger: Incomplete
remat: Incomplete

def shift_tokens_right(input_ids: np.array, pad_token_id: int, decoder_start_token_id: int) -> np.ndarray:
    """
    Shift input ids one token to the right.
    """

class FlaxT5LayerNorm(nn.Module):
    hidden_size: int
    dtype: jnp.dtype
    eps: float
    weight_init: Callable[..., np.ndarray]
    weight: Incomplete
    def setup(self) -> None: ...
    def __call__(self, hidden_states):
        """
        Construct a layernorm module in the T5 style; No bias and no subtraction of mean.
        """

class FlaxT5DenseActDense(nn.Module):
    config: T5Config
    dtype: jnp.dtype
    wi: Incomplete
    wo: Incomplete
    dropout: Incomplete
    act: Incomplete
    def setup(self) -> None: ...
    def __call__(self, hidden_states, deterministic: bool = True): ...

class FlaxT5DenseGatedActDense(nn.Module):
    config: T5Config
    dtype: jnp.dtype
    wi_0: Incomplete
    wi_1: Incomplete
    wo: Incomplete
    dropout: Incomplete
    act: Incomplete
    def setup(self) -> None: ...
    def __call__(self, hidden_states, deterministic): ...

class FlaxT5LayerFF(nn.Module):
    config: T5Config
    dtype: jnp.dtype
    DenseReluDense: Incomplete
    layer_norm: Incomplete
    dropout: Incomplete
    def setup(self) -> None: ...
    def __call__(self, hidden_states, deterministic: bool = True): ...

class FlaxT5Attention(nn.Module):
    config: T5Config
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

class FlaxT5LayerSelfAttention(nn.Module):
    config: T5Config
    has_relative_attention_bias: bool
    dtype: jnp.dtype
    SelfAttention: Incomplete
    layer_norm: Incomplete
    dropout: Incomplete
    def setup(self) -> None: ...
    def __call__(self, hidden_states, attention_mask: Incomplete | None = None, position_bias: Incomplete | None = None, output_attentions: bool = False, deterministic: bool = True, init_cache: bool = False): ...

class FlaxT5LayerCrossAttention(nn.Module):
    config: T5Config
    dtype: jnp.dtype
    EncDecAttention: Incomplete
    layer_norm: Incomplete
    dropout: Incomplete
    def setup(self) -> None: ...
    def __call__(self, hidden_states, key_value_states, attention_mask: Incomplete | None = None, position_bias: Incomplete | None = None, output_attentions: bool = False, deterministic: bool = True): ...

class FlaxT5Block(nn.Module):
    config: T5Config
    has_relative_attention_bias: bool
    dtype: jnp.dtype
    causal: Incomplete
    layer: Incomplete
    def setup(self) -> None: ...
    def __call__(self, hidden_states, attention_mask: Incomplete | None = None, position_bias: Incomplete | None = None, encoder_hidden_states: Incomplete | None = None, encoder_attention_mask: Incomplete | None = None, encoder_decoder_position_bias: Incomplete | None = None, output_attentions: bool = False, return_dict: bool = True, deterministic: bool = True, init_cache: bool = False): ...

class FlaxT5LayerCollection(nn.Module):
    config: T5Config
    has_relative_attention_bias: bool
    dtype: jnp.dtype
    layer: Incomplete
    def setup(self) -> None: ...
    def __call__(self, hidden_states, attention_mask: Incomplete | None = None, position_bias: Incomplete | None = None, encoder_hidden_states: Incomplete | None = None, encoder_attention_mask: Incomplete | None = None, encoder_decoder_position_bias: Incomplete | None = None, output_attentions: bool = False, deterministic: bool = True, init_cache: bool = False): ...

class FlaxT5BlockCollection(nn.Module):
    config: T5Config
    dtype: jnp.dtype
    gradient_checkpointing: bool
    causal: Incomplete
    blocks: Incomplete
    def setup(self) -> None: ...
    def __call__(self, hidden_states: Incomplete | None = None, attention_mask: Incomplete | None = None, encoder_hidden_states: Incomplete | None = None, encoder_attention_mask: Incomplete | None = None, output_attentions: bool = False, output_hidden_states: bool = False, deterministic: bool = True, init_cache: bool = False): ...

class FlaxT5Stack(nn.Module):
    config: T5Config
    embed_tokens: nn.Embed
    dtype: jnp.dtype
    gradient_checkpointing: bool
    causal: Incomplete
    block: Incomplete
    final_layer_norm: Incomplete
    dropout: Incomplete
    def setup(self) -> None: ...
    def __call__(self, input_ids: Incomplete | None = None, attention_mask: Incomplete | None = None, encoder_hidden_states: Incomplete | None = None, encoder_attention_mask: Incomplete | None = None, output_attentions: bool = False, output_hidden_states: bool = False, return_dict: bool = True, deterministic: bool = True, init_cache: bool = False): ...

T5_ENCODE_INPUTS_DOCSTRING: str
T5_DECODE_INPUTS_DOCSTRING: str
T5_INPUTS_DOCSTRING: str

class FlaxT5PreTrainedModel(FlaxPreTrainedModel):
    """
    An abstract class to handle weights initialization and a simple interface for downloading and loading pretrained
    models.
    """
    config_class = T5Config
    base_model_prefix: str
    module_class: nn.Module
    def __init__(self, config: T5Config, input_shape: Tuple[int] = (1, 1), seed: int = 0, dtype: jnp.dtype = ..., _do_init: bool = True, gradient_checkpointing: bool = False, **kwargs) -> None: ...
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
        >>> from transformers import AutoTokenizer, FlaxT5ForConditionalGeneration

        >>> tokenizer = AutoTokenizer.from_pretrained("t5-small")
        >>> model = FlaxT5ForConditionalGeneration.from_pretrained("t5-small")

        >>> text = "My friends are cool but they eat too many carbs."
        >>> inputs = tokenizer(text, return_tensors="np")
        >>> encoder_outputs = model.encode(**inputs)
        ```'''
    def decode(self, decoder_input_ids, encoder_outputs, encoder_attention_mask: Optional[jnp.ndarray] = None, decoder_attention_mask: Optional[jnp.ndarray] = None, past_key_values: dict = None, output_attentions: Optional[bool] = None, output_hidden_states: Optional[bool] = None, return_dict: Optional[bool] = None, train: bool = False, params: dict = None, dropout_rng: PRNGKey = None):
        '''
        Returns:

        Example:

        ```python
        >>> from transformers import AutoTokenizer, FlaxT5ForConditionalGeneration
        >>> import jax.numpy as jnp

        >>> tokenizer = AutoTokenizer.from_pretrained("t5-small")
        >>> model = FlaxT5ForConditionalGeneration.from_pretrained("t5-small")

        >>> text = "My friends are cool but they eat too many carbs."
        >>> inputs = tokenizer(text, return_tensors="np")
        >>> encoder_outputs = model.encode(**inputs)

        >>> decoder_start_token_id = model.config.decoder_start_token_id
        >>> decoder_input_ids = jnp.ones((inputs.input_ids.shape[0], 1), dtype="i4") * decoder_start_token_id

        >>> outputs = model.decode(decoder_input_ids, encoder_outputs)
        >>> logits = outputs.logits
        ```'''

T5_START_DOCSTRING: str

class FlaxT5Module(nn.Module):
    config: T5Config
    dtype: jnp.dtype
    gradient_checkpointing: bool
    shared: Incomplete
    encoder: Incomplete
    decoder: Incomplete
    def setup(self) -> None: ...
    def __call__(self, input_ids: Incomplete | None = None, attention_mask: Incomplete | None = None, decoder_input_ids: Incomplete | None = None, decoder_attention_mask: Incomplete | None = None, encoder_outputs: Incomplete | None = None, output_attentions: Incomplete | None = None, output_hidden_states: Incomplete | None = None, return_dict: Incomplete | None = None, deterministic: bool = True): ...

class FlaxT5Model(FlaxT5PreTrainedModel):
    module_class = FlaxT5Module

FLAX_T5_MODEL_DOCSTRING: str

class FlaxT5EncoderModule(nn.Module):
    config: T5Config
    dtype: jnp.dtype
    gradient_checkpointing: bool
    shared: Incomplete
    encoder: Incomplete
    def setup(self) -> None: ...
    def __call__(self, input_ids: Incomplete | None = None, attention_mask: Incomplete | None = None, output_attentions: bool = False, output_hidden_states: bool = False, return_dict: bool = True, deterministic: bool = True): ...

class FlaxT5EncoderModel(FlaxT5PreTrainedModel):
    module_class = FlaxT5EncoderModule
    def __call__(self, input_ids: jnp.ndarray, attention_mask: Optional[jnp.ndarray] = None, output_attentions: Optional[bool] = None, output_hidden_states: Optional[bool] = None, return_dict: Optional[bool] = None, train: bool = False, params: dict = None, dropout_rng: PRNGKey = None): ...

class FlaxT5ForConditionalGenerationModule(nn.Module):
    config: T5Config
    dtype: jnp.dtype
    gradient_checkpointing: bool
    model_dim: Incomplete
    shared: Incomplete
    encoder: Incomplete
    decoder: Incomplete
    lm_head: Incomplete
    def setup(self) -> None: ...
    def __call__(self, input_ids: Incomplete | None = None, attention_mask: Incomplete | None = None, decoder_input_ids: Incomplete | None = None, decoder_attention_mask: Incomplete | None = None, encoder_outputs: Incomplete | None = None, output_attentions: Incomplete | None = None, output_hidden_states: Incomplete | None = None, return_dict: Incomplete | None = None, deterministic: bool = True): ...

class FlaxT5ForConditionalGeneration(FlaxT5PreTrainedModel):
    module_class = FlaxT5ForConditionalGenerationModule
    def decode(self, decoder_input_ids, encoder_outputs, encoder_attention_mask: Optional[jnp.ndarray] = None, decoder_attention_mask: Optional[jnp.ndarray] = None, past_key_values: dict = None, output_attentions: Optional[bool] = None, output_hidden_states: Optional[bool] = None, return_dict: Optional[bool] = None, train: bool = False, params: dict = None, dropout_rng: PRNGKey = None):
        '''
        Returns:

        Example:

        ```python
        >>> from transformers import AutoTokenizer, FlaxT5ForConditionalGeneration
        >>> import jax.numpy as jnp

        >>> tokenizer = AutoTokenizer.from_pretrained("t5-small")
        >>> model = FlaxT5ForConditionalGeneration.from_pretrained("t5-small")

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

FLAX_T5_CONDITIONAL_GENERATION_DOCSTRING: str
