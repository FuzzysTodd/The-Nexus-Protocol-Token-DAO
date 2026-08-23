import numpy as np
import tensorflow as tf
from ...activations_tf import get_tf_activation as get_tf_activation
from ...modeling_tf_outputs import TFBaseModelOutputWithPastAndCrossAttentions as TFBaseModelOutputWithPastAndCrossAttentions, TFBaseModelOutputWithPoolingAndCrossAttentions as TFBaseModelOutputWithPoolingAndCrossAttentions, TFCausalLMOutputWithCrossAttentions as TFCausalLMOutputWithCrossAttentions, TFMaskedLMOutput as TFMaskedLMOutput, TFMultipleChoiceModelOutput as TFMultipleChoiceModelOutput, TFNextSentencePredictorOutput as TFNextSentencePredictorOutput, TFQuestionAnsweringModelOutput as TFQuestionAnsweringModelOutput, TFSequenceClassifierOutput as TFSequenceClassifierOutput, TFTokenClassifierOutput as TFTokenClassifierOutput
from ...modeling_tf_utils import TFCausalLanguageModelingLoss as TFCausalLanguageModelingLoss, TFMaskedLanguageModelingLoss as TFMaskedLanguageModelingLoss, TFModelInputType as TFModelInputType, TFMultipleChoiceLoss as TFMultipleChoiceLoss, TFNextSentencePredictionLoss as TFNextSentencePredictionLoss, TFPreTrainedModel as TFPreTrainedModel, TFQuestionAnsweringLoss as TFQuestionAnsweringLoss, TFSequenceClassificationLoss as TFSequenceClassificationLoss, TFTokenClassificationLoss as TFTokenClassificationLoss, get_initializer as get_initializer, keras_serializable as keras_serializable, unpack_inputs as unpack_inputs
from ...tf_utils import shape_list as shape_list, stable_softmax as stable_softmax
from ...utils import DUMMY_INPUTS as DUMMY_INPUTS, MULTIPLE_CHOICE_DUMMY_INPUTS as MULTIPLE_CHOICE_DUMMY_INPUTS, ModelOutput as ModelOutput, add_code_sample_docstrings as add_code_sample_docstrings, add_start_docstrings as add_start_docstrings, add_start_docstrings_to_model_forward as add_start_docstrings_to_model_forward, logging as logging, replace_return_docstrings as replace_return_docstrings
from .configuration_bert import BertConfig as BertConfig
from _typeshed import Incomplete
from dataclasses import dataclass
from typing import Dict, Optional, Tuple, Union

logger: Incomplete
TF_BERT_PRETRAINED_MODEL_ARCHIVE_LIST: Incomplete

class TFBertPreTrainingLoss:
    """
    Loss function suitable for BERT-like pretraining, that is, the task of pretraining a language model by combining
    NSP + MLM. .. note:: Any label of -100 will be ignored (along with the corresponding logits) in the loss
    computation.
    """
    def hf_compute_loss(self, labels: tf.Tensor, logits: tf.Tensor) -> tf.Tensor: ...

class TFBertEmbeddings(tf.keras.layers.Layer):
    """Construct the embeddings from word, position and token_type embeddings."""
    config: Incomplete
    hidden_size: Incomplete
    max_position_embeddings: Incomplete
    initializer_range: Incomplete
    LayerNorm: Incomplete
    dropout: Incomplete
    def __init__(self, config: BertConfig, **kwargs) -> None: ...
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

