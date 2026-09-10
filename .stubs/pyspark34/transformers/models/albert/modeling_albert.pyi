import torch
from ...activations import ACT2FN as ACT2FN
from ...modeling_outputs import BaseModelOutput as BaseModelOutput, BaseModelOutputWithPooling as BaseModelOutputWithPooling, MaskedLMOutput as MaskedLMOutput, MultipleChoiceModelOutput as MultipleChoiceModelOutput, QuestionAnsweringModelOutput as QuestionAnsweringModelOutput, SequenceClassifierOutput as SequenceClassifierOutput, TokenClassifierOutput as TokenClassifierOutput
from ...modeling_utils import PreTrainedModel as PreTrainedModel
from ...pytorch_utils import apply_chunking_to_forward as apply_chunking_to_forward, find_pruneable_heads_and_indices as find_pruneable_heads_and_indices, prune_linear_layer as prune_linear_layer
from ...utils import ModelOutput as ModelOutput, add_code_sample_docstrings as add_code_sample_docstrings, add_start_docstrings as add_start_docstrings, add_start_docstrings_to_model_forward as add_start_docstrings_to_model_forward, logging as logging, replace_return_docstrings as replace_return_docstrings
from .configuration_albert import AlbertConfig as AlbertConfig
from _typeshed import Incomplete
from dataclasses import dataclass
from torch import nn
from typing import List, Optional, Tuple, Union

logger: Incomplete
ALBERT_PRETRAINED_MODEL_ARCHIVE_LIST: Incomplete

def load_tf_weights_in_albert(model, config, tf_checkpoint_path):
    """Load tf checkpoints in a pytorch model."""

class AlbertEmbeddings(nn.Module):
    """
    Construct the embeddings from word, position and token_type embeddings.
    """
    word_embeddings: Incomplete
    position_embeddings: Incomplete
    token_type_embeddings: Incomplete
    LayerNorm: Incomplete
    dropout: Incomplete
    position_embedding_type: Incomplete
    def __init__(self, config: AlbertConfig) -> None: ...
    def forward(self, input_ids: Optional[torch.LongTensor] = None, token_type_ids: Optional[torch.LongTensor] = None, position_ids: Optional[torch.LongTensor] = None, inputs_embeds: Optional[torch.FloatTensor] = None, past_key_values_length: int = 0) -> torch.Tensor: ...

class AlbertAttention(nn.Module):
    num_attention_heads: Incomplete
    hidden_size: Incomplete
    attention_head_size: Incomplete
    all_head_size: Incomplete
    query: Incomplete
    key: Incomplete
    value: Incomplete
    attention_dropout: Incomplete
    output_dropout: Incomplete
    dense: Incomplete
    LayerNorm: Incomplete
    pruned_heads: Incomplete
    position_embedding_type: Incomplete
    max_position_embeddings: Incomplete
    distance_embedding: Incomplete
    def __init__(self, config: AlbertConfig) -> None: ...
    def transpose_for_scores(self, x: torch.Tensor) -> torch.Tensor: ...
    def prune_heads(self, heads: List[int]) -> None: ...
    def forward(self, hidden_states: torch.Tensor, attention_mask: Optional[torch.FloatTensor] = None, head_mask: Optional[torch.FloatTensor] = None, output_attentions: bool = False) -> Union[Tuple[torch.Tensor], Tuple[torch.Tensor, torch.Tensor]]: ...

class AlbertLayer(nn.Module):
    config: Incomplete
    chunk_size_feed_forward: Incomplete
    seq_len_dim: int
    full_layer_layer_norm: Incomplete
    attention: Incomplete
    ffn: Incomplete
    ffn_output: Incomplete
    activation: Incomplete
    dropout: Incomplete
    def __init__(self, config: AlbertConfig) -> None: ...
    def forward(self, hidden_states: torch.Tensor, attention_mask: Optional[torch.FloatTensor] = None, head_mask: Optional[torch.FloatTensor] = None, output_attentions: bool = False, output_hidden_states: bool = False) -> Tuple[torch.Tensor, torch.Tensor]: ...
    def ff_chunk(self, attention_output: torch.Tensor) -> torch.Tensor: ...

