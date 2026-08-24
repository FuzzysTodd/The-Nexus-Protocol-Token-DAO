import torch
from ...activations import gelu as gelu
from ...modeling_outputs import BaseModelOutputWithPastAndCrossAttentions as BaseModelOutputWithPastAndCrossAttentions, BaseModelOutputWithPoolingAndCrossAttentions as BaseModelOutputWithPoolingAndCrossAttentions, MaskedLMOutput as MaskedLMOutput, MultipleChoiceModelOutput as MultipleChoiceModelOutput, QuestionAnsweringModelOutput as QuestionAnsweringModelOutput, SequenceClassifierOutput as SequenceClassifierOutput, TokenClassifierOutput as TokenClassifierOutput
from ...modeling_utils import PreTrainedModel as PreTrainedModel
from ...pytorch_utils import find_pruneable_heads_and_indices as find_pruneable_heads_and_indices, prune_linear_layer as prune_linear_layer
from ...utils import add_code_sample_docstrings as add_code_sample_docstrings, add_start_docstrings as add_start_docstrings, add_start_docstrings_to_model_forward as add_start_docstrings_to_model_forward, logging as logging
from .configuration_ibert import IBertConfig as IBertConfig
from .quant_modules import IntGELU as IntGELU, IntLayerNorm as IntLayerNorm, IntSoftmax as IntSoftmax, QuantAct as QuantAct, QuantEmbedding as QuantEmbedding, QuantLinear as QuantLinear
from _typeshed import Incomplete
from torch import nn
from typing import Optional, Tuple, Union

logger: Incomplete
IBERT_PRETRAINED_MODEL_ARCHIVE_LIST: Incomplete

class IBertEmbeddings(nn.Module):
    """
    Same as BertEmbeddings with a tiny tweak for positional embeddings indexing.
    """
    quant_mode: Incomplete
    embedding_bit: int
    embedding_act_bit: int
    act_bit: int
    ln_input_bit: int
    ln_output_bit: int
    word_embeddings: Incomplete
    token_type_embeddings: Incomplete
    position_embedding_type: Incomplete
    padding_idx: Incomplete
    position_embeddings: Incomplete
    embeddings_act1: Incomplete
    embeddings_act2: Incomplete
    LayerNorm: Incomplete
    output_activation: Incomplete
    dropout: Incomplete
    def __init__(self, config) -> None: ...
    def forward(self, input_ids: Incomplete | None = None, token_type_ids: Incomplete | None = None, position_ids: Incomplete | None = None, inputs_embeds: Incomplete | None = None, past_key_values_length: int = 0): ...
    def create_position_ids_from_inputs_embeds(self, inputs_embeds):
        """
        We are provided embeddings directly. We cannot infer which are padded so just generate sequential position ids.

        Args:
            inputs_embeds: torch.Tensor

        Returns: torch.Tensor
        """

class IBertSelfAttention(nn.Module):
    quant_mode: Incomplete
    weight_bit: int
    bias_bit: int
    act_bit: int
    num_attention_heads: Incomplete
    attention_head_size: Incomplete
    all_head_size: Incomplete
    query: Incomplete
    key: Incomplete
    value: Incomplete
    query_activation: Incomplete
    key_activation: Incomplete
    value_activation: Incomplete
    output_activation: Incomplete
    dropout: Incomplete
    position_embedding_type: Incomplete
    softmax: Incomplete
    def __init__(self, config) -> None: ...
    def transpose_for_scores(self, x): ...
    def forward(self, hidden_states, hidden_states_scaling_factor, attention_mask: Incomplete | None = None, head_mask: Incomplete | None = None, output_attentions: bool = False): ...

class IBertSelfOutput(nn.Module):
    quant_mode: Incomplete
    act_bit: int
    weight_bit: int
    bias_bit: int
    ln_input_bit: int
    ln_output_bit: int
    dense: Incomplete
    ln_input_act: Incomplete
    LayerNorm: Incomplete
    output_activation: Incomplete
    dropout: Incomplete
    def __init__(self, config) -> None: ...
    def forward(self, hidden_states, hidden_states_scaling_factor, input_tensor, input_tensor_scaling_factor): ...