class TFBertSelfAttention(tf.keras.layers.Layer):
    num_attention_heads: Incomplete
    attention_head_size: Incomplete
    all_head_size: Incomplete
    sqrt_att_head_size: Incomplete
    query: Incomplete
    key: Incomplete
    value: Incomplete
    dropout: Incomplete
    is_decoder: Incomplete
    def __init__(self, config: BertConfig, **kwargs) -> None: ...
    def transpose_for_scores(self, tensor: tf.Tensor, batch_size: int) -> tf.Tensor: ...
    def call(self, hidden_states: tf.Tensor, attention_mask: tf.Tensor, head_mask: tf.Tensor, encoder_hidden_states: tf.Tensor, encoder_attention_mask: tf.Tensor, past_key_value: Tuple[tf.Tensor], output_attentions: bool, training: bool = False) -> Tuple[tf.Tensor]: ...

class TFBertSelfOutput(tf.keras.layers.Layer):
    dense: Incomplete
    LayerNorm: Incomplete
    dropout: Incomplete
    def __init__(self, config: BertConfig, **kwargs) -> None: ...
    def call(self, hidden_states: tf.Tensor, input_tensor: tf.Tensor, training: bool = False) -> tf.Tensor: ...

class TFBertAttention(tf.keras.layers.Layer):
    self_attention: Incomplete
    dense_output: Incomplete
    def __init__(self, config: BertConfig, **kwargs) -> None: ...
    def prune_heads(self, heads) -> None: ...
    def call(self, input_tensor: tf.Tensor, attention_mask: tf.Tensor, head_mask: tf.Tensor, encoder_hidden_states: tf.Tensor, encoder_attention_mask: tf.Tensor, past_key_value: Tuple[tf.Tensor], output_attentions: bool, training: bool = False) -> Tuple[tf.Tensor]: ...

class TFBertIntermediate(tf.keras.layers.Layer):
    dense: Incomplete
    intermediate_act_fn: Incomplete
    def __init__(self, config: BertConfig, **kwargs) -> None: ...
    def call(self, hidden_states: tf.Tensor) -> tf.Tensor: ...

class TFBertOutput(tf.keras.layers.Layer):
    dense: Incomplete
    LayerNorm: Incomplete
    dropout: Incomplete
    def __init__(self, config: BertConfig, **kwargs) -> None: ...
    def call(self, hidden_states: tf.Tensor, input_tensor: tf.Tensor, training: bool = False) -> tf.Tensor: ...

class TFBertLayer(tf.keras.layers.Layer):
    attention: Incomplete
    is_decoder: Incomplete
    add_cross_attention: Incomplete
    crossattention: Incomplete
    intermediate: Incomplete
    bert_output: Incomplete
    def __init__(self, config: BertConfig, **kwargs) -> None: ...
    def call(self, hidden_states: tf.Tensor, attention_mask: tf.Tensor, head_mask: tf.Tensor, encoder_hidden_states: Optional[tf.Tensor], encoder_attention_mask: Optional[tf.Tensor], past_key_value: Optional[Tuple[tf.Tensor]], output_attentions: bool, training: bool = False) -> Tuple[tf.Tensor]: ...

class TFBertEncoder(tf.keras.layers.Layer):
    config: Incomplete
    layer: Incomplete
    def __init__(self, config: BertConfig, **kwargs) -> None: ...
    def call(self, hidden_states: tf.Tensor, attention_mask: tf.Tensor, head_mask: tf.Tensor, encoder_hidden_states: Optional[tf.Tensor], encoder_attention_mask: Optional[tf.Tensor], past_key_values: Optional[Tuple[Tuple[tf.Tensor]]], use_cache: Optional[bool], output_attentions: bool, output_hidden_states: bool, return_dict: bool, training: bool = False) -> Union[TFBaseModelOutputWithPastAndCrossAttentions, Tuple[tf.Tensor]]: ...

class TFBertPooler(tf.keras.layers.Layer):
    dense: Incomplete
    def __init__(self, config: BertConfig, **kwargs) -> None: ...
    def call(self, hidden_states: tf.Tensor) -> tf.Tensor: ...

class TFBertPredictionHeadTransform(tf.keras.layers.Layer):
    dense: Incomplete
    transform_act_fn: Incomplete
    LayerNorm: Incomplete
    def __init__(self, config: BertConfig, **kwargs) -> None: ...
    def call(self, hidden_states: tf.Tensor) -> tf.Tensor: ...

