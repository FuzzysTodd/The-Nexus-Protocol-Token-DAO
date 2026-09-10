import enum
import numpy as np
import tensorflow as tf
from ...activations_tf import get_tf_activation as get_tf_activation
from ...modeling_tf_outputs import TFBaseModelOutputWithPastAndCrossAttentions as TFBaseModelOutputWithPastAndCrossAttentions, TFBaseModelOutputWithPooling as TFBaseModelOutputWithPooling, TFMaskedLMOutput as TFMaskedLMOutput, TFSequenceClassifierOutput as TFSequenceClassifierOutput
from ...modeling_tf_utils import TFMaskedLanguageModelingLoss as TFMaskedLanguageModelingLoss, TFModelInputType as TFModelInputType, TFPreTrainedModel as TFPreTrainedModel, TFSequenceClassificationLoss as TFSequenceClassificationLoss, get_initializer as get_initializer, keras_serializable as keras_serializable, unpack_inputs as unpack_inputs
from ...tf_utils import shape_list as shape_list, stable_softmax as stable_softmax
from ...utils import ModelOutput as ModelOutput, add_start_docstrings as add_start_docstrings, add_start_docstrings_to_model_forward as add_start_docstrings_to_model_forward, is_tensorflow_probability_available as is_tensorflow_probability_available, logging as logging, replace_return_docstrings as replace_return_docstrings, requires_backends as requires_backends
from .configuration_tapas import TapasConfig as TapasConfig
from _typeshed import Incomplete
from dataclasses import dataclass
from typing import Dict, Optional, Tuple, Union

logger: Incomplete
n: Incomplete
TF_TAPAS_PRETRAINED_MODEL_ARCHIVE_LIST: Incomplete
EPSILON_ZERO_DIVISION: float
CLOSE_ENOUGH_TO_LOG_ZERO: float

@dataclass
class TFTableQuestionAnsweringOutput(ModelOutput):
    """
    Output type of [`TFTapasForQuestionAnswering`].

    Args:
        loss (`tf.Tensor` of shape `(1,)`, *optional*, returned when `labels` (and possibly `answer`, `aggregation_labels`, `numeric_values` and `numeric_values_scale` are provided)):
            Total loss as the sum of the hierarchical cell selection log-likelihood loss and (optionally) the
            semi-supervised regression loss and (optionally) supervised loss for aggregations.
        logits (`tf.Tensor` of shape `(batch_size, sequence_length)`):
            Prediction scores of the cell selection head, for every token.
        logits_aggregation (`tf.Tensor`, *optional*, of shape `(batch_size, num_aggregation_labels)`):
            Prediction scores of the aggregation head, for every aggregation operator.
        hidden_states (`tuple(tf.Tensor)`, *optional*, returned when `output_hidden_states=True` is passed or when `config.output_hidden_states=True`):
            Tuple of `tf.Tensor` (one for the output of the embeddings + one for the output of each layer) of shape
            `(batch_size, sequence_length, hidden_size)`. Hidden-states of the model at the output of each layer plus
            the initial embedding outputs.
        attentions (`tuple(tf.Tensor)`, *optional*, returned when `output_attentions=True` is passed or when `config.output_attentions=True`):
            Tuple of `tf.Tensor` (one for each layer) of shape `(batch_size, num_heads, sequence_length,
            sequence_length)`. Attentions weights after the attention softmax, used to compute the weighted average in
            the self-attention heads.
    """
    loss: Optional[tf.Tensor] = ...
    logits: tf.Tensor = ...
    logits_aggregation: Optional[tf.Tensor] = ...
    hidden_states: Optional[Tuple[tf.Tensor]] = ...
    attentions: Optional[Tuple[tf.Tensor]] = ...
    def __init__(self, loss, logits, logits_aggregation, hidden_states, attentions) -> None: ...

