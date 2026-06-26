import torch
from ...activations import ACT2FN as ACT2FN, gelu as gelu
from ...modeling_outputs import BaseModelOutput as BaseModelOutput, BaseModelOutputWithPooling as BaseModelOutputWithPooling
from ...modeling_utils import PreTrainedModel as PreTrainedModel
from ...pytorch_utils import apply_chunking_to_forward as apply_chunking_to_forward
from ...utils import ModelOutput as ModelOutput, add_code_sample_docstrings as add_code_sample_docstrings, add_start_docstrings as add_start_docstrings, add_start_docstrings_to_model_forward as add_start_docstrings_to_model_forward, logging as logging, replace_return_docstrings as replace_return_docstrings
from .configuration_luke import LukeConfig as LukeConfig
from _typeshed import Incomplete
from dataclasses import dataclass
from torch import nn
from typing import Optional, Tuple, Union

logger: Incomplete
LUKE_PRETRAINED_MODEL_ARCHIVE_LIST: Incomplete

@dataclass
class BaseLukeModelOutputWithPooling(BaseModelOutputWithPooling):
    """
    Base class for outputs of the LUKE model.

    Args:
        last_hidden_state (`torch.FloatTensor` of shape `(batch_size, sequence_length, hidden_size)`):
            Sequence of hidden-states at the output of the last layer of the model.
        entity_last_hidden_state (`torch.FloatTensor` of shape `(batch_size, entity_length, hidden_size)`):
            Sequence of entity hidden-states at the output of the last layer of the model.
        pooler_output (`torch.FloatTensor` of shape `(batch_size, hidden_size)`):
            Last layer hidden-state of the first token of the sequence (classification token) further processed by a
            Linear layer and a Tanh activation function.
        hidden_states (`tuple(torch.FloatTensor)`, *optional*, returned when `output_hidden_states=True` is passed or when `config.output_hidden_states=True`):
            Tuple of `torch.FloatTensor` (one for the output of the embeddings + one for the output of each layer) of
            shape `(batch_size, sequence_length, hidden_size)`. Hidden-states of the model at the output of each layer
            plus the initial embedding outputs.
        entity_hidden_states (`tuple(torch.FloatTensor)`, *optional*, returned when `output_hidden_states=True` is passed or when `config.output_hidden_states=True`):
            Tuple of `torch.FloatTensor` (one for the output of the embeddings + one for the output of each layer) of
            shape `(batch_size, entity_length, hidden_size)`. Entity hidden-states of the model at the output of each
            layer plus the initial entity embedding outputs.
        attentions (`tuple(torch.FloatTensor)`, *optional*, returned when `output_attentions=True` is passed or when `config.output_attentions=True`):
            Tuple of `torch.FloatTensor` (one for each layer) of shape `(batch_size, num_heads, sequence_length +
            entity_length, sequence_length + entity_length)`. Attentions weights after the attention softmax, used to
            compute the weighted average in the self-attention heads.
    """
    entity_last_hidden_state: torch.FloatTensor = ...
    entity_hidden_states: Optional[Tuple[torch.FloatTensor]] = ...
    def __init__(self, last_hidden_state, pooler_output, hidden_states, attentions, entity_last_hidden_state, entity_hidden_states) -> None: ...

@dataclass
class BaseLukeModelOutput(BaseModelOutput):
    """
    Base class for model's outputs, with potential hidden states and attentions.

    Args:
        last_hidden_state (`torch.FloatTensor` of shape `(batch_size, sequence_length, hidden_size)`):
            Sequence of hidden-states at the output of the last layer of the model.
        entity_last_hidden_state (`torch.FloatTensor` of shape `(batch_size, entity_length, hidden_size)`):
            Sequence of entity hidden-states at the output of the last layer of the model.
        hidden_states (`tuple(torch.FloatTensor)`, *optional*, returned when `output_hidden_states=True` is passed or when `config.output_hidden_states=True`):
            Tuple of `torch.FloatTensor` (one for the output of the embeddings + one for the output of each layer) of
            shape `(batch_size, sequence_length, hidden_size)`.

            Hidden-states of the model at the output of each layer plus the initial embedding outputs.
        entity_hidden_states (`tuple(torch.FloatTensor)`, *optional*, returned when `output_hidden_states=True` is passed or when `config.output_hidden_states=True`):
            Tuple of `torch.FloatTensor` (one for the output of the embeddings + one for the output of each layer) of
            shape `(batch_size, entity_length, hidden_size)`. Entity hidden-states of the model at the output of each
            layer plus the initial entity embedding outputs.
        attentions (`tuple(torch.FloatTensor)`, *optional*, returned when `output_attentions=True` is passed or when `config.output_attentions=True`):
            Tuple of `torch.FloatTensor` (one for each layer) of shape `(batch_size, num_heads, sequence_length,
            sequence_length)`.

            Attentions weights after the attention softmax, used to compute the weighted average in the self-attention
            heads.
    """
    entity_last_hidden_state: torch.FloatTensor = ...
    entity_hidden_states: Optional[Tuple[torch.FloatTensor]] = ...
    def __init__(self, last_hidden_state, hidden_states, attentions, entity_last_hidden_state, entity_hidden_states) -> None: ...

