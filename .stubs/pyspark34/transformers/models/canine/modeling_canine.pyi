import torch
from ...activations import ACT2FN as ACT2FN
from ...modeling_outputs import BaseModelOutput as BaseModelOutput, ModelOutput as ModelOutput, MultipleChoiceModelOutput as MultipleChoiceModelOutput, QuestionAnsweringModelOutput as QuestionAnsweringModelOutput, SequenceClassifierOutput as SequenceClassifierOutput, TokenClassifierOutput as TokenClassifierOutput
from ...modeling_utils import PreTrainedModel as PreTrainedModel
from ...pytorch_utils import apply_chunking_to_forward as apply_chunking_to_forward, find_pruneable_heads_and_indices as find_pruneable_heads_and_indices, prune_linear_layer as prune_linear_layer
from ...utils import add_code_sample_docstrings as add_code_sample_docstrings, add_start_docstrings as add_start_docstrings, add_start_docstrings_to_model_forward as add_start_docstrings_to_model_forward, logging as logging, replace_return_docstrings as replace_return_docstrings
from .configuration_canine import CanineConfig as CanineConfig
from _typeshed import Incomplete
from dataclasses import dataclass
from torch import nn
from typing import Optional, Tuple, Union

logger: Incomplete
CANINE_PRETRAINED_MODEL_ARCHIVE_LIST: Incomplete

@dataclass
class CanineModelOutputWithPooling(ModelOutput):
    """
    Output type of [`CanineModel`]. Based on [`~modeling_outputs.BaseModelOutputWithPooling`], but with slightly
    different `hidden_states` and `attentions`, as these also include the hidden states and attentions of the shallow
    Transformer encoders.

    Args:
        last_hidden_state (`torch.FloatTensor` of shape `(batch_size, sequence_length, hidden_size)`):
            Sequence of hidden-states at the output of the last layer of the model (i.e. the output of the final
            shallow Transformer encoder).
        pooler_output (`torch.FloatTensor` of shape `(batch_size, hidden_size)`):
            Hidden-state of the first token of the sequence (classification token) at the last layer of the deep
            Transformer encoder, further processed by a Linear layer and a Tanh activation function. The Linear layer
            weights are trained from the next sentence prediction (classification) objective during pretraining.
        hidden_states (`tuple(torch.FloatTensor)`, *optional*, returned when `output_hidden_states=True` is passed or when `config.output_hidden_states=True`):
            Tuple of `torch.FloatTensor` (one for the input to each encoder + one for the output of each layer of each
            encoder) of shape `(batch_size, sequence_length, hidden_size)` and `(batch_size, sequence_length //
            config.downsampling_rate, hidden_size)`. Hidden-states of the model at the output of each layer plus the
            initial input to each Transformer encoder. The hidden states of the shallow encoders have length
            `sequence_length`, but the hidden states of the deep encoder have length `sequence_length` //
            `config.downsampling_rate`.
        attentions (`tuple(torch.FloatTensor)`, *optional*, returned when `output_attentions=True` is passed or when `config.output_attentions=True`):
            Tuple of `torch.FloatTensor` (one for each layer) of the 3 Transformer encoders of shape `(batch_size,
            num_heads, sequence_length, sequence_length)` and `(batch_size, num_heads, sequence_length //
            config.downsampling_rate, sequence_length // config.downsampling_rate)`. Attentions weights after the
            attention softmax, used to compute the weighted average in the self-attention heads.
    """
    last_hidden_state: torch.FloatTensor = ...
    pooler_output: torch.FloatTensor = ...
    hidden_states: Optional[Tuple[torch.FloatTensor]] = ...
    attentions: Optional[Tuple[torch.FloatTensor]] = ...
    def __init__(self, last_hidden_state, pooler_output, hidden_states, attentions) -> None: ...

def load_tf_weights_in_canine(model, config, tf_checkpoint_path):
    """Load tf checkpoints in a pytorch model."""

class CanineEmbeddings(nn.Module):
    """Construct the character, position and token_type embeddings."""
    config: Incomplete
    char_position_embeddings: Incomplete
    token_type_embeddings: Incomplete
    LayerNorm: Incomplete
    dropout: Incomplete
    position_embedding_type: Incomplete
    def __init__(self, config) -> None: ...
    def forward(self, input_ids: Optional[torch.LongTensor] = None, token_type_ids: Optional[torch.LongTensor] = None, position_ids: Optional[torch.LongTensor] = None, inputs_embeds: Optional[torch.FloatTensor] = None) -> torch.FloatTensor: ...

