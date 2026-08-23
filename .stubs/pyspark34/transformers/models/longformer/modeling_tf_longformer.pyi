import numpy as np
import tensorflow as tf
from ...activations_tf import get_tf_activation as get_tf_activation
from ...modeling_tf_utils import TFMaskedLanguageModelingLoss as TFMaskedLanguageModelingLoss, TFModelInputType as TFModelInputType, TFMultipleChoiceLoss as TFMultipleChoiceLoss, TFPreTrainedModel as TFPreTrainedModel, TFQuestionAnsweringLoss as TFQuestionAnsweringLoss, TFSequenceClassificationLoss as TFSequenceClassificationLoss, TFTokenClassificationLoss as TFTokenClassificationLoss, get_initializer as get_initializer, keras_serializable as keras_serializable, unpack_inputs as unpack_inputs
from ...tf_utils import shape_list as shape_list, stable_softmax as stable_softmax
from ...utils import MULTIPLE_CHOICE_DUMMY_INPUTS as MULTIPLE_CHOICE_DUMMY_INPUTS, ModelOutput as ModelOutput, add_code_sample_docstrings as add_code_sample_docstrings, add_start_docstrings as add_start_docstrings, add_start_docstrings_to_model_forward as add_start_docstrings_to_model_forward, logging as logging
from .configuration_longformer import LongformerConfig as LongformerConfig
from _typeshed import Incomplete
from dataclasses import dataclass
from typing import Optional, Tuple, Union

logger: Incomplete
LARGE_NEGATIVE: float
TF_LONGFORMER_PRETRAINED_MODEL_ARCHIVE_LIST: Incomplete

@dataclass
class TFLongformerBaseModelOutput(ModelOutput):
    """
    Base class for Longformer's outputs, with potential hidden states, local and global attentions.

    Args:
        last_hidden_state (`tf.Tensor` of shape `(batch_size, sequence_length, hidden_size)`):
            Sequence of hidden-states at the output of the last layer of the model.
        hidden_states (`tuple(tf.Tensor)`, *optional*, returned when `output_hidden_states=True` is passed or when `config.output_hidden_states=True`):
            Tuple of `tf.Tensor` (one for the output of the embeddings + one for the output of each layer) of shape
            `(batch_size, sequence_length, hidden_size)`.

            Hidden-states of the model at the output of each layer plus the initial embedding outputs.
        attentions (`tuple(tf.Tensor)`, *optional*, returned when `output_attentions=True` is passed or when `config.output_attentions=True`):
            Tuple of `tf.Tensor` (one for each layer) of shape `(batch_size, num_heads, sequence_length, x +
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
        global_attentions (`tuple(tf.Tensor)`, *optional*, returned when `output_attentions=True` is passed or when `config.output_attentions=True`):
            Tuple of `tf.Tensor` (one for each layer) of shape `(batch_size, num_heads, sequence_length, x)`, where `x`
            is the number of tokens with global attention mask.

            Global attentions weights after the attention softmax, used to compute the weighted average in the
            self-attention heads. Those are the attention weights from every token with global attention to every token
            in the sequence.
    """
    last_hidden_state: tf.Tensor = ...
    hidden_states: Optional[Tuple[tf.Tensor]] = ...
    attentions: Optional[Tuple[tf.Tensor]] = ...
    global_attentions: Optional[Tuple[tf.Tensor]] = ...
    def __init__(self, last_hidden_state, hidden_states, attentions, global_attentions) -> None: ...

