import flax.linen as nn
import jax
import jax.numpy as jnp
from ...modeling_flax_outputs import FlaxBaseModelOutput as FlaxBaseModelOutput, FlaxBaseModelOutputWithPastAndCrossAttentions as FlaxBaseModelOutputWithPastAndCrossAttentions, FlaxCausalLMOutputWithCrossAttentions as FlaxCausalLMOutputWithCrossAttentions, FlaxSeq2SeqLMOutput as FlaxSeq2SeqLMOutput, FlaxSeq2SeqModelOutput as FlaxSeq2SeqModelOutput
from ...modeling_flax_utils import ACT2FN as ACT2FN, FlaxPreTrainedModel as FlaxPreTrainedModel, append_call_sample_docstring as append_call_sample_docstring, append_replace_return_docstrings as append_replace_return_docstrings, overwrite_call_docstring as overwrite_call_docstring
from ...utils import add_start_docstrings as add_start_docstrings, add_start_docstrings_to_model_forward as add_start_docstrings_to_model_forward, logging as logging, replace_return_docstrings as replace_return_docstrings
from .configuration_marian import MarianConfig as MarianConfig
from _typeshed import Incomplete
from flax.core.frozen_dict import FrozenDict as FrozenDict
from jax.random import PRNGKey as PRNGKey
from typing import Callable, Optional, Tuple

logger: Incomplete
MARIAN_START_DOCSTRING: str
MARIAN_INPUTS_DOCSTRING: str
MARIAN_ENCODE_INPUTS_DOCSTRING: str
MARIAN_DECODE_INPUTS_DOCSTRING: str

def create_sinusoidal_positions(n_pos, dim): ...
def shift_tokens_right(input_ids: jnp.ndarray, pad_token_id: int, decoder_start_token_id: int) -> jnp.ndarray:
    """
    Shift input ids one token to the right.
    """

class FlaxMarianAttention(nn.Module):
    config: MarianConfig
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

class FlaxMarianEncoderLayer(nn.Module):
    config: MarianConfig
    dtype: jnp.dtype
    embed_dim: Incomplete
    self_attn: Incomplete
    self_attn_layer_norm: Incomplete
    dropout_layer: Incomplete
    activation_fn: Incomplete
    activation_dropout_layer: Incomplete
    fc1: Incomplete
    fc2: Incomplete
    final_layer_norm: Incomplete
    def setup(self) -> None: ...
    def __call__(self, hidden_states: jnp.ndarray, attention_mask: jnp.ndarray, output_attentions: bool = True, deterministic: bool = True) -> Tuple[jnp.ndarray]: ...

class FlaxMarianEncoderLayerCollection(nn.Module):
    config: MarianConfig
    dtype: jnp.dtype
    layers: Incomplete
    layerdrop: Incomplete
    def setup(self) -> None: ...
    def __call__(self, hidden_states, attention_mask, deterministic: bool = True, output_attentions: bool = False, output_hidden_states: bool = False, return_dict: bool = True): ...

class FlaxMarianDecoderLayer(nn.Module):
    config: MarianConfig
    dtype: jnp.dtype
    embed_dim: Incomplete
    self_attn: Incomplete
    dropout_layer: Incomplete
    activation_fn: Incomplete
    activation_dropout_layer: Incomplete
    self_attn_layer_norm: Incomplete
    encoder_attn: Incomplete
    encoder_attn_layer_norm: Incomplete
    fc1: Incomplete
    fc2: Incomplete
    final_layer_norm: Incomplete
    def setup(self) -> None: ...
    def __call__(self, hidden_states: jnp.ndarray, attention_mask: jnp.ndarray, encoder_hidden_states: Optional[jnp.ndarray] = None, encoder_attention_mask: Optional[jnp.ndarray] = None, init_cache: bool = False, output_attentions: bool = True, deterministic: bool = True) -> Tuple[jnp.ndarray]: ...

