import os
import tensorflow as tf
from ...activations_tf import get_tf_activation as get_tf_activation
from ...modeling_tf_outputs import TFBaseModelOutput as TFBaseModelOutput, TFBaseModelOutputWithPastAndCrossAttentions as TFBaseModelOutputWithPastAndCrossAttentions, TFSeq2SeqLMOutput as TFSeq2SeqLMOutput, TFSeq2SeqModelOutput as TFSeq2SeqModelOutput
from ...modeling_tf_utils import DUMMY_INPUTS as DUMMY_INPUTS, TFCausalLanguageModelingLoss as TFCausalLanguageModelingLoss, TFPreTrainedModel as TFPreTrainedModel, keras_serializable as keras_serializable, unpack_inputs as unpack_inputs
from ...tf_utils import shape_list as shape_list, stable_softmax as stable_softmax
from ...utils import ContextManagers as ContextManagers, add_code_sample_docstrings as add_code_sample_docstrings, add_end_docstrings as add_end_docstrings, add_start_docstrings as add_start_docstrings, add_start_docstrings_to_model_forward as add_start_docstrings_to_model_forward, logging as logging, replace_return_docstrings as replace_return_docstrings
from .configuration_blenderbot import BlenderbotConfig as BlenderbotConfig
from _typeshed import Incomplete
from typing import List, Optional, Tuple, Union

logger: Incomplete
LARGE_NEGATIVE: float

def shift_tokens_right(input_ids: tf.Tensor, pad_token_id: int, decoder_start_token_id: int): ...

class TFBlenderbotLearnedPositionalEmbedding(tf.keras.layers.Embedding):
    """
    This module learns positional embeddings up to a fixed maximum size.
    """
    def __init__(self, num_embeddings: int, embedding_dim: int, **kwargs) -> None: ...
    def call(self, input_shape: tf.TensorShape, past_key_values_length: int = 0, position_ids: Optional[tf.Tensor] = None):
        """Input is expected to be of size [bsz x seqlen]."""

class TFBlenderbotAttention(tf.keras.layers.Layer):
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

class TFBlenderbotEncoderLayer(tf.keras.layers.Layer):
    embed_dim: Incomplete
    self_attn: Incomplete
    self_attn_layer_norm: Incomplete
    dropout: Incomplete
    activation_fn: Incomplete
    activation_dropout: Incomplete
    fc1: Incomplete
    fc2: Incomplete
    final_layer_norm: Incomplete
    def __init__(self, config: BlenderbotConfig, **kwargs) -> None: ...
    def call(self, hidden_states: tf.Tensor, attention_mask: tf.Tensor, layer_head_mask: tf.Tensor, training: Optional[bool] = False):
        """
        Args:
            hidden_states (`tf.Tensor`): input to the layer of shape *(seq_len, batch, embed_dim)*
            attention_mask (`tf.Tensor`): attention mask of size
                *(batch, 1, tgt_len, src_len)* where padding elements are indicated by very large negative values.
            layer_head_mask (`tf.Tensor`): mask for attention heads in a given layer of size
                *(encoder_attention_heads,)*
        """

class TFBlenderbotDecoderLayer(tf.keras.layers.Layer):
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
    def __init__(self, config: BlenderbotConfig, **kwargs) -> None: ...
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

class TFBlenderbotPreTrainedModel(TFPreTrainedModel):
    config_class = BlenderbotConfig
    base_model_prefix: str
    @property
    def dummy_inputs(self): ...
    def serving(self, inputs): ...

BLENDERBOT_START_DOCSTRING: str
BLENDERBOT_GENERATION_EXAMPLE: str
BLENDERBOT_INPUTS_DOCSTRING: str

