import numpy as np
import tensorflow as tf
from ...activations_tf import get_tf_activation as get_tf_activation
from ...modeling_tf_outputs import TFBaseModelOutputWithPastAndCrossAttentions as TFBaseModelOutputWithPastAndCrossAttentions, TFMaskedLMOutput as TFMaskedLMOutput, TFMultipleChoiceModelOutput as TFMultipleChoiceModelOutput, TFQuestionAnsweringModelOutput as TFQuestionAnsweringModelOutput, TFSequenceClassifierOutput as TFSequenceClassifierOutput, TFTokenClassifierOutput as TFTokenClassifierOutput
from ...modeling_tf_utils import TFMaskedLanguageModelingLoss as TFMaskedLanguageModelingLoss, TFModelInputType as TFModelInputType, TFMultipleChoiceLoss as TFMultipleChoiceLoss, TFPreTrainedModel as TFPreTrainedModel, TFQuestionAnsweringLoss as TFQuestionAnsweringLoss, TFSequenceClassificationLoss as TFSequenceClassificationLoss, TFSequenceSummary as TFSequenceSummary, TFTokenClassificationLoss as TFTokenClassificationLoss, get_initializer as get_initializer, keras_serializable as keras_serializable, unpack_inputs as unpack_inputs
from ...tf_utils import shape_list as shape_list, stable_softmax as stable_softmax
from ...utils import DUMMY_INPUTS as DUMMY_INPUTS, MULTIPLE_CHOICE_DUMMY_INPUTS as MULTIPLE_CHOICE_DUMMY_INPUTS, ModelOutput as ModelOutput, add_code_sample_docstrings as add_code_sample_docstrings, add_start_docstrings as add_start_docstrings, add_start_docstrings_to_model_forward as add_start_docstrings_to_model_forward, logging as logging, replace_return_docstrings as replace_return_docstrings
from .configuration_electra import ElectraConfig as ElectraConfig
from _typeshed import Incomplete
from dataclasses import dataclass
from typing import Dict, Optional, Tuple, Union

logger: Incomplete
TF_ELECTRA_PRETRAINED_MODEL_ARCHIVE_LIST: Incomplete

class TFElectraSelfAttention(tf.keras.layers.Layer):
    num_attention_heads: Incomplete
    attention_head_size: Incomplete
    all_head_size: Incomplete
    sqrt_att_head_size: Incomplete
    query: Incomplete
    key: Incomplete
    value: Incomplete
    dropout: Incomplete
    is_decoder: Incomplete
    def __init__(self, config: ElectraConfig, **kwargs) -> None: ...
    def transpose_for_scores(self, tensor: tf.Tensor, batch_size: int) -> tf.Tensor: ...
    def call(self, hidden_states: tf.Tensor, attention_mask: tf.Tensor, head_mask: tf.Tensor, encoder_hidden_states: tf.Tensor, encoder_attention_mask: tf.Tensor, past_key_value: Tuple[tf.Tensor], output_attentions: bool, training: bool = False) -> Tuple[tf.Tensor]: ...

class TFElectraSelfOutput(tf.keras.layers.Layer):
    dense: Incomplete
    LayerNorm: Incomplete
    dropout: Incomplete
    def __init__(self, config: ElectraConfig, **kwargs) -> None: ...
    def call(self, hidden_states: tf.Tensor, input_tensor: tf.Tensor, training: bool = False) -> tf.Tensor: ...

class TFElectraAttention(tf.keras.layers.Layer):
    self_attention: Incomplete
    dense_output: Incomplete
    def __init__(self, config: ElectraConfig, **kwargs) -> None: ...
    def prune_heads(self, heads) -> None: ...
    def call(self, input_tensor: tf.Tensor, attention_mask: tf.Tensor, head_mask: tf.Tensor, encoder_hidden_states: tf.Tensor, encoder_attention_mask: tf.Tensor, past_key_value: Tuple[tf.Tensor], output_attentions: bool, training: bool = False) -> Tuple[tf.Tensor]: ...