@dataclass
class LukeMaskedLMOutput(ModelOutput):
    """
    Base class for model's outputs, with potential hidden states and attentions.

    Args:
        loss (`torch.FloatTensor` of shape `(1,)`, *optional*, returned when `labels` is provided):
            The sum of masked language modeling (MLM) loss and entity prediction loss.
        mlm_loss (`torch.FloatTensor` of shape `(1,)`, *optional*, returned when `labels` is provided):
            Masked language modeling (MLM) loss.
        mep_loss (`torch.FloatTensor` of shape `(1,)`, *optional*, returned when `labels` is provided):
            Masked entity prediction (MEP) loss.
        logits (`torch.FloatTensor` of shape `(batch_size, sequence_length, config.vocab_size)`):
            Prediction scores of the language modeling head (scores for each vocabulary token before SoftMax).
        entity_logits (`torch.FloatTensor` of shape `(batch_size, sequence_length, config.vocab_size)`):
            Prediction scores of the entity prediction head (scores for each entity vocabulary token before SoftMax).
        hidden_states (`tuple(torch.FloatTensor)`, *optional*, returned when `output_hidden_states=True` is passed or when `config.output_hidden_states=True`):
            Tuple of `torch.FloatTensor` (one for the output of the embeddings + one for the output of each layer) of
            shape `(batch_size, sequence_length, hidden_size)`.

            Hidden-states of the model at the output of each layer plus the initial embedding outputs.
        entity_hidden_states (`tuple(torch.FloatTensor)`, *optional*, returned when `output_hidden_states=True` is passed or when `config.output_hidden_states=True`):
            Tuple of `torch.FloatTensor` (one for the output of the embeddings + one for the output of each layer) of
            shape `(batch_size, entity_length, hidden_size)`. Entity hidden-states of the model at the output of each
            layer plus the initial entity embedding outputs.
        attentions (`tuple(torch.FloatTensor)`, *optional*, returned when `output_attentions=True` is passed or when `config.output_attentions=True`):
            Tuple of `torch.FloatTensor` (one for each layer) of shape `(batch_size, num_heads, sequence_length,
            sequence_length)`.

            Attentions weights after the attention softmax, used to compute the weighted average in the self-attention
            heads.
    """
    loss: Optional[torch.FloatTensor] = ...
    mlm_loss: Optional[torch.FloatTensor] = ...
    mep_loss: Optional[torch.FloatTensor] = ...
    logits: torch.FloatTensor = ...
    entity_logits: torch.FloatTensor = ...
    hidden_states: Optional[Tuple[torch.FloatTensor]] = ...
    entity_hidden_states: Optional[Tuple[torch.FloatTensor]] = ...
    attentions: Optional[Tuple[torch.FloatTensor]] = ...
    def __init__(self, loss, mlm_loss, mep_loss, logits, entity_logits, hidden_states, entity_hidden_states, attentions) -> None: ...

@dataclass
class EntityClassificationOutput(ModelOutput):
    """
    Outputs of entity classification models.

    Args:
        loss (`torch.FloatTensor` of shape `(1,)`, *optional*, returned when `labels` is provided):
            Classification loss.
        logits (`torch.FloatTensor` of shape `(batch_size, config.num_labels)`):
            Classification scores (before SoftMax).
        hidden_states (`tuple(torch.FloatTensor)`, *optional*, returned when `output_hidden_states=True` is passed or when `config.output_hidden_states=True`):
            Tuple of `torch.FloatTensor` (one for the output of the embeddings + one for the output of each layer) of
            shape `(batch_size, sequence_length, hidden_size)`. Hidden-states of the model at the output of each layer
            plus the initial embedding outputs.
        entity_hidden_states (`tuple(torch.FloatTensor)`, *optional*, returned when `output_hidden_states=True` is passed or when `config.output_hidden_states=True`):
            Tuple of `torch.FloatTensor` (one for the output of the embeddings + one for the output of each layer) of
            shape `(batch_size, entity_length, hidden_size)`. Entity hidden-states of the model at the output of each
            layer plus the initial entity embedding outputs.
        attentions (`tuple(torch.FloatTensor)`, *optional*, returned when `output_attentions=True` is passed or when `config.output_attentions=True`):
            Tuple of `torch.FloatTensor` (one for each layer) of shape `(batch_size, num_heads, sequence_length,
            sequence_length)`. Attentions weights after the attention softmax, used to compute the weighted average in
            the self-attention heads.
    """
    loss: Optional[torch.FloatTensor] = ...
    logits: torch.FloatTensor = ...
    hidden_states: Optional[Tuple[torch.FloatTensor]] = ...
    entity_hidden_states: Optional[Tuple[torch.FloatTensor]] = ...
    attentions: Optional[Tuple[torch.FloatTensor]] = ...
    def __init__(self, loss, logits, hidden_states, entity_hidden_states, attentions) -> None: ...

@dataclass
class EntityPairClassificationOutput(ModelOutput):
    """
    Outputs of entity pair classification models.

    Args:
        loss (`torch.FloatTensor` of shape `(1,)`, *optional*, returned when `labels` is provided):
            Classification loss.
        logits (`torch.FloatTensor` of shape `(batch_size, config.num_labels)`):
            Classification scores (before SoftMax).
        hidden_states (`tuple(torch.FloatTensor)`, *optional*, returned when `output_hidden_states=True` is passed or when `config.output_hidden_states=True`):
            Tuple of `torch.FloatTensor` (one for the output of the embeddings + one for the output of each layer) of
            shape `(batch_size, sequence_length, hidden_size)`. Hidden-states of the model at the output of each layer
            plus the initial embedding outputs.
        entity_hidden_states (`tuple(torch.FloatTensor)`, *optional*, returned when `output_hidden_states=True` is passed or when `config.output_hidden_states=True`):
            Tuple of `torch.FloatTensor` (one for the output of the embeddings + one for the output of each layer) of
            shape `(batch_size, entity_length, hidden_size)`. Entity hidden-states of the model at the output of each
            layer plus the initial entity embedding outputs.
        attentions (`tuple(torch.FloatTensor)`, *optional*, returned when `output_attentions=True` is passed or when `config.output_attentions=True`):
            Tuple of `torch.FloatTensor` (one for each layer) of shape `(batch_size, num_heads, sequence_length,
            sequence_length)`. Attentions weights after the attention softmax, used to compute the weighted average in
            the self-attention heads.
    """
    loss: Optional[torch.FloatTensor] = ...
    logits: torch.FloatTensor = ...
    hidden_states: Optional[Tuple[torch.FloatTensor]] = ...
    entity_hidden_states: Optional[Tuple[torch.FloatTensor]] = ...
    attentions: Optional[Tuple[torch.FloatTensor]] = ...
    def __init__(self, loss, logits, hidden_states, entity_hidden_states, attentions) -> None: ...

