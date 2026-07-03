import numpy as np
import tensorflow as tf
from ...activations_tf import get_tf_activation as get_tf_activation
from ...modeling_tf_outputs import TFBaseModelOutput as TFBaseModelOutput, TFBaseModelOutputWithPastAndCrossAttentions as TFBaseModelOutputWithPastAndCrossAttentions, TFSeq2SeqLMOutput as TFSeq2SeqLMOutput, TFSeq2SeqModelOutput as TFSeq2SeqModelOutput
from ...modeling_tf_utils import TFCausalLanguageModelingLoss as TFCausalLanguageModelingLoss, TFModelInputType as TFModelInputType, TFPreTrainedModel as TFPreTrainedModel, keras_serializable as keras_serializable, unpack_inputs as unpack_inputs
from ...tf_utils import shape_list as shape_list, stable_softmax as stable_softmax
from ...utils import add_start_docstrings as add_start_docstrings, add_start_docstrings_to_model_forward as add_start_docstrings_to_model_forward, logging as logging, replace_return_docstrings as replace_return_docstrings
from .configuration_whisper import WhisperConfig as WhisperConfig
from _typeshed import Incomplete
from typing import Dict, Optional, Tuple, Union

logger: Incomplete
TF_WHISPER_PRETRAINED_MODEL_ARCHIVE_LIST: Incomplete
LARGE_NEGATIVE: float

def shift_tokens_right(input_ids: tf.Tensor, pad_token_id: int, decoder_start_token_id: int): ...

class TFWhisperPositionalEmbedding(tf.keras.layers.Layer):
    num_positions: Incomplete
    embedding_dim: Incomplete
    padding_idx: Incomplete
    def __init__(self, num_positions: int, embedding_dim: int, padding_idx: Optional[int] = None, **kwargs) -> None: ...
    weight: Incomplete
    def build(self, input_shape) -> None: ...
    def call(self, input_ids, past_key_values_length: int = 0): ...

class TFWhisperAttention(tf.keras.layers.Layer):
    """Multi-headed attention from 'Attention Is All You Need' paper"""
    embed_dim: Incomplete
    num_heads: Incomplete
    dropout: Incomplete
    head_dim: Incomplete
    scaling: Incomplete
    is_decoder: Incomplete
    k_proj: Incomplete
    v_proj: Incomplete
    q_proj: Incomplete
    out_proj: Incomplete
    def __init__(self, embed_dim: int, num_heads: int, dropout: float = 0.0, is_decoder: bool = False, bias: bool = True, **kwargs) -> None: ...
    def call(self, hidden_states: tf.Tensor, key_value_states: Optional[tf.Tensor] = None, past_key_value: Optional[Tuple[Tuple[tf.Tensor]]] = None, attention_mask: Optional[tf.Tensor] = None, layer_head_mask: Optional[tf.Tensor] = None, training: Optional[bool] = False) -> Tuple[tf.Tensor, Optional[tf.Tensor]]:
        """Input shape: Batch x Time x Channel"""

class TFWhisperEncoderLayer(tf.keras.layers.Layer):
    embed_dim: Incomplete
    self_attn: Incomplete
    self_attn_layer_norm: Incomplete
    dropout: Incomplete
    activation_fn: Incomplete
    activation_dropout: Incomplete
    fc1: Incomplete
    fc2: Incomplete
    final_layer_norm: Incomplete
    def __init__(self, config: WhisperConfig, **kwargs) -> None: ...
    def call(self, hidden_states: tf.Tensor, attention_mask: tf.Tensor, layer_head_mask: tf.Tensor, training: bool = False):
        """
        Args:
            hidden_states (`tf.Tensor`): input to the layer of shape `(seq_len, batch, embed_dim)`
            attention_mask (`tf.Tensor`): attention mask of size
                `(batch, 1, tgt_len, src_len)` where padding elements are indicated by very large negative values.
            layer_head_mask (`tf.Tensor`): mask for attention heads in a given layer of size
                `(encoder_attention_heads,)`
        """

class TFWhisperDecoderLayer(tf.keras.layers.Layer):
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
    def __init__(self, config: WhisperConfig, **kwargs) -> None: ...
    def call(self, hidden_states, attention_mask: Optional[tf.Tensor] = None, encoder_hidden_states: Optional[tf.Tensor] = None, encoder_attention_mask: Optional[tf.Tensor] = None, layer_head_mask: Optional[tf.Tensor] = None, cross_attn_layer_head_mask: Optional[tf.Tensor] = None, past_key_value: Optional[Tuple[tf.Tensor]] = None, training: bool = False) -> Tuple[tf.Tensor, tf.Tensor, Tuple[Tuple[tf.Tensor]]]:
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

