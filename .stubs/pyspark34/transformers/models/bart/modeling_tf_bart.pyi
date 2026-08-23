import numpy as np
import tensorflow as tf
from ...activations_tf import get_tf_activation as get_tf_activation
from ...modeling_tf_outputs import TFBaseModelOutput as TFBaseModelOutput, TFBaseModelOutputWithPastAndCrossAttentions as TFBaseModelOutputWithPastAndCrossAttentions, TFSeq2SeqLMOutput as TFSeq2SeqLMOutput, TFSeq2SeqModelOutput as TFSeq2SeqModelOutput, TFSeq2SeqSequenceClassifierOutput as TFSeq2SeqSequenceClassifierOutput
from ...modeling_tf_utils import DUMMY_INPUTS as DUMMY_INPUTS, TFCausalLanguageModelingLoss as TFCausalLanguageModelingLoss, TFModelInputType as TFModelInputType, TFPreTrainedModel as TFPreTrainedModel, TFSequenceClassificationLoss as TFSequenceClassificationLoss, keras_serializable as keras_serializable, unpack_inputs as unpack_inputs
from ...tf_utils import shape_list as shape_list, stable_softmax as stable_softmax
from ...utils import ContextManagers as ContextManagers, add_code_sample_docstrings as add_code_sample_docstrings, add_end_docstrings as add_end_docstrings, add_start_docstrings as add_start_docstrings, add_start_docstrings_to_model_forward as add_start_docstrings_to_model_forward, logging as logging, replace_return_docstrings as replace_return_docstrings
from .configuration_bart import BartConfig as BartConfig
from _typeshed import Incomplete
from typing import Optional, Tuple, Union

logger: Incomplete
LARGE_NEGATIVE: float

def shift_tokens_right(input_ids: tf.Tensor, pad_token_id: int, decoder_start_token_id: int): ...

class TFBartLearnedPositionalEmbedding(tf.keras.layers.Embedding):
    """
    This module learns positional embeddings up to a fixed maximum size.
    """
    offset: int
    def __init__(self, num_embeddings: int, embedding_dim: int, **kwargs) -> None: ...
    def call(self, input_shape: Optional[tf.TensorShape] = None, past_key_values_length: int = 0, position_ids: Optional[tf.Tensor] = None):
        """Input is expected to be of size [bsz x seqlen]."""

class TFBartAttention(tf.keras.layers.Layer):
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

class TFBartEncoderLayer(tf.keras.layers.Layer):
    embed_dim: Incomplete
    self_attn: Incomplete
    self_attn_layer_norm: Incomplete
    dropout: Incomplete
    activation_fn: Incomplete
    activation_dropout: Incomplete
    fc1: Incomplete
    fc2: Incomplete
    final_layer_norm: Incomplete
    def __init__(self, config: BartConfig, **kwargs) -> None: ...
    def call(self, hidden_states: tf.Tensor, attention_mask: Optional[Union[np.ndarray, tf.Tensor]], layer_head_mask: Optional[tf.Tensor], training: Optional[bool] = False) -> tf.Tensor:
        """
        Args:
            hidden_states (`tf.Tensor`): input to the layer of shape `(seq_len, batch, embed_dim)`
            attention_mask (`tf.Tensor`): attention mask of size
                `(batch, 1, tgt_len, src_len)` where padding elements are indicated by very large negative values.
            layer_head_mask (`tf.Tensor`): mask for attention heads in a given layer of size
                `(encoder_attention_heads,)`
        """

class TFBartDecoderLayer(tf.keras.layers.Layer):
    embed_dim: Incomplete
    self_attn: Incomplete
    dropout: Incomplete
    activation_fn: Incomplete
    activation_dropout: Incomplete
    self_attn_layer_norm: Incomplete
    encoder_attn: Incomplete
    encoder_attn_layer_norm: Incomplete
    fc1: Incomplete
    fc2: Incomplete
    final_layer_norm: Incomplete
    def __init__(self, config: BartConfig, **kwargs) -> None: ...
    def call(self, hidden_states: tf.Tensor, attention_mask: Optional[Union[np.ndarray, tf.Tensor]] = None, encoder_hidden_states: Optional[Union[np.ndarray, tf.Tensor]] = None, encoder_attention_mask: Optional[Union[np.ndarray, tf.Tensor]] = None, layer_head_mask: Optional[tf.Tensor] = None, cross_attn_layer_head_mask: Optional[tf.Tensor] = None, past_key_value: Optional[Tuple[Tuple[Union[np.ndarray, tf.Tensor]]]] = None, training: Optional[bool] = False) -> Tuple[tf.Tensor, tf.Tensor, Tuple[Tuple[tf.Tensor]]]:
        """
        Args:
            hidden_states (`tf.Tensor`): input to the layer of shape `(seq_len, batch, embed_dim)`
            attention_mask (`tf.Tensor`): attention mask of size
                `(batch, 1, tgt_len, src_len)` where padding elements are indicated by very large negative values.
            encoder_hidden_states (`tf.Tensor`):
                cross attention input to the layer of shape `(seq_len, batch, embed_dim)`
            encoder_attention_mask (`tf.Tensor`): encoder attention mask of size
                `(batch, 1, tgt_len, src_len)` where padding elements are indicated by very large negative values.
            layer_head_mask (`tf.Tensor`): mask for attention heads in a given layer of size
                `(decoder_attention_heads,)`
            cross_attn_layer_head_mask (`tf.Tensor`): mask for heads of the cross-attention module.
                `(decoder_attention_heads,)`
            past_key_value (`Tuple(tf.Tensor)`): cached past key and value projection states
        """

