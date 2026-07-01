import enum
import torch
from ...activations import ACT2FN as ACT2FN
from ...modeling_outputs import BaseModelOutput as BaseModelOutput, BaseModelOutputWithPooling as BaseModelOutputWithPooling, MaskedLMOutput as MaskedLMOutput, SequenceClassifierOutput as SequenceClassifierOutput
from ...modeling_utils import PreTrainedModel as PreTrainedModel
from ...pytorch_utils import apply_chunking_to_forward as apply_chunking_to_forward, find_pruneable_heads_and_indices as find_pruneable_heads_and_indices, prune_linear_layer as prune_linear_layer
from ...utils import ModelOutput as ModelOutput, add_start_docstrings as add_start_docstrings, add_start_docstrings_to_model_forward as add_start_docstrings_to_model_forward, logging as logging, replace_return_docstrings as replace_return_docstrings
from .configuration_tapas import TapasConfig as TapasConfig
from _typeshed import Incomplete
from dataclasses import dataclass
from torch import nn
from typing import Optional, Tuple, Union

logger: Incomplete
TAPAS_PRETRAINED_MODEL_ARCHIVE_LIST: Incomplete
EPSILON_ZERO_DIVISION: float
CLOSE_ENOUGH_TO_LOG_ZERO: float

@dataclass
class TableQuestionAnsweringOutput(ModelOutput):
    """
    Output type of [`TapasForQuestionAnswering`].

    Args:
        loss (`torch.FloatTensor` of shape `(1,)`, *optional*, returned when `labels` (and possibly `answer`, `aggregation_labels`, `numeric_values` and `numeric_values_scale` are provided)):
            Total loss as the sum of the hierarchical cell selection log-likelihood loss and (optionally) the
            semi-supervised regression loss and (optionally) supervised loss for aggregations.
        logits (`torch.FloatTensor` of shape `(batch_size, sequence_length)`):
            Prediction scores of the cell selection head, for every token.
        logits_aggregation (`torch.FloatTensor`, *optional*, of shape `(batch_size, num_aggregation_labels)`):
            Prediction scores of the aggregation head, for every aggregation operator.
        hidden_states (`tuple(torch.FloatTensor)`, *optional*, returned when `output_hidden_states=True` is passed or when `config.output_hidden_states=True`):
            Tuple of `torch.FloatTensor` (one for the output of the embeddings + one for the output of each layer) of
            shape `(batch_size, sequence_length, hidden_size)`. Hidden-states of the model at the output of each layer
            plus the initial embedding outputs.
        attentions (`tuple(torch.FloatTensor)`, *optional*, returned when `output_attentions=True` is passed or when `config.output_attentions=True`):
            Tuple of `torch.FloatTensor` (one for each layer) of shape `(batch_size, num_heads, sequence_length,
            sequence_length)`. Attentions weights after the attention softmax, used to compute the weighted average in
            the self-attention heads.
    """
    loss: Optional[torch.FloatTensor] = ...
    logits: torch.FloatTensor = ...
    logits_aggregation: torch.FloatTensor = ...
    hidden_states: Optional[Tuple[torch.FloatTensor]] = ...
    attentions: Optional[Tuple[torch.FloatTensor]] = ...
    def __init__(self, loss, logits, logits_aggregation, hidden_states, attentions) -> None: ...

def load_tf_weights_in_tapas(model, config, tf_checkpoint_path):
    """
    Load tf checkpoints in a PyTorch model. This is an adaptation from load_tf_weights_in_bert

    - add cell selection and aggregation heads
    - take into account additional token type embedding layers
    """

