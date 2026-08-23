import torch
from ...activations import ACT2FN as ACT2FN
from ...modeling_outputs import BaseModelOutput as BaseModelOutput
from ...modeling_utils import PreTrainedModel as PreTrainedModel
from ...utils import ModelOutput as ModelOutput, add_start_docstrings as add_start_docstrings, add_start_docstrings_to_model_forward as add_start_docstrings_to_model_forward, logging as logging, replace_return_docstrings as replace_return_docstrings
from .configuration_xlm_prophetnet import XLMProphetNetConfig as XLMProphetNetConfig
from _typeshed import Incomplete
from dataclasses import dataclass
from torch import Tensor as Tensor, nn
from typing import Optional, Tuple, Union

logger: Incomplete
XLM_PROPHETNET_PRETRAINED_MODEL_ARCHIVE_LIST: Incomplete
XLM_PROPHETNET_START_DOCSTRING: str
XLM_PROPHETNET_INPUTS_DOCSTRING: str
XLM_PROPHETNET_STANDALONE_INPUTS_DOCSTRING: str

def softmax(hidden_state, dim, onnx_trace: bool = False): ...
def ngram_attention_bias(sequence_length, ngram, device, dtype):
    """
    This function computes the bias for the predict stream
    """
def compute_relative_buckets(num_buckets, max_distance, relative_positions, is_bidirectional: bool = False):
    """
    This function computes individual parts of the relative position buckets. For more detail, see paper.
    """
def compute_all_stream_relative_buckets(num_buckets, max_distance, position_ids):
    """
    This function computes both main and predict relative position buckets. For more detail, see paper.
    """

@dataclass
class XLMProphetNetSeq2SeqLMOutput(ModelOutput):
    """
    Base class for sequence-to-sequence language models outputs.

    Args:
        loss (`torch.FloatTensor` of shape `(1,)`, *optional*, returned when `labels` is provided):
            Language modeling loss.
        logits (`torch.FloatTensor` of shape `(batch_size, decoder_sequence_length, config.vocab_size)`):
            Prediction scores of the main stream language modeling head (scores for each vocabulary token before
            SoftMax).
        logits_ngram (`torch.FloatTensor` of shape `(batch_size, ngram * decoder_sequence_length, config.vocab_size)`):
            Prediction scores of the predict stream language modeling head (scores for each vocabulary token before
            SoftMax).
        past_key_values (`List[torch.FloatTensor]`, *optional*, returned when `use_cache=True` is passed or when `config.use_cache=True`):
            List of `torch.FloatTensor` of length `config.n_layers`, with each tensor of shape `(2, batch_size,
            num_attn_heads, decoder_sequence_length, embed_size_per_head)`).

            Contains pre-computed hidden-states (key and values in the attention blocks) of the decoder that can be
            used (see `past_key_values` input) to speed up sequential decoding.
        decoder_hidden_states (`tuple(torch.FloatTensor)`, *optional*, returned when `output_hidden_states=True` is passed or when `config.output_hidden_states=True`):
            Tuple of `torch.FloatTensor` (one for the output of the embeddings + one for the output of each layer) of
            shape `(batch_size, decoder_sequence_length, hidden_size)`.

            Hidden-states of main stream of the decoder at the output of each layer plus the initial embedding outputs.
        decoder_ngram_hidden_states (`tuple(torch.FloatTensor)`, *optional*, returned when `output_hidden_states=True` is passed or when `config.output_hidden_states=True`):
            Tuple of `torch.FloatTensor` (one for the output of the embeddings + one for the output of each layer) of
            shape `(batch_size, ngram * decoder_sequence_length, hidden_size)`.

            Hidden-states of the predict stream of the decoder at the output of each layer plus the initial embedding
            outputs.
        decoder_attentions (`tuple(torch.FloatTensor)`, *optional*, returned when `output_attentions=True` is passed or when `config.output_attentions=True`):
            Tuple of `torch.FloatTensor` (one for each layer) of shape `(batch_size, num_attn_heads,
            decoder_sequence_length, decoder_sequence_length)`.

            Attentions weights of the decoder, after the attention softmax, used to compute the weighted average in the
            self-attention heads.
        decoder_ngram_attentions (`tuple(torch.FloatTensor)`, *optional*, returned when `output_attentions=True` is passed or when `config.output_attentions=True`):
            Tuple of `torch.FloatTensor` (one for each layer) of shape `(batch_size, num_attn_heads,
            decoder_sequence_length, decoder_sequence_length)`.

            Attentions weights of the predict stream of the decoder, after the attention softmax, used to compute the
            weighted average in the self-attention heads.
        cross_attentions (`tuple(torch.FloatTensor)`, *optional*, returned when `output_attentions=True` is passed or when `config.output_attentions=True`):
            Tuple of `torch.FloatTensor` (one for each layer) of shape `(batch_size, num_attn_heads,
            encoder_sequence_length, decoder_sequence_length)`.

            Attentions weights of the cross-attention layer of the decoder, after the attention softmax, used to
            compute the weighted average in the
        encoder_last_hidden_state (`torch.FloatTensor` of shape `(batch_size, encoder_sequence_length, hidden_size)`, *optional*):
            Sequence of hidden-states at the output of the last layer of the encoder of the model.
        encoder_hidden_states (`tuple(torch.FloatTensor)`, *optional*, returned when `output_hidden_states=True` is passed or when `config.output_hidden_states=True`):
            Tuple of `torch.FloatTensor` (one for the output of the embeddings + one for the output of each layer) of
            shape `(batch_size, encoder_sequence_length, hidden_size)`.

            Hidden-states of the encoder at the output of each layer plus the initial embedding outputs.
        encoder_attentions (`tuple(torch.FloatTensor)`, *optional*, returned when `output_attentions=True` is passed or when `config.output_attentions=True`):
            Tuple of `torch.FloatTensor` (one for each layer) of shape `(batch_size, num_attn_heads,
            encoder_sequence_length, encoder_sequence_length)`. Attentions weights of the encoder, after the attention
            softmax, used to compute the weighted average in the self-attention heads.
    """
    loss: Optional[torch.FloatTensor] = ...
    logits: torch.FloatTensor = ...
    logits_ngram: Optional[torch.FloatTensor] = ...
    past_key_values: Optional[Tuple[torch.FloatTensor]] = ...
    decoder_hidden_states: Optional[Tuple[torch.FloatTensor]] = ...
    decoder_ngram_hidden_states: Optional[Tuple[torch.FloatTensor]] = ...
    decoder_attentions: Optional[Tuple[torch.FloatTensor]] = ...
    decoder_ngram_attentions: Optional[Tuple[torch.FloatTensor]] = ...
    cross_attentions: Optional[Tuple[torch.FloatTensor]] = ...
    encoder_last_hidden_state: Optional[torch.FloatTensor] = ...
    encoder_hidden_states: Optional[Tuple[torch.FloatTensor]] = ...
    encoder_attentions: Optional[Tuple[torch.FloatTensor]] = ...
    @property
    def decoder_cross_attentions(self): ...
    def __init__(self, loss, logits, logits_ngram, past_key_values, decoder_hidden_states, decoder_ngram_hidden_states, decoder_attentions, decoder_ngram_attentions, cross_attentions, encoder_last_hidden_state, encoder_hidden_states, encoder_attentions) -> None: ...

