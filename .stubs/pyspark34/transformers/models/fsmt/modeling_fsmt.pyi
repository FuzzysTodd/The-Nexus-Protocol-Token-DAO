import torch
from ...activations import ACT2FN as ACT2FN
from ...deepspeed import is_deepspeed_zero3_enabled as is_deepspeed_zero3_enabled
from ...modeling_outputs import BaseModelOutput as BaseModelOutput, BaseModelOutputWithPastAndCrossAttentions as BaseModelOutputWithPastAndCrossAttentions, Seq2SeqLMOutput as Seq2SeqLMOutput, Seq2SeqModelOutput as Seq2SeqModelOutput
from ...modeling_utils import PreTrainedModel as PreTrainedModel
from ...utils import add_code_sample_docstrings as add_code_sample_docstrings, add_end_docstrings as add_end_docstrings, add_start_docstrings as add_start_docstrings, add_start_docstrings_to_model_forward as add_start_docstrings_to_model_forward, logging as logging, replace_return_docstrings as replace_return_docstrings
from .configuration_fsmt import FSMTConfig as FSMTConfig
from _typeshed import Incomplete
from torch import Tensor as Tensor, nn
from typing import Any, Dict, List, Optional, Tuple, Union

logger: Incomplete
FSMT_START_DOCSTRING: str
FSMT_GENERATION_EXAMPLE: str
FSMT_INPUTS_DOCSTRING: str

def invert_mask(attention_mask):
    """Turns 1->0, 0->1, False->True, True-> False"""
def triu_onnx(x, diagonal: int = 0): ...

class PretrainedFSMTModel(PreTrainedModel):
    config_class = FSMTConfig
    base_model_prefix: str
    @property
    def dummy_inputs(self): ...

def shift_tokens_right(input_ids, pad_token_id):
    """Shift input ids one token to the right, and wrap the last non pad token (usually <eos>)."""
def make_padding_mask(input_ids, padding_idx: int = 1):
    """True for pad tokens"""

class EncoderLayer(nn.Module):
    embed_dim: Incomplete
    self_attn: Incomplete
    self_attn_layer_norm: Incomplete
    dropout: Incomplete
    activation_fn: Incomplete
    activation_dropout: Incomplete
    fc1: Incomplete
    fc2: Incomplete
    final_layer_norm: Incomplete
    def __init__(self, config: FSMTConfig) -> None: ...
    def forward(self, x, encoder_padding_mask, layer_head_mask, output_attentions: bool = False):
        """
        Args:
            x (`torch.Tensor`): input to the layer of shape *(seq_len, batch, embed_dim)*
            encoder_padding_mask (`torch.ByteTensor`): binary ByteTensor of shape
                *(batch, src_len)* where padding elements are indicated by `1`.
            for t_tgt, t_src is excluded (or masked out), =0 means it is
            included in attention
            layer_head_mask (`torch.FloatTensor`): mask for attention heads in a given layer of size
                *(config.encoder_attention_heads,)*.

        Returns:
            encoded output of shape *(seq_len, batch, embed_dim)*
        """

class FSMTEncoder(nn.Module):
    """
    Transformer encoder consisting of *config.encoder_layers* self attention layers. Each layer is a [`EncoderLayer`].

    Args:
        config: FSMTConfig
    """
    dropout: Incomplete
    layerdrop: Incomplete
    padding_idx: Incomplete
    embed_tokens: Incomplete
    embed_scale: Incomplete
    embed_positions: Incomplete
    layers: Incomplete
    def __init__(self, config: FSMTConfig, embed_tokens) -> None: ...
    def forward(self, input_ids: torch.Tensor, attention_mask: Optional[torch.Tensor] = None, inputs_embeds: torch.Tensor = None, head_mask: Optional[torch.Tensor] = None, output_attentions: bool = False, output_hidden_states: bool = False, return_dict: bool = True):
        """
        Args:
            input_ids (`torch.LongTensor`): tokens in the source language of shape
                *(batch, src_len)*
            attention_mask (`torch.LongTensor`): indicating which indices are padding tokens
            inputs_embeds (`torch.FloatTensor`):
                embedding vectors of shape *(batch, src_len, embed_dim)*
            head_mask (`torch.Tensor` of shape `(num_layers, num_heads)`, *optional*):
                Mask to nullify selected heads of the attention modules. Mask values selected in `[0, 1]`:

                - 1 indicates the head is **not masked**,
                - 0 indicates the head is **masked**.

        Returns:
            BaseModelOutput or Tuple comprised of:

                - **x** (`torch.Tensor`): the last encoder layer's output of shape *(src_len, batch, embed_dim)*
                - **encoder_states** (`Tuple(torch.FloatTensor`)): all intermediate hidden states of shape *(src_len,
                  batch, embed_dim)*. Only populated if *output_hidden_states:* is True.
                - **all_attentions** (`Tuple(torch.FloatTensor`)): Attention weights for each layer.
                During training might not be of length n_layers because of layer dropout.
        """