class TapasEmbeddings(nn.Module):
    """
    Construct the embeddings from word, position and token_type embeddings. Same as BertEmbeddings but with a number of
    additional token type embeddings to encode tabular structure.
    """
    word_embeddings: Incomplete
    position_embeddings: Incomplete
    number_of_token_type_embeddings: Incomplete
    LayerNorm: Incomplete
    dropout: Incomplete
    config: Incomplete
    def __init__(self, config) -> None: ...
    def forward(self, input_ids: Incomplete | None = None, token_type_ids: Incomplete | None = None, position_ids: Incomplete | None = None, inputs_embeds: Incomplete | None = None): ...

class TapasSelfAttention(nn.Module):
    num_attention_heads: Incomplete
    attention_head_size: Incomplete
    all_head_size: Incomplete
    query: Incomplete
    key: Incomplete
    value: Incomplete
    dropout: Incomplete
    is_decoder: Incomplete
    def __init__(self, config) -> None: ...
    def transpose_for_scores(self, x): ...
    def forward(self, hidden_states, attention_mask: Incomplete | None = None, head_mask: Incomplete | None = None, encoder_hidden_states: Incomplete | None = None, encoder_attention_mask: Incomplete | None = None, past_key_value: Incomplete | None = None, output_attentions: bool = False): ...

class TapasSelfOutput(nn.Module):
    dense: Incomplete
    LayerNorm: Incomplete
    dropout: Incomplete
    def __init__(self, config) -> None: ...
    def forward(self, hidden_states: torch.Tensor, input_tensor: torch.Tensor) -> torch.Tensor: ...

class TapasAttention(nn.Module):
    self: Incomplete
    output: Incomplete
    pruned_heads: Incomplete
    def __init__(self, config) -> None: ...
    def prune_heads(self, heads) -> None: ...
    def forward(self, hidden_states: torch.Tensor, attention_mask: Optional[torch.FloatTensor] = None, head_mask: Optional[torch.FloatTensor] = None, encoder_hidden_states: Optional[torch.FloatTensor] = None, encoder_attention_mask: Optional[torch.FloatTensor] = None, past_key_value: Optional[Tuple[Tuple[torch.FloatTensor]]] = None, output_attentions: Optional[bool] = False) -> Tuple[torch.Tensor]: ...

class TapasIntermediate(nn.Module):
    dense: Incomplete
    intermediate_act_fn: Incomplete
    def __init__(self, config) -> None: ...
    def forward(self, hidden_states: torch.Tensor) -> torch.Tensor: ...

class TapasOutput(nn.Module):
    dense: Incomplete
    LayerNorm: Incomplete
    dropout: Incomplete
    def __init__(self, config) -> None: ...
    def forward(self, hidden_states: torch.Tensor, input_tensor: torch.Tensor) -> torch.Tensor: ...

class TapasLayer(nn.Module):
    chunk_size_feed_forward: Incomplete
    seq_len_dim: int
    attention: Incomplete
    is_decoder: Incomplete
    add_cross_attention: Incomplete
    crossattention: Incomplete
    intermediate: Incomplete
    output: Incomplete
    def __init__(self, config) -> None: ...
    def forward(self, hidden_states: torch.Tensor, attention_mask: Optional[torch.FloatTensor] = None, head_mask: Optional[torch.FloatTensor] = None, encoder_hidden_states: Optional[torch.FloatTensor] = None, encoder_attention_mask: Optional[torch.FloatTensor] = None, past_key_value: Optional[Tuple[Tuple[torch.FloatTensor]]] = None, output_attentions: Optional[bool] = False) -> Tuple[torch.Tensor]: ...
    def feed_forward_chunk(self, attention_output): ...

class TapasEncoder(nn.Module):
    config: Incomplete
    layer: Incomplete
    gradient_checkpointing: bool
    def __init__(self, config) -> None: ...
    def forward(self, hidden_states, attention_mask: Incomplete | None = None, head_mask: Incomplete | None = None, encoder_hidden_states: Incomplete | None = None, encoder_attention_mask: Incomplete | None = None, past_key_values: Incomplete | None = None, use_cache: Incomplete | None = None, output_attentions: bool = False, output_hidden_states: bool = False, return_dict: bool = True): ...

