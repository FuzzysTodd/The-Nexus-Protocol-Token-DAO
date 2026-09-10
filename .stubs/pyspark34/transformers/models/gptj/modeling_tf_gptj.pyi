import numpy as np
import tensorflow as tf
from ...activations_tf import get_tf_activation as get_tf_activation
from ...file_utils import DUMMY_INPUTS as DUMMY_INPUTS, add_code_sample_docstrings as add_code_sample_docstrings, add_start_docstrings as add_start_docstrings, add_start_docstrings_to_model_forward as add_start_docstrings_to_model_forward
from ...modeling_tf_outputs import TFBaseModelOutputWithPast as TFBaseModelOutputWithPast, TFCausalLMOutputWithPast as TFCausalLMOutputWithPast, TFQuestionAnsweringModelOutput as TFQuestionAnsweringModelOutput, TFSequenceClassifierOutputWithPast as TFSequenceClassifierOutputWithPast
from ...modeling_tf_utils import TFCausalLanguageModelingLoss as TFCausalLanguageModelingLoss, TFModelInputType as TFModelInputType, TFPreTrainedModel as TFPreTrainedModel, TFQuestionAnsweringLoss as TFQuestionAnsweringLoss, TFSequenceClassificationLoss as TFSequenceClassificationLoss, TFSharedEmbeddings as TFSharedEmbeddings, get_initializer as get_initializer, keras_serializable as keras_serializable, unpack_inputs as unpack_inputs
from ...tf_utils import shape_list as shape_list, stable_softmax as stable_softmax
from ...utils import logging as logging
from .configuration_gptj import GPTJConfig as GPTJConfig
from _typeshed import Incomplete
from typing import Optional, Tuple, Union

logger: Incomplete
GPTJ_PRETRAINED_MODEL_ARCHIVE_LIST: Incomplete

def create_sinusoidal_positions(num_pos: int, dim: int) -> tf.Tensor: ...
def rotate_every_two(x: tf.Tensor) -> tf.Tensor: ...
def apply_rotary_pos_emb(tensor: tf.Tensor, sincos: tf.Tensor) -> tf.Tensor: ...

class TFGPTJAttention(tf.keras.layers.Layer):
    embed_dim: Incomplete
    num_attention_heads: Incomplete
    head_dim: Incomplete
    scale_attn: Incomplete
    rotary_dim: Incomplete
    attn_dropout: Incomplete
    resid_dropout: Incomplete
    q_proj: Incomplete
    k_proj: Incomplete
    v_proj: Incomplete
    out_proj: Incomplete
    max_positions: Incomplete
    lower_triangle_mask: Incomplete
    embed_positions: Incomplete
    def __init__(self, config: GPTJConfig, **kwargs) -> None: ...
    def get_causal_mask(self, key_length, query_length) -> tf.Tensor: ...
    @staticmethod
    def get_masked_bias(dtype: tf.DType) -> tf.Tensor: ...
    def call(self, hidden_states: tf.Tensor, layer_past: Optional[Tuple[tf.Tensor, tf.Tensor]] = None, attention_mask: Optional[tf.Tensor] = None, position_ids: Optional[tf.Tensor] = None, head_mask: Optional[tf.Tensor] = None, use_cache: bool = False, output_attentions: bool = False): ...

class TFGPTJMLP(tf.keras.layers.Layer):
    fc_in: Incomplete
    fc_out: Incomplete
    act: Incomplete
    dropout: Incomplete
    def __init__(self, intermediate_size: int, config: GPTJConfig, **kwargs) -> None: ...
    def call(self, hidden_states: tf.Tensor) -> tf.Tensor: ...

class TFGPTJBlock(tf.keras.layers.Layer):
    ln_1: Incomplete
    attn: Incomplete
    mlp: Incomplete
    def __init__(self, config: GPTJConfig, **kwargs) -> None: ...
    def call(self, hidden_states: tf.Tensor, layer_past: Optional[tf.Tensor] = None, attention_mask: Optional[tf.Tensor] = None, position_ids: Optional[tf.Tensor] = None, head_mask: Optional[tf.Tensor] = None, use_cache: bool = False, output_attentions: bool = False): ...

