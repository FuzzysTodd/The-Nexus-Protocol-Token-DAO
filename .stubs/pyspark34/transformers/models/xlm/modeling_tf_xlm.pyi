import numpy as np
import tensorflow as tf
from ...activations_tf import get_tf_activation as get_tf_activation
from ...modeling_tf_outputs import TFBaseModelOutput as TFBaseModelOutput, TFMultipleChoiceModelOutput as TFMultipleChoiceModelOutput, TFQuestionAnsweringModelOutput as TFQuestionAnsweringModelOutput, TFSequenceClassifierOutput as TFSequenceClassifierOutput, TFTokenClassifierOutput as TFTokenClassifierOutput
from ...modeling_tf_utils import TFModelInputType as TFModelInputType, TFMultipleChoiceLoss as TFMultipleChoiceLoss, TFPreTrainedModel as TFPreTrainedModel, TFQuestionAnsweringLoss as TFQuestionAnsweringLoss, TFSequenceClassificationLoss as TFSequenceClassificationLoss, TFSequenceSummary as TFSequenceSummary, TFSharedEmbeddings as TFSharedEmbeddings, TFTokenClassificationLoss as TFTokenClassificationLoss, get_initializer as get_initializer, keras_serializable as keras_serializable, unpack_inputs as unpack_inputs
from ...tf_utils import shape_list as shape_list, stable_softmax as stable_softmax
from ...utils import MULTIPLE_CHOICE_DUMMY_INPUTS as MULTIPLE_CHOICE_DUMMY_INPUTS, ModelOutput as ModelOutput, add_code_sample_docstrings as add_code_sample_docstrings, add_start_docstrings as add_start_docstrings, add_start_docstrings_to_model_forward as add_start_docstrings_to_model_forward, logging as logging
from .configuration_xlm import XLMConfig as XLMConfig
from _typeshed import Incomplete
from dataclasses import dataclass
from typing import Dict, Optional, Tuple, Union

logger: Incomplete
TF_XLM_PRETRAINED_MODEL_ARCHIVE_LIST: Incomplete

def create_sinusoidal_embeddings(n_pos, dim, out) -> None: ...
def get_masks(slen, lengths, causal, padding_mask: Incomplete | None = None):
    """
    Generate hidden states mask, and optionally an attention mask.
    """

class TFXLMMultiHeadAttention(tf.keras.layers.Layer):
    NEW_ID: Incomplete
    layer_id: Incomplete
    dim: Incomplete
    n_heads: Incomplete
    output_attentions: Incomplete
    q_lin: Incomplete
    k_lin: Incomplete
    v_lin: Incomplete
    out_lin: Incomplete
    dropout: Incomplete
    pruned_heads: Incomplete
    def __init__(self, n_heads, dim, config, **kwargs) -> None: ...
    def prune_heads(self, heads) -> None: ...
    def call(self, input, mask, kv, cache, head_mask, output_attentions, training: bool = False):
        """
        Self-attention (if kv is None) or attention over source sentence (provided by kv).
        """

class TFXLMTransformerFFN(tf.keras.layers.Layer):
    lin1: Incomplete
    lin2: Incomplete
    act: Incomplete
    dropout: Incomplete
    def __init__(self, in_dim, dim_hidden, out_dim, config, **kwargs) -> None: ...
    def call(self, input, training: bool = False): ...

class TFXLMMainLayer(tf.keras.layers.Layer):
    config_class = XLMConfig
    config: Incomplete
    output_hidden_states: Incomplete
    output_attentions: Incomplete
    return_dict: Incomplete
    is_encoder: Incomplete
    is_decoder: Incomplete
    causal: Incomplete
    n_langs: Incomplete
    use_lang_emb: Incomplete
    n_words: Incomplete
    eos_index: Incomplete
    pad_index: Incomplete
    dim: Incomplete
    hidden_dim: Incomplete
    n_heads: Incomplete
    n_layers: Incomplete
    max_position_embeddings: Incomplete
    embed_init_std: Incomplete
    dropout: Incomplete
    attention_dropout: Incomplete
    embeddings: Incomplete
    layer_norm_emb: Incomplete
    attentions: Incomplete
    layer_norm1: Incomplete
    ffns: Incomplete
    layer_norm2: Incomplete
    def __init__(self, config, **kwargs) -> None: ...
    position_embeddings: Incomplete
    lang_embeddings: Incomplete
    def build(self, input_shape) -> None: ...
    def get_input_embeddings(self): ...
    def set_input_embeddings(self, value) -> None: ...
    def call(self, input_ids: Incomplete | None = None, attention_mask: Incomplete | None = None, langs: Incomplete | None = None, token_type_ids: Incomplete | None = None, position_ids: Incomplete | None = None, lengths: Incomplete | None = None, cache: Incomplete | None = None, head_mask: Incomplete | None = None, inputs_embeds: Incomplete | None = None, output_attentions: Incomplete | None = None, output_hidden_states: Incomplete | None = None, return_dict: Incomplete | None = None, training: bool = False) -> Union[TFBaseModelOutput, Tuple[tf.Tensor]]: ...

