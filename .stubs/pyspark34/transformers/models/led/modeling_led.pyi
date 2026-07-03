import torch
from ...activations import ACT2FN as ACT2FN
from ...modeling_outputs import BaseModelOutputWithPastAndCrossAttentions as BaseModelOutputWithPastAndCrossAttentions, Seq2SeqLMOutput as Seq2SeqLMOutput, Seq2SeqModelOutput as Seq2SeqModelOutput, Seq2SeqQuestionAnsweringModelOutput as Seq2SeqQuestionAnsweringModelOutput, Seq2SeqSequenceClassifierOutput as Seq2SeqSequenceClassifierOutput
from ...modeling_utils import PreTrainedModel as PreTrainedModel
from ...utils import ModelOutput as ModelOutput, add_code_sample_docstrings as add_code_sample_docstrings, add_end_docstrings as add_end_docstrings, add_start_docstrings as add_start_docstrings, add_start_docstrings_to_model_forward as add_start_docstrings_to_model_forward, logging as logging, replace_return_docstrings as replace_return_docstrings
from .configuration_led import LEDConfig as LEDConfig
from _typeshed import Incomplete
from dataclasses import dataclass
from torch import nn
from typing import List, Optional, Tuple, Union

logger: Incomplete
LED_PRETRAINED_MODEL_ARCHIVE_LIST: Incomplete

def shift_tokens_right(input_ids: torch.Tensor, pad_token_id: int, decoder_start_token_id: int):
    """
    Shift input ids one token to the right.
    """

class LEDLearnedPositionalEmbedding(nn.Embedding):
    """
    This module learns positional embeddings up to a fixed maximum size.
    """
    def __init__(self, num_embeddings: int, embedding_dim: int) -> None: ...
    def forward(self, input_ids_shape: torch.Size, past_key_values_length: int = 0):
        """`input_ids_shape` is expected to be [bsz x seqlen]."""

class LEDEncoderSelfAttention(nn.Module):
    num_heads: Incomplete
    head_dim: Incomplete
    embed_dim: Incomplete
    query: Incomplete
    key: Incomplete
    value: Incomplete
    query_global: Incomplete
    key_global: Incomplete
    value_global: Incomplete
    dropout: Incomplete
    layer_id: Incomplete
    one_sided_attn_window_size: Incomplete
    config: Incomplete
    def __init__(self, config, layer_id) -> None: ...
    def forward(self, hidden_states, attention_mask: Incomplete | None = None, layer_head_mask: Incomplete | None = None, is_index_masked: Incomplete | None = None, is_index_global_attn: Incomplete | None = None, is_global_attn: Incomplete | None = None, output_attentions: bool = False):
        """
        [`LEDEncoderSelfAttention`] expects *len(hidden_states)* to be multiple of *attention_window*. Padding to
        *attention_window* happens in [`LEDEncoderModel.forward`] to avoid redoing the padding on each layer.

        The *attention_mask* is changed in [`LEDEncoderModel.forward`] from 0, 1, 2 to:

            - -10000: no attention
            - 0: local attention
            - +10000: global attention
        """

class LEDEncoderAttention(nn.Module):
    longformer_self_attn: Incomplete
    output: Incomplete
    def __init__(self, config, layer_id) -> None: ...
    def forward(self, hidden_states: torch.Tensor, attention_mask: Optional[torch.Tensor] = None, layer_head_mask: Optional[torch.Tensor] = None, is_index_masked: Optional[torch.Tensor] = None, is_index_global_attn: Optional[torch.Tensor] = None, is_global_attn: Optional[bool] = None, output_attentions: bool = False) -> Tuple[torch.Tensor, Optional[torch.Tensor], Optional[Tuple[torch.Tensor]]]:
        """Input shape: Batch x Time x Channel"""

class LEDDecoderAttention(nn.Module):
    """Multi-headed attention from 'Attention Is All You Need' paper"""
    embed_dim: Incomplete
    num_heads: Incomplete
    dropout: Incomplete
    head_dim: Incomplete
    scaling: Incomplete
    is_decoder: Incomplete
    k_proj: Incomplete
    v_proj: Incomplete
    q_proj: Incomplete
    out_proj: Incomplete
    def __init__(self, embed_dim: int, num_heads: int, dropout: float = 0.0, is_decoder: bool = False, bias: bool = True) -> None: ...
    def forward(self, hidden_states: torch.Tensor, key_value_states: Optional[torch.Tensor] = None, past_key_value: Optional[Tuple[torch.Tensor]] = None, attention_mask: Optional[torch.Tensor] = None, layer_head_mask: Optional[torch.Tensor] = None, output_attentions: bool = False) -> Tuple[torch.Tensor, Optional[torch.Tensor], Optional[Tuple[torch.Tensor]]]:
        """Input shape: Batch x Time x Channel"""

class LEDEncoderLayer(nn.Module):
    embed_dim: Incomplete
    self_attn: Incomplete
    self_attn_layer_norm: Incomplete
    dropout: Incomplete
    activation_fn: Incomplete
    activation_dropout: Incomplete
    fc1: Incomplete
    fc2: Incomplete
    final_layer_norm: Incomplete
    def __init__(self, config: LEDConfig, layer_id: int) -> None: ...
    def forward(self, hidden_states: torch.Tensor, attention_mask: torch.Tensor, layer_head_mask: torch.Tensor, is_index_masked: Incomplete | None = None, is_index_global_attn: Incomplete | None = None, is_global_attn: Incomplete | None = None, output_attentions: bool = False):
        """
        Args:
            hidden_states (`torch.FloatTensor`): input to the layer of shape *(seq_len, batch, embed_dim)*
            attention_mask (`torch.FloatTensor`): attention mask of size
                *(batch, 1, tgt_len, src_len)* where padding elements are indicated by very large negative values.
            layer_head_mask (`torch.FloatTensor`): mask for attention heads in a given layer of size
                *(encoder_attention_heads,)*.
        """

