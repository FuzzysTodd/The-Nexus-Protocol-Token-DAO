import torch
from ...file_utils import add_code_sample_docstrings as add_code_sample_docstrings, add_start_docstrings as add_start_docstrings, add_start_docstrings_to_model_forward as add_start_docstrings_to_model_forward
from ...modeling_outputs import BaseModelOutputWithPastAndCrossAttentions as BaseModelOutputWithPastAndCrossAttentions, BaseModelOutputWithPoolingAndCrossAttentions as BaseModelOutputWithPoolingAndCrossAttentions, MaskedLMOutput as MaskedLMOutput, SequenceClassifierOutput as SequenceClassifierOutput, TokenClassifierOutput as TokenClassifierOutput
from ...modeling_utils import PreTrainedModel as PreTrainedModel, find_pruneable_heads_and_indices as find_pruneable_heads_and_indices, prune_linear_layer as prune_linear_layer
from ...utils import logging as logging
from .configuration_esm import EsmConfig as EsmConfig
from _typeshed import Incomplete
from torch import nn
from typing import List, Optional, Tuple, Union

logger: Incomplete
ESM_PRETRAINED_MODEL_ARCHIVE_LIST: Incomplete

def rotate_half(x): ...
def apply_rotary_pos_emb(x, cos, sin): ...
def gelu(x):
    """
    This is the gelu implementation from the original ESM repo. Using F.gelu yields subtly wrong results.
    """
def symmetrize(x):
    """Make layer symmetric in final two dimensions, used for contact prediction."""
def average_product_correct(x):
    """Perform average product correct, used for contact prediction."""

class RotaryEmbedding(torch.nn.Module):
    """
    Rotary position embeddings based on those in
    [RoFormer](https://huggingface.co/docs/transformers/model_doc/roformer). Query and keys are transformed by rotation
    matrices which depend on their relative positions.
    """
    def __init__(self, dim: int) -> None: ...
    def forward(self, q: torch.Tensor, k: torch.Tensor) -> Tuple[torch.Tensor, torch.Tensor]: ...

class EsmContactPredictionHead(nn.Module):
    """Performs symmetrization, apc, and computes a logistic regression on the output features"""
    in_features: Incomplete
    eos_idx: Incomplete
    regression: Incomplete
    activation: Incomplete
    def __init__(self, in_features: int, bias: bool = True, eos_idx: int = 2) -> None: ...
    def forward(self, tokens, attentions): ...

class EsmEmbeddings(nn.Module):
    """
    Same as BertEmbeddings with a tiny tweak for positional embeddings indexing.
    """
    word_embeddings: Incomplete
    layer_norm: Incomplete
    dropout: Incomplete
    position_embedding_type: Incomplete
    padding_idx: Incomplete
    position_embeddings: Incomplete
    token_dropout: Incomplete
    mask_token_id: Incomplete
    def __init__(self, config) -> None: ...
    def forward(self, input_ids: Incomplete | None = None, attention_mask: Incomplete | None = None, position_ids: Incomplete | None = None, inputs_embeds: Incomplete | None = None, past_key_values_length: int = 0): ...
    def create_position_ids_from_inputs_embeds(self, inputs_embeds):
        """
        We are provided embeddings directly. We cannot infer which are padded so just generate sequential position ids.

        Args:
            inputs_embeds: torch.Tensor

        Returns: torch.Tensor
        """

class EsmSelfAttention(nn.Module):
    num_attention_heads: Incomplete
    attention_head_size: Incomplete
    all_head_size: Incomplete
    query: Incomplete
    key: Incomplete
    value: Incomplete
    dropout: Incomplete
    position_embedding_type: Incomplete
    rotary_embeddings: Incomplete
    max_position_embeddings: Incomplete
    distance_embedding: Incomplete
    is_decoder: Incomplete
    def __init__(self, config, position_embedding_type: Incomplete | None = None) -> None: ...
    def transpose_for_scores(self, x: torch.Tensor) -> torch.Tensor: ...
    def forward(self, hidden_states: torch.Tensor, attention_mask: Optional[torch.FloatTensor] = None, head_mask: Optional[torch.FloatTensor] = None, encoder_hidden_states: Optional[torch.FloatTensor] = None, encoder_attention_mask: Optional[torch.FloatTensor] = None, past_key_value: Optional[Tuple[Tuple[torch.FloatTensor]]] = None, output_attentions: Optional[bool] = False) -> Tuple[torch.Tensor]: ...

class EsmSelfOutput(nn.Module):
    dense: Incomplete
    dropout: Incomplete
    def __init__(self, config) -> None: ...
    def forward(self, hidden_states, input_tensor): ...

class EsmAttention(nn.Module):
    self: Incomplete
    output: Incomplete
    pruned_heads: Incomplete
    LayerNorm: Incomplete
    def __init__(self, config) -> None: ...
    def prune_heads(self, heads) -> None: ...
    def forward(self, hidden_states, attention_mask: Incomplete | None = None, head_mask: Incomplete | None = None, encoder_hidden_states: Incomplete | None = None, encoder_attention_mask: Incomplete | None = None, past_key_value: Incomplete | None = None, output_attentions: bool = False): ...