class FlaxMarianDecoderLayerCollection(nn.Module):
    config: MarianConfig
    dtype: jnp.dtype
    layers: Incomplete
    layerdrop: Incomplete
    def setup(self) -> None: ...
    def __call__(self, hidden_states, attention_mask, encoder_hidden_states: Optional[jnp.ndarray] = None, encoder_attention_mask: Optional[jnp.ndarray] = None, deterministic: bool = True, init_cache: bool = False, output_attentions: bool = False, output_hidden_states: bool = False, return_dict: bool = True): ...

class FlaxMarianEncoder(nn.Module):
    config: MarianConfig
    embed_tokens: nn.Embed
    dtype: jnp.dtype
    dropout_layer: Incomplete
    max_source_positions: Incomplete
    embed_scale: Incomplete
    embed_positions: Incomplete
    layers: Incomplete
    def setup(self) -> None: ...
    def __call__(self, input_ids, attention_mask, position_ids, output_attentions: bool = False, output_hidden_states: bool = False, return_dict: bool = True, deterministic: bool = True): ...

class FlaxMarianDecoder(nn.Module):
    config: MarianConfig
    embed_tokens: nn.Embed
    dtype: jnp.dtype
    dropout_layer: Incomplete
    max_target_positions: Incomplete
    embed_scale: Incomplete
    embed_positions: Incomplete
    layers: Incomplete
    def setup(self) -> None: ...
    def __call__(self, input_ids, attention_mask, position_ids, encoder_hidden_states: Optional[jnp.ndarray] = None, encoder_attention_mask: Optional[jnp.ndarray] = None, init_cache: bool = False, output_attentions: bool = False, output_hidden_states: bool = False, return_dict: bool = True, deterministic: bool = True): ...

class FlaxMarianModule(nn.Module):
    config: MarianConfig
    dtype: jnp.dtype
    shared: Incomplete
    encoder: Incomplete
    decoder: Incomplete
    def setup(self) -> None: ...
    def __call__(self, input_ids, attention_mask, decoder_input_ids, decoder_attention_mask, position_ids, decoder_position_ids, output_attentions: bool = False, output_hidden_states: bool = False, return_dict: bool = True, deterministic: bool = True): ...

class FlaxMarianPreTrainedModel(FlaxPreTrainedModel):
    config_class = MarianConfig
    base_model_prefix: str
    module_class: nn.Module
    def __init__(self, config: MarianConfig, input_shape: Tuple[int] = (1, 1), seed: int = 0, dtype: jnp.dtype = ..., _do_init: bool = True, **kwargs) -> None: ...
    def init_weights(self, rng: jax.random.PRNGKey, input_shape: Tuple, params: FrozenDict = None) -> FrozenDict: ...
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
    def encode(self, input_ids: jnp.ndarray, attention_mask: Optional[jnp.ndarray] = None, position_ids: Optional[jnp.ndarray] = None, output_attentions: Optional[bool] = None, output_hidden_states: Optional[bool] = None, return_dict: Optional[bool] = None, train: bool = False, params: dict = None, dropout_rng: PRNGKey = None):
        '''
        Returns:

        Example:

        ```python
        >>> from transformers import AutoTokenizer, FlaxMarianMTModel

        >>> tokenizer = AutoTokenizer.from_pretrained("Helsinki-NLP/opus-mt-en-de")
        >>> model = FlaxMarianMTModel.from_pretrained("Helsinki-NLP/opus-mt-en-de")

        >>> text = "My friends are cool but they eat too many carbs."
        >>> inputs = tokenizer(text, max_length=64, return_tensors="jax")
        >>> encoder_outputs = model.encode(**inputs)
        ```'''
    def decode(self, decoder_input_ids, encoder_outputs, encoder_attention_mask: Optional[jnp.ndarray] = None, decoder_attention_mask: Optional[jnp.ndarray] = None, decoder_position_ids: Optional[jnp.ndarray] = None, past_key_values: dict = None, output_attentions: Optional[bool] = None, output_hidden_states: Optional[bool] = None, return_dict: Optional[bool] = None, train: bool = False, params: dict = None, dropout_rng: PRNGKey = None):
        '''
        Returns:

        Example:

        ```python
        >>> import jax.numpy as jnp
        >>> from transformers import AutoTokenizer, FlaxMarianMTModel

        >>> tokenizer = AutoTokenizer.from_pretrained("Helsinki-NLP/opus-mt-en-de")
        >>> model = FlaxMarianMTModel.from_pretrained("Helsinki-NLP/opus-mt-en-de")

        >>> text = "My friends are cool but they eat too many carbs."
        >>> inputs = tokenizer(text, max_length=64, return_tensors="jax")
        >>> encoder_outputs = model.encode(**inputs)

        >>> decoder_start_token_id = model.config.decoder_start_token_id
        >>> decoder_input_ids = jnp.ones((inputs.input_ids.shape[0], 1), dtype="i4") * decoder_start_token_id

        >>> outputs = model.decode(decoder_input_ids, encoder_outputs)
        >>> last_decoder_hidden_states = outputs.last_hidden_state
        ```'''
    def __call__(self, input_ids: jnp.ndarray, attention_mask: Optional[jnp.ndarray] = None, decoder_input_ids: Optional[jnp.ndarray] = None, decoder_attention_mask: Optional[jnp.ndarray] = None, position_ids: Optional[jnp.ndarray] = None, decoder_position_ids: Optional[jnp.ndarray] = None, output_attentions: Optional[bool] = None, output_hidden_states: Optional[bool] = None, return_dict: Optional[bool] = None, train: bool = False, params: dict = None, dropout_rng: PRNGKey = None): ...