class TFBartClassificationHead(tf.keras.layers.Layer):
    """Head for sentence-level classification tasks."""
    dense: Incomplete
    dropout: Incomplete
    out_proj: Incomplete
    def __init__(self, inner_dim: int, num_classes: int, pooler_dropout: float, name: str, **kwargs) -> None: ...
    def call(self, inputs): ...

class TFBartPretrainedModel(TFPreTrainedModel):
    config_class = BartConfig
    base_model_prefix: str
    @property
    def dummy_inputs(self): ...
    def serving(self, inputs): ...

BART_START_DOCSTRING: str
BART_GENERATION_EXAMPLE: str
BART_INPUTS_DOCSTRING: str

class TFBartEncoder(tf.keras.layers.Layer):
    config_class = BartConfig
    config: Incomplete
    dropout: Incomplete
    layerdrop: Incomplete
    padding_idx: Incomplete
    max_source_positions: Incomplete
    embed_scale: Incomplete
    embed_tokens: Incomplete
    embed_positions: Incomplete
    layers: Incomplete
    layernorm_embedding: Incomplete
    def __init__(self, config: BartConfig, embed_tokens: Optional[tf.keras.layers.Embedding] = None, **kwargs) -> None: ...
    def call(self, input_ids: Optional[TFModelInputType] = None, inputs_embeds: Optional[Union[np.ndarray, tf.Tensor]] = None, attention_mask: Optional[Union[np.ndarray, tf.Tensor]] = None, head_mask: Optional[Union[np.ndarray, tf.Tensor]] = None, output_attentions: Optional[bool] = None, output_hidden_states: Optional[bool] = None, return_dict: Optional[bool] = None, training: Optional[bool] = False) -> Union[TFBaseModelOutput, Tuple[tf.Tensor]]:
        """
        Args:
            input_ids (`tf.Tensor` of shape `(batch_size, sequence_length)`):
                Indices of input sequence tokens in the vocabulary. Padding will be ignored by default should you
                provide it.

                Indices can be obtained using [`AutoTokenizer`]. See [`PreTrainedTokenizer.encode`] and
                [`PreTrainedTokenizer.__call__`] for details.

                [What are input IDs?](../glossary#input-ids)
            attention_mask (`tf.Tensor` of shape `(batch_size, sequence_length)`, *optional*):
                Mask to avoid performing attention on padding token indices. Mask values selected in `[0, 1]`:

                - 1 for tokens that are **not masked**,
                - 0 for tokens that are **masked**.

                [What are attention masks?](../glossary#attention-mask)
            head_mask (`tf.Tensor` of shape `(encoder_layers, encoder_attention_heads)`, `optional):
                Mask to nullify selected heads of the attention modules. Mask values selected in `[0, 1]`:

                - 1 indicates the head is **not masked**,
                - 0 indicates the head is **masked**.

            inputs_embeds (`tf.Tensor` of shape `(batch_size, sequence_length, hidden_size)`, *optional*):
                Optionally, instead of passing `input_ids` you can choose to directly pass an embedded representation.
                This is useful if you want more control over how to convert `input_ids` indices into associated vectors
                than the model's internal embedding lookup matrix.
            output_attentions (`bool`, *optional*):
                Whether or not to return the attentions tensors of all attention layers. See `attentions` under
                returned tensors for more detail.
            output_hidden_states (`bool`, *optional*):
                Whether or not to return the hidden states of all layers. See `hidden_states` under returned tensors
                for more detail.
            return_dict (`bool`, *optional*):
                Whether or not to return a [`~utils.ModelOutput`] instead of a plain tuple.
        """

