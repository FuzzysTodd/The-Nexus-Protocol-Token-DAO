import numpy as np
import tensorflow as tf
from ...activations_tf import get_tf_activation as get_tf_activation
from ...modeling_tf_outputs import TFBaseModelOutput as TFBaseModelOutput, TFBaseModelOutputWithPastAndCrossAttentions as TFBaseModelOutputWithPastAndCrossAttentions, TFSeq2SeqLMOutput as TFSeq2SeqLMOutput, TFSeq2SeqModelOutput as TFSeq2SeqModelOutput
from ...modeling_tf_utils import TFCausalLanguageModelingLoss as TFCausalLanguageModelingLoss, TFModelInputType as TFModelInputType, TFPreTrainedModel as TFPreTrainedModel, get_initializer as get_initializer, keras_serializable as keras_serializable, unpack_inputs as unpack_inputs
from ...tf_utils import shape_list as shape_list, stable_softmax as stable_softmax
from ...utils import ContextManagers as ContextManagers, DUMMY_INPUTS as DUMMY_INPUTS, DUMMY_MASK as DUMMY_MASK, add_start_docstrings as add_start_docstrings, add_start_docstrings_to_model_forward as add_start_docstrings_to_model_forward, logging as logging, replace_return_docstrings as replace_return_docstrings
from .configuration_t5 import T5Config as T5Config
from _typeshed import Incomplete
from typing import Optional, Tuple, Union

logger: Incomplete
TF_T5_PRETRAINED_MODEL_ARCHIVE_LIST: Incomplete

class TFT5LayerNorm(tf.keras.layers.Layer):
    variance_epsilon: Incomplete
    def __init__(self, epsilon: float = 1e-06, **kwargs) -> None:
        """
        Construct a layernorm module in the T5 style No bias and no subtraction of mean.
        """
    weight: Incomplete
    def build(self, input_shape) -> None:
        """Build shared word embedding layer"""
    def call(self, hidden_states): ...

class TFT5DenseActDense(tf.keras.layers.Layer):
    wi: Incomplete
    wo: Incomplete
    dropout: Incomplete
    act: Incomplete
    def __init__(self, config, **kwargs) -> None: ...
    def call(self, hidden_states, training: bool = False): ...

class TFT5DenseGatedActDense(tf.keras.layers.Layer):
    wi_0: Incomplete
    wi_1: Incomplete
    wo: Incomplete
    dropout: Incomplete
    act: Incomplete
    def __init__(self, config, **kwargs) -> None: ...
    def call(self, hidden_states, training: bool = False): ...

class TFT5LayerFF(tf.keras.layers.Layer):
    DenseReluDense: Incomplete
    layer_norm: Incomplete
    dropout: Incomplete
    def __init__(self, config, **kwargs) -> None: ...
    def call(self, hidden_states, training: bool = False): ...

class TFT5Attention(tf.keras.layers.Layer):
    NEW_ID: Incomplete
    layer_id: Incomplete
    is_decoder: Incomplete
    use_cache: Incomplete
    has_relative_attention_bias: Incomplete
    output_attentions: Incomplete
    relative_attention_num_buckets: Incomplete
    relative_attention_max_distance: Incomplete
    d_model: Incomplete
    key_value_proj_dim: Incomplete
    n_heads: Incomplete
    inner_dim: Incomplete
    relative_attention_bias_initializer: Incomplete
    q: Incomplete
    k: Incomplete
    v: Incomplete
    o: Incomplete
    dropout: Incomplete
    pruned_heads: Incomplete
    def __init__(self, config, has_relative_attention_bias: bool = False, **kwargs) -> None: ...
    relative_attention_bias: Incomplete
    def build(self, input_shape): ...
    def prune_heads(self, heads) -> None: ...
    def compute_bias(self, query_length, key_length):
        """Compute binned relative position bias"""
    def call(self, hidden_states, mask: Incomplete | None = None, key_value_states: Incomplete | None = None, position_bias: Incomplete | None = None, past_key_value: Incomplete | None = None, layer_head_mask: Incomplete | None = None, query_length: Incomplete | None = None, use_cache: bool = False, training: bool = False, output_attentions: bool = False):
        """
        Self-attention (if key_value_states is None) or attention over source sentence (provided by key_value_states).
        """

class TFT5LayerSelfAttention(tf.keras.layers.Layer):
    SelfAttention: Incomplete
    layer_norm: Incomplete
    dropout: Incomplete
    def __init__(self, config, has_relative_attention_bias: bool = False, **kwargs) -> None: ...
    def call(self, hidden_states, attention_mask: Incomplete | None = None, position_bias: Incomplete | None = None, layer_head_mask: Incomplete | None = None, past_key_value: Incomplete | None = None, use_cache: bool = False, output_attentions: bool = False, training: bool = False): ...

