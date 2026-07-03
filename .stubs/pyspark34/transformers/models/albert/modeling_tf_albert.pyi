import numpy as np
import tensorflow as tf
from ...activations_tf import get_tf_activation as get_tf_activation
from ...modeling_tf_outputs import TFBaseModelOutput as TFBaseModelOutput, TFBaseModelOutputWithPooling as TFBaseModelOutputWithPooling, TFMaskedLMOutput as TFMaskedLMOutput, TFMultipleChoiceModelOutput as TFMultipleChoiceModelOutput, TFQuestionAnsweringModelOutput as TFQuestionAnsweringModelOutput, TFSequenceClassifierOutput as TFSequenceClassifierOutput, TFTokenClassifierOutput as TFTokenClassifierOutput
from ...modeling_tf_utils import TFMaskedLanguageModelingLoss as TFMaskedLanguageModelingLoss, TFModelInputType as TFModelInputType, TFMultipleChoiceLoss as TFMultipleChoiceLoss, TFPreTrainedModel as TFPreTrainedModel, TFQuestionAnsweringLoss as TFQuestionAnsweringLoss, TFSequenceClassificationLoss as TFSequenceClassificationLoss, TFTokenClassificationLoss as TFTokenClassificationLoss, get_initializer as get_initializer, keras_serializable as keras_serializable, unpack_inputs as unpack_inputs
from ...tf_utils import shape_list as shape_list, stable_softmax as stable_softmax
from ...utils import MULTIPLE_CHOICE_DUMMY_INPUTS as MULTIPLE_CHOICE_DUMMY_INPUTS, ModelOutput as ModelOutput, add_code_sample_docstrings as add_code_sample_docstrings, add_start_docstrings as add_start_docstrings, add_start_docstrings_to_model_forward as add_start_docstrings_to_model_forward, logging as logging, replace_return_docstrings as replace_return_docstrings
from .configuration_albert import AlbertConfig as AlbertConfig
from _typeshed import Incomplete
from dataclasses import dataclass
from typing import Dict, Optional, Tuple, Union

logger: Incomplete
TF_ALBERT_PRETRAINED_MODEL_ARCHIVE_LIST: Incomplete

class TFAlbertPreTrainingLoss:
    """
    Loss function suitable for ALBERT pretraining, that is, the task of pretraining a language model by combining SOP +
    MLM. .. note:: Any label of -100 will be ignored (along with the corresponding logits) in the loss computation.
    """
    def hf_compute_loss(self, labels: tf.Tensor, logits: tf.Tensor) -> tf.Tensor: ...

class TFAlbertEmbeddings(tf.keras.layers.Layer):
    """Construct the embeddings from word, position and token_type embeddings."""
    config: Incomplete
    embedding_size: Incomplete
    max_position_embeddings: Incomplete
    initializer_range: Incomplete
    LayerNorm: Incomplete
    dropout: Incomplete
    def __init__(self, config: AlbertConfig, **kwargs) -> None: ...
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

class TFAlbertAttention(tf.keras.layers.Layer):
    """Contains the complete attention sublayer, including both dropouts and layer norm."""
    num_attention_heads: Incomplete
    attention_head_size: Incomplete
    all_head_size: Incomplete
    sqrt_att_head_size: Incomplete
    output_attentions: Incomplete
    query: Incomplete
    key: Incomplete
    value: Incomplete
    dense: Incomplete
    LayerNorm: Incomplete
    attention_dropout: Incomplete
    output_dropout: Incomplete
    def __init__(self, config: AlbertConfig, **kwargs) -> None: ...
    def transpose_for_scores(self, tensor: tf.Tensor, batch_size: int) -> tf.Tensor: ...
    def call(self, input_tensor: tf.Tensor, attention_mask: tf.Tensor, head_mask: tf.Tensor, output_attentions: bool, training: bool = False) -> Tuple[tf.Tensor]: ...

class TFAlbertLayer(tf.keras.layers.Layer):
    attention: Incomplete
    ffn: Incomplete
    activation: Incomplete
    ffn_output: Incomplete
    full_layer_layer_norm: Incomplete
    dropout: Incomplete
    def __init__(self, config: AlbertConfig, **kwargs) -> None: ...
    def call(self, hidden_states: tf.Tensor, attention_mask: tf.Tensor, head_mask: tf.Tensor, output_attentions: bool, training: bool = False) -> Tuple[tf.Tensor]: ...