@dataclass
class XLMProphetNetSeq2SeqModelOutput(ModelOutput):
    """
    Base class for model encoder's outputs that also contains : pre-computed hidden states that can speed up sequential
    decoding.

    Args:
        last_hidden_state (`torch.FloatTensor` of shape `(batch_size, decoder_sequence_length, hidden_size)`):
            Sequence of main stream hidden-states at the output of the last layer of the decoder of the model.

            If `past_key_values` is used only the last hidden-state of the sequences of shape `(batch_size, 1,
            hidden_size)` is output.
        last_hidden_state_ngram (`torch.FloatTensor` of shape `(batch_size,ngram * decoder_sequence_length, config.vocab_size)`, *optional*):
            Sequence of predict stream hidden-states at the output of the last layer of the decoder of the model.
        past_key_values (`List[torch.FloatTensor]`, *optional*, returned when `use_cache=True` is passed or when `config.use_cache=True`):
            List of `torch.FloatTensor` of length `config.n_layers`, with each tensor of shape `(2, batch_size,
            num_attn_heads, decoder_sequence_length, embed_size_per_head)`).

            Contains pre-computed hidden-states (key and values in the attention blocks) of the decoder that can be
            used (see `past_key_values` input) to speed up sequential decoding.
        decoder_hidden_states (`tuple(torch.FloatTensor)`, *optional*, returned when `output_hidden_states=True` is passed or when `config.output_hidden_states=True`):
            Tuple of `torch.FloatTensor` (one for the output of the embeddings + one for the output of each layer) of
            shape `(batch_size, decoder_sequence_length, hidden_size)`.

            Hidden-states of main stream of the decoder at the output of each layer plus the initial embedding outputs.
        decoder_ngram_hidden_states (`tuple(torch.FloatTensor)`, *optional*, returned when `output_hidden_states=True` is passed or when `config.output_hidden_states=True`):
            Tuple of `torch.FloatTensor` (one for the output of the embeddings + one for the output of each layer) of
            shape `(batch_size, ngram * decoder_sequence_length, hidden_size)`.

            Hidden-states of the predict stream of the decoder at the output of each layer plus the initial embedding
            outputs.
        decoder_attentions (`tuple(torch.FloatTensor)`, *optional*, returned when `output_attentions=True` is passed or when `config.output_attentions=True`):
            Tuple of `torch.FloatTensor` (one for each layer) of shape `(batch_size, num_attn_heads,
            decoder_sequence_length, decoder_sequence_length)`.

            Attentions weights of the decoder, after the attention softmax, used to compute the weighted average in the
            self-attention heads.
        decoder_ngram_attentions (`tuple(torch.FloatTensor)`, *optional*, returned when `output_attentions=True` is passed or when `config.output_attentions=True`):
            Tuple of `torch.FloatTensor` (one for each layer) of shape `(batch_size, num_attn_heads,
            decoder_sequence_length, decoder_sequence_length)`.

            Attentions weights of the predict stream of the decoder, after the attention softmax, used to compute the
            weighted average in the
        cross_attentions (`tuple(torch.FloatTensor)`, *optional*, returned when `output_attentions=True` is passed or when `config.output_attentions=True`):
            Tuple of `torch.FloatTensor` (one for each layer) of shape `(batch_size, num_attn_heads,
            encoder_sequence_length, decoder_sequence_length)`.

            Attentions weights of the cross-attention layer of the decoder, after the attention softmax, used to
            compute the weighted average in the
        encoder_last_hidden_state (`torch.FloatTensor` of shape `(batch_size, encoder_sequence_length, hidden_size)`, *optional*):
            Sequence of hidden-states at the output of the last layer of the encoder of the model.
        encoder_hidden_states (`tuple(torch.FloatTensor)`, *optional*, returned when `output_hidden_states=True` is passed or when `config.output_hidden_states=True`):
            Tuple of `torch.FloatTensor` (one for the output of the embeddings + one for the output of each layer) of
            shape `(batch_size, encoder_sequence_length, hidden_size)`.

            Hidden-states of the encoder at the output of each layer plus the initial embedding outputs.
        encoder_attentions (`tuple(torch.FloatTensor)`, *optional*, returned when `output_attentions=True` is passed or when `config.output_attentions=True`):
            Tuple of `torch.FloatTensor` (one for each layer) of shape `(batch_size, num_attn_heads,
            encoder_sequence_length, encoder_sequence_length)`.

            Attentions weights of the encoder, after the attention softmax, used to compute the weighted average in the
            self-attention heads.
    """
    last_hidden_state: torch.FloatTensor
    last_hidden_state_ngram: Optional[torch.FloatTensor] = ...
    past_key_values: Optional[Tuple[torch.FloatTensor]] = ...
    decoder_hidden_states: Optional[Tuple[torch.FloatTensor]] = ...
    decoder_ngram_hidden_states: Optional[Tuple[torch.FloatTensor]] = ...
    decoder_attentions: Optional[Tuple[torch.FloatTensor]] = ...
    decoder_ngram_attentions: Optional[Tuple[torch.FloatTensor]] = ...
    cross_attentions: Optional[Tuple[torch.FloatTensor]] = ...
    encoder_last_hidden_state: Optional[torch.FloatTensor] = ...
    encoder_hidden_states: Optional[Tuple[torch.FloatTensor]] = ...
    encoder_attentions: Optional[Tuple[torch.FloatTensor]] = ...
    @property
    def decoder_cross_attentions(self): ...
    def __init__(self, last_hidden_state, last_hidden_state_ngram, past_key_values, decoder_hidden_states, decoder_ngram_hidden_states, decoder_attentions, decoder_ngram_attentions, cross_attentions, encoder_last_hidden_state, encoder_hidden_states, encoder_attentions) -> None: ...