class TFXLMPreTrainedModel(TFPreTrainedModel):
    """
    An abstract class to handle weights initialization and a simple interface for downloading and loading pretrained
    models.
    """
    config_class = XLMConfig
    base_model_prefix: str
    @property
    def dummy_inputs(self): ...

@dataclass
class TFXLMWithLMHeadModelOutput(ModelOutput):
    """
    Base class for [`TFXLMWithLMHeadModel`] outputs.

    Args:
        logits (`tf.Tensor` of shape `(batch_size, sequence_length, config.vocab_size)`):
            Prediction scores of the language modeling head (scores for each vocabulary token before SoftMax).
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

XLM_START_DOCSTRING: str
XLM_INPUTS_DOCSTRING: str

class TFXLMModel(TFXLMPreTrainedModel):
    transformer: Incomplete
    def __init__(self, config, *inputs, **kwargs) -> None: ...
    def call(self, input_ids: Incomplete | None = None, attention_mask: Incomplete | None = None, langs: Incomplete | None = None, token_type_ids: Incomplete | None = None, position_ids: Incomplete | None = None, lengths: Incomplete | None = None, cache: Incomplete | None = None, head_mask: Incomplete | None = None, inputs_embeds: Incomplete | None = None, output_attentions: Incomplete | None = None, output_hidden_states: Incomplete | None = None, return_dict: Incomplete | None = None, training: bool = False) -> Union[TFBaseModelOutput, Tuple[tf.Tensor]]: ...
    def serving_output(self, output): ...

class TFXLMPredLayer(tf.keras.layers.Layer):
    """
    Prediction layer (cross_entropy or adaptive_softmax).
    """
    asm: Incomplete
    n_words: Incomplete
    pad_index: Incomplete
    input_embeddings: Incomplete
    def __init__(self, config, input_embeddings, **kwargs) -> None: ...
    bias: Incomplete
    def build(self, input_shape) -> None: ...
    def get_output_embeddings(self): ...
    def set_output_embeddings(self, value) -> None: ...
    def get_bias(self): ...
    vocab_size: Incomplete
    def set_bias(self, value) -> None: ...
    def call(self, hidden_states): ...

class TFXLMWithLMHeadModel(TFXLMPreTrainedModel):
    transformer: Incomplete
    pred_layer: Incomplete
    supports_xla_generation: bool
    def __init__(self, config, *inputs, **kwargs) -> None: ...
    def get_lm_head(self): ...
    def get_prefix_bias_name(self): ...
    def prepare_inputs_for_generation(self, inputs, **kwargs): ...
    def call(self, input_ids: Optional[TFModelInputType] = None, attention_mask: Optional[Union[np.ndarray, tf.Tensor]] = None, langs: Optional[Union[np.ndarray, tf.Tensor]] = None, token_type_ids: Optional[Union[np.ndarray, tf.Tensor]] = None, position_ids: Optional[Union[np.ndarray, tf.Tensor]] = None, lengths: Optional[Union[np.ndarray, tf.Tensor]] = None, cache: Optional[Dict[str, tf.Tensor]] = None, head_mask: Optional[Union[np.ndarray, tf.Tensor]] = None, inputs_embeds: Optional[Union[np.ndarray, tf.Tensor]] = None, output_attentions: Optional[bool] = None, output_hidden_states: Optional[bool] = None, return_dict: Optional[bool] = None, training: bool = False) -> Union[TFXLMWithLMHeadModelOutput, Tuple[tf.Tensor]]: ...
    def serving_output(self, output): ...

class TFXLMForSequenceClassification(TFXLMPreTrainedModel, TFSequenceClassificationLoss):
    num_labels: Incomplete
    transformer: Incomplete
    sequence_summary: Incomplete
    def __init__(self, config, *inputs, **kwargs) -> None: ...
    def call(self, input_ids: Optional[TFModelInputType] = None, attention_mask: Optional[Union[np.ndarray, tf.Tensor]] = None, langs: Optional[Union[np.ndarray, tf.Tensor]] = None, token_type_ids: Optional[Union[np.ndarray, tf.Tensor]] = None, position_ids: Optional[Union[np.ndarray, tf.Tensor]] = None, lengths: Optional[Union[np.ndarray, tf.Tensor]] = None, cache: Optional[Dict[str, tf.Tensor]] = None, head_mask: Optional[Union[np.ndarray, tf.Tensor]] = None, inputs_embeds: Optional[Union[np.ndarray, tf.Tensor]] = None, output_attentions: Optional[bool] = None, output_hidden_states: Optional[bool] = None, return_dict: Optional[bool] = None, labels: Optional[Union[np.ndarray, tf.Tensor]] = None, training: bool = False) -> Union[TFSequenceClassifierOutput, Tuple[tf.Tensor]]:
        """
        labels (`tf.Tensor` of shape `(batch_size,)`, *optional*):
            Labels for computing the sequence classification/regression loss. Indices should be in `[0, ...,
            config.num_labels - 1]`. If `config.num_labels == 1` a regression loss is computed (Mean-Square loss), If
            `config.num_labels > 1` a classification loss is computed (Cross-Entropy).
        """
    def serving_output(self, output: TFSequenceClassifierOutput) -> TFSequenceClassifierOutput: ...

class TFXLMForMultipleChoice(TFXLMPreTrainedModel, TFMultipleChoiceLoss):
    transformer: Incomplete
    sequence_summary: Incomplete
    logits_proj: Incomplete
    def __init__(self, config, *inputs, **kwargs) -> None: ...
    @property
    def dummy_inputs(self):
        """
        Dummy inputs to build the network.

        Returns:
            tf.Tensor with dummy inputs
        """
    def call(self, input_ids: Optional[TFModelInputType] = None, attention_mask: Optional[Union[np.ndarray, tf.Tensor]] = None, langs: Optional[Union[np.ndarray, tf.Tensor]] = None, token_type_ids: Optional[Union[np.ndarray, tf.Tensor]] = None, position_ids: Optional[Union[np.ndarray, tf.Tensor]] = None, lengths: Optional[Union[np.ndarray, tf.Tensor]] = None, cache: Optional[Dict[str, tf.Tensor]] = None, head_mask: Optional[Union[np.ndarray, tf.Tensor]] = None, inputs_embeds: Optional[Union[np.ndarray, tf.Tensor]] = None, output_attentions: Optional[bool] = None, output_hidden_states: Optional[bool] = None, return_dict: Optional[bool] = None, labels: Optional[Union[np.ndarray, tf.Tensor]] = None, training: bool = False) -> Union[TFMultipleChoiceModelOutput, Tuple[tf.Tensor]]: ...
    def serving(self, inputs: Dict[str, tf.Tensor]): ...
    def serving_output(self, output: TFMultipleChoiceModelOutput) -> TFMultipleChoiceModelOutput: ...

class TFXLMForTokenClassification(TFXLMPreTrainedModel, TFTokenClassificationLoss):
    num_labels: Incomplete
    transformer: Incomplete
    dropout: Incomplete
    classifier: Incomplete
    def __init__(self, config, *inputs, **kwargs) -> None: ...
    def call(self, input_ids: Optional[TFModelInputType] = None, attention_mask: Optional[Union[np.ndarray, tf.Tensor]] = None, langs: Optional[Union[np.ndarray, tf.Tensor]] = None, token_type_ids: Optional[Union[np.ndarray, tf.Tensor]] = None, position_ids: Optional[Union[np.ndarray, tf.Tensor]] = None, lengths: Optional[Union[np.ndarray, tf.Tensor]] = None, cache: Optional[Dict[str, tf.Tensor]] = None, head_mask: Optional[Union[np.ndarray, tf.Tensor]] = None, inputs_embeds: Optional[Union[np.ndarray, tf.Tensor]] = None, output_attentions: Optional[bool] = None, output_hidden_states: Optional[bool] = None, return_dict: Optional[bool] = None, labels: Optional[Union[np.ndarray, tf.Tensor]] = None, training: bool = False) -> Union[TFTokenClassifierOutput, Tuple[tf.Tensor]]:
        """
        labels (`tf.Tensor` of shape `(batch_size, sequence_length)`, *optional*):
            Labels for computing the token classification loss. Indices should be in `[0, ..., config.num_labels - 1]`.
        """
    def serving_output(self, output: TFTokenClassifierOutput) -> TFTokenClassifierOutput: ...

class TFXLMForQuestionAnsweringSimple(TFXLMPreTrainedModel, TFQuestionAnsweringLoss):
    transformer: Incomplete
    qa_outputs: Incomplete
    def __init__(self, config, *inputs, **kwargs) -> None: ...
    def call(self, input_ids: Optional[TFModelInputType] = None, attention_mask: Optional[Union[np.ndarray, tf.Tensor]] = None, langs: Optional[Union[np.ndarray, tf.Tensor]] = None, token_type_ids: Optional[Union[np.ndarray, tf.Tensor]] = None, position_ids: Optional[Union[np.ndarray, tf.Tensor]] = None, lengths: Optional[Union[np.ndarray, tf.Tensor]] = None, cache: Optional[Dict[str, tf.Tensor]] = None, head_mask: Optional[Union[np.ndarray, tf.Tensor]] = None, inputs_embeds: Optional[Union[np.ndarray, tf.Tensor]] = None, output_attentions: Optional[bool] = None, output_hidden_states: Optional[bool] = None, return_dict: Optional[bool] = None, start_positions: Optional[Union[np.ndarray, tf.Tensor]] = None, end_positions: Optional[Union[np.ndarray, tf.Tensor]] = None, training: bool = False) -> Union[TFQuestionAnsweringModelOutput, Tuple[tf.Tensor]]:
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