class EsmIntermediate(nn.Module):
    dense: Incomplete
    def __init__(self, config) -> None: ...
    def forward(self, hidden_states: torch.Tensor) -> torch.Tensor: ...

class EsmOutput(nn.Module):
    dense: Incomplete
    dropout: Incomplete
    def __init__(self, config) -> None: ...
    def forward(self, hidden_states, input_tensor): ...

class EsmLayer(nn.Module):
    chunk_size_feed_forward: Incomplete
    seq_len_dim: int
    attention: Incomplete
    is_decoder: Incomplete
    add_cross_attention: Incomplete
    crossattention: Incomplete
    intermediate: Incomplete
    output: Incomplete
    LayerNorm: Incomplete
    def __init__(self, config) -> None: ...
    def forward(self, hidden_states, attention_mask: Incomplete | None = None, head_mask: Incomplete | None = None, encoder_hidden_states: Incomplete | None = None, encoder_attention_mask: Incomplete | None = None, past_key_value: Incomplete | None = None, output_attentions: bool = False): ...
    def feed_forward_chunk(self, attention_output): ...

class EsmEncoder(nn.Module):
    config: Incomplete
    layer: Incomplete
    emb_layer_norm_after: Incomplete
    gradient_checkpointing: bool
    def __init__(self, config) -> None: ...
    def forward(self, hidden_states, attention_mask: Incomplete | None = None, head_mask: Incomplete | None = None, encoder_hidden_states: Incomplete | None = None, encoder_attention_mask: Incomplete | None = None, past_key_values: Incomplete | None = None, use_cache: Incomplete | None = None, output_attentions: bool = False, output_hidden_states: bool = False, return_dict: bool = True): ...

class EsmPooler(nn.Module):
    dense: Incomplete
    activation: Incomplete
    def __init__(self, config) -> None: ...
    def forward(self, hidden_states: torch.Tensor) -> torch.Tensor: ...

class EsmPreTrainedModel(PreTrainedModel):
    """
    An abstract class to handle weights initialization and a simple interface for downloading and loading pretrained
    models.
    """
    config_class = EsmConfig
    base_model_prefix: str

ESM_START_DOCSTRING: str
ESM_INPUTS_DOCSTRING: str

class EsmModel(EsmPreTrainedModel):
    """

    The model can behave as an encoder (with only self-attention) as well as a decoder, in which case a layer of
    cross-attention is added between the self-attention layers, following the architecture described in [Attention is
    all you need](https://arxiv.org/abs/1706.03762) by Ashish Vaswani, Noam Shazeer, Niki Parmar, Jakob Uszkoreit,
    Llion Jones, Aidan N. Gomez, Lukasz Kaiser and Illia Polosukhin.

    To behave as an decoder the model needs to be initialized with the `is_decoder` argument of the configuration set
    to `True`. To be used in a Seq2Seq model, the model needs to initialized with both `is_decoder` argument and
    `add_cross_attention` set to `True`; an `encoder_hidden_states` is then expected as an input to the forward pass.
    """
    supports_gradient_checkpointing: bool
    config: Incomplete
    embeddings: Incomplete
    encoder: Incomplete
    pooler: Incomplete
    contact_head: Incomplete
    def __init__(self, config, add_pooling_layer: bool = True) -> None: ...
    def get_input_embeddings(self): ...
    def set_input_embeddings(self, value) -> None: ...
    def forward(self, input_ids: Optional[torch.Tensor] = None, attention_mask: Optional[torch.Tensor] = None, position_ids: Optional[torch.Tensor] = None, head_mask: Optional[torch.Tensor] = None, inputs_embeds: Optional[torch.Tensor] = None, encoder_hidden_states: Optional[torch.Tensor] = None, encoder_attention_mask: Optional[torch.Tensor] = None, past_key_values: Optional[List[torch.FloatTensor]] = None, use_cache: Optional[bool] = None, output_attentions: Optional[bool] = None, output_hidden_states: Optional[bool] = None, return_dict: Optional[bool] = None) -> Union[Tuple[torch.Tensor], BaseModelOutputWithPoolingAndCrossAttentions]:
        """
        encoder_hidden_states  (`torch.FloatTensor` of shape `(batch_size, sequence_length, hidden_size)`, *optional*):
            Sequence of hidden-states at the output of the last layer of the encoder. Used in the cross-attention if
            the model is configured as a decoder.
        encoder_attention_mask (`torch.FloatTensor` of shape `(batch_size, sequence_length)`, *optional*):
            Mask to avoid performing attention on the padding token indices of the encoder input. This mask is used in
            the cross-attention if the model is configured as a decoder. Mask values selected in `[0, 1]`:

            - 1 for tokens that are **not masked**,
            - 0 for tokens that are **masked**.
        past_key_values (`tuple(tuple(torch.FloatTensor))` of length `config.n_layers` with each tuple having 4 tensors of shape `(batch_size, num_heads, sequence_length - 1, embed_size_per_head)`):
            Contains precomputed key and value hidden states of the attention blocks. Can be used to speed up decoding.

            If `past_key_values` are used, the user can optionally input only the last `decoder_input_ids` (those that
            don't have their past key value states given to this model) of shape `(batch_size, 1)` instead of all
            `decoder_input_ids` of shape `(batch_size, sequence_length)`.
        use_cache (`bool`, *optional*):
            If set to `True`, `past_key_values` key value states are returned and can be used to speed up decoding (see
            `past_key_values`).
        """
    def predict_contacts(self, tokens, attention_mask): ...

