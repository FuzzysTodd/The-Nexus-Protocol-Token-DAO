import numpy as np
import tensorflow as tf
from ...activations_tf import get_tf_activation as get_tf_activation
from ...modeling_tf_outputs import TFBaseModelOutput as TFBaseModelOutput, TFBaseModelOutputWithPooling as TFBaseModelOutputWithPooling, TFMaskedLMOutput as TFMaskedLMOutput, TFMultipleChoiceModelOutput as TFMultipleChoiceModelOutput, TFQuestionAnsweringModelOutput as TFQuestionAnsweringModelOutput, TFSequenceClassifierOutput as TFSequenceClassifierOutput, TFTokenClassifierOutput as TFTokenClassifierOutput
from ...modeling_tf_utils import TFMaskedLanguageModelingLoss as TFMaskedLanguageModelingLoss, TFModelInputType as TFModelInputType, TFMultipleChoiceLoss as TFMultipleChoiceLoss, TFPreTrainedModel as TFPreTrainedModel, TFQuestionAnsweringLoss as TFQuestionAnsweringLoss, TFSequenceClassificationLoss as TFSequenceClassificationLoss, TFTokenClassificationLoss as TFTokenClassificationLoss, get_initializer as get_initializer, keras_serializable as keras_serializable, unpack_inputs as unpack_inputs
from ...tf_utils import shape_list as shape_list, stable_softmax as stable_softmax
from ...utils import MULTIPLE_CHOICE_DUMMY_INPUTS as MULTIPLE_CHOICE_DUMMY_INPUTS, add_code_sample_docstrings as add_code_sample_docstrings, add_start_docstrings as add_start_docstrings, add_start_docstrings_to_model_forward as add_start_docstrings_to_model_forward, logging as logging
from .configuration_mpnet import MPNetConfig as MPNetConfig
from _typeshed import Incomplete
from typing import Optional, Tuple, Union

logger: Incomplete
TF_MPNET_PRETRAINED_MODEL_ARCHIVE_LIST: Incomplete

class TFMPNetPreTrainedModel(TFPreTrainedModel):
    """
    An abstract class to handle weights initialization and a simple interface for downloading and loading pretrained
    models.
    """
    config_class = MPNetConfig
    base_model_prefix: str
    def serving(self, inputs): ...

class TFMPNetEmbeddings(tf.keras.layers.Layer):
    """Construct the embeddings from word, position embeddings."""
    padding_idx: int
    config: Incomplete
    hidden_size: Incomplete
    max_position_embeddings: Incomplete
    initializer_range: Incomplete
    LayerNorm: Incomplete
    dropout: Incomplete
    def __init__(self, config, **kwargs) -> None: ...
    weight: Incomplete
    position_embeddings: Incomplete
    def build(self, input_shape: tf.TensorShape): ...
    def create_position_ids_from_input_ids(self, input_ids):
        """
        Replace non-padding symbols with their position numbers. Position numbers begin at padding_idx+1. Padding
        symbols are ignored. This is modified from fairseq's `utils.make_positions`.

        Args:
            input_ids: tf.Tensor
        Returns: tf.Tensor
        """
    def call(self, input_ids: Incomplete | None = None, position_ids: Incomplete | None = None, inputs_embeds: Incomplete | None = None, training: bool = False):
        """
        Applies embedding based on inputs tensor.

        Returns:
            final_embeddings (`tf.Tensor`): output embedding tensor.
        """

class TFMPNetPooler(tf.keras.layers.Layer):
    dense: Incomplete
    def __init__(self, config: MPNetConfig, **kwargs) -> None: ...
    def call(self, hidden_states: tf.Tensor) -> tf.Tensor: ...

class TFMPNetSelfAttention(tf.keras.layers.Layer):
    num_attention_heads: Incomplete
    attention_head_size: Incomplete
    all_head_size: Incomplete
    q: Incomplete
    k: Incomplete
    v: Incomplete
    o: Incomplete
    dropout: Incomplete
    def __init__(self, config, **kwargs) -> None: ...
    def transpose_for_scores(self, x, batch_size): ...
    def call(self, hidden_states, attention_mask, head_mask, output_attentions, position_bias: Incomplete | None = None, training: bool = False): ...

class TFMPNetAttention(tf.keras.layers.Layer):
    attn: Incomplete
    LayerNorm: Incomplete
    dropout: Incomplete
    def __init__(self, config, **kwargs) -> None: ...
    def prune_heads(self, heads) -> None: ...
    def call(self, input_tensor, attention_mask, head_mask, output_attentions, position_bias: Incomplete | None = None, training: bool = False): ...

class TFMPNetIntermediate(tf.keras.layers.Layer):
    dense: Incomplete
    intermediate_act_fn: Incomplete
    def __init__(self, config: MPNetConfig, **kwargs) -> None: ...
    def call(self, hidden_states: tf.Tensor) -> tf.Tensor: ...