class CharactersToMolecules(nn.Module):
    """Convert character sequence to initial molecule sequence (i.e. downsample) using strided convolutions."""
    conv: Incomplete
    activation: Incomplete
    LayerNorm: Incomplete
    def __init__(self, config) -> None: ...
    def forward(self, char_encoding: torch.Tensor) -> torch.Tensor: ...

class ConvProjection(nn.Module):
    """
    Project representations from hidden_size*2 back to hidden_size across a window of w = config.upsampling_kernel_size
    characters.
    """
    config: Incomplete
    conv: Incomplete
    activation: Incomplete
    LayerNorm: Incomplete
    dropout: Incomplete
    def __init__(self, config) -> None: ...
    def forward(self, inputs: torch.Tensor, final_seq_char_positions: Optional[torch.Tensor] = None) -> torch.Tensor: ...

class CanineSelfAttention(nn.Module):
    num_attention_heads: Incomplete
    attention_head_size: Incomplete
    all_head_size: Incomplete
    query: Incomplete
    key: Incomplete
    value: Incomplete
    dropout: Incomplete
    position_embedding_type: Incomplete
    max_position_embeddings: Incomplete
    distance_embedding: Incomplete
    def __init__(self, config) -> None: ...
    def transpose_for_scores(self, x): ...
    def forward(self, from_tensor: torch.Tensor, to_tensor: torch.Tensor, attention_mask: Optional[torch.FloatTensor] = None, head_mask: Optional[torch.FloatTensor] = None, output_attentions: Optional[bool] = False) -> Tuple[torch.Tensor, Optional[torch.Tensor]]: ...

class CanineSelfOutput(nn.Module):
    dense: Incomplete
    LayerNorm: Incomplete
    dropout: Incomplete
    def __init__(self, config) -> None: ...
    def forward(self, hidden_states: Tuple[torch.FloatTensor], input_tensor: torch.FloatTensor) -> Tuple[torch.FloatTensor, torch.FloatTensor]: ...

class CanineAttention(nn.Module):
    """
    Additional arguments related to local attention:

        - **local** (`bool`, *optional*, defaults to `False`) -- Whether to apply local attention.
        - **always_attend_to_first_position** (`bool`, *optional*, defaults to `False`) -- Should all blocks be able to
          attend
        to the `to_tensor`'s first position (e.g. a [CLS] position)? - **first_position_attends_to_all** (`bool`,
        *optional*, defaults to `False`) -- Should the *from_tensor*'s first position be able to attend to all
        positions within the *from_tensor*? - **attend_from_chunk_width** (`int`, *optional*, defaults to 128) -- The
        width of each block-wise chunk in `from_tensor`. - **attend_from_chunk_stride** (`int`, *optional*, defaults to
        128) -- The number of elements to skip when moving to the next block in `from_tensor`. -
        **attend_to_chunk_width** (`int`, *optional*, defaults to 128) -- The width of each block-wise chunk in
        *to_tensor*. - **attend_to_chunk_stride** (`int`, *optional*, defaults to 128) -- The number of elements to
        skip when moving to the next block in `to_tensor`.
    """
    self: Incomplete
    output: Incomplete
    pruned_heads: Incomplete
    local: Incomplete
    always_attend_to_first_position: Incomplete
    first_position_attends_to_all: Incomplete
    attend_from_chunk_width: Incomplete
    attend_from_chunk_stride: Incomplete
    attend_to_chunk_width: Incomplete
    attend_to_chunk_stride: Incomplete
    def __init__(self, config, local: bool = False, always_attend_to_first_position: bool = False, first_position_attends_to_all: bool = False, attend_from_chunk_width: int = 128, attend_from_chunk_stride: int = 128, attend_to_chunk_width: int = 128, attend_to_chunk_stride: int = 128) -> None: ...
    def prune_heads(self, heads) -> None: ...
    def forward(self, hidden_states: Tuple[torch.FloatTensor], attention_mask: Optional[torch.FloatTensor] = None, head_mask: Optional[torch.FloatTensor] = None, output_attentions: Optional[bool] = False) -> Tuple[torch.FloatTensor, Optional[torch.FloatTensor]]: ...

class CanineIntermediate(nn.Module):
    dense: Incomplete
    intermediate_act_fn: Incomplete
    def __init__(self, config) -> None: ...
    def forward(self, hidden_states: torch.FloatTensor) -> torch.FloatTensor: ...

class CanineOutput(nn.Module):
    dense: Incomplete
    LayerNorm: Incomplete
    dropout: Incomplete
    def __init__(self, config) -> None: ...
    def forward(self, hidden_states: Tuple[torch.FloatTensor], input_tensor: torch.FloatTensor) -> torch.FloatTensor: ...

