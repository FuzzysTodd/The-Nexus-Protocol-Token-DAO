import numpy as np
import tensorflow as tf
from ...activations_tf import get_tf_activation as get_tf_activation
from ...modeling_tf_outputs import TFBaseModelOutput as TFBaseModelOutput, TFMaskedLMOutput as TFMaskedLMOutput, TFMultipleChoiceModelOutput as TFMultipleChoiceModelOutput, TFQuestionAnsweringModelOutput as TFQuestionAnsweringModelOutput, TFSequenceClassifierOutput as TFSequenceClassifierOutput, TFTokenClassifierOutput as TFTokenClassifierOutput
from ...modeling_tf_utils import TFMaskedLanguageModelingLoss as TFMaskedLanguageModelingLoss, TFModelInputType as TFModelInputType, TFMultipleChoiceLoss as TFMultipleChoiceLoss, TFPreTrainedModel as TFPreTrainedModel, TFQuestionAnsweringLoss as TFQuestionAnsweringLoss, TFSequenceClassificationLoss as TFSequenceClassificationLoss, TFSequenceSummary as TFSequenceSummary, TFTokenClassificationLoss as TFTokenClassificationLoss, get_initializer as get_initializer, keras_serializable as keras_serializable, unpack_inputs as unpack_inputs
from ...tf_utils import shape_list as shape_list, stable_softmax as stable_softmax
from ...utils import MULTIPLE_CHOICE_DUMMY_INPUTS as MULTIPLE_CHOICE_DUMMY_INPUTS, add_code_sample_docstrings as add_code_sample_docstrings, add_start_docstrings as add_start_docstrings, add_start_docstrings_to_model_forward as add_start_docstrings_to_model_forward, logging as logging
from .configuration_convbert import ConvBertConfig as ConvBertConfig
from _typeshed import Incomplete
from typing import Optional, Tuple, Union

logger: Incomplete
TF_CONVBERT_PRETRAINED_MODEL_ARCHIVE_LIST: Incomplete

class TFConvBertEmbeddings(tf.keras.layers.Layer):
    """Construct the embeddings from word, position and token_type embeddings."""
    config: Incomplete
    embedding_size: Incomplete
    max_position_embeddings: Incomplete
    initializer_range: Incomplete
    LayerNorm: Incomplete
    dropout: Incomplete
    def __init__(self, config: ConvBertConfig, **kwargs) -> None: ...
    weight: Incomplete
    token_type_embeddings: Incomplete
    position_embeddings: Incomplete
    def build(self, input_shape: tf.TensorShape): ...
    def call(self, input_ids: tf.Tensor = None, position_ids: tf.Tensor = None, token_type_ids: tf.Tensor = None, inputs_embeds: tf.Tensor = None, past_key_values_length: int = 0, training: bool = False) -> tf.Tensor:
        """
        Applies embedding based on inputs tensor.

        Returns:
            final_embeddings (`tf.Tensor`): output embedding tensor.
        """

class TFConvBertSelfAttention(tf.keras.layers.Layer):
    head_ratio: Incomplete
    num_attention_heads: Incomplete
    conv_kernel_size: Incomplete
    attention_head_size: Incomplete
    all_head_size: Incomplete
    query: Incomplete
    key: Incomplete
    value: Incomplete
    key_conv_attn_layer: Incomplete
    conv_kernel_layer: Incomplete
    conv_out_layer: Incomplete
    dropout: Incomplete
    def __init__(self, config, **kwargs) -> None: ...
    def transpose_for_scores(self, x, batch_size): ...
    def call(self, hidden_states, attention_mask, head_mask, output_attentions, training: bool = False): ...

class TFConvBertSelfOutput(tf.keras.layers.Layer):
    dense: Incomplete
    LayerNorm: Incomplete
    dropout: Incomplete
    def __init__(self, config, **kwargs) -> None: ...
    def call(self, hidden_states, input_tensor, training: bool = False): ...