class TFTapasEmbeddings(tf.keras.layers.Layer):
    """
    Construct the embeddings from word, position and token_type embeddings. Same as BertEmbeddings but with a number of
    additional token type embeddings to encode tabular structure.
    """
    config: Incomplete
    number_of_token_type_embeddings: Incomplete
    reset_position_index_per_cell: Incomplete
    hidden_size: Incomplete
    max_position_embeddings: Incomplete
    initializer_range: Incomplete
    LayerNorm: Incomplete
    dropout: Incomplete
    def __init__(self, config: TapasConfig, **kwargs) -> None: ...
    weight: Incomplete
    position_embeddings: Incomplete
    def build(self, input_shape: tf.TensorShape): ...
    def call(self, input_ids: tf.Tensor = None, position_ids: tf.Tensor = None, token_type_ids: tf.Tensor = None, inputs_embeds: tf.Tensor = None, training: bool = False) -> tf.Tensor:
        """
        Applies embedding based on inputs tensor.

        Returns:
            final_embeddings (`tf.Tensor`): output embedding tensor.
        """

class TFTapasSelfAttention(tf.keras.layers.Layer):
    num_attention_heads: Incomplete
    attention_head_size: Incomplete
    all_head_size: Incomplete
    sqrt_att_head_size: Incomplete
    query: Incomplete
    key: Incomplete
    value: Incomplete
    dropout: Incomplete
    is_decoder: Incomplete
    def __init__(self, config: TapasConfig, **kwargs) -> None: ...
    def transpose_for_scores(self, tensor: tf.Tensor, batch_size: int) -> tf.Tensor: ...
    def call(self, hidden_states: tf.Tensor, attention_mask: tf.Tensor, head_mask: tf.Tensor, encoder_hidden_states: tf.Tensor, encoder_attention_mask: tf.Tensor, past_key_value: Tuple[tf.Tensor], output_attentions: bool, training: bool = False) -> Tuple[tf.Tensor]: ...

class TFTapasSelfOutput(tf.keras.layers.Layer):
    dense: Incomplete
    LayerNorm: Incomplete
    dropout: Incomplete
    def __init__(self, config: TapasConfig, **kwargs) -> None: ...
    def call(self, hidden_states: tf.Tensor, input_tensor: tf.Tensor, training: bool = False) -> tf.Tensor: ...

class TFTapasAttention(tf.keras.layers.Layer):
    self_attention: Incomplete
    dense_output: Incomplete
    def __init__(self, config: TapasConfig, **kwargs) -> None: ...
    def prune_heads(self, heads) -> None: ...
    def call(self, input_tensor: tf.Tensor, attention_mask: tf.Tensor, head_mask: tf.Tensor, encoder_hidden_states: tf.Tensor, encoder_attention_mask: tf.Tensor, past_key_value: Tuple[tf.Tensor], output_attentions: bool, training: bool = False) -> Tuple[tf.Tensor]: ...

class TFTapasIntermediate(tf.keras.layers.Layer):
    dense: Incomplete
    intermediate_act_fn: Incomplete
    def __init__(self, config: TapasConfig, **kwargs) -> None: ...
    def call(self, hidden_states: tf.Tensor) -> tf.Tensor: ...

class TFTapasOutput(tf.keras.layers.Layer):
    dense: Incomplete
    LayerNorm: Incomplete
    dropout: Incomplete
    def __init__(self, config: TapasConfig, **kwargs) -> None: ...
    def call(self, hidden_states: tf.Tensor, input_tensor: tf.Tensor, training: bool = False) -> tf.Tensor: ...

class TFTapasLayer(tf.keras.layers.Layer):
    attention: Incomplete
    is_decoder: Incomplete
    add_cross_attention: Incomplete
    crossattention: Incomplete
    intermediate: Incomplete
    bert_output: Incomplete
    def __init__(self, config: TapasConfig, **kwargs) -> None: ...
    def call(self, hidden_states: tf.Tensor, attention_mask: tf.Tensor, head_mask: tf.Tensor, encoder_hidden_states: Optional[tf.Tensor], encoder_attention_mask: Optional[tf.Tensor], past_key_value: Optional[Tuple[tf.Tensor]], output_attentions: bool, training: bool = False) -> Tuple[tf.Tensor]: ...