@dataclass
class TFLongformerBaseModelOutputWithPooling(ModelOutput):
    """
    Base class for Longformer's outputs that also contains a pooling of the last hidden states.

    Args:
        last_hidden_state (`tf.Tensor` of shape `(batch_size, sequence_length, hidden_size)`):
            Sequence of hidden-states at the output of the last layer of the model.
        pooler_output (`tf.Tensor` of shape `(batch_size, hidden_size)`):
            Last layer hidden-state of the first token of the sequence (classification token) further processed by a
            Linear layer and a Tanh activation function. The Linear layer weights are trained from the next sentence
            prediction (classification) objective during pretraining.
        hidden_states (`tuple(tf.Tensor)`, *optional*, returned when `output_hidden_states=True` is passed or when `config.output_hidden_states=True`):
            Tuple of `tf.Tensor` (one for the output of the embeddings + one for the output of each layer) of shape
            `(batch_size, sequence_length, hidden_size)`.

            Hidden-states of the model at the output of each layer plus the initial embedding outputs.
        attentions (`tuple(tf.Tensor)`, *optional*, returned when `output_attentions=True` is passed or when `config.output_attentions=True`):
            Tuple of `tf.Tensor` (one for each layer) of shape `(batch_size, num_heads, sequence_length, x +
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
        global_attentions (`tuple(tf.Tensor)`, *optional*, returned when `output_attentions=True` is passed or when `config.output_attentions=True`):
            Tuple of `tf.Tensor` (one for each layer) of shape `(batch_size, num_heads, sequence_length, x)`, where `x`
            is the number of tokens with global attention mask.

            Global attentions weights after the attention softmax, used to compute the weighted average in the
            self-attention heads. Those are the attention weights from every token with global attention to every token
            in the sequence.
    """
    last_hidden_state: tf.Tensor = ...
    pooler_output: tf.Tensor = ...
    hidden_states: Optional[Tuple[tf.Tensor]] = ...
    attentions: Optional[Tuple[tf.Tensor]] = ...
    global_attentions: Optional[Tuple[tf.Tensor]] = ...
    def __init__(self, last_hidden_state, pooler_output, hidden_states, attentions, global_attentions) -> None: ...

@dataclass
class TFLongformerMaskedLMOutput(ModelOutput):
    """
    Base class for masked language models outputs.

    Args:
        loss (`tf.Tensor` of shape `(1,)`, *optional*, returned when `labels` is provided):
            Masked language modeling (MLM) loss.
        logits (`tf.Tensor` of shape `(batch_size, sequence_length, config.vocab_size)`):
            Prediction scores of the language modeling head (scores for each vocabulary token before SoftMax).
        hidden_states (`tuple(tf.Tensor)`, *optional*, returned when `output_hidden_states=True` is passed or when `config.output_hidden_states=True`):
            Tuple of `tf.Tensor` (one for the output of the embeddings + one for the output of each layer) of shape
            `(batch_size, sequence_length, hidden_size)`.

            Hidden-states of the model at the output of each layer plus the initial embedding outputs.
        attentions (`tuple(tf.Tensor)`, *optional*, returned when `output_attentions=True` is passed or when `config.output_attentions=True`):
            Tuple of `tf.Tensor` (one for each layer) of shape `(batch_size, num_heads, sequence_length, x +
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
        global_attentions (`tuple(tf.Tensor)`, *optional*, returned when `output_attentions=True` is passed or when `config.output_attentions=True`):
            Tuple of `tf.Tensor` (one for each layer) of shape `(batch_size, num_heads, sequence_length, x)`, where `x`
            is the number of tokens with global attention mask.

            Global attentions weights after the attention softmax, used to compute the weighted average in the
            self-attention heads. Those are the attention weights from every token with global attention to every token
            in the sequence.
    """
    loss: Optional[tf.Tensor] = ...
    logits: tf.Tensor = ...
    hidden_states: Optional[Tuple[tf.Tensor]] = ...
    attentions: Optional[Tuple[tf.Tensor]] = ...
    global_attentions: Optional[Tuple[tf.Tensor]] = ...
    def __init__(self, loss, logits, hidden_states, attentions, global_attentions) -> None: ...