@dataclass
class EntitySpanClassificationOutput(ModelOutput):
    """
    Outputs of entity span classification models.

    Args:
        loss (`torch.FloatTensor` of shape `(1,)`, *optional*, returned when `labels` is provided):
            Classification loss.
        logits (`torch.FloatTensor` of shape `(batch_size, entity_length, config.num_labels)`):
            Classification scores (before SoftMax).
        hidden_states (`tuple(torch.FloatTensor)`, *optional*, returned when `output_hidden_states=True` is passed or when `config.output_hidden_states=True`):
            Tuple of `torch.FloatTensor` (one for the output of the embeddings + one for the output of each layer) of
            shape `(batch_size, sequence_length, hidden_size)`. Hidden-states of the model at the output of each layer
            plus the initial embedding outputs.
        entity_hidden_states (`tuple(torch.FloatTensor)`, *optional*, returned when `output_hidden_states=True` is passed or when `config.output_hidden_states=True`):
            Tuple of `torch.FloatTensor` (one for the output of the embeddings + one for the output of each layer) of
            shape `(batch_size, entity_length, hidden_size)`. Entity hidden-states of the model at the output of each
            layer plus the initial entity embedding outputs.
        attentions (`tuple(torch.FloatTensor)`, *optional*, returned when `output_attentions=True` is passed or when `config.output_attentions=True`):
            Tuple of `torch.FloatTensor` (one for each layer) of shape `(batch_size, num_heads, sequence_length,
            sequence_length)`. Attentions weights after the attention softmax, used to compute the weighted average in
            the self-attention heads.
    """
    loss: Optional[torch.FloatTensor] = ...
    logits: torch.FloatTensor = ...
    hidden_states: Optional[Tuple[torch.FloatTensor]] = ...
    entity_hidden_states: Optional[Tuple[torch.FloatTensor]] = ...
    attentions: Optional[Tuple[torch.FloatTensor]] = ...
    def __init__(self, loss, logits, hidden_states, entity_hidden_states, attentions) -> None: ...

@dataclass
class LukeSequenceClassifierOutput(ModelOutput):
    """
    Outputs of sentence classification models.

    Args:
        loss (`torch.FloatTensor` of shape `(1,)`, *optional*, returned when `labels` is provided):
            Classification (or regression if config.num_labels==1) loss.
        logits (`torch.FloatTensor` of shape `(batch_size, config.num_labels)`):
            Classification (or regression if config.num_labels==1) scores (before SoftMax).
        hidden_states (`tuple(torch.FloatTensor)`, *optional*, returned when `output_hidden_states=True` is passed or when `config.output_hidden_states=True`):
            Tuple of `torch.FloatTensor` (one for the output of the embeddings, if the model has an embedding layer, +
            one for the output of each layer) of shape `(batch_size, sequence_length, hidden_size)`.

            Hidden-states of the model at the output of each layer plus the optional initial embedding outputs.
        entity_hidden_states (`tuple(torch.FloatTensor)`, *optional*, returned when `output_hidden_states=True` is passed or when `config.output_hidden_states=True`):
            Tuple of `torch.FloatTensor` (one for the output of the embeddings + one for the output of each layer) of
            shape `(batch_size, entity_length, hidden_size)`. Entity hidden-states of the model at the output of each
            layer plus the initial entity embedding outputs.
        attentions (`tuple(torch.FloatTensor)`, *optional*, returned when `output_attentions=True` is passed or when `config.output_attentions=True`):
            Tuple of `torch.FloatTensor` (one for each layer) of shape `(batch_size, num_heads, sequence_length,
            sequence_length)`.

            Attentions weights after the attention softmax, used to compute the weighted average in the self-attention
            heads.
    """
    loss: Optional[torch.FloatTensor] = ...
    logits: torch.FloatTensor = ...
    hidden_states: Optional[Tuple[torch.FloatTensor]] = ...
    entity_hidden_states: Optional[Tuple[torch.FloatTensor]] = ...
    attentions: Optional[Tuple[torch.FloatTensor]] = ...
    def __init__(self, loss, logits, hidden_states, entity_hidden_states, attentions) -> None: ...

@dataclass
class LukeTokenClassifierOutput(ModelOutput):
    """
    Base class for outputs of token classification models.

    Args:
        loss (`torch.FloatTensor` of shape `(1,)`, *optional*, returned when `labels` is provided) :
            Classification loss.
        logits (`torch.FloatTensor` of shape `(batch_size, sequence_length, config.num_labels)`):
            Classification scores (before SoftMax).
        hidden_states (`tuple(torch.FloatTensor)`, *optional*, returned when `output_hidden_states=True` is passed or when `config.output_hidden_states=True`):
            Tuple of `torch.FloatTensor` (one for the output of the embeddings, if the model has an embedding layer, +
            one for the output of each layer) of shape `(batch_size, sequence_length, hidden_size)`.

            Hidden-states of the model at the output of each layer plus the optional initial embedding outputs.
        entity_hidden_states (`tuple(torch.FloatTensor)`, *optional*, returned when `output_hidden_states=True` is passed or when `config.output_hidden_states=True`):
            Tuple of `torch.FloatTensor` (one for the output of the embeddings + one for the output of each layer) of
            shape `(batch_size, entity_length, hidden_size)`. Entity hidden-states of the model at the output of each
            layer plus the initial entity embedding outputs.
        attentions (`tuple(torch.FloatTensor)`, *optional*, returned when `output_attentions=True` is passed or when `config.output_attentions=True`):
            Tuple of `torch.FloatTensor` (one for each layer) of shape `(batch_size, num_heads, sequence_length,
            sequence_length)`.

            Attentions weights after the attention softmax, used to compute the weighted average in the self-attention
            heads.
    """
    loss: Optional[torch.FloatTensor] = ...
    logits: torch.FloatTensor = ...
    hidden_states: Optional[Tuple[torch.FloatTensor]] = ...
    entity_hidden_states: Optional[Tuple[torch.FloatTensor]] = ...
    attentions: Optional[Tuple[torch.FloatTensor]] = ...
    def __init__(self, loss, logits, hidden_states, entity_hidden_states, attentions) -> None: ...