class IBertAttention(nn.Module):
    quant_mode: Incomplete
    self: Incomplete
    output: Incomplete
    pruned_heads: Incomplete
    def __init__(self, config) -> None: ...
    def prune_heads(self, heads) -> None: ...
    def forward(self, hidden_states, hidden_states_scaling_factor, attention_mask: Incomplete | None = None, head_mask: Incomplete | None = None, output_attentions: bool = False): ...

class IBertIntermediate(nn.Module):
    quant_mode: Incomplete
    act_bit: int
    weight_bit: int
    bias_bit: int
    dense: Incomplete
    intermediate_act_fn: Incomplete
    output_activation: Incomplete
    def __init__(self, config) -> None: ...
    def forward(self, hidden_states, hidden_states_scaling_factor): ...

class IBertOutput(nn.Module):
    quant_mode: Incomplete
    act_bit: int
    weight_bit: int
    bias_bit: int
    ln_input_bit: int
    ln_output_bit: int
    dense: Incomplete
    ln_input_act: Incomplete
    LayerNorm: Incomplete
    output_activation: Incomplete
    dropout: Incomplete
    def __init__(self, config) -> None: ...
    def forward(self, hidden_states, hidden_states_scaling_factor, input_tensor, input_tensor_scaling_factor): ...

class IBertLayer(nn.Module):
    quant_mode: Incomplete
    act_bit: int
    seq_len_dim: int
    attention: Incomplete
    intermediate: Incomplete
    output: Incomplete
    pre_intermediate_act: Incomplete
    pre_output_act: Incomplete
    def __init__(self, config) -> None: ...
    def forward(self, hidden_states, hidden_states_scaling_factor, attention_mask: Incomplete | None = None, head_mask: Incomplete | None = None, output_attentions: bool = False): ...
    def feed_forward_chunk(self, attention_output, attention_output_scaling_factor): ...

class IBertEncoder(nn.Module):
    config: Incomplete
    quant_mode: Incomplete
    layer: Incomplete
    def __init__(self, config) -> None: ...
    def forward(self, hidden_states, hidden_states_scaling_factor, attention_mask: Incomplete | None = None, head_mask: Incomplete | None = None, output_attentions: bool = False, output_hidden_states: bool = False, return_dict: bool = True): ...

class IBertPooler(nn.Module):
    quant_mode: Incomplete
    dense: Incomplete
    activation: Incomplete
    def __init__(self, config) -> None: ...
    def forward(self, hidden_states): ...

class IBertPreTrainedModel(PreTrainedModel):
    """
    An abstract class to handle weights initialization and a simple interface for downloading and loading pretrained
    models.
    """
    config_class = IBertConfig
    base_model_prefix: str
    def resize_token_embeddings(self, new_num_tokens: Incomplete | None = None) -> None: ...

IBERT_START_DOCSTRING: str
IBERT_INPUTS_DOCSTRING: str

class IBertModel(IBertPreTrainedModel):
    """

    The model can behave as an encoder (with only self-attention) as well as a decoder, in which case a layer of
    cross-attention is added between the self-attention layers, following the architecture described in [Attention is
    all you need](https://arxiv.org/abs/1706.03762) by Ashish Vaswani, Noam Shazeer, Niki Parmar, Jakob Uszkoreit,
    Llion Jones, Aidan N. Gomez, Lukasz Kaiser and Illia Polosukhin.

    """
    config: Incomplete
    quant_mode: Incomplete
    embeddings: Incomplete
    encoder: Incomplete
    pooler: Incomplete
    def __init__(self, config, add_pooling_layer: bool = True) -> None: ...
    def get_input_embeddings(self): ...
    def set_input_embeddings(self, value) -> None: ...
    def forward(self, input_ids: Optional[torch.LongTensor] = None, attention_mask: Optional[torch.FloatTensor] = None, token_type_ids: Optional[torch.LongTensor] = None, position_ids: Optional[torch.LongTensor] = None, head_mask: Optional[torch.FloatTensor] = None, inputs_embeds: Optional[torch.FloatTensor] = None, output_attentions: Optional[bool] = None, output_hidden_states: Optional[bool] = None, return_dict: Optional[bool] = None) -> Union[BaseModelOutputWithPoolingAndCrossAttentions, Tuple[torch.FloatTensor]]: ...