class FlaxMarianModel(FlaxMarianPreTrainedModel):
    config: MarianConfig
    dtype: jnp.dtype
    module_class = FlaxMarianModule

class FlaxMarianMTModule(nn.Module):
    config: MarianConfig
    dtype: jnp.dtype
    bias_init: Callable[..., jnp.ndarray]
    model: Incomplete
    lm_head: Incomplete
    final_logits_bias: Incomplete
    def setup(self) -> None: ...
    def __call__(self, input_ids, attention_mask, decoder_input_ids, decoder_attention_mask, position_ids, decoder_position_ids, output_attentions: bool = False, output_hidden_states: bool = False, return_dict: bool = True, deterministic: bool = True): ...

class FlaxMarianMTModel(FlaxMarianPreTrainedModel):
    module_class = FlaxMarianMTModule
    dtype: jnp.dtype
    def decode(self, decoder_input_ids, encoder_outputs, encoder_attention_mask: Optional[jnp.ndarray] = None, decoder_attention_mask: Optional[jnp.ndarray] = None, decoder_position_ids: Optional[jnp.ndarray] = None, past_key_values: dict = None, output_attentions: Optional[bool] = None, output_hidden_states: Optional[bool] = None, return_dict: Optional[bool] = None, train: bool = False, params: dict = None, dropout_rng: PRNGKey = None):
        '''
        Returns:

        Example:

        ```python
        >>> import jax.numpy as jnp
        >>> from transformers import AutoTokenizer, FlaxMarianMTModel

        >>> model = FlaxMarianMTModel.from_pretrained("Helsinki-NLP/opus-mt-en-de")
        >>> tokenizer = AutoTokenizer.from_pretrained("Helsinki-NLP/opus-mt-en-de")

        >>> text = "My friends are cool but they eat too many carbs."
        >>> inputs = tokenizer(text, max_length=64, return_tensors="jax")
        >>> encoder_outputs = model.encode(**inputs)

        >>> decoder_start_token_id = model.config.decoder_start_token_id
        >>> decoder_input_ids = jnp.ones((inputs.input_ids.shape[0], 1), dtype="i4") * decoder_start_token_id

        >>> outputs = model.decode(decoder_input_ids, encoder_outputs)
        >>> logits = outputs.logits
        ```'''
    def prepare_inputs_for_generation(self, decoder_input_ids, max_length, attention_mask: Optional[jnp.DeviceArray] = None, decoder_attention_mask: Optional[jnp.DeviceArray] = None, encoder_outputs: Incomplete | None = None, **kwargs): ...
    def update_inputs_for_generation(self, model_outputs, model_kwargs): ...

FLAX_MARIAN_MT_DOCSTRING: str