class TFConvBertAttention(tf.keras.layers.Layer):
    self_attention: Incomplete
    dense_output: Incomplete
    def __init__(self, config, **kwargs) -> None: ...
    def prune_heads(self, heads) -> None: ...
    def call(self, input_tensor, attention_mask, head_mask, output_attentions, training: bool = False): ...

class GroupedLinearLayer(tf.keras.layers.Layer):
    input_size: Incomplete
    output_size: Incomplete
    num_groups: Incomplete
    kernel_initializer: Incomplete
    group_in_dim: Incomplete
    group_out_dim: Incomplete
    def __init__(self, input_size, output_size, num_groups, kernel_initializer, **kwargs) -> None: ...
    kernel: Incomplete
    bias: Incomplete
    def build(self, input_shape) -> None: ...
    def call(self, hidden_states): ...

class TFConvBertIntermediate(tf.keras.layers.Layer):
    dense: Incomplete
    intermediate_act_fn: Incomplete
    def __init__(self, config, **kwargs) -> None: ...
    def call(self, hidden_states): ...

class TFConvBertOutput(tf.keras.layers.Layer):
    dense: Incomplete
    LayerNorm: Incomplete
    dropout: Incomplete
    def __init__(self, config, **kwargs) -> None: ...
    def call(self, hidden_states, input_tensor, training: bool = False): ...

class TFConvBertLayer(tf.keras.layers.Layer):
    attention: Incomplete
    intermediate: Incomplete
    bert_output: Incomplete
    def __init__(self, config, **kwargs) -> None: ...
    def call(self, hidden_states, attention_mask, head_mask, output_attentions, training: bool = False): ...

class TFConvBertEncoder(tf.keras.layers.Layer):
    layer: Incomplete
    def __init__(self, config, **kwargs) -> None: ...
    def call(self, hidden_states, attention_mask, head_mask, output_attentions, output_hidden_states, return_dict, training: bool = False): ...

class TFConvBertPredictionHeadTransform(tf.keras.layers.Layer):
    dense: Incomplete
    transform_act_fn: Incomplete
    LayerNorm: Incomplete
    def __init__(self, config, **kwargs) -> None: ...
    def call(self, hidden_states): ...

class TFConvBertMainLayer(tf.keras.layers.Layer):
    config_class = ConvBertConfig
    embeddings: Incomplete
    embeddings_project: Incomplete
    encoder: Incomplete
    config: Incomplete
    def __init__(self, config, **kwargs) -> None: ...
    def get_input_embeddings(self): ...
    def set_input_embeddings(self, value) -> None: ...
    def get_extended_attention_mask(self, attention_mask, input_shape, dtype): ...
    def get_head_mask(self, head_mask): ...
    def call(self, input_ids: Incomplete | None = None, attention_mask: Incomplete | None = None, token_type_ids: Incomplete | None = None, position_ids: Incomplete | None = None, head_mask: Incomplete | None = None, inputs_embeds: Incomplete | None = None, output_attentions: Incomplete | None = None, output_hidden_states: Incomplete | None = None, return_dict: Incomplete | None = None, training: bool = False): ...

class TFConvBertPreTrainedModel(TFPreTrainedModel):
    """
    An abstract class to handle weights initialization and a simple interface for downloading and loading pretrained
    models.
    """
    config_class = ConvBertConfig
    base_model_prefix: str

CONVBERT_START_DOCSTRING: str
CONVBERT_INPUTS_DOCSTRING: str

class TFConvBertModel(TFConvBertPreTrainedModel):
    convbert: Incomplete
    def __init__(self, config, *inputs, **kwargs) -> None: ...
    def call(self, input_ids: Optional[TFModelInputType] = None, attention_mask: Optional[Union[np.array, tf.Tensor]] = None, token_type_ids: Optional[Union[np.array, tf.Tensor]] = None, position_ids: Optional[Union[np.array, tf.Tensor]] = None, head_mask: Optional[Union[np.array, tf.Tensor]] = None, inputs_embeds: Optional[tf.Tensor] = None, output_attentions: Optional[bool] = None, output_hidden_states: Optional[bool] = None, return_dict: Optional[bool] = None, training: bool = False) -> Union[TFBaseModelOutput, Tuple[tf.Tensor]]: ...
    def serving_output(self, output): ...