@dataclass
class XLMProphetNetDecoderModelOutput(ModelOutput):
    """
    Base class for model's outputs that may also contain a past key/values (to speed up sequential decoding).

    Args:
        last_hidden_state (`torch.FloatTensor` of shape `(batch_size, decoder_sequence_length, hidden_size)`):
            Sequence of main stream hidden-states at the output of the last layer of the decoder of the model.

            If `past_key_values` is used only the last hidden-state of the sequences of shape `(batch_size, 1,
            hidden_size)` is output.
        last_hidden_state_ngram (`torch.FloatTensor` of shape `(batch_size, ngram * decoder_sequence_length, config.vocab_size)`):
            Sequence of predict stream hidden-states at the output of the last layer of the decoder of the model.
        past_key_values (`List[torch.FloatTensor]`, *optional*, returned when `use_cache=True` is passed or when `config.use_cache=True`):
            List of `torch.FloatTensor` of length `config.n_layers`, with each tensor of shape `(2, batch_size,
            num_attn_heads, decoder_sequence_length, embed_size_per_head)`).

            Contains pre-computed hidden-states (key and values in the attention blocks) of the decoder that can be
            used (see `past_key_values` input) to speed up sequential decoding.
        hidden_states (`tuple(torch.FloatTensor)`, *optional*, returned when `output_hidden_states=True` is passed or when `config.output_hidden_states=True`):
            Tuple of `torch.FloatTensor` (one for the output of the embeddings + one for the output of each layer) of
            shape `(batch_size, decoder_sequence_length, hidden_size)`.

            Hidden-states of main stream of the decoder at the output of each layer plus the initial embedding outputs.
        ngram_hidden_states (`tuple(torch.FloatTensor)`, *optional*, returned when `output_hidden_states=True` is passed or when `config.output_hidden_states=True`):
            Tuple of `torch.FloatTensor` (one for the output of the embeddings + one for the output of each layer) of
            shape `(batch_size, ngram * decoder_sequence_length, hidden_size)`.

            Hidden-states of the predict stream of the decoder at the output of each layer plus the initial embedding
            outputs.
        attentions (`tuple(torch.FloatTensor)`, *optional*, returned when `output_attentions=True` is passed or when `config.output_attentions=True`):
            Tuple of `torch.FloatTensor` (one for each layer) of shape `(batch_size, num_attn_heads,
            decoder_sequence_length, decoder_sequence_length)`.

            Attentions weights of the decoder, after the attention softmax, used to compute the weighted average in the
            self-attention heads.
        ngram_attentions (`tuple(torch.FloatTensor)`, *optional*, returned when `output_attentions=True` is passed or when `config.output_attentions=True`):
            Tuple of `torch.FloatTensor` (one for each layer) of shape `(batch_size, num_attn_heads,
            decoder_sequence_length, decoder_sequence_length)`.

            Attentions weights of the predict stream of the decoder, after the attention softmax, used to compute the
            weighted average in the
        cross_attentions (`tuple(torch.FloatTensor)`, *optional*, returned when `output_attentions=True` is passed or when `config.output_attentions=True`):
            Tuple of `torch.FloatTensor` (one for each layer) of shape `(batch_size, num_attn_heads,
            encoder_sequence_length, decoder_sequence_length)`.

            Attentions weights of the cross-attention layer of the decoder, after the attention softmax, used to
            compute the weighted average in the
    """
    last_hidden_state: torch.FloatTensor
    last_hidden_state_ngram: Optional[torch.FloatTensor] = ...
    past_key_values: Optional[Tuple[torch.FloatTensor]] = ...
    hidden_states: Optional[Tuple[torch.FloatTensor]] = ...
    hidden_states_ngram: Optional[Tuple[torch.FloatTensor]] = ...
    attentions: Optional[Tuple[torch.FloatTensor]] = ...
    ngram_attentions: Optional[Tuple[torch.FloatTensor]] = ...
    cross_attentions: Optional[Tuple[torch.FloatTensor]] = ...
    def __init__(self, last_hidden_state, last_hidden_state_ngram, past_key_values, hidden_states, hidden_states_ngram, attentions, ngram_attentions, cross_attentions) -> None: ...