class LEDDecoderLayer(nn.Module):
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
    def __init__(self, config: LEDConfig) -> None: ...
    def forward(self, hidden_states: torch.Tensor, attention_mask: Optional[torch.Tensor] = None, encoder_hidden_states: Optional[torch.Tensor] = None, encoder_attention_mask: Optional[torch.Tensor] = None, layer_head_mask: Optional[torch.Tensor] = None, cross_attn_layer_head_mask: Optional[torch.Tensor] = None, past_key_value: Optional[Tuple[torch.Tensor]] = None, output_attentions: Optional[bool] = False, use_cache: Optional[bool] = True):
        """
        Args:
            hidden_states (`torch.FloatTensor`): input to the layer of shape *(seq_len, batch, embed_dim)*
            attention_mask (`torch.FloatTensor`): attention mask of size
                *(batch, 1, tgt_len, src_len)* where padding elements are indicated by very large negative values.
            encoder_hidden_states (`torch.FloatTensor`):
                cross attention input to the layer of shape *(seq_len, batch, embed_dim)*
            encoder_attention_mask (`torch.FloatTensor`): encoder attention mask of size
                *(batch, 1, tgt_len, src_len)* where padding elements are indicated by very large negative values.
            layer_head_mask (`torch.FloatTensor`): mask for attention heads in a given layer of size
                *(decoder_attention_heads,)*.
            cross_attn_layer_head_mask (`torch.FloatTensor`): mask for encoder attention heads in a given layer of
                size *(decoder_attention_heads,)*.
            past_key_value (`Tuple(torch.FloatTensor)`): cached past key and value projection states
            output_attentions (`bool`): Whether the base model outputs attentions.
                This requires the attentions tensor to be reshaped in this function.
        """

class LEDClassificationHead(nn.Module):
    """Head for sentence-level classification tasks."""
    dense: Incomplete
    dropout: Incomplete
    out_proj: Incomplete
    def __init__(self, input_dim: int, inner_dim: int, num_classes: int, pooler_dropout: float) -> None: ...
    def forward(self, hidden_states: torch.Tensor): ...

class LEDPreTrainedModel(PreTrainedModel):
    config_class = LEDConfig
    base_model_prefix: str
    supports_gradient_checkpointing: bool
    @property
    def dummy_inputs(self): ...

@dataclass
class LEDEncoderBaseModelOutput(ModelOutput):
    """
    Base class for LEDEncoder's outputs, with potential hidden states, local and global attentions.

    Args:
        last_hidden_state (`torch.FloatTensor` of shape `(batch_size, sequence_length, hidden_size)`):
            Sequence of hidden-states at the output of the last layer of the model.
        hidden_states (`tuple(torch.FloatTensor)`, *optional*, returned when `output_hidden_states=True` is passed or when `config.output_hidden_states=True`):
            Tuple of `torch.FloatTensor` (one for the output of the embeddings + one for the output of each layer) of
            shape `(batch_size, sequence_length, hidden_size)`.

            Hidden-states of the model at the output of each layer plus the initial embedding outputs.
        attentions (`tuple(torch.FloatTensor)`, *optional*, returned when `output_attentions=True` is passed or when `config.output_attentions=True`):
            Tuple of `torch.FloatTensor` (one for each layer) of shape `(batch_size, num_heads, sequence_length, x +
            attention_window + 1)`, where `x` is the number of tokens with global attention mask.

            Local attentions weights after the attention softmax, used to compute the weighted average in the
            self-attention heads. Those are the attention weights from every token in the sequence to every token with
            global attention (first `x` values) and to every token in the attention window (remaining `attention_window
            + 1` values). Note that the first `x` values refer to tokens with fixed positions in the text, but the
            remaining `attention_window + 1` values refer to tokens with relative positions: the attention weight of a
            token to itself is located at index `x + attention_window / 2` and the `attention_window / 2` preceding
            (succeeding) values are the attention weights to the `attention_window / 2` preceding (succeeding) tokens.
            If the attention window contains a token with global attention, the attention weight at the corresponding
            index is set to 0; the value should be accessed from the first `x` attention weights. If a token has global
            attention, the attention weights to all other tokens in `attentions` is set to 0, the values should be
            accessed from `global_attentions`.
        global_attentions (`tuple(torch.FloatTensor)`, *optional*, returned when `output_attentions=True` is passed or when `config.output_attentions=True`):
            Tuple of `torch.FloatTensor` (one for each layer) of shape `(batch_size, num_heads, sequence_length, x)`,
            where `x` is the number of tokens with global attention mask.

            Global attentions weights after the attention softmax, used to compute the weighted average in the
            self-attention heads. Those are the attention weights from every token with global attention to every token
            in the sequence.
    """
    last_hidden_state: torch.FloatTensor
    hidden_states: Optional[Tuple[torch.FloatTensor]] = ...
    attentions: Optional[Tuple[torch.FloatTensor]] = ...
    global_attentions: Optional[Tuple[torch.FloatTensor]] = ...
    def __init__(self, last_hidden_state, hidden_states, attentions, global_attentions) -> None: ...