class TFGPTJMainLayer(tf.keras.layers.Layer):
    config_class = GPTJConfig
    config: Incomplete
    output_attentions: Incomplete
    output_hidden_states: Incomplete
    use_cache: Incomplete
    return_dict: Incomplete
    num_hidden_layers: Incomplete
    n_embd: Incomplete
    n_positions: Incomplete
    initializer_range: Incomplete
    wte: Incomplete
    drop: Incomplete
    h: Incomplete
    ln_f: Incomplete
    def __init__(self, config: GPTJConfig, *inputs, **kwargs) -> None: ...
    def get_input_embeddings(self): ...
    def set_input_embeddings(self, value: tf.Tensor): ...
    def call(self, input_ids: Incomplete | None = None, past_key_values: Incomplete | None = None, attention_mask: Incomplete | None = None, token_type_ids: Incomplete | None = None, position_ids: Incomplete | None = None, head_mask: Incomplete | None = None, inputs_embeds: Incomplete | None = None, use_cache: Incomplete | None = None, output_attentions: Incomplete | None = None, output_hidden_states: Incomplete | None = None, return_dict: Incomplete | None = None, training: bool = False) -> Union[TFBaseModelOutputWithPast, Tuple[tf.Tensor]]: ...

class TFGPTJPreTrainedModel(TFPreTrainedModel):
    """
    An abstract class to handle weights initialization and a simple interface for downloading and loading pretrained
    models.
    """
    config_class = GPTJConfig
    base_model_prefix: str
    @property
    def dummy_inputs(self):
        """
        Dummy inputs to build the network.

        Returns:
            `Dict[str, tf.Tensor]`: The dummy inputs.
        """
    def serving(self, inputs): ...

GPTJ_START_DOCSTRING: str
GPTJ_INPUTS_DOCSTRING: str

class TFGPTJModel(TFGPTJPreTrainedModel):
    transformer: Incomplete
    def __init__(self, config, *inputs, **kwargs) -> None: ...
    def call(self, input_ids: Optional[TFModelInputType] = None, past_key_values: Optional[Tuple[Tuple[Union[np.ndarray, tf.Tensor]]]] = None, attention_mask: Optional[Union[np.ndarray, tf.Tensor]] = None, token_type_ids: Optional[Union[np.ndarray, tf.Tensor]] = None, position_ids: Optional[Union[np.ndarray, tf.Tensor]] = None, head_mask: Optional[Union[np.ndarray, tf.Tensor]] = None, inputs_embeds: Optional[Union[np.ndarray, tf.Tensor]] = None, use_cache: Optional[bool] = None, output_attentions: Optional[bool] = None, output_hidden_states: Optional[bool] = None, return_dict: Optional[bool] = None, training: Optional[bool] = False) -> Union[TFBaseModelOutputWithPast, Tuple[tf.Tensor]]:
        """
        use_cache (`bool`, *optional*, defaults to `True`):
            If set to `True`, `past_key_values` key value states are returned and can be used to speed up decoding (see
            `past`). Set to `False` during training, `True` during generation
        """
    def serving_output(self, output): ...

class TFGPTJForCausalLM(TFGPTJPreTrainedModel, TFCausalLanguageModelingLoss):
    transformer: Incomplete
    lm_head: Incomplete
    def __init__(self, config, *inputs, **kwargs) -> None: ...
    def get_output_embeddings(self): ...
    def set_output_embeddings(self, new_embeddings) -> None: ...
    def prepare_inputs_for_generation(self, inputs, past_key_values: Incomplete | None = None, use_cache: Incomplete | None = None, **kwargs): ...
    def call(self, input_ids: Optional[TFModelInputType] = None, past_key_values: Optional[Tuple[Tuple[Union[np.ndarray, tf.Tensor]]]] = None, attention_mask: Optional[Union[np.ndarray, tf.Tensor]] = None, token_type_ids: Optional[Union[np.ndarray, tf.Tensor]] = None, position_ids: Optional[Union[np.ndarray, tf.Tensor]] = None, head_mask: Optional[Union[np.ndarray, tf.Tensor]] = None, inputs_embeds: Optional[Union[np.ndarray, tf.Tensor]] = None, labels: Optional[Union[np.ndarray, tf.Tensor]] = None, use_cache: Optional[bool] = None, output_attentions: Optional[bool] = None, output_hidden_states: Optional[bool] = None, return_dict: Optional[bool] = None, training: Optional[bool] = False) -> Union[TFCausalLMOutputWithPast, Tuple[tf.Tensor]]:
        """
        labels (`np.ndarray` or `tf.Tensor` of shape `(batch_size, sequence_length)`, *optional*):
            Labels for language modeling. Note that the labels **are shifted** inside the model, i.e. you can set
            `labels = input_ids` Indices are selected in `[-100, 0, ..., config.vocab_size]` All labels set to `-100`
            are ignored (masked), the loss is only computed for labels in `[0, ..., config.vocab_size]`
        """
    def serving_output(self, output): ...