@dataclass
class LukeQuestionAnsweringModelOutput(ModelOutput):
    """
    Outputs of question answering models.

    Args:
        loss (`torch.FloatTensor` of shape `(1,)`, *optional*, returned when `labels` is provided):
            Total span extraction loss is the sum of a Cross-Entropy for the start and end positions.
        start_logits (`torch.FloatTensor` of shape `(batch_size, sequence_length)`):
            Span-start scores (before SoftMax).
        end_logits (`torch.FloatTensor` of shape `(batch_size, sequence_length)`):
            Span-end scores (before SoftMax).
        hidden_states (`tuple(torch.FloatTensor)`, *optional*, returned when `output_hidden_states=True` is passed or when `config.output_hidden_states=True`):
            Tuple of `torch.FloatTensor` (one for the output of the embeddings, if the model has an embedding layer, +
            one for the output of each layer) of shape `(batch_size, sequence_length, hidden_size)`.

            Hidden-states of the model at the output of each layer plus the optional initial embedding outputs.
        entity_hidden_states (`tuple(torch.FloatTensor)`, *optional*, returned when `output_hidden_states=True` is passed or when `config.output_hidden_states=True`):
            Tuple of `torch.FloatTensor` (one for the output of the embeddings + one for the output of each layer) of
            shape `(batch_size, entity_length, hidden_size)`. Entity hidden-states of the model at the output of each
            layer plus the initial entity embedding outputs.
        attentions (`tuple(torch.FloatTensor)`, *optional*, returned when `output_attentions=True` is passed or when `config.output_attentions=True`):
            Tuple of `torch.FloatTensor` (one for each layer) of shape `(batch_size, num_heads, sequence_length,
            sequence_length)`.

            Attentions weights after the attention softmax, used to compute the weighted average in the self-attention
            heads.
    """
    loss: Optional[torch.FloatTensor] = ...
    start_logits: torch.FloatTensor = ...
    end_logits: torch.FloatTensor = ...
    hidden_states: Optional[Tuple[torch.FloatTensor]] = ...
    entity_hidden_states: Optional[Tuple[torch.FloatTensor]] = ...
    attentions: Optional[Tuple[torch.FloatTensor]] = ...
    def __init__(self, loss, start_logits, end_logits, hidden_states, entity_hidden_states, attentions) -> None: ...

@dataclass
class LukeMultipleChoiceModelOutput(ModelOutput):
    """
    Outputs of multiple choice models.

    Args:
        loss (`torch.FloatTensor` of shape *(1,)*, *optional*, returned when `labels` is provided):
            Classification loss.
        logits (`torch.FloatTensor` of shape `(batch_size, num_choices)`):
            *num_choices* is the second dimension of the input tensors. (see *input_ids* above).

            Classification scores (before SoftMax).
        hidden_states (`tuple(torch.FloatTensor)`, *optional*, returned when `output_hidden_states=True` is passed or when `config.output_hidden_states=True`):
            Tuple of `torch.FloatTensor` (one for the output of the embeddings, if the model has an embedding layer, +
            one for the output of each layer) of shape `(batch_size, sequence_length, hidden_size)`.

            Hidden-states of the model at the output of each layer plus the optional initial embedding outputs.
        entity_hidden_states (`tuple(torch.FloatTensor)`, *optional*, returned when `output_hidden_states=True` is passed or when `config.output_hidden_states=True`):
            Tuple of `torch.FloatTensor` (one for the output of the embeddings + one for the output of each layer) of
            shape `(batch_size, entity_length, hidden_size)`. Entity hidden-states of the model at the output of each
            layer plus the initial entity embedding outputs.
        attentions (`tuple(torch.FloatTensor)`, *optional*, returned when `output_attentions=True` is passed or when `config.output_attentions=True`):
            Tuple of `torch.FloatTensor` (one for each layer) of shape `(batch_size, num_heads, sequence_length,
            sequence_length)`.

            Attentions weights after the attention softmax, used to compute the weighted average in the self-attention
            heads.
    """
    loss: Optional[torch.FloatTensor] = ...
    logits: torch.FloatTensor = ...
    hidden_states: Optional[Tuple[torch.FloatTensor]] = ...
    entity_hidden_states: Optional[Tuple[torch.FloatTensor]] = ...
    attentions: Optional[Tuple[torch.FloatTensor]] = ...
    def __init__(self, loss, logits, hidden_states, entity_hidden_states, attentions) -> None: ...

class LukeEmbeddings(nn.Module):
    """
    Same as BertEmbeddings with a tiny tweak for positional embeddings indexing.
    """
    word_embeddings: Incomplete
    position_embeddings: Incomplete
    token_type_embeddings: Incomplete
    LayerNorm: Incomplete
    dropout: Incomplete
    padding_idx: Incomplete
    def __init__(self, config) -> None: ...
    def forward(self, input_ids: Incomplete | None = None, token_type_ids: Incomplete | None = None, position_ids: Incomplete | None = None, inputs_embeds: Incomplete | None = None): ...
    def create_position_ids_from_inputs_embeds(self, inputs_embeds):
        """
        We are provided embeddings directly. We cannot infer which are padded so just generate sequential position ids.

        Args:
            inputs_embeds: torch.Tensor

        Returns: torch.Tensor
        """

class LukeEntityEmbeddings(nn.Module):
    config: Incomplete
    entity_embeddings: Incomplete
    entity_embedding_dense: Incomplete
    position_embeddings: Incomplete
    token_type_embeddings: Incomplete
    LayerNorm: Incomplete
    dropout: Incomplete
    def __init__(self, config: LukeConfig) -> None: ...
    def forward(self, entity_ids: torch.LongTensor, position_ids: torch.LongTensor, token_type_ids: torch.LongTensor = None): ...