class TapasPooler(nn.Module):
    dense: Incomplete
    activation: Incomplete
    def __init__(self, config) -> None: ...
    def forward(self, hidden_states: torch.Tensor) -> torch.Tensor: ...

class TapasPredictionHeadTransform(nn.Module):
    dense: Incomplete
    transform_act_fn: Incomplete
    LayerNorm: Incomplete
    def __init__(self, config) -> None: ...
    def forward(self, hidden_states: torch.Tensor) -> torch.Tensor: ...

class TapasLMPredictionHead(nn.Module):
    transform: Incomplete
    decoder: Incomplete
    bias: Incomplete
    def __init__(self, config) -> None: ...
    def forward(self, hidden_states): ...

class TapasOnlyMLMHead(nn.Module):
    predictions: Incomplete
    def __init__(self, config) -> None: ...
    def forward(self, sequence_output: torch.Tensor) -> torch.Tensor: ...

class TapasPreTrainedModel(PreTrainedModel):
    """
    An abstract class to handle weights initialization and a simple interface for downloading and loading pretrained
    models.
    """
    config_class = TapasConfig
    base_model_prefix: str
    supports_gradient_checkpointing: bool

TAPAS_START_DOCSTRING: str
TAPAS_INPUTS_DOCSTRING: str

class TapasModel(TapasPreTrainedModel):
    """
    This class is a small change compared to [`BertModel`], taking into account the additional token type ids.

    The model can behave as an encoder (with only self-attention) as well as a decoder, in which case a layer of
    cross-attention is added between the self-attention layers, following the architecture described in [Attention is
    all you need](https://arxiv.org/abs/1706.03762) by Ashish Vaswani, Noam Shazeer, Niki Parmar, Jakob Uszkoreit,
    Llion Jones, Aidan N. Gomez, Lukasz Kaiser and Illia Polosukhin.

    """
    config: Incomplete
    embeddings: Incomplete
    encoder: Incomplete
    pooler: Incomplete
    def __init__(self, config, add_pooling_layer: bool = True) -> None: ...
    def get_input_embeddings(self): ...
    def set_input_embeddings(self, value) -> None: ...
    def forward(self, input_ids: Optional[torch.LongTensor] = None, attention_mask: Optional[torch.FloatTensor] = None, token_type_ids: Optional[torch.LongTensor] = None, position_ids: Optional[torch.LongTensor] = None, head_mask: Optional[torch.FloatTensor] = None, inputs_embeds: Optional[torch.FloatTensor] = None, encoder_hidden_states: Optional[torch.FloatTensor] = None, encoder_attention_mask: Optional[torch.FloatTensor] = None, output_attentions: Optional[bool] = None, output_hidden_states: Optional[bool] = None, return_dict: Optional[bool] = None) -> Union[Tuple, BaseModelOutputWithPooling]:
        '''
        Returns:

        Examples:

        ```python
        >>> from transformers import AutoTokenizer, TapasModel
        >>> import pandas as pd

        >>> tokenizer = AutoTokenizer.from_pretrained("google/tapas-base")
        >>> model = TapasModel.from_pretrained("google/tapas-base")

        >>> data = {
        ...     "Actors": ["Brad Pitt", "Leonardo Di Caprio", "George Clooney"],
        ...     "Age": ["56", "45", "59"],
        ...     "Number of movies": ["87", "53", "69"],
        ... }
        >>> table = pd.DataFrame.from_dict(data)
        >>> queries = ["How many movies has George Clooney played in?", "How old is Brad Pitt?"]

        >>> inputs = tokenizer(table=table, queries=queries, padding="max_length", return_tensors="pt")
        >>> outputs = model(**inputs)

        >>> last_hidden_states = outputs.last_hidden_state
        ```'''