@dataclass
class XLMProphetNetDecoderLMOutput(ModelOutput):
    """
    Base class for model's outputs that may also contain a past key/values (to speed up sequential decoding).

    Args:
        loss (`torch.FloatTensor` of shape `(1,)`, *optional*, returned when `labels` is provided):
            Language modeling loss.
        logits (`torch.FloatTensor` of shape `(batch_size, decoder_sequence_length, config.vocab_size)`):
            Prediction scores of the main stream language modeling head (scores for each vocabulary token before
            SoftMax).
        logits_ngram (`torch.FloatTensor` of shape `(batch_size, ngram * decoder_sequence_length, config.vocab_size)`):
            Prediction scores of the predict stream language modeling head (scores for each vocabulary token before
            SoftMax).
        past_key_values (`List[torch.FloatTensor]`, *optional*, returned when `use_cache=True` is passed or when `config.use_cache=True`):
            List of `torch.FloatTensor` of length `config.n_layers`, with each tensor of shape `(2, batch_size,
            num_attn_heads, decoder_sequence_length, embed_size_per_head)`).

            Contains pre-computed hidden-states (key and values in the attention blocks) of the decoder that can be
            used (see `past_key_values` input) to speed up sequential decoding.
        hidden_states (`tuple(torch.FloatTensor)`, *optional*, returned when `output_hidden_states=True` is passed or when `config.output_hidden_states=True`):
            Tuple of `torch.FloatTensor` (one for the output of the embeddings + one for the output of each layer) of
            shape `(batch_size, decoder_sequence_length, hidden_size)`.

            Hidden-states of main stream of the decoder at the output of each layer plus the initial embedding outputs.
        ngram_hidden_states (`tuple(torch.FloatTensor)`, *optional*, returned when `output_hidden_states=True` is passed or when `config.output_hidden_states=True`):
            Tuple of `torch.FloatTensor` (one for the output of the embeddings + one for the output of each layer) of
            shape `(batch_size, ngram * decoder_sequence_length, hidden_size)`.

            Hidden-states of the predict stream of the decoder at the output of each layer plus the initial embedding
            outputs.
        attentions (`tuple(torch.FloatTensor)`, *optional*, returned when `output_attentions=True` is passed or when `config.output_attentions=True`):
            Tuple of `torch.FloatTensor` (one for each layer) of shape `(batch_size, num_attn_heads,
            decoder_sequence_length, decoder_sequence_length)`.

            Attentions weights of the decoder, after the attention softmax, used to compute the weighted average in the
            self-attention heads.
        ngram_attentions (`tuple(torch.FloatTensor)`, *optional*, returned when `output_attentions=True` is passed or when `config.output_attentions=True`):
            Tuple of `torch.FloatTensor` (one for each layer) of shape `(batch_size, num_attn_heads,
            decoder_sequence_length, decoder_sequence_length)`.

            Attentions weights of the predict stream of the decoder, after the attention softmax, used to compute the
            weighted average in the
        cross_attentions (`tuple(torch.FloatTensor)`, *optional*, returned when `output_attentions=True` is passed or when `config.output_attentions=True`):
            Tuple of `torch.FloatTensor` (one for each layer) of shape `(batch_size, num_attn_heads,
            encoder_sequence_length, decoder_sequence_length)`.

            Attentions weights of the cross-attention layer of the decoder, after the attention softmax, used to
            compute the weighted average in the
    """
    loss: Optional[torch.FloatTensor] = ...
    logits: torch.FloatTensor = ...
    logits_ngram: Optional[torch.FloatTensor] = ...
    past_key_values: Optional[Tuple[torch.FloatTensor]] = ...
    hidden_states: Optional[Tuple[torch.FloatTensor]] = ...
    hidden_states_ngram: Optional[Tuple[torch.FloatTensor]] = ...
    attentions: Optional[Tuple[torch.FloatTensor]] = ...
    ngram_attentions: Optional[Tuple[torch.FloatTensor]] = ...
    cross_attentions: Optional[Tuple[torch.FloatTensor]] = ...
    def __init__(self, loss, logits, logits_ngram, past_key_values, hidden_states, hidden_states_ngram, attentions, ngram_attentions, cross_attentions) -> None: ...

class XLMProphetNetPreTrainedModel(PreTrainedModel):
    config_class = XLMProphetNetConfig
    base_model_prefix: str
    supports_gradient_checkpointing: bool