class AlbertLayerGroup(nn.Module):
    albert_layers: Incomplete
    def __init__(self, config: AlbertConfig) -> None: ...
    def forward(self, hidden_states: torch.Tensor, attention_mask: Optional[torch.FloatTensor] = None, head_mask: Optional[torch.FloatTensor] = None, output_attentions: bool = False, output_hidden_states: bool = False) -> Tuple[Union[torch.Tensor, Tuple[torch.Tensor]], ...]: ...

class AlbertTransformer(nn.Module):
    config: Incomplete
    embedding_hidden_mapping_in: Incomplete
    albert_layer_groups: Incomplete
    def __init__(self, config: AlbertConfig) -> None: ...
    def forward(self, hidden_states: torch.Tensor, attention_mask: Optional[torch.FloatTensor] = None, head_mask: Optional[torch.FloatTensor] = None, output_attentions: bool = False, output_hidden_states: bool = False, return_dict: bool = True) -> Union[BaseModelOutput, Tuple]: ...

class AlbertPreTrainedModel(PreTrainedModel):
    """
    An abstract class to handle weights initialization and a simple interface for downloading and loading pretrained
    models.
    """
    config_class = AlbertConfig
    load_tf_weights = load_tf_weights_in_albert
    base_model_prefix: str

@dataclass
class AlbertForPreTrainingOutput(ModelOutput):
    """
    Output type of [`AlbertForPreTraining`].

    Args:
        loss (*optional*, returned when `labels` is provided, `torch.FloatTensor` of shape `(1,)`):
            Total loss as the sum of the masked language modeling loss and the next sequence prediction
            (classification) loss.
        prediction_logits (`torch.FloatTensor` of shape `(batch_size, sequence_length, config.vocab_size)`):
            Prediction scores of the language modeling head (scores for each vocabulary token before SoftMax).
        sop_logits (`torch.FloatTensor` of shape `(batch_size, 2)`):
            Prediction scores of the next sequence prediction (classification) head (scores of True/False continuation
            before SoftMax).
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
    prediction_logits: torch.FloatTensor = ...
    sop_logits: torch.FloatTensor = ...
    hidden_states: Optional[Tuple[torch.FloatTensor]] = ...
    attentions: Optional[Tuple[torch.FloatTensor]] = ...
    def __init__(self, loss, prediction_logits, sop_logits, hidden_states, attentions) -> None: ...

ALBERT_START_DOCSTRING: str
ALBERT_INPUTS_DOCSTRING: str

class AlbertModel(AlbertPreTrainedModel):
    config_class = AlbertConfig
    base_model_prefix: str
    config: Incomplete
    embeddings: Incomplete
    encoder: Incomplete
    pooler: Incomplete
    pooler_activation: Incomplete
    def __init__(self, config: AlbertConfig, add_pooling_layer: bool = True) -> None: ...
    def get_input_embeddings(self) -> nn.Embedding: ...
    def set_input_embeddings(self, value: nn.Embedding) -> None: ...
    def forward(self, input_ids: Optional[torch.LongTensor] = None, attention_mask: Optional[torch.FloatTensor] = None, token_type_ids: Optional[torch.LongTensor] = None, position_ids: Optional[torch.LongTensor] = None, head_mask: Optional[torch.FloatTensor] = None, inputs_embeds: Optional[torch.FloatTensor] = None, output_attentions: Optional[None] = None, output_hidden_states: Optional[None] = None, return_dict: Optional[None] = None) -> Union[BaseModelOutputWithPooling, Tuple]: ...

class AlbertForPreTraining(AlbertPreTrainedModel):
    albert: Incomplete
    predictions: Incomplete
    sop_classifier: Incomplete
    def __init__(self, config: AlbertConfig) -> None: ...
    def get_output_embeddings(self) -> nn.Linear: ...
    def set_output_embeddings(self, new_embeddings: nn.Linear) -> None: ...
    def get_input_embeddings(self) -> nn.Embedding: ...
    def forward(self, input_ids: Optional[torch.LongTensor] = None, attention_mask: Optional[torch.FloatTensor] = None, token_type_ids: Optional[torch.LongTensor] = None, position_ids: Optional[torch.LongTensor] = None, head_mask: Optional[torch.FloatTensor] = None, inputs_embeds: Optional[torch.FloatTensor] = None, labels: Optional[torch.LongTensor] = None, sentence_order_label: Optional[torch.LongTensor] = None, output_attentions: Optional[bool] = None, output_hidden_states: Optional[bool] = None, return_dict: Optional[bool] = None) -> Union[AlbertForPreTrainingOutput, Tuple]:
        '''
        labels (`torch.LongTensor` of shape `(batch_size, sequence_length)`, *optional*):
            Labels for computing the masked language modeling loss. Indices should be in `[-100, 0, ...,
            config.vocab_size]` (see `input_ids` docstring) Tokens with indices set to `-100` are ignored (masked), the
            loss is only computed for the tokens with labels in `[0, ..., config.vocab_size]`
        sentence_order_label (`torch.LongTensor` of shape `(batch_size,)`, *optional*):
            Labels for computing the next sequence prediction (classification) loss. Input should be a sequence pair
            (see `input_ids` docstring) Indices should be in `[0, 1]`. `0` indicates original order (sequence A, then
            sequence B), `1` indicates switched order (sequence B, then sequence A).

        Returns:

        Example:

        ```python
        >>> from transformers import AutoTokenizer, AlbertForPreTraining
        >>> import torch

        >>> tokenizer = AutoTokenizer.from_pretrained("albert-base-v2")
        >>> model = AlbertForPreTraining.from_pretrained("albert-base-v2")

        >>> input_ids = torch.tensor(tokenizer.encode("Hello, my dog is cute", add_special_tokens=True)).unsqueeze(0)
        >>> # Batch size 1
        >>> outputs = model(input_ids)

        >>> prediction_logits = outputs.prediction_logits
        >>> sop_logits = outputs.sop_logits
        ```'''

class AlbertMLMHead(nn.Module):
    LayerNorm: Incomplete
    bias: Incomplete
    dense: Incomplete
    decoder: Incomplete
    activation: Incomplete
    def __init__(self, config: AlbertConfig) -> None: ...
    def forward(self, hidden_states: torch.Tensor) -> torch.Tensor: ...

class AlbertSOPHead(nn.Module):
    dropout: Incomplete
    classifier: Incomplete
    def __init__(self, config: AlbertConfig) -> None: ...
    def forward(self, pooled_output: torch.Tensor) -> torch.Tensor: ...

class AlbertForMaskedLM(AlbertPreTrainedModel):
    albert: Incomplete
    predictions: Incomplete
    def __init__(self, config) -> None: ...
    def get_output_embeddings(self) -> nn.Linear: ...
    def set_output_embeddings(self, new_embeddings: nn.Linear) -> None: ...
    def get_input_embeddings(self) -> nn.Embedding: ...
    def forward(self, input_ids: Optional[torch.LongTensor] = None, attention_mask: Optional[torch.FloatTensor] = None, token_type_ids: Optional[torch.LongTensor] = None, position_ids: Optional[torch.LongTensor] = None, head_mask: Optional[torch.FloatTensor] = None, inputs_embeds: Optional[torch.FloatTensor] = None, labels: Optional[torch.LongTensor] = None, output_attentions: Optional[bool] = None, output_hidden_states: Optional[bool] = None, return_dict: Optional[bool] = None) -> Union[MaskedLMOutput, Tuple]:
        '''
        labels (`torch.LongTensor` of shape `(batch_size, sequence_length)`, *optional*):
            Labels for computing the masked language modeling loss. Indices should be in `[-100, 0, ...,
            config.vocab_size]` (see `input_ids` docstring) Tokens with indices set to `-100` are ignored (masked), the
            loss is only computed for the tokens with labels in `[0, ..., config.vocab_size]`

        Returns:

        Example:

        ```python
        >>> import torch
        >>> from transformers import AutoTokenizer, AlbertForMaskedLM

        >>> tokenizer = AutoTokenizer.from_pretrained("albert-base-v2")
        >>> model = AlbertForMaskedLM.from_pretrained("albert-base-v2")

        >>> # add mask_token
        >>> inputs = tokenizer("The capital of [MASK] is Paris.", return_tensors="pt")
        >>> with torch.no_grad():
        ...     logits = model(**inputs).logits

        >>> # retrieve index of [MASK]
        >>> mask_token_index = (inputs.input_ids == tokenizer.mask_token_id)[0].nonzero(as_tuple=True)[0]
        >>> predicted_token_id = logits[0, mask_token_index].argmax(axis=-1)
        >>> tokenizer.decode(predicted_token_id)
        \'france\'
        ```

        ```python
        >>> labels = tokenizer("The capital of France is Paris.", return_tensors="pt")["input_ids"]
        >>> labels = torch.where(inputs.input_ids == tokenizer.mask_token_id, labels, -100)
        >>> outputs = model(**inputs, labels=labels)
        >>> round(outputs.loss.item(), 2)
        0.81
        ```
        '''

class AlbertForSequenceClassification(AlbertPreTrainedModel):
    num_labels: Incomplete
    config: Incomplete
    albert: Incomplete
    dropout: Incomplete
    classifier: Incomplete
    def __init__(self, config: AlbertConfig) -> None: ...
    def forward(self, input_ids: Optional[torch.LongTensor] = None, attention_mask: Optional[torch.FloatTensor] = None, token_type_ids: Optional[torch.LongTensor] = None, position_ids: Optional[torch.LongTensor] = None, head_mask: Optional[torch.FloatTensor] = None, inputs_embeds: Optional[torch.FloatTensor] = None, labels: Optional[torch.LongTensor] = None, output_attentions: Optional[bool] = None, output_hidden_states: Optional[bool] = None, return_dict: Optional[bool] = None) -> Union[SequenceClassifierOutput, Tuple]:
        """
        labels (`torch.LongTensor` of shape `(batch_size,)`, *optional*):
            Labels for computing the sequence classification/regression loss. Indices should be in `[0, ...,
            config.num_labels - 1]`. If `config.num_labels == 1` a regression loss is computed (Mean-Square loss), If
            `config.num_labels > 1` a classification loss is computed (Cross-Entropy).
        """

class AlbertForTokenClassification(AlbertPreTrainedModel):
    num_labels: Incomplete
    albert: Incomplete
    dropout: Incomplete
    classifier: Incomplete
    def __init__(self, config: AlbertConfig) -> None: ...
    def forward(self, input_ids: Optional[torch.LongTensor] = None, attention_mask: Optional[torch.FloatTensor] = None, token_type_ids: Optional[torch.LongTensor] = None, position_ids: Optional[torch.LongTensor] = None, head_mask: Optional[torch.FloatTensor] = None, inputs_embeds: Optional[torch.FloatTensor] = None, labels: Optional[torch.LongTensor] = None, output_attentions: Optional[bool] = None, output_hidden_states: Optional[bool] = None, return_dict: Optional[bool] = None) -> Union[TokenClassifierOutput, Tuple]:
        """
        labels (`torch.LongTensor` of shape `(batch_size, sequence_length)`, *optional*):
            Labels for computing the token classification loss. Indices should be in `[0, ..., config.num_labels - 1]`.
        """

class AlbertForQuestionAnswering(AlbertPreTrainedModel):
    num_labels: Incomplete
    albert: Incomplete
    qa_outputs: Incomplete
    def __init__(self, config: AlbertConfig) -> None: ...
    def forward(self, input_ids: Optional[torch.LongTensor] = None, attention_mask: Optional[torch.FloatTensor] = None, token_type_ids: Optional[torch.LongTensor] = None, position_ids: Optional[torch.LongTensor] = None, head_mask: Optional[torch.FloatTensor] = None, inputs_embeds: Optional[torch.FloatTensor] = None, start_positions: Optional[torch.LongTensor] = None, end_positions: Optional[torch.LongTensor] = None, output_attentions: Optional[bool] = None, output_hidden_states: Optional[bool] = None, return_dict: Optional[bool] = None) -> Union[AlbertForPreTrainingOutput, Tuple]:
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

class AlbertForMultipleChoice(AlbertPreTrainedModel):
    albert: Incomplete
    dropout: Incomplete
    classifier: Incomplete
    def __init__(self, config: AlbertConfig) -> None: ...
    def forward(self, input_ids: Optional[torch.LongTensor] = None, attention_mask: Optional[torch.FloatTensor] = None, token_type_ids: Optional[torch.LongTensor] = None, position_ids: Optional[torch.LongTensor] = None, head_mask: Optional[torch.FloatTensor] = None, inputs_embeds: Optional[torch.FloatTensor] = None, labels: Optional[torch.LongTensor] = None, output_attentions: Optional[bool] = None, output_hidden_states: Optional[bool] = None, return_dict: Optional[bool] = None) -> Union[AlbertForPreTrainingOutput, Tuple]:
        """
        labels (`torch.LongTensor` of shape `(batch_size,)`, *optional*):
            Labels for computing the multiple choice classification loss. Indices should be in `[0, ...,
            num_choices-1]` where *num_choices* is the size of the second dimension of the input tensors. (see
            *input_ids* above)
        """