class TFWhisperPreTrainedModel(TFPreTrainedModel):
    config_class = WhisperConfig
    base_model_prefix: str
    main_input_name: str
    @property
    def dummy_inputs(self) -> Dict[str, tf.Tensor]:
        """
        Dummy inputs to build the network.

        Returns:
            `Dict[str, tf.Tensor]`: The dummy inputs.
        """
    def serving(self, inputs): ...

WHISPER_START_DOCSTRING: str
WHISPER_INPUTS_DOCSTRING: str

class TFWhisperEncoder(tf.keras.layers.Layer):
    config_class = WhisperConfig
    config: Incomplete
    layerdrop: Incomplete
    embed_dim: Incomplete
    num_mel_bins: Incomplete
    padding_idx: Incomplete
    max_source_positions: Incomplete
    embed_scale: Incomplete
    conv1: Incomplete
    conv2: Incomplete
    embed_positions: Incomplete
    encoder_layers: Incomplete
    layer_norm: Incomplete
    dropout: Incomplete
    def __init__(self, config: WhisperConfig, **kwargs) -> None: ...
    def call(self, input_features: Incomplete | None = None, head_mask: Incomplete | None = None, output_attentions: Incomplete | None = None, output_hidden_states: Incomplete | None = None, return_dict: Incomplete | None = None, training: bool = False):
        """
        Args:
            input_features (`tf.Tensor` of shape `(batch_size, feature_size, sequence_length)`):
                Float values of fbank features extracted from the raw speech waveform. Raw speech waveform can be
                obtained by loading a `.flac` or `.wav` audio file into an array of type `List[float]` or a
                `numpy.ndarray`, *e.g.* via the soundfile library (`pip install soundfile`). To prepare the array into
                `input_features`, the [`AutoFeatureExtractor`] should be used for extracting the fbank features,
                padding and conversion into a tensor of type `tf.Tensor`. See [`~WhisperFeatureExtractor.__call__`]
            head_mask (`tf.Tensor` of shape `(encoder_layers, encoder_attention_heads)`, *optional*):
                Mask to nullify selected heads of the attention modules. Mask values selected in `[0, 1]`:

                - 1 indicates the head is **not masked**,
                - 0 indicates the head is **masked**.

            output_attentions (`bool`, *optional*):
                Whether or not to return the attentions tensors of all attention layers. See `attentions` under
                returned tensors for more detail.
            output_hidden_states (`bool`, *optional*):
                Whether or not to return the hidden states of all layers. See `hidden_states` under returned tensors
                for more detail.
            return_dict (`bool`, *optional*):
                Whether or not to return a [`~utils.ModelOutput`] instead of a plain tuple.
        """