class TFElectraIntermediate(tf.keras.layers.Layer):
    dense: Incomplete
    intermediate_act_fn: Incomplete
    def __init__(self, config: ElectraConfig, **kwargs) -> None: ...
    def call(self, hidden_states: tf.Tensor) -> tf.Tensor: ...

class TFElectraOutput(tf.keras.layers.Layer):
    dense: Incomplete
    LayerNorm: Incomplete
    dropout: Incomplete
    def __init__(self, config: ElectraConfig, **kwargs) -> None: ...
    def call(self, hidden_states: tf.Tensor, input_tensor: tf.Tensor, training: bool = False) -> tf.Tensor: ...

class TFElectraLayer(tf.keras.layers.Layer):
    attention: Incomplete
    is_decoder: Incomplete
    add_cross_attention: Incomplete
    crossattention: Incomplete
    intermediate: Incomplete
    bert_output: Incomplete
    def __init__(self, config: ElectraConfig, **kwargs) -> None: ...
    def call(self, hidden_states: tf.Tensor, attention_mask: tf.Tensor, head_mask: tf.Tensor, encoder_hidden_states: Optional[tf.Tensor], encoder_attention_mask: Optional[tf.Tensor], past_key_value: Optional[Tuple[tf.Tensor]], output_attentions: bool, training: bool = False) -> Tuple[tf.Tensor]: ...

class TFElectraEncoder(tf.keras.layers.Layer):
    config: Incomplete
    layer: Incomplete
    def __init__(self, config: ElectraConfig, **kwargs) -> None: ...
    def call(self, hidden_states: tf.Tensor, attention_mask: tf.Tensor, head_mask: tf.Tensor, encoder_hidden_states: Optional[tf.Tensor], encoder_attention_mask: Optional[tf.Tensor], past_key_values: Optional[Tuple[Tuple[tf.Tensor]]], use_cache: Optional[bool], output_attentions: bool, output_hidden_states: bool, return_dict: bool, training: bool = False) -> Union[TFBaseModelOutputWithPastAndCrossAttentions, Tuple[tf.Tensor]]: ...

class TFElectraPooler(tf.keras.layers.Layer):
    dense: Incomplete
    def __init__(self, config: ElectraConfig, **kwargs) -> None: ...
    def call(self, hidden_states: tf.Tensor) -> tf.Tensor: ...

class TFElectraEmbeddings(tf.keras.layers.Layer):
    """Construct the embeddings from word, position and token_type embeddings."""
    config: Incomplete
    embedding_size: Incomplete
    max_position_embeddings: Incomplete
    initializer_range: Incomplete
    LayerNorm: Incomplete
    dropout: Incomplete
    def __init__(self, config: ElectraConfig, **kwargs) -> None: ...
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

class TFElectraDiscriminatorPredictions(tf.keras.layers.Layer):
    dense: Incomplete
    dense_prediction: Incomplete
    config: Incomplete
    def __init__(self, config, **kwargs) -> None: ...
    def call(self, discriminator_hidden_states, training: bool = False): ...

class TFElectraGeneratorPredictions(tf.keras.layers.Layer):
    LayerNorm: Incomplete
    dense: Incomplete
    def __init__(self, config, **kwargs) -> None: ...
    def call(self, generator_hidden_states, training: bool = False): ...

class TFElectraPreTrainedModel(TFPreTrainedModel):
    """
    An abstract class to handle weights initialization and a simple interface for downloading and loading pretrained
    models.
    """
    config_class = ElectraConfig
    base_model_prefix: str
    @property
    def dummy_inputs(self):
        """
        Dummy inputs to build the network.

        Returns:
            `Dict[str, tf.Tensor]`: The dummy inputs.
        """

