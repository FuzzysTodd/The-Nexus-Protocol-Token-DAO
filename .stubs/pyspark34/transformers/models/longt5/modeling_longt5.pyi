import torch
from ...activations import ACT2FN as ACT2FN
from ...modeling_outputs import BaseModelOutput as BaseModelOutput, BaseModelOutputWithPastAndCrossAttentions as BaseModelOutputWithPastAndCrossAttentions, Seq2SeqLMOutput as Seq2SeqLMOutput, Seq2SeqModelOutput as Seq2SeqModelOutput
from ...modeling_utils import PreTrainedModel as PreTrainedModel
from ...pytorch_utils import ALL_LAYERNORM_LAYERS as ALL_LAYERNORM_LAYERS, find_pruneable_heads_and_indices as find_pruneable_heads_and_indices, prune_linear_layer as prune_linear_layer
from ...utils import DUMMY_INPUTS as DUMMY_INPUTS, DUMMY_MASK as DUMMY_MASK, add_start_docstrings as add_start_docstrings, add_start_docstrings_to_model_forward as add_start_docstrings_to_model_forward, is_torch_fx_proxy as is_torch_fx_proxy, logging as logging, replace_return_docstrings as replace_return_docstrings
from .configuration_longt5 import LongT5Config as LongT5Config
from _typeshed import Incomplete
from apex.normalization import FusedRMSNorm
from torch import nn
from typing import Any, Optional, Tuple, Union

logger: Incomplete
LONGT5_PRETRAINED_MODEL_ARCHIVE_LIST: Incomplete

class LongT5LayerNorm(nn.Module):
    weight: Incomplete
    variance_epsilon: Incomplete
    def __init__(self, hidden_size, eps: float = 1e-06) -> None:
        """
        Construct a layernorm module in the LongT5 style. No bias and no subtraction of mean.
        """
    def forward(self, hidden_states): ...
LongT5LayerNorm = FusedRMSNorm

class LongT5DenseActDense(nn.Module):
    wi: Incomplete
    wo: Incomplete
    dropout: Incomplete
    act: Incomplete
    def __init__(self, config: LongT5Config) -> None: ...
    def forward(self, hidden_states): ...

class LongT5DenseGatedActDense(nn.Module):
    wi_0: Incomplete
    wi_1: Incomplete
    wo: Incomplete
    dropout: Incomplete
    act: Incomplete
    def __init__(self, config: LongT5Config) -> None: ...
    def forward(self, hidden_states): ...

class LongT5LayerFF(nn.Module):
    DenseReluDense: Incomplete
    layer_norm: Incomplete
    dropout: Incomplete
    def __init__(self, config: LongT5Config) -> None: ...
    def forward(self, hidden_states): ...

class LongT5Attention(nn.Module):
    is_decoder: Incomplete
    has_relative_attention_bias: Incomplete
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
    pruned_heads: Incomplete
    gradient_checkpointing: bool
    def __init__(self, config: LongT5Config, has_relative_attention_bias: bool = False) -> None: ...
    def prune_heads(self, heads) -> None: ...
    def compute_bias(self, query_length, key_length, device: Incomplete | None = None):
        """Compute binned relative position bias"""
    def forward(self, hidden_states, mask: Incomplete | None = None, key_value_states: Incomplete | None = None, position_bias: Incomplete | None = None, past_key_value: Incomplete | None = None, layer_head_mask: Incomplete | None = None, query_length: Incomplete | None = None, use_cache: bool = False, output_attentions: bool = False):
        """
        Self-attention (if key_value_states is None) or attention over source sentence (provided by key_value_states).
        """

class LongT5LocalAttention(nn.Module):
    is_decoder: Incomplete
    has_relative_attention_bias: Incomplete
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
    pruned_heads: Incomplete
    gradient_checkpointing: bool
    def __init__(self, config: LongT5Config, has_relative_attention_bias: bool = False) -> None: ...
    def prune_heads(self, heads) -> None: ...
    def compute_bias(self, block_length: int):
        """Compute binned relative position bias"""
    def forward(self, hidden_states, mask: Incomplete | None = None, position_bias: Incomplete | None = None, layer_head_mask: Incomplete | None = None, output_attentions: bool = False): ...

