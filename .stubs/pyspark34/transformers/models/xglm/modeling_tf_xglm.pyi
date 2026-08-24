import numpy as np
import tensorflow as tf
from ...activations_tf import get_tf_activation as get_tf_activation
from ...file_utils import DUMMY_INPUTS as DUMMY_INPUTS, add_code_sample_docstrings as add_code_sample_docstrings, add_start_docstrings as add_start_docstrings, add_start_docstrings_to_model_forward as add_start_docstrings_to_model_forward, replace_return_docstrings as replace_return_docstrings
from ...modeling_tf_outputs import TFBaseModelOutputWithPastAndCrossAttentions as TFBaseModelOutputWithPastAndCrossAttentions, TFCausalLMOutputWithCrossAttentions as TFCausalLMOutputWithCrossAttentions
from ...modeling_tf_utils import TFCausalLanguageModelingLoss as TFCausalLanguageModelingLoss, TFModelInputType as TFModelInputType, TFPreTrainedModel as TFPreTrainedModel, TFSharedEmbeddings as TFSharedEmbeddings, get_initializer as get_initializer, keras_serializable as keras_serializable, unpack_inputs as unpack_inputs
from ...tf_utils import shape_list as shape_list, stable_softmax as stable_softmax
from ...utils import logging as logging
from .configuration_xglm import XGLMConfig as XGLMConfig
from _typeshed import Incomplete
from typing import Any, Optional, Tuple, Union

logger: Incomplete
TF_XGLM_PRETRAINED_MODEL_ARCHIVE_LIST: Incomplete
LARGE_NEGATIVE: float

def create_sinusiodal_positions(num_positions: int, embedding_dim: int, padding_idx: Optional[int]) -> tf.Tensor: ...

class TFXGLMAttention(tf.keras.layers.Layer):
    '''Multi-headed attention from "Attention Is All You Need'''
    embed_dim: Incomplete
    num_heads: Incomplete
    dropout: Incomplete
    head_dim: Incomplete
    scaling: Incomplete
    is_decoder: Incomplete
    k_proj: Incomplete
    q_proj: Incomplete
    v_proj: Incomplete
    out_proj: Incomplete
    def __init__(self, embed_dim: int, num_heads: int, dropout: float = 0.0, is_decoder: bool = False, bias: bool = True, **kwargs) -> None: ...
    def call(self, hidden_states: tf.Tensor, key_value_states: Optional[tf.Tensor] = None, past_key_value: Optional[Tuple[Tuple[tf.Tensor]]] = None, attention_mask: Optional[tf.Tensor] = None, layer_head_mask: Optional[tf.Tensor] = None, training: Optional[bool] = False) -> Tuple[tf.Tensor, Optional[tf.Tensor]]:
        """Input shape: Batch x Time x Channel"""

class TFXGLMDecoderLayer(tf.keras.layers.Layer):
    embed_dim: Incomplete
    self_attn: Incomplete
    dropout: Incomplete
    activation_fn: Incomplete
    activation_dropout: Incomplete
    encoder_attn: Incomplete
    encoder_attn_layer_norm: Incomplete
    self_attn_layer_norm: Incomplete
    fc1: Incomplete
    fc2: Incomplete
    final_layer_norm: Incomplete
    def __init__(self, config: XGLMConfig, **kwargs: Any) -> None: ...
    def call(self, hidden_states: tf.Tensor, attention_mask: Optional[tf.Tensor] = None, encoder_hidden_states: Optional[tf.Tensor] = None, encoder_attention_mask: Optional[tf.Tensor] = None, layer_head_mask: Optional[tf.Tensor] = None, cross_attn_layer_head_mask: Optional[tf.Tensor] = None, past_key_value: Optional[Tuple[tf.Tensor]] = None, training: Optional[bool] = False) -> Tuple[tf.Tensor, tf.Tensor, Tuple[Tuple[tf.Tensor]]]:
        """
        Args:
            hidden_states (`tf.Tensor`): input to the layer of shape *(seq_len, batch, embed_dim)*
            attention_mask (`tf.Tensor`): attention mask of size
                *(batch, 1, tgt_len, src_len)* where padding elements are indicated by very large negative values.
            encoder_hidden_states (`tf.Tensor`):
                cross attention input to the layer of shape *(seq_len, batch, embed_dim)*
            encoder_attention_mask (`tf.Tensor`): encoder attention mask of size
                *(batch, 1, tgt_len, src_len)* where padding elements are indicated by very large negative values.
            layer_head_mask (`tf.Tensor`): mask for attention heads in a given layer of size
                *(decoder_attention_heads,)*
            cross_attn_layer_head_mask (`tf.Tensor`): mask for heads of the cross-attention module.
                *(decoder_attention_heads,)*
            past_key_value (`Tuple(tf.Tensor)`): cached past key and value projection states
        """