class TFElectraMainLayer(tf.keras.layers.Layer):
    config_class = ElectraConfig
    config: Incomplete
    is_decoder: Incomplete
    embeddings: Incomplete
    embeddings_project: Incomplete
    encoder: Incomplete
    def __init__(self, config, **kwargs) -> None: ...
    def get_input_embeddings(self): ...
    def set_input_embeddings(self, value) -> None: ...
    def get_extended_attention_mask(self, attention_mask, input_shape, dtype, past_key_values_length: int = 0): ...
    def get_head_mask(self, head_mask): ...
    def call(self, input_ids: Optional[TFModelInputType] = None, attention_mask: Optional[Union[np.ndarray, tf.Tensor]] = None, token_type_ids: Optional[Union[np.ndarray, tf.Tensor]] = None, position_ids: Optional[Union[np.ndarray, tf.Tensor]] = None, head_mask: Optional[Union[np.ndarray, tf.Tensor]] = None, inputs_embeds: Optional[Union[np.ndarray, tf.Tensor]] = None, encoder_hidden_states: Optional[Union[np.ndarray, tf.Tensor]] = None, encoder_attention_mask: Optional[Union[np.ndarray, tf.Tensor]] = None, past_key_values: Optional[Tuple[Tuple[Union[np.ndarray, tf.Tensor]]]] = None, use_cache: Optional[bool] = None, output_attentions: Optional[bool] = None, output_hidden_states: Optional[bool] = None, return_dict: Optional[bool] = None, training: Optional[bool] = False) -> Union[TFBaseModelOutputWithPastAndCrossAttentions, Tuple[tf.Tensor]]: ...

