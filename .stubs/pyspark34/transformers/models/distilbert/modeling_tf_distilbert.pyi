import numpy as np
import tensorflow as tf
from ...activations_tf import get_tf_activation as get_tf_activation
from ...modeling_tf_outputs import TFBaseModelOutput as TFBaseModelOutput, TFMaskedLMOutput as TFMaskedLMOutput, TFMultipleChoiceModelOutput as TFMultipleChoiceModelOutput, TFQuestionAnsweringModelOutput as TFQuestionAnsweringModelOutput, TFSequenceClassifierOutput as TFSequenceClassifierOutput, TFTokenClassifierOutput as TFTokenClassifierOutput
from ...modeling_tf_utils import TFMaskedLanguageModelingLoss as TFMaskedLanguageModelingLoss, TFModelInputType as TFModelInputType, TFMultipleChoiceLoss as TFMultipleChoiceLoss, TFPreTrainedModel as TFPreTrainedModel, TFQuestionAnsweringLoss as TFQuestionAnsweringLoss, TFSequenceClassificationLoss as TFSequenceClassificationLoss, TFTokenClassificationLoss as TFTokenClassificationLoss, get_initializer as get_initializer, keras_serializable as keras_serializable, unpack_inputs as unpack_inputs
from ...tf_utils import shape_list as shape_list, stable_softmax as stable_softmax
from ...utils import MULTIPLE_CHOICE_DUMMY_INPUTS as MULTIPLE_CHOICE_DUMMY_INPUTS, add_code_sample_docstrings as add_code_sample_docstrings, add_start_docstrings as add_start_docstrings, add_start_docstrings_to_model_forward as add_start_docstrings_to_model_forward, logging as logging
from .configuration_distilbert import DistilBertConfig as DistilBertConfig
from _typeshed import Incomplete
from typing import Optional, Tuple, Union

logger: Incomplete
TF_DISTILBERT_PRETRAINED_MODEL_ARCHIVE_LIST: Incomplete

class TFEmbeddings(tf.keras.layers.Layer):
    """Construct the embeddings from word, position and token_type embeddings."""
    config: Incomplete
    dim: Incomplete
    initializer_range: Incomplete
    max_position_embeddings: Incomplete
    LayerNorm: Incomplete
    dropout: Incomplete
    def __init__(self, config, **kwargs) -> None: ...
    weight: Incomplete
    position_embeddings: Incomplete
    def build(self, input_shape: tf.TensorShape): ...
    def call(self, input_ids: Incomplete | None = None, position_ids: Incomplete | None = None, inputs_embeds: Incomplete | None = None, training: bool = False):
        """
        Applies embedding based on inputs tensor.

        Returns:
            final_embeddings (`tf.Tensor`): output embedding tensor.
        """

class TFMultiHeadSelfAttention(tf.keras.layers.Layer):
    n_heads: Incomplete
    dim: Incomplete
    dropout: Incomplete
    output_attentions: Incomplete
    q_lin: Incomplete
    k_lin: Incomplete
    v_lin: Incomplete
    out_lin: Incomplete
    pruned_heads: Incomplete
    def __init__(self, config, **kwargs) -> None: ...
    def prune_heads(self, heads) -> None: ...
    def call(self, query, key, value, mask, head_mask, output_attentions, training: bool = False):
        """
        Parameters:
            query: tf.Tensor(bs, seq_length, dim)
            key: tf.Tensor(bs, seq_length, dim)
            value: tf.Tensor(bs, seq_length, dim)
            mask: tf.Tensor(bs, seq_length)

        Returns:
            weights: tf.Tensor(bs, n_heads, seq_length, seq_length) Attention weights context: tf.Tensor(bs,
            seq_length, dim) Contextualized layer. Optional: only if `output_attentions=True`
        """

class TFFFN(tf.keras.layers.Layer):
    dropout: Incomplete
    lin1: Incomplete
    lin2: Incomplete
    activation: Incomplete
    def __init__(self, config, **kwargs) -> None: ...
    def call(self, input, training: bool = False): ...