@dataclass
class TFLongformerQuestionAnsweringModelOutput(ModelOutput):
    """
    Base class for outputs of question answering Longformer models.

    Args:
        loss (`tf.Tensor` of shape `(1,)`, *optional*, returned when `labels` is provided):
            Total span extraction loss is the sum of a Cross-Entropy for the start and end positions.
        start_logits (`tf.Tensor` of shape `(batch_size, sequence_length)`):
            Span-start scores (before SoftMax).
        end_logits (`tf.Tensor` of shape `(batch_size, sequence_length)`):
            Span-end scores (before SoftMax).
        hidden_states (`tuple(tf.Tensor)`, *optional*, returned when `output_hidden_states=True` is passed or when `config.output_hidden_states=True`):
            Tuple of `tf.Tensor` (one for the output of the embeddings + one for the output of each layer) of shape
            `(batch_size, sequence_length, hidden_size)`.

            Hidden-states of the model at the output of each layer plus the initial embedding outputs.
        attentions (`tuple(tf.Tensor)`, *optional*, returned when `output_attentions=True` is passed or when `config.output_attentions=True`):
            Tuple of `tf.Tensor` (one for each layer) of shape `(batch_size, num_heads, sequence_length, x +
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
        global_attentions (`tuple(tf.Tensor)`, *optional*, returned when `output_attentions=True` is passed or when `config.output_attentions=True`):
            Tuple of `tf.Tensor` (one for each layer) of shape `(batch_size, num_heads, sequence_length, x)`, where `x`
            is the number of tokens with global attention mask.

            Global attentions weights after the attention softmax, used to compute the weighted average in the
            self-attention heads. Those are the attention weights from every token with global attention to every token
            in the sequence.
    """
    loss: Optional[tf.Tensor] = ...
    start_logits: tf.Tensor = ...
    end_logits: tf.Tensor = ...
    hidden_states: Optional[Tuple[tf.Tensor]] = ...
    attentions: Optional[Tuple[tf.Tensor]] = ...
    global_attentions: Optional[Tuple[tf.Tensor]] = ...
    def __init__(self, loss, start_logits, end_logits, hidden_states, attentions, global_attentions) -> None: ...

@dataclass
class TFLongformerSequenceClassifierOutput(ModelOutput):
    """
    Base class for outputs of sentence classification models.

    Args:
        loss (`tf.Tensor` of shape `(1,)`, *optional*, returned when `labels` is provided):
            Classification (or regression if config.num_labels==1) loss.
        logits (`tf.Tensor` of shape `(batch_size, config.num_labels)`):
            Classification (or regression if config.num_labels==1) scores (before SoftMax).
        hidden_states (`tuple(tf.Tensor)`, *optional*, returned when `output_hidden_states=True` is passed or when `config.output_hidden_states=True`):
            Tuple of `tf.Tensor` (one for the output of the embeddings + one for the output of each layer) of shape
            `(batch_size, sequence_length, hidden_size)`.

            Hidden-states of the model at the output of each layer plus the initial embedding outputs.
        attentions (`tuple(tf.Tensor)`, *optional*, returned when `output_attentions=True` is passed or when `config.output_attentions=True`):
            Tuple of `tf.Tensor` (one for each layer) of shape `(batch_size, num_heads, sequence_length, x +
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
        global_attentions (`tuple(tf.Tensor)`, *optional*, returned when `output_attentions=True` is passed or when `config.output_attentions=True`):
            Tuple of `tf.Tensor` (one for each layer) of shape `(batch_size, num_heads, sequence_length, x)`, where `x`
            is the number of tokens with global attention mask.

            Global attentions weights after the attention softmax, used to compute the weighted average in the
            self-attention heads. Those are the attention weights from every token with global attention to every token
            in the sequence.
    """
    loss: Optional[tf.Tensor] = ...
    logits: tf.Tensor = ...
    hidden_states: Optional[Tuple[tf.Tensor]] = ...
    attentions: Optional[Tuple[tf.Tensor]] = ...
    global_attentions: Optional[Tuple[tf.Tensor]] = ...
    def __init__(self, loss, logits, hidden_states, attentions, global_attentions) -> None: ...