class TFXGLMMainLayer(tf.keras.layers.Layer):
    config_class = XGLMConfig
    config: Incomplete
    padding_idx: Incomplete
    max_target_positions: Incomplete
    embed_scale: Incomplete
    embed_tokens: Incomplete
    offset: int
    dropout: Incomplete
    layers: Incomplete
    layerdrop: Incomplete
    layer_norm: Incomplete
    def __init__(self, config: XGLMConfig, embed_tokens: Optional[TFSharedEmbeddings] = None, *inputs, **kwargs: Any) -> None: ...
    def get_input_embeddings(self) -> TFSharedEmbeddings: ...
    def set_input_embeddings(self, value: TFSharedEmbeddings) -> None: ...
    def embed_positions(self, input_ids: Optional[TFModelInputType] = None, inputs_embeds: Optional[Union[np.ndarray, tf.Tensor]] = None, past_key_values_length: Optional[int] = None) -> tf.Tensor: ...
    def call(self, input_ids: Optional[TFModelInputType] = None, attention_mask: Optional[Union[np.ndarray, tf.Tensor]] = None, encoder_hidden_states: Optional[Union[np.ndarray, tf.Tensor]] = None, encoder_attention_mask: Optional[Union[np.ndarray, tf.Tensor]] = None, head_mask: Optional[Union[np.ndarray, tf.Tensor]] = None, cross_attn_head_mask: Optional[Union[np.ndarray, tf.Tensor]] = None, past_key_values: Optional[Tuple[Tuple[Union[np.ndarray, tf.Tensor]]]] = None, inputs_embeds: Optional[Union[np.ndarray, tf.Tensor]] = None, use_cache: Optional[bool] = None, output_attentions: Optional[bool] = None, output_hidden_states: Optional[bool] = None, return_dict: Optional[bool] = None, training: Optional[bool] = False, **kwargs: Any) -> Union[TFBaseModelOutputWithPastAndCrossAttentions, Tuple[tf.Tensor]]: ...

class TFXGLMPreTrainedModel(TFPreTrainedModel):
    config_class = XGLMConfig
    base_model_prefix: str
    @property
    def dummy_inputs(self): ...
    def serving(self, inputs): ...

XGLM_START_DOCSTRING: str
XGLM_INPUTS_DOCSTRING: str

class TFXGLMModel(TFXGLMPreTrainedModel):
    """
    Transformer decoder consisting of *config.num_layers* layers. Each layer is a [`TFXGLMDecoderLayer`]

    Args:
        config: XGLMConfig
        embed_tokens: [TFSharedEmbeddings]: output embedding
    """
    model: Incomplete
    def __init__(self, config: XGLMConfig, embed_tokens: Optional[TFSharedEmbeddings] = None, *inputs: Any, **kwargs: Any) -> None: ...
    def call(self, input_ids: Optional[TFModelInputType] = None, attention_mask: Optional[Union[np.ndarray, tf.Tensor]] = None, encoder_hidden_states: Optional[Union[np.ndarray, tf.Tensor]] = None, encoder_attention_mask: Optional[Union[np.ndarray, tf.Tensor]] = None, head_mask: Optional[Union[np.ndarray, tf.Tensor]] = None, cross_attn_head_mask: Optional[Union[np.ndarray, tf.Tensor]] = None, past_key_values: Optional[Tuple[Tuple[Union[np.ndarray, tf.Tensor]]]] = None, inputs_embeds: Optional[Union[np.ndarray, tf.Tensor]] = None, use_cache: Optional[bool] = None, output_attentions: Optional[bool] = None, output_hidden_states: Optional[bool] = None, return_dict: Optional[bool] = None, training: Optional[bool] = False, **kwargs: Any) -> Union[TFBaseModelOutputWithPastAndCrossAttentions, Tuple[tf.Tensor]]: ...
    def serving_output(self, output): ...

class TFXGLMForCausalLM(TFXGLMPreTrainedModel, TFCausalLanguageModelingLoss):
    base_model_prefix: str
    model: Incomplete
    lm_head: Incomplete
    supports_xla_generation: bool
    def __init__(self, config: XGLMConfig, embed_tokens: Optional[TFSharedEmbeddings] = None, *inputs: Any, **kwargs: Any) -> None: ...
    def get_output_embeddings(self): ...
    def set_output_embeddings(self, new_embeddings) -> None: ...
    def prepare_inputs_for_generation(self, inputs, past_key_values: Incomplete | None = None, use_cache: Incomplete | None = None, **kwargs): ...
    def call(self, input_ids: Optional[TFModelInputType] = None, attention_mask: Optional[Union[np.ndarray, tf.Tensor]] = None, encoder_hidden_states: Optional[Union[np.ndarray, tf.Tensor]] = None, encoder_attention_mask: Optional[Union[np.ndarray, tf.Tensor]] = None, head_mask: Optional[Union[np.ndarray, tf.Tensor]] = None, cross_attn_head_mask: Optional[Union[np.ndarray, tf.Tensor]] = None, past_key_values: Optional[Tuple[Tuple[Union[np.ndarray, tf.Tensor]]]] = None, inputs_embeds: Optional[Union[np.ndarray, tf.Tensor]] = None, labels: Optional[Union[np.ndarray, tf.Tensor]] = None, use_cache: Optional[bool] = None, output_attentions: Optional[bool] = None, output_hidden_states: Optional[bool] = None, return_dict: Optional[bool] = None, training: Optional[bool] = False, **kwargs: Any) -> Union[TFCausalLMOutputWithCrossAttentions, Tuple[tf.Tensor]]:
        """
        labels (`np.ndarray` or `tf.Tensor` of shape `(batch_size, sequence_length)`, *optional*):
            Labels for language modeling. Note that the labels **are shifted** inside the model, i.e. you can set
            `labels = input_ids` Indices are selected in `[-100, 0, ..., config.vocab_size]` All labels set to `-100`
            are ignored (masked), the loss is only computed for labels in `[0, ..., config.vocab_size]`
        """
    def serving_output(self, output): ...