class TFTapasEncoder(tf.keras.layers.Layer):
    config: Incomplete
    layer: Incomplete
    def __init__(self, config: TapasConfig, **kwargs) -> None: ...
    def call(self, hidden_states: tf.Tensor, attention_mask: tf.Tensor, head_mask: tf.Tensor, encoder_hidden_states: Optional[tf.Tensor], encoder_attention_mask: Optional[tf.Tensor], past_key_values: Optional[Tuple[Tuple[tf.Tensor]]], use_cache: Optional[bool], output_attentions: bool, output_hidden_states: bool, return_dict: bool, training: bool = False) -> Union[TFBaseModelOutputWithPastAndCrossAttentions, Tuple[tf.Tensor]]: ...

class TFTapasPooler(tf.keras.layers.Layer):
    dense: Incomplete
    def __init__(self, config: TapasConfig, **kwargs) -> None: ...
    def call(self, hidden_states: tf.Tensor) -> tf.Tensor: ...

class TFTapasPredictionHeadTransform(tf.keras.layers.Layer):
    dense: Incomplete
    transform_act_fn: Incomplete
    LayerNorm: Incomplete
    def __init__(self, config: TapasConfig, **kwargs) -> None: ...
    def call(self, hidden_states: tf.Tensor) -> tf.Tensor: ...

class TFTapasLMPredictionHead(tf.keras.layers.Layer):
    config: Incomplete
    hidden_size: Incomplete
    transform: Incomplete
    input_embeddings: Incomplete
    def __init__(self, config: TapasConfig, input_embeddings: tf.keras.layers.Layer, **kwargs) -> None: ...
    bias: Incomplete
    def build(self, input_shape: tf.TensorShape): ...
    def get_output_embeddings(self) -> tf.keras.layers.Layer: ...
    def set_output_embeddings(self, value: tf.Variable): ...
    def get_bias(self) -> Dict[str, tf.Variable]: ...
    def set_bias(self, value: tf.Variable): ...
    def call(self, hidden_states: tf.Tensor) -> tf.Tensor: ...

class TFTapasMLMHead(tf.keras.layers.Layer):
    predictions: Incomplete
    def __init__(self, config: TapasConfig, input_embeddings: tf.keras.layers.Layer, **kwargs) -> None: ...
    def call(self, sequence_output: tf.Tensor) -> tf.Tensor: ...

class TFTapasMainLayer(tf.keras.layers.Layer):
    config_class = TapasConfig
    config: Incomplete
    embeddings: Incomplete
    encoder: Incomplete
    pooler: Incomplete
    def __init__(self, config: TapasConfig, add_pooling_layer: bool = True, **kwargs) -> None: ...
    def get_input_embeddings(self) -> tf.keras.layers.Layer: ...
    def set_input_embeddings(self, value: tf.Variable): ...
    def call(self, input_ids: Optional[TFModelInputType] = None, attention_mask: Optional[Union[np.ndarray, tf.Tensor]] = None, token_type_ids: Optional[Union[np.ndarray, tf.Tensor]] = None, position_ids: Optional[Union[np.ndarray, tf.Tensor]] = None, head_mask: Optional[Union[np.ndarray, tf.Tensor]] = None, inputs_embeds: Optional[Union[np.ndarray, tf.Tensor]] = None, output_attentions: Optional[bool] = None, output_hidden_states: Optional[bool] = None, return_dict: Optional[bool] = None, training: bool = False) -> Union[TFBaseModelOutputWithPooling, Tuple[tf.Tensor]]: ...

class TFTapasPreTrainedModel(TFPreTrainedModel):
    """
    An abstract class to handle weights initialization and a simple interface for downloading and loading pretrained
    models.
    """
    config_class = TapasConfig
    base_model_prefix: str
    def serving(self, inputs): ...