@dataclass
class TFLongformerMultipleChoiceModelOutput(ModelOutput):
    """
    Base class for outputs of multiple choice models.

    Args:
        loss (`tf.Tensor` of shape *(1,)*, *optional*, returned when `labels` is provided):
            Classification loss.
        logits (`tf.Tensor` of shape `(batch_size, num_choices)`):
            *num_choices* is the second dimension of the input tensors. (see *input_ids* above).

            Classification scores (before SoftMax).
        hidden_states (`tuple(tf.Tensor)`, *optional*, returned when `output_hidden_states=True` is passed or when `config.output_hidden_states=True`):
            Tuple of `tf.Tensor` (one for the output of the embeddings + one for the output of each layer) of shape
            `(batch_size, sequence_length, hidden_size)`.

            Hidden-states of the model at the output of each layer plus the initial embedding outputs.
        attentions (`tuple(tf.Tensor)`, *optional*, returned when `output_attentions=True` is passed or when `config.output_attentions=True`):
            Tuple of `tf.Tensor` (one for each layer) of shape `(batch_size, num_heads, sequence_length, x +
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
        global_attentions (`tuple(tf.Tensor)`, *optional*, returned when `output_attentions=True` is passed or when `config.output_attentions=True`):
            Tuple of `tf.Tensor` (one for each layer) of shape `(batch_size, num_heads, sequence_length, x)`, where `x`
            is the number of tokens with global attention mask.

            Global attentions weights after the attention softmax, used to compute the weighted average in the
            self-attention heads. Those are the attention weights from every token with global attention to every token
            in the sequence.
    """
    loss: Optional[tf.Tensor] = ...
    logits: tf.Tensor = ...
    hidden_states: Optional[Tuple[tf.Tensor]] = ...
    attentions: Optional[Tuple[tf.Tensor]] = ...
    global_attentions: Optional[Tuple[tf.Tensor]] = ...
    def __init__(self, loss, logits, hidden_states, attentions, global_attentions) -> None: ...

@dataclass
class TFLongformerTokenClassifierOutput(ModelOutput):
    """
    Base class for outputs of token classification models.

    Args:
        loss (`tf.Tensor` of shape `(1,)`, *optional*, returned when `labels` is provided) :
            Classification loss.
        logits (`tf.Tensor` of shape `(batch_size, sequence_length, config.num_labels)`):
            Classification scores (before SoftMax).
        hidden_states (`tuple(tf.Tensor)`, *optional*, returned when `output_hidden_states=True` is passed or when `config.output_hidden_states=True`):
            Tuple of `tf.Tensor` (one for the output of the embeddings + one for the output of each layer) of shape
            `(batch_size, sequence_length, hidden_size)`.

            Hidden-states of the model at the output of each layer plus the initial embedding outputs.
        attentions (`tuple(tf.Tensor)`, *optional*, returned when `output_attentions=True` is passed or when `config.output_attentions=True`):
            Tuple of `tf.Tensor` (one for each layer) of shape `(batch_size, num_heads, sequence_length, x +
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
        global_attentions (`tuple(tf.Tensor)`, *optional*, returned when `output_attentions=True` is passed or when `config.output_attentions=True`):
            Tuple of `tf.Tensor` (one for each layer) of shape `(batch_size, num_heads, sequence_length, x)`, where `x`
            is the number of tokens with global attention mask.

            Global attentions weights after the attention softmax, used to compute the weighted average in the
            self-attention heads. Those are the attention weights from every token with global attention to every token
            in the sequence.
    """
    loss: Optional[tf.Tensor] = ...
    logits: tf.Tensor = ...
    hidden_states: Optional[Tuple[tf.Tensor]] = ...
    attentions: Optional[Tuple[tf.Tensor]] = ...
    global_attentions: Optional[Tuple[tf.Tensor]] = ...
    def __init__(self, loss, logits, hidden_states, attentions, global_attentions) -> None: ...

class TFLongformerLMHead(tf.keras.layers.Layer):
    """Longformer Head for masked language modeling."""
    config: Incomplete
    hidden_size: Incomplete
    dense: Incomplete
    layer_norm: Incomplete
    act: Incomplete
    decoder: Incomplete
    def __init__(self, config, input_embeddings, **kwargs) -> None: ...
    bias: Incomplete
    def build(self, input_shape) -> None: ...
    def get_output_embeddings(self): ...
    def set_output_embeddings(self, value) -> None: ...
    def get_bias(self): ...
    def set_bias(self, value) -> None: ...
    def call(self, hidden_states): ...

