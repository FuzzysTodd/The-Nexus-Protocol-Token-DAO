import numpy as np
import tensorflow as tf
from ...activations_tf import get_tf_activation as get_tf_activation
from ...modeling_tf_outputs import TFBaseModelOutput as TFBaseModelOutput, TFBaseModelOutputWithPooling as TFBaseModelOutputWithPooling, TFMaskedLMOutput as TFMaskedLMOutput, TFMultipleChoiceModelOutput as TFMultipleChoiceModelOutput, TFNextSentencePredictorOutput as TFNextSentencePredictorOutput, TFQuestionAnsweringModelOutput as TFQuestionAnsweringModelOutput, TFSequenceClassifierOutput as TFSequenceClassifierOutput, TFTokenClassifierOutput as TFTokenClassifierOutput
from ...modeling_tf_utils import TFMaskedLanguageModelingLoss as TFMaskedLanguageModelingLoss, TFModelInputType as TFModelInputType, TFMultipleChoiceLoss as TFMultipleChoiceLoss, TFNextSentencePredictionLoss as TFNextSentencePredictionLoss, TFPreTrainedModel as TFPreTrainedModel, TFQuestionAnsweringLoss as TFQuestionAnsweringLoss, TFSequenceClassificationLoss as TFSequenceClassificationLoss, TFTokenClassificationLoss as TFTokenClassificationLoss, get_initializer as get_initializer, keras_serializable as keras_serializable, unpack_inputs as unpack_inputs
from ...tf_utils import shape_list as shape_list, stable_softmax as stable_softmax
from ...utils import MULTIPLE_CHOICE_DUMMY_INPUTS as MULTIPLE_CHOICE_DUMMY_INPUTS, ModelOutput as ModelOutput, add_code_sample_docstrings as add_code_sample_docstrings, add_start_docstrings as add_start_docstrings, add_start_docstrings_to_model_forward as add_start_docstrings_to_model_forward, logging as logging, replace_return_docstrings as replace_return_docstrings
from .configuration_mobilebert import MobileBertConfig as MobileBertConfig
from _typeshed import Incomplete
from dataclasses import dataclass
from typing import Dict, Optional, Tuple, Union

logger: Incomplete
TF_MOBILEBERT_PRETRAINED_MODEL_ARCHIVE_LIST: Incomplete

class TFMobileBertPreTrainingLoss:
    """
    Loss function suitable for BERT-like pretraining, that is, the task of pretraining a language model by combining
    NSP + MLM. .. note:: Any label of -100 will be ignored (along with the corresponding logits) in the loss
    computation.
    """
    def hf_compute_loss(self, labels: tf.Tensor, logits: tf.Tensor) -> tf.Tensor: ...

class TFMobileBertIntermediate(tf.keras.layers.Layer):
    dense: Incomplete
    intermediate_act_fn: Incomplete
    def __init__(self, config, **kwargs) -> None: ...
    def call(self, hidden_states): ...

class TFLayerNorm(tf.keras.layers.LayerNormalization):
    def __init__(self, feat_size, *args, **kwargs) -> None: ...

class TFNoNorm(tf.keras.layers.Layer):
    feat_size: Incomplete
    def __init__(self, feat_size, epsilon: Incomplete | None = None, **kwargs) -> None: ...
    bias: Incomplete
    weight: Incomplete
    def build(self, input_shape) -> None: ...
    def call(self, inputs: tf.Tensor): ...

NORM2FN: Incomplete