class DecoderLayer(nn.Module):
    embed_dim: Incomplete
    self_attn: Incomplete
    dropout: Incomplete
    activation_fn: Incomplete
    activation_dropout: Incomplete
    self_attn_layer_norm: Incomplete
    encoder_attn: Incomplete
    encoder_attn_layer_norm: Incomplete
    fc1: Incomplete
    fc2: Incomplete
    final_layer_norm: Incomplete
    def __init__(self, config: FSMTConfig) -> None: ...
    def forward(self, x, encoder_hidden_states, encoder_attn_mask: Incomplete | None = None, layer_state: Incomplete | None = None, causal_mask: Incomplete | None = None, layer_head_mask: Incomplete | None = None, cross_attn_layer_head_mask: Incomplete | None = None, decoder_padding_mask: Incomplete | None = None, output_attentions: bool = False): ...

class FSMTDecoder(nn.Module):
    """
    Transformer decoder consisting of *config.decoder_layers* layers. Each layer is a [`DecoderLayer`]

    Args:
        config: FSMTConfig
        embed_tokens (nn.Embedding): output embedding
    """
    dropout: Incomplete
    layerdrop: Incomplete
    padding_idx: Incomplete
    embed_scale: Incomplete
    embed_tokens: Incomplete
    embed_positions: Incomplete
    layers: Incomplete
    output_projection: Incomplete
    def __init__(self, config: FSMTConfig, embed_tokens: nn.Embedding) -> None: ...
    def forward(self, input_ids: torch.Tensor, encoder_hidden_states: torch.Tensor, encoder_padding_mask: torch.Tensor, decoder_padding_mask: torch.Tensor, decoder_causal_mask: torch.Tensor, head_mask: Optional[torch.Tensor] = None, inputs_embeds: Optional[torch.Tensor] = None, cross_attn_head_mask: Optional[torch.Tensor] = None, past_key_values: Optional[List[torch.FloatTensor]] = None, use_cache: bool = False, output_attentions: bool = False, output_hidden_states: bool = False, return_dict: bool = True):
        '''
        Includes several features from "Jointly Learning to Align and Translate with Transformer Models" (Garg et al.,
        EMNLP 2019).

        Args:
            input_ids (`torch.LongTensor` of shape `(batch, tgt_len)`):
                previous decoder outputs for teacher forcing
            encoder_hidden_states: output from the encoder, used for
                encoder-side attention
            encoder_padding_mask: for ignoring pad tokens
            past_key_values (dict or None): dictionary used for storing state during generation
            head_mask (`torch.Tensor` of shape `(num_layers, num_heads)`, *optional*):
                Mask to nullify selected heads of the attention modules. Mask values selected in `[0, 1]`:

                - 1 indicates the head is **not masked**,
                - 0 indicates the head is **masked**.

            cross_attn_head_mask (`torch.Tensor` of shape `(num_layers, num_heads)`, *optional*):
                Mask to nullify selected heads of the cross-attention modules. Mask values selected in `[0, 1]`:

                - 1 indicates the head is **not masked**,
                - 0 indicates the head is **masked**.

        Returns:
            BaseModelOutputWithPast or tuple:

                - the decoder\'s features of shape *(batch, tgt_len, embed_dim)*
                - the cache
                - hidden states
                - attentions
        '''

class Attention(nn.Module):
    """Multi-headed attention from 'Attention Is All You Need' paper"""
    embed_dim: Incomplete
    num_heads: Incomplete
    dropout: Incomplete
    head_dim: Incomplete
    scaling: Incomplete
    encoder_decoder_attention: Incomplete
    k_proj: Incomplete
    v_proj: Incomplete
    q_proj: Incomplete
    out_proj: Incomplete
    cache_key: Incomplete
    def __init__(self, embed_dim, num_heads, dropout: float = 0.0, bias: bool = True, encoder_decoder_attention: bool = False) -> None: ...
    def forward(self, query, key: Optional[Tensor], key_padding_mask: Optional[Tensor] = None, layer_state: Optional[Dict[str, Optional[Tensor]]] = None, attn_mask: Optional[Tensor] = None, layer_head_mask: Optional[Tensor] = None, output_attentions: bool = False) -> Tuple[Tensor, Optional[Tensor]]:
        """Input shape: Time(SeqLen) x Batch x Channel"""

def fill_with_neg_inf(t):
    """FP16-compatible function that fills a input_ids with -inf."""