class TFLongformerEmbeddings(tf.keras.layers.Layer):
    """
    Same as BertEmbeddings with a tiny tweak for positional embeddings indexing and some extra casting.
    """
    padding_idx: int
    config: Incomplete
    hidden_size: Incomplete
    max_position_embeddings: Incomplete
    initializer_range: Incomplete
    LayerNorm: Incomplete
    dropout: Incomplete
    def __init__(self, config, **kwargs) -> None: ...
    weight: Incomplete
    token_type_embeddings: Incomplete
    position_embeddings: Incomplete
    def build(self, input_shape: tf.TensorShape): ...
    def create_position_ids_from_input_ids(self, input_ids, past_key_values_length: int = 0):
        """
        Replace non-padding symbols with their position numbers. Position numbers begin at padding_idx+1. Padding
        symbols are ignored. This is modified from fairseq's `utils.make_positions`.

        Args:
            input_ids: tf.Tensor
        Returns: tf.Tensor
        """
    def call(self, input_ids: Incomplete | None = None, position_ids: Incomplete | None = None, token_type_ids: Incomplete | None = None, inputs_embeds: Incomplete | None = None, past_key_values_length: int = 0, training: bool = False):
        """
        Applies embedding based on inputs tensor.

        Returns:
            final_embeddings (`tf.Tensor`): output embedding tensor.
        """

class TFLongformerIntermediate(tf.keras.layers.Layer):
    dense: Incomplete
    intermediate_act_fn: Incomplete
    def __init__(self, config: LongformerConfig, **kwargs) -> None: ...
    def call(self, hidden_states: tf.Tensor) -> tf.Tensor: ...

class TFLongformerOutput(tf.keras.layers.Layer):
    dense: Incomplete
    LayerNorm: Incomplete
    dropout: Incomplete
    def __init__(self, config: LongformerConfig, **kwargs) -> None: ...
    def call(self, hidden_states: tf.Tensor, input_tensor: tf.Tensor, training: bool = False) -> tf.Tensor: ...

class TFLongformerPooler(tf.keras.layers.Layer):
    dense: Incomplete
    def __init__(self, config: LongformerConfig, **kwargs) -> None: ...
    def call(self, hidden_states: tf.Tensor) -> tf.Tensor: ...

class TFLongformerSelfOutput(tf.keras.layers.Layer):
    dense: Incomplete
    LayerNorm: Incomplete
    dropout: Incomplete
    def __init__(self, config: LongformerConfig, **kwargs) -> None: ...
    def call(self, hidden_states: tf.Tensor, input_tensor: tf.Tensor, training: bool = False) -> tf.Tensor: ...

class TFLongformerSelfAttention(tf.keras.layers.Layer):
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
    global_dropout: Incomplete
    layer_id: Incomplete
    one_sided_attn_window_size: Incomplete
    def __init__(self, config, layer_id, **kwargs) -> None: ...
    def call(self, inputs, training: bool = False):
        """
        LongformerSelfAttention expects *len(hidden_states)* to be multiple of *attention_window*. Padding to
        *attention_window* happens in LongformerModel.forward to avoid redoing the padding on each layer.

        The *attention_mask* is changed in [`LongformerModel.forward`] from 0, 1, 2 to:

            - -10000: no attention
            - 0: local attention
            - +10000: global attention
        """
    def reshape_and_transpose(self, vector, batch_size): ...

class TFLongformerAttention(tf.keras.layers.Layer):
    self_attention: Incomplete
    dense_output: Incomplete
    def __init__(self, config, layer_id: int = 0, **kwargs) -> None: ...
    def prune_heads(self, heads) -> None: ...
    def call(self, inputs, training: bool = False): ...

class TFLongformerLayer(tf.keras.layers.Layer):
    attention: Incomplete
    intermediate: Incomplete
    longformer_output: Incomplete
    def __init__(self, config, layer_id: int = 0, **kwargs) -> None: ...
    def call(self, inputs, training: bool = False): ...