class TFMobileBertEmbeddings(tf.keras.layers.Layer):
    """Construct the embeddings from word, position and token_type embeddings."""
    trigram_input: Incomplete
    embedding_size: Incomplete
    config: Incomplete
    hidden_size: Incomplete
    max_position_embeddings: Incomplete
    initializer_range: Incomplete
    embedding_transformation: Incomplete
    LayerNorm: Incomplete
    dropout: Incomplete
    def __init__(self, config, **kwargs) -> None: ...
    weight: Incomplete
    token_type_embeddings: Incomplete
    position_embeddings: Incomplete
    def build(self, input_shape) -> None: ...
    def call(self, input_ids: Incomplete | None = None, position_ids: Incomplete | None = None, token_type_ids: Incomplete | None = None, inputs_embeds: Incomplete | None = None, training: bool = False):
        """
        Applies embedding based on inputs tensor.

        Returns:
            final_embeddings (`tf.Tensor`): output embedding tensor.
        """

class TFMobileBertSelfAttention(tf.keras.layers.Layer):
    num_attention_heads: Incomplete
    output_attentions: Incomplete
    attention_head_size: Incomplete
    all_head_size: Incomplete
    query: Incomplete
    key: Incomplete
    value: Incomplete
    dropout: Incomplete
    def __init__(self, config, **kwargs) -> None: ...
    def transpose_for_scores(self, x, batch_size): ...
    def call(self, query_tensor, key_tensor, value_tensor, attention_mask, head_mask, output_attentions, training: bool = False): ...

class TFMobileBertSelfOutput(tf.keras.layers.Layer):
    use_bottleneck: Incomplete
    dense: Incomplete
    LayerNorm: Incomplete
    dropout: Incomplete
    def __init__(self, config, **kwargs) -> None: ...
    def call(self, hidden_states, residual_tensor, training: bool = False): ...

class TFMobileBertAttention(tf.keras.layers.Layer):
    self: Incomplete
    mobilebert_output: Incomplete
    def __init__(self, config, **kwargs) -> None: ...
    def prune_heads(self, heads) -> None: ...
    def call(self, query_tensor, key_tensor, value_tensor, layer_input, attention_mask, head_mask, output_attentions, training: bool = False): ...

class TFOutputBottleneck(tf.keras.layers.Layer):
    dense: Incomplete
    LayerNorm: Incomplete
    dropout: Incomplete
    def __init__(self, config, **kwargs) -> None: ...
    def call(self, hidden_states, residual_tensor, training: bool = False): ...

class TFMobileBertOutput(tf.keras.layers.Layer):
    use_bottleneck: Incomplete
    dense: Incomplete
    LayerNorm: Incomplete
    dropout: Incomplete
    bottleneck: Incomplete
    def __init__(self, config, **kwargs) -> None: ...
    def call(self, hidden_states, residual_tensor_1, residual_tensor_2, training: bool = False): ...

class TFBottleneckLayer(tf.keras.layers.Layer):
    dense: Incomplete
    LayerNorm: Incomplete
    def __init__(self, config, **kwargs) -> None: ...
    def call(self, inputs): ...

class TFBottleneck(tf.keras.layers.Layer):
    key_query_shared_bottleneck: Incomplete
    use_bottleneck_attention: Incomplete
    bottleneck_input: Incomplete
    attention: Incomplete
    def __init__(self, config, **kwargs) -> None: ...
    def call(self, hidden_states): ...

class TFFFNOutput(tf.keras.layers.Layer):
    dense: Incomplete
    LayerNorm: Incomplete
    def __init__(self, config, **kwargs) -> None: ...
    def call(self, hidden_states, residual_tensor): ...

class TFFFNLayer(tf.keras.layers.Layer):
    intermediate: Incomplete
    mobilebert_output: Incomplete
    def __init__(self, config, **kwargs) -> None: ...
    def call(self, hidden_states): ...

class TFMobileBertLayer(tf.keras.layers.Layer):
    use_bottleneck: Incomplete
    num_feedforward_networks: Incomplete
    attention: Incomplete
    intermediate: Incomplete
    mobilebert_output: Incomplete
    bottleneck: Incomplete
    ffn: Incomplete
    def __init__(self, config, **kwargs) -> None: ...
    def call(self, hidden_states, attention_mask, head_mask, output_attentions, training: bool = False): ...

