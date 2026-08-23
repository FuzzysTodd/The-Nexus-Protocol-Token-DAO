import torch
from ...activations import gelu as gelu
from ...modeling_outputs import BaseModelOutput as BaseModelOutput, MaskedLMOutput as MaskedLMOutput, MultipleChoiceModelOutput as MultipleChoiceModelOutput, QuestionAnsweringModelOutput as QuestionAnsweringModelOutput, SequenceClassifierOutput as SequenceClassifierOutput, TokenClassifierOutput as TokenClassifierOutput
from ...modeling_utils import PreTrainedModel as PreTrainedModel, SQuADHead as SQuADHead, SequenceSummary as SequenceSummary
from ...pytorch_utils import apply_chunking_to_forward as apply_chunking_to_forward, find_pruneable_heads_and_indices as find_pruneable_heads_and_indices, prune_linear_layer as prune_linear_layer
from ...utils import ModelOutput as ModelOutput, add_code_sample_docstrings as add_code_sample_docstrings, add_start_docstrings as add_start_docstrings, add_start_docstrings_to_model_forward as add_start_docstrings_to_model_forward, logging as logging, replace_return_docstrings as replace_return_docstrings
from .configuration_xlm import XLMConfig as XLMConfig
from _typeshed import Incomplete
from dataclasses import dataclass
from torch import nn
from typing import Dict, Optional, Tuple, Union

logger: Incomplete
XLM_PRETRAINED_MODEL_ARCHIVE_LIST: Incomplete

def create_sinusoidal_embeddings(n_pos, dim, out) -> None: ...
def get_masks(slen, lengths, causal, padding_mask: Incomplete | None = None):
    """
    Generate hidden states mask, and optionally an attention mask.
    """

class MultiHeadAttention(nn.Module):
    NEW_ID: Incomplete
    layer_id: Incomplete
    dim: Incomplete
    n_heads: Incomplete
    dropout: Incomplete
    q_lin: Incomplete
    k_lin: Incomplete
    v_lin: Incomplete
    out_lin: Incomplete
    pruned_heads: Incomplete
    def __init__(self, n_heads, dim, config) -> None: ...
    def prune_heads(self, heads) -> None: ...
    def forward(self, input, mask, kv: Incomplete | None = None, cache: Incomplete | None = None, head_mask: Incomplete | None = None, output_attentions: bool = False):
        """
        Self-attention (if kv is None) or attention over source sentence (provided by kv).
        """

class TransformerFFN(nn.Module):
    dropout: Incomplete
    lin1: Incomplete
    lin2: Incomplete
    act: Incomplete
    chunk_size_feed_forward: Incomplete
    seq_len_dim: int
    def __init__(self, in_dim, dim_hidden, out_dim, config) -> None: ...
    def forward(self, input): ...
    def ff_chunk(self, input): ...

class XLMPreTrainedModel(PreTrainedModel):
    """
    An abstract class to handle weights initialization and a simple interface for downloading and loading pretrained
    models.
    """
    config_class = XLMConfig
    load_tf_weights: Incomplete
    base_model_prefix: str
    def __init__(self, *inputs, **kwargs) -> None: ...
    @property
    def dummy_inputs(self): ...