class XLMProphetNetPositionalEmbeddings(nn.Embedding):
    """
    This module learns positional embeddings up to a fixed maximum size. Padding ids are ignored by either offsetting
    based on padding_idx or by setting padding_idx to None and ensuring that the appropriate position ids are passed to
    the forward function.
    """
    max_length: Incomplete
    def __init__(self, config: XLMProphetNetConfig) -> None: ...
    def forward(self, inputs_shape, device, attention_mask: Incomplete | None = None, past_key_values: Incomplete | None = None, position_ids: Incomplete | None = None): ...

class XLMProphetNetAttention(nn.Module):
    """Multi-headed attention from 'Attention Is All You Need' paper"""
    attention_dropout: Incomplete
    dropout: Incomplete
    num_attn_heads: Incomplete
    head_dim: Incomplete
    key_proj: Incomplete
    value_proj: Incomplete
    query_proj: Incomplete
    out_proj: Incomplete
    def __init__(self, config: XLMProphetNetConfig, num_attn_heads: int) -> None: ...
    def forward(self, hidden_states, key_value_states: Optional[Tensor] = None, attention_mask: Optional[Tensor] = None, layer_head_mask: Optional[Tensor] = None, past_key_value: Optional[Tuple[Tensor]] = None, output_attentions: bool = False) -> Tuple[Tensor, Optional[Tensor]]: ...

class XLMProphetNetFeedForward(nn.Module):
    """
    This is the residual two feed-forward layer block based on the original Transformer implementation.
    """
    activation_fn: Incomplete
    intermediate: Incomplete
    output: Incomplete
    activation_dropout: Incomplete
    dropout: Incomplete
    def __init__(self, config: XLMProphetNetConfig, ffn_dim: int) -> None: ...
    def forward(self, hidden_states): ...

class XLMProphetNetNgramSelfAttention(nn.Module):
    hidden_size: Incomplete
    num_buckets: Incomplete
    relative_max_distance: Incomplete
    num_attn_heads: Incomplete
    dropout: Incomplete
    attention_dropout: Incomplete
    head_dim: Incomplete
    ngram: Incomplete
    key_proj: Incomplete
    value_proj: Incomplete
    query_proj: Incomplete
    out_proj: Incomplete
    relative_pos_embeddings: Incomplete
    onnx_trace: bool
    def __init__(self, config: XLMProphetNetConfig) -> None: ...
    def prepare_for_onnx_export_(self) -> None: ...
    def forward(self, hidden_states, past_key_value: Optional[Tuple[Tensor]] = None, attention_mask: Incomplete | None = None, layer_head_mask: Incomplete | None = None, extended_predict_attention_mask: Incomplete | None = None, main_relative_position_buckets: Incomplete | None = None, predict_relative_position_buckets: Incomplete | None = None, position_ids: Incomplete | None = None): ...
    def get_main_relative_pos_embeddings(self, hidden_states, attn_weights, position_ids, main_relative_position_buckets): ...
    def get_predict_relative_pos_embeddings(self, hidden_states, attn_weights, position_ids, predict_relative_position_buckets): ...

class XLMProphetNetEncoderLayer(nn.Module):
    """
    Encoder block for XLMProphetnet
    """
    self_attn: Incomplete
    self_attn_layer_norm: Incomplete
    feed_forward: Incomplete
    feed_forward_layer_norm: Incomplete
    def __init__(self, config: XLMProphetNetConfig) -> None: ...
    def forward(self, hidden_states, attention_mask, layer_head_mask, output_attentions: bool = False): ...

class XLMProphetNetDecoderLayer(nn.Module):
    """
    Decoder block for XLMProphetnet
    """
    self_attn: Incomplete
    self_attn_layer_norm: Incomplete
    cross_attn: Incomplete
    cross_attn_layer_norm: Incomplete
    feed_forward: Incomplete
    feed_forward_layer_norm: Incomplete
    def __init__(self, config: XLMProphetNetConfig) -> None: ...
    def forward(self, hidden_states, attention_mask: Incomplete | None = None, encoder_hidden_states: Incomplete | None = None, encoder_attn_mask: Incomplete | None = None, layer_head_mask: Incomplete | None = None, cross_attn_layer_head_mask: Incomplete | None = None, extended_predict_attention_mask: Incomplete | None = None, main_relative_position_buckets: Incomplete | None = None, predict_relative_position_buckets: Incomplete | None = None, position_ids: Incomplete | None = None, past_key_value: Incomplete | None = None, use_cache: bool = True, output_attentions: bool = False): ...

class XLMProphetNetEncoder(XLMProphetNetPreTrainedModel):
    """
    word_embeddings  (`torch.nn.Embeddings` of shape `(config.vocab_size, config.hidden_size)`, *optional*):
        The word embedding parameters. This can be used to initialize [`XLMProphetNetEncoder`] with pre-defined word
        embeddings instead of randomly initialized word embeddings.
    """
    word_embeddings: Incomplete
    position_embeddings: Incomplete
    embeddings_layer_norm: Incomplete
    layers: Incomplete
    gradient_checkpointing: bool
    def __init__(self, config: XLMProphetNetConfig, word_embeddings: nn.Embedding = None) -> None: ...
    def get_input_embeddings(self): ...
    def set_input_embeddings(self, value) -> None: ...
    def forward(self, input_ids: Optional[torch.Tensor] = None, attention_mask: Optional[torch.Tensor] = None, head_mask: Optional[torch.Tensor] = None, inputs_embeds: Optional[torch.Tensor] = None, output_attentions: Optional[bool] = None, output_hidden_states: Optional[bool] = None, return_dict: Optional[bool] = None) -> Union[Tuple, BaseModelOutput]:
        '''
        Returns:

        Example:

        ```python
        >>> from transformers import AutoTokenizer, XLMProphetNetEncoder
        >>> import torch

        >>> tokenizer = AutoTokenizer.from_pretrained("patrickvonplaten/xprophetnet-large-uncased-standalone")
        >>> model = XLMProphetNetEncoder.from_pretrained("patrickvonplaten/prophetnet-large-uncased-standalone")
        >>> inputs = tokenizer("Hello, my dog is cute", return_tensors="pt")
        >>> outputs = model(**inputs)

        >>> last_hidden_states = outputs.last_hidden_state
        ```'''