class IBertForMaskedLM(IBertPreTrainedModel):
    ibert: Incomplete
    lm_head: Incomplete
    def __init__(self, config) -> None: ...
    def get_output_embeddings(self): ...
    def set_output_embeddings(self, new_embeddings) -> None: ...
    def forward(self, input_ids: Optional[torch.LongTensor] = None, attention_mask: Optional[torch.FloatTensor] = None, token_type_ids: Optional[torch.LongTensor] = None, position_ids: Optional[torch.LongTensor] = None, head_mask: Optional[torch.FloatTensor] = None, inputs_embeds: Optional[torch.FloatTensor] = None, labels: Optional[torch.LongTensor] = None, output_attentions: Optional[bool] = None, output_hidden_states: Optional[bool] = None, return_dict: Optional[bool] = None) -> Union[MaskedLMOutput, Tuple[torch.FloatTensor]]:
        """
        labels (`torch.LongTensor` of shape `(batch_size, sequence_length)`, *optional*):
            Labels for computing the masked language modeling loss. Indices should be in `[-100, 0, ...,
            config.vocab_size]` (see `input_ids` docstring) Tokens with indices set to `-100` are ignored (masked), the
            loss is only computed for the tokens with labels in `[0, ..., config.vocab_size]`
        kwargs (`Dict[str, any]`, optional, defaults to *{}*):
            Used to hide legacy arguments that have been deprecated.
        """

class IBertLMHead(nn.Module):
    """I-BERT Head for masked language modeling."""
    dense: Incomplete
    layer_norm: Incomplete
    decoder: Incomplete
    bias: Incomplete
    def __init__(self, config) -> None: ...
    def forward(self, features, **kwargs): ...

class IBertForSequenceClassification(IBertPreTrainedModel):
    num_labels: Incomplete
    ibert: Incomplete
    classifier: Incomplete
    def __init__(self, config) -> None: ...
    def forward(self, input_ids: Optional[torch.LongTensor] = None, attention_mask: Optional[torch.FloatTensor] = None, token_type_ids: Optional[torch.LongTensor] = None, position_ids: Optional[torch.LongTensor] = None, head_mask: Optional[torch.FloatTensor] = None, inputs_embeds: Optional[torch.FloatTensor] = None, labels: Optional[torch.LongTensor] = None, output_attentions: Optional[bool] = None, output_hidden_states: Optional[bool] = None, return_dict: Optional[bool] = None) -> Union[SequenceClassifierOutput, Tuple[torch.FloatTensor]]:
        """
        labels (`torch.LongTensor` of shape `(batch_size,)`, *optional*):
            Labels for computing the sequence classification/regression loss. Indices should be in `[0, ...,
            config.num_labels - 1]`. If `config.num_labels == 1` a regression loss is computed (Mean-Square loss), If
            `config.num_labels > 1` a classification loss is computed (Cross-Entropy).
        """