class LongT5TransientGlobalAttention(nn.Module):
    is_decoder: Incomplete
    has_relative_attention_bias: Incomplete
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
    pruned_heads: Incomplete
    gradient_checkpointing: bool
    global_relative_attention_bias: Incomplete
    global_input_layer_norm: Incomplete
    def __init__(self, config: LongT5Config, has_relative_attention_bias: bool = False) -> None: ...
    def prune_heads(self, heads) -> None: ...
    def compute_bias(self, block_length: int):
        """Compute binned relative position bias"""
    def compute_side_bias(self, mask: torch.Tensor, global_segment_ids: torch.Tensor) -> torch.Tensor: ...
    def forward(self, hidden_states, mask: Incomplete | None = None, position_bias: Incomplete | None = None, layer_head_mask: Incomplete | None = None, output_attentions: bool = False): ...

class LongT5LayerSelfAttention(nn.Module):
    SelfAttention: Incomplete
    layer_norm: Incomplete
    dropout: Incomplete
    def __init__(self, config, has_relative_attention_bias: bool = False) -> None: ...
    def forward(self, hidden_states, attention_mask: Incomplete | None = None, position_bias: Incomplete | None = None, layer_head_mask: Incomplete | None = None, past_key_value: Incomplete | None = None, use_cache: bool = False, output_attentions: bool = False): ...

class LongT5LayerLocalSelfAttention(nn.Module):
    """Local self attention used in encoder"""
    LocalSelfAttention: Incomplete
    layer_norm: Incomplete
    dropout: Incomplete
    def __init__(self, config, has_relative_attention_bias: bool = False) -> None: ...
    def forward(self, hidden_states, attention_mask: Incomplete | None = None, position_bias: Incomplete | None = None, layer_head_mask: Incomplete | None = None, output_attentions: bool = False, **kwargs: Any): ...

class LongT5LayerTransientGlobalSelfAttention(nn.Module):
    """Transient-Global self attention used in encoder"""
    TransientGlobalSelfAttention: Incomplete
    layer_norm: Incomplete
    dropout: Incomplete
    def __init__(self, config, has_relative_attention_bias: bool = False) -> None: ...
    def forward(self, hidden_states, attention_mask: Incomplete | None = None, position_bias: Incomplete | None = None, layer_head_mask: Incomplete | None = None, output_attentions: bool = False, **kwargs: Any): ...

class LongT5LayerCrossAttention(nn.Module):
    EncDecAttention: Incomplete
    layer_norm: Incomplete
    dropout: Incomplete
    def __init__(self, config) -> None: ...
    def forward(self, hidden_states, key_value_states, attention_mask: Incomplete | None = None, position_bias: Incomplete | None = None, layer_head_mask: Incomplete | None = None, past_key_value: Incomplete | None = None, use_cache: bool = False, query_length: Incomplete | None = None, output_attentions: bool = False): ...

class LongT5Block(nn.Module):
    is_decoder: Incomplete
    layer: Incomplete
    def __init__(self, config, has_relative_attention_bias: bool = False) -> None: ...
    def forward(self, hidden_states, attention_mask: Incomplete | None = None, position_bias: Incomplete | None = None, encoder_hidden_states: Incomplete | None = None, encoder_attention_mask: Incomplete | None = None, encoder_decoder_position_bias: Incomplete | None = None, layer_head_mask: Incomplete | None = None, cross_attn_layer_head_mask: Incomplete | None = None, past_key_value: Incomplete | None = None, use_cache: bool = False, output_attentions: bool = False, return_dict: bool = True): ...

class LongT5PreTrainedModel(PreTrainedModel):
    """
    An abstract class to handle weights initialization and a simple interface for downloading and loading pretrained
    models.
    """
    config_class = LongT5Config
    base_model_prefix: str
    supports_gradient_checkpointing: bool
    @property
    def dummy_inputs(self): ...