class TapasForMaskedLM(TapasPreTrainedModel):
    config_class = TapasConfig
    base_model_prefix: str
    tapas: Incomplete
    cls: Incomplete
    def __init__(self, config) -> None: ...
    def get_output_embeddings(self): ...
    def set_output_embeddings(self, new_embeddings) -> None: ...
    def forward(self, input_ids: Optional[torch.LongTensor] = None, attention_mask: Optional[torch.FloatTensor] = None, token_type_ids: Optional[torch.LongTensor] = None, position_ids: Optional[torch.LongTensor] = None, head_mask: Optional[torch.FloatTensor] = None, inputs_embeds: Optional[torch.FloatTensor] = None, encoder_hidden_states: Optional[torch.FloatTensor] = None, encoder_attention_mask: Optional[torch.FloatTensor] = None, labels: Optional[torch.LongTensor] = None, output_attentions: Optional[bool] = None, output_hidden_states: Optional[bool] = None, return_dict: Optional[bool] = None, **kwargs) -> Union[Tuple, MaskedLMOutput]:
        '''
        labels (`torch.LongTensor` of shape `(batch_size, sequence_length)`, *optional*):
            Labels for computing the masked language modeling loss. Indices should be in `[-100, 0, ...,
            config.vocab_size]` (see `input_ids` docstring) Tokens with indices set to `-100` are ignored (masked), the
            loss is only computed for the tokens with labels in `[0, ..., config.vocab_size]`

        Returns:

        Examples:

        ```python
        >>> from transformers import AutoTokenizer, TapasForMaskedLM
        >>> import pandas as pd

        >>> tokenizer = AutoTokenizer.from_pretrained("google/tapas-base")
        >>> model = TapasForMaskedLM.from_pretrained("google/tapas-base")

        >>> data = {
        ...     "Actors": ["Brad Pitt", "Leonardo Di Caprio", "George Clooney"],
        ...     "Age": ["56", "45", "59"],
        ...     "Number of movies": ["87", "53", "69"],
        ... }
        >>> table = pd.DataFrame.from_dict(data)

        >>> inputs = tokenizer(
        ...     table=table, queries="How many [MASK] has George [MASK] played in?", return_tensors="pt"
        ... )
        >>> labels = tokenizer(
        ...     table=table, queries="How many movies has George Clooney played in?", return_tensors="pt"
        ... )["input_ids"]

        >>> outputs = model(**inputs, labels=labels)
        >>> logits = outputs.logits
        ```'''