class TFTransformerBlock(tf.keras.layers.Layer):
    n_heads: Incomplete
    dim: Incomplete
    hidden_dim: Incomplete
    dropout: Incomplete
    activation: Incomplete
    output_attentions: Incomplete
    attention: Incomplete
    sa_layer_norm: Incomplete
    ffn: Incomplete
    output_layer_norm: Incomplete
    def __init__(self, config, **kwargs) -> None: ...
    def call(self, x, attn_mask, head_mask, output_attentions, training: bool = False):
        """
        Parameters:
            x: tf.Tensor(bs, seq_length, dim)
            attn_mask: tf.Tensor(bs, seq_length)

        Outputs: sa_weights: tf.Tensor(bs, n_heads, seq_length, seq_length) The attention weights ffn_output:
        tf.Tensor(bs, seq_length, dim) The output of the transformer block contextualization.
        """

class TFTransformer(tf.keras.layers.Layer):
    n_layers: Incomplete
    output_hidden_states: Incomplete
    output_attentions: Incomplete
    layer: Incomplete
    def __init__(self, config, **kwargs) -> None: ...
    def call(self, x, attn_mask, head_mask, output_attentions, output_hidden_states, return_dict, training: bool = False):
        """
        Parameters:
            x: tf.Tensor(bs, seq_length, dim) Input sequence embedded.
            attn_mask: tf.Tensor(bs, seq_length) Attention mask on the sequence.

        Returns:
            hidden_state: tf.Tensor(bs, seq_length, dim)
                Sequence of hidden states in the last (top) layer
            all_hidden_states: Tuple[tf.Tensor(bs, seq_length, dim)]
                Tuple of length n_layers with the hidden states from each layer.
                Optional: only if output_hidden_states=True
            all_attentions: Tuple[tf.Tensor(bs, n_heads, seq_length, seq_length)]
                Tuple of length n_layers with the attention weights from each layer
                Optional: only if output_attentions=True
        """

class TFDistilBertMainLayer(tf.keras.layers.Layer):
    config_class = DistilBertConfig
    config: Incomplete
    num_hidden_layers: Incomplete
    output_attentions: Incomplete
    output_hidden_states: Incomplete
    return_dict: Incomplete
    embeddings: Incomplete
    transformer: Incomplete
    def __init__(self, config, **kwargs) -> None: ...
    def get_input_embeddings(self): ...
    def set_input_embeddings(self, value) -> None: ...
    def call(self, input_ids: Incomplete | None = None, attention_mask: Incomplete | None = None, head_mask: Incomplete | None = None, inputs_embeds: Incomplete | None = None, output_attentions: Incomplete | None = None, output_hidden_states: Incomplete | None = None, return_dict: Incomplete | None = None, training: bool = False): ...

class TFDistilBertPreTrainedModel(TFPreTrainedModel):
    """
    An abstract class to handle weights initialization and a simple interface for downloading and loading pretrained
    models.
    """
    config_class = DistilBertConfig
    base_model_prefix: str
    def serving(self, inputs): ...

DISTILBERT_START_DOCSTRING: str
DISTILBERT_INPUTS_DOCSTRING: str

class TFDistilBertModel(TFDistilBertPreTrainedModel):
    distilbert: Incomplete
    def __init__(self, config, *inputs, **kwargs) -> None: ...
    def call(self, input_ids: Optional[TFModelInputType] = None, attention_mask: Optional[Union[np.ndarray, tf.Tensor]] = None, head_mask: Optional[Union[np.ndarray, tf.Tensor]] = None, inputs_embeds: Optional[Union[np.ndarray, tf.Tensor]] = None, output_attentions: Optional[bool] = None, output_hidden_states: Optional[bool] = None, return_dict: Optional[bool] = None, training: Optional[bool] = False) -> Union[TFBaseModelOutput, Tuple[tf.Tensor]]: ...
    def serving_output(self, output): ...