class TFBertLMPredictionHead(tf.keras.layers.Layer):
    config: Incomplete
    hidden_size: Incomplete
    transform: Incomplete
    input_embeddings: Incomplete
    def __init__(self, config: BertConfig, input_embeddings: tf.keras.layers.Layer, **kwargs) -> None: ...
    bias: Incomplete
    def build(self, input_shape: tf.TensorShape): ...
    def get_output_embeddings(self) -> tf.keras.layers.Layer: ...
    def set_output_embeddings(self, value: tf.Variable): ...
    def get_bias(self) -> Dict[str, tf.Variable]: ...
    def set_bias(self, value: tf.Variable): ...
    def call(self, hidden_states: tf.Tensor) -> tf.Tensor: ...

class TFBertMLMHead(tf.keras.layers.Layer):
    predictions: Incomplete
    def __init__(self, config: BertConfig, input_embeddings: tf.keras.layers.Layer, **kwargs) -> None: ...
    def call(self, sequence_output: tf.Tensor) -> tf.Tensor: ...

class TFBertNSPHead(tf.keras.layers.Layer):
    seq_relationship: Incomplete
    def __init__(self, config: BertConfig, **kwargs) -> None: ...
    def call(self, pooled_output: tf.Tensor) -> tf.Tensor: ...

class TFBertMainLayer(tf.keras.layers.Layer):
    config_class = BertConfig
    config: Incomplete
    is_decoder: Incomplete
    embeddings: Incomplete
    encoder: Incomplete
    pooler: Incomplete
    def __init__(self, config: BertConfig, add_pooling_layer: bool = True, **kwargs) -> None: ...
    def get_input_embeddings(self) -> tf.keras.layers.Layer: ...
    def set_input_embeddings(self, value: tf.Variable): ...
    def call(self, input_ids: Optional[TFModelInputType] = None, attention_mask: Optional[Union[np.ndarray, tf.Tensor]] = None, token_type_ids: Optional[Union[np.ndarray, tf.Tensor]] = None, position_ids: Optional[Union[np.ndarray, tf.Tensor]] = None, head_mask: Optional[Union[np.ndarray, tf.Tensor]] = None, inputs_embeds: Optional[Union[np.ndarray, tf.Tensor]] = None, encoder_hidden_states: Optional[Union[np.ndarray, tf.Tensor]] = None, encoder_attention_mask: Optional[Union[np.ndarray, tf.Tensor]] = None, past_key_values: Optional[Tuple[Tuple[Union[np.ndarray, tf.Tensor]]]] = None, use_cache: Optional[bool] = None, output_attentions: Optional[bool] = None, output_hidden_states: Optional[bool] = None, return_dict: Optional[bool] = None, training: bool = False) -> Union[TFBaseModelOutputWithPoolingAndCrossAttentions, Tuple[tf.Tensor]]: ...

class TFBertPreTrainedModel(TFPreTrainedModel):
    """
    An abstract class to handle weights initialization and a simple interface for downloading and loading pretrained
    models.
    """
    config_class = BertConfig
    base_model_prefix: str
    @property
    def dummy_inputs(self):
        """
        Dummy inputs to build the network.

        Returns:
            `Dict[str, tf.Tensor]`: The dummy inputs.
        """