TAPAS_START_DOCSTRING: str
TAPAS_INPUTS_DOCSTRING: str

class TFTapasModel(TFTapasPreTrainedModel):
    tapas: Incomplete
    def __init__(self, config: TapasConfig, *inputs, **kwargs) -> None: ...
    def call(self, input_ids: Optional[TFModelInputType] = None, attention_mask: Optional[Union[np.ndarray, tf.Tensor]] = None, token_type_ids: Optional[Union[np.ndarray, tf.Tensor]] = None, position_ids: Optional[Union[np.ndarray, tf.Tensor]] = None, head_mask: Optional[Union[np.ndarray, tf.Tensor]] = None, inputs_embeds: Optional[Union[np.ndarray, tf.Tensor]] = None, output_attentions: Optional[bool] = None, output_hidden_states: Optional[bool] = None, return_dict: Optional[bool] = None, training: Optional[bool] = False) -> Union[TFBaseModelOutputWithPooling, Tuple[tf.Tensor]]:
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

        >>> inputs = tokenizer(table=table, queries=queries, padding="max_length", return_tensors="tf")
        >>> outputs = model(**inputs)

        >>> last_hidden_states = outputs.last_hidden_state
        ```'''
    def serving_output(self, output: TFBaseModelOutputWithPooling) -> TFBaseModelOutputWithPooling: ...

class TFTapasForMaskedLM(TFTapasPreTrainedModel, TFMaskedLanguageModelingLoss):
    tapas: Incomplete
    lm_head: Incomplete
    def __init__(self, config: TapasConfig, *inputs, **kwargs) -> None: ...
    def get_lm_head(self) -> tf.keras.layers.Layer: ...
    def call(self, input_ids: Optional[TFModelInputType] = None, attention_mask: Optional[Union[np.ndarray, tf.Tensor]] = None, token_type_ids: Optional[Union[np.ndarray, tf.Tensor]] = None, position_ids: Optional[Union[np.ndarray, tf.Tensor]] = None, head_mask: Optional[Union[np.ndarray, tf.Tensor]] = None, inputs_embeds: Optional[Union[np.ndarray, tf.Tensor]] = None, output_attentions: Optional[bool] = None, output_hidden_states: Optional[bool] = None, return_dict: Optional[bool] = None, labels: Optional[Union[np.ndarray, tf.Tensor]] = None, training: Optional[bool] = False) -> Union[TFMaskedLMOutput, Tuple[tf.Tensor]]:
        '''
        labels (`tf.Tensor` or `np.ndarray` of shape `(batch_size, sequence_length)`, *optional*):
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
        ...     table=table, queries="How many [MASK] has George [MASK] played in?", return_tensors="tf"
        ... )
        >>> labels = tokenizer(
        ...     table=table, queries="How many movies has George Clooney played in?", return_tensors="tf"
        ... )["input_ids"]

        >>> outputs = model(**inputs, labels=labels)
        >>> logits = outputs.logits
        ```'''
    def serving_output(self, output: TFMaskedLMOutput) -> TFMaskedLMOutput: ...

class TFTapasComputeTokenLogits(tf.keras.layers.Layer):
    temperature: Incomplete
    output_weights: Incomplete
    output_bias: Incomplete
    def __init__(self, config: TapasConfig, **kwargs) -> None: ...
    def call(self, sequence_output: tf.Tensor) -> tf.Tensor:
        """
        Computes logits per token

        Args:
            sequence_output (`tf.Tensor` of shape `(batch_size, sequence_length, hidden_size)`):
                Also known as last_hidden_state. Sequence of hidden-states at the output of the last layer of the
                model.

        Returns:
            logits (`tf.Tensor` of shape `(batch_size, sequence_length)`): Logits per token.
        """

class TFTapasComputeColumnLogits(tf.keras.layers.Layer):
    column_output_weights: Incomplete
    column_output_bias: Incomplete
    def __init__(self, config: TapasConfig, **kwargs) -> None: ...
    def call(self, sequence_output, cell_index, cell_mask, allow_empty_column_selection) -> tf.Tensor:
        """
        Computes the column logits.

        Args:
            sequence_output (`tf.Tensor` of shape `(batch_size, sequence_length, hidden_size)`):
                Also known as last_hidden_state. Sequence of hidden-states at the output of the last layer of the
                model.
            cell_index (`ProductIndexMap`):
                Index that groups tokens into cells.
            cell_mask (`tf.Tensor` of shape `(batch_size, max_num_rows * max_num_cols)`):
                Mask for cells that exist in the table (i.e. that are not padding).
            allow_empty_column_selection (`bool`):
                Whether to allow not to select any column

        Returns:
            column_logits (`tf.Tensor`of shape `(batch_size, max_num_cols)`): Tensor containing the column logits for
            every example in the batch.
        """

class TFTapasForQuestionAnswering(TFTapasPreTrainedModel):
    tapas: Incomplete
    dropout: Incomplete
    compute_token_logits: Incomplete
    compute_column_logits: Incomplete
    aggregation_classifier: Incomplete
    config: Incomplete
    def __init__(self, config: TapasConfig, *inputs, **kwargs) -> None: ...
    def call(self, input_ids: Optional[TFModelInputType] = None, attention_mask: Optional[Union[np.ndarray, tf.Tensor]] = None, token_type_ids: Optional[Union[np.ndarray, tf.Tensor]] = None, position_ids: Optional[Union[np.ndarray, tf.Tensor]] = None, head_mask: Optional[Union[np.ndarray, tf.Tensor]] = None, inputs_embeds: Optional[Union[np.ndarray, tf.Tensor]] = None, table_mask: Optional[Union[np.ndarray, tf.Tensor]] = None, aggregation_labels: Optional[Union[np.ndarray, tf.Tensor]] = None, float_answer: Optional[Union[np.ndarray, tf.Tensor]] = None, numeric_values: Optional[Union[np.ndarray, tf.Tensor]] = None, numeric_values_scale: Optional[Union[np.ndarray, tf.Tensor]] = None, output_attentions: Optional[bool] = None, output_hidden_states: Optional[bool] = None, return_dict: Optional[bool] = None, labels: Optional[Union[np.ndarray, tf.Tensor]] = None, training: Optional[bool] = False) -> Union[TFTableQuestionAnsweringOutput, Tuple[tf.Tensor]]:
        '''
        table_mask (`tf.Tensor` of shape `(batch_size, seq_length)`, *optional*):
            Mask for the table. Indicates which tokens belong to the table (1). Question tokens, table headers and
            padding are 0.
        labels (`tf.Tensor` of shape `(batch_size, seq_length)`, *optional*):
            Labels per token for computing the hierarchical cell selection loss. This encodes the positions of the
            answer appearing in the table. Can be obtained using [`AutoTokenizer`].

            - 1 for tokens that are **part of the answer**,
            - 0 for tokens that are **not part of the answer**.

        aggregation_labels (`tf.Tensor` of shape `(batch_size, )`, *optional*):
            Aggregation function index for every example in the batch for computing the aggregation loss. Indices
            should be in `[0, ..., config.num_aggregation_labels - 1]`. Only required in case of strong supervision for
            aggregation (WikiSQL-supervised).
        float_answer (`tf.Tensor` of shape `(batch_size, )`, *optional*):
            Float answer for every example in the batch. Set to *float(\'nan\')* for cell selection questions. Only
            required in case of weak supervision (WTQ) to calculate the aggregate mask and regression loss.
        numeric_values (`tf.Tensor` of shape `(batch_size, seq_length)`, *optional*):
            Numeric values of every token, NaN for tokens which are not numeric values. Can be obtained using
            [`AutoTokenizer`]. Only required in case of weak supervision for aggregation (WTQ) to calculate the
            regression loss.
        numeric_values_scale (`tf.Tensor` of shape `(batch_size, seq_length)`, *optional*):
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

        >>> inputs = tokenizer(table=table, queries=queries, padding="max_length", return_tensors="tf")
        >>> outputs = model(**inputs)

        >>> logits = outputs.logits
        >>> logits_aggregation = outputs.logits_aggregation
        ```'''
    def serving_output(self, output: TFTableQuestionAnsweringOutput) -> TFTableQuestionAnsweringOutput: ...

class TFTapasForSequenceClassification(TFTapasPreTrainedModel, TFSequenceClassificationLoss):
    num_labels: Incomplete
    tapas: Incomplete
    dropout: Incomplete
    classifier: Incomplete
    def __init__(self, config: TapasConfig, *inputs, **kwargs) -> None: ...
    def call(self, input_ids: Optional[TFModelInputType] = None, attention_mask: Optional[Union[np.ndarray, tf.Tensor]] = None, token_type_ids: Optional[Union[np.ndarray, tf.Tensor]] = None, position_ids: Optional[Union[np.ndarray, tf.Tensor]] = None, head_mask: Optional[Union[np.ndarray, tf.Tensor]] = None, inputs_embeds: Optional[Union[np.ndarray, tf.Tensor]] = None, output_attentions: Optional[bool] = None, output_hidden_states: Optional[bool] = None, return_dict: Optional[bool] = None, labels: Optional[Union[np.ndarray, tf.Tensor]] = None, training: Optional[bool] = False) -> Union[TFSequenceClassifierOutput, Tuple[tf.Tensor]]:
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
        >>> import tensorflow as tf
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

        >>> inputs = tokenizer(table=table, queries=queries, padding="max_length", return_tensors="tf")
        >>> labels = tf.convert_to_tensor([1, 0])  # 1 means entailed, 0 means refuted

        >>> outputs = model(**inputs, labels=labels)
        >>> loss = outputs.loss
        >>> logits = outputs.logits
        ```'''
    def serving_output(self, output: TFSequenceClassifierOutput) -> TFSequenceClassifierOutput: ...

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
        Creates an index.

        Args:
          indices: <int32> Tensor of indices, same shape as `values`.
          num_segments: <int32> Scalar tensor, the number of segments. All elements
            in a batched segmented tensor must have the same number of segments (although many segments can be empty).
          batch_dims: Python integer, the number of batch dimensions. The first
            `batch_dims` dimensions of a SegmentedTensor are treated as batch dimensions. Segments in different batch
            elements are always distinct even if they have the same index.
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
        combines indices {0, .., n - 1} and {0, .., m - 1} into {0, .., nm - 1}. The output has `num_segments` equal to
        `outer_index.num_segements` * `inner_index.num_segments`.

        Args:
          outer_index: IndexMap.
          inner_index: IndexMap, must have the same shape as `outer_index`.
        """
    def project_outer(self, index):
        """Projects an index with the same index set onto the outer components."""
    def project_inner(self, index):
        """Projects an index with the same index set onto the inner components."""

def gather(values, index, name: str = 'segmented_gather'):
    """
    Gathers from `values` using the index map. For each element in the domain of the index map this operation looks up
    a value for that index in `values`. Two elements from the same segment always get assigned the same value.

    Args:
      values: [B1, ..., Bn, num_segments, V1, ...] Tensor with segment values.
      index: [B1, ..., Bn, I1, ..., Ik] IndexMap.
      name: Name for the TensorFlow operation.

    Returns:
      [B1, ..., Bn, I1, ..., Ik, V1, ...] Tensor with the gathered values.
    """
def flatten(index, name: str = 'segmented_flatten'):
    """
    Flattens a batched index map to a 1d index map. This operation relabels the segments to keep batch elements
    distinct. The k-th batch element will have indices shifted by `num_segments` * (k - 1). The result is a tensor with
    `num_segments` multiplied by the number of elements in the batch.

    Args:
      index: IndexMap to flatten.
      name: Name for the TensorFlow operation.

    Returns:
      The flattened IndexMap.
    """
def range_index_map(batch_shape, num_segments, name: str = 'range_index_map'):
    """
    Constructs an index map equal to range(num_segments).

    Args:
        batch_shape (`tf.Tensor`):
            Batch shape
        num_segments (`int`):
            Number of segments
        name (`str`, *optional*, defaults to 'range_index_map'):
            Name for the operation. Currently not used

    Returns:
        (`IndexMap`): IndexMap of shape batch_shape with elements equal to range(num_segments).
    """
def reduce_mean(values, index, name: str = 'segmented_reduce_mean'):
    """
    Averages a tensor over its segments. Outputs 0 for empty segments. This operations computes the mean over segments,
    with support for:

      - Batching using the first dimensions [B1, B2, ..., Bn]. Each element in a batch can have different indices.
      - Vectorization using the last dimension [V1, V2, ...]. If they are present the output will be a mean of vectors
        rather than scalars.
    Only the middle dimensions [I1, ..., Ik] are reduced by the operation.

    Args:
      values: [B1, B2, ..., Bn, I1, .., Ik, V1, V2, ..] tensor of values to be
        averaged.
      index: IndexMap [B1, B2, ..., Bn, I1, .., Ik] index defining the segments.
      name: Name for the TensorFlow ops.

    Returns:
      A pair (output_values, output_index) where `output_values` is a tensor of shape [B1, B2, ..., Bn, num_segments,
      V1, V2, ..] and `index` is an IndexMap with shape [B1, B2, ..., Bn, num_segments].
    """
def reduce_sum(values, index, name: str = 'segmented_reduce_sum'):
    """
    Sums a tensor over its segments. Outputs 0 for empty segments. This operations computes the sum over segments, with
    support for:

      - Batching using the first dimensions [B1, B2, ..., Bn]. Each element in a batch can have different indices.
      - Vectorization using the last dimension [V1, V2, ...]. If they are present the output will be a sum of vectors
        rather than scalars.
    Only the middle dimensions [I1, ..., Ik] are reduced by the operation.

    Args:
      values: [B1, B2, ..., Bn, I1, .., Ik, V1, V2, ..] tensor of values to be
        averaged.
      index: IndexMap [B1, B2, ..., Bn, I1, .., Ik] index defining the segments.
      name: Name for the TensorFlow ops.

    Returns:
      A pair (output_values, output_index) where `output_values` is a tensor of shape [B1, B2, ..., Bn, num_segments,
      V1, V2, ..] and `index` is an IndexMap with shape [B1, B2, ..., Bn, num_segments].
    """
def reduce_max(values, index, name: str = 'segmented_reduce_max'):
    """
    Computes the maximum over segments. This operations computes the maximum over segments, with support for:

      - Batching using the first dimensions [B1, B2, ..., Bn]. Each element in a batch can have different indices.
      - Vectorization using the last dimension [V1, V2, ...]. If they are present the output will be an element-wise
        maximum of vectors rather than scalars.
    Only the middle dimensions [I1, ..., Ik] are reduced by the operation.

    Args:
      values: [B1, B2, ..., Bn, I1, .., Ik, V1, V2, ..] tensor of values to be
        averaged.
      index: IndexMap [B1, B2, ..., Bn, I1, .., Ik] index defining the segments.
      name: Name for the TensorFlow ops.

    Returns:
      A pair (output_values, output_index) where `output_values` is a tensor of shape [B1, B2, ..., Bn, num_segments,
      V1, V2, ..] and `index` is an IndexMap with shape [B1, B2, ..., Bn, num_segments].
    """
def reduce_min(values, index, name: str = 'segmented_reduce_min'):
    """Computes the minimum over segments."""