class XLMProphetNetDecoder(XLMProphetNetPreTrainedModel):
    """
    word_embeddings  (`torch.nn.Embeddings` of shape `(config.vocab_size, config.hidden_size)`, *optional*):
        The word embedding parameters. This can be used to initialize [`XLMProphetNetEncoder`] with pre-defined word
        embeddings instead of randomly initialized word embeddings.
    """
    ngram: Incomplete
    num_buckets: Incomplete
    relative_max_distance: Incomplete
    dropout: Incomplete
    max_target_positions: Incomplete
    word_embeddings: Incomplete
    position_embeddings: Incomplete
    ngram_embeddings: Incomplete
    layers: Incomplete
    embeddings_layer_norm: Incomplete
    gradient_checkpointing: bool
    def __init__(self, config: XLMProphetNetConfig, word_embeddings: Optional[nn.Embedding] = None) -> None: ...
    def get_input_embeddings(self): ...
    def set_input_embeddings(self, value) -> None: ...
    def forward(self, input_ids: Optional[torch.Tensor] = None, attention_mask: Optional[torch.Tensor] = None, encoder_hidden_states: Optional[torch.Tensor] = None, encoder_attention_mask: Optional[torch.Tensor] = None, head_mask: Optional[torch.Tensor] = None, cross_attn_head_mask: Optional[torch.Tensor] = None, past_key_values: Optional[Tuple[Tuple[torch.Tensor]]] = None, inputs_embeds: Optional[torch.Tensor] = None, use_cache: Optional[bool] = None, output_attentions: Optional[bool] = None, output_hidden_states: Optional[bool] = None, return_dict: Optional[bool] = None) -> Union[Tuple, XLMProphetNetDecoderModelOutput]:
        '''
        encoder_hidden_states  (`torch.FloatTensor` of shape `(batch_size, sequence_length, hidden_size)`, *optional*):
            Sequence of hidden-states at the output of the last layer of the encoder. Used in the cross-attention if
            the model is configured as a decoder.
        encoder_attention_mask (`torch.FloatTensor` of shape `(batch_size, sequence_length)`, *optional*):
            Mask to avoid performing attention on the padding token indices of the encoder input. This mask is used in
            the cross-attention if the model is configured as a decoder. Mask values selected in `[0, 1]`:
        cross_attn_head_mask (`torch.Tensor` of shape `(decoder_layers, decoder_attention_heads)`, *optional*):
            Mask to nullify selected heads of the cross-attention modules. Mask values selected in `[0, 1]`:

            - 1 indicates the head is **not masked**,
            - 0 indicates the head is **masked**.

        past_key_values (`tuple(tuple(torch.FloatTensor))` of length `config.n_layers` with each tuple having 4 tensors of shape `(batch_size, num_heads, sequence_length - 1, embed_size_per_head)`):
            Contains precomputed key and value hidden-states of the attention blocks. Can be used to speed up decoding.

            If `past_key_values` are used, the user can optionally input only the last `decoder_input_ids` (those that
            don\'t have their past key value states given to this model) of shape `(batch_size, 1)` instead of all
            `decoder_input_ids` of shape `(batch_size, sequence_length)`.
        use_cache (`bool`, *optional*):
            If set to `True`, `past_key_values` key value states are returned and can be used to speed up decoding (see
            `past_key_values`).

            - 1 for tokens that are **not masked**,
            - 0 for tokens that are **masked**.

        Returns:

        Example:

        ```python
        >>> from transformers import AutoTokenizer, XLMProphetNetDecoder
        >>> import torch

        >>> tokenizer = AutoTokenizer.from_pretrained("patrickvonplaten/xprophetnet-large-uncased-standalone")
        >>> model = XLMProphetNetDecoder.from_pretrained(
        ...     "patrickvonplaten/xprophetnet-large-uncased-standalone", add_cross_attention=False
        ... )
        >>> inputs = tokenizer("Hello, my dog is cute", return_tensors="pt")
        >>> outputs = model(**inputs)

        >>> last_hidden_states = outputs.last_hidden_state
        ```'''
    def compute_buffered_relative_buckets(self, position_ids): ...
    def prepare_attention_mask(self, hidden_states, attention_mask): ...
    def prepare_predict_attention_mask(self, hidden_states, attention_mask): ...