class TFBartDecoder(tf.keras.layers.Layer):
    config_class = BartConfig
    config: Incomplete
    padding_idx: Incomplete
    embed_tokens: Incomplete
    layerdrop: Incomplete
    embed_positions: Incomplete
    embed_scale: Incomplete
    layers: Incomplete
    layernorm_embedding: Incomplete
    dropout: Incomplete
    def __init__(self, config: BartConfig, embed_tokens: Optional[tf.keras.layers.Embedding] = None, **kwargs) -> None: ...
    def call(self, input_ids: Optional[TFModelInputType] = None, inputs_embeds: Optional[Union[np.ndarray, tf.Tensor]] = None, attention_mask: Optional[Union[np.ndarray, tf.Tensor]] = None, position_ids: Optional[Union[np.ndarray, tf.Tensor]] = None, encoder_hidden_states: Optional[Union[np.ndarray, tf.Tensor]] = None, encoder_attention_mask: Optional[Union[np.ndarray, tf.Tensor]] = None, head_mask: Optional[Union[np.ndarray, tf.Tensor]] = None, cross_attn_head_mask: Optional[Union[np.ndarray, tf.Tensor]] = None, past_key_values: Optional[Tuple[Tuple[Union[np.ndarray, tf.Tensor]]]] = None, use_cache: Optional[bool] = None, output_attentions: Optional[bool] = None, output_hidden_states: Optional[bool] = None, return_dict: Optional[bool] = None, training: Optional[bool] = False) -> Union[TFBaseModelOutputWithPastAndCrossAttentions, Tuple[tf.Tensor]]:
        """
        Args:
            input_ids (`tf.Tensor` of shape `(batch_size, sequence_length)`):
                Indices of input sequence tokens in the vocabulary. Padding will be ignored by default should you
                provide it.

                Indices can be obtained using [`AutoTokenizer`]. See [`PreTrainedTokenizer.encode`] and
                [`PreTrainedTokenizer.__call__`] for details.

                [What are input IDs?](../glossary#input-ids)
            attention_mask (`tf.Tensor` of shape `(batch_size, sequence_length)`, *optional*):
                Mask to avoid performing attention on padding token indices. Mask values selected in `[0, 1]`:

                - 1 for tokens that are **not masked**,
                - 0 for tokens that are **masked**.

                [What are attention masks?](../glossary#attention-mask)
            position_ids (`tf.Tensor` of shape `(batch_size, sequence_length)`, *optional*):
                Indices of positions of each decoder input sequence tokens in the position embeddings. Selected in the
                range `[0, config.max_position_embeddings - 1]`.
            encoder_hidden_states (`tf.Tensor` of shape `(batch_size, encoder_sequence_length, hidden_size)`, *optional*):
                Sequence of hidden-states at the output of the last layer of the encoder. Used in the cross-attention
                of the decoder.
            encoder_attention_mask (`tf.Tensor` of shape `(batch_size, encoder_sequence_length)`, *optional*):
                Mask to avoid performing cross-attention on padding tokens indices of encoder input_ids. Mask values
                selected in `[0, 1]`:

                - 1 for tokens that are **not masked**,
                - 0 for tokens that are **masked**.

                [What are attention masks?](../glossary#attention-mask)
            head_mask (`tf.Tensor` of shape `(decoder_layers, decoder_attention_heads)`, *optional*):
                Mask to nullify selected heads of the attention modules. Mask values selected in `[0, 1]`:

                - 1 indicates the head is **not masked**,
                - 0 indicates the head is **masked**.

            cross_attn_head_mask (`tf.Tensor` of shape `(decoder_layers, decoder_attention_heads)`, *optional*):
                Mask to nullify selected heads of the cross-attention modules. Mask values selected in `[0, 1]`:

                - 1 indicates the head is **not masked**,
                - 0 indicates the head is **masked**.

            past_key_values (`Tuple[Tuple[tf.Tensor]]` of length `config.n_layers` with each tuple having 2 tuples each of which has 2 tensors of shape `(batch_size, num_heads, sequence_length - 1, embed_size_per_head)`):
                Contains precomputed key and value hidden-states of the attention blocks. Can be used to speed up
                decoding.

                If `past_key_values` are used, the user can optionally input only the last `decoder_input_ids` (those
                that don't have their past key value states given to this model) of shape `(batch_size, 1)` instead of
                all `decoder_input_ids` of shape `(batch_size, sequence_length)`. inputs_embeds (`tf.Tensor` of shape
                `(batch_size, sequence_length, hidden_size)`, *optional*): Optionally, instead of passing `input_ids`
                you can choose to directly pass an embedded representation. This is useful if you want more control
                over how to convert `input_ids` indices into associated vectors than the model's internal embedding
                lookup matrix.
            output_attentions (`bool`, *optional*):
                Whether or not to return the attentions tensors of all attention layers. See `attentions` under
                returned tensors for more detail.
            output_hidden_states (`bool`, *optional*):
                Whether or not to return the hidden states of all layers. See `hidden_states` under returned tensors
                for more detail.
            return_dict (`bool`, *optional*):
                Whether or not to return a [`~utils.ModelOutput`] instead of a plain tuple.
        """