class TFT5LayerCrossAttention(tf.keras.layers.Layer):
    EncDecAttention: Incomplete
    layer_norm: Incomplete
    dropout: Incomplete
    def __init__(self, config, **kwargs) -> None: ...
    def call(self, hidden_states, key_value_states, attention_mask: Incomplete | None = None, position_bias: Incomplete | None = None, layer_head_mask: Incomplete | None = None, past_key_value: Incomplete | None = None, query_length: Incomplete | None = None, use_cache: bool = False, output_attentions: bool = False, training: bool = False): ...

class TFT5Block(tf.keras.layers.Layer):
    is_decoder: Incomplete
    layer: Incomplete
    def __init__(self, config, has_relative_attention_bias: bool = False, **kwargs) -> None: ...
    def call(self, hidden_states, attention_mask: Incomplete | None = None, position_bias: Incomplete | None = None, encoder_hidden_states: Incomplete | None = None, encoder_attention_mask: Incomplete | None = None, encoder_decoder_position_bias: Incomplete | None = None, layer_head_mask: Incomplete | None = None, encoder_layer_head_mask: Incomplete | None = None, past_key_value: Incomplete | None = None, use_cache: bool = False, output_attentions: bool = False, training: bool = False): ...

class TFT5MainLayer(tf.keras.layers.Layer):
    config_class = T5Config
    config: Incomplete
    output_hidden_states: Incomplete
    output_attentions: Incomplete
    use_cache: Incomplete
    embed_tokens: Incomplete
    is_decoder: Incomplete
    num_hidden_layers: Incomplete
    block: Incomplete
    final_layer_norm: Incomplete
    dropout: Incomplete
    def __init__(self, config, embed_tokens: Incomplete | None = None, **kwargs) -> None: ...
    def call(self, input_ids: Incomplete | None = None, attention_mask: Incomplete | None = None, encoder_hidden_states: Incomplete | None = None, encoder_attention_mask: Incomplete | None = None, inputs_embeds: Incomplete | None = None, head_mask: Incomplete | None = None, encoder_head_mask: Incomplete | None = None, past_key_values: Incomplete | None = None, use_cache: Incomplete | None = None, output_attentions: Incomplete | None = None, output_hidden_states: Incomplete | None = None, return_dict: Incomplete | None = None, training: bool = False) -> Tuple: ...

class TFT5PreTrainedModel(TFPreTrainedModel):
    """
    An abstract class to handle weights initialization and a simple interface for downloading and loading pretrained
    models.
    """
    config_class = T5Config
    base_model_prefix: str
    @property
    def dummy_inputs(self): ...
    def serving(self, inputs): ...
    def get_input_embeddings(self): ...
    shared: Incomplete
    def set_input_embeddings(self, value) -> None: ...

T5_START_DOCSTRING: str
T5_INPUTS_DOCSTRING: str
T5_ENCODER_INPUTS_DOCSTRING: str

class TFT5Model(TFT5PreTrainedModel):
    shared: Incomplete
    encoder: Incomplete
    decoder: Incomplete
    def __init__(self, config, *inputs, **kwargs) -> None: ...
    def get_encoder(self): ...
    def get_decoder(self): ...
    def call(self, input_ids: Optional[TFModelInputType] = None, attention_mask: Optional[Union[np.ndarray, tf.Tensor]] = None, decoder_input_ids: Optional[Union[np.ndarray, tf.Tensor]] = None, decoder_attention_mask: Optional[Union[np.ndarray, tf.Tensor]] = None, head_mask: Optional[Union[np.ndarray, tf.Tensor]] = None, decoder_head_mask: Optional[Union[np.ndarray, tf.Tensor]] = None, encoder_outputs: Optional[Union[np.ndarray, tf.Tensor]] = None, past_key_values: Optional[Tuple[Tuple[Union[np.ndarray, tf.Tensor]]]] = None, inputs_embeds: Optional[Union[np.ndarray, tf.Tensor]] = None, decoder_inputs_embeds: Optional[Union[np.ndarray, tf.Tensor]] = None, use_cache: Optional[bool] = None, output_attentions: Optional[bool] = None, output_hidden_states: Optional[bool] = None, return_dict: Optional[bool] = None, training: Optional[bool] = False) -> Union[Tuple, TFSeq2SeqModelOutput]:
        '''
        Returns:

        Examples:

        ```python
        >>> from transformers import AutoTokenizer, TFT5Model

        >>> tokenizer = AutoTokenizer.from_pretrained("t5-small")
        >>> model = TFT5Model.from_pretrained("t5-small")

        >>> input_ids = tokenizer(
        ...     "Studies have been shown that owning a dog is good for you", return_tensors="tf"
        ... ).input_ids  # Batch size 1
        >>> decoder_input_ids = tokenizer("Studies show that", return_tensors="tf").input_ids  # Batch size 1

        >>> # preprocess: Prepend decoder_input_ids with start token which is pad token for T5Model.
        >>> # This is not needed for torch\'s T5ForConditionalGeneration as it does this internally using labels arg.
        >>> decoder_input_ids = model._shift_right(decoder_input_ids)

        >>> # forward pass
        >>> outputs = model(input_ids, decoder_input_ids=decoder_input_ids)
        >>> last_hidden_states = outputs.last_hidden_state
        ```'''
    def serving_output(self, output): ...