class TapasForQuestionAnswering(TapasPreTrainedModel):
    tapas: Incomplete
    dropout: Incomplete
    output_weights: Incomplete
    column_output_weights: Incomplete
    output_bias: Incomplete
    column_output_bias: Incomplete
    aggregation_classifier: Incomplete
    def __init__(self, config: TapasConfig) -> None: ...
    def forward(self, input_ids: Optional[torch.LongTensor] = None, attention_mask: Optional[torch.FloatTensor] = None, token_type_ids: Optional[torch.LongTensor] = None, position_ids: Optional[torch.LongTensor] = None, head_mask: Optional[torch.FloatTensor] = None, inputs_embeds: Optional[torch.FloatTensor] = None, table_mask: Optional[torch.LongTensor] = None, labels: Optional[torch.LongTensor] = None, aggregation_labels: Optional[torch.LongTensor] = None, float_answer: Optional[torch.FloatTensor] = None, numeric_values: Optional[torch.FloatTensor] = None, numeric_values_scale: Optional[torch.FloatTensor] = None, output_attentions: Optional[bool] = None, output_hidden_states: Optional[bool] = None, return_dict: Optional[bool] = None) -> Union[Tuple, TableQuestionAnsweringOutput]:
        '''
        table_mask (`torch.LongTensor` of shape `(batch_size, seq_length)`, *optional*):
            Mask for the table. Indicates which tokens belong to the table (1). Question tokens, table headers and
            padding are 0.
        labels (`torch.LongTensor` of shape `(batch_size, seq_length)`, *optional*):
            Labels per token for computing the hierarchical cell selection loss. This encodes the positions of the
            answer appearing in the table. Can be obtained using [`AutoTokenizer`].

            - 1 for tokens that are **part of the answer**,
            - 0 for tokens that are **not part of the answer**.

        aggregation_labels (`torch.LongTensor` of shape `(batch_size, )`, *optional*):
            Aggregation function index for every example in the batch for computing the aggregation loss. Indices
            should be in `[0, ..., config.num_aggregation_labels - 1]`. Only required in case of strong supervision for
            aggregation (WikiSQL-supervised).
        float_answer (`torch.FloatTensor` of shape `(batch_size, )`, *optional*):
            Float answer for every example in the batch. Set to *float(\'nan\')* for cell selection questions. Only
            required in case of weak supervision (WTQ) to calculate the aggregate mask and regression loss.
        numeric_values (`torch.FloatTensor` of shape `(batch_size, seq_length)`, *optional*):
            Numeric values of every token, NaN for tokens which are not numeric values. Can be obtained using
            [`AutoTokenizer`]. Only required in case of weak supervision for aggregation (WTQ) to calculate the
            regression loss.
        numeric_values_scale (`torch.FloatTensor` of shape `(batch_size, seq_length)`, *optional*):
            Scale of the numeric values of every token. Can be obtained using [`AutoTokenizer`]. Only required in case
            of weak supervision for aggregation (WTQ) to calculate the regression loss.

        Returns:

        Examples:

        ```python
        >>> from transformers import AutoTokenizer, TapasForQuestionAnswering
        >>> import pandas as pd

        >>> tokenizer = AutoTokenizer.from_pretrained("google/tapas-base-finetuned-wtq")
        >>> model = TapasForQuestionAnswering.from_pretrained("google/tapas-base-finetuned-wtq")

        >>> data = {
        ...     "Actors": ["Brad Pitt", "Leonardo Di Caprio", "George Clooney"],
        ...     "Age": ["56", "45", "59"],
        ...     "Number of movies": ["87", "53", "69"],
        ... }
        >>> table = pd.DataFrame.from_dict(data)
        >>> queries = ["How many movies has George Clooney played in?", "How old is Brad Pitt?"]

        >>> inputs = tokenizer(table=table, queries=queries, padding="max_length", return_tensors="pt")
        >>> outputs = model(**inputs)

        >>> logits = outputs.logits
        >>> logits_aggregation = outputs.logits_aggregation
        ```'''

class TapasForSequenceClassification(TapasPreTrainedModel):
    num_labels: Incomplete
    tapas: Incomplete
    dropout: Incomplete
    classifier: Incomplete
    def __init__(self, config) -> None: ...
    def forward(self, input_ids: Optional[torch.LongTensor] = None, attention_mask: Optional[torch.FloatTensor] = None, token_type_ids: Optional[torch.LongTensor] = None, position_ids: Optional[torch.LongTensor] = None, head_mask: Optional[torch.FloatTensor] = None, inputs_embeds: Optional[torch.FloatTensor] = None, labels: Optional[torch.LongTensor] = None, output_attentions: Optional[bool] = None, output_hidden_states: Optional[bool] = None, return_dict: Optional[bool] = None) -> Union[Tuple[torch.Tensor], SequenceClassifierOutput]:
        '''
        labels (`torch.LongTensor` of shape `(batch_size,)`, *optional*):
            Labels for computing the sequence classification/regression loss. Indices should be in `[0, ...,
            config.num_labels - 1]`. If `config.num_labels == 1` a regression loss is computed (Mean-Square loss), If
            `config.num_labels > 1` a classification loss is computed (Cross-Entropy). Note: this is called
            "classification_class_index" in the original implementation.

        Returns:

        Examples:

        ```python
        >>> from transformers import AutoTokenizer, TapasForSequenceClassification
        >>> import torch
        >>> import pandas as pd

        >>> tokenizer = AutoTokenizer.from_pretrained("google/tapas-base-finetuned-tabfact")
        >>> model = TapasForSequenceClassification.from_pretrained("google/tapas-base-finetuned-tabfact")

        >>> data = {
        ...     "Actors": ["Brad Pitt", "Leonardo Di Caprio", "George Clooney"],
        ...     "Age": ["56", "45", "59"],
        ...     "Number of movies": ["87", "53", "69"],
        ... }
        >>> table = pd.DataFrame.from_dict(data)
        >>> queries = [
        ...     "There is only one actor who is 45 years old",
        ...     "There are 3 actors which played in more than 60 movies",
        ... ]

        >>> inputs = tokenizer(table=table, queries=queries, padding="max_length", return_tensors="pt")
        >>> labels = torch.tensor([1, 0])  # 1 means entailed, 0 means refuted

        >>> outputs = model(**inputs, labels=labels)
        >>> loss = outputs.loss
        >>> logits = outputs.logits
        ```'''