class TFDistilBertLMHead(tf.keras.layers.Layer):
    config: Incomplete
    dim: Incomplete
    input_embeddings: Incomplete
    def __init__(self, config, input_embeddings, **kwargs) -> None: ...
    bias: Incomplete
    def build(self, input_shape) -> None: ...
    def get_output_embeddings(self): ...
    def set_output_embeddings(self, value) -> None: ...
    def get_bias(self): ...
    def set_bias(self, value) -> None: ...
    def call(self, hidden_states): ...

class TFDistilBertForMaskedLM(TFDistilBertPreTrainedModel, TFMaskedLanguageModelingLoss):
    config: Incomplete
    distilbert: Incomplete
    vocab_transform: Incomplete
    act: Incomplete
    vocab_layer_norm: Incomplete
    vocab_projector: Incomplete
    def __init__(self, config, *inputs, **kwargs) -> None: ...
    def get_lm_head(self): ...
    def get_prefix_bias_name(self): ...
    def call(self, input_ids: Optional[TFModelInputType] = None, attention_mask: Optional[Union[np.ndarray, tf.Tensor]] = None, head_mask: Optional[Union[np.ndarray, tf.Tensor]] = None, inputs_embeds: Optional[Union[np.ndarray, tf.Tensor]] = None, output_attentions: Optional[bool] = None, output_hidden_states: Optional[bool] = None, return_dict: Optional[bool] = None, labels: Optional[Union[np.ndarray, tf.Tensor]] = None, training: Optional[bool] = False) -> Union[TFMaskedLMOutput, Tuple[tf.Tensor]]:
        """
        labels (`tf.Tensor` of shape `(batch_size, sequence_length)`, *optional*):
            Labels for computing the masked language modeling loss. Indices should be in `[-100, 0, ...,
            config.vocab_size]` (see `input_ids` docstring) Tokens with indices set to `-100` are ignored (masked), the
            loss is only computed for the tokens with labels in `[0, ..., config.vocab_size]`
        """
    def serving_output(self, output: TFMaskedLMOutput) -> TFMaskedLMOutput: ...

class TFDistilBertForSequenceClassification(TFDistilBertPreTrainedModel, TFSequenceClassificationLoss):
    num_labels: Incomplete
    distilbert: Incomplete
    pre_classifier: Incomplete
    classifier: Incomplete
    dropout: Incomplete
    def __init__(self, config, *inputs, **kwargs) -> None: ...
    def call(self, input_ids: Optional[TFModelInputType] = None, attention_mask: Optional[Union[np.ndarray, tf.Tensor]] = None, head_mask: Optional[Union[np.ndarray, tf.Tensor]] = None, inputs_embeds: Optional[Union[np.ndarray, tf.Tensor]] = None, output_attentions: Optional[bool] = None, output_hidden_states: Optional[bool] = None, return_dict: Optional[bool] = None, labels: Optional[Union[np.ndarray, tf.Tensor]] = None, training: Optional[bool] = False) -> Union[TFSequenceClassifierOutput, Tuple[tf.Tensor]]:
        """
        labels (`tf.Tensor` of shape `(batch_size,)`, *optional*):
            Labels for computing the sequence classification/regression loss. Indices should be in `[0, ...,
            config.num_labels - 1]`. If `config.num_labels == 1` a regression loss is computed (Mean-Square loss), If
            `config.num_labels > 1` a classification loss is computed (Cross-Entropy).
        """
    def serving_output(self, output: TFSequenceClassifierOutput) -> TFSequenceClassifierOutput: ...