class EsmForMaskedLM(EsmPreTrainedModel):
    esm: Incomplete
    lm_head: Incomplete
    def __init__(self, config) -> None: ...
    def get_output_embeddings(self): ...
    def set_output_embeddings(self, new_embeddings) -> None: ...
    def forward(self, input_ids: Optional[torch.LongTensor] = None, attention_mask: Optional[torch.Tensor] = None, position_ids: Optional[torch.LongTensor] = None, head_mask: Optional[torch.Tensor] = None, inputs_embeds: Optional[torch.FloatTensor] = None, encoder_hidden_states: Optional[torch.FloatTensor] = None, encoder_attention_mask: Optional[torch.Tensor] = None, labels: Optional[torch.LongTensor] = None, output_attentions: Optional[bool] = None, output_hidden_states: Optional[bool] = None, return_dict: Optional[bool] = None) -> Union[Tuple, MaskedLMOutput]:
        """
        labels (`torch.LongTensor` of shape `(batch_size, sequence_length)`, *optional*):
            Labels for computing the masked language modeling loss. Indices should be in `[-100, 0, ...,
            config.vocab_size]` (see `input_ids` docstring) Tokens with indices set to `-100` are ignored (masked), the
            loss is only computed for the tokens with labels in `[0, ..., config.vocab_size]`
        kwargs (`Dict[str, any]`, optional, defaults to *{}*):
            Used to hide legacy arguments that have been deprecated.
        """
    def predict_contacts(self, tokens, attention_mask): ...

class EsmLMHead(nn.Module):
    """ESM Head for masked language modeling."""
    dense: Incomplete
    layer_norm: Incomplete
    decoder: Incomplete
    bias: Incomplete
    def __init__(self, config) -> None: ...
    def forward(self, features, **kwargs): ...

class EsmForSequenceClassification(EsmPreTrainedModel):
    num_labels: Incomplete
    config: Incomplete
    esm: Incomplete
    classifier: Incomplete
    def __init__(self, config) -> None: ...
    def forward(self, input_ids: Optional[torch.LongTensor] = None, attention_mask: Optional[torch.Tensor] = None, position_ids: Optional[torch.LongTensor] = None, head_mask: Optional[torch.Tensor] = None, inputs_embeds: Optional[torch.FloatTensor] = None, labels: Optional[torch.LongTensor] = None, output_attentions: Optional[bool] = None, output_hidden_states: Optional[bool] = None, return_dict: Optional[bool] = None) -> Union[Tuple, SequenceClassifierOutput]:
        """
        labels (`torch.LongTensor` of shape `(batch_size,)`, *optional*):
            Labels for computing the sequence classification/regression loss. Indices should be in `[0, ...,
            config.num_labels - 1]`. If `config.num_labels == 1` a regression loss is computed (Mean-Square loss), If
            `config.num_labels > 1` a classification loss is computed (Cross-Entropy).
        """

class EsmForTokenClassification(EsmPreTrainedModel):
    num_labels: Incomplete
    esm: Incomplete
    dropout: Incomplete
    classifier: Incomplete
    def __init__(self, config) -> None: ...
    def forward(self, input_ids: Optional[torch.LongTensor] = None, attention_mask: Optional[torch.Tensor] = None, position_ids: Optional[torch.LongTensor] = None, head_mask: Optional[torch.Tensor] = None, inputs_embeds: Optional[torch.FloatTensor] = None, labels: Optional[torch.LongTensor] = None, output_attentions: Optional[bool] = None, output_hidden_states: Optional[bool] = None, return_dict: Optional[bool] = None) -> Union[Tuple, TokenClassifierOutput]:
        """
        labels (`torch.LongTensor` of shape `(batch_size, sequence_length)`, *optional*):
            Labels for computing the token classification loss. Indices should be in `[0, ..., config.num_labels - 1]`.
        """

class EsmClassificationHead(nn.Module):
    """Head for sentence-level classification tasks."""
    dense: Incomplete
    dropout: Incomplete
    out_proj: Incomplete
    def __init__(self, config) -> None: ...
    def forward(self, features, **kwargs): ...

def create_position_ids_from_input_ids(input_ids, padding_idx, past_key_values_length: int = 0):
    """
    Replace non-padding symbols with their position numbers. Position numbers begin at padding_idx+1. Padding symbols
    are ignored. This is modified from fairseq's `utils.make_positions`.

    Args:
        x: torch.Tensor x:

    Returns: torch.Tensor
    """