@dataclass
class LEDSeq2SeqModelOutput(ModelOutput):
    """
    Base class for model encoder's outputs that also contains : pre-computed hidden states that can speed up sequential
    decoding.

    Args:
        last_hidden_state (`torch.FloatTensor` of shape `(batch_size, sequence_length, hidden_size)`):
            Sequence of hidden-states at the output of the last layer of the decoder of the model.

            If `past_key_values` is used only the last hidden-state of the sequences of shape `(batch_size, 1,
            hidden_size)` is output.
        past_key_values (`List[torch.FloatTensor]`, *optional*, returned when `use_cache=True` is passed or when `config.use_cache=True`):
            List of `torch.FloatTensor` of length `config.n_layers`, with each tensor of shape `(2, batch_size,
            num_heads, sequence_length, embed_size_per_head)`).

            Contains pre-computed hidden-states (key and values in the attention blocks) of the decoder that can be
            used (see `past_key_values` input) to speed up sequential decoding.
        decoder_hidden_states (`tuple(torch.FloatTensor)`, *optional*, returned when `output_hidden_states=True` is passed or when `config.output_hidden_states=True`):
            Tuple of `torch.FloatTensor` (one for the output of the embeddings + one for the output of each layer) of
            shape `(batch_size, sequence_length, hidden_size)`.

            Hidden-states of the decoder at the output of each layer plus the initial embedding outputs.
        decoder_attentions (`tuple(torch.FloatTensor)`, *optional*, returned when `output_attentions=True` is passed or when `config.output_attentions=True`):
            Tuple of `torch.FloatTensor` (one for each layer) of shape `(batch_size, num_heads, sequence_length,
            sequence_length)`.

            Attentions weights of the decoder, after the attention softmax, used to compute the weighted average in the
            self-attention heads.
        cross_attentions (`tuple(torch.FloatTensor)`, *optional*, returned when `output_attentions=True` is passed or when `config.output_attentions=True`):
            Tuple of `torch.FloatTensor` (one for each layer) of shape `(batch_size, num_heads, sequence_length,
            sequence_length)`.

            Attentions weights of the decoder's cross-attention layer, after the attention softmax, used to compute the
            weighted average in the cross-attention heads.
        encoder_last_hidden_state (`torch.FloatTensor` of shape `(batch_size, sequence_length, hidden_size)`, *optional*):
            Sequence of hidden-states at the output of the last layer of the encoder of the model.
        encoder_hidden_states (`tuple(torch.FloatTensor)`, *optional*, returned when `output_hidden_states=True` is passed or when `config.output_hidden_states=True`):
            Tuple of `torch.FloatTensor` (one for the output of the embeddings + one for the output of each layer) of
            shape `(batch_size, sequence_length, hidden_size)`.

            Hidden-states of the encoder at the output of each layer plus the initial embedding outputs.
        encoder_attentions (`tuple(torch.FloatTensor)`, *optional*, returned when `output_attentions=True` is passed or when `config.output_attentions=True`):
            Tuple of `torch.FloatTensor` (one for each layer) of shape `(batch_size, num_heads, sequence_length,
            sequence_length)`.

            Attentions weights of the encoder, after the attention softmax, used to compute the weighted average in the
            self-attention heads.
        encoder_global_attentions (`tuple(torch.FloatTensor)`, *optional*, returned when `output_attentions=True` is passed or when `config.output_attentions=True`):
            Tuple of `torch.FloatTensor` (one for each layer) of shape `(batch_size, num_heads, sequence_length, x)`,
            where `x` is the number of tokens with global attention mask.

            Global attentions weights after the attention softmax, used to compute the weighted average in the
            self-attention heads. Those are the attention weights from every token with global attention to every token
            in the sequence.
    """
    last_hidden_state: torch.FloatTensor = ...
    past_key_values: Optional[List[torch.FloatTensor]] = ...
    decoder_hidden_states: Optional[Tuple[torch.FloatTensor]] = ...
    decoder_attentions: Optional[Tuple[torch.FloatTensor]] = ...
    cross_attentions: Optional[Tuple[torch.FloatTensor]] = ...
    encoder_last_hidden_state: Optional[torch.FloatTensor] = ...
    encoder_hidden_states: Optional[Tuple[torch.FloatTensor]] = ...
    encoder_attentions: Optional[Tuple[torch.FloatTensor]] = ...
    encoder_global_attentions: Optional[Tuple[torch.FloatTensor]] = ...
    def __init__(self, last_hidden_state, past_key_values, decoder_hidden_states, decoder_attentions, cross_attentions, encoder_last_hidden_state, encoder_hidden_states, encoder_attentions, encoder_global_attentions) -> None: ...

