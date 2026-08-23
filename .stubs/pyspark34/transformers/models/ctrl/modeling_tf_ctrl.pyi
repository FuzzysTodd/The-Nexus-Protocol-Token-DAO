import numpy as np
import tensorflow as tf
from ...modeling_tf_outputs import TFBaseModelOutputWithPast as TFBaseModelOutputWithPast, TFCausalLMOutputWithPast as TFCausalLMOutputWithPast, TFSequenceClassifierOutput as TFSequenceClassifierOutput
from ...modeling_tf_utils import TFCausalLanguageModelingLoss as TFCausalLanguageModelingLoss, TFModelInputType as TFModelInputType, TFPreTrainedModel as TFPreTrainedModel, TFSequenceClassificationLoss as TFSequenceClassificationLoss, TFSharedEmbeddings as TFSharedEmbeddings, get_initializer as get_initializer, keras_serializable as keras_serializable, unpack_inputs as unpack_inputs
from ...tf_utils import shape_list as shape_list, stable_softmax as stable_softmax
from ...utils import add_code_sample_docstrings as add_code_sample_docstrings, add_start_docstrings as add_start_docstrings, add_start_docstrings_to_model_forward as add_start_docstrings_to_model_forward, logging as logging
from .configuration_ctrl import CTRLConfig as CTRLConfig
from _typeshed import Incomplete
from typing import Optional, Tuple, Union

logger: Incomplete
TF_CTRL_PRETRAINED_MODEL_ARCHIVE_LIST: Incomplete

def angle_defn(pos, i, d_model_size): ...
def positional_encoding(position, d_model_size): ...
def scaled_dot_product_attention(q, k, v, mask, attention_mask: Incomplete | None = None, head_mask: Incomplete | None = None): ...

class TFMultiHeadAttention(tf.keras.layers.Layer):
    num_heads: Incomplete
    d_model_size: Incomplete
    output_attentions: Incomplete
    depth: Incomplete
    Wq: Incomplete
    Wk: Incomplete
    Wv: Incomplete
    dense: Incomplete
    def __init__(self, d_model_size, num_heads, output_attentions: bool = False, **kwargs) -> None: ...
    def split_into_heads(self, x, batch_size): ...
    def call(self, v, k, q, mask, layer_past, attention_mask, head_mask, use_cache, output_attentions, training: bool = False): ...

class TFPointWiseFeedForwardLayer(tf.keras.layers.Layer):
    dense_0: Incomplete
    dense_2: Incomplete
    def __init__(self, d_model_size, dff, **kwargs) -> None: ...
    def call(self, inputs, trainable: bool = False): ...

class TFEncoderLayer(tf.keras.layers.Layer):
    output_attentions: Incomplete
    multi_head_attention: Incomplete
    ffn: Incomplete
    layernorm1: Incomplete
    layernorm2: Incomplete
    dropout1: Incomplete
    dropout2: Incomplete
    def __init__(self, d_model_size, num_heads, dff, rate: float = 0.1, layer_norm_epsilon: float = 1e-06, output_attentions: bool = False, **kwargs) -> None: ...
    def call(self, x, mask, layer_past, attention_mask, head_mask, use_cache, output_attentions, training: bool = False): ...

class TFCTRLMainLayer(tf.keras.layers.Layer):
    config_class = CTRLConfig
    config: Incomplete
    output_hidden_states: Incomplete
    output_attentions: Incomplete
    use_cache: Incomplete
    return_dict: Incomplete
    d_model_size: Incomplete
    num_layers: Incomplete
    pos_encoding: Incomplete
    w: Incomplete
    dropout: Incomplete
    h: Incomplete
    layernorm: Incomplete
    def __init__(self, config, **kwargs) -> None: ...
    def get_input_embeddings(self): ...
    def set_input_embeddings(self, value) -> None: ...
    def call(self, input_ids: Optional[TFModelInputType] = None, past_key_values: Optional[Tuple[Tuple[Union[np.ndarray, tf.Tensor]]]] = None, attention_mask: Optional[Union[np.ndarray, tf.Tensor]] = None, token_type_ids: Optional[Union[np.ndarray, tf.Tensor]] = None, position_ids: Optional[Union[np.ndarray, tf.Tensor]] = None, head_mask: Optional[Union[np.ndarray, tf.Tensor]] = None, inputs_embeds: Optional[Union[np.ndarray, tf.Tensor]] = None, use_cache: Optional[bool] = None, output_attentions: Optional[bool] = None, output_hidden_states: Optional[bool] = None, return_dict: Optional[bool] = None, training: Optional[bool] = False) -> Union[Tuple, TFBaseModelOutputWithPast]: ...

class TFCTRLPreTrainedModel(TFPreTrainedModel):
    """
    An abstract class to handle weights initialization and a simple interface for downloading and loading pretrained
    models.
    """
    config_class = CTRLConfig
    base_model_prefix: str

