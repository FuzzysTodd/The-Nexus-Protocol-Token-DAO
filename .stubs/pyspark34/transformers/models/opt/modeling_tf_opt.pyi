import numpy as np
import tensorflow as tf
from ...activations_tf import get_tf_activation as get_tf_activation
from ...modeling_tf_outputs import TFBaseModelOutputWithPast as TFBaseModelOutputWithPast, TFCausalLMOutputWithPast as TFCausalLMOutputWithPast
from ...modeling_tf_utils import DUMMY_INPUTS as DUMMY_INPUTS, TFCausalLanguageModelingLoss as TFCausalLanguageModelingLoss, TFModelInputType as TFModelInputType, TFPreTrainedModel as TFPreTrainedModel, TFSharedEmbeddings as TFSharedEmbeddings, keras_serializable as keras_serializable, unpack_inputs as unpack_inputs
from ...tf_utils import shape_list as shape_list, stable_softmax as stable_softmax
from ...utils import add_code_sample_docstrings as add_code_sample_docstrings, add_start_docstrings as add_start_docstrings, add_start_docstrings_to_model_forward as add_start_docstrings_to_model_forward, logging as logging, replace_return_docstrings as replace_return_docstrings
from .configuration_opt import OPTConfig as OPTConfig
from _typeshed import Incomplete
from typing import Optional, Tuple, Union

logger: Incomplete
LARGE_NEGATIVE: float

class TFOPTLearnedPositionalEmbedding(TFSharedEmbeddings):
    """
    This module learns positional embeddings up to a fixed maximum size.
    """
    offset: int
    def __init__(self, num_embeddings: int, embedding_dim: int, **kwargs) -> None: ...
    def call(self, attention_mask, past_key_values_length: int = 0):
        """`input_ids_shape` is expected to be [bsz x seqlen]."""

class TFOPTAttention(tf.keras.layers.Layer):
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

class TFOPTDecoderLayer(tf.keras.layers.Layer):
    do_layer_norm_before: Incomplete
    embed_dim: Incomplete
    self_attn: Incomplete
    dropout: Incomplete
    activation_fn: Incomplete
    self_attn_layer_norm: Incomplete
    fc1: Incomplete
    fc2: Incomplete
    final_layer_norm: Incomplete
    def __init__(self, config: OPTConfig, **kwargs) -> None: ...
    def call(self, hidden_states: tf.Tensor, attention_mask: Optional[Union[np.ndarray, tf.Tensor]] = None, layer_head_mask: Optional[tf.Tensor] = None, past_key_value: Optional[Tuple[Tuple[Union[np.ndarray, tf.Tensor]]]] = None, training: Optional[bool] = False, output_attentions: Optional[bool] = False, use_cache: Optional[bool] = False) -> Tuple[tf.Tensor, tf.Tensor, Tuple[Tuple[tf.Tensor]]]:
        """
        Args:
            hidden_states (`tf.Tensor`): input to the layer of shape `(seq_len, batch, embed_dim)`
            attention_mask (`tf.Tensor`, *optional*): attention mask of size
                `(batch, 1, tgt_len, src_len)` where padding elements are indicated by very large negative values.
            layer_head_mask (`tf.Tensor`, *optional*): mask for attention heads in a given layer of size
                `(decoder_attention_heads,)`
            past_key_value (`Tuple(tf.Tensor)`, *optional*): cached past key and value projection states
            training (`bool`, *optional*, defaults to `False`):
                Whether or not to use the model in training mode (some modules like dropout modules have different
                behaviors between training and evaluation).
        """

OPT_START_DOCSTRING: str

class TFOPTPreTrainedModel(TFPreTrainedModel):
    """
    TFOPT Pretrained Model that inheritates from transformers.TFPreTrainedModel

    Args:
        config: OPTConfig
    """
    config_class = OPTConfig
    base_model_prefix: str
    @property
    def dummy_inputs(self): ...
    def serving(self, inputs): ...

OPT_INPUTS_DOCSTRING: str