class LukeSelfAttention(nn.Module):
    num_attention_heads: Incomplete
    attention_head_size: Incomplete
    all_head_size: Incomplete
    use_entity_aware_attention: Incomplete
    query: Incomplete
    key: Incomplete
    value: Incomplete
    w2e_query: Incomplete
    e2w_query: Incomplete
    e2e_query: Incomplete
    dropout: Incomplete
    def __init__(self, config) -> None: ...
    def transpose_for_scores(self, x): ...
    def forward(self, word_hidden_states, entity_hidden_states, attention_mask: Incomplete | None = None, head_mask: Incomplete | None = None, output_attentions: bool = False): ...

class LukeSelfOutput(nn.Module):
    dense: Incomplete
    LayerNorm: Incomplete
    dropout: Incomplete
    def __init__(self, config) -> None: ...
    def forward(self, hidden_states: torch.Tensor, input_tensor: torch.Tensor) -> torch.Tensor: ...

class LukeAttention(nn.Module):
    self: Incomplete
    output: Incomplete
    pruned_heads: Incomplete
    def __init__(self, config) -> None: ...
    def prune_heads(self, heads) -> None: ...
    def forward(self, word_hidden_states, entity_hidden_states, attention_mask: Incomplete | None = None, head_mask: Incomplete | None = None, output_attentions: bool = False): ...

class LukeIntermediate(nn.Module):
    dense: Incomplete
    intermediate_act_fn: Incomplete
    def __init__(self, config) -> None: ...
    def forward(self, hidden_states: torch.Tensor) -> torch.Tensor: ...

class LukeOutput(nn.Module):
    dense: Incomplete
    LayerNorm: Incomplete
    dropout: Incomplete
    def __init__(self, config) -> None: ...
    def forward(self, hidden_states: torch.Tensor, input_tensor: torch.Tensor) -> torch.Tensor: ...

class LukeLayer(nn.Module):
    chunk_size_feed_forward: Incomplete
    seq_len_dim: int
    attention: Incomplete
    intermediate: Incomplete
    output: Incomplete
    def __init__(self, config) -> None: ...
    def forward(self, word_hidden_states, entity_hidden_states, attention_mask: Incomplete | None = None, head_mask: Incomplete | None = None, output_attentions: bool = False): ...
    def feed_forward_chunk(self, attention_output): ...

class LukeEncoder(nn.Module):
    config: Incomplete
    layer: Incomplete
    gradient_checkpointing: bool
    def __init__(self, config) -> None: ...
    def forward(self, word_hidden_states, entity_hidden_states, attention_mask: Incomplete | None = None, head_mask: Incomplete | None = None, output_attentions: bool = False, output_hidden_states: bool = False, return_dict: bool = True): ...

class LukePooler(nn.Module):
    dense: Incomplete
    activation: Incomplete
    def __init__(self, config) -> None: ...
    def forward(self, hidden_states: torch.Tensor) -> torch.Tensor: ...

class EntityPredictionHeadTransform(nn.Module):
    dense: Incomplete
    transform_act_fn: Incomplete
    LayerNorm: Incomplete
    def __init__(self, config) -> None: ...
    def forward(self, hidden_states): ...

class EntityPredictionHead(nn.Module):
    config: Incomplete
    transform: Incomplete
    decoder: Incomplete
    bias: Incomplete
    def __init__(self, config) -> None: ...
    def forward(self, hidden_states): ...

class LukePreTrainedModel(PreTrainedModel):
    """
    An abstract class to handle weights initialization and a simple interface for downloading and loading pretrained
    models.
    """
    config_class = LukeConfig
    base_model_prefix: str
    supports_gradient_checkpointing: bool

LUKE_START_DOCSTRING: str
LUKE_INPUTS_DOCSTRING: str

class LukeModel(LukePreTrainedModel):
    config: Incomplete
    embeddings: Incomplete
    entity_embeddings: Incomplete
    encoder: Incomplete
    pooler: Incomplete
    def __init__(self, config: LukeConfig, add_pooling_layer: bool = True) -> None: ...
    def get_input_embeddings(self): ...
    def set_input_embeddings(self, value) -> None: ...
    def get_entity_embeddings(self): ...
    def set_entity_embeddings(self, value) -> None: ...
    def forward(self, input_ids: Optional[torch.LongTensor] = None, attention_mask: Optional[torch.FloatTensor] = None, token_type_ids: Optional[torch.LongTensor] = None, position_ids: Optional[torch.LongTensor] = None, entity_ids: Optional[torch.LongTensor] = None, entity_attention_mask: Optional[torch.FloatTensor] = None, entity_token_type_ids: Optional[torch.LongTensor] = None, entity_position_ids: Optional[torch.LongTensor] = None, head_mask: Optional[torch.FloatTensor] = None, inputs_embeds: Optional[torch.FloatTensor] = None, output_attentions: Optional[bool] = None, output_hidden_states: Optional[bool] = None, return_dict: Optional[bool] = None) -> Union[Tuple, BaseLukeModelOutputWithPooling]:
        '''

        Returns:

        Examples:

        ```python
        >>> from transformers import AutoTokenizer, LukeModel

        >>> tokenizer = AutoTokenizer.from_pretrained("studio-ousia/luke-base")
        >>> model = LukeModel.from_pretrained("studio-ousia/luke-base")
        # Compute the contextualized entity representation corresponding to the entity mention "Beyoncé"

        >>> text = "Beyoncé lives in Los Angeles."
        >>> entity_spans = [(0, 7)]  # character-based entity span corresponding to "Beyoncé"

        >>> encoding = tokenizer(text, entity_spans=entity_spans, add_prefix_space=True, return_tensors="pt")
        >>> outputs = model(**encoding)
        >>> word_last_hidden_state = outputs.last_hidden_state
        >>> entity_last_hidden_state = outputs.entity_last_hidden_state
        # Input Wikipedia entities to obtain enriched contextualized representations of word tokens

        >>> text = "Beyoncé lives in Los Angeles."
        >>> entities = [
        ...     "Beyoncé",
        ...     "Los Angeles",
        ... ]  # Wikipedia entity titles corresponding to the entity mentions "Beyoncé" and "Los Angeles"
        >>> entity_spans = [
        ...     (0, 7),
        ...     (17, 28),
        ... ]  # character-based entity spans corresponding to "Beyoncé" and "Los Angeles"

        >>> encoding = tokenizer(
        ...     text, entities=entities, entity_spans=entity_spans, add_prefix_space=True, return_tensors="pt"
        ... )
        >>> outputs = model(**encoding)
        >>> word_last_hidden_state = outputs.last_hidden_state
        >>> entity_last_hidden_state = outputs.entity_last_hidden_state
        ```'''
    def get_extended_attention_mask(self, word_attention_mask: torch.LongTensor, entity_attention_mask: Optional[torch.LongTensor]):
        """
        Makes broadcastable attention and causal masks so that future and masked tokens are ignored.

        Arguments:
            word_attention_mask (`torch.LongTensor`):
                Attention mask for word tokens with ones indicating tokens to attend to, zeros for tokens to ignore.
            entity_attention_mask (`torch.LongTensor`, *optional*):
                Attention mask for entity tokens with ones indicating tokens to attend to, zeros for tokens to ignore.

        Returns:
            `torch.Tensor` The extended attention mask, with a the same dtype as `attention_mask.dtype`.
        """