class AverageApproximationFunction(str, enum.Enum):
    RATIO: str
    FIRST_ORDER: str
    SECOND_ORDER: str

class IndexMap:
    """Index grouping entries within a tensor."""
    indices: Incomplete
    num_segments: Incomplete
    batch_dims: Incomplete
    def __init__(self, indices, num_segments, batch_dims: int = 0) -> None:
        """
        Creates an index

        Args:
            indices (`torch.LongTensor`, same shape as a *values* Tensor to which the indices refer):
                Tensor containing the indices.
            num_segments (`torch.LongTensor`):
                Scalar tensor, the number of segments. All elements in a batched segmented tensor must have the same
                number of segments (although many segments can be empty).
            batch_dims (`int`, *optional*, defaults to 0):
                The number of batch dimensions. The first *batch_dims* dimensions of a SegmentedTensor are treated as
                batch dimensions. Segments in different batch elements are always distinct even if they have the same
                index.
        """
    def batch_shape(self): ...

class ProductIndexMap(IndexMap):
    """The product of two indices."""
    outer_index: Incomplete
    inner_index: Incomplete
    def __init__(self, outer_index, inner_index) -> None:
        """
        Combines indices i and j into pairs (i, j). The result is an index where each segment (i, j) is the
        intersection of segments i and j. For example if the inputs represent table cells indexed by respectively rows
        and columns the output will be a table indexed by (row, column) pairs, i.e. by cell. The implementation
        combines indices {0, .., n - 1} and {0, .., m - 1} into {0, .., nm - 1}. The output has *num_segments* equal to
        *outer_index.num_segments* * *inner_index.num_segments*

        Args:
            outer_index (`IndexMap`):
                IndexMap.
            inner_index (`IndexMap`):
                IndexMap, must have the same shape as *outer_index*.
        """
    def project_outer(self, index):
        """Projects an index with the same index set onto the outer components."""
    def project_inner(self, index):
        """Projects an index with the same index set onto the inner components."""

def gather(values, index, name: str = 'segmented_gather'):
    """
    Gathers from *values* using the index map. For each element in the domain of the index map this operation looks up
    a value for that index in *values*. Two elements from the same segment always get assigned the same value.

    Args:
        values (`torch.Tensor` of shape (B1, ..., Bn, num_segments, V1, ...)):
            Tensor with segment values.
        index (`IndexMap` of shape (B1, ..., Bn, I1, ..., Ik)):
            IndexMap.
        name (`str`, *optional*, defaults to 'segmented_gather'):
            Name for the operation. Currently not used

    Returns:
        `tuple(torch.Tensor)`: Tensor of shape (B1, ..., Bn, I1, ..., Ik, V1, ...) with the gathered values.
    """
