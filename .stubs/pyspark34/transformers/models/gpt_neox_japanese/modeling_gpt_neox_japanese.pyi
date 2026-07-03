import torch
from ...activations import ACT2FN as ACT2FN
from ...file_utils import add_start_docstrings as add_start_docstrings, add_start_docstrings_to_model_forward as add_start_docstrings_to_model_forward, replace_return_docstrings as replace_return_docstrings
from ...modeling_outputs import BaseModelOutputWithPast as BaseModelOutputWithPast, CausalLMOutputWithPast as CausalLMOutputWithPast
from ...modeling_utils import PreTrainedModel as PreTrainedModel
from ...utils import logging as logging
from .configuration_gpt_neox_japanese import GPTNeoXJapaneseConfig as GPTNeoXJapaneseConfig
from _typeshed import Incomplete
from torch import Tensor as Tensor, nn
from typing import Optional, Tuple, Union

logger: Incomplete
GPT_NEOX_JAPANESE_PRETRAINED_MODEL_ARCHIVE_LIST: Incomplete

class GPTNeoXJapanesePreTrainedModel(PreTrainedModel):
    """
    An abstract class to handle weights initialization and a simple interface for downloading and loading pretrained
    models.
    """
    config_class = GPTNeoXJapaneseConfig
    base_model_prefix: str
    supports_gradient_checkpointing: bool

class GPTNeoXJapaneseAttention(nn.Module):
    num_attention_heads: Incomplete
    hidden_size: Incomplete
    head_size: Incomplete
    rotary_ndims: Incomplete
    rotary_emb: Incomplete
    max_positions: Incomplete
    attention_dropout: Incomplete
    norm_factor: Incomplete
    query_key_value: Incomplete
    dense: Incomplete
    use_bias: Incomplete
    dense_bias: Incomplete
    def __init__(self, config, use_bias: bool = False) -> None: ...
    def forward(self, hidden_states, attention_mask, head_mask: Incomplete | None = None, layer_past: Incomplete | None = None, use_cache: bool = False, output_attentions: bool = False): ...

class RotaryEmbedding(torch.nn.Module):
    max_seq_len_cached: Incomplete
    cos_cached: Incomplete
    sin_cached: Incomplete
    def __init__(self, dim, max_position_embeddings, base: int = 10000, device: Incomplete | None = None) -> None: ...
    def forward(self, x, seq_len: Incomplete | None = None): ...

def rotate_half(x):
    """Rotates half the hidden dims of the input."""
def apply_rotary_pos_emb(q, k, cos, sin, offset: int = 0): ...
def bias_dropout_add(x: Tensor, bias: Tensor, residual: Optional[Tensor], prob: float, training: bool) -> Tensor:
    """add bias to x, apply dropout and residual connection

    Args:
        x (Tensor): main path of output
        bias (Tensor): None or attn_bias of the last attention layer
        residual (Optional[Tensor]): residual value
        prob (float): dropout probability
        training (bool): whether in training mode or not

    Returns:
        Tensor: dropout(x + bias) + residual
    """

class GPTNeoXJapaneseMLP(nn.Module):
    dense_h_to_4h: Incomplete
    dense_4h_to_h: Incomplete
    act: Incomplete
    def __init__(self, config) -> None: ...
    def forward(self, hidden_states): ...

class GPTNeoXJapaneseLayer(nn.Module):
    layer_number: Incomplete
    input_layernorm: Incomplete
    post_attention_layernorm: Incomplete
    attention: Incomplete
    mlp: Incomplete
    hidden_dropout: Incomplete
    def __init__(self, config, layer_number) -> None: ...
    def forward(self, hidden_states, attention_mask: Incomplete | None = None, head_mask: Incomplete | None = None, use_cache: bool = False, layer_past: Incomplete | None = None, output_attentions: bool = False): ...

GPT_NEOX_JAPANESE_START_DOCSTRING: str
GPT_NEOX_JAPANESE_INPUTS_DOCSTRING: str