def create_position_ids_from_input_ids(input_ids, padding_idx):
    """
    Replace non-padding symbols with their position numbers. Position numbers begin at padding_idx+1. Padding symbols
    are ignored. This is modified from fairseq's `utils.make_positions`.

    Args:
        x: torch.Tensor x:

    Returns: torch.Tensor
    """

class LukeLMHead(nn.Module):
    """Roberta Head for masked language modeling."""
    dense: Incomplete
    layer_norm: Incomplete
    decoder: Incomplete
    bias: Incomplete
    def __init__(self, config) -> None: ...
    def forward(self, features, **kwargs): ...

class LukeForMaskedLM(LukePreTrainedModel):
    luke: Incomplete
    lm_head: Incomplete
    entity_predictions: Incomplete
    loss_fn: Incomplete
    def __init__(self, config) -> None: ...
    def tie_weights(self) -> None: ...
    def get_output_embeddings(self): ...
    def set_output_embeddings(self, new_embeddings) -> None: ...
    def forward(self, input_ids: Optional[torch.LongTensor] = None, attention_mask: Optional[torch.FloatTensor] = None, token_type_ids: Optional[torch.LongTensor] = None, position_ids: Optional[torch.LongTensor] = None, entity_ids: Optional[torch.LongTensor] = None, entity_attention_mask: Optional[torch.LongTensor] = None, entity_token_type_ids: Optional[torch.LongTensor] = None, entity_position_ids: Optional[torch.LongTensor] = None, labels: Optional[torch.LongTensor] = None, entity_labels: Optional[torch.LongTensor] = None, head_mask: Optional[torch.FloatTensor] = None, inputs_embeds: Optional[torch.FloatTensor] = None, output_attentions: Optional[bool] = None, output_hidden_states: Optional[bool] = None, return_dict: Optional[bool] = None) -> Union[Tuple, LukeMaskedLMOutput]:
        """
        labels (`torch.LongTensor` of shape `(batch_size, sequence_length)`, *optional*):
            Labels for computing the masked language modeling loss. Indices should be in `[-100, 0, ...,
            config.vocab_size]` (see `input_ids` docstring) Tokens with indices set to `-100` are ignored (masked), the
            loss is only computed for the tokens with labels in `[0, ..., config.vocab_size]`
        entity_labels (`torch.LongTensor` of shape `(batch_size, entity_length)`, *optional*):
            Labels for computing the masked language modeling loss. Indices should be in `[-100, 0, ...,
            config.vocab_size]` (see `input_ids` docstring) Tokens with indices set to `-100` are ignored (masked), the
            loss is only computed for the tokens with labels in `[0, ..., config.vocab_size]`

        Returns:

        """

class LukeForEntityClassification(LukePreTrainedModel):
    luke: Incomplete
    num_labels: Incomplete
    dropout: Incomplete
    classifier: Incomplete
    def __init__(self, config) -> None: ...
    def forward(self, input_ids: Optional[torch.LongTensor] = None, attention_mask: Optional[torch.FloatTensor] = None, token_type_ids: Optional[torch.LongTensor] = None, position_ids: Optional[torch.LongTensor] = None, entity_ids: Optional[torch.LongTensor] = None, entity_attention_mask: Optional[torch.FloatTensor] = None, entity_token_type_ids: Optional[torch.LongTensor] = None, entity_position_ids: Optional[torch.LongTensor] = None, head_mask: Optional[torch.FloatTensor] = None, inputs_embeds: Optional[torch.FloatTensor] = None, labels: Optional[torch.FloatTensor] = None, output_attentions: Optional[bool] = None, output_hidden_states: Optional[bool] = None, return_dict: Optional[bool] = None) -> Union[Tuple, EntityClassificationOutput]:
        '''
        labels (`torch.LongTensor` of shape `(batch_size,)` or `(batch_size, num_labels)`, *optional*):
            Labels for computing the classification loss. If the shape is `(batch_size,)`, the cross entropy loss is
            used for the single-label classification. In this case, labels should contain the indices that should be in
            `[0, ..., config.num_labels - 1]`. If the shape is `(batch_size, num_labels)`, the binary cross entropy
            loss is used for the multi-label classification. In this case, labels should only contain `[0, 1]`, where 0
            and 1 indicate false and true, respectively.

        Returns:

        Examples:

        ```python
        >>> from transformers import AutoTokenizer, LukeForEntityClassification

        >>> tokenizer = AutoTokenizer.from_pretrained("studio-ousia/luke-large-finetuned-open-entity")
        >>> model = LukeForEntityClassification.from_pretrained("studio-ousia/luke-large-finetuned-open-entity")

        >>> text = "Beyoncé lives in Los Angeles."
        >>> entity_spans = [(0, 7)]  # character-based entity span corresponding to "Beyoncé"
        >>> inputs = tokenizer(text, entity_spans=entity_spans, return_tensors="pt")
        >>> outputs = model(**inputs)
        >>> logits = outputs.logits
        >>> predicted_class_idx = logits.argmax(-1).item()
        >>> print("Predicted class:", model.config.id2label[predicted_class_idx])
        Predicted class: person
        ```'''