@dataclass
class LEDSeq2SeqLMOutput(ModelOutput):
    """
    Base class for sequence-to-sequence language models outputs.

    Args:
        loss (`torch.FloatTensor` of shape `(1,)`, *optional*, returned when `labels` is provided):
            Language modeling loss.
        logits (`torch.FloatTensor` of shape `(batch_size, sequence_length, config.vocab_size)`):
            Prediction scores of the language modeling head (scores for each vocabulary token before SoftMax).
        past_key_values (`List[torch.FloatTensor]`, *optional*, returned when `use_cache=True` is passed or when `config.use_cache=True`):
            List of `torch.FloatTensor` of length `config.n_layers`, with each tensor of shape `(2, batch_size,
            num_heads, sequence_length, embed_size_per_head)`).

            Contains pre-computed hidden-states (key and values in the attention blocks) of the decoder that can be
            used (see `past_key_values` input) to speed up sequential decoding.
        decoder_hidden_states (`tuple(torch.FloatTensor)`, *optional*, returned when `output_hidden_states=True` is passed or when `config.output_hidden_states=True`):
            Tuple of `torch.FloatTensor` (one for the output of the embeddings + one for the output of each layer) of
            shape `(batch_size, sequence_length, hidden_size)`.

            Hidden-states of the decoder at the output of each layer plus the initial embedding outputs.
        decoder_attentions (`tuple(torch.FloatTensor)`, *optional*, returned when `output_attentions=True` is passed or when `config.output_attentions=True`):
            Tuple of `torch.FloatTensor` (one for each layer) of shape `(batch_size, num_heads, sequence_length,
            sequence_length)`.

            Attentions weights of the decoder, after the attention softmax, used to compute the weighted average in the
            self-attention heads.
        cross_attentions (`tuple(torch.FloatTensor)`, *optional*, returned when `output_attentions=True` is passed or when `config.output_attentions=True`):
            Tuple of `torch.FloatTensor` (one for each layer) of shape `(batch_size, num_heads, sequence_length,
            sequence_length)`.

            Attentions weights of the decoder's cross-attention layer, after the attention softmax, used to compute the
            weighted average in the cross-attention heads.
        encoder_last_hidden_state (`torch.FloatTensor` of shape `(batch_size, sequence_length, hidden_size)`, *optional*):
            Sequence of hidden-states at the output of the last layer of the encoder of the model.
        encoder_hidden_states (`tuple(torch.FloatTensor)`, *optional*, returned when `output_hidden_states=True` is passed or when `config.output_hidden_states=True`):
            Tuple of `torch.FloatTensor` (one for the output of the embeddings + one for the output of each layer) of
            shape `(batch_size, sequence_length, hidden_size)`.

            Hidden-states of the encoder at the output of each layer plus the initial embedding outputs.
        encoder_attentions (`tuple(torch.FloatTensor)`, *optional*, returned when `output_attentions=True` is passed or when `config.output_attentions=True`):
            Tuple of `torch.FloatTensor` (one for each layer) of shape `(batch_size, num_heads, sequence_length,
            sequence_length)`.

            Attentions weights of the encoder, after the attention softmax, used to compute the weighted average in the
            self-attention heads.
        encoder_global_attentions (`tuple(torch.FloatTensor)`, *optional*, returned when `output_attentions=True` is passed or when `config.output_attentions=True`):
            Tuple of `torch.FloatTensor` (one for each layer) of shape `(batch_size, num_heads, sequence_length, x)`,
            where `x` is the number of tokens with global attention mask.

            Global attentions weights after the attention softmax, used to compute the weighted average in the
            self-attention heads. Those are the attention weights from every token with global attention to every token
            in the sequence.
    """
    loss: Optional[torch.FloatTensor] = ...
    logits: torch.FloatTensor = ...
    past_key_values: Optional[List[torch.FloatTensor]] = ...
    decoder_hidden_states: Optional[Tuple[torch.FloatTensor]] = ...
    decoder_attentions: Optional[Tuple[torch.FloatTensor]] = ...
    cross_attentions: Optional[Tuple[torch.FloatTensor]] = ...
    encoder_last_hidden_state: Optional[torch.FloatTensor] = ...
    encoder_hidden_states: Optional[Tuple[torch.FloatTensor]] = ...
    encoder_attentions: Optional[Tuple[torch.FloatTensor]] = ...
    encoder_global_attentions: Optional[Tuple[torch.FloatTensor]] = ...
    def __init__(self, loss, logits, past_key_values, decoder_hidden_states, decoder_attentions, cross_attentions, encoder_last_hidden_state, encoder_hidden_states, encoder_attentions, encoder_global_attentions) -> None: ...

@dataclass
class LEDSeq2SeqSequenceClassifierOutput(ModelOutput):
    """
    Base class for outputs of sequence-to-sequence sentence classification models.

    Args:
        loss (`torch.FloatTensor` of shape `(1,)`, *optional*, returned when `label` is provided):
            Classification (or regression if config.num_labels==1) loss.
        logits (`torch.FloatTensor` of shape `(batch_size, config.num_labels)`):
            Classification (or regression if config.num_labels==1) scores (before SoftMax).
        past_key_values (`List[torch.FloatTensor]`, *optional*, returned when `use_cache=True` is passed or when `config.use_cache=True`):
            List of `torch.FloatTensor` of length `config.n_layers`, with each tensor of shape `(2, batch_size,
            num_heads, sequence_length, embed_size_per_head)`).

            Contains pre-computed hidden-states (key and values in the attention blocks) of the decoder that can be
            used (see `past_key_values` input) to speed up sequential decoding.
        decoder_hidden_states (`tuple(torch.FloatTensor)`, *optional*, returned when `output_hidden_states=True` is passed or when `config.output_hidden_states=True`):
            Tuple of `torch.FloatTensor` (one for the output of the embeddings + one for the output of each layer) of
            shape `(batch_size, sequence_length, hidden_size)`.

            Hidden-states of the decoder at the output of each layer plus the initial embedding outputs.
        decoder_attentions (`tuple(torch.FloatTensor)`, *optional*, returned when `output_attentions=True` is passed or when `config.output_attentions=True`):
            Tuple of `torch.FloatTensor` (one for each layer) of shape `(batch_size, num_heads, sequence_length,
            sequence_length)`.

            Attentions weights of the decoder, after the attention softmax, used to compute the weighted average in the
            self-attention heads.
        cross_attentions (`tuple(torch.FloatTensor)`, *optional*, returned when `output_attentions=True` is passed or when `config.output_attentions=True`):
            Tuple of `torch.FloatTensor` (one for each layer) of shape `(batch_size, num_heads, sequence_length,
            sequence_length)`.

            Attentions weights of the decoder's cross-attention layer, after the attention softmax, used to compute the
            weighted average in the cross-attention heads.
        encoder_last_hidden_state (`torch.FloatTensor` of shape `(batch_size, sequence_length, hidden_size)`, *optional*):
            Sequence of hidden-states at the output of the last layer of the encoder of the model.
        encoder_hidden_states (`tuple(torch.FloatTensor)`, *optional*, returned when `output_hidden_states=True` is passed or when `config.output_hidden_states=True`):
            Tuple of `torch.FloatTensor` (one for the output of the embeddings + one for the output of each layer) of
            shape `(batch_size, sequence_length, hidden_size)`.

            Hidden-states of the encoder at the output of each layer plus the initial embedding outputs.
        encoder_attentions (`tuple(torch.FloatTensor)`, *optional*, returned when `output_attentions=True` is passed or when `config.output_attentions=True`):
            Tuple of `torch.FloatTensor` (one for each layer) of shape `(batch_size, num_heads, sequence_length,
            sequence_length)`.

            Attentions weights of the encoder, after the attention softmax, used to compute the weighted average in the
            self-attention heads.
        encoder_global_attentions (`tuple(torch.FloatTensor)`, *optional*, returned when `output_attentions=True` is passed or when `config.output_attentions=True`):
            Tuple of `torch.FloatTensor` (one for each layer) of shape `(batch_size, num_heads, sequence_length, x)`,
            where `x` is the number of tokens with global attention mask.

            Global attentions weights after the attention softmax, used to compute the weighted average in the
            self-attention heads. Those are the attention weights from every token with global attention to every token
            in the sequence.
    """
    loss: Optional[torch.FloatTensor] = ...
    logits: torch.FloatTensor = ...
    past_key_values: Optional[List[torch.FloatTensor]] = ...
    decoder_hidden_states: Optional[Tuple[torch.FloatTensor]] = ...
    decoder_attentions: Optional[Tuple[torch.FloatTensor]] = ...
    cross_attentions: Optional[Tuple[torch.FloatTensor]] = ...
    encoder_last_hidden_state: Optional[torch.FloatTensor] = ...
    encoder_hidden_states: Optional[Tuple[torch.FloatTensor]] = ...
    encoder_attentions: Optional[Tuple[torch.FloatTensor]] = ...
    encoder_global_attentions: Optional[Tuple[torch.FloatTensor]] = ...
    def __init__(self, loss, logits, past_key_values, decoder_hidden_states, decoder_attentions, cross_attentions, encoder_last_hidden_state, encoder_hidden_states, encoder_attentions, encoder_global_attentions) -> None: ...