class CanineLayer(nn.Module):
    chunk_size_feed_forward: Incomplete
    seq_len_dim: int
    attention: Incomplete
    intermediate: Incomplete
    output: Incomplete
    def __init__(self, config, local, always_attend_to_first_position, first_position_attends_to_all, attend_from_chunk_width, attend_from_chunk_stride, attend_to_chunk_width, attend_to_chunk_stride) -> None: ...
    def forward(self, hidden_states: Tuple[torch.FloatTensor], attention_mask: Optional[torch.FloatTensor] = None, head_mask: Optional[torch.FloatTensor] = None, output_attentions: Optional[bool] = False) -> Tuple[torch.FloatTensor, Optional[torch.FloatTensor]]: ...
    def feed_forward_chunk(self, attention_output): ...

class CanineEncoder(nn.Module):
    config: Incomplete
    layer: Incomplete
    gradient_checkpointing: bool
    def __init__(self, config, local: bool = False, always_attend_to_first_position: bool = False, first_position_attends_to_all: bool = False, attend_from_chunk_width: int = 128, attend_from_chunk_stride: int = 128, attend_to_chunk_width: int = 128, attend_to_chunk_stride: int = 128) -> None: ...
    def forward(self, hidden_states: Tuple[torch.FloatTensor], attention_mask: Optional[torch.FloatTensor] = None, head_mask: Optional[torch.FloatTensor] = None, output_attentions: Optional[bool] = False, output_hidden_states: Optional[bool] = False, return_dict: Optional[bool] = True) -> Union[Tuple, BaseModelOutput]: ...

class CaninePooler(nn.Module):
    dense: Incomplete
    activation: Incomplete
    def __init__(self, config) -> None: ...
    def forward(self, hidden_states: Tuple[torch.FloatTensor]) -> torch.FloatTensor: ...

class CaninePredictionHeadTransform(nn.Module):
    dense: Incomplete
    transform_act_fn: Incomplete
    LayerNorm: Incomplete
    def __init__(self, config) -> None: ...
    def forward(self, hidden_states: Tuple[torch.FloatTensor]) -> torch.FloatTensor: ...

class CanineLMPredictionHead(nn.Module):
    transform: Incomplete
    decoder: Incomplete
    bias: Incomplete
    def __init__(self, config) -> None: ...
    def forward(self, hidden_states: Tuple[torch.FloatTensor]) -> torch.FloatTensor: ...

class CanineOnlyMLMHead(nn.Module):
    predictions: Incomplete
    def __init__(self, config) -> None: ...
    def forward(self, sequence_output: Tuple[torch.Tensor]) -> Tuple[torch.Tensor]: ...

class CaninePreTrainedModel(PreTrainedModel):
    """
    An abstract class to handle weights initialization and a simple interface for downloading and loading pretrained
    models.
    """
    config_class = CanineConfig
    load_tf_weights = load_tf_weights_in_canine
    base_model_prefix: str
    supports_gradient_checkpointing: bool

CANINE_START_DOCSTRING: str
CANINE_INPUTS_DOCSTRING: str

class CanineModel(CaninePreTrainedModel):
    config: Incomplete
    char_embeddings: Incomplete
    initial_char_encoder: Incomplete
    chars_to_molecules: Incomplete
    encoder: Incomplete
    projection: Incomplete
    final_char_encoder: Incomplete
    pooler: Incomplete
    def __init__(self, config, add_pooling_layer: bool = True) -> None: ...
    def forward(self, input_ids: Optional[torch.LongTensor] = None, attention_mask: Optional[torch.FloatTensor] = None, token_type_ids: Optional[torch.LongTensor] = None, position_ids: Optional[torch.LongTensor] = None, head_mask: Optional[torch.FloatTensor] = None, inputs_embeds: Optional[torch.FloatTensor] = None, output_attentions: Optional[bool] = None, output_hidden_states: Optional[bool] = None, return_dict: Optional[bool] = None) -> Union[Tuple, CanineModelOutputWithPooling]: ...

class CanineForSequenceClassification(CaninePreTrainedModel):
    num_labels: Incomplete
    canine: Incomplete
    dropout: Incomplete
    classifier: Incomplete
    def __init__(self, config) -> None: ...
    def forward(self, input_ids: Optional[torch.LongTensor] = None, attention_mask: Optional[torch.FloatTensor] = None, token_type_ids: Optional[torch.LongTensor] = None, position_ids: Optional[torch.LongTensor] = None, head_mask: Optional[torch.FloatTensor] = None, inputs_embeds: Optional[torch.FloatTensor] = None, labels: Optional[torch.LongTensor] = None, output_attentions: Optional[bool] = None, output_hidden_states: Optional[bool] = None, return_dict: Optional[bool] = None) -> Union[Tuple, SequenceClassifierOutput]:
        """
        labels (`torch.LongTensor` of shape `(batch_size,)`, *optional*):
            Labels for computing the sequence classification/regression loss. Indices should be in `[0, ...,
            config.num_labels - 1]`. If `config.num_labels == 1` a regression loss is computed (Mean-Square loss), If
            `config.num_labels > 1` a classification loss is computed (Cross-Entropy).
        """