class TFT5ForConditionalGeneration(TFT5PreTrainedModel, TFCausalLanguageModelingLoss):
    model_dim: Incomplete
    shared: Incomplete
    encoder: Incomplete
    decoder: Incomplete
    lm_head: Incomplete
    def __init__(self, config, *inputs, **kwargs) -> None: ...
    def get_output_embeddings(self): ...
    def set_output_embeddings(self, value) -> None: ...
    def get_encoder(self): ...
    def get_decoder(self): ...
    def call(self, input_ids: Optional[TFModelInputType] = None, attention_mask: Optional[Union[np.ndarray, tf.Tensor]] = None, decoder_input_ids: Optional[Union[np.ndarray, tf.Tensor]] = None, decoder_attention_mask: Optional[Union[np.ndarray, tf.Tensor]] = None, head_mask: Optional[Union[np.ndarray, tf.Tensor]] = None, decoder_head_mask: Optional[Union[np.ndarray, tf.Tensor]] = None, encoder_outputs: Optional[Union[np.ndarray, tf.Tensor]] = None, past_key_values: Optional[Tuple[Tuple[Union[np.ndarray, tf.Tensor]]]] = None, inputs_embeds: Optional[Union[np.ndarray, tf.Tensor]] = None, decoder_inputs_embeds: Optional[Union[np.ndarray, tf.Tensor]] = None, labels: Optional[Union[np.ndarray, tf.Tensor]] = None, use_cache: Optional[bool] = None, output_attentions: Optional[bool] = None, output_hidden_states: Optional[bool] = None, return_dict: Optional[bool] = None, training: Optional[bool] = False) -> Union[Tuple, TFSeq2SeqLMOutput]:
        '''
        labels (`tf.Tensor` of shape `(batch_size, sequence_length)`, *optional*):
            Labels for computing the cross entropy classification loss. Indices should be in `[0, ...,
            config.vocab_size - 1]`.

        Returns:

        Examples:

        ```python
        >>> from transformers import AutoTokenizer, TFT5ForConditionalGeneration

        >>> tokenizer = AutoTokenizer.from_pretrained("t5-small")
        >>> model = TFT5ForConditionalGeneration.from_pretrained("t5-small")

        >>> # training
        >>> inputs = tokenizer("The <extra_id_0> walks in <extra_id_1> park", return_tensors="tf").input_ids
        >>> labels = tokenizer("<extra_id_0> cute dog <extra_id_1> the <extra_id_2>", return_tensors="tf").input_ids
        >>> outputs = model(inputs, labels=labels)
        >>> loss = outputs.loss
        >>> logits = outputs.logits

        >>> # inference
        >>> inputs = tokenizer(
        ...     "summarize: studies have shown that owning a dog is good for you", return_tensors="tf"
        ... ).input_ids  # Batch size 1
        >>> outputs = model.generate(inputs)
        >>> print(tokenizer.decode(outputs[0], skip_special_tokens=True))
        >>> # studies have shown that owning a dog is good for you
        ```'''
    def serving_output(self, output): ...
    def prepare_inputs_for_generation(self, input_ids, past_key_values: Incomplete | None = None, attention_mask: Incomplete | None = None, decoder_attention_mask: Incomplete | None = None, head_mask: Incomplete | None = None, decoder_head_mask: Incomplete | None = None, use_cache: Incomplete | None = None, encoder_outputs: Incomplete | None = None, **kwargs): ...
    def prepare_decoder_input_ids_from_labels(self, labels: tf.Tensor): ...

class TFT5EncoderModel(TFT5PreTrainedModel):
    shared: Incomplete
    encoder: Incomplete
    def __init__(self, config, *inputs, **kwargs) -> None: ...
    @property
    def dummy_inputs(self): ...
    def get_encoder(self): ...
    def call(self, input_ids: Optional[TFModelInputType] = None, attention_mask: Optional[Union[np.ndarray, tf.Tensor]] = None, head_mask: Optional[Union[np.ndarray, tf.Tensor]] = None, inputs_embeds: Optional[Union[np.ndarray, tf.Tensor]] = None, output_attentions: Optional[bool] = None, output_hidden_states: Optional[bool] = None, return_dict: Optional[bool] = None, training: Optional[bool] = False) -> Union[Tuple, TFBaseModelOutput]:
        '''
        Returns:

        Examples:

        ```python
        >>> from transformers import AutoTokenizer, TFT5EncoderModel

        >>> tokenizer = AutoTokenizer.from_pretrained("t5-small")
        >>> model = TFT5EncoderModel.from_pretrained("t5-small")

        >>> input_ids = tokenizer(
        ...     "Studies have been shown that owning a dog is good for you", return_tensors="tf"
        ... ).input_ids  # Batch size 1
        >>> outputs = model(input_ids)
        ```'''
    def serving(self, inputs): ...
    def serving_output(self, output): ...