class TFBlenderbotEncoder(tf.keras.layers.Layer):
    config_class = BlenderbotConfig
    config: Incomplete
    dropout: Incomplete
    layerdrop: Incomplete
    padding_idx: Incomplete
    max_source_positions: Incomplete
    embed_scale: Incomplete
    embed_tokens: Incomplete
    embed_positions: Incomplete
    layers: Incomplete
    layer_norm: Incomplete
    def __init__(self, config: BlenderbotConfig, embed_tokens: Optional[tf.keras.layers.Embedding] = None, **kwargs) -> None: ...
    def get_embed_tokens(self): ...
    def set_embed_tokens(self, embed_tokens) -> None: ...
    def call(self, input_ids: Incomplete | None = None, inputs_embeds: Incomplete | None = None, attention_mask: Incomplete | None = None, head_mask: Incomplete | None = None, output_attentions: Incomplete | None = None, output_hidden_states: Incomplete | None = None, return_dict: Incomplete | None = None, training: bool = False):
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
                returned tensors for more detail. This argument can be used only in eager mode, in graph mode the value
                in the config will be used instead.
            output_hidden_states (`bool`, *optional*):
                Whether or not to return the hidden states of all layers. See `hidden_states` under returned tensors
                for more detail. This argument can be used only in eager mode, in graph mode the value in the config
                will be used instead.
            return_dict (`bool`, *optional*):
                Whether or not to return a [`~utils.ModelOutput`] instead of a plain tuple. This argument can be used
                in eager mode, in graph mode the value will always be set to True.
            training (`bool`, *optional*, defaults to `False`):
                Whether or not to use the model in training mode (some modules like dropout modules have different
                behaviors between training and evaluation).
        """

class TFBlenderbotDecoder(tf.keras.layers.Layer):
    config_class = BlenderbotConfig
    config: Incomplete
    padding_idx: Incomplete
    embed_tokens: Incomplete
    layerdrop: Incomplete
    embed_positions: Incomplete
    embed_scale: Incomplete
    layers: Incomplete
    layer_norm: Incomplete
    dropout: Incomplete
    def __init__(self, config: BlenderbotConfig, embed_tokens: Optional[tf.keras.layers.Embedding] = None, **kwargs) -> None: ...
    def get_embed_tokens(self): ...
    def set_embed_tokens(self, embed_tokens) -> None: ...
    def call(self, input_ids: Incomplete | None = None, inputs_embeds: Incomplete | None = None, attention_mask: Incomplete | None = None, position_ids: Incomplete | None = None, encoder_hidden_states: Incomplete | None = None, encoder_attention_mask: Incomplete | None = None, head_mask: Incomplete | None = None, cross_attn_head_mask: Incomplete | None = None, past_key_values: Incomplete | None = None, use_cache: Incomplete | None = None, output_attentions: Incomplete | None = None, output_hidden_states: Incomplete | None = None, return_dict: Incomplete | None = None, training: bool = False):
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
                returned tensors for more detail. This argument can be used only in eager mode, in graph mode the value
                in the config will be used instead.
            output_hidden_states (`bool`, *optional*):
                Whether or not to return the hidden states of all layers. See `hidden_states` under returned tensors
                for more detail. This argument can be used only in eager mode, in graph mode the value in the config
                will be used instead.
            return_dict (`bool`, *optional*):
                Whether or not to return a [`~utils.ModelOutput`] instead of a plain tuple. This argument can be used
                in eager mode, in graph mode the value will always be set to True.
            training (`bool`, *optional*, defaults to `False`):
                Whether or not to use the model in training mode (some modules like dropout modules have different
                behaviors between training and evaluation).
        """

class TFBlenderbotMainLayer(tf.keras.layers.Layer):
    config_class = BlenderbotConfig
    config: Incomplete
    shared: Incomplete
    encoder: Incomplete
    decoder: Incomplete
    def __init__(self, config: BlenderbotConfig, **kwargs) -> None: ...
    def get_input_embeddings(self): ...
    def set_input_embeddings(self, new_embeddings) -> None: ...
    def call(self, input_ids: Incomplete | None = None, attention_mask: Incomplete | None = None, decoder_input_ids: Incomplete | None = None, decoder_attention_mask: Incomplete | None = None, decoder_position_ids: Incomplete | None = None, head_mask: Incomplete | None = None, decoder_head_mask: Incomplete | None = None, cross_attn_head_mask: Incomplete | None = None, encoder_outputs: Optional[Union[Tuple, TFBaseModelOutput]] = None, past_key_values: Incomplete | None = None, inputs_embeds: Incomplete | None = None, decoder_inputs_embeds: Incomplete | None = None, use_cache: Incomplete | None = None, output_attentions: Incomplete | None = None, output_hidden_states: Incomplete | None = None, return_dict: Incomplete | None = None, training: bool = False, **kwargs): ...