class CanineForMultipleChoice(CaninePreTrainedModel):
    canine: Incomplete
    dropout: Incomplete
    classifier: Incomplete
    def __init__(self, config) -> None: ...
    def forward(self, input_ids: Optional[torch.LongTensor] = None, attention_mask: Optional[torch.FloatTensor] = None, token_type_ids: Optional[torch.LongTensor] = None, position_ids: Optional[torch.LongTensor] = None, head_mask: Optional[torch.FloatTensor] = None, inputs_embeds: Optional[torch.FloatTensor] = None, labels: Optional[torch.LongTensor] = None, output_attentions: Optional[bool] = None, output_hidden_states: Optional[bool] = None, return_dict: Optional[bool] = None) -> Union[Tuple, MultipleChoiceModelOutput]:
        """
        labels (`torch.LongTensor` of shape `(batch_size,)`, *optional*):
            Labels for computing the multiple choice classification loss. Indices should be in `[0, ...,
            num_choices-1]` where `num_choices` is the size of the second dimension of the input tensors. (See
            `input_ids` above)
        """

class CanineForTokenClassification(CaninePreTrainedModel):
    num_labels: Incomplete
    canine: Incomplete
    dropout: Incomplete
    classifier: Incomplete
    def __init__(self, config) -> None: ...
    def forward(self, input_ids: Optional[torch.LongTensor] = None, attention_mask: Optional[torch.FloatTensor] = None, token_type_ids: Optional[torch.LongTensor] = None, position_ids: Optional[torch.LongTensor] = None, head_mask: Optional[torch.FloatTensor] = None, inputs_embeds: Optional[torch.FloatTensor] = None, labels: Optional[torch.LongTensor] = None, output_attentions: Optional[bool] = None, output_hidden_states: Optional[bool] = None, return_dict: Optional[bool] = None) -> Union[Tuple, TokenClassifierOutput]:
        '''
        labels (`torch.LongTensor` of shape `(batch_size, sequence_length)`, *optional*):
            Labels for computing the token classification loss. Indices should be in `[0, ..., config.num_labels - 1]`.

        Returns:

        Example:

        ```python
        >>> from transformers import AutoTokenizer, CanineForTokenClassification
        >>> import torch

        >>> tokenizer = AutoTokenizer.from_pretrained("google/canine-s")
        >>> model = CanineForTokenClassification.from_pretrained("google/canine-s")

        >>> inputs = tokenizer(
        ...     "HuggingFace is a company based in Paris and New York", add_special_tokens=False, return_tensors="pt"
        ... )

        >>> with torch.no_grad():
        ...     logits = model(**inputs).logits

        >>> predicted_token_class_ids = logits.argmax(-1)

        >>> # Note that tokens are classified rather then input words which means that
        >>> # there might be more predicted token classes than words.
        >>> # Multiple token classes might account for the same word
        >>> predicted_tokens_classes = [model.config.id2label[t.item()] for t in predicted_token_class_ids[0]]
        >>> predicted_tokens_classes  # doctest: +SKIP
        ```

        ```python
        >>> labels = predicted_token_class_ids
        >>> loss = model(**inputs, labels=labels).loss
        >>> round(loss.item(), 2)  # doctest: +SKIP
        ```'''

class CanineForQuestionAnswering(CaninePreTrainedModel):
    num_labels: Incomplete
    canine: Incomplete
    qa_outputs: Incomplete
    def __init__(self, config) -> None: ...
    def forward(self, input_ids: Optional[torch.LongTensor] = None, attention_mask: Optional[torch.FloatTensor] = None, token_type_ids: Optional[torch.LongTensor] = None, position_ids: Optional[torch.LongTensor] = None, head_mask: Optional[torch.FloatTensor] = None, inputs_embeds: Optional[torch.FloatTensor] = None, start_positions: Optional[torch.LongTensor] = None, end_positions: Optional[torch.LongTensor] = None, output_attentions: Optional[bool] = None, output_hidden_states: Optional[bool] = None, return_dict: Optional[bool] = None) -> Union[Tuple, QuestionAnsweringModelOutput]:
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