class TFAlbertLayerGroup(tf.keras.layers.Layer):
    albert_layers: Incomplete
    def __init__(self, config: AlbertConfig, **kwargs) -> None: ...
    def call(self, hidden_states: tf.Tensor, attention_mask: tf.Tensor, head_mask: tf.Tensor, output_attentions: bool, output_hidden_states: bool, training: bool = False) -> Union[TFBaseModelOutput, Tuple[tf.Tensor]]: ...

class TFAlbertTransformer(tf.keras.layers.Layer):
    num_hidden_layers: Incomplete
    num_hidden_groups: Incomplete
    layers_per_group: Incomplete
    embedding_hidden_mapping_in: Incomplete
    albert_layer_groups: Incomplete
    def __init__(self, config: AlbertConfig, **kwargs) -> None: ...
    def call(self, hidden_states: tf.Tensor, attention_mask: tf.Tensor, head_mask: tf.Tensor, output_attentions: bool, output_hidden_states: bool, return_dict: bool, training: bool = False) -> Union[TFBaseModelOutput, Tuple[tf.Tensor]]: ...

class TFAlbertPreTrainedModel(TFPreTrainedModel):
    """
    An abstract class to handle weights initialization and a simple interface for downloading and loading pretrained
    models.
    """
    config_class = AlbertConfig
    base_model_prefix: str

class TFAlbertMLMHead(tf.keras.layers.Layer):
    config: Incomplete
    embedding_size: Incomplete
    dense: Incomplete
    activation: Incomplete
    LayerNorm: Incomplete
    decoder: Incomplete
    def __init__(self, config: AlbertConfig, input_embeddings: tf.keras.layers.Layer, **kwargs) -> None: ...
    bias: Incomplete
    decoder_bias: Incomplete
    def build(self, input_shape: tf.TensorShape): ...
    def get_output_embeddings(self) -> tf.keras.layers.Layer: ...
    def set_output_embeddings(self, value: tf.Variable): ...
    def get_bias(self) -> Dict[str, tf.Variable]: ...
    def set_bias(self, value: tf.Variable): ...
    def call(self, hidden_states: tf.Tensor) -> tf.Tensor: ...

class TFAlbertMainLayer(tf.keras.layers.Layer):
    config_class = AlbertConfig
    config: Incomplete
    embeddings: Incomplete
    encoder: Incomplete
    pooler: Incomplete
    def __init__(self, config: AlbertConfig, add_pooling_layer: bool = True, **kwargs) -> None: ...
    def get_input_embeddings(self) -> tf.keras.layers.Layer: ...
    def set_input_embeddings(self, value: tf.Variable): ...
    def call(self, input_ids: Optional[TFModelInputType] = None, attention_mask: Optional[Union[np.ndarray, tf.Tensor]] = None, token_type_ids: Optional[Union[np.ndarray, tf.Tensor]] = None, position_ids: Optional[Union[np.ndarray, tf.Tensor]] = None, head_mask: Optional[Union[np.ndarray, tf.Tensor]] = None, inputs_embeds: Optional[Union[np.ndarray, tf.Tensor]] = None, output_attentions: Optional[bool] = None, output_hidden_states: Optional[bool] = None, return_dict: Optional[bool] = None, training: bool = False) -> Union[TFBaseModelOutputWithPooling, Tuple[tf.Tensor]]: ...

@dataclass
class TFAlbertForPreTrainingOutput(ModelOutput):
    """
    Output type of [`TFAlbertForPreTraining`].

    Args:
        prediction_logits (`tf.Tensor` of shape `(batch_size, sequence_length, config.vocab_size)`):
            Prediction scores of the language modeling head (scores for each vocabulary token before SoftMax).
        sop_logits (`tf.Tensor` of shape `(batch_size, 2)`):
            Prediction scores of the next sequence prediction (classification) head (scores of True/False continuation
            before SoftMax).
        hidden_states (`tuple(tf.Tensor)`, *optional*, returned when `output_hidden_states=True` is passed or when `config.output_hidden_states=True`):
            Tuple of `tf.Tensor` (one for the output of the embeddings + one for the output of each layer) of shape
            `(batch_size, sequence_length, hidden_size)`.

            Hidden-states of the model at the output of each layer plus the initial embedding outputs.
        attentions (`tuple(tf.Tensor)`, *optional*, returned when `output_attentions=True` is passed or when `config.output_attentions=True`):
            Tuple of `tf.Tensor` (one for each layer) of shape `(batch_size, num_heads, sequence_length,
            sequence_length)`.

            Attentions weights after the attention softmax, used to compute the weighted average in the self-attention
            heads.
    """
    loss: tf.Tensor = ...
    prediction_logits: tf.Tensor = ...
    sop_logits: tf.Tensor = ...
    hidden_states: Optional[Tuple[tf.Tensor]] = ...
    attentions: Optional[Tuple[tf.Tensor]] = ...
    def __init__(self, loss, prediction_logits, sop_logits, hidden_states, attentions) -> None: ...