class TFMobileBertEncoder(tf.keras.layers.Layer):
    output_attentions: Incomplete
    output_hidden_states: Incomplete
    layer: Incomplete
    def __init__(self, config, **kwargs) -> None: ...
    def call(self, hidden_states, attention_mask, head_mask, output_attentions, output_hidden_states, return_dict, training: bool = False): ...

class TFMobileBertPooler(tf.keras.layers.Layer):
    do_activate: Incomplete
    dense: Incomplete
    def __init__(self, config, **kwargs) -> None: ...
    def call(self, hidden_states): ...

class TFMobileBertPredictionHeadTransform(tf.keras.layers.Layer):
    dense: Incomplete
    transform_act_fn: Incomplete
    LayerNorm: Incomplete
    def __init__(self, config, **kwargs) -> None: ...
    def call(self, hidden_states): ...

class TFMobileBertLMPredictionHead(tf.keras.layers.Layer):
    transform: Incomplete
    config: Incomplete
    def __init__(self, config, **kwargs) -> None: ...
    bias: Incomplete
    dense: Incomplete
    decoder: Incomplete
    def build(self, input_shape) -> None: ...
    def get_output_embeddings(self): ...
    def set_output_embeddings(self, value) -> None: ...
    def get_bias(self): ...
    def set_bias(self, value) -> None: ...
    def call(self, hidden_states): ...

class TFMobileBertMLMHead(tf.keras.layers.Layer):
    predictions: Incomplete
    def __init__(self, config, **kwargs) -> None: ...
    def call(self, sequence_output): ...

class TFMobileBertMainLayer(tf.keras.layers.Layer):
    config_class = MobileBertConfig
    config: Incomplete
    num_hidden_layers: Incomplete
    output_attentions: Incomplete
    output_hidden_states: Incomplete
    return_dict: Incomplete
    embeddings: Incomplete
    encoder: Incomplete
    pooler: Incomplete
    def __init__(self, config, add_pooling_layer: bool = True, **kwargs) -> None: ...
    def get_input_embeddings(self): ...
    def set_input_embeddings(self, value) -> None: ...
    def call(self, input_ids: Incomplete | None = None, attention_mask: Incomplete | None = None, token_type_ids: Incomplete | None = None, position_ids: Incomplete | None = None, head_mask: Incomplete | None = None, inputs_embeds: Incomplete | None = None, output_attentions: Incomplete | None = None, output_hidden_states: Incomplete | None = None, return_dict: Incomplete | None = None, training: bool = False): ...

class TFMobileBertPreTrainedModel(TFPreTrainedModel):
    """
    An abstract class to handle weights initialization and a simple interface for downloading and loading pretrained
    models.
    """
    config_class = MobileBertConfig
    base_model_prefix: str