@dataclass
class XLMForQuestionAnsweringOutput(ModelOutput):
    """
    Base class for outputs of question answering models using a `SquadHead`.

    Args:
        loss (`torch.FloatTensor` of shape `(1,)`, *optional*, returned if both `start_positions` and `end_positions` are provided):
            Classification loss as the sum of start token, end token (and is_impossible if provided) classification
            losses.
        start_top_log_probs (`torch.FloatTensor` of shape `(batch_size, config.start_n_top)`, *optional*, returned if `start_positions` or `end_positions` is not provided):
            Log probabilities for the top config.start_n_top start token possibilities (beam-search).
        start_top_index (`torch.LongTensor` of shape `(batch_size, config.start_n_top)`, *optional*, returned if `start_positions` or `end_positions` is not provided):
            Indices for the top config.start_n_top start token possibilities (beam-search).
        end_top_log_probs (`torch.FloatTensor` of shape `(batch_size, config.start_n_top * config.end_n_top)`, *optional*, returned if `start_positions` or `end_positions` is not provided):
            Log probabilities for the top `config.start_n_top * config.end_n_top` end token possibilities
            (beam-search).
        end_top_index (`torch.LongTensor` of shape `(batch_size, config.start_n_top * config.end_n_top)`, *optional*, returned if `start_positions` or `end_positions` is not provided):
            Indices for the top `config.start_n_top * config.end_n_top` end token possibilities (beam-search).
        cls_logits (`torch.FloatTensor` of shape `(batch_size,)`, *optional*, returned if `start_positions` or `end_positions` is not provided):
            Log probabilities for the `is_impossible` label of the answers.
        hidden_states (`tuple(torch.FloatTensor)`, *optional*, returned when `output_hidden_states=True` is passed or when `config.output_hidden_states=True`):
            Tuple of `torch.FloatTensor` (one for the output of the embeddings + one for the output of each layer) of
            shape `(batch_size, sequence_length, hidden_size)`.

            Hidden-states of the model at the output of each layer plus the initial embedding outputs.
        attentions (`tuple(torch.FloatTensor)`, *optional*, returned when `output_attentions=True` is passed or when `config.output_attentions=True`):
            Tuple of `torch.FloatTensor` (one for each layer) of shape `(batch_size, num_heads, sequence_length,
            sequence_length)`.

            Attentions weights after the attention softmax, used to compute the weighted average in the self-attention
            heads.
    """
    loss: Optional[torch.FloatTensor] = ...
    start_top_log_probs: Optional[torch.FloatTensor] = ...
    start_top_index: Optional[torch.LongTensor] = ...
    end_top_log_probs: Optional[torch.FloatTensor] = ...
    end_top_index: Optional[torch.LongTensor] = ...
    cls_logits: Optional[torch.FloatTensor] = ...
    hidden_states: Optional[Tuple[torch.FloatTensor]] = ...
    attentions: Optional[Tuple[torch.FloatTensor]] = ...
    def __init__(self, loss, start_top_log_probs, start_top_index, end_top_log_probs, end_top_index, cls_logits, hidden_states, attentions) -> None: ...

XLM_START_DOCSTRING: str
XLM_INPUTS_DOCSTRING: str

class XLMModel(XLMPreTrainedModel):
    is_encoder: Incomplete
    is_decoder: Incomplete
    causal: Incomplete
    n_langs: Incomplete
    use_lang_emb: Incomplete
    n_words: Incomplete
    eos_index: Incomplete
    pad_index: Incomplete
    dim: Incomplete
    hidden_dim: Incomplete
    n_heads: Incomplete
    n_layers: Incomplete
    dropout: Incomplete
    attention_dropout: Incomplete
    position_embeddings: Incomplete
    lang_embeddings: Incomplete
    embeddings: Incomplete
    layer_norm_emb: Incomplete
    attentions: Incomplete
    layer_norm1: Incomplete
    ffns: Incomplete
    layer_norm2: Incomplete
    def __init__(self, config) -> None: ...
    def get_input_embeddings(self): ...
    def set_input_embeddings(self, new_embeddings) -> None: ...
    def forward(self, input_ids: Optional[torch.Tensor] = None, attention_mask: Optional[torch.Tensor] = None, langs: Optional[torch.Tensor] = None, token_type_ids: Optional[torch.Tensor] = None, position_ids: Optional[torch.Tensor] = None, lengths: Optional[torch.Tensor] = None, cache: Optional[Dict[str, torch.Tensor]] = None, head_mask: Optional[torch.Tensor] = None, inputs_embeds: Optional[torch.Tensor] = None, output_attentions: Optional[bool] = None, output_hidden_states: Optional[bool] = None, return_dict: Optional[bool] = None) -> Union[Tuple, BaseModelOutput]: ...

class XLMPredLayer(nn.Module):
    """
    Prediction layer (cross_entropy or adaptive_softmax).
    """
    asm: Incomplete
    n_words: Incomplete
    pad_index: Incomplete
    proj: Incomplete
    def __init__(self, config) -> None: ...
    def forward(self, x, y: Incomplete | None = None):
        """Compute the loss, and optionally the scores."""