ALBERT_START_DOCSTRING: str
ALBERT_INPUTS_DOCSTRING: str

class TFAlbertModel(TFAlbertPreTrainedModel):
    albert: Incomplete
    def __init__(self, config: AlbertConfig, *inputs, **kwargs) -> None: ...
    def call(self, input_ids: Optional[TFModelInputType] = None, attention_mask: Optional[Union[np.ndarray, tf.Tensor]] = None, token_type_ids: Optional[Union[np.ndarray, tf.Tensor]] = None, position_ids: Optional[Union[np.ndarray, tf.Tensor]] = None, head_mask: Optional[Union[np.ndarray, tf.Tensor]] = None, inputs_embeds: Optional[Union[np.ndarray, tf.Tensor]] = None, output_attentions: Optional[bool] = None, output_hidden_states: Optional[bool] = None, return_dict: Optional[bool] = None, training: Optional[bool] = False) -> Union[TFBaseModelOutputWithPooling, Tuple[tf.Tensor]]: ...
    def serving_output(self, output: TFBaseModelOutputWithPooling) -> TFBaseModelOutputWithPooling: ...

class TFAlbertForPreTraining(TFAlbertPreTrainedModel, TFAlbertPreTrainingLoss):
    num_labels: Incomplete
    albert: Incomplete
    predictions: Incomplete
    sop_classifier: Incomplete
    def __init__(self, config: AlbertConfig, *inputs, **kwargs) -> None: ...
    def get_lm_head(self) -> tf.keras.layers.Layer: ...
    def call(self, input_ids: Optional[TFModelInputType] = None, attention_mask: Optional[Union[np.ndarray, tf.Tensor]] = None, token_type_ids: Optional[Union[np.ndarray, tf.Tensor]] = None, position_ids: Optional[Union[np.ndarray, tf.Tensor]] = None, head_mask: Optional[Union[np.ndarray, tf.Tensor]] = None, inputs_embeds: Optional[Union[np.ndarray, tf.Tensor]] = None, output_attentions: Optional[bool] = None, output_hidden_states: Optional[bool] = None, return_dict: Optional[bool] = None, labels: Optional[Union[np.ndarray, tf.Tensor]] = None, sentence_order_label: Optional[Union[np.ndarray, tf.Tensor]] = None, training: Optional[bool] = False) -> Union[TFAlbertForPreTrainingOutput, Tuple[tf.Tensor]]:
        '''
        Return:

        Example:

        ```python
        >>> import tensorflow as tf
        >>> from transformers import AutoTokenizer, TFAlbertForPreTraining

        >>> tokenizer = AutoTokenizer.from_pretrained("albert-base-v2")
        >>> model = TFAlbertForPreTraining.from_pretrained("albert-base-v2")

        >>> input_ids = tf.constant(tokenizer.encode("Hello, my dog is cute", add_special_tokens=True))[None, :]
        >>> # Batch size 1
        >>> outputs = model(input_ids)

        >>> prediction_logits = outputs.prediction_logits
        >>> sop_logits = outputs.sop_logits
        ```'''
    def serving_output(self, output: TFAlbertForPreTrainingOutput) -> TFAlbertForPreTrainingOutput: ...

class TFAlbertSOPHead(tf.keras.layers.Layer):
    dropout: Incomplete
    classifier: Incomplete
    def __init__(self, config: AlbertConfig, **kwargs) -> None: ...
    def call(self, pooled_output: tf.Tensor, training: bool) -> tf.Tensor: ...