class LukeForEntityPairClassification(LukePreTrainedModel):
    luke: Incomplete
    num_labels: Incomplete
    dropout: Incomplete
    classifier: Incomplete
    def __init__(self, config) -> None: ...
    def forward(self, input_ids: Optional[torch.LongTensor] = None, attention_mask: Optional[torch.FloatTensor] = None, token_type_ids: Optional[torch.LongTensor] = None, position_ids: Optional[torch.LongTensor] = None, entity_ids: Optional[torch.LongTensor] = None, entity_attention_mask: Optional[torch.FloatTensor] = None, entity_token_type_ids: Optional[torch.LongTensor] = None, entity_position_ids: Optional[torch.LongTensor] = None, head_mask: Optional[torch.FloatTensor] = None, inputs_embeds: Optional[torch.FloatTensor] = None, labels: Optional[torch.LongTensor] = None, output_attentions: Optional[bool] = None, output_hidden_states: Optional[bool] = None, return_dict: Optional[bool] = None) -> Union[Tuple, EntityPairClassificationOutput]:
        '''
        labels (`torch.LongTensor` of shape `(batch_size,)` or `(batch_size, num_labels)`, *optional*):
            Labels for computing the classification loss. If the shape is `(batch_size,)`, the cross entropy loss is
            used for the single-label classification. In this case, labels should contain the indices that should be in
            `[0, ..., config.num_labels - 1]`. If the shape is `(batch_size, num_labels)`, the binary cross entropy
            loss is used for the multi-label classification. In this case, labels should only contain `[0, 1]`, where 0
            and 1 indicate false and true, respectively.

        Returns:

        Examples:

        ```python
        >>> from transformers import AutoTokenizer, LukeForEntityPairClassification

        >>> tokenizer = AutoTokenizer.from_pretrained("studio-ousia/luke-large-finetuned-tacred")
        >>> model = LukeForEntityPairClassification.from_pretrained("studio-ousia/luke-large-finetuned-tacred")

        >>> text = "Beyoncé lives in Los Angeles."
        >>> entity_spans = [
        ...     (0, 7),
        ...     (17, 28),
        ... ]  # character-based entity spans corresponding to "Beyoncé" and "Los Angeles"
        >>> inputs = tokenizer(text, entity_spans=entity_spans, return_tensors="pt")
        >>> outputs = model(**inputs)
        >>> logits = outputs.logits
        >>> predicted_class_idx = logits.argmax(-1).item()
        >>> print("Predicted class:", model.config.id2label[predicted_class_idx])
        Predicted class: per:cities_of_residence
        ```'''

class LukeForEntitySpanClassification(LukePreTrainedModel):
    luke: Incomplete
    num_labels: Incomplete
    dropout: Incomplete
    classifier: Incomplete
    def __init__(self, config) -> None: ...
    def forward(self, input_ids: Optional[torch.LongTensor] = None, attention_mask: Incomplete | None = None, token_type_ids: Optional[torch.LongTensor] = None, position_ids: Optional[torch.LongTensor] = None, entity_ids: Optional[torch.LongTensor] = None, entity_attention_mask: Optional[torch.LongTensor] = None, entity_token_type_ids: Optional[torch.LongTensor] = None, entity_position_ids: Optional[torch.LongTensor] = None, entity_start_positions: Optional[torch.LongTensor] = None, entity_end_positions: Optional[torch.LongTensor] = None, head_mask: Optional[torch.FloatTensor] = None, inputs_embeds: Optional[torch.FloatTensor] = None, labels: Optional[torch.LongTensor] = None, output_attentions: Optional[bool] = None, output_hidden_states: Optional[bool] = None, return_dict: Optional[bool] = None) -> Union[Tuple, EntitySpanClassificationOutput]:
        '''
        entity_start_positions (`torch.LongTensor`):
            The start positions of entities in the word token sequence.

        entity_end_positions (`torch.LongTensor`):
            The end positions of entities in the word token sequence.

        labels (`torch.LongTensor` of shape `(batch_size, entity_length)` or `(batch_size, entity_length, num_labels)`, *optional*):
            Labels for computing the classification loss. If the shape is `(batch_size, entity_length)`, the cross
            entropy loss is used for the single-label classification. In this case, labels should contain the indices
            that should be in `[0, ..., config.num_labels - 1]`. If the shape is `(batch_size, entity_length,
            num_labels)`, the binary cross entropy loss is used for the multi-label classification. In this case,
            labels should only contain `[0, 1]`, where 0 and 1 indicate false and true, respectively.

        Returns:

        Examples:

        ```python
        >>> from transformers import AutoTokenizer, LukeForEntitySpanClassification

        >>> tokenizer = AutoTokenizer.from_pretrained("studio-ousia/luke-large-finetuned-conll-2003")
        >>> model = LukeForEntitySpanClassification.from_pretrained("studio-ousia/luke-large-finetuned-conll-2003")

        >>> text = "Beyoncé lives in Los Angeles"
        # List all possible entity spans in the text

        >>> word_start_positions = [0, 8, 14, 17, 21]  # character-based start positions of word tokens
        >>> word_end_positions = [7, 13, 16, 20, 28]  # character-based end positions of word tokens
        >>> entity_spans = []
        >>> for i, start_pos in enumerate(word_start_positions):
        ...     for end_pos in word_end_positions[i:]:
        ...         entity_spans.append((start_pos, end_pos))

        >>> inputs = tokenizer(text, entity_spans=entity_spans, return_tensors="pt")
        >>> outputs = model(**inputs)
        >>> logits = outputs.logits
        >>> predicted_class_indices = logits.argmax(-1).squeeze().tolist()
        >>> for span, predicted_class_idx in zip(entity_spans, predicted_class_indices):
        ...     if predicted_class_idx != 0:
        ...         print(text[span[0] : span[1]], model.config.id2label[predicted_class_idx])
        Beyoncé PER
        Los Angeles LOC
        ```'''