def flatten(index, name: str = 'segmented_flatten'):
    """
    Flattens a batched index map (which is typically of shape batch_size, seq_length) to a 1d index map. This operation
    relabels the segments to keep batch elements distinct. The k-th batch element will have indices shifted by
    *num_segments* * (k - 1). The result is a tensor with *num_segments* multiplied by the number of elements in the
    batch.

    Args:
        index (`IndexMap`):
            IndexMap to flatten.
        name (`str`, *optional*, defaults to 'segmented_flatten'):
            Name for the operation. Currently not used

    Returns:
        (`IndexMap`): The flattened IndexMap.
    """
def range_index_map(batch_shape, num_segments, name: str = 'range_index_map'):
    """
    Constructs an index map equal to range(num_segments).

    Args:
        batch_shape (`torch.Size`):
            Batch shape
        num_segments (`int`):
            Number of segments
        name (`str`, *optional*, defaults to 'range_index_map'):
            Name for the operation. Currently not used

    Returns:
        (`IndexMap`): IndexMap of shape batch_shape with elements equal to range(num_segments).
    """
def reduce_sum(values, index, name: str = 'segmented_reduce_sum'):
    """
    Sums a tensor over its segments.

    Outputs 0 for empty segments.

    This operations computes the sum over segments, with support for:

        - Batching using the first dimensions [B1, B2, ..., Bn]. Each element in a batch can have different indices.
        - Vectorization using the last dimension [V1, V2, ...]. If they are present, the output will be a sum of
          vectors rather than scalars. Only the middle dimensions [I1, ..., Ik] are reduced by the operation.

    Args:
        values (`torch.Tensor` of shape [B1, B2, ..., Bn, I1, .., Ik, V1, V2, ..]):
            Tensor containing the values of which the sum must be taken segment-wise.
        index (`IndexMap`, indices are of shape [B1, B2, ..., Bn, I1, .., Ik].):
            Index defining the segments.
        name (`str`, *optional*, defaults to 'segmented_reduce_sum'):
            Name for the operation. Currently not used

    Returns:
        output_values (`torch.Tensor`of shape [B1, B2, ..., Bn, num_segments, V1, V2, ..]): Tensor containing the
        output values. output_index (`IndexMap`): IndexMap with shape [B1, B2, ..., Bn, num_segments]. .
    """
def reduce_mean(values, index, name: str = 'segmented_reduce_mean'):
    """
    Averages a tensor over its segments.

    Outputs 0 for empty segments.

    This operations computes the mean over segments, with support for:

        - Batching using the first dimensions [B1, B2, ..., Bn]. Each element in a batch can have different indices.
        - Vectorization using the last dimension [V1, V2, ...]. If they are present, the output will be a mean of
          vectors rather than scalars.

    Only the middle dimensions [I1, ..., Ik] are reduced by the operation.

    Args:
        values (`torch.Tensor` of shape [B1, B2, ..., Bn, I1, .., Ik, V1, V2, ..]):
            Tensor containing the values of which the mean must be taken segment-wise.
        index (`IndexMap`, indices are of shape [B1, B2, ..., Bn, I1, .., Ik].):
            Index defining the segments.
        name (`str`, *optional*, defaults to 'segmented_reduce_sum'):
            Name for the operation. Currently not used

    Returns:
        output_values (`torch.Tensor`of shape [B1, B2, ..., Bn, num_segments, V1, V2, ..]): Tensor containing the
        output values. output_index (`IndexMap`): IndexMap with shape [B1, B2, ..., Bn, num_segments].
    """