@dataclass
class TFElectraForPreTrainingOutput(ModelOutput):
    """
    Output type of [`TFElectraForPreTraining`].

    Args:
        loss (*optional*, returned when `labels` is provided, `tf.Tensor` of shape `(1,)`):
            Total loss of the ELECTRA objective.
        logits (`tf.Tensor` of shape `(batch_size, sequence_length)`):
            Prediction scores of the head (scores for each token before SoftMax).
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
    logits: tf.Tensor = ...
    hidden_states: Optional[Tuple[tf.Tensor]] = ...
    attentions: Optional[Tuple[tf.Tensor]] = ...
    def __init__(self, logits, hidden_states, attentions) -> None: ...

ELECTRA_START_DOCSTRING: str
ELECTRA_INPUTS_DOCSTRING: str

class TFElectraModel(TFElectraPreTrainedModel):
    electra: Incomplete
    def __init__(self, config, *inputs, **kwargs) -> None: ...
    def call(self, input_ids: Optional[TFModelInputType] = None, attention_mask: Optional[Union[np.ndarray, tf.Tensor]] = None, token_type_ids: Optional[Union[np.ndarray, tf.Tensor]] = None, position_ids: Optional[Union[np.ndarray, tf.Tensor]] = None, head_mask: Optional[Union[np.ndarray, tf.Tensor]] = None, inputs_embeds: Optional[Union[np.ndarray, tf.Tensor]] = None, encoder_hidden_states: Optional[Union[np.ndarray, tf.Tensor]] = None, encoder_attention_mask: Optional[Union[np.ndarray, tf.Tensor]] = None, past_key_values: Optional[Tuple[Tuple[Union[np.ndarray, tf.Tensor]]]] = None, use_cache: Optional[bool] = None, output_attentions: Optional[bool] = None, output_hidden_states: Optional[bool] = None, return_dict: Optional[bool] = None, training: Optional[bool] = False) -> Union[TFBaseModelOutputWithPastAndCrossAttentions, Tuple[tf.Tensor]]:
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
    def serving_output(self, output): ...

class TFElectraForPreTraining(TFElectraPreTrainedModel):
    electra: Incomplete
    discriminator_predictions: Incomplete
    def __init__(self, config, **kwargs) -> None: ...
    def call(self, input_ids: Optional[TFModelInputType] = None, attention_mask: Optional[Union[np.ndarray, tf.Tensor]] = None, token_type_ids: Optional[Union[np.ndarray, tf.Tensor]] = None, position_ids: Optional[Union[np.ndarray, tf.Tensor]] = None, head_mask: Optional[Union[np.ndarray, tf.Tensor]] = None, inputs_embeds: Optional[Union[np.ndarray, tf.Tensor]] = None, output_attentions: Optional[bool] = None, output_hidden_states: Optional[bool] = None, return_dict: Optional[bool] = None, training: Optional[bool] = False) -> Union[TFElectraForPreTrainingOutput, Tuple[tf.Tensor]]:
        '''
        Returns:

        Examples:

        ```python
        >>> import tensorflow as tf
        >>> from transformers import AutoTokenizer, TFElectraForPreTraining

        >>> tokenizer = AutoTokenizer.from_pretrained("google/electra-small-discriminator")
        >>> model = TFElectraForPreTraining.from_pretrained("google/electra-small-discriminator")
        >>> input_ids = tf.constant(tokenizer.encode("Hello, my dog is cute"))[None, :]  # Batch size 1
        >>> outputs = model(input_ids)
        >>> scores = outputs[0]
        ```'''
    def serving_output(self, output): ...

class TFElectraMaskedLMHead(tf.keras.layers.Layer):
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

class TFElectraForMaskedLM(TFElectraPreTrainedModel, TFMaskedLanguageModelingLoss):
    config: Incomplete
    electra: Incomplete
    generator_predictions: Incomplete
    activation: Incomplete
    generator_lm_head: Incomplete
    def __init__(self, config, **kwargs) -> None: ...
    def get_lm_head(self): ...
    def get_prefix_bias_name(self): ...
    def call(self, input_ids: Optional[TFModelInputType] = None, attention_mask: Optional[Union[np.ndarray, tf.Tensor]] = None, token_type_ids: Optional[Union[np.ndarray, tf.Tensor]] = None, position_ids: Optional[Union[np.ndarray, tf.Tensor]] = None, head_mask: Optional[Union[np.ndarray, tf.Tensor]] = None, inputs_embeds: Optional[Union[np.ndarray, tf.Tensor]] = None, output_attentions: Optional[bool] = None, output_hidden_states: Optional[bool] = None, return_dict: Optional[bool] = None, labels: Optional[Union[np.ndarray, tf.Tensor]] = None, training: Optional[bool] = False) -> Union[TFMaskedLMOutput, Tuple[tf.Tensor]]:
        """
        labels (`tf.Tensor` of shape `(batch_size, sequence_length)`, *optional*):
            Labels for computing the masked language modeling loss. Indices should be in `[-100, 0, ...,
            config.vocab_size]` (see `input_ids` docstring) Tokens with indices set to `-100` are ignored (masked), the
            loss is only computed for the tokens with labels in `[0, ..., config.vocab_size]`
        """
    def serving_output(self, output: TFMaskedLMOutput) -> TFMaskedLMOutput: ...

class TFElectraClassificationHead(tf.keras.layers.Layer):
    """Head for sentence-level classification tasks."""
    dense: Incomplete
    dropout: Incomplete
    out_proj: Incomplete
    def __init__(self, config, **kwargs) -> None: ...
    def call(self, inputs, **kwargs): ...

class TFElectraForSequenceClassification(TFElectraPreTrainedModel, TFSequenceClassificationLoss):
    num_labels: Incomplete
    electra: Incomplete
    classifier: Incomplete
    def __init__(self, config, *inputs, **kwargs) -> None: ...
    def call(self, input_ids: Optional[TFModelInputType] = None, attention_mask: Optional[Union[np.ndarray, tf.Tensor]] = None, token_type_ids: Optional[Union[np.ndarray, tf.Tensor]] = None, position_ids: Optional[Union[np.ndarray, tf.Tensor]] = None, head_mask: Optional[Union[np.ndarray, tf.Tensor]] = None, inputs_embeds: Optional[Union[np.ndarray, tf.Tensor]] = None, output_attentions: Optional[bool] = None, output_hidden_states: Optional[bool] = None, return_dict: Optional[bool] = None, labels: Optional[Union[np.ndarray, tf.Tensor]] = None, training: Optional[bool] = False) -> Union[TFSequenceClassifierOutput, Tuple[tf.Tensor]]:
        """
        labels (`tf.Tensor` of shape `(batch_size,)`, *optional*):
            Labels for computing the sequence classification/regression loss. Indices should be in `[0, ...,
            config.num_labels - 1]`. If `config.num_labels == 1` a regression loss is computed (Mean-Square loss), If
            `config.num_labels > 1` a classification loss is computed (Cross-Entropy).
        """
    def serving_output(self, output: TFSequenceClassifierOutput) -> TFSequenceClassifierOutput: ...

class TFElectraForMultipleChoice(TFElectraPreTrainedModel, TFMultipleChoiceLoss):
    electra: Incomplete
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
    def call(self, input_ids: Optional[TFModelInputType] = None, attention_mask: Optional[Union[np.ndarray, tf.Tensor]] = None, token_type_ids: Optional[Union[np.ndarray, tf.Tensor]] = None, position_ids: Optional[Union[np.ndarray, tf.Tensor]] = None, head_mask: Optional[Union[np.ndarray, tf.Tensor]] = None, inputs_embeds: Optional[Union[np.ndarray, tf.Tensor]] = None, output_attentions: Optional[bool] = None, output_hidden_states: Optional[bool] = None, return_dict: Optional[bool] = None, labels: Optional[Union[np.ndarray, tf.Tensor]] = None, training: Optional[bool] = False) -> Union[TFMultipleChoiceModelOutput, Tuple[tf.Tensor]]:
        """
        labels (`tf.Tensor` of shape `(batch_size,)`, *optional*):
            Labels for computing the multiple choice classification loss. Indices should be in `[0, ..., num_choices]`
            where `num_choices` is the size of the second dimension of the input tensors. (See `input_ids` above)
        """
    def serving(self, inputs: Dict[str, tf.Tensor]): ...
    def serving_output(self, output: TFMultipleChoiceModelOutput) -> TFMultipleChoiceModelOutput: ...

class TFElectraForTokenClassification(TFElectraPreTrainedModel, TFTokenClassificationLoss):
    electra: Incomplete
    dropout: Incomplete
    classifier: Incomplete
    def __init__(self, config, **kwargs) -> None: ...
    def call(self, input_ids: Optional[TFModelInputType] = None, attention_mask: Optional[Union[np.ndarray, tf.Tensor]] = None, token_type_ids: Optional[Union[np.ndarray, tf.Tensor]] = None, position_ids: Optional[Union[np.ndarray, tf.Tensor]] = None, head_mask: Optional[Union[np.ndarray, tf.Tensor]] = None, inputs_embeds: Optional[Union[np.ndarray, tf.Tensor]] = None, output_attentions: Optional[bool] = None, output_hidden_states: Optional[bool] = None, return_dict: Optional[bool] = None, labels: Optional[Union[np.ndarray, tf.Tensor]] = None, training: Optional[bool] = False) -> Union[TFTokenClassifierOutput, Tuple[tf.Tensor]]:
        """
        labels (`tf.Tensor` of shape `(batch_size, sequence_length)`, *optional*):
            Labels for computing the token classification loss. Indices should be in `[0, ..., config.num_labels - 1]`.
        """
    def serving_output(self, output: TFTokenClassifierOutput) -> TFTokenClassifierOutput: ...

class TFElectraForQuestionAnswering(TFElectraPreTrainedModel, TFQuestionAnsweringLoss):
    num_labels: Incomplete
    electra: Incomplete
    qa_outputs: Incomplete
    def __init__(self, config, *inputs, **kwargs) -> None: ...
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