class LongT5Stack(LongT5PreTrainedModel):
    embed_tokens: Incomplete
    is_decoder: Incomplete
    local_radius: Incomplete
    block_len: Incomplete
    block: Incomplete
    final_layer_norm: Incomplete
    dropout: Incomplete
    gradient_checkpointing: bool
    def __init__(self, config, embed_tokens: Incomplete | None = None) -> None: ...
    def get_input_embeddings(self): ...
    def set_input_embeddings(self, new_embeddings) -> None: ...
    def forward(self, input_ids: Incomplete | None = None, attention_mask: Incomplete | None = None, encoder_hidden_states: Incomplete | None = None, encoder_attention_mask: Incomplete | None = None, inputs_embeds: Incomplete | None = None, head_mask: Incomplete | None = None, cross_attn_head_mask: Incomplete | None = None, past_key_values: Incomplete | None = None, use_cache: Incomplete | None = None, output_attentions: Incomplete | None = None, output_hidden_states: Incomplete | None = None, return_dict: Incomplete | None = None): ...

LONGT5_START_DOCSTRING: str
LONGT5_INPUTS_DOCSTRING: str
LONGT5_ENCODER_INPUTS_DOCSTRING: str

class LongT5Model(LongT5PreTrainedModel):
    shared: Incomplete
    encoder: Incomplete
    decoder: Incomplete
    def __init__(self, config: LongT5Config) -> None: ...
    def get_input_embeddings(self): ...
    def set_input_embeddings(self, new_embeddings) -> None: ...
    def get_encoder(self): ...
    def get_decoder(self): ...
    def forward(self, input_ids: Optional[torch.LongTensor] = None, attention_mask: Optional[torch.FloatTensor] = None, decoder_input_ids: Optional[torch.LongTensor] = None, decoder_attention_mask: Optional[torch.BoolTensor] = None, head_mask: Optional[torch.FloatTensor] = None, decoder_head_mask: Optional[torch.FloatTensor] = None, cross_attn_head_mask: Optional[torch.Tensor] = None, encoder_outputs: Optional[Tuple[Tuple[torch.FloatTensor]]] = None, past_key_values: Optional[Tuple[Tuple[torch.FloatTensor]]] = None, inputs_embeds: Optional[torch.Tensor] = None, decoder_inputs_embeds: Optional[torch.Tensor] = None, use_cache: Optional[bool] = None, output_attentions: Optional[bool] = None, output_hidden_states: Optional[bool] = None, return_dict: Optional[bool] = None) -> Union[Tuple[torch.FloatTensor], Seq2SeqModelOutput]:
        '''
        Returns:

        Example:

        ```python
        >>> from transformers import AutoTokenizer, LongT5Model

        >>> tokenizer = AutoTokenizer.from_pretrained("google/long-t5-local-base")
        >>> model = LongT5Model.from_pretrained("google/long-t5-local-base")

        >>> # Let\'s try a very long encoder input.
        >>> input_ids = tokenizer(
        ...     100 * "Studies have been shown that owning a dog is good for you", return_tensors="pt"
        ... ).input_ids  # Batch size 1

        >>> decoder_input_ids = tokenizer("Studies show that", return_tensors="pt").input_ids  # Batch size 1

        >>> # forward pass
        >>> outputs = model(input_ids=input_ids, decoder_input_ids=decoder_input_ids)
        >>> last_hidden_states = outputs.last_hidden_state
        ```'''