class XLMWithLMHeadModel(XLMPreTrainedModel):
    transformer: Incomplete
    pred_layer: Incomplete
    def __init__(self, config) -> None: ...
    def get_output_embeddings(self): ...
    def set_output_embeddings(self, new_embeddings) -> None: ...
    def prepare_inputs_for_generation(self, input_ids, **kwargs): ...
    def forward(self, input_ids: Optional[torch.Tensor] = None, attention_mask: Optional[torch.Tensor] = None, langs: Optional[torch.Tensor] = None, token_type_ids: Optional[torch.Tensor] = None, position_ids: Optional[torch.Tensor] = None, lengths: Optional[torch.Tensor] = None, cache: Optional[Dict[str, torch.Tensor]] = None, head_mask: Optional[torch.Tensor] = None, inputs_embeds: Optional[torch.Tensor] = None, labels: Optional[torch.Tensor] = None, output_attentions: Optional[bool] = None, output_hidden_states: Optional[bool] = None, return_dict: Optional[bool] = None) -> Union[Tuple, MaskedLMOutput]:
        """
        labels (`torch.LongTensor` of shape `(batch_size, sequence_length)`, *optional*):
            Labels for language modeling. Note that the labels **are shifted** inside the model, i.e. you can set
            `labels = input_ids` Indices are selected in `[-100, 0, ..., config.vocab_size]` All labels set to `-100`
            are ignored (masked), the loss is only computed for labels in `[0, ..., config.vocab_size]`
        """

class XLMForSequenceClassification(XLMPreTrainedModel):
    num_labels: Incomplete
    config: Incomplete
    transformer: Incomplete
    sequence_summary: Incomplete
    def __init__(self, config) -> None: ...
    def forward(self, input_ids: Optional[torch.Tensor] = None, attention_mask: Optional[torch.Tensor] = None, langs: Optional[torch.Tensor] = None, token_type_ids: Optional[torch.Tensor] = None, position_ids: Optional[torch.Tensor] = None, lengths: Optional[torch.Tensor] = None, cache: Optional[Dict[str, torch.Tensor]] = None, head_mask: Optional[torch.Tensor] = None, inputs_embeds: Optional[torch.Tensor] = None, labels: Optional[torch.Tensor] = None, output_attentions: Optional[bool] = None, output_hidden_states: Optional[bool] = None, return_dict: Optional[bool] = None) -> Union[Tuple, SequenceClassifierOutput]:
        """
        labels (`torch.LongTensor` of shape `(batch_size,)`, *optional*):
            Labels for computing the sequence classification/regression loss. Indices should be in `[0, ...,
            config.num_labels - 1]`. If `config.num_labels == 1` a regression loss is computed (Mean-Square loss), If
            `config.num_labels > 1` a classification loss is computed (Cross-Entropy).
        """

class XLMForQuestionAnsweringSimple(XLMPreTrainedModel):
    transformer: Incomplete
    qa_outputs: Incomplete
    def __init__(self, config) -> None: ...
    def forward(self, input_ids: Optional[torch.Tensor] = None, attention_mask: Optional[torch.Tensor] = None, langs: Optional[torch.Tensor] = None, token_type_ids: Optional[torch.Tensor] = None, position_ids: Optional[torch.Tensor] = None, lengths: Optional[torch.Tensor] = None, cache: Optional[Dict[str, torch.Tensor]] = None, head_mask: Optional[torch.Tensor] = None, inputs_embeds: Optional[torch.Tensor] = None, start_positions: Optional[torch.Tensor] = None, end_positions: Optional[torch.Tensor] = None, output_attentions: Optional[bool] = None, output_hidden_states: Optional[bool] = None, return_dict: Optional[bool] = None) -> Union[Tuple, QuestionAnsweringModelOutput]:
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