class XLMProphetNetModel(XLMProphetNetPreTrainedModel):
    word_embeddings: Incomplete
    encoder: Incomplete
    decoder: Incomplete
    def __init__(self, config: XLMProphetNetConfig) -> None: ...
    def get_input_embeddings(self): ...
    def set_input_embeddings(self, value) -> None: ...
    def get_encoder(self): ...
    def get_decoder(self): ...
    def forward(self, input_ids: Optional[torch.Tensor] = None, attention_mask: Optional[torch.Tensor] = None, decoder_input_ids: Optional[torch.Tensor] = None, decoder_attention_mask: Optional[torch.BoolTensor] = None, head_mask: Optional[torch.Tensor] = None, decoder_head_mask: Optional[torch.Tensor] = None, cross_attn_head_mask: Optional[torch.Tensor] = None, encoder_outputs: Optional[Tuple] = None, past_key_values: Optional[Tuple[Tuple[torch.Tensor]]] = None, inputs_embeds: Optional[torch.Tensor] = None, decoder_inputs_embeds: Optional[torch.Tensor] = None, use_cache: Optional[bool] = None, output_attentions: Optional[bool] = None, output_hidden_states: Optional[bool] = None, return_dict: Optional[bool] = None) -> Union[Tuple, XLMProphetNetSeq2SeqModelOutput]:
        '''
        Returns:

        Example:

        ```python
        >>> from transformers import AutoTokenizer, XLMProphetNetModel

        >>> tokenizer = AutoTokenizer.from_pretrained("patrickvonplaten/xprophetnet-large-uncased-standalone")
        >>> model = XLMProphetNetModel.from_pretrained("patrickvonplaten/xprophetnet-large-uncased-standalone")

        >>> input_ids = tokenizer(
        ...     "Studies have been shown that owning a dog is good for you", return_tensors="pt"
        ... ).input_ids  # Batch size 1
        >>> decoder_input_ids = tokenizer("Studies show that", return_tensors="pt").input_ids  # Batch size 1
        >>> outputs = model(input_ids=input_ids, decoder_input_ids=decoder_input_ids)

        >>> last_hidden_states = outputs.last_hidden_state  # main stream hidden states
        >>> last_hidden_states_ngram = outputs.last_hidden_state_ngram  # predict hidden states
        ```'''

class XLMProphetNetForConditionalGeneration(XLMProphetNetPreTrainedModel):
    prophetnet: Incomplete
    padding_idx: Incomplete
    disable_ngram_loss: Incomplete
    lm_head: Incomplete
    def __init__(self, config: XLMProphetNetConfig) -> None: ...
    def get_output_embeddings(self): ...
    def set_output_embeddings(self, new_embeddings) -> None: ...
    def get_input_embeddings(self): ...
    def forward(self, input_ids: Optional[torch.Tensor] = None, attention_mask: Optional[torch.Tensor] = None, decoder_input_ids: Optional[torch.Tensor] = None, decoder_attention_mask: Optional[torch.BoolTensor] = None, head_mask: Optional[torch.Tensor] = None, decoder_head_mask: Optional[torch.Tensor] = None, cross_attn_head_mask: Optional[torch.Tensor] = None, encoder_outputs: Optional[torch.Tensor] = None, past_key_values: Optional[Tuple[Tuple[torch.Tensor]]] = None, inputs_embeds: Optional[torch.Tensor] = None, decoder_inputs_embeds: Optional[torch.Tensor] = None, labels: Optional[torch.Tensor] = None, use_cache: Optional[bool] = None, output_attentions: Optional[bool] = None, output_hidden_states: Optional[bool] = None, return_dict: Optional[bool] = None) -> Union[Tuple, XLMProphetNetSeq2SeqLMOutput]:
        '''
        labels (`torch.LongTensor` of shape `(batch_size,)`, *optional*):
            Labels for computing the sequence classification/regression loss. Indices should be in `[-100, 0, ...,
            config.vocab_size - 1]`. All labels set to `-100` are ignored (masked), the loss is only computed for
            labels in `[0, ..., config.vocab_size]`

        Returns:

        Example:

        ```python
        >>> from transformers import AutoTokenizer, XLMProphetNetForConditionalGeneration

        >>> tokenizer = AutoTokenizer.from_pretrained("patrickvonplaten/xprophetnet-large-uncased-standalone")
        >>> model = XLMProphetNetForConditionalGeneration.from_pretrained(
        ...     "patrickvonplaten/xprophetnet-large-uncased-standalone"
        ... )

        >>> input_ids = tokenizer(
        ...     "Studies have been shown that owning a dog is good for you", return_tensors="pt"
        ... ).input_ids  # Batch size 1
        >>> decoder_input_ids = tokenizer("Studies show that", return_tensors="pt").input_ids  # Batch size 1
        >>> outputs = model(input_ids=input_ids, decoder_input_ids=decoder_input_ids)

        >>> logits_next_token = outputs.logits  # logits to predict next token as usual
        >>> logits_ngram_next_tokens = outputs.logits_ngram  # logits to predict 2nd, 3rd, ... next tokens
        ```'''
    def prepare_inputs_for_generation(self, decoder_input_ids, past_key_values: Incomplete | None = None, attention_mask: Incomplete | None = None, head_mask: Incomplete | None = None, decoder_head_mask: Incomplete | None = None, cross_attn_head_mask: Incomplete | None = None, use_cache: Incomplete | None = None, encoder_outputs: Incomplete | None = None, **kwargs): ...
    def prepare_decoder_input_ids_from_labels(self, labels: torch.Tensor): ...
    def get_encoder(self): ...
    def get_decoder(self): ...