@dataclass
class TFMobileBertForPreTrainingOutput(ModelOutput):
    """
    Output type of [`TFMobileBertForPreTraining`].

    Args:
        prediction_logits (`tf.Tensor` of shape `(batch_size, sequence_length, config.vocab_size)`):
            Prediction scores of the language modeling head (scores for each vocabulary token before SoftMax).
        seq_relationship_logits (`tf.Tensor` of shape `(batch_size, 2)`):
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
    loss: Optional[tf.Tensor] = ...
    prediction_logits: tf.Tensor = ...
    seq_relationship_logits: tf.Tensor = ...
    hidden_states: Optional[Tuple[tf.Tensor]] = ...
    attentions: Optional[Tuple[tf.Tensor]] = ...
    def __init__(self, loss, prediction_logits, seq_relationship_logits, hidden_states, attentions) -> None: ...

MOBILEBERT_START_DOCSTRING: str
MOBILEBERT_INPUTS_DOCSTRING: str

class TFMobileBertModel(TFMobileBertPreTrainedModel):
    mobilebert: Incomplete
    def __init__(self, config, *inputs, **kwargs) -> None: ...
    def call(self, input_ids: Optional[TFModelInputType] = None, attention_mask: Optional[Union[np.ndarray, tf.Tensor]] = None, token_type_ids: Optional[Union[np.ndarray, tf.Tensor]] = None, position_ids: Optional[Union[np.ndarray, tf.Tensor]] = None, head_mask: Optional[Union[np.ndarray, tf.Tensor]] = None, inputs_embeds: Optional[Union[np.ndarray, tf.Tensor]] = None, output_attentions: Optional[bool] = None, output_hidden_states: Optional[bool] = None, return_dict: Optional[bool] = None, training: Optional[bool] = False) -> Union[Tuple, TFBaseModelOutputWithPooling]: ...
    def serving_output(self, output: TFBaseModelOutputWithPooling) -> TFBaseModelOutputWithPooling: ...

class TFMobileBertForPreTraining(TFMobileBertPreTrainedModel, TFMobileBertPreTrainingLoss):
    mobilebert: Incomplete
    predictions: Incomplete
    seq_relationship: Incomplete
    def __init__(self, config, *inputs, **kwargs) -> None: ...
    def get_lm_head(self): ...
    def get_prefix_bias_name(self): ...
    def call(self, input_ids: Optional[TFModelInputType] = None, attention_mask: Optional[Union[np.ndarray, tf.Tensor]] = None, token_type_ids: Optional[Union[np.ndarray, tf.Tensor]] = None, position_ids: Optional[Union[np.ndarray, tf.Tensor]] = None, head_mask: Optional[Union[np.ndarray, tf.Tensor]] = None, inputs_embeds: Optional[Union[np.ndarray, tf.Tensor]] = None, output_attentions: Optional[bool] = None, output_hidden_states: Optional[bool] = None, return_dict: Optional[bool] = None, labels: Optional[Union[np.ndarray, tf.Tensor]] = None, next_sentence_label: Optional[Union[np.ndarray, tf.Tensor]] = None, training: Optional[bool] = False) -> Union[Tuple, TFMobileBertForPreTrainingOutput]:
        '''
        Return:

        Examples:

        ```python
        >>> import tensorflow as tf
        >>> from transformers import AutoTokenizer, TFMobileBertForPreTraining

        >>> tokenizer = AutoTokenizer.from_pretrained("google/mobilebert-uncased")
        >>> model = TFMobileBertForPreTraining.from_pretrained("google/mobilebert-uncased")
        >>> input_ids = tf.constant(tokenizer.encode("Hello, my dog is cute"))[None, :]  # Batch size 1
        >>> outputs = model(input_ids)
        >>> prediction_scores, seq_relationship_scores = outputs[:2]
        ```'''
    def serving_output(self, output): ...

class TFMobileBertForMaskedLM(TFMobileBertPreTrainedModel, TFMaskedLanguageModelingLoss):
    mobilebert: Incomplete
    predictions: Incomplete
    def __init__(self, config, *inputs, **kwargs) -> None: ...
    def get_lm_head(self): ...
    def get_prefix_bias_name(self): ...
    def call(self, input_ids: Optional[TFModelInputType] = None, attention_mask: Optional[Union[np.ndarray, tf.Tensor]] = None, token_type_ids: Optional[Union[np.ndarray, tf.Tensor]] = None, position_ids: Optional[Union[np.ndarray, tf.Tensor]] = None, head_mask: Optional[Union[np.ndarray, tf.Tensor]] = None, inputs_embeds: Optional[Union[np.ndarray, tf.Tensor]] = None, output_attentions: Optional[bool] = None, output_hidden_states: Optional[bool] = None, return_dict: Optional[bool] = None, labels: Optional[Union[np.ndarray, tf.Tensor]] = None, training: Optional[bool] = False) -> Union[Tuple, TFMaskedLMOutput]:
        """
        labels (`tf.Tensor` of shape `(batch_size, sequence_length)`, *optional*):
            Labels for computing the masked language modeling loss. Indices should be in `[-100, 0, ...,
            config.vocab_size]` (see `input_ids` docstring) Tokens with indices set to `-100` are ignored (masked), the
            loss is only computed for the tokens with labels
        """
    def serving_output(self, output: TFMaskedLMOutput) -> TFMaskedLMOutput: ...

class TFMobileBertOnlyNSPHead(tf.keras.layers.Layer):
    seq_relationship: Incomplete
    def __init__(self, config, **kwargs) -> None: ...
    def call(self, pooled_output): ...

class TFMobileBertForNextSentencePrediction(TFMobileBertPreTrainedModel, TFNextSentencePredictionLoss):
    mobilebert: Incomplete
    cls: Incomplete
    def __init__(self, config, *inputs, **kwargs) -> None: ...
    def call(self, input_ids: Optional[TFModelInputType] = None, attention_mask: Optional[Union[np.ndarray, tf.Tensor]] = None, token_type_ids: Optional[Union[np.ndarray, tf.Tensor]] = None, position_ids: Optional[Union[np.ndarray, tf.Tensor]] = None, head_mask: Optional[Union[np.ndarray, tf.Tensor]] = None, inputs_embeds: Optional[Union[np.ndarray, tf.Tensor]] = None, output_attentions: Optional[bool] = None, output_hidden_states: Optional[bool] = None, return_dict: Optional[bool] = None, next_sentence_label: Optional[Union[np.ndarray, tf.Tensor]] = None, training: Optional[bool] = False) -> Union[Tuple, TFNextSentencePredictorOutput]:
        '''
        Return:

        Examples:

        ```python
        >>> import tensorflow as tf
        >>> from transformers import AutoTokenizer, TFMobileBertForNextSentencePrediction

        >>> tokenizer = AutoTokenizer.from_pretrained("google/mobilebert-uncased")
        >>> model = TFMobileBertForNextSentencePrediction.from_pretrained("google/mobilebert-uncased")

        >>> prompt = "In Italy, pizza served in formal settings, such as at a restaurant, is presented unsliced."
        >>> next_sentence = "The sky is blue due to the shorter wavelength of blue light."
        >>> encoding = tokenizer(prompt, next_sentence, return_tensors="tf")

        >>> logits = model(encoding["input_ids"], token_type_ids=encoding["token_type_ids"])[0]
        ```'''
    def serving_output(self, output: TFNextSentencePredictorOutput) -> TFNextSentencePredictorOutput: ...

class TFMobileBertForSequenceClassification(TFMobileBertPreTrainedModel, TFSequenceClassificationLoss):
    num_labels: Incomplete
    mobilebert: Incomplete
    dropout: Incomplete
    classifier: Incomplete
    def __init__(self, config, *inputs, **kwargs) -> None: ...
    def call(self, input_ids: Optional[TFModelInputType] = None, attention_mask: Optional[Union[np.ndarray, tf.Tensor]] = None, token_type_ids: Optional[Union[np.ndarray, tf.Tensor]] = None, position_ids: Optional[Union[np.ndarray, tf.Tensor]] = None, head_mask: Optional[Union[np.ndarray, tf.Tensor]] = None, inputs_embeds: Optional[Union[np.ndarray, tf.Tensor]] = None, output_attentions: Optional[bool] = None, output_hidden_states: Optional[bool] = None, return_dict: Optional[bool] = None, labels: Optional[Union[np.ndarray, tf.Tensor]] = None, training: Optional[bool] = False) -> Union[Tuple, TFSequenceClassifierOutput]:
        """
        labels (`tf.Tensor` of shape `(batch_size,)`, *optional*):
            Labels for computing the sequence classification/regression loss. Indices should be in `[0, ...,
            config.num_labels - 1]`. If `config.num_labels == 1` a regression loss is computed (Mean-Square loss), If
            `config.num_labels > 1` a classification loss is computed (Cross-Entropy).
        """
    def serving_output(self, output: TFSequenceClassifierOutput) -> TFSequenceClassifierOutput: ...

class TFMobileBertForQuestionAnswering(TFMobileBertPreTrainedModel, TFQuestionAnsweringLoss):
    num_labels: Incomplete
    mobilebert: Incomplete
    qa_outputs: Incomplete
    def __init__(self, config, *inputs, **kwargs) -> None: ...
    def call(self, input_ids: Optional[TFModelInputType] = None, attention_mask: Optional[Union[np.ndarray, tf.Tensor]] = None, token_type_ids: Optional[Union[np.ndarray, tf.Tensor]] = None, position_ids: Optional[Union[np.ndarray, tf.Tensor]] = None, head_mask: Optional[Union[np.ndarray, tf.Tensor]] = None, inputs_embeds: Optional[Union[np.ndarray, tf.Tensor]] = None, output_attentions: Optional[bool] = None, output_hidden_states: Optional[bool] = None, return_dict: Optional[bool] = None, start_positions: Optional[Union[np.ndarray, tf.Tensor]] = None, end_positions: Optional[Union[np.ndarray, tf.Tensor]] = None, training: Optional[bool] = False) -> Union[Tuple, TFQuestionAnsweringModelOutput]:
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

class TFMobileBertForMultipleChoice(TFMobileBertPreTrainedModel, TFMultipleChoiceLoss):
    mobilebert: Incomplete
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
    def call(self, input_ids: Optional[TFModelInputType] = None, attention_mask: Optional[Union[np.ndarray, tf.Tensor]] = None, token_type_ids: Optional[Union[np.ndarray, tf.Tensor]] = None, position_ids: Optional[Union[np.ndarray, tf.Tensor]] = None, head_mask: Optional[Union[np.ndarray, tf.Tensor]] = None, inputs_embeds: Optional[Union[np.ndarray, tf.Tensor]] = None, output_attentions: Optional[bool] = None, output_hidden_states: Optional[bool] = None, return_dict: Optional[bool] = None, labels: Optional[Union[np.ndarray, tf.Tensor]] = None, training: Optional[bool] = False) -> Union[Tuple, TFMultipleChoiceModelOutput]:
        """
        labels (`tf.Tensor` of shape `(batch_size,)`, *optional*):
            Labels for computing the multiple choice classification loss. Indices should be in `[0, ..., num_choices]`
            where `num_choices` is the size of the second dimension of the input tensors. (See `input_ids` above)
        """
    def serving(self, inputs: Dict[str, tf.Tensor]): ...
    def serving_output(self, output: TFMultipleChoiceModelOutput) -> TFMultipleChoiceModelOutput: ...

class TFMobileBertForTokenClassification(TFMobileBertPreTrainedModel, TFTokenClassificationLoss):
    num_labels: Incomplete
    mobilebert: Incomplete
    dropout: Incomplete
    classifier: Incomplete
    def __init__(self, config, *inputs, **kwargs) -> None: ...
    def call(self, input_ids: Optional[TFModelInputType] = None, attention_mask: Optional[Union[np.ndarray, tf.Tensor]] = None, token_type_ids: Optional[Union[np.ndarray, tf.Tensor]] = None, position_ids: Optional[Union[np.ndarray, tf.Tensor]] = None, head_mask: Optional[Union[np.ndarray, tf.Tensor]] = None, inputs_embeds: Optional[Union[np.ndarray, tf.Tensor]] = None, output_attentions: Optional[bool] = None, output_hidden_states: Optional[bool] = None, return_dict: Optional[bool] = None, labels: Optional[Union[np.ndarray, tf.Tensor]] = None, training: Optional[bool] = False) -> Union[Tuple, TFTokenClassifierOutput]:
        """
        labels (`tf.Tensor` of shape `(batch_size, sequence_length)`, *optional*):
            Labels for computing the token classification loss. Indices should be in `[0, ..., config.num_labels - 1]`.
        """
    def serving_output(self, output: TFTokenClassifierOutput) -> TFTokenClassifierOutput: ...