class XLMForQuestionAnswering(XLMPreTrainedModel):
    transformer: Incomplete
    qa_outputs: Incomplete
    def __init__(self, config) -> None: ...
    def forward(self, input_ids: Optional[torch.Tensor] = None, attention_mask: Optional[torch.Tensor] = None, langs: Optional[torch.Tensor] = None, token_type_ids: Optional[torch.Tensor] = None, position_ids: Optional[torch.Tensor] = None, lengths: Optional[torch.Tensor] = None, cache: Optional[Dict[str, torch.Tensor]] = None, head_mask: Optional[torch.Tensor] = None, inputs_embeds: Optional[torch.Tensor] = None, start_positions: Optional[torch.Tensor] = None, end_positions: Optional[torch.Tensor] = None, is_impossible: Optional[torch.Tensor] = None, cls_index: Optional[torch.Tensor] = None, p_mask: Optional[torch.Tensor] = None, output_attentions: Optional[bool] = None, output_hidden_states: Optional[bool] = None, return_dict: Optional[bool] = None) -> Union[Tuple, XLMForQuestionAnsweringOutput]:
        '''
        start_positions (`torch.LongTensor` of shape `(batch_size,)`, *optional*):
            Labels for position (index) of the start of the labelled span for computing the token classification loss.
            Positions are clamped to the length of the sequence (`sequence_length`). Position outside of the sequence
            are not taken into account for computing the loss.
        end_positions (`torch.LongTensor` of shape `(batch_size,)`, *optional*):
            Labels for position (index) of the end of the labelled span for computing the token classification loss.
            Positions are clamped to the length of the sequence (`sequence_length`). Position outside of the sequence
            are not taken into account for computing the loss.
        is_impossible (`torch.LongTensor` of shape `(batch_size,)`, *optional*):
            Labels whether a question has an answer or no answer (SQuAD 2.0)
        cls_index (`torch.LongTensor` of shape `(batch_size,)`, *optional*):
            Labels for position (index) of the classification token to use as input for computing plausibility of the
            answer.
        p_mask (`torch.FloatTensor` of shape `(batch_size, sequence_length)`, *optional*):
            Optional mask of tokens which can\'t be in answers (e.g. [CLS], [PAD], ...). 1.0 means token should be
            masked. 0.0 mean token is not masked.

        Returns:

        Example:

        ```python
        >>> from transformers import AutoTokenizer, XLMForQuestionAnswering
        >>> import torch

        >>> tokenizer = AutoTokenizer.from_pretrained("xlm-mlm-en-2048")
        >>> model = XLMForQuestionAnswering.from_pretrained("xlm-mlm-en-2048")

        >>> input_ids = torch.tensor(tokenizer.encode("Hello, my dog is cute", add_special_tokens=True)).unsqueeze(
        ...     0
        ... )  # Batch size 1
        >>> start_positions = torch.tensor([1])
        >>> end_positions = torch.tensor([3])

        >>> outputs = model(input_ids, start_positions=start_positions, end_positions=end_positions)
        >>> loss = outputs.loss
        ```'''

class XLMForTokenClassification(XLMPreTrainedModel):
    num_labels: Incomplete
    transformer: Incomplete
    dropout: Incomplete
    classifier: Incomplete
    def __init__(self, config) -> None: ...
    def forward(self, input_ids: Optional[torch.Tensor] = None, attention_mask: Optional[torch.Tensor] = None, langs: Optional[torch.Tensor] = None, token_type_ids: Optional[torch.Tensor] = None, position_ids: Optional[torch.Tensor] = None, lengths: Optional[torch.Tensor] = None, cache: Optional[Dict[str, torch.Tensor]] = None, head_mask: Optional[torch.Tensor] = None, inputs_embeds: Optional[torch.Tensor] = None, labels: Optional[torch.Tensor] = None, output_attentions: Optional[bool] = None, output_hidden_states: Optional[bool] = None, return_dict: Optional[bool] = None) -> Union[Tuple, TokenClassifierOutput]:
        """
        labels (`torch.LongTensor` of shape `(batch_size, sequence_length)`, *optional*):
            Labels for computing the token classification loss. Indices should be in `[0, ..., config.num_labels - 1]`.
        """

class XLMForMultipleChoice(XLMPreTrainedModel):
    transformer: Incomplete
    sequence_summary: Incomplete
    logits_proj: Incomplete
    def __init__(self, config, *inputs, **kwargs) -> None: ...
    def forward(self, input_ids: Optional[torch.Tensor] = None, attention_mask: Optional[torch.Tensor] = None, langs: Optional[torch.Tensor] = None, token_type_ids: Optional[torch.Tensor] = None, position_ids: Optional[torch.Tensor] = None, lengths: Optional[torch.Tensor] = None, cache: Optional[Dict[str, torch.Tensor]] = None, head_mask: Optional[torch.Tensor] = None, inputs_embeds: Optional[torch.Tensor] = None, labels: Optional[torch.Tensor] = None, output_attentions: Optional[bool] = None, output_hidden_states: Optional[bool] = None, return_dict: Optional[bool] = None) -> Union[Tuple, MultipleChoiceModelOutput]:
        """
        labels (`torch.LongTensor` of shape `(batch_size,)`, *optional*):
            Labels for computing the multiple choice classification loss. Indices should be in `[0, ...,
            num_choices-1]` where `num_choices` is the size of the second dimension of the input tensors. (See
            `input_ids` above)
        """