class XLMProphetNetForCausalLM(XLMProphetNetPreTrainedModel):
    prophetnet: Incomplete
    padding_idx: Incomplete
    disable_ngram_loss: Incomplete
    lm_head: Incomplete
    def __init__(self, config: XLMProphetNetConfig) -> None: ...
    def get_input_embeddings(self): ...
    def set_input_embeddings(self, value) -> None: ...
    def get_output_embeddings(self): ...
    def set_output_embeddings(self, new_embeddings) -> None: ...
    def set_decoder(self, decoder) -> None: ...
    def get_decoder(self): ...
    def forward(self, input_ids: Optional[torch.Tensor] = None, attention_mask: Optional[torch.Tensor] = None, encoder_hidden_states: Optional[torch.Tensor] = None, encoder_attention_mask: Optional[torch.Tensor] = None, head_mask: Optional[torch.Tensor] = None, cross_attn_head_mask: Optional[torch.Tensor] = None, past_key_values: Optional[Tuple[Tuple[torch.Tensor]]] = None, inputs_embeds: Optional[torch.Tensor] = None, labels: Optional[torch.Tensor] = None, use_cache: Optional[bool] = None, output_attentions: Optional[bool] = None, output_hidden_states: Optional[bool] = None, return_dict: Optional[bool] = None) -> Union[Tuple, XLMProphetNetDecoderLMOutput]:
        '''
        encoder_hidden_states (`torch.FloatTensor` of shape `(batch_size, sequence_length, hidden_size)`, *optional*):
            Sequence of hidden-states at the output of the last layer of the encoder. Used in the cross-attention if
            the model is configured as a decoder.
        encoder_attention_mask (`torch.FloatTensor` of shape `(batch_size, sequence_length)`, *optional*):
            Mask to avoid performing attention on the padding token indices of the encoder input. This mask is used in
            the cross-attention if the model is configured as a decoder. Mask values selected in `[0, 1]`:
        cross_attn_head_mask (`torch.Tensor` of shape `(decoder_layers, decoder_attention_heads)`, *optional*):
            Mask to nullify selected heads of the cross-attention modules. Mask values selected in `[0, 1]`:

            - 1 indicates the head is **not masked**,
            - 0 indicates the head is **masked**.

        past_key_values (`tuple(tuple(torch.FloatTensor))` of length `config.n_layers` with each tuple having 4 tensors of shape `(batch_size, num_heads, sequence_length - 1, embed_size_per_head)`):
            Contains precomputed key and value hidden-states of the attention blocks. Can be used to speed up decoding.

            If `past_key_values` are used, the user can optionally input only the last `decoder_input_ids` (those that
            don\'t have their past key value states given to this model) of shape `(batch_size, 1)` instead of all
            `decoder_input_ids` of shape `(batch_size, sequence_length)`.
        use_cache (`bool`, *optional*):
            If set to `True`, `past_key_values` key value states are returned and can be used to speed up decoding (see
            `past_key_values`).

            - 1 for tokens that are **not masked**,
            - 0 for tokens that are **masked**.

        labels (`torch.LongTensor` of shape `(batch_size, sequence_length)`, *optional*):
            Labels for computing the left-to-right language modeling loss (next word prediction). Indices should be in
            `[-100, 0, ..., config.vocab_size]` (see `input_ids` docstring) Tokens with indices set to `-100` are
            ignored (masked), the loss is only computed for the tokens with labels n `[0, ..., config.vocab_size]`

        Returns:

        Example:

        ```python
        >>> from transformers import AutoTokenizer, XLMProphetNetForCausalLM
        >>> import torch

        >>> tokenizer = AutoTokenizer.from_pretrained("patrickvonplaten/xprophetnet-large-uncased-standalone")
        >>> model = XLMProphetNetForCausalLM.from_pretrained("patrickvonplaten/xprophetnet-large-uncased-standalone")
        >>> assert model.config.is_decoder, f"{model.__class__} has to be configured as a decoder."
        >>> inputs = tokenizer("Hello, my dog is cute", return_tensors="pt")
        >>> outputs = model(**inputs)

        >>> logits = outputs.logits

        >>> # Model can also be used with EncoderDecoder framework
        >>> from transformers import BertTokenizer, EncoderDecoderModel, AutoTokenizer
        >>> import torch

        >>> tokenizer_enc = BertTokenizer.from_pretrained("bert-large-uncased")
        >>> tokenizer_dec = AutoTokenizer.from_pretrained("patrickvonplaten/xprophetnet-large-uncased-standalone")
        >>> model = EncoderDecoderModel.from_encoder_decoder_pretrained(
        ...     "bert-large-uncased", "patrickvonplaten/xprophetnet-large-uncased-standalone"
        ... )

        >>> ARTICLE = (
        ...     "the us state department said wednesday it had received no "
        ...     "formal word from bolivia that it was expelling the us ambassador there "
        ...     "but said the charges made against him are `` baseless ."
        ... )
        >>> input_ids = tokenizer_enc(ARTICLE, return_tensors="pt").input_ids
        >>> labels = tokenizer_dec(
        ...     "us rejects charges against its ambassador in bolivia", return_tensors="pt"
        ... ).input_ids
        >>> outputs = model(input_ids=input_ids, decoder_input_ids=labels[:, :-1], labels=labels[:, 1:])

        >>> loss = outputs.loss
        ```'''
    def prepare_inputs_for_generation(self, input_ids, past_key_values: Incomplete | None = None, attention_mask: Incomplete | None = None, head_mask: Incomplete | None = None, use_cache: Incomplete | None = None, **kwargs): ...

class XLMProphetNetDecoderWrapper(XLMProphetNetPreTrainedModel):
    """
    This is a wrapper class, so that [`XLMProphetNetForCausalLM`] can correctly be loaded from pretrained XLMProphetNet
    classes.
    """
    decoder: Incomplete
    def __init__(self, config: XLMProphetNetConfig) -> None: ...
    def forward(self, *args, **kwargs): ...