class TFBartMainLayer(tf.keras.layers.Layer):
    config_class = BartConfig
    config: Incomplete
    shared: Incomplete
    encoder: Incomplete
    decoder: Incomplete
    def __init__(self, config: BartConfig, load_weight_prefix: Incomplete | None = None, **kwargs) -> None: ...
    def get_input_embeddings(self): ...
    def set_input_embeddings(self, new_embeddings) -> None: ...
    def call(self, input_ids: Optional[TFModelInputType] = None, attention_mask: Optional[Union[np.ndarray, tf.Tensor]] = None, decoder_input_ids: Optional[Union[np.ndarray, tf.Tensor]] = None, decoder_attention_mask: Optional[Union[np.ndarray, tf.Tensor]] = None, decoder_position_ids: Optional[Union[np.ndarray, tf.Tensor]] = None, head_mask: Optional[Union[np.ndarray, tf.Tensor]] = None, decoder_head_mask: Optional[Union[np.ndarray, tf.Tensor]] = None, cross_attn_head_mask: Optional[Union[np.ndarray, tf.Tensor]] = None, encoder_outputs: Optional[Union[Tuple, TFBaseModelOutput]] = None, past_key_values: Optional[Tuple[Tuple[Union[np.ndarray, tf.Tensor]]]] = None, inputs_embeds: Optional[Union[np.ndarray, tf.Tensor]] = None, decoder_inputs_embeds: Optional[Union[np.ndarray, tf.Tensor]] = None, use_cache: Optional[bool] = None, output_attentions: Optional[bool] = None, output_hidden_states: Optional[bool] = None, return_dict: Optional[bool] = None, training: Optional[bool] = False, **kwargs) -> Union[TFSeq2SeqModelOutput, Tuple[tf.Tensor]]: ...

class TFBartModel(TFBartPretrainedModel):
    model: Incomplete
    def __init__(self, config: BartConfig, load_weight_prefix: Incomplete | None = None, *inputs, **kwargs) -> None: ...
    def get_encoder(self): ...
    def get_decoder(self): ...
    def call(self, input_ids: Optional[TFModelInputType] = None, attention_mask: Optional[Union[np.ndarray, tf.Tensor]] = None, decoder_input_ids: Optional[Union[np.ndarray, tf.Tensor]] = None, decoder_attention_mask: Optional[Union[np.ndarray, tf.Tensor]] = None, decoder_position_ids: Optional[Union[np.ndarray, tf.Tensor]] = None, head_mask: Optional[Union[np.ndarray, tf.Tensor]] = None, decoder_head_mask: Optional[Union[np.ndarray, tf.Tensor]] = None, cross_attn_head_mask: Optional[Union[np.ndarray, tf.Tensor]] = None, encoder_outputs: Optional[Union[Tuple, TFBaseModelOutput]] = None, past_key_values: Optional[Tuple[Tuple[Union[np.ndarray, tf.Tensor]]]] = None, inputs_embeds: Optional[Union[np.ndarray, tf.Tensor]] = None, decoder_inputs_embeds: Optional[Union[np.ndarray, tf.Tensor]] = None, use_cache: Optional[bool] = None, output_attentions: Optional[bool] = None, output_hidden_states: Optional[bool] = None, return_dict: Optional[bool] = None, training: Optional[bool] = False, **kwargs) -> Union[TFBaseModelOutput, Tuple[tf.Tensor]]: ...
    def serving_output(self, output): ...

class BiasLayer(tf.keras.layers.Layer):
    """
    Bias as a layer. It is used for serialization purposes: `tf.keras.Model.save_weights` stores on a per-layer basis,
    so all weights have to be registered in a layer.
    """
    bias: Incomplete
    def __init__(self, shape, initializer, trainable, name, **kwargs) -> None: ...
    def call(self, x): ...