class TFBlenderbotModel(TFBlenderbotPreTrainedModel):
    model: Incomplete
    def __init__(self, config: BlenderbotConfig, *inputs, **kwargs) -> None: ...
    def get_encoder(self): ...
    def get_decoder(self): ...
    @classmethod
    def from_pretrained(cls, pretrained_model_name_or_path: Optional[Union[str, os.PathLike]], *model_args, **kwargs): ...
    def call(self, input_ids: Optional[tf.Tensor] = None, attention_mask: Optional[tf.Tensor] = None, decoder_input_ids: Optional[tf.Tensor] = None, decoder_attention_mask: Optional[tf.Tensor] = None, decoder_position_ids: Optional[tf.Tensor] = None, head_mask: Optional[tf.Tensor] = None, decoder_head_mask: Optional[tf.Tensor] = None, cross_attn_head_mask: Optional[tf.Tensor] = None, encoder_outputs: Optional[Union[Tuple, TFBaseModelOutput]] = None, past_key_values: Optional[List[tf.Tensor]] = None, inputs_embeds: Optional[tf.Tensor] = None, decoder_inputs_embeds: Optional[tf.Tensor] = None, use_cache: Optional[bool] = None, output_attentions: Optional[bool] = None, output_hidden_states: Optional[bool] = None, return_dict: Optional[bool] = None, training: Optional[bool] = False, **kwargs) -> Union[Tuple[tf.Tensor], TFSeq2SeqModelOutput]: ...
    def serving_output(self, output): ...

class BiasLayer(tf.keras.layers.Layer):
    """
    Bias as a layer. It is used for serialization purposes: `tf.keras.Model.save_weights` stores on a per-layer basis,
    so all weights have to be registered in a layer.
    """
    bias: Incomplete
    def __init__(self, shape, initializer, trainable, name, **kwargs) -> None: ...
    def call(self, x): ...

class TFBlenderbotForConditionalGeneration(TFBlenderbotPreTrainedModel, TFCausalLanguageModelingLoss):
    model: Incomplete
    use_cache: Incomplete
    bias_layer: Incomplete
    def __init__(self, config, *inputs, **kwargs) -> None: ...
    def get_decoder(self): ...
    def get_encoder(self): ...
    def get_output_embeddings(self): ...
    def set_output_embeddings(self, value) -> None: ...
    def get_bias(self): ...
    def set_bias(self, value) -> None: ...
    @classmethod
    def from_pretrained(cls, pretrained_model_name_or_path: Optional[Union[str, os.PathLike]], *model_args, **kwargs): ...
    def call(self, input_ids: Optional[tf.Tensor] = None, attention_mask: Optional[tf.Tensor] = None, decoder_input_ids: Optional[tf.Tensor] = None, decoder_attention_mask: Optional[tf.Tensor] = None, decoder_position_ids: Optional[tf.Tensor] = None, head_mask: Optional[tf.Tensor] = None, decoder_head_mask: Optional[tf.Tensor] = None, cross_attn_head_mask: Optional[tf.Tensor] = None, encoder_outputs: Optional[Union[Tuple, TFBaseModelOutput]] = None, past_key_values: Optional[List[tf.Tensor]] = None, inputs_embeds: Optional[tf.Tensor] = None, decoder_inputs_embeds: Optional[tf.Tensor] = None, use_cache: Optional[bool] = None, output_attentions: Optional[bool] = None, output_hidden_states: Optional[bool] = None, return_dict: Optional[bool] = None, labels: Optional[tf.Tensor] = None, training: Optional[bool] = False) -> Union[Tuple[tf.Tensor], TFSeq2SeqLMOutput]:
        """
        labels (`tf.tensor` of shape `(batch_size, sequence_length)`, *optional*):
            Labels for computing the masked language modeling loss. Indices should either be in `[0, ...,
            config.vocab_size]` or -100 (see `input_ids` docstring). Tokens with indices set to `-100` are ignored
            (masked), the loss is only computed for the tokens with labels in `[0, ..., config.vocab_size]`.

        Returns:

        """
    def serving_output(self, output): ...
    def prepare_inputs_for_generation(self, decoder_input_ids, past_key_values: Incomplete | None = None, attention_mask: Incomplete | None = None, decoder_attention_mask: Incomplete | None = None, head_mask: Incomplete | None = None, decoder_head_mask: Incomplete | None = None, cross_attn_head_mask: Incomplete | None = None, use_cache: Incomplete | None = None, encoder_outputs: Incomplete | None = None, **kwargs): ...