class TFMPNetOutput(tf.keras.layers.Layer):
    dense: Incomplete
    LayerNorm: Incomplete
    dropout: Incomplete
    def __init__(self, config: MPNetConfig, **kwargs) -> None: ...
    def call(self, hidden_states: tf.Tensor, input_tensor: tf.Tensor, training: bool = False) -> tf.Tensor: ...

class TFMPNetLayer(tf.keras.layers.Layer):
    attention: Incomplete
    intermediate: Incomplete
    out: Incomplete
    def __init__(self, config, **kwargs) -> None: ...
    def call(self, hidden_states, attention_mask, head_mask, output_attentions, position_bias: Incomplete | None = None, training: bool = False): ...

class TFMPNetEncoder(tf.keras.layers.Layer):
    config: Incomplete
    n_heads: Incomplete
    output_attentions: Incomplete
    output_hidden_states: Incomplete
    relative_attention_num_buckets: Incomplete
    initializer_range: Incomplete
    layer: Incomplete
    def __init__(self, config, **kwargs) -> None: ...
    relative_attention_bias: Incomplete
    def build(self, input_shape): ...
    def call(self, hidden_states, attention_mask, head_mask, output_attentions, output_hidden_states, return_dict, training: bool = False): ...
    def compute_position_bias(self, x, position_ids: Incomplete | None = None):
        """Compute binned relative position bias"""

class TFMPNetMainLayer(tf.keras.layers.Layer):
    config_class = MPNetConfig
    config: Incomplete
    num_hidden_layers: Incomplete
    initializer_range: Incomplete
    output_attentions: Incomplete
    output_hidden_states: Incomplete
    return_dict: Incomplete
    encoder: Incomplete
    pooler: Incomplete
    embeddings: Incomplete
    def __init__(self, config, **kwargs) -> None: ...
    def get_input_embeddings(self) -> tf.keras.layers.Layer: ...
    def set_input_embeddings(self, value: tf.Variable): ...
    def call(self, input_ids: Incomplete | None = None, attention_mask: Incomplete | None = None, position_ids: Incomplete | None = None, head_mask: Incomplete | None = None, inputs_embeds: Incomplete | None = None, output_attentions: Incomplete | None = None, output_hidden_states: Incomplete | None = None, return_dict: Incomplete | None = None, training: bool = False): ...

MPNET_START_DOCSTRING: str
MPNET_INPUTS_DOCSTRING: str

class TFMPNetModel(TFMPNetPreTrainedModel):
    mpnet: Incomplete
    def __init__(self, config, *inputs, **kwargs) -> None: ...
    def call(self, input_ids: Optional[TFModelInputType] = None, attention_mask: Optional[Union[np.array, tf.Tensor]] = None, position_ids: Optional[Union[np.array, tf.Tensor]] = None, head_mask: Optional[Union[np.array, tf.Tensor]] = None, inputs_embeds: Optional[tf.Tensor] = None, output_attentions: Optional[bool] = None, output_hidden_states: Optional[bool] = None, return_dict: Optional[bool] = None, training: bool = False) -> Union[TFBaseModelOutput, Tuple[tf.Tensor]]: ...
    def serving_output(self, output: TFBaseModelOutputWithPooling) -> TFBaseModelOutputWithPooling: ...

class TFMPNetLMHead(tf.keras.layers.Layer):
    """MPNet head for masked and permuted language modeling"""
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

class TFMPNetForMaskedLM(TFMPNetPreTrainedModel, TFMaskedLanguageModelingLoss):
    mpnet: Incomplete
    lm_head: Incomplete
    def __init__(self, config, *inputs, **kwargs) -> None: ...
    def get_lm_head(self): ...
    def get_prefix_bias_name(self): ...
    def call(self, input_ids: Optional[TFModelInputType] = None, attention_mask: Optional[Union[np.ndarray, tf.Tensor]] = None, position_ids: Optional[Union[np.ndarray, tf.Tensor]] = None, head_mask: Optional[Union[np.ndarray, tf.Tensor]] = None, inputs_embeds: Optional[tf.Tensor] = None, output_attentions: Optional[bool] = None, output_hidden_states: Optional[bool] = None, return_dict: Optional[bool] = None, labels: Optional[tf.Tensor] = None, training: bool = False) -> Union[TFMaskedLMOutput, Tuple[tf.Tensor]]:
        """
        labels (`tf.Tensor` of shape `(batch_size, sequence_length)`, *optional*):
            Labels for computing the masked language modeling loss. Indices should be in `[-100, 0, ...,
            config.vocab_size]` (see `input_ids` docstring) Tokens with indices set to `-100` are ignored (masked), the
            loss is only computed for the tokens with labels in `[0, ..., config.vocab_size]`
        """
    def serving_output(self, output: TFMaskedLMOutput) -> TFMaskedLMOutput: ...

class TFMPNetClassificationHead(tf.keras.layers.Layer):
    """Head for sentence-level classification tasks."""
    dense: Incomplete
    dropout: Incomplete
    out_proj: Incomplete
    def __init__(self, config, **kwargs) -> None: ...
    def call(self, features, training: bool = False): ...