class TFOPTDecoder(tf.keras.layers.Layer):
    config_class = OPTConfig
    config: Incomplete
    padding_idx: Incomplete
    layerdrop: Incomplete
    embed_tokens: Incomplete
    embed_positions: Incomplete
    final_layer_norm: Incomplete
    project_out: Incomplete
    project_in: Incomplete
    layers: Incomplete
    dropout: Incomplete
    def __init__(self, config: OPTConfig, load_weight_prefix: Incomplete | None = None, **kwargs) -> None: ...
    def get_embed_tokens(self): ...
    def set_embed_tokens(self, embed_tokens) -> None: ...
    def set_input_embeddings(self, new_embeddings) -> None: ...
    def get_input_embeddings(self): ...
    def call(self, input_ids: Optional[TFModelInputType] = None, inputs_embeds: Optional[Union[np.ndarray, tf.Tensor]] = None, attention_mask: Optional[Union[np.ndarray, tf.Tensor]] = None, head_mask: Optional[Union[np.ndarray, tf.Tensor]] = None, past_key_values: Optional[Tuple[Tuple[Union[np.ndarray, tf.Tensor]]]] = None, use_cache: Optional[bool] = None, output_attentions: Optional[bool] = None, output_hidden_states: Optional[bool] = None, return_dict: Optional[bool] = None, training: Optional[bool] = False) -> Union[TFBaseModelOutputWithPast, Tuple[tf.Tensor]]:
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

            head_mask (`tf.Tensor` of shape `(decoder_layers, decoder_attention_heads)`, *optional*):
                Mask to nullify selected heads of the attention modules. Mask values selected in `[0, 1]`:

                - 1 indicates the head is **not masked**,
                - 0 indicates the head is **masked**.

            past_key_values (`Tuple[Tuple[tf.Tensor]]` of length `config.n_layers` with each tuple having 2 tuples each of which has 2 tensors of shape `(batch_size, num_heads, sequence_length - 1, embed_size_per_head)`):
                Contains precomputed key and value hidden-states of the attention blocks. Can be used to speed up
                decoding.

                If `past_key_values` are used, the user can optionally input only the last `decoder_input_ids` (those
                that don't have their past key value states given to this model) of shape `(batch_size, 1)` instead of
                all `decoder_input_ids` of shape `(batch_size, sequence_length)`.
            inputs_embeds (`tf.Tensor` of
                shape `(batch_size, sequence_length, hidden_size)`, *optional*): Optionally, instead of passing
                `input_ids` you can choose to directly pass an embedded representation. This is useful if you want more
                control over how to convert `input_ids` indices into associated vectors than the model's internal
                embedding lookup matrix.
            output_attentions (`bool`, *optional*):
                Whether or not to return the attentions tensors of all attention layers. See `attentions` under
                returned tensors for more detail.
            output_hidden_states (`bool`, *optional*):
                Whether or not to return the hidden states of all layers. See `hidden_states` under returned tensors
                for more detail.
            return_dict (`bool`, *optional*):
                Whether or not to return a [`~utils.ModelOutput`] instead of a plain tuple.
            training (`bool`, *optional*, defaults to `False`):
                Whether or not to use the model in training mode (some modules like dropout modules have different
                behaviors between training and evaluation).
        """

class TFOPTMainLayer(tf.keras.layers.Layer):
    config_class = OPTConfig
    config: Incomplete
    decoder: Incomplete
    def __init__(self, config: OPTConfig, **kwargs) -> None: ...
    def get_input_embeddings(self): ...
    def set_input_embeddings(self, new_embeddings) -> None: ...
    def call(self, input_ids: Optional[TFModelInputType] = None, attention_mask: Optional[Union[np.ndarray, tf.Tensor]] = None, head_mask: Optional[Union[np.ndarray, tf.Tensor]] = None, past_key_values: Optional[Tuple[Tuple[Union[np.ndarray, tf.Tensor]]]] = None, inputs_embeds: Optional[Union[np.ndarray, tf.Tensor]] = None, use_cache: Optional[bool] = None, output_attentions: Optional[bool] = None, output_hidden_states: Optional[bool] = None, return_dict: Optional[bool] = None, training: Optional[bool] = False, **kwargs) -> Union[TFBaseModelOutputWithPast, Tuple[tf.Tensor]]: ...

class TFOPTModel(TFOPTPreTrainedModel):
    config_class = OPTConfig
    config: Incomplete
    model: Incomplete
    def __init__(self, config: OPTConfig, **kwargs) -> None: ...
    def get_input_embeddings(self): ...
    def set_input_embeddings(self, new_embeddings) -> None: ...
    def call(self, input_ids: Optional[TFModelInputType] = None, attention_mask: Optional[Union[np.ndarray, tf.Tensor]] = None, head_mask: Optional[Union[np.ndarray, tf.Tensor]] = None, past_key_values: Optional[Tuple[Tuple[Union[np.ndarray, tf.Tensor]]]] = None, inputs_embeds: Optional[Union[np.ndarray, tf.Tensor]] = None, use_cache: Optional[bool] = None, output_attentions: Optional[bool] = None, output_hidden_states: Optional[bool] = None, return_dict: Optional[bool] = None, training: Optional[bool] = False, **kwargs) -> Union[TFBaseModelOutputWithPast, Tuple[tf.Tensor]]: ...
    def serving_output(self, output): ...

class TFOPTForCausalLM(TFOPTPreTrainedModel, TFCausalLanguageModelingLoss):
    config_class = OPTConfig
    config: Incomplete
    model: Incomplete
    def __init__(self, config: OPTConfig, **kwargs) -> None: ...
    def get_output_embeddings(self): ...
    def prepare_inputs_for_generation(self, inputs, past_key_values: Incomplete | None = None, use_cache: Incomplete | None = None, **kwargs): ...
    def call(self, input_ids: Optional[TFModelInputType] = None, past_key_values: Optional[Tuple[Tuple[Union[np.ndarray, tf.Tensor]]]] = None, attention_mask: Optional[Union[np.ndarray, tf.Tensor]] = None, position_ids: Optional[Union[np.ndarray, tf.Tensor]] = None, head_mask: Optional[Union[np.ndarray, tf.Tensor]] = None, inputs_embeds: Optional[Union[np.ndarray, tf.Tensor]] = None, labels: Optional[Union[np.ndarray, tf.Tensor]] = None, use_cache: Optional[bool] = None, output_attentions: Optional[bool] = None, output_hidden_states: Optional[bool] = None, return_dict: Optional[bool] = None, training: Optional[bool] = False, **kwargs) -> Union[TFCausalLMOutputWithPast, Tuple[tf.Tensor]]:
        """
        Args:
            input_ids (`torch.LongTensor` of shape `(batch_size, sequence_length)`):
                Indices of input sequence tokens in the vocabulary. Padding will be ignored by default should you
                provide it.

                Indices can be obtained using [`AutoTokenizer`]. See [`PreTrainedTokenizer.encode`] and
                [`PreTrainedTokenizer.__call__`] for details.

                [What are input IDs?](../glossary#input-ids)
            attention_mask (`torch.Tensor` of shape `(batch_size, sequence_length)`, *optional*):
                Mask to avoid performing attention on padding token indices. Mask values selected in `[0, 1]`:

                - 1 for tokens that are **not masked**,
                - 0 for tokens that are **masked**.

                [What are attention masks?](../glossary#attention-mask)
            head_mask (`torch.Tensor` of shape `(num_hidden_layers, num_attention_heads)`, *optional*):
                Mask to nullify selected heads of the attention modules. Mask values selected in `[0, 1]`:

                - 1 indicates the head is **not masked**,
                - 0 indicates the head is **masked**.

            past_key_values (`tuple(tuple(torch.FloatTensor))`, *optional*, returned when `use_cache=True` is passed or when `config.use_cache=True`):
                Tuple of `tuple(torch.FloatTensor)` of length `config.n_layers`, with each tuple having 2 tensors of
                shape `(batch_size, num_heads, sequence_length, embed_size_per_head)`) and 2 additional tensors of
                shape `(batch_size, num_heads, encoder_sequence_length, embed_size_per_head)`. The two additional
                tensors are only required when the model is used as a decoder in a Sequence to Sequence model.

                Contains pre-computed hidden-states (key and values in the self-attention blocks and in the
                cross-attention blocks) that can be used (see `past_key_values` input) to speed up sequential decoding.

                If `past_key_values` are used, the user can optionally input only the last `input_ids` (those that
                don't have their past key value states given to this model) of shape `(batch_size, 1)` instead of all
                `decoder_input_ids` of shape `(batch_size, sequence_length)`.
            inputs_embeds (`torch.FloatTensor` of shape `(batch_size, sequence_length, hidden_size)`, *optional*):
                Optionally, instead of passing `input_ids` you can choose to directly pass an embedded representation.
                This is useful if you want more control over how to convert `input_ids` indices into associated vectors
                than the model's internal embedding lookup matrix.
            labels (`torch.LongTensor` of shape `(batch_size, sequence_length)`, *optional*):
                Labels for computing the masked language modeling loss. Indices should either be in `[0, ...,
                config.vocab_size]` or -100 (see `input_ids` docstring). Tokens with indices set to `-100` are ignored
                (masked), the loss is only computed for the tokens with labels in `[0, ..., config.vocab_size]`.
            use_cache (`bool`, *optional*):
                If set to `True`, `past_key_values` key value states are returned and can be used to speed up decoding
                (see `past_key_values`).
            output_attentions (`bool`, *optional*):
                Whether or not to return the attentions tensors of all attention layers. See `attentions` under
                returned tensors for more detail.
            output_hidden_states (`bool`, *optional*):
                Whether or not to return the hidden states of all layers. See `hidden_states` under returned tensors
                for more detail.
            return_dict (`bool`, *optional*):
                Whether or not to return a [`~utils.ModelOutput`] instead of a plain tuple.
        """
    def serving_output(self, output): ...