class FSMTModel(PretrainedFSMTModel):
    encoder: Incomplete
    decoder: Incomplete
    def __init__(self, config: FSMTConfig) -> None: ...
    def get_encoder(self): ...
    def get_decoder(self): ...
    def forward(self, input_ids: torch.LongTensor, attention_mask: Optional[torch.Tensor] = None, decoder_input_ids: Optional[torch.LongTensor] = None, decoder_attention_mask: Optional[torch.BoolTensor] = None, head_mask: Optional[torch.Tensor] = None, decoder_head_mask: Optional[torch.Tensor] = None, cross_attn_head_mask: Optional[torch.Tensor] = None, encoder_outputs: Optional[Tuple[torch.FloatTensor]] = None, past_key_values: Optional[Tuple[torch.FloatTensor]] = None, use_cache: Optional[bool] = None, output_attentions: Optional[bool] = None, output_hidden_states: Optional[bool] = None, inputs_embeds: Optional[torch.FloatTensor] = None, decoder_inputs_embeds: Optional[torch.FloatTensor] = None, return_dict: Optional[bool] = None) -> Union[Tuple[torch.Tensor], Seq2SeqModelOutput]: ...
    def get_input_embeddings(self): ...
    def set_input_embeddings(self, value) -> None: ...
    def get_output_embeddings(self): ...
    def set_output_embeddings(self, value) -> None: ...

class FSMTForConditionalGeneration(PretrainedFSMTModel):
    base_model_prefix: str
    model: Incomplete
    def __init__(self, config: FSMTConfig) -> None: ...
    def forward(self, input_ids: torch.LongTensor, attention_mask: Optional[torch.Tensor] = None, decoder_input_ids: Optional[torch.LongTensor] = None, decoder_attention_mask: Optional[torch.BoolTensor] = None, head_mask: Optional[torch.Tensor] = None, decoder_head_mask: Optional[torch.Tensor] = None, cross_attn_head_mask: Optional[torch.Tensor] = None, encoder_outputs: Optional[Tuple[torch.FloatTensor]] = None, past_key_values: Optional[Tuple[torch.FloatTensor]] = None, inputs_embeds: Optional[torch.Tensor] = None, decoder_inputs_embeds: Optional[torch.Tensor] = None, labels: Optional[torch.LongTensor] = None, use_cache: Optional[bool] = None, output_attentions: Optional[bool] = None, output_hidden_states: Optional[bool] = None, return_dict: Optional[bool] = None) -> Union[Tuple[torch.Tensor], Seq2SeqLMOutput]:
        """
        labels (`torch.LongTensor` of shape `(batch_size, sequence_length)`, *optional*):
            Labels for computing the masked language modeling loss. Indices should either be in `[0, ...,
            config.vocab_size]` or -100 (see `input_ids` docstring). Tokens with indices set to `-100` are ignored
            (masked), the loss is only computed for the tokens with labels in `[0, ..., config.vocab_size]`.

        Returns:

        """
    def prepare_inputs_for_generation(self, decoder_input_ids, past_key_values: Incomplete | None = None, attention_mask: Incomplete | None = None, head_mask: Incomplete | None = None, decoder_head_mask: Incomplete | None = None, cross_attn_head_mask: Incomplete | None = None, use_cache: Incomplete | None = None, encoder_outputs: Incomplete | None = None, **kwargs): ...
    def prepare_decoder_input_ids_from_labels(self, labels: torch.Tensor): ...
    def get_encoder(self): ...
    def get_decoder(self): ...
    def get_output_embeddings(self): ...
    def set_output_embeddings(self, value) -> None: ...

class SinusoidalPositionalEmbedding(nn.Embedding):
    """
    This module produces sinusoidal positional embeddings of any length.

    We don't want to save the weight of this embedding since it's not trained (deterministic) and it can be huge.

    Padding symbols are ignored.

    These embeddings get automatically extended in forward if more positions is needed.
    """
    def __init__(self, num_positions, embedding_dim, padding_idx) -> None: ...
    weight: Incomplete
    def make_weight(self, num_positions, embedding_dim, padding_idx) -> None: ...
    @staticmethod
    def get_embedding(num_embeddings, embedding_dim, padding_idx):
        '''
        Build sinusoidal embeddings.

        This matches the implementation in tensor2tensor, but differs slightly from the description in Section 3.5 of
        "Attention Is All You Need".
        '''
    @staticmethod
    def make_positions(tensor, padding_idx: int):
        """
        Replace non-padding symbols with their position numbers.

        Position numbers begin at padding_idx+1. Padding symbols are ignored.
        """
    def forward(self, input, incremental_state: Optional[Any] = None, timestep: Optional[Tensor] = None):
        """Input is expected to be of size [bsz x seqlen]."""