@dataclass
class LEDSeq2SeqQuestionAnsweringModelOutput(ModelOutput):
    """
    Base class for outputs of sequence-to-sequence question answering models.

    Args:
        loss (`torch.FloatTensor` of shape `(1,)`, *optional*, returned when `labels` is provided):
            Total span extraction loss is the sum of a Cross-Entropy for the start and end positions.
        start_logits (`torch.FloatTensor` of shape `(batch_size, sequence_length)`):
            Span-start scores (before SoftMax).
        end_logits (`torch.FloatTensor` of shape `(batch_size, sequence_length)`):
            Span-end scores (before SoftMax).
        past_key_values (`List[torch.FloatTensor]`, *optional*, returned when `use_cache=True` is passed or when `config.use_cache=True`):
            List of `torch.FloatTensor` of length `config.n_layers`, with each tensor of shape `(2, batch_size,
            num_heads, sequence_length, embed_size_per_head)`).

            Contains pre-computed hidden-states (key and values in the attention blocks) of the decoder that can be
            used (see `past_key_values` input) to speed up sequential decoding.
        decoder_hidden_states (`tuple(torch.FloatTensor)`, *optional*, returned when `output_hidden_states=True` is passed or when `config.output_hidden_states=True`):
            Tuple of `torch.FloatTensor` (one for the output of the embeddings + one for the output of each layer) of
            shape `(batch_size, sequence_length, hidden_size)`.

            Hidden-states of the decoder at the output of each layer plus the initial embedding outputs.
        decoder_attentions (`tuple(torch.FloatTensor)`, *optional*, returned when `output_attentions=True` is passed or when `config.output_attentions=True`):
            Tuple of `torch.FloatTensor` (one for each layer) of shape `(batch_size, num_heads, sequence_length,
            sequence_length)`.

            Attentions weights of the decoder, after the attention softmax, used to compute the weighted average in the
            self-attention heads.
        cross_attentions (`tuple(torch.FloatTensor)`, *optional*, returned when `output_attentions=True` is passed or when `config.output_attentions=True`):
            Tuple of `torch.FloatTensor` (one for each layer) of shape `(batch_size, num_heads, sequence_length,
            sequence_length)`.

            Attentions weights of the decoder's cross-attention layer, after the attention softmax, used to compute the
            weighted average in the cross-attention heads.
        encoder_last_hidden_state (`torch.FloatTensor` of shape `(batch_size, sequence_length, hidden_size)`, *optional*):
            Sequence of hidden-states at the output of the last layer of the encoder of the model.
        encoder_hidden_states (`tuple(torch.FloatTensor)`, *optional*, returned when `output_hidden_states=True` is passed or when `config.output_hidden_states=True`):
            Tuple of `torch.FloatTensor` (one for the output of the embeddings + one for the output of each layer) of
            shape `(batch_size, sequence_length, hidden_size)`.

            Hidden-states of the encoder at the output of each layer plus the initial embedding outputs.
        encoder_attentions (`tuple(torch.FloatTensor)`, *optional*, returned when `output_attentions=True` is passed or when `config.output_attentions=True`):
            Tuple of `torch.FloatTensor` (one for each layer) of shape `(batch_size, num_heads, sequence_length,
            sequence_length)`.

            Attentions weights of the encoder, after the attention softmax, used to compute the weighted average in the
            self-attention heads.
        encoder_global_attentions (`tuple(torch.FloatTensor)`, *optional*, returned when `output_attentions=True` is passed or when `config.output_attentions=True`):
            Tuple of `torch.FloatTensor` (one for each layer) of shape `(batch_size, num_heads, sequence_length, x)`,
            where `x` is the number of tokens with global attention mask.

            Global attentions weights after the attention softmax, used to compute the weighted average in the
            self-attention heads. Those are the attention weights from every token with global attention to every token
            in the sequence.
    """
    loss: Optional[torch.FloatTensor] = ...
    start_logits: torch.FloatTensor = ...
    end_logits: torch.FloatTensor = ...
    past_key_values: Optional[List[torch.FloatTensor]] = ...
    decoder_hidden_states: Optional[Tuple[torch.FloatTensor]] = ...
    decoder_attentions: Optional[Tuple[torch.FloatTensor]] = ...
    cross_attentions: Optional[Tuple[torch.FloatTensor]] = ...
    encoder_last_hidden_state: Optional[torch.FloatTensor] = ...
    encoder_hidden_states: Optional[Tuple[torch.FloatTensor]] = ...
    encoder_attentions: Optional[Tuple[torch.FloatTensor]] = ...
    encoder_global_attentions: Optional[Tuple[torch.FloatTensor]] = ...
    def __init__(self, loss, start_logits, end_logits, past_key_values, decoder_hidden_states, decoder_attentions, cross_attentions, encoder_last_hidden_state, encoder_hidden_states, encoder_attentions, encoder_global_attentions) -> None: ...