class TFConvBertMaskedLMHead(tf.keras.layers.Layer):
    config: Incomplete
    embedding_size: Incomplete
    input_embeddings: Incomplete
    def __init__(self, config, input_embeddings, **kwargs) -> None: ...
    bias: Incomplete
    def build(self, input_shape) -> None: ...
    def get_output_embeddings(self): ...
    def set_output_embeddings(self, value) -> None: ...
    def get_bias(self): ...
    def set_bias(self, value) -> None: ...
    def call(self, hidden_states): ...

class TFConvBertGeneratorPredictions(tf.keras.layers.Layer):
    LayerNorm: Incomplete
    dense: Incomplete
    def __init__(self, config, **kwargs) -> None: ...
    def call(self, generator_hidden_states, training: bool = False): ...

class TFConvBertForMaskedLM(TFConvBertPreTrainedModel, TFMaskedLanguageModelingLoss):
    config: Incomplete
    convbert: Incomplete
    generator_predictions: Incomplete
    activation: Incomplete
    generator_lm_head: Incomplete
    def __init__(self, config, *inputs, **kwargs) -> None: ...
    def get_lm_head(self): ...
    def get_prefix_bias_name(self): ...
    def call(self, input_ids: Optional[TFModelInputType] = None, attention_mask: Optional[Union[np.ndarray, tf.Tensor]] = None, token_type_ids: Optional[Union[np.ndarray, tf.Tensor]] = None, position_ids: Optional[Union[np.ndarray, tf.Tensor]] = None, head_mask: Optional[Union[np.ndarray, tf.Tensor]] = None, inputs_embeds: Optional[tf.Tensor] = None, output_attentions: Optional[bool] = None, output_hidden_states: Optional[bool] = None, return_dict: Optional[bool] = None, labels: Optional[tf.Tensor] = None, training: Optional[bool] = False) -> Union[Tuple, TFMaskedLMOutput]:
        """
        labels (`tf.Tensor` of shape `(batch_size, sequence_length)`, *optional*):
            Labels for computing the masked language modeling loss. Indices should be in `[-100, 0, ...,
            config.vocab_size]` (see `input_ids` docstring) Tokens with indices set to `-100` are ignored (masked), the
            loss is only computed for the tokens with labels in `[0, ..., config.vocab_size]`
        """
    def serving_output(self, output): ...

class TFConvBertClassificationHead(tf.keras.layers.Layer):
    """Head for sentence-level classification tasks."""
    dense: Incomplete
    dropout: Incomplete
    out_proj: Incomplete
    config: Incomplete
    def __init__(self, config, **kwargs) -> None: ...
    def call(self, hidden_states, **kwargs): ...

class TFConvBertForSequenceClassification(TFConvBertPreTrainedModel, TFSequenceClassificationLoss):
    num_labels: Incomplete
    convbert: Incomplete
    classifier: Incomplete
    def __init__(self, config, *inputs, **kwargs) -> None: ...
    def call(self, input_ids: Optional[TFModelInputType] = None, attention_mask: Optional[Union[np.ndarray, tf.Tensor]] = None, token_type_ids: Optional[Union[np.ndarray, tf.Tensor]] = None, position_ids: Optional[Union[np.ndarray, tf.Tensor]] = None, head_mask: Optional[Union[np.ndarray, tf.Tensor]] = None, inputs_embeds: Optional[tf.Tensor] = None, output_attentions: Optional[bool] = None, output_hidden_states: Optional[bool] = None, return_dict: Optional[bool] = None, labels: Optional[tf.Tensor] = None, training: Optional[bool] = False) -> Union[Tuple, TFSequenceClassifierOutput]:
        """
        labels (`tf.Tensor` of shape `(batch_size,)`, *optional*):
            Labels for computing the sequence classification/regression loss. Indices should be in `[0, ...,
            config.num_labels - 1]`. If `config.num_labels == 1` a regression loss is computed (Mean-Square loss), If
            `config.num_labels > 1` a classification loss is computed (Cross-Entropy).
        """
    def serving_output(self, output): ...