class TFAlbertForMaskedLM(TFAlbertPreTrainedModel, TFMaskedLanguageModelingLoss):
    albert: Incomplete
    predictions: Incomplete
    def __init__(self, config: AlbertConfig, *inputs, **kwargs) -> None: ...
    def get_lm_head(self) -> tf.keras.layers.Layer: ...
    def call(self, input_ids: Optional[TFModelInputType] = None, attention_mask: Optional[Union[np.ndarray, tf.Tensor]] = None, token_type_ids: Optional[Union[np.ndarray, tf.Tensor]] = None, position_ids: Optional[Union[np.ndarray, tf.Tensor]] = None, head_mask: Optional[Union[np.ndarray, tf.Tensor]] = None, inputs_embeds: Optional[Union[np.ndarray, tf.Tensor]] = None, output_attentions: Optional[bool] = None, output_hidden_states: Optional[bool] = None, return_dict: Optional[bool] = None, labels: Optional[Union[np.ndarray, tf.Tensor]] = None, training: Optional[bool] = False) -> Union[TFMaskedLMOutput, Tuple[tf.Tensor]]:
        '''
        labels (`tf.Tensor` of shape `(batch_size, sequence_length)`, *optional*):
            Labels for computing the masked language modeling loss. Indices should be in `[-100, 0, ...,
            config.vocab_size]` (see `input_ids` docstring) Tokens with indices set to `-100` are ignored (masked), the
            loss is only computed for the tokens with labels in `[0, ..., config.vocab_size]`

        Returns:

        Example:

        ```python
        >>> import tensorflow as tf
        >>> from transformers import AutoTokenizer, TFAlbertForMaskedLM

        >>> tokenizer = AutoTokenizer.from_pretrained("albert-base-v2")
        >>> model = TFAlbertForMaskedLM.from_pretrained("albert-base-v2")

        >>> # add mask_token
        >>> inputs = tokenizer(f"The capital of [MASK] is Paris.", return_tensors="tf")
        >>> logits = model(**inputs).logits

        >>> # retrieve index of [MASK]
        >>> mask_token_index = tf.where(inputs.input_ids == tokenizer.mask_token_id)[0][1]
        >>> predicted_token_id = tf.math.argmax(logits[0, mask_token_index], axis=-1)
        >>> tokenizer.decode(predicted_token_id)
        \'france\'
        ```

        ```python
        >>> labels = tokenizer("The capital of France is Paris.", return_tensors="tf")["input_ids"]
        >>> labels = tf.where(inputs.input_ids == tokenizer.mask_token_id, labels, -100)
        >>> outputs = model(**inputs, labels=labels)
        >>> round(float(outputs.loss), 2)
        0.81
        ```
        '''
    def serving_output(self, output: TFMaskedLMOutput) -> TFMaskedLMOutput: ...

class TFAlbertForSequenceClassification(TFAlbertPreTrainedModel, TFSequenceClassificationLoss):
    num_labels: Incomplete
    albert: Incomplete
    dropout: Incomplete
    classifier: Incomplete
    def __init__(self, config: AlbertConfig, *inputs, **kwargs) -> None: ...
    def call(self, input_ids: Optional[TFModelInputType] = None, attention_mask: Optional[Union[np.ndarray, tf.Tensor]] = None, token_type_ids: Optional[Union[np.ndarray, tf.Tensor]] = None, position_ids: Optional[Union[np.ndarray, tf.Tensor]] = None, head_mask: Optional[Union[np.ndarray, tf.Tensor]] = None, inputs_embeds: Optional[Union[np.ndarray, tf.Tensor]] = None, output_attentions: Optional[bool] = None, output_hidden_states: Optional[bool] = None, return_dict: Optional[bool] = None, labels: Optional[Union[np.ndarray, tf.Tensor]] = None, training: Optional[bool] = False) -> Union[TFSequenceClassifierOutput, Tuple[tf.Tensor]]:
        """
        labels (`tf.Tensor` of shape `(batch_size,)`, *optional*):
            Labels for computing the sequence classification/regression loss. Indices should be in `[0, ...,
            config.num_labels - 1]`. If `config.num_labels == 1` a regression loss is computed (Mean-Square loss), If
            `config.num_labels > 1` a classification loss is computed (Cross-Entropy).
        """
    def serving_output(self, output: TFSequenceClassifierOutput) -> TFSequenceClassifierOutput: ...