LED_START_DOCSTRING: str
LED_GENERATION_EXAMPLE: str
LED_INPUTS_DOCSTRING: str

class LEDEncoder(LEDPreTrainedModel):
    """
    Transformer encoder consisting of *config.encoder_layers* self-attention layers. Each layer is a
    [`LEDEncoderLayer`].

    Args:
        config: LEDConfig
        embed_tokens (nn.Embedding): output embedding
    """
    dropout: Incomplete
    layerdrop: Incomplete
    padding_idx: Incomplete
    max_source_positions: Incomplete
    embed_tokens: Incomplete
    embed_positions: Incomplete
    layers: Incomplete
    layernorm_embedding: Incomplete
    gradient_checkpointing: bool
    def __init__(self, config: LEDConfig, embed_tokens: Optional[nn.Embedding] = None) -> None: ...
    def forward(self, input_ids: Incomplete | None = None, attention_mask: Incomplete | None = None, global_attention_mask: Incomplete | None = None, head_mask: Incomplete | None = None, inputs_embeds: Incomplete | None = None, output_attentions: Incomplete | None = None, output_hidden_states: Incomplete | None = None, return_dict: Incomplete | None = None):
        """
        Args:
            input_ids (`torch.LongTensor` of shape `(batch_size, sequence_length)`):
                Indices of input sequence tokens in the vocabulary. Padding will be ignored by default should you
                provide it.

                Indices can be obtained using [`AutoTokenizer`]. See [`PreTrainedTokenizer.encode`] and
                [`PreTrainedTokenizer.__call__`] for details.

                [What are input IDs?](../glossary#input-ids)
            attention_mask (`torch.Tensor` of shape `(batch_size, sequence_length)`, *optional*):
                Mask to avoid performing attention on padding token indices. Mask values selected in `[0, 1]`:

                - 1 for tokens that are **not masked**,
                - 0 for tokens that are **masked**.

                [What are attention masks?](../glossary#attention-mask)
            global_attention_mask (`torch.FloatTensor` of shape `(batch_size, sequence_length)`, *optional*):
                Mask to decide the attention given on each token, local attention or global attention for the encoder.
                Tokens with global attention attends to all other tokens, and all other tokens attend to them. This is
                important for task-specific finetuning because it makes the model more flexible at representing the
                task. For example, for classification, the <s> token should be given global attention. For QA, all
                question tokens should also have global attention. Please refer to the [Longformer
                paper](https://arxiv.org/abs/2004.05150) for more details. Mask values selected in `[0, 1]`:

                - 0 for local attention (a sliding window attention),
                - 1 for global attention (tokens that attend to all other tokens, and all other tokens attend to them).
            head_mask (`torch.Tensor` of shape `(encoder_layers, encoder_attention_heads)`, *optional*):
                Mask to nullify selected heads of the attention modules. Mask values selected in `[0, 1]`:

                - 1 indicates the head is **not masked**,
                - 0 indicates the head is **masked**.
            inputs_embeds (`torch.FloatTensor` of shape `(batch_size, sequence_length, hidden_size)`, *optional*):
                Optionally, instead of passing `input_ids` you can choose to directly pass an embedded representation.
                This is useful if you want more control over how to convert `input_ids` indices into associated vectors
                than the model's internal embedding lookup matrix.
            output_attentions (`bool`, *optional*):
                Whether or not to return the attentions tensors of all attention layers. See `attentions` under
                returned tensors for more detail.
            output_hidden_states (`bool`, *optional*):
                Whether or not to return the hidden states of all layers. See `hidden_states` under returned tensors
                for more detail.
            return_dict (`bool`, *optional*):
                Whether or not to return a [`~utils.ModelOutput`] instead of a plain tuple.
        """