class TFConvBertForMultipleChoice(TFConvBertPreTrainedModel, TFMultipleChoiceLoss):
    convbert: Incomplete
    sequence_summary: Incomplete
    classifier: Incomplete
    def __init__(self, config, *inputs, **kwargs) -> None: ...
    @property
    def dummy_inputs(self):
        """
        Dummy inputs to build the network.

        Returns:
            tf.Tensor with dummy inputs
        """
    def call(self, input_ids: Optional[TFModelInputType] = None, attention_mask: Optional[Union[np.ndarray, tf.Tensor]] = None, token_type_ids: Optional[Union[np.ndarray, tf.Tensor]] = None, position_ids: Optional[Union[np.ndarray, tf.Tensor]] = None, head_mask: Optional[Union[np.ndarray, tf.Tensor]] = None, inputs_embeds: Optional[tf.Tensor] = None, output_attentions: Optional[bool] = None, output_hidden_states: Optional[bool] = None, return_dict: Optional[bool] = None, labels: Optional[tf.Tensor] = None, training: Optional[bool] = False) -> Union[Tuple, TFMultipleChoiceModelOutput]:
        """
        labels (`tf.Tensor` of shape `(batch_size,)`, *optional*):
            Labels for computing the multiple choice classification loss. Indices should be in `[0, ..., num_choices]`
            where `num_choices` is the size of the second dimension of the input tensors. (See `input_ids` above)
        """
    def serving(self, inputs): ...
    def serving_output(self, output): ...

class TFConvBertForTokenClassification(TFConvBertPreTrainedModel, TFTokenClassificationLoss):
    num_labels: Incomplete
    convbert: Incomplete
    dropout: Incomplete
    classifier: Incomplete
    def __init__(self, config, *inputs, **kwargs) -> None: ...
    def call(self, input_ids: Optional[TFModelInputType] = None, attention_mask: Optional[Union[np.ndarray, tf.Tensor]] = None, token_type_ids: Optional[Union[np.ndarray, tf.Tensor]] = None, position_ids: Optional[Union[np.ndarray, tf.Tensor]] = None, head_mask: Optional[Union[np.ndarray, tf.Tensor]] = None, inputs_embeds: Optional[tf.Tensor] = None, output_attentions: Optional[bool] = None, output_hidden_states: Optional[bool] = None, return_dict: Optional[bool] = None, labels: Optional[tf.Tensor] = None, training: Optional[bool] = False) -> Union[Tuple, TFTokenClassifierOutput]:
        """
        labels (`tf.Tensor` of shape `(batch_size, sequence_length)`, *optional*):
            Labels for computing the token classification loss. Indices should be in `[0, ..., config.num_labels - 1]`.
        """
    def serving_output(self, output): ...

class TFConvBertForQuestionAnswering(TFConvBertPreTrainedModel, TFQuestionAnsweringLoss):
    num_labels: Incomplete
    convbert: Incomplete
    qa_outputs: Incomplete
    def __init__(self, config, *inputs, **kwargs) -> None: ...
    def call(self, input_ids: Optional[TFModelInputType] = None, attention_mask: Optional[Union[np.ndarray, tf.Tensor]] = None, token_type_ids: Optional[Union[np.ndarray, tf.Tensor]] = None, position_ids: Optional[Union[np.ndarray, tf.Tensor]] = None, head_mask: Optional[Union[np.ndarray, tf.Tensor]] = None, inputs_embeds: Optional[tf.Tensor] = None, output_attentions: Optional[bool] = None, output_hidden_states: Optional[bool] = None, return_dict: Optional[bool] = None, start_positions: Optional[tf.Tensor] = None, end_positions: Optional[tf.Tensor] = None, training: Optional[bool] = False) -> Union[Tuple, TFQuestionAnsweringModelOutput]:
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
    def serving_output(self, output): ...