@dataclass
class TFBertForPreTrainingOutput(ModelOutput):
    """
    Output type of [`TFBertForPreTraining`].

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
    hidden_states: Optional[Union[Tuple[tf.Tensor], tf.Tensor]] = ...
    attentions: Optional[Union[Tuple[tf.Tensor], tf.Tensor]] = ...
    def __init__(self, loss, prediction_logits, seq_relationship_logits, hidden_states, attentions) -> None: ...

BERT_START_DOCSTRING: str
BERT_INPUTS_DOCSTRING: str

class TFBertModel(TFBertPreTrainedModel):
    bert: Incomplete
    def __init__(self, config: BertConfig, *inputs, **kwargs) -> None: ...
    def call(self, input_ids: Optional[TFModelInputType] = None, attention_mask: Optional[Union[np.ndarray, tf.Tensor]] = None, token_type_ids: Optional[Union[np.ndarray, tf.Tensor]] = None, position_ids: Optional[Union[np.ndarray, tf.Tensor]] = None, head_mask: Optional[Union[np.ndarray, tf.Tensor]] = None, inputs_embeds: Optional[Union[np.ndarray, tf.Tensor]] = None, encoder_hidden_states: Optional[Union[np.ndarray, tf.Tensor]] = None, encoder_attention_mask: Optional[Union[np.ndarray, tf.Tensor]] = None, past_key_values: Optional[Tuple[Tuple[Union[np.ndarray, tf.Tensor]]]] = None, use_cache: Optional[bool] = None, output_attentions: Optional[bool] = None, output_hidden_states: Optional[bool] = None, return_dict: Optional[bool] = None, training: Optional[bool] = False) -> Union[TFBaseModelOutputWithPoolingAndCrossAttentions, Tuple[tf.Tensor]]:
        """
        encoder_hidden_states  (`tf.Tensor` of shape `(batch_size, sequence_length, hidden_size)`, *optional*):
            Sequence of hidden-states at the output of the last layer of the encoder. Used in the cross-attention if
            the model is configured as a decoder.
        encoder_attention_mask (`tf.Tensor` of shape `(batch_size, sequence_length)`, *optional*):
            Mask to avoid performing attention on the padding token indices of the encoder input. This mask is used in
            the cross-attention if the model is configured as a decoder. Mask values selected in `[0, 1]`:

            - 1 for tokens that are **not masked**,
            - 0 for tokens that are **masked**.

        past_key_values (`Tuple[Tuple[tf.Tensor]]` of length `config.n_layers`)
            contains precomputed key and value hidden states of the attention blocks. Can be used to speed up decoding.
            If `past_key_values` are used, the user can optionally input only the last `decoder_input_ids` (those that
            don't have their past key value states given to this model) of shape `(batch_size, 1)` instead of all
            `decoder_input_ids` of shape `(batch_size, sequence_length)`.
        use_cache (`bool`, *optional*, defaults to `True`):
            If set to `True`, `past_key_values` key value states are returned and can be used to speed up decoding (see
            `past_key_values`). Set to `False` during training, `True` during generation
        """
    def serving_output(self, output: TFBaseModelOutputWithPoolingAndCrossAttentions) -> TFBaseModelOutputWithPoolingAndCrossAttentions: ...

class TFBertForPreTraining(TFBertPreTrainedModel, TFBertPreTrainingLoss):
    bert: Incomplete
    nsp: Incomplete
    mlm: Incomplete
    def __init__(self, config: BertConfig, *inputs, **kwargs) -> None: ...
    def get_lm_head(self) -> tf.keras.layers.Layer: ...
    def get_prefix_bias_name(self) -> str: ...
    def call(self, input_ids: Optional[TFModelInputType] = None, attention_mask: Optional[Union[np.ndarray, tf.Tensor]] = None, token_type_ids: Optional[Union[np.ndarray, tf.Tensor]] = None, position_ids: Optional[Union[np.ndarray, tf.Tensor]] = None, head_mask: Optional[Union[np.ndarray, tf.Tensor]] = None, inputs_embeds: Optional[Union[np.ndarray, tf.Tensor]] = None, output_attentions: Optional[bool] = None, output_hidden_states: Optional[bool] = None, return_dict: Optional[bool] = None, labels: Optional[Union[np.ndarray, tf.Tensor]] = None, next_sentence_label: Optional[Union[np.ndarray, tf.Tensor]] = None, training: Optional[bool] = False) -> Union[TFBertForPreTrainingOutput, Tuple[tf.Tensor]]:
        '''
        labels (`tf.Tensor` of shape `(batch_size, sequence_length)`, *optional*):
            Labels for computing the masked language modeling loss. Indices should be in `[-100, 0, ...,
            config.vocab_size]` (see `input_ids` docstring) Tokens with indices set to `-100` are ignored (masked), the
            loss is only computed for the tokens with labels in `[0, ..., config.vocab_size]`
        next_sentence_label (`tf.Tensor` of shape `(batch_size,)`, *optional*):
            Labels for computing the next sequence prediction (classification) loss. Input should be a sequence pair
            (see `input_ids` docstring) Indices should be in `[0, 1]`:

            - 0 indicates sequence B is a continuation of sequence A,
            - 1 indicates sequence B is a random sequence.
        kwargs (`Dict[str, any]`, optional, defaults to *{}*):
            Used to hide legacy arguments that have been deprecated.

        Return:

        Examples:

        ```python
        >>> import tensorflow as tf
        >>> from transformers import AutoTokenizer, TFBertForPreTraining

        >>> tokenizer = AutoTokenizer.from_pretrained("bert-base-uncased")
        >>> model = TFBertForPreTraining.from_pretrained("bert-base-uncased")
        >>> input_ids = tokenizer("Hello, my dog is cute", add_special_tokens=True, return_tensors="tf")
        >>> # Batch size 1

        >>> outputs = model(input_ids)
        >>> prediction_logits, seq_relationship_logits = outputs[:2]
        ```'''
    def serving_output(self, output: TFBertForPreTrainingOutput) -> TFBertForPreTrainingOutput: ...

class TFBertForMaskedLM(TFBertPreTrainedModel, TFMaskedLanguageModelingLoss):
    bert: Incomplete
    mlm: Incomplete
    def __init__(self, config: BertConfig, *inputs, **kwargs) -> None: ...
    def get_lm_head(self) -> tf.keras.layers.Layer: ...
    def get_prefix_bias_name(self) -> str: ...
    def call(self, input_ids: Optional[TFModelInputType] = None, attention_mask: Optional[Union[np.ndarray, tf.Tensor]] = None, token_type_ids: Optional[Union[np.ndarray, tf.Tensor]] = None, position_ids: Optional[Union[np.ndarray, tf.Tensor]] = None, head_mask: Optional[Union[np.ndarray, tf.Tensor]] = None, inputs_embeds: Optional[Union[np.ndarray, tf.Tensor]] = None, output_attentions: Optional[bool] = None, output_hidden_states: Optional[bool] = None, return_dict: Optional[bool] = None, labels: Optional[Union[np.ndarray, tf.Tensor]] = None, training: Optional[bool] = False) -> Union[TFMaskedLMOutput, Tuple[tf.Tensor]]:
        """
        labels (`tf.Tensor` or `np.ndarray` of shape `(batch_size, sequence_length)`, *optional*):
            Labels for computing the masked language modeling loss. Indices should be in `[-100, 0, ...,
            config.vocab_size]` (see `input_ids` docstring) Tokens with indices set to `-100` are ignored (masked), the
            loss is only computed for the tokens with labels in `[0, ..., config.vocab_size]`
        """
    def serving_output(self, output: TFMaskedLMOutput) -> TFMaskedLMOutput: ...

class TFBertLMHeadModel(TFBertPreTrainedModel, TFCausalLanguageModelingLoss):
    bert: Incomplete
    mlm: Incomplete
    def __init__(self, config: BertConfig, *inputs, **kwargs) -> None: ...
    def get_lm_head(self) -> tf.keras.layers.Layer: ...
    def get_prefix_bias_name(self) -> str: ...
    def prepare_inputs_for_generation(self, input_ids, past_key_values: Incomplete | None = None, attention_mask: Incomplete | None = None, **model_kwargs): ...
    def call(self, input_ids: Optional[TFModelInputType] = None, attention_mask: Optional[Union[np.ndarray, tf.Tensor]] = None, token_type_ids: Optional[Union[np.ndarray, tf.Tensor]] = None, position_ids: Optional[Union[np.ndarray, tf.Tensor]] = None, head_mask: Optional[Union[np.ndarray, tf.Tensor]] = None, inputs_embeds: Optional[Union[np.ndarray, tf.Tensor]] = None, encoder_hidden_states: Optional[Union[np.ndarray, tf.Tensor]] = None, encoder_attention_mask: Optional[Union[np.ndarray, tf.Tensor]] = None, past_key_values: Optional[Tuple[Tuple[Union[np.ndarray, tf.Tensor]]]] = None, use_cache: Optional[bool] = None, output_attentions: Optional[bool] = None, output_hidden_states: Optional[bool] = None, return_dict: Optional[bool] = None, labels: Optional[Union[np.ndarray, tf.Tensor]] = None, training: Optional[bool] = False, **kwargs) -> Union[TFCausalLMOutputWithCrossAttentions, Tuple[tf.Tensor]]:
        """
        encoder_hidden_states  (`tf.Tensor` of shape `(batch_size, sequence_length, hidden_size)`, *optional*):
            Sequence of hidden-states at the output of the last layer of the encoder. Used in the cross-attention if
            the model is configured as a decoder.
        encoder_attention_mask (`tf.Tensor` of shape `(batch_size, sequence_length)`, *optional*):
            Mask to avoid performing attention on the padding token indices of the encoder input. This mask is used in
            the cross-attention if the model is configured as a decoder. Mask values selected in `[0, 1]`:

            - 1 for tokens that are **not masked**,
            - 0 for tokens that are **masked**.

        past_key_values (`Tuple[Tuple[tf.Tensor]]` of length `config.n_layers`)
            contains precomputed key and value hidden states of the attention blocks. Can be used to speed up decoding.
            If `past_key_values` are used, the user can optionally input only the last `decoder_input_ids` (those that
            don't have their past key value states given to this model) of shape `(batch_size, 1)` instead of all
            `decoder_input_ids` of shape `(batch_size, sequence_length)`.
        use_cache (`bool`, *optional*, defaults to `True`):
            If set to `True`, `past_key_values` key value states are returned and can be used to speed up decoding (see
            `past_key_values`). Set to `False` during training, `True` during generation
        labels (`tf.Tensor` or `np.ndarray` of shape `(batch_size, sequence_length)`, *optional*):
            Labels for computing the cross entropy classification loss. Indices should be in `[0, ...,
            config.vocab_size - 1]`.
        """
    def serving_output(self, output: TFCausalLMOutputWithCrossAttentions) -> TFCausalLMOutputWithCrossAttentions: ...

class TFBertForNextSentencePrediction(TFBertPreTrainedModel, TFNextSentencePredictionLoss):
    bert: Incomplete
    nsp: Incomplete
    def __init__(self, config: BertConfig, *inputs, **kwargs) -> None: ...
    def call(self, input_ids: Optional[TFModelInputType] = None, attention_mask: Optional[Union[np.ndarray, tf.Tensor]] = None, token_type_ids: Optional[Union[np.ndarray, tf.Tensor]] = None, position_ids: Optional[Union[np.ndarray, tf.Tensor]] = None, head_mask: Optional[Union[np.ndarray, tf.Tensor]] = None, inputs_embeds: Optional[Union[np.ndarray, tf.Tensor]] = None, output_attentions: Optional[bool] = None, output_hidden_states: Optional[bool] = None, return_dict: Optional[bool] = None, next_sentence_label: Optional[Union[np.ndarray, tf.Tensor]] = None, training: Optional[bool] = False) -> Union[TFNextSentencePredictorOutput, Tuple[tf.Tensor]]:
        '''
        Return:

        Examples:

        ```python
        >>> import tensorflow as tf
        >>> from transformers import AutoTokenizer, TFBertForNextSentencePrediction

        >>> tokenizer = AutoTokenizer.from_pretrained("bert-base-uncased")
        >>> model = TFBertForNextSentencePrediction.from_pretrained("bert-base-uncased")

        >>> prompt = "In Italy, pizza served in formal settings, such as at a restaurant, is presented unsliced."
        >>> next_sentence = "The sky is blue due to the shorter wavelength of blue light."
        >>> encoding = tokenizer(prompt, next_sentence, return_tensors="tf")

        >>> logits = model(encoding["input_ids"], token_type_ids=encoding["token_type_ids"])[0]
        >>> assert logits[0][0] < logits[0][1]  # the next sentence was random
        ```'''
    def serving_output(self, output: TFNextSentencePredictorOutput) -> TFNextSentencePredictorOutput: ...

class TFBertForSequenceClassification(TFBertPreTrainedModel, TFSequenceClassificationLoss):
    num_labels: Incomplete
    bert: Incomplete
    dropout: Incomplete
    classifier: Incomplete
    def __init__(self, config: BertConfig, *inputs, **kwargs) -> None: ...
    def call(self, input_ids: Optional[TFModelInputType] = None, attention_mask: Optional[Union[np.ndarray, tf.Tensor]] = None, token_type_ids: Optional[Union[np.ndarray, tf.Tensor]] = None, position_ids: Optional[Union[np.ndarray, tf.Tensor]] = None, head_mask: Optional[Union[np.ndarray, tf.Tensor]] = None, inputs_embeds: Optional[Union[np.ndarray, tf.Tensor]] = None, output_attentions: Optional[bool] = None, output_hidden_states: Optional[bool] = None, return_dict: Optional[bool] = None, labels: Optional[Union[np.ndarray, tf.Tensor]] = None, training: Optional[bool] = False) -> Union[TFSequenceClassifierOutput, Tuple[tf.Tensor]]:
        """
        labels (`tf.Tensor` or `np.ndarray` of shape `(batch_size,)`, *optional*):
            Labels for computing the sequence classification/regression loss. Indices should be in `[0, ...,
            config.num_labels - 1]`. If `config.num_labels == 1` a regression loss is computed (Mean-Square loss), If
            `config.num_labels > 1` a classification loss is computed (Cross-Entropy).
        """
    def serving_output(self, output: TFSequenceClassifierOutput) -> TFSequenceClassifierOutput: ...

class TFBertForMultipleChoice(TFBertPreTrainedModel, TFMultipleChoiceLoss):
    bert: Incomplete
    dropout: Incomplete
    classifier: Incomplete
    def __init__(self, config: BertConfig, *inputs, **kwargs) -> None: ...
    @property
    def dummy_inputs(self) -> Dict[str, tf.Tensor]:
        """
        Dummy inputs to build the network.

        Returns:
            tf.Tensor with dummy inputs
        """
    def call(self, input_ids: Optional[TFModelInputType] = None, attention_mask: Optional[Union[np.ndarray, tf.Tensor]] = None, token_type_ids: Optional[Union[np.ndarray, tf.Tensor]] = None, position_ids: Optional[Union[np.ndarray, tf.Tensor]] = None, head_mask: Optional[Union[np.ndarray, tf.Tensor]] = None, inputs_embeds: Optional[Union[np.ndarray, tf.Tensor]] = None, output_attentions: Optional[bool] = None, output_hidden_states: Optional[bool] = None, return_dict: Optional[bool] = None, labels: Optional[Union[np.ndarray, tf.Tensor]] = None, training: Optional[bool] = False) -> Union[TFMultipleChoiceModelOutput, Tuple[tf.Tensor]]:
        """
        labels (`tf.Tensor` or `np.ndarray` of shape `(batch_size,)`, *optional*):
            Labels for computing the multiple choice classification loss. Indices should be in `[0, ..., num_choices]`
            where `num_choices` is the size of the second dimension of the input tensors. (See `input_ids` above)
        """
    def serving(self, inputs: Dict[str, tf.Tensor]) -> TFMultipleChoiceModelOutput: ...
    def serving_output(self, output: TFMultipleChoiceModelOutput) -> TFMultipleChoiceModelOutput: ...

class TFBertForTokenClassification(TFBertPreTrainedModel, TFTokenClassificationLoss):
    num_labels: Incomplete
    bert: Incomplete
    dropout: Incomplete
    classifier: Incomplete
    def __init__(self, config: BertConfig, *inputs, **kwargs) -> None: ...
    def call(self, input_ids: Optional[TFModelInputType] = None, attention_mask: Optional[Union[np.ndarray, tf.Tensor]] = None, token_type_ids: Optional[Union[np.ndarray, tf.Tensor]] = None, position_ids: Optional[Union[np.ndarray, tf.Tensor]] = None, head_mask: Optional[Union[np.ndarray, tf.Tensor]] = None, inputs_embeds: Optional[Union[np.ndarray, tf.Tensor]] = None, output_attentions: Optional[bool] = None, output_hidden_states: Optional[bool] = None, return_dict: Optional[bool] = None, labels: Optional[Union[np.ndarray, tf.Tensor]] = None, training: Optional[bool] = False) -> Union[TFTokenClassifierOutput, Tuple[tf.Tensor]]:
        """
        labels (`tf.Tensor` or `np.ndarray` of shape `(batch_size, sequence_length)`, *optional*):
            Labels for computing the token classification loss. Indices should be in `[0, ..., config.num_labels - 1]`.
        """
    def serving_output(self, output: TFTokenClassifierOutput) -> TFTokenClassifierOutput: ...

class TFBertForQuestionAnswering(TFBertPreTrainedModel, TFQuestionAnsweringLoss):
    num_labels: Incomplete
    bert: Incomplete
    qa_outputs: Incomplete
    def __init__(self, config: BertConfig, *inputs, **kwargs) -> None: ...
    def call(self, input_ids: Optional[TFModelInputType] = None, attention_mask: Optional[Union[np.ndarray, tf.Tensor]] = None, token_type_ids: Optional[Union[np.ndarray, tf.Tensor]] = None, position_ids: Optional[Union[np.ndarray, tf.Tensor]] = None, head_mask: Optional[Union[np.ndarray, tf.Tensor]] = None, inputs_embeds: Optional[Union[np.ndarray, tf.Tensor]] = None, output_attentions: Optional[bool] = None, output_hidden_states: Optional[bool] = None, return_dict: Optional[bool] = None, start_positions: Optional[Union[np.ndarray, tf.Tensor]] = None, end_positions: Optional[Union[np.ndarray, tf.Tensor]] = None, training: Optional[bool] = False) -> Union[TFQuestionAnsweringModelOutput, Tuple[tf.Tensor]]:
        """
        start_positions (`tf.Tensor` or `np.ndarray` of shape `(batch_size,)`, *optional*):
            Labels for position (index) of the start of the labelled span for computing the token classification loss.
            Positions are clamped to the length of the sequence (`sequence_length`). Position outside of the sequence
            are not taken into account for computing the loss.
        end_positions (`tf.Tensor` or `np.ndarray` of shape `(batch_size,)`, *optional*):
            Labels for position (index) of the end of the labelled span for computing the token classification loss.
            Positions are clamped to the length of the sequence (`sequence_length`). Position outside of the sequence
            are not taken into account for computing the loss.
        """
    def serving_output(self, output: TFQuestionAnsweringModelOutput) -> TFQuestionAnsweringModelOutput: ...