class TFLongformerEncoder(tf.keras.layers.Layer):
    output_hidden_states: Incomplete
    output_attentions: Incomplete
    layer: Incomplete
    def __init__(self, config, **kwargs) -> None: ...
    def call(self, hidden_states, attention_mask: Incomplete | None = None, head_mask: Incomplete | None = None, padding_len: int = 0, is_index_masked: Incomplete | None = None, is_index_global_attn: Incomplete | None = None, is_global_attn: Incomplete | None = None, output_attentions: Incomplete | None = None, output_hidden_states: Incomplete | None = None, return_dict: Incomplete | None = None, training: bool = False): ...

class TFLongformerMainLayer(tf.keras.layers.Layer):
    config_class = LongformerConfig
    config: Incomplete
    num_hidden_layers: Incomplete
    initializer_range: Incomplete
    output_attentions: Incomplete
    output_hidden_states: Incomplete
    return_dict: Incomplete
    pad_token_id: Incomplete
    attention_window: Incomplete
    embeddings: Incomplete
    encoder: Incomplete
    pooler: Incomplete
    def __init__(self, config, add_pooling_layer: bool = True, **kwargs) -> None: ...
    def get_input_embeddings(self): ...
    def set_input_embeddings(self, value) -> None: ...
    def call(self, input_ids: Incomplete | None = None, attention_mask: Incomplete | None = None, head_mask: Incomplete | None = None, global_attention_mask: Incomplete | None = None, token_type_ids: Incomplete | None = None, position_ids: Incomplete | None = None, inputs_embeds: Incomplete | None = None, output_attentions: Incomplete | None = None, output_hidden_states: Incomplete | None = None, return_dict: Incomplete | None = None, training: bool = False): ...

class TFLongformerPreTrainedModel(TFPreTrainedModel):
    """
    An abstract class to handle weights initialization and a simple interface for downloading and loading pretrained
    models.
    """
    config_class = LongformerConfig
    base_model_prefix: str
    @property
    def dummy_inputs(self): ...
    def serving(self, inputs): ...

LONGFORMER_START_DOCSTRING: str
LONGFORMER_INPUTS_DOCSTRING: str

class TFLongformerModel(TFLongformerPreTrainedModel):
    """

    This class copies code from [`TFRobertaModel`] and overwrites standard self-attention with longformer
    self-attention to provide the ability to process long sequences following the self-attention approach described in
    [Longformer: the Long-Document Transformer](https://arxiv.org/abs/2004.05150) by Iz Beltagy, Matthew E. Peters, and
    Arman Cohan. Longformer self-attention combines a local (sliding window) and global attention to extend to long
    documents without the O(n^2) increase in memory and compute.

    The self-attention module `TFLongformerSelfAttention` implemented here supports the combination of local and global
    attention but it lacks support for autoregressive attention and dilated attention. Autoregressive and dilated
    attention are more relevant for autoregressive language modeling than finetuning on downstream tasks. Future
    release will add support for autoregressive attention, but the support for dilated attention requires a custom CUDA
    kernel to be memory and compute efficient.

    """
    longformer: Incomplete
    def __init__(self, config, *inputs, **kwargs) -> None: ...
    def call(self, input_ids: Optional[TFModelInputType] = None, attention_mask: Optional[Union[np.ndarray, tf.Tensor]] = None, head_mask: Optional[Union[np.ndarray, tf.Tensor]] = None, global_attention_mask: Optional[Union[np.ndarray, tf.Tensor]] = None, token_type_ids: Optional[Union[np.ndarray, tf.Tensor]] = None, position_ids: Optional[Union[np.ndarray, tf.Tensor]] = None, inputs_embeds: Optional[Union[np.ndarray, tf.Tensor]] = None, output_attentions: Optional[bool] = None, output_hidden_states: Optional[bool] = None, return_dict: Optional[bool] = None, training: Optional[bool] = False) -> Union[TFLongformerBaseModelOutputWithPooling, Tuple[tf.Tensor]]: ...
    def serving_output(self, output): ...