class TFMPNetForSequenceClassification(TFMPNetPreTrainedModel, TFSequenceClassificationLoss):
    num_labels: Incomplete
    mpnet: Incomplete
    classifier: Incomplete
    def __init__(self, config, *inputs, **kwargs) -> None: ...
    def call(self, input_ids: Optional[TFModelInputType] = None, attention_mask: Optional[Union[np.array, tf.Tensor]] = None, position_ids: Optional[Union[np.array, tf.Tensor]] = None, head_mask: Optional[Union[np.array, tf.Tensor]] = None, inputs_embeds: Optional[tf.Tensor] = None, output_attentions: Optional[bool] = None, output_hidden_states: Optional[bool] = None, return_dict: Optional[bool] = None, labels: Optional[tf.Tensor] = None, training: bool = False) -> Union[TFSequenceClassifierOutput, Tuple[tf.Tensor]]:
        """
        labels (`tf.Tensor` of shape `(batch_size,)`, *optional*):
            Labels for computing the sequence classification/regression loss. Indices should be in `[0, ...,
            config.num_labels - 1]`. If `config.num_labels == 1` a regression loss is computed (Mean-Square loss), If
            `config.num_labels > 1` a classification loss is computed (Cross-Entropy).
        """
    def serving_output(self, output: TFSequenceClassifierOutput) -> TFSequenceClassifierOutput: ...

class TFMPNetForMultipleChoice(TFMPNetPreTrainedModel, TFMultipleChoiceLoss):
    mpnet: Incomplete
    dropout: Incomplete
    classifier: Incomplete
    def __init__(self, config, *inputs, **kwargs) -> None: ...
    @property
    def dummy_inputs(self):
        """
        Dummy inputs to build the network.

        Returns:
            tf.Tensor with dummy inputs
        """
    def call(self, input_ids: Optional[TFModelInputType] = None, attention_mask: Optional[Union[np.ndarray, tf.Tensor]] = None, position_ids: Optional[Union[np.ndarray, tf.Tensor]] = None, head_mask: Optional[Union[np.ndarray, tf.Tensor]] = None, inputs_embeds: Optional[tf.Tensor] = None, output_attentions: Optional[bool] = None, output_hidden_states: Optional[bool] = None, return_dict: Optional[bool] = None, labels: Optional[tf.Tensor] = None, training: bool = False) -> Union[TFMultipleChoiceModelOutput, Tuple[tf.Tensor]]:
        """
        labels (`tf.Tensor` of shape `(batch_size,)`, *optional*):
            Labels for computing the multiple choice classification loss. Indices should be in `[0, ..., num_choices]`
            where `num_choices` is the size of the second dimension of the input tensors. (See `input_ids` above)
        """
    def serving(self, inputs): ...
    def serving_output(self, output: TFMultipleChoiceModelOutput) -> TFMultipleChoiceModelOutput: ...

class TFMPNetForTokenClassification(TFMPNetPreTrainedModel, TFTokenClassificationLoss):
    num_labels: Incomplete
    mpnet: Incomplete
    dropout: Incomplete
    classifier: Incomplete
    def __init__(self, config, *inputs, **kwargs) -> None: ...
    def call(self, input_ids: Optional[TFModelInputType] = None, attention_mask: Optional[Union[np.ndarray, tf.Tensor]] = None, position_ids: Optional[Union[np.ndarray, tf.Tensor]] = None, head_mask: Optional[Union[np.ndarray, tf.Tensor]] = None, inputs_embeds: Optional[tf.Tensor] = None, output_attentions: Optional[bool] = None, output_hidden_states: Optional[bool] = None, return_dict: Optional[bool] = None, labels: Optional[tf.Tensor] = None, training: bool = False) -> Union[TFTokenClassifierOutput, Tuple[tf.Tensor]]:
        """
        labels (`tf.Tensor` of shape `(batch_size, sequence_length)`, *optional*):
            Labels for computing the token classification loss. Indices should be in `[0, ..., config.num_labels - 1]`.
        """
    def serving_output(self, output: TFTokenClassifierOutput) -> TFTokenClassifierOutput: ...

class TFMPNetForQuestionAnswering(TFMPNetPreTrainedModel, TFQuestionAnsweringLoss):
    num_labels: Incomplete
    mpnet: Incomplete
    qa_outputs: Incomplete
    def __init__(self, config, *inputs, **kwargs) -> None: ...
    def call(self, input_ids: Optional[TFModelInputType] = None, attention_mask: Optional[Union[np.array, tf.Tensor]] = None, position_ids: Optional[Union[np.array, tf.Tensor]] = None, head_mask: Optional[Union[np.array, tf.Tensor]] = None, inputs_embeds: Optional[tf.Tensor] = None, output_attentions: Optional[bool] = None, output_hidden_states: Optional[bool] = None, return_dict: Optional[bool] = None, start_positions: Optional[tf.Tensor] = None, end_positions: Optional[tf.Tensor] = None, training: bool = False, **kwargs) -> Union[TFQuestionAnsweringModelOutput, Tuple[tf.Tensor]]:
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