class GPTNeoXJapaneseModel(GPTNeoXJapanesePreTrainedModel):
    config: Incomplete
    embed_in: Incomplete
    layers: Incomplete
    final_layer_norm: Incomplete
    def __init__(self, config) -> None: ...
    def get_input_embeddings(self): ...
    def set_input_embeddings(self, value) -> None: ...
    def forward(self, input_ids: Optional[torch.LongTensor] = None, attention_mask: Optional[torch.FloatTensor] = None, head_mask: Optional[torch.FloatTensor] = None, inputs_embeds: Optional[torch.FloatTensor] = None, past_key_values: Optional[Tuple[Tuple[torch.FloatTensor]]] = None, use_cache: Optional[bool] = None, output_attentions: Optional[bool] = None, output_hidden_states: Optional[bool] = None, return_dict: Optional[bool] = None) -> Union[Tuple, BaseModelOutputWithPast]:
        '''
        past_key_values (`tuple(tuple(torch.FloatTensor))` of length `config.n_layers` with each tuple having 4 tensors of shape `(batch_size, num_heads, sequence_length - 1, embed_size_per_head)`):
            Contains precomputed key and value hidden states of the attention blocks. Can be used to speed up decoding.
            If `past_key_values` are used, the user can optionally input only the last `decoder_input_ids` (those that
            don\'t have their past key value states given to this model) of shape `(batch_size, 1)` instead of all
            `decoder_input_ids` of shape `(batch_size, sequence_length)`.
        use_cache (`bool`, *optional*):
            If set to `True`, `past_key_values` key value states are returned and can be used to speed up decoding (see
            `past_key_values`).

        Returns:

        Example:

        ```python
        >>> from transformers import AutoTokenizer, GPTNeoXJapaneseModel
        >>> import torch

        >>> tokenizer = AutoTokenizer.from_pretrained("abeja/gpt-neox-japanese-2.7b")
        >>> model = GPTNeoXJapaneseModel.from_pretrained("abeja/gpt-neox-japanese-2.7b")

        >>> inputs = tokenizer("日本語のGPT-neoxがHugging Faceで使えます😀", return_tensors="pt")
        >>> outputs = model(**inputs)

        >>> last_hidden_states = outputs.last_hidden_state
        ```
        '''

class GPTNeoXJapaneseForCausalLM(GPTNeoXJapanesePreTrainedModel):
    config: Incomplete
    gpt_neox_japanese: Incomplete
    embed_out: Incomplete
    def __init__(self, config) -> None: ...
    def get_output_embeddings(self): ...
    def set_output_embeddings(self, new_embeddings) -> None: ...
    def forward(self, input_ids: Optional[torch.LongTensor] = None, attention_mask: Optional[torch.FloatTensor] = None, inputs_embeds: Optional[torch.FloatTensor] = None, head_mask: Optional[torch.FloatTensor] = None, past_key_values: Optional[Tuple[Tuple[torch.FloatTensor]]] = None, labels: Optional[torch.LongTensor] = None, use_cache: Optional[bool] = None, output_attentions: Optional[bool] = None, output_hidden_states: Optional[bool] = None, return_dict: Optional[bool] = None) -> Union[Tuple, CausalLMOutputWithPast]:
        '''
        past_key_values (`tuple(tuple(torch.FloatTensor))`, *optional*, returned when `use_cache=True` is passed or when `config.use_cache=True`):
            Tuple of `tuple(torch.FloatTensor)` of length `config.n_layers`, with each tuple having 2 tensors of shape
            `(batch_size, num_heads, sequence_length, embed_size_per_head)`) and 2 additional tensors of shape
            `(batch_size, num_heads, encoder_sequence_length, embed_size_per_head)`. The two additional tensors are
            only required when the model is used as a decoder in a Sequence to Sequence model.

            Contains pre-computed hidden-states (key and values in the self-attention blocks that can be used (see
            `past_key_values` input) to speed up sequential decoding.

            If `past_key_values` are used, the user can optionally input only the last `decoder_input_ids` (those that
            don\'t have their past key value states given to this model) of shape `(batch_size, 1)` instead of all
            `decoder_input_ids` of shape `(batch_size, sequence_length)`.
        labels (`torch.LongTensor` of shape `(batch_size, sequence_length)`, *optional*):
            Labels for computing the left-to-right language modeling loss (next word prediction). Indices should be in
            `[-100, 0, ..., config.vocab_size]` (see `input_ids` docstring) Tokens with indices set to `-100` are
            ignored (masked), the loss is only computed for the tokens with labels n `[0, ..., config.vocab_size]`.
        use_cache (`bool`, *optional*):
            If set to `True`, `past_key_values` key value states are returned and can be used to speed up decoding (see
            `past_key_values`).

        Returns:

        Example:

        ```python
        >>> from transformers import AutoTokenizer, GPTNeoXJapaneseForCausalLM, GPTNeoXJapaneseConfig
        >>> import torch

        >>> tokenizer = AutoTokenizer.from_pretrained("abeja/gpt-neox-japanese-2.7b")
        >>> config = GPTNeoXJapaneseConfig.from_pretrained("abeja/gpt-neox-japanese-2.7b")
        >>> config.is_decoder = True
        >>> model = GPTNeoXJapaneseForCausalLM.from_pretrained("abeja/gpt-neox-japanese-2.7b", config=config)

        >>> inputs = tokenizer("日本語のGPT-neoxがHugging Faceで使えます😀", return_tensors="pt")
        >>> outputs = model(**inputs)

        >>> prediction_logits = outputs.logits
        ```
        '''
    def prepare_inputs_for_generation(self, input_ids, past_key_values: Incomplete | None = None, attention_mask: Incomplete | None = None, **model_kwargs): ...