class TFDistilBertForTokenClassification(TFDistilBertPreTrainedModel, TFTokenClassificationLoss):
    num_labels: Incomplete
    distilbert: Incomplete
    dropout: Incomplete
    classifier: Incomplete
    def __init__(self, config, *inputs, **kwargs) -> None: ...
    def call(self, input_ids: Optional[TFModelInputType] = None, attention_mask: Optional[Union[np.ndarray, tf.Tensor]] = None, head_mask: Optional[Union[np.ndarray, tf.Tensor]] = None, inputs_embeds: Optional[Union[np.ndarray, tf.Tensor]] = None, output_attentions: Optional[bool] = None, output_hidden_states: Optional[bool] = None, return_dict: Optional[bool] = None, labels: Optional[Union[np.ndarray, tf.Tensor]] = None, training: Optional[bool] = False) -> Union[TFTokenClassifierOutput, Tuple[tf.Tensor]]:
        """
        labels (`tf.Tensor` of shape `(batch_size, sequence_length)`, *optional*):
            Labels for computing the token classification loss. Indices should be in `[0, ..., config.num_labels - 1]`.
        """
    def serving_output(self, output: TFTokenClassifierOutput) -> TFTokenClassifierOutput: ...

class TFDistilBertForMultipleChoice(TFDistilBertPreTrainedModel, TFMultipleChoiceLoss):
    distilbert: Incomplete
    dropout: Incomplete
    pre_classifier: Incomplete
    classifier: Incomplete
    def __init__(self, config, *inputs, **kwargs) -> None: ...
    @property
    def dummy_inputs(self):
        """
        Dummy inputs to build the network.

        Returns:
            tf.Tensor with dummy inputs
        """
    def call(self, input_ids: Optional[TFModelInputType] = None, attention_mask: Optional[Union[np.ndarray, tf.Tensor]] = None, head_mask: Optional[Union[np.ndarray, tf.Tensor]] = None, inputs_embeds: Optional[Union[np.ndarray, tf.Tensor]] = None, output_attentions: Optional[bool] = None, output_hidden_states: Optional[bool] = None, return_dict: Optional[bool] = None, labels: Optional[Union[np.ndarray, tf.Tensor]] = None, training: Optional[bool] = False) -> Union[TFMultipleChoiceModelOutput, Tuple[tf.Tensor]]:
        """
        labels (`tf.Tensor` of shape `(batch_size,)`, *optional*):
            Labels for computing the multiple choice classification loss. Indices should be in `[0, ..., num_choices]`
            where `num_choices` is the size of the second dimension of the input tensors. (See `input_ids` above)
        """
    def serving(self, inputs): ...
    def serving_output(self, output: TFMultipleChoiceModelOutput) -> TFMultipleChoiceModelOutput: ...

class TFDistilBertForQuestionAnswering(TFDistilBertPreTrainedModel, TFQuestionAnsweringLoss):
    distilbert: Incomplete
    qa_outputs: Incomplete
    dropout: Incomplete
    def __init__(self, config, *inputs, **kwargs) -> None: ...
    def call(self, input_ids: Optional[TFModelInputType] = None, attention_mask: Optional[Union[np.ndarray, tf.Tensor]] = None, head_mask: Optional[Union[np.ndarray, tf.Tensor]] = None, inputs_embeds: Optional[Union[np.ndarray, tf.Tensor]] = None, output_attentions: Optional[bool] = None, output_hidden_states: Optional[bool] = None, return_dict: Optional[bool] = None, start_positions: Optional[Union[np.ndarray, tf.Tensor]] = None, end_positions: Optional[Union[np.ndarray, tf.Tensor]] = None, training: Optional[bool] = False) -> Union[TFQuestionAnsweringModelOutput, Tuple[tf.Tensor]]:
        """
        start_positions (`tf.Tensor` of shape `(batch_size,)`, *optional*):
            Labels for position (index) of the start of the labelled span for computing the token classification loss.
            Positions are clamped to the length of the sequence (`sequence_length`). Position outside of the sequence
            are not taken into account for computing the loss.
        end_positions (`tf.Tensor` of shape `(batch_size,)`, *optional*):
            Labels for position (index) of the end of the labelled span for computing the token classification loss.
            Positions are clamped to the length of the sequence (`sequence_length`). Position outside of the sequence
            are not taken into account for computing the loss.
        """
    def serving_output(self, output: TFQuestionAnsweringModelOutput) -> TFQuestionAnsweringModelOutput: ...