class IBertForMultipleChoice(IBertPreTrainedModel):
    ibert: Incomplete
    dropout: Incomplete
    classifier: Incomplete
    def __init__(self, config) -> None: ...
    def forward(self, input_ids: Optional[torch.LongTensor] = None, token_type_ids: Optional[torch.LongTensor] = None, attention_mask: Optional[torch.FloatTensor] = None, labels: Optional[torch.LongTensor] = None, position_ids: Optional[torch.LongTensor] = None, head_mask: Optional[torch.FloatTensor] = None, inputs_embeds: Optional[torch.FloatTensor] = None, output_attentions: Optional[bool] = None, output_hidden_states: Optional[bool] = None, return_dict: Optional[bool] = None) -> Union[MultipleChoiceModelOutput, Tuple[torch.FloatTensor]]:
        """
        labels (`torch.LongTensor` of shape `(batch_size,)`, *optional*):
            Labels for computing the multiple choice classification loss. Indices should be in `[0, ...,
            num_choices-1]` where `num_choices` is the size of the second dimension of the input tensors. (See
            `input_ids` above)
        """

class IBertForTokenClassification(IBertPreTrainedModel):
    num_labels: Incomplete
    ibert: Incomplete
    dropout: Incomplete
    classifier: Incomplete
    def __init__(self, config) -> None: ...
    def forward(self, input_ids: Optional[torch.LongTensor] = None, attention_mask: Optional[torch.FloatTensor] = None, token_type_ids: Optional[torch.LongTensor] = None, position_ids: Optional[torch.LongTensor] = None, head_mask: Optional[torch.FloatTensor] = None, inputs_embeds: Optional[torch.FloatTensor] = None, labels: Optional[torch.LongTensor] = None, output_attentions: Optional[bool] = None, output_hidden_states: Optional[bool] = None, return_dict: Optional[bool] = None) -> Union[TokenClassifierOutput, Tuple[torch.FloatTensor]]:
        """
        labels (`torch.LongTensor` of shape `(batch_size, sequence_length)`, *optional*):
            Labels for computing the token classification loss. Indices should be in `[0, ..., config.num_labels - 1]`.
        """

class IBertClassificationHead(nn.Module):
    """Head for sentence-level classification tasks."""
    dense: Incomplete
    dropout: Incomplete
    out_proj: Incomplete
    def __init__(self, config) -> None: ...
    def forward(self, features, **kwargs): ...

class IBertForQuestionAnswering(IBertPreTrainedModel):
    num_labels: Incomplete
    ibert: Incomplete
    qa_outputs: Incomplete
    def __init__(self, config) -> None: ...
    def forward(self, input_ids: Optional[torch.LongTensor] = None, attention_mask: Optional[torch.FloatTensor] = None, token_type_ids: Optional[torch.LongTensor] = None, position_ids: Optional[torch.LongTensor] = None, head_mask: Optional[torch.FloatTensor] = None, inputs_embeds: Optional[torch.FloatTensor] = None, start_positions: Optional[torch.LongTensor] = None, end_positions: Optional[torch.LongTensor] = None, output_attentions: Optional[bool] = None, output_hidden_states: Optional[bool] = None, return_dict: Optional[bool] = None) -> Union[QuestionAnsweringModelOutput, Tuple[torch.FloatTensor]]:
        """
        start_positions (`torch.LongTensor` of shape `(batch_size,)`, *optional*):
            Labels for position (index) of the start of the labelled span for computing the token classification loss.
            Positions are clamped to the length of the sequence (`sequence_length`). Position outside of the sequence
            are not taken into account for computing the loss.
        end_positions (`torch.LongTensor` of shape `(batch_size,)`, *optional*):
            Labels for position (index) of the end of the labelled span for computing the token classification loss.
            Positions are clamped to the length of the sequence (`sequence_length`). Position outside of the sequence
            are not taken into account for computing the loss.
        """

def create_position_ids_from_input_ids(input_ids, padding_idx, past_key_values_length: int = 0):
    """
    Replace non-padding symbols with their position numbers. Position numbers begin at padding_idx+1. Padding symbols
    are ignored. This is modified from fairseq's *utils.make_positions*.

    Args:
    input_ids (`torch.LongTensor`):
           Indices of input sequence tokens in the vocabulary.

    Returns: torch.Tensor
    """