class TFAlbertForTokenClassification(TFAlbertPreTrainedModel, TFTokenClassificationLoss):
    num_labels: Incomplete
    albert: Incomplete
    dropout: Incomplete
    classifier: Incomplete
    def __init__(self, config: AlbertConfig, *inputs, **kwargs) -> None: ...
    def call(self, input_ids: Optional[TFModelInputType] = None, attention_mask: Optional[Union[np.ndarray, tf.Tensor]] = None, token_type_ids: Optional[Union[np.ndarray, tf.Tensor]] = None, position_ids: Optional[Union[np.ndarray, tf.Tensor]] = None, head_mask: Optional[Union[np.ndarray, tf.Tensor]] = None, inputs_embeds: Optional[Union[np.ndarray, tf.Tensor]] = None, output_attentions: Optional[bool] = None, output_hidden_states: Optional[bool] = None, return_dict: Optional[bool] = None, labels: Optional[Union[np.ndarray, tf.Tensor]] = None, training: Optional[bool] = False) -> Union[TFTokenClassifierOutput, Tuple[tf.Tensor]]:
        """
        labels (`tf.Tensor` of shape `(batch_size, sequence_length)`, *optional*):
            Labels for computing the token classification loss. Indices should be in `[0, ..., config.num_labels - 1]`.
        """
    def serving_output(self, output: TFTokenClassifierOutput) -> TFTokenClassifierOutput: ...

class TFAlbertForQuestionAnswering(TFAlbertPreTrainedModel, TFQuestionAnsweringLoss):
    num_labels: Incomplete
    albert: Incomplete
    qa_outputs: Incomplete
    def __init__(self, config: AlbertConfig, *inputs, **kwargs) -> None: ...
    def call(self, input_ids: Optional[TFModelInputType] = None, attention_mask: Optional[Union[np.ndarray, tf.Tensor]] = None, token_type_ids: Optional[Union[np.ndarray, tf.Tensor]] = None, position_ids: Optional[Union[np.ndarray, tf.Tensor]] = None, head_mask: Optional[Union[np.ndarray, tf.Tensor]] = None, inputs_embeds: Optional[Union[np.ndarray, tf.Tensor]] = None, output_attentions: Optional[bool] = None, output_hidden_states: Optional[bool] = None, return_dict: Optional[bool] = None, start_positions: Optional[Union[np.ndarray, tf.Tensor]] = None, end_positions: Optional[Union[np.ndarray, tf.Tensor]] = None, training: Optional[bool] = False) -> Union[TFQuestionAnsweringModelOutput, Tuple[tf.Tensor]]:
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

class TFAlbertForMultipleChoice(TFAlbertPreTrainedModel, TFMultipleChoiceLoss):
    albert: Incomplete
    dropout: Incomplete
    classifier: Incomplete
    def __init__(self, config: AlbertConfig, *inputs, **kwargs) -> None: ...
    @property
    def dummy_inputs(self):
        """
        Dummy inputs to build the network.

        Returns:
            tf.Tensor with dummy inputs
        """
    def call(self, input_ids: Optional[TFModelInputType] = None, attention_mask: Optional[Union[np.ndarray, tf.Tensor]] = None, token_type_ids: Optional[Union[np.ndarray, tf.Tensor]] = None, position_ids: Optional[Union[np.ndarray, tf.Tensor]] = None, head_mask: Optional[Union[np.ndarray, tf.Tensor]] = None, inputs_embeds: Optional[Union[np.ndarray, tf.Tensor]] = None, output_attentions: Optional[bool] = None, output_hidden_states: Optional[bool] = None, return_dict: Optional[bool] = None, labels: Optional[Union[np.ndarray, tf.Tensor]] = None, training: Optional[bool] = False) -> Union[TFMultipleChoiceModelOutput, Tuple[tf.Tensor]]:
        """
        labels (`tf.Tensor` of shape `(batch_size,)`, *optional*):
            Labels for computing the multiple choice classification loss. Indices should be in `[0, ..., num_choices]`
            where `num_choices` is the size of the second dimension of the input tensors. (See `input_ids` above)
        """
    def serving(self, inputs: Dict[str, tf.Tensor]) -> TFMultipleChoiceModelOutput: ...
    def serving_output(self, output: TFMultipleChoiceModelOutput) -> TFMultipleChoiceModelOutput: ...