class LEDDecoder(LEDPreTrainedModel):
    """
    Transformer decoder consisting of *config.decoder_layers* layers. Each layer is a [`LEDDecoderLayer`]

    Args:
        config: LEDConfig
        embed_tokens (nn.Embedding): output embedding
    """
    dropout: Incomplete
    layerdrop: Incomplete
    padding_idx: Incomplete
    max_target_positions: Incomplete
    embed_tokens: Incomplete
    embed_positions: Incomplete
    layers: Incomplete
    layernorm_embedding: Incomplete
    gradient_checkpointing: bool
    def __init__(self, config: LEDConfig, embed_tokens: Optional[nn.Embedding] = None) -> None: ...
    def forward(self, input_ids: Incomplete | None = None, attention_mask: Incomplete | None = None, global_attention_mask: Incomplete | None = None, encoder_hidden_states: Incomplete | None = None, encoder_attention_mask: Incomplete | None = None, head_mask: Incomplete | None = None, cross_attn_head_mask: Incomplete | None = None, past_key_values: Incomplete | None = None, inputs_embeds: Incomplete | None = None, use_cache: Incomplete | None = None, output_attentions: Incomplete | None = None, output_hidden_states: Incomplete | None = None, return_dict: Incomplete | None = None):
        """
        Args:
            input_ids (`torch.LongTensor` of shape `(batch_size, sequence_length)`):
                Indices of input sequence tokens in the vocabulary. Padding will be ignored by default should you
                provide it.

                Indices can be obtained using [`AutoTokenizer`]. See [`PreTrainedTokenizer.encode`] and
                [`PreTrainedTokenizer.__call__`] for details.

                [What are input IDs?](../glossary#input-ids)
            attention_mask (`torch.Tensor` of shape `(batch_size, sequence_length)`, *optional*):
                Mask to avoid performing attention on padding token indices. Mask values selected in `[0, 1]`:

                - 1 for tokens that are **not masked**,
                - 0 for tokens that are **masked**.

                [What are attention masks?](../glossary#attention-mask)
            global_attention_mask (`torch.FloatTensor` of shape `(batch_size, sequence_length)`, *optional*):
                Mask to decide the attention given on each token, local attention or global attention. Tokens with
                global attention attends to all other tokens, and all other tokens attend to them. This is important
                for task-specific finetuning because it makes the model more flexible at representing the task. For
                example, for classification, the <s> token should be given global attention. For QA, all question
                tokens should also have global attention. Please refer to the [Longformer
                paper](https://arxiv.org/abs/2004.05150) for more details. Mask values selected in `[0, 1]`:

                - 0 for local attention (a sliding window attention),
                - 1 for global attention (tokens that attend to all other tokens, and all other tokens attend to them).
            encoder_hidden_states (`torch.FloatTensor` of shape `(batch_size, encoder_sequence_length, hidden_size)`, *optional*):
                Sequence of hidden-states at the output of the last layer of the encoder. Used in the cross-attention
                of the decoder.
            encoder_attention_mask (`torch.LongTensor` of shape `(batch_size, encoder_sequence_length)`, *optional*):
                Mask to avoid performing cross-attention on padding tokens indices of encoder input_ids. Mask values
                selected in `[0, 1]`:

                - 1 for tokens that are **not masked**,
                - 0 for tokens that are **masked**.

                [What are attention masks?](../glossary#attention-mask)
            head_mask (`torch.Tensor` of shape `(decoder_layers, decoder_attention_heads)`, *optional*):
                Mask to nullify selected heads of the attention modules. Mask values selected in `[0, 1]`:

                - 1 indicates the head is **not masked**,
                - 0 indicates the head is **masked**.

            cross_attn_head_mask (`torch.Tensor` of shape `(decoder_layers, decoder_attention_heads)`, *optional*):
                Mask to nullify selected heads of the cross-attention modules. Mask values selected in `[0, 1]`:

                - 1 indicates the head is **not masked**,
                - 0 indicates the head is **masked**.

            past_key_values (`tuple(tuple(torch.FloatTensor))`, *optional*, returned when `use_cache=True` is passed or when `config.use_cache=True`):
                Tuple of `tuple(torch.FloatTensor)` of length `config.n_layers`, with each tuple having 2 tensors of
                shape `(batch_size, num_heads, sequence_length, embed_size_per_head)`) and 2 additional tensors of
                shape `(batch_size, num_heads, encoder_sequence_length, embed_size_per_head)`.

                Contains pre-computed hidden-states (key and values in the self-attention blocks and in the
                cross-attention blocks) that can be used (see `past_key_values` input) to speed up sequential decoding.

                If `past_key_values` are used, the user can optionally input only the last `decoder_input_ids` (those
                that don't have their past key value states given to this model) of shape `(batch_size, 1)` instead of
                all `decoder_input_ids` of shape `(batch_size, sequence_length)`. inputs_embeds (`torch.FloatTensor` of
                shape `(batch_size, sequence_length, hidden_size)`, *optional*): Optionally, instead of passing
                `input_ids` you can choose to directly pass an embedded representation. This is useful if you want more
                control over how to convert `input_ids` indices into associated vectors than the model's internal
                embedding lookup matrix.
            output_attentions (`bool`, *optional*):
                Whether or not to return the attentions tensors of all attention layers. See `attentions` under
                returned tensors for more detail.
            output_hidden_states (`bool`, *optional*):
                Whether or not to return the hidden states of all layers. See `hidden_states` under returned tensors
                for more detail.
            return_dict (`bool`, *optional*):
                Whether or not to return a [`~utils.ModelOutput`] instead of a plain tuple.
        """

class LEDModel(LEDPreTrainedModel):
    shared: Incomplete
    encoder: Incomplete
    decoder: Incomplete
    def __init__(self, config: LEDConfig) -> None: ...
    def get_input_embeddings(self): ...
    def set_input_embeddings(self, value) -> None: ...
    def get_encoder(self): ...
    def get_decoder(self): ...
    def forward(self, input_ids: Optional[torch.LongTensor] = None, attention_mask: Optional[torch.Tensor] = None, decoder_input_ids: Optional[torch.LongTensor] = None, decoder_attention_mask: Optional[torch.LongTensor] = None, head_mask: Optional[torch.Tensor] = None, decoder_head_mask: Optional[torch.Tensor] = None, cross_attn_head_mask: Optional[torch.Tensor] = None, encoder_outputs: Optional[Tuple[Tuple[torch.FloatTensor]]] = None, global_attention_mask: Optional[torch.FloatTensor] = None, past_key_values: Optional[Tuple[Tuple[torch.FloatTensor]]] = None, inputs_embeds: Optional[torch.FloatTensor] = None, decoder_inputs_embeds: Optional[torch.FloatTensor] = None, use_cache: Optional[bool] = None, output_attentions: Optional[bool] = None, output_hidden_states: Optional[bool] = None, return_dict: Optional[bool] = None) -> Union[Tuple[torch.Tensor], LEDSeq2SeqModelOutput]: ...