class LongT5ForConditionalGeneration(LongT5PreTrainedModel):
    model_dim: Incomplete
    shared: Incomplete
    encoder: Incomplete
    decoder: Incomplete
    lm_head: Incomplete
    def __init__(self, config: LongT5Config) -> None: ...
    def get_input_embeddings(self): ...
    def set_input_embeddings(self, new_embeddings) -> None: ...
    def set_output_embeddings(self, new_embeddings) -> None: ...
    def get_output_embeddings(self): ...
    def get_encoder(self): ...
    def get_decoder(self): ...
    def forward(self, input_ids: Optional[torch.LongTensor] = None, attention_mask: Optional[torch.FloatTensor] = None, decoder_input_ids: Optional[torch.LongTensor] = None, decoder_attention_mask: Optional[torch.BoolTensor] = None, head_mask: Optional[torch.FloatTensor] = None, decoder_head_mask: Optional[torch.FloatTensor] = None, cross_attn_head_mask: Optional[torch.Tensor] = None, encoder_outputs: Optional[Tuple[Tuple[torch.Tensor]]] = None, past_key_values: Optional[Tuple[Tuple[torch.Tensor]]] = None, inputs_embeds: Optional[torch.FloatTensor] = None, decoder_inputs_embeds: Optional[torch.FloatTensor] = None, labels: Optional[torch.LongTensor] = None, use_cache: Optional[bool] = None, output_attentions: Optional[bool] = None, output_hidden_states: Optional[bool] = None, return_dict: Optional[bool] = None) -> Union[Tuple[torch.FloatTensor], Seq2SeqLMOutput]:
        '''
        labels (`torch.LongTensor` of shape `(batch_size,)`, *optional*):
            Labels for computing the sequence classification/regression loss. Indices should be in `[-100, 0, ...,
            config.vocab_size - 1]`. All labels set to `-100` are ignored (masked), the loss is only computed for
            labels in `[0, ..., config.vocab_size]`

        Returns:

        Examples:

        ```python
        >>> from transformers import AutoTokenizer, LongT5ForConditionalGeneration

        >>> tokenizer = AutoTokenizer.from_pretrained("Stancld/longt5-tglobal-large-16384-pubmed-3k_steps")
        >>> model = LongT5ForConditionalGeneration.from_pretrained(
        ...     "Stancld/longt5-tglobal-large-16384-pubmed-3k_steps"
        ... )

        >>> # Let\'s try a very long input.
        >>> inputs = tokenizer(100 * "studies have shown that owning a dog is good for you ", return_tensors="pt")
        >>> input_ids = inputs.input_ids

        >>> outputs = model.generate(input_ids)
        >>> print(tokenizer.decode(outputs[0], skip_special_tokens=True))
        abstractthe aim of this article is to provide an overview of the literature on the role of dog
        ```'''
    def prepare_inputs_for_generation(self, input_ids, past_key_values: Incomplete | None = None, attention_mask: Incomplete | None = None, head_mask: Incomplete | None = None, decoder_head_mask: Incomplete | None = None, cross_attn_head_mask: Incomplete | None = None, use_cache: Incomplete | None = None, encoder_outputs: Incomplete | None = None, **kwargs): ...
    def prepare_decoder_input_ids_from_labels(self, labels: torch.Tensor): ...

class LongT5EncoderModel(LongT5PreTrainedModel):
    shared: Incomplete
    encoder: Incomplete
    def __init__(self, config: LongT5Config) -> None: ...
    def get_input_embeddings(self): ...
    def set_input_embeddings(self, new_embeddings) -> None: ...
    def get_encoder(self): ...
    def forward(self, input_ids: Optional[torch.LongTensor] = None, attention_mask: Optional[torch.FloatTensor] = None, head_mask: Optional[torch.FloatTensor] = None, inputs_embeds: Optional[torch.FloatTensor] = None, output_attentions: Optional[bool] = None, output_hidden_states: Optional[bool] = None, return_dict: Optional[bool] = None) -> Union[Tuple[torch.FloatTensor], BaseModelOutput]:
        '''
        Returns:

        Example:

        ```python
        >>> from transformers import AutoTokenizer, LongT5ForConditionalGeneration

        >>> tokenizer = AutoTokenizer.from_pretrained("google/long-t5-local-base")
        >>> model = LongT5EncoderModel.from_pretrained("google/long-t5-local-base")
        >>> input_ids = tokenizer(
        ...     100 * "Studies have been shown that owning a dog is good for you ", return_tensors="pt"
        ... ).input_ids  # Batch size 1
        >>> outputs = model(input_ids=input_ids)
        >>> last_hidden_states = outputs.last_hidden_state
        ```'''