class TFBartForConditionalGeneration(TFBartPretrainedModel, TFCausalLanguageModelingLoss):
    model: Incomplete
    use_cache: Incomplete
    bias_layer: Incomplete
    def __init__(self, config, load_weight_prefix: Incomplete | None = None, *inputs, **kwargs) -> None: ...
    def get_decoder(self): ...
    def get_encoder(self): ...
    def get_output_embeddings(self): ...
    def set_output_embeddings(self, value) -> None: ...
    def get_bias(self): ...
    def set_bias(self, value) -> None: ...
    def call(self, input_ids: Optional[TFModelInputType] = None, attention_mask: Optional[Union[np.ndarray, tf.Tensor]] = None, decoder_input_ids: Optional[Union[np.ndarray, tf.Tensor]] = None, decoder_attention_mask: Optional[Union[np.ndarray, tf.Tensor]] = None, decoder_position_ids: Optional[Union[np.ndarray, tf.Tensor]] = None, head_mask: Optional[Union[np.ndarray, tf.Tensor]] = None, decoder_head_mask: Optional[Union[np.ndarray, tf.Tensor]] = None, cross_attn_head_mask: Optional[Union[np.ndarray, tf.Tensor]] = None, encoder_outputs: Optional[TFBaseModelOutput] = None, past_key_values: Optional[Tuple[Tuple[Union[np.ndarray, tf.Tensor]]]] = None, inputs_embeds: Optional[Union[np.ndarray, tf.Tensor]] = None, decoder_inputs_embeds: Optional[Union[np.ndarray, tf.Tensor]] = None, use_cache: Optional[bool] = None, output_attentions: Optional[bool] = None, output_hidden_states: Optional[bool] = None, return_dict: Optional[bool] = None, labels: Optional[tf.Tensor] = None, training: Optional[bool] = False) -> Union[TFSeq2SeqLMOutput, Tuple[tf.Tensor]]:
        """
        labels (`tf.Tensor` of shape `(batch_size, sequence_length)`, *optional*):
            Labels for computing the masked language modeling loss. Indices should either be in `[0, ...,
            config.vocab_size]` or -100 (see `input_ids` docstring). Tokens with indices set to `-100` are ignored
            (masked), the loss is only computed for the tokens with labels in `[0, ..., config.vocab_size]`.

        Returns:

        """
    def serving_output(self, output): ...
    def prepare_inputs_for_generation(self, decoder_input_ids, past_key_values: Incomplete | None = None, attention_mask: Incomplete | None = None, decoder_attention_mask: Incomplete | None = None, head_mask: Incomplete | None = None, decoder_head_mask: Incomplete | None = None, cross_attn_head_mask: Incomplete | None = None, use_cache: Incomplete | None = None, encoder_outputs: Incomplete | None = None, **kwargs): ...
    def prepare_decoder_input_ids_from_labels(self, labels: tf.Tensor): ...

class TFBartForSequenceClassification(TFBartPretrainedModel, TFSequenceClassificationLoss):
    @property
    def dummy_inputs(self): ...
    model: Incomplete
    classification_head: Incomplete
    def __init__(self, config: BartConfig, load_weight_prefix: Incomplete | None = None, *inputs, **kwargs) -> None: ...
    def call(self, input_ids: Optional[TFModelInputType] = None, attention_mask: Optional[Union[np.ndarray, tf.Tensor]] = None, decoder_input_ids: Optional[Union[np.ndarray, tf.Tensor]] = None, decoder_attention_mask: Optional[Union[np.ndarray, tf.Tensor]] = None, decoder_position_ids: Optional[Union[np.ndarray, tf.Tensor]] = None, head_mask: Optional[Union[np.ndarray, tf.Tensor]] = None, decoder_head_mask: Optional[Union[np.ndarray, tf.Tensor]] = None, cross_attn_head_mask: Optional[Union[np.ndarray, tf.Tensor]] = None, encoder_outputs: Optional[TFBaseModelOutput] = None, past_key_values: Optional[Tuple[Tuple[Union[np.ndarray, tf.Tensor]]]] = None, inputs_embeds: Optional[Union[np.ndarray, tf.Tensor]] = None, decoder_inputs_embeds: Optional[Union[np.ndarray, tf.Tensor]] = None, use_cache: Optional[bool] = None, output_attentions: Optional[bool] = None, output_hidden_states: Optional[bool] = None, return_dict: Optional[bool] = None, labels: Optional[tf.Tensor] = None, training: Optional[bool] = False) -> Union[TFSeq2SeqSequenceClassifierOutput, Tuple[tf.Tensor]]:
        """
        labels (`tf.Tensor` of shape `(batch_size, sequence_length)`, *optional*):
            Labels for computing the sequence classification/regression loss. Indices should be in `[0, ...,
            config.num_labels - 1]`. If `config.num_labels > 1` a classification loss is computed (Cross-Entropy).

        Returns:
        """
    def serving_output(self, output): ...