class TFLongformerForMaskedLM(TFLongformerPreTrainedModel, TFMaskedLanguageModelingLoss):
    longformer: Incomplete
    lm_head: Incomplete
    def __init__(self, config, *inputs, **kwargs) -> None: ...
    def get_lm_head(self): ...
    def get_prefix_bias_name(self): ...
    def call(self, input_ids: Optional[TFModelInputType] = None, attention_mask: Optional[Union[np.ndarray, tf.Tensor]] = None, head_mask: Optional[Union[np.ndarray, tf.Tensor]] = None, global_attention_mask: Optional[Union[np.ndarray, tf.Tensor]] = None, token_type_ids: Optional[Union[np.ndarray, tf.Tensor]] = None, position_ids: Optional[Union[np.ndarray, tf.Tensor]] = None, inputs_embeds: Optional[Union[np.ndarray, tf.Tensor]] = None, output_attentions: Optional[bool] = None, output_hidden_states: Optional[bool] = None, return_dict: Optional[bool] = None, labels: Optional[Union[np.ndarray, tf.Tensor]] = None, training: Optional[bool] = False) -> Union[TFLongformerMaskedLMOutput, Tuple[tf.Tensor]]:
        """
        labels (`tf.Tensor` of shape `(batch_size, sequence_length)`, *optional*):
            Labels for computing the masked language modeling loss. Indices should be in `[-100, 0, ...,
            config.vocab_size]` (see `input_ids` docstring) Tokens with indices set to `-100` are ignored (masked), the
            loss is only computed for the tokens with labels in `[0, ..., config.vocab_size]`
        """
    def serving_output(self, output): ...

class TFLongformerForQuestionAnswering(TFLongformerPreTrainedModel, TFQuestionAnsweringLoss):
    num_labels: Incomplete
    longformer: Incomplete
    qa_outputs: Incomplete
    def __init__(self, config, *inputs, **kwargs) -> None: ...
    def call(self, input_ids: Optional[TFModelInputType] = None, attention_mask: Optional[Union[np.ndarray, tf.Tensor]] = None, head_mask: Optional[Union[np.ndarray, tf.Tensor]] = None, global_attention_mask: Optional[Union[np.ndarray, tf.Tensor]] = None, token_type_ids: Optional[Union[np.ndarray, tf.Tensor]] = None, position_ids: Optional[Union[np.ndarray, tf.Tensor]] = None, inputs_embeds: Optional[Union[np.ndarray, tf.Tensor]] = None, output_attentions: Optional[bool] = None, output_hidden_states: Optional[bool] = None, return_dict: Optional[bool] = None, start_positions: Optional[Union[np.ndarray, tf.Tensor]] = None, end_positions: Optional[Union[np.ndarray, tf.Tensor]] = None, training: Optional[bool] = False) -> Union[TFLongformerQuestionAnsweringModelOutput, Tuple[tf.Tensor]]:
        """
        start_positions (`tf.Tensor` of shape `(batch_size,)`, *optional*):
            Labels for position (index) of the start of the labelled span for computing the token classification loss.
            Positions are clamped to the length of the sequence (*sequence_length*). Position outside of the sequence
            are not taken into account for computing the loss.
        end_positions (`tf.Tensor` of shape `(batch_size,)`, *optional*):
            Labels for position (index) of the end of the labelled span for computing the token classification loss.
            Positions are clamped to the length of the sequence (*sequence_length*). Position outside of the sequence
            are not taken into account for computing the loss.
        """
    def serving_output(self, output): ...

class TFLongformerClassificationHead(tf.keras.layers.Layer):
    """Head for sentence-level classification tasks."""
    dense: Incomplete
    dropout: Incomplete
    out_proj: Incomplete
    def __init__(self, config, **kwargs) -> None: ...
    def call(self, hidden_states, training: bool = False): ...