class LukeForSequenceClassification(LukePreTrainedModel):
    num_labels: Incomplete
    luke: Incomplete
    dropout: Incomplete
    classifier: Incomplete
    def __init__(self, config) -> None: ...
    def forward(self, input_ids: Optional[torch.LongTensor] = None, attention_mask: Optional[torch.FloatTensor] = None, token_type_ids: Optional[torch.LongTensor] = None, position_ids: Optional[torch.LongTensor] = None, entity_ids: Optional[torch.LongTensor] = None, entity_attention_mask: Optional[torch.FloatTensor] = None, entity_token_type_ids: Optional[torch.LongTensor] = None, entity_position_ids: Optional[torch.LongTensor] = None, head_mask: Optional[torch.FloatTensor] = None, inputs_embeds: Optional[torch.FloatTensor] = None, labels: Optional[torch.FloatTensor] = None, output_attentions: Optional[bool] = None, output_hidden_states: Optional[bool] = None, return_dict: Optional[bool] = None) -> Union[Tuple, LukeSequenceClassifierOutput]:
        """
        labels (`torch.LongTensor` of shape `(batch_size,)`, *optional*):
            Labels for computing the sequence classification/regression loss. Indices should be in `[0, ...,
            config.num_labels - 1]`. If `config.num_labels == 1` a regression loss is computed (Mean-Square loss), If
            `config.num_labels > 1` a classification loss is computed (Cross-Entropy).
        """

class LukeForTokenClassification(LukePreTrainedModel):
    num_labels: Incomplete
    luke: Incomplete
    dropout: Incomplete
    classifier: Incomplete
    def __init__(self, config) -> None: ...
    def forward(self, input_ids: Optional[torch.LongTensor] = None, attention_mask: Optional[torch.FloatTensor] = None, token_type_ids: Optional[torch.LongTensor] = None, position_ids: Optional[torch.LongTensor] = None, entity_ids: Optional[torch.LongTensor] = None, entity_attention_mask: Optional[torch.FloatTensor] = None, entity_token_type_ids: Optional[torch.LongTensor] = None, entity_position_ids: Optional[torch.LongTensor] = None, head_mask: Optional[torch.FloatTensor] = None, inputs_embeds: Optional[torch.FloatTensor] = None, labels: Optional[torch.FloatTensor] = None, output_attentions: Optional[bool] = None, output_hidden_states: Optional[bool] = None, return_dict: Optional[bool] = None) -> Union[Tuple, LukeTokenClassifierOutput]:
        """
        labels (`torch.LongTensor` of shape `(batch_size,)`, *optional*):
            Labels for computing the multiple choice classification loss. Indices should be in `[0, ...,
            num_choices-1]` where `num_choices` is the size of the second dimension of the input tensors. (See
            `input_ids` above)
        """

class LukeForQuestionAnswering(LukePreTrainedModel):
    num_labels: Incomplete
    luke: Incomplete
    qa_outputs: Incomplete
    def __init__(self, config) -> None: ...
    def forward(self, input_ids: Optional[torch.LongTensor] = None, attention_mask: Optional[torch.FloatTensor] = None, token_type_ids: Optional[torch.LongTensor] = None, position_ids: Optional[torch.FloatTensor] = None, entity_ids: Optional[torch.LongTensor] = None, entity_attention_mask: Optional[torch.FloatTensor] = None, entity_token_type_ids: Optional[torch.LongTensor] = None, entity_position_ids: Optional[torch.LongTensor] = None, head_mask: Optional[torch.FloatTensor] = None, inputs_embeds: Optional[torch.FloatTensor] = None, start_positions: Optional[torch.LongTensor] = None, end_positions: Optional[torch.LongTensor] = None, output_attentions: Optional[bool] = None, output_hidden_states: Optional[bool] = None, return_dict: Optional[bool] = None) -> Union[Tuple, LukeQuestionAnsweringModelOutput]:
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

class LukeForMultipleChoice(LukePreTrainedModel):
    luke: Incomplete
    dropout: Incomplete
    classifier: Incomplete
    def __init__(self, config) -> None: ...
    def forward(self, input_ids: Optional[torch.LongTensor] = None, attention_mask: Optional[torch.FloatTensor] = None, token_type_ids: Optional[torch.LongTensor] = None, position_ids: Optional[torch.LongTensor] = None, entity_ids: Optional[torch.LongTensor] = None, entity_attention_mask: Optional[torch.FloatTensor] = None, entity_token_type_ids: Optional[torch.LongTensor] = None, entity_position_ids: Optional[torch.LongTensor] = None, head_mask: Optional[torch.FloatTensor] = None, inputs_embeds: Optional[torch.FloatTensor] = None, labels: Optional[torch.FloatTensor] = None, output_attentions: Optional[bool] = None, output_hidden_states: Optional[bool] = None, return_dict: Optional[bool] = None) -> Union[Tuple, LukeMultipleChoiceModelOutput]:
        """
        labels (`torch.LongTensor` of shape `(batch_size,)`, *optional*):
            Labels for computing the multiple choice classification loss. Indices should be in `[0, ...,
            num_choices-1]` where `num_choices` is the size of the second dimension of the input tensors. (See
            `input_ids` above)
        """