class TFWhisperDecoder(tf.keras.layers.Layer):
    config_class = WhisperConfig
    config: Incomplete
    dropout: Incomplete
    layerdrop: Incomplete
    padding_idx: Incomplete
    max_target_positions: Incomplete
    max_source_positions: Incomplete
    embed_scale: Incomplete
    embed_tokens: Incomplete
    embed_positions: Incomplete
    decoder_layers: Incomplete
    layer_norm: Incomplete
    def __init__(self, config: WhisperConfig, **kwargs) -> None: ...
    def get_input_embeddings(self): ...
    def set_input_embeddings(self, value) -> None: ...
    def call(self, input_ids: Incomplete | None = None, attention_mask: Incomplete | None = None, position_ids: Incomplete | None = None, encoder_hidden_states: Incomplete | None = None, head_mask: Incomplete | None = None, cross_attn_head_mask: Incomplete | None = None, past_key_values: Incomplete | None = None, inputs_embeds: Incomplete | None = None, use_cache: Incomplete | None = None, output_attentions: Incomplete | None = None, output_hidden_states: Incomplete | None = None, return_dict: Incomplete | None = None, training: bool = False):
        """
        Args:
            input_ids (`tf.Tensor` of shape `(batch_size, sequence_length)`):
                Indices of input sequence tokens in the vocabulary. Padding will be ignored by default should you
                provide it.

                Indices can be obtained using [`WhisperTokenizer`]. See [`PreTrainedTokenizer.encode`] and
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
            head_mask (`tf.Tensor` of shape `(decoder_layers, decoder_attention_heads)`, *optional*):
                Mask to nullify selected heads of the attention modules. Mask values selected in `[0, 1]`:

                - 1 indicates the head is **not masked**,
                - 0 indicates the head is **masked**.

            cross_attn_head_mask (`tf.Tensor` of shape `(decoder_layers, decoder_attention_heads)`, *optional*):
                Mask to nullify selected heads of the attention modules in encoder to avoid performing cross-attention
                on hidden heads. Mask values selected in `[0, 1]`:

                - 1 indicates the head is **not masked**,
                - 0 indicates the head is **masked**.

            past_key_values (`tuple(tuple(tf.Tensor))`, *optional*, returned when `use_cache=True` is passed or when `config.use_cache=True`):
                Tuple of `tuple(tf.Tensor)` of length `config.n_layers`, with each tuple having 2 tensors of shape
                `(batch_size, num_heads, sequence_length, embed_size_per_head)`) and 2 additional tensors of shape
                `(batch_size, num_heads, encoder_sequence_length, embed_size_per_head)`.

                Contains pre-computed hidden-states (key and values in the self-attention blocks and in the
                cross-attention blocks) that can be used (see `past_key_values` input) to speed up sequential decoding.

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

class TFWhisperMainLayer(tf.keras.layers.Layer):
    config_class = WhisperConfig
    config: Incomplete
    encoder: Incomplete
    decoder: Incomplete
    def __init__(self, config: WhisperConfig, **kwargs) -> None: ...
    def get_input_embeddings(self): ...
    def set_input_embeddings(self, value) -> None: ...
    def get_encoder(self): ...
    def get_decoder(self): ...
    def call(self, input_features: Incomplete | None = None, decoder_input_ids: Incomplete | None = None, decoder_attention_mask: Incomplete | None = None, decoder_position_ids: Incomplete | None = None, head_mask: Incomplete | None = None, decoder_head_mask: Incomplete | None = None, cross_attn_head_mask: Incomplete | None = None, encoder_outputs: Incomplete | None = None, past_key_values: Incomplete | None = None, decoder_inputs_embeds: Incomplete | None = None, use_cache: Incomplete | None = None, output_attentions: Incomplete | None = None, output_hidden_states: Incomplete | None = None, return_dict: Incomplete | None = None, training: bool = False):
        '''
        Returns:

        Example:

         ```python
         >>> import tensorflow as tf
         >>> from transformers import TFWhisperModel, AutoFeatureExtractor
         >>> from datasets import load_dataset

         >>> model = TFWhisperModel.from_pretrained("openai/whisper-base")
         >>> feature_extractor = AutoFeatureExtractor.from_pretrained("openai/whisper-base")
         >>> ds = load_dataset("hf-internal-testing/librispeech_asr_dummy", "clean", split="validation")
         >>> inputs = feature_extractor(ds[0]["audio"]["array"], return_tensors="tf")
         >>> input_features = inputs.input_features
         >>> decoder_input_ids = tf.convert_to_tensor([[1, 1]]) * model.config.decoder_start_token_id
         >>> last_hidden_state = model(input_features, decoder_input_ids=decoder_input_ids).last_hidden_state
         >>> list(last_hidden_state.shape)
         [1, 2, 512]
         ```'''

class TFWhisperModel(TFWhisperPreTrainedModel):
    model: Incomplete
    def __init__(self, config: WhisperConfig, **kwargs) -> None: ...
    def get_input_embeddings(self): ...
    def set_input_embeddings(self, value) -> None: ...
    def get_encoder(self): ...
    def get_decoder(self): ...
    def decoder(self): ...
    def encoder(self): ...
    def call(self, input_features: Optional[TFModelInputType] = None, decoder_input_ids: Optional[Union[np.ndarray, tf.Tensor]] = None, decoder_attention_mask: Optional[Union[np.ndarray, tf.Tensor]] = None, decoder_position_ids: Optional[Union[np.ndarray, tf.Tensor]] = None, head_mask: Optional[Union[np.ndarray, tf.Tensor]] = None, decoder_head_mask: Optional[Union[np.ndarray, tf.Tensor]] = None, cross_attn_head_mask: Optional[Union[np.ndarray, tf.Tensor]] = None, encoder_outputs: Optional[Tuple[Tuple[Union[np.ndarray, tf.Tensor]]]] = None, past_key_values: Optional[Tuple[Tuple[Union[np.ndarray, tf.Tensor]]]] = None, decoder_inputs_embeds: Optional[Tuple[Union[np.ndarray, tf.Tensor]]] = None, use_cache: Optional[bool] = None, output_attentions: Optional[bool] = None, output_hidden_states: Optional[bool] = None, return_dict: Optional[bool] = None, training: bool = False) -> Union[Tuple[tf.Tensor], TFSeq2SeqModelOutput]:
        '''
        Returns:

        Example:

         ```python
         >>> import tensorflow as tf
         >>> from transformers import TFWhisperModel, AutoFeatureExtractor
         >>> from datasets import load_dataset

         >>> model = TFWhisperModel.from_pretrained("openai/whisper-base")
         >>> feature_extractor = AutoFeatureExtractor.from_pretrained("openai/whisper-base")
         >>> ds = load_dataset("hf-internal-testing/librispeech_asr_dummy", "clean", split="validation")
         >>> inputs = feature_extractor(ds[0]["audio"]["array"], return_tensors="tf")
         >>> input_features = inputs.input_features
         >>> decoder_input_ids = tf.convert_to_tensor([[1, 1]]) * model.config.decoder_start_token_id
         >>> last_hidden_state = model(input_features, decoder_input_ids=decoder_input_ids).last_hidden_state
         >>> list(last_hidden_state.shape)
         [1, 2, 512]
         ```'''
    def serving_output(self, output): ...

class TFWhisperForConditionalGeneration(TFWhisperPreTrainedModel, TFCausalLanguageModelingLoss):
    base_model_prefix: str
    model: Incomplete
    def __init__(self, config: WhisperConfig, **kwargs) -> None: ...
    def get_encoder(self): ...
    def get_decoder(self): ...
    def get_output_embeddings(self): ...
    def set_output_embeddings(self, value) -> None: ...
    def resize_token_embeddings(self, new_num_tokens: int) -> tf.keras.layers.Embedding: ...
    def call(self, input_features: Optional[TFModelInputType] = None, decoder_input_ids: Optional[Union[np.ndarray, tf.Tensor]] = None, decoder_attention_mask: Optional[Union[np.ndarray, tf.Tensor]] = None, decoder_position_ids: Optional[Union[np.ndarray, tf.Tensor]] = None, head_mask: Optional[Union[np.ndarray, tf.Tensor]] = None, decoder_head_mask: Optional[Union[np.ndarray, tf.Tensor]] = None, cross_attn_head_mask: Optional[Union[np.ndarray, tf.Tensor]] = None, encoder_outputs: Optional[Tuple[Tuple[Union[np.ndarray, tf.Tensor]]]] = None, past_key_values: Optional[Tuple[Tuple[Union[np.ndarray, tf.Tensor]]]] = None, decoder_inputs_embeds: Optional[Tuple[Union[np.ndarray, tf.Tensor]]] = None, labels: Optional[Union[np.ndarray, tf.Tensor]] = None, use_cache: Optional[bool] = None, output_attentions: Optional[bool] = None, output_hidden_states: Optional[bool] = None, return_dict: Optional[bool] = None, training: bool = False) -> Union[Tuple[tf.Tensor], TFSeq2SeqLMOutput]:
        '''
        labels (`tf.Tensor` of shape `(batch_size, sequence_length)`, *optional*):
            Labels for computing the language modeling loss. Indices should either be in `[0, ..., config.vocab_size]`
            or -100 (see `input_ids` docstring). Tokens with indices set to `-100` are ignored (masked), the loss is
            only computed for the tokens with labels in `[0, ..., config.vocab_size]`.

        Returns:

        Example:

        ```python
        >>> import tensorflow as tf
        >>> from transformers import AutoProcessor, TFWhisperForConditionalGeneration
        >>> from datasets import load_dataset

        >>> processor = AutoProcessor.from_pretrained("openai/whisper-tiny.en")
        >>> model = TFWhisperForConditionalGeneration.from_pretrained("openai/whisper-tiny.en")

        >>> ds = load_dataset("hf-internal-testing/librispeech_asr_dummy", "clean", split="validation")

        >>> inputs = processor(ds[0]["audio"]["array"], return_tensors="tf")
        >>> input_features = inputs.input_features

        >>> generated_ids = model.generate(input_ids=input_features)

        >>> transcription = processor.batch_decode(generated_ids, skip_special_tokens=True)[0]
        >>> transcription
        \' Mr. Quilter is the apostle of the middle classes, and we are glad to welcome his gospel.\'
        ```'''
    def serving_output(self, output): ...
    def prepare_inputs_for_generation(self, decoder_input_ids, past_key_values: Incomplete | None = None, use_cache: Incomplete | None = None, encoder_outputs: Incomplete | None = None, attention_mask: Incomplete | None = None, decoder_attention_mask: Incomplete | None = None, **kwargs): ...