CTRL_START_DOCSTRING: str
CTRL_INPUTS_DOCSTRING: str

class TFCTRLModel(TFCTRLPreTrainedModel):
    transformer: Incomplete
    def __init__(self, config, *inputs, **kwargs) -> None: ...
    def call(self, input_ids: Optional[TFModelInputType] = None, past_key_values: Optional[Tuple[Tuple[Union[np.ndarray, tf.Tensor]]]] = None, attention_mask: Optional[Union[np.ndarray, tf.Tensor]] = None, token_type_ids: Optional[Union[np.ndarray, tf.Tensor]] = None, position_ids: Optional[Union[np.ndarray, tf.Tensor]] = None, head_mask: Optional[Union[np.ndarray, tf.Tensor]] = None, inputs_embeds: Optional[Union[np.ndarray, tf.Tensor]] = None, use_cache: Optional[bool] = None, output_attentions: Optional[bool] = None, output_hidden_states: Optional[bool] = None, return_dict: Optional[bool] = None, training: Optional[bool] = False) -> Union[Tuple, TFBaseModelOutputWithPast]: ...
    def serving_output(self, output): ...

class TFCTRLLMHead(tf.keras.layers.Layer):
    config: Incomplete
    supports_xla_generation: bool
    input_embeddings: Incomplete
    def __init__(self, config, input_embeddings, **kwargs) -> None: ...
    bias: Incomplete
    def build(self, input_shape) -> None: ...
    def get_output_embeddings(self): ...
    def set_output_embeddings(self, value) -> None: ...
    def get_bias(self): ...
    def set_bias(self, value) -> None: ...
    def call(self, hidden_states): ...

class TFCTRLLMHeadModel(TFCTRLPreTrainedModel, TFCausalLanguageModelingLoss):
    transformer: Incomplete
    lm_head: Incomplete
    supports_xla_generation: bool
    def __init__(self, config, *inputs, **kwargs) -> None: ...
    def get_lm_head(self): ...
    def get_prefix_bias_name(self): ...
    def prepare_inputs_for_generation(self, input_ids, past_key_values: Incomplete | None = None, use_cache: Incomplete | None = None, **kwargs): ...
    def call(self, input_ids: Optional[TFModelInputType] = None, past_key_values: Optional[Tuple[Tuple[Union[np.ndarray, tf.Tensor]]]] = None, attention_mask: Optional[Union[np.ndarray, tf.Tensor]] = None, token_type_ids: Optional[Union[np.ndarray, tf.Tensor]] = None, position_ids: Optional[Union[np.ndarray, tf.Tensor]] = None, head_mask: Optional[Union[np.ndarray, tf.Tensor]] = None, inputs_embeds: Optional[Union[np.ndarray, tf.Tensor]] = None, use_cache: Optional[bool] = None, output_attentions: Optional[bool] = None, output_hidden_states: Optional[bool] = None, return_dict: Optional[bool] = None, labels: Optional[Union[np.ndarray, tf.Tensor]] = None, training: Optional[bool] = False) -> Union[Tuple, TFCausalLMOutputWithPast]:
        """
        labels (`tf.Tensor` of shape `(batch_size, sequence_length)`, *optional*):
            Labels for computing the cross entropy classification loss. Indices should be in `[0, ...,
            config.vocab_size - 1]`.
        """
    def serving_output(self, output): ...

class TFCTRLForSequenceClassification(TFCTRLPreTrainedModel, TFSequenceClassificationLoss):
    num_labels: Incomplete
    classifier: Incomplete
    transformer: Incomplete
    def __init__(self, config, *inputs, **kwargs) -> None: ...
    def get_output_embeddings(self): ...
    def call(self, input_ids: Optional[TFModelInputType] = None, past_key_values: Optional[Tuple[Tuple[Union[np.ndarray, tf.Tensor]]]] = None, attention_mask: Optional[Union[np.ndarray, tf.Tensor]] = None, token_type_ids: Optional[Union[np.ndarray, tf.Tensor]] = None, position_ids: Optional[Union[np.ndarray, tf.Tensor]] = None, head_mask: Optional[Union[np.ndarray, tf.Tensor]] = None, inputs_embeds: Optional[Union[np.ndarray, tf.Tensor]] = None, use_cache: Optional[bool] = None, output_attentions: Optional[bool] = None, output_hidden_states: Optional[bool] = None, return_dict: Optional[bool] = None, labels: Optional[Union[np.ndarray, tf.Tensor]] = None, training: Optional[bool] = False) -> Union[Tuple, TFSequenceClassifierOutput]:
        """
        labels (`tf.Tensor` of shape `(batch_size, sequence_length)`, *optional*):
            Labels for computing the cross entropy classification loss. Indices should be in `[0, ...,
            config.vocab_size - 1]`.
        """
    def serving_output(self, output: TFSequenceClassifierOutput) -> TFSequenceClassifierOutput: ...