class TFGPTJForSequenceClassification(TFGPTJPreTrainedModel, TFSequenceClassificationLoss):
    num_labels: Incomplete
    transformer: Incomplete
    score: Incomplete
    def __init__(self, config, *inputs, **kwargs) -> None: ...
    def call(self, input_ids: Optional[TFModelInputType] = None, past_key_values: Optional[Tuple[Tuple[Union[np.ndarray, tf.Tensor]]]] = None, attention_mask: Optional[Union[np.ndarray, tf.Tensor]] = None, token_type_ids: Optional[Union[np.ndarray, tf.Tensor]] = None, position_ids: Optional[Union[np.ndarray, tf.Tensor]] = None, head_mask: Optional[Union[np.ndarray, tf.Tensor]] = None, inputs_embeds: Optional[Union[np.ndarray, tf.Tensor]] = None, labels: Optional[Union[np.ndarray, tf.Tensor]] = None, use_cache: Optional[bool] = None, output_attentions: Optional[bool] = None, output_hidden_states: Optional[bool] = None, return_dict: Optional[bool] = None, training: Optional[bool] = False) -> Union[TFSequenceClassifierOutputWithPast, Tuple[tf.Tensor]]:
        """
        labels (`np.ndarray` or `tf.Tensor` of shape `(batch_size,)`, *optional*):
            Labels for computing the sequence classification/regression loss. Indices should be in `[0, ...,
            config.num_labels - 1]`. If `config.num_labels == 1` a regression loss is computed (Mean-Square loss), If
            `config.num_labels > 1` a classification loss is computed (Cross-Entropy).
        """
    def serving_output(self, output): ...

class TFGPTJForQuestionAnswering(TFGPTJPreTrainedModel, TFQuestionAnsweringLoss):
    num_labels: Incomplete
    transformer: Incomplete
    qa_outputs: Incomplete
    def __init__(self, config, *inputs, **kwargs) -> None: ...
    def call(self, input_ids: Optional[TFModelInputType] = None, past_key_values: Optional[Tuple[Tuple[Union[np.ndarray, tf.Tensor]]]] = None, attention_mask: Optional[Union[np.ndarray, tf.Tensor]] = None, token_type_ids: Optional[Union[np.ndarray, tf.Tensor]] = None, position_ids: Optional[Union[np.ndarray, tf.Tensor]] = None, head_mask: Optional[Union[np.ndarray, tf.Tensor]] = None, inputs_embeds: Optional[Union[np.ndarray, tf.Tensor]] = None, start_positions: Optional[Union[np.ndarray, tf.Tensor]] = None, end_positions: Optional[Union[np.ndarray, tf.Tensor]] = None, output_attentions: Optional[bool] = None, output_hidden_states: Optional[bool] = None, return_dict: Optional[bool] = None, training: Optional[bool] = False) -> Union[TFQuestionAnsweringModelOutput, Tuple[tf.Tensor]]:
        """
        start_positions (`np.ndarray` or `tf.Tensor` of shape `(batch_size,)`, *optional*):
            Labels for position (index) of the start of the labelled span for computing the token classification loss.
            Positions are clamped to the length of the sequence (`sequence_length`). Position outside of the sequence
            are not taken into account for computing the loss.
        end_positions (`np.ndarray` or `tf.Tensor` of shape `(batch_size,)`, *optional*):
            Labels for position (index) of the end of the labelled span for computing the token classification loss.
            Positions are clamped to the length of the sequence (`sequence_length`). Position outside of the sequence
            are not taken into account for computing the loss.
        """
    def serving_output(self, output: TFQuestionAnsweringModelOutput) -> TFQuestionAnsweringModelOutput: ...