class TFLongformerForSequenceClassification(TFLongformerPreTrainedModel, TFSequenceClassificationLoss):
    num_labels: Incomplete
    longformer: Incomplete
    classifier: Incomplete
    def __init__(self, config, *inputs, **kwargs) -> None: ...
    def call(self, input_ids: Optional[TFModelInputType] = None, attention_mask: Optional[Union[np.ndarray, tf.Tensor]] = None, head_mask: Optional[Union[np.ndarray, tf.Tensor]] = None, token_type_ids: Optional[Union[np.ndarray, tf.Tensor]] = None, position_ids: Optional[Union[np.ndarray, tf.Tensor]] = None, global_attention_mask: Optional[Union[np.ndarray, tf.Tensor]] = None, inputs_embeds: Optional[Union[np.ndarray, tf.Tensor]] = None, output_attentions: Optional[bool] = None, output_hidden_states: Optional[bool] = None, return_dict: Optional[bool] = None, labels: Optional[Union[np.ndarray, tf.Tensor]] = None, training: Optional[bool] = False) -> Union[TFLongformerSequenceClassifierOutput, Tuple[tf.Tensor]]: ...
    def serving_output(self, output): ...

class TFLongformerForMultipleChoice(TFLongformerPreTrainedModel, TFMultipleChoiceLoss):
    longformer: Incomplete
    dropout: Incomplete
    classifier: Incomplete
    def __init__(self, config, *inputs, **kwargs) -> None: ...
    @property
    def dummy_inputs(self): ...
    def call(self, input_ids: Optional[TFModelInputType] = None, attention_mask: Optional[Union[np.ndarray, tf.Tensor]] = None, head_mask: Optional[Union[np.ndarray, tf.Tensor]] = None, token_type_ids: Optional[Union[np.ndarray, tf.Tensor]] = None, position_ids: Optional[Union[np.ndarray, tf.Tensor]] = None, global_attention_mask: Optional[Union[np.ndarray, tf.Tensor]] = None, inputs_embeds: Optional[Union[np.ndarray, tf.Tensor]] = None, output_attentions: Optional[bool] = None, output_hidden_states: Optional[bool] = None, return_dict: Optional[bool] = None, labels: Optional[Union[np.ndarray, tf.Tensor]] = None, training: Optional[bool] = False) -> Union[TFLongformerMultipleChoiceModelOutput, Tuple[tf.Tensor]]:
        """
        labels (`tf.Tensor` of shape `(batch_size,)`, *optional*):
            Labels for computing the multiple choice classification loss. Indices should be in `[0, ..., num_choices]`
            where `num_choices` is the size of the second dimension of the input tensors. (See `input_ids` above)
        """
    def serving(self, inputs): ...
    def serving_output(self, output): ...

class TFLongformerForTokenClassification(TFLongformerPreTrainedModel, TFTokenClassificationLoss):
    num_labels: Incomplete
    longformer: Incomplete
    dropout: Incomplete
    classifier: Incomplete
    def __init__(self, config, *inputs, **kwargs) -> None: ...
    def call(self, input_ids: Optional[TFModelInputType] = None, attention_mask: Optional[Union[np.ndarray, tf.Tensor]] = None, head_mask: Optional[Union[np.ndarray, tf.Tensor]] = None, token_type_ids: Optional[Union[np.ndarray, tf.Tensor]] = None, position_ids: Optional[Union[np.ndarray, tf.Tensor]] = None, global_attention_mask: Optional[Union[np.ndarray, tf.Tensor]] = None, inputs_embeds: Optional[Union[np.ndarray, tf.Tensor]] = None, output_attentions: Optional[bool] = None, output_hidden_states: Optional[bool] = None, return_dict: Optional[bool] = None, labels: Optional[Union[np.array, tf.Tensor]] = None, training: Optional[bool] = False) -> Union[TFLongformerTokenClassifierOutput, Tuple[tf.Tensor]]:
        """
        labels (`tf.Tensor` of shape `(batch_size, sequence_length)`, *optional*):
            Labels for computing the token classification loss. Indices should be in `[0, ..., config.num_labels - 1]`.
        """
    def serving_output(self, output): ...