class LEDForConditionalGeneration(LEDPreTrainedModel):
    base_model_prefix: str
    led: Incomplete
    lm_head: Incomplete
    def __init__(self, config: LEDConfig) -> None: ...
    def get_encoder(self): ...
    def get_decoder(self): ...
    def resize_token_embeddings(self, new_num_tokens: int) -> nn.Embedding: ...
    def get_output_embeddings(self): ...
    def set_output_embeddings(self, new_embeddings) -> None: ...
    def forward(self, input_ids: Optional[torch.LongTensor] = None, attention_mask: Optional[torch.Tensor] = None, decoder_input_ids: Optional[torch.LongTensor] = None, decoder_attention_mask: Optional[torch.LongTensor] = None, head_mask: Optional[torch.Tensor] = None, decoder_head_mask: Optional[torch.Tensor] = None, cross_attn_head_mask: Optional[torch.Tensor] = None, encoder_outputs: Optional[Tuple[Tuple[torch.FloatTensor]]] = None, global_attention_mask: Optional[torch.FloatTensor] = None, past_key_values: Optional[Tuple[Tuple[torch.FloatTensor]]] = None, inputs_embeds: Optional[torch.FloatTensor] = None, decoder_inputs_embeds: Optional[torch.FloatTensor] = None, labels: Optional[torch.LongTensor] = None, use_cache: Optional[bool] = None, output_attentions: Optional[bool] = None, output_hidden_states: Optional[bool] = None, return_dict: Optional[bool] = None) -> Union[Tuple[torch.Tensor], LEDSeq2SeqLMOutput]:
        '''
        labels (`torch.LongTensor` of shape `(batch_size, sequence_length)`, *optional*):
            Labels for computing the masked language modeling loss. Indices should either be in `[0, ...,
            config.vocab_size]` or -100 (see `input_ids` docstring). Tokens with indices set to `-100` are ignored
            (masked), the loss is only computed for the tokens with labels in `[0, ..., config.vocab_size]`.

        Returns:

        Conditional generation example:

        ```python
        >>> from transformers import AutoTokenizer, LEDForConditionalGeneration

        >>> tokenizer = AutoTokenizer.from_pretrained("allenai/led-base-16384")
        >>> TXT = "My friends are <mask> but they eat too many carbs."

        >>> model = LEDForConditionalGeneration.from_pretrained("allenai/led-base-16384")
        >>> input_ids = tokenizer([TXT], return_tensors="pt")["input_ids"]

        >>> prediction = model.generate(input_ids)[0]
        >>> print(tokenizer.decode(prediction, skip_special_tokens=True))
        ```'''
    def prepare_inputs_for_generation(self, decoder_input_ids, past_key_values: Incomplete | None = None, attention_mask: Incomplete | None = None, global_attention_mask: Incomplete | None = None, head_mask: Incomplete | None = None, decoder_head_mask: Incomplete | None = None, cross_attn_head_mask: Incomplete | None = None, use_cache: Incomplete | None = None, encoder_outputs: Incomplete | None = None, **kwargs): ...
    def prepare_decoder_input_ids_from_labels(self, labels: torch.Tensor): ...

class LEDForSequenceClassification(LEDPreTrainedModel):
    led: Incomplete
    classification_head: Incomplete
    def __init__(self, config: LEDConfig, **kwargs) -> None: ...
    def forward(self, input_ids: Optional[torch.LongTensor] = None, attention_mask: Optional[torch.Tensor] = None, decoder_input_ids: Optional[torch.LongTensor] = None, decoder_attention_mask: Optional[torch.LongTensor] = None, head_mask: Optional[torch.Tensor] = None, decoder_head_mask: Optional[torch.Tensor] = None, cross_attn_head_mask: Optional[torch.Tensor] = None, encoder_outputs: Optional[Tuple[Tuple[torch.FloatTensor]]] = None, global_attention_mask: Optional[torch.FloatTensor] = None, inputs_embeds: Optional[torch.FloatTensor] = None, decoder_inputs_embeds: Optional[torch.FloatTensor] = None, labels: Optional[torch.LongTensor] = None, use_cache: Optional[bool] = None, output_attentions: Optional[bool] = None, output_hidden_states: Optional[bool] = None, return_dict: Optional[bool] = None) -> Union[Tuple[torch.Tensor], LEDSeq2SeqSequenceClassifierOutput]:
        """
        labels (`torch.LongTensor` of shape `(batch_size,)`, *optional*):
            Labels for computing the sequence classification/regression loss. Indices should be in `[0, ...,
            config.num_labels - 1]`. If `config.num_labels > 1` a classification loss is computed (Cross-Entropy).
        """

class LEDForQuestionAnswering(LEDPreTrainedModel):
    num_labels: Incomplete
    led: Incomplete
    qa_outputs: Incomplete
    def __init__(self, config) -> None: ...
    def forward(self, input_ids: Optional[torch.LongTensor] = None, attention_mask: Optional[torch.Tensor] = None, decoder_input_ids: Optional[torch.LongTensor] = None, decoder_attention_mask: Optional[torch.LongTensor] = None, head_mask: Optional[torch.Tensor] = None, decoder_head_mask: Optional[torch.Tensor] = None, cross_attn_head_mask: Optional[torch.Tensor] = None, encoder_outputs: Optional[Tuple[Tuple[torch.FloatTensor]]] = None, global_attention_mask: Optional[torch.FloatTensor] = None, start_positions: Optional[torch.LongTensor] = None, end_positions: Optional[torch.LongTensor] = None, inputs_embeds: Optional[torch.FloatTensor] = None, decoder_inputs_embeds: Optional[torch.FloatTensor] = None, use_cache: Optional[bool] = None, output_attentions: Optional[bool] = None, output_hidden_states: Optional[bool] = None, return_dict: Optional[bool] = None) -> Union[Tuple[torch.Tensor], LEDSeq2SeqQuestionAnsweringModelOutput]:
        """
        start_positions (`torch.LongTensor` of shape `(batch_size,)`, *optional*):
            Labels for position (index) of the start of the labelled span for computing the token classification loss.
            Positions are clamped to the length of the sequence (*sequence_length*). Position outside of the sequence
            are not taken into account for computing the loss.
        end_positions (`torch.LongTensor` of shape `(batch_size,)`, *optional*):
            Labels for position (index) of the end of the labelled span for computing the token classification loss.
            Positions are clamped to the length of the sequence (*sequence_length*). Position outside of the sequence
            are not taken into account for computing the loss.
        """