def reduce_max(values, index, name: str = 'segmented_reduce_max'):
    """
    Computes the maximum over segments.

    This operation computes the maximum over segments, with support for:

        - Batching using the first dimensions [B1, B2, ..., Bn]. Each element in a batch can have different indices.
        - Vectorization using the last dimension [V1, V2, ...]. If they are present, the output will be an element-wise
          maximum of vectors rather than scalars.

    Only the middle dimensions [I1, ..., Ik] are reduced by the operation.

    Args:
        values (`torch.Tensor` of shape [B1, B2, ..., Bn, I1, .., Ik, V1, V2, ..]):
            Tensor containing the values of which the max must be taken segment-wise.
        index (`IndexMap`, indices are of shape [B1, B2, ..., Bn, I1, .., Ik].):
            Index defining the segments.
        name (`str`, *optional*, defaults to 'segmented_reduce_sum'):
            Name for the operation. Currently not used

    Returns:
        output_values (`torch.Tensor`of shape [B1, B2, ..., Bn, num_segments, V1, V2, ..]): Tensor containing the
        output values. output_index (`IndexMap`): IndexMap with shape [B1, B2, ..., Bn, num_segments].
    """
def reduce_min(values, index, name: str = 'segmented_reduce_min'):
    """
    Computes the minimum over segments.

    This operations computes the minimum over segments, with support for:

        - Batching using the first dimensions [B1, B2, ..., Bn]. Each element in a batch can have different indices.
        - Vectorization using the last dimension [V1, V2, ...]. If they are present, the output will be an element-wise
          minimum of vectors rather than scalars.

    Only the middle dimensions [I1, ..., Ik] are reduced by the operation.

    Args:
        values (`torch.Tensor` of shape [B1, B2, ..., Bn, I1, .., Ik, V1, V2, ..]):
            Tensor containing the values of which the min must be taken segment-wise.
        index (`IndexMap`, indices are of shape [B1, B2, ..., Bn, I1, .., Ik].):
            Index defining the segments.
        name (`str`, *optional*, defaults to 'segmented_reduce_sum'):
            Name for the operation. Currently not used

    Returns:
        output_values (`torch.Tensor`of shape [B1, B2, ..., Bn, num_segments, V1, V2, ..]): Tensor containing the
        output values. output_index (`IndexMap`): IndexMap with shape [B1, B2, ..., Bn, num_segments].
    """
def compute_column_logits(sequence_output, column_output_weights, column_output_bias, cell_index, cell_mask, allow_empty_column_selection):
    """
    Computes the column logits.

    Args:
        sequence_output (`torch.FloatTensor` of shape `(batch_size, sequence_length, hidden_size)`):
            Also known as last_hidden_state. Sequence of hidden-states at the output of the last layer of the model.
        column_output_weights (`torch.FloatTensor` of shape `(hidden_size)`):
            Weights of the linear layer for column selection.
        column_output_bias (`torch.FloatTensor` of shape `()`):
            Bias of the linear layer for column selection.
        cell_index (`ProductIndexMap`):
            Index that groups tokens into cells.
        cell_mask (`torch.FloatTensor` of shape `(batch_size, max_num_rows * max_num_cols)`):
            Mask for cells that exist in the table (i.e. that are not padding).
        allow_empty_column_selection (`bool`):
            Whether to allow not to select any column

    Returns:
        column_logits (`torch.FloatTensor`of shape `(batch_size, max_num_cols)`): Tensor containing the column logits
        for every example in the batch.
    """
def compute_token_logits(sequence_output, temperature, output_weights, output_bias):
    """
    Computes logits per token

    Args:
        sequence_output (`torch.FloatTensor` of shape `(batch_size, sequence_length, hidden_size)`):
            Also known as last_hidden_state. Sequence of hidden-states at the output of the last layer of the model.
        temperature (`float`):
            Temperature for the Bernoulli distribution.
        output_weights (`torch.FloatTensor` of shape `(hidden_size,)`):
            Weights of the linear layer for cell selection.
        output_bias (`torch.FloatTensor` of shape `()`):
            Bias of the linear layer for cell selection

    Returns:
        logits (`torch.FloatTensor` of shape `(batch_size, sequence_length)`): Logits per token.
    """
def huber_loss(input, target, delta: float = 1.0): ...
