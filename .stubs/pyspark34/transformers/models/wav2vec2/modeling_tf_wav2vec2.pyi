import tensorflow as tf
from ...activations_tf import get_tf_activation as get_tf_activation
from ...modeling_tf_outputs import TFBaseModelOutput as TFBaseModelOutput, TFCausalLMOutput as TFCausalLMOutput
from ...modeling_tf_utils import TFPreTrainedModel as TFPreTrainedModel, booleans_processing as booleans_processing, get_initializer as get_initializer, keras_serializable as keras_serializable, unpack_inputs as unpack_inputs
from ...tf_utils import shape_list as shape_list, stable_softmax as stable_softmax
from ...utils import ModelOutput as ModelOutput, add_start_docstrings as add_start_docstrings, add_start_docstrings_to_model_forward as add_start_docstrings_to_model_forward, logging as logging, replace_return_docstrings as replace_return_docstrings
from .configuration_wav2vec2 import Wav2Vec2Config as Wav2Vec2Config
from _typeshed import Incomplete
from dataclasses import dataclass
from typing import Any, Dict, Optional, Tuple, Union

logger: Incomplete
TF_WAV_2_VEC_2_PRETRAINED_MODEL_ARCHIVE_LIST: Incomplete
LARGE_NEGATIVE: float

@dataclass
class TFWav2Vec2BaseModelOutput(ModelOutput):
    """
    Output type of [`TFWav2Vec2BaseModelOutput`], with potential hidden states and attentions.

    Args:
        last_hidden_state (`tf.Tensor` of shape `(batch_size, sequence_length, hidden_size)`):
            Sequence of hidden-states at the output of the last layer of the model.
        extract_features (`tf.Tensor` of shape `(batch_size, sequence_length, conv_dim[-1])`):
            Sequence of extracted feature vectors of the last convolutional layer of the model.
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
    last_hidden_state: tf.Tensor = ...
    extract_features: tf.Tensor = ...
    hidden_states: Optional[Tuple[tf.Tensor]] = ...
    attentions: Optional[Tuple[tf.Tensor]] = ...
    def __init__(self, last_hidden_state, extract_features, hidden_states, attentions) -> None: ...

def input_values_processing(func, config, input_values, **kwargs):
    '''
    Process the input of each TensorFlow model including the booleans. In case of a list of symbolic inputs, each input
    has to be named accordingly to the parameters name, i.e. `input_values = tf.keras.Input(shape=(128,),
    dtype=\'float32\', name="input_values")` otherwise the order of the tensors will not be guaranteed during the
    training.

    Args:
        func (`callable`):
            The callable function of the TensorFlow model.
        config ([`PretrainedConfig`]):
            The config of the running model.
        **kwargs:
            The inputs of the model.

    Returns:
        Two lists, one for the missing layers, and another one for the unexpected layers.
    '''

class TFWav2Vec2GroupNorm(tf.keras.layers.Layer):
    """
    From tensorflow-addons https://www.tensorflow.org/addons/api_docs/python/tfa/layers/GroupNormalization
    """
    supports_masking: bool
    groups: Incomplete
    axis: Incomplete
    epsilon: Incomplete
    center: Incomplete
    scale: Incomplete
    beta_initializer: Incomplete
    gamma_initializer: Incomplete
    beta_regularizer: Incomplete
    gamma_regularizer: Incomplete
    beta_constraint: Incomplete
    gamma_constraint: Incomplete
    def __init__(self, groups: int = 32, axis: int = -1, epsilon: float = 0.001, center: bool = True, scale: bool = True, beta_initializer: tf.keras.initializers.Initializer = 'zeros', gamma_initializer: tf.keras.initializers.Initializer = 'ones', beta_regularizer: tf.keras.regularizers.Regularizer = None, gamma_regularizer: tf.keras.regularizers.Regularizer = None, beta_constraint: tf.keras.constraints.Constraint = None, gamma_constraint: tf.keras.constraints.Constraint = None, **kwargs) -> None: ...
    built: bool
    def build(self, input_shape) -> None: ...
    def call(self, inputs): ...
    def get_config(self): ...
    def compute_output_shape(self, input_shape): ...

class TFWav2Vec2WeightNormConv1D(tf.keras.layers.Conv1D):
    """Adapted from https://www.tensorflow.org/probability/api_docs/python/tfp/layers/weight_norm/WeightNorm"""
    explicit_padding: Incomplete
    filter_axis: int
    initialized: bool
    kernel_norm_axes: Incomplete
    def __init__(self, filters, kernel_size, groups, explicit_padding, **kwargs) -> None: ...
    kernel: Incomplete
    weight_v: Incomplete
    weight_g: Incomplete
    bias: Incomplete
    def build(self, input_shape) -> None: ...
    def call(self, inputs): ...

class TFWav2Vec2NoLayerNormConvLayer(tf.keras.layers.Layer):
    in_conv_dim: Incomplete
    out_conv_dim: Incomplete
    conv: Incomplete
    activation: Incomplete
    def __init__(self, config: Wav2Vec2Config, layer_id: int = 0, **kwargs: Any) -> None: ...
    def call(self, hidden_states: tf.Tensor) -> tf.Tensor: ...

class TFWav2Vec2LayerNormConvLayer(tf.keras.layers.Layer):
    in_conv_dim: Incomplete
    out_conv_dim: Incomplete
    conv: Incomplete
    layer_norm: Incomplete
    activation: Incomplete
    def __init__(self, config: Wav2Vec2Config, layer_id: int = 0, **kwargs: Any) -> None: ...
    def call(self, hidden_states: tf.Tensor) -> tf.Tensor: ...

class TFWav2Vec2GroupNormConvLayer(tf.keras.layers.Layer):
    in_conv_dim: Incomplete
    out_conv_dim: Incomplete
    conv: Incomplete
    activation: Incomplete
    layer_norm: Incomplete
    def __init__(self, config: Wav2Vec2Config, layer_id: int = 0, **kwargs: Any) -> None: ...
    def call(self, hidden_states: tf.Tensor) -> tf.Tensor: ...

class TFWav2Vec2PositionalConvEmbedding(tf.keras.layers.Layer):
    conv: Incomplete
    padding: Incomplete
    activation: Incomplete
    def __init__(self, config: Wav2Vec2Config, **kwargs: Any) -> None: ...
    def call(self, hidden_states: tf.Tensor) -> tf.Tensor: ...

class TFWav2Vec2SamePadLayer(tf.keras.layers.Layer):
    num_pad_remove: Incomplete
    def __init__(self, num_conv_pos_embeddings, **kwargs) -> None: ...
    def call(self, hidden_states): ...

class TFWav2Vec2FeatureEncoder(tf.keras.layers.Layer):
    conv_layers: Incomplete
    def __init__(self, config: Wav2Vec2Config, **kwargs: Any) -> None: ...
    def call(self, input_values): ...

class TFWav2Vec2FeatureExtractor(TFWav2Vec2FeatureEncoder):
    def __init__(self, config, **kwargs) -> None: ...

class TFWav2Vec2FeatureProjection(tf.keras.layers.Layer):
    layer_norm: Incomplete
    projection: Incomplete
    dropout: Incomplete
    def __init__(self, config: Wav2Vec2Config, **kwargs) -> None: ...
    def call(self, hidden_states: tf.Tensor, training: bool = False) -> tf.Tensor: ...

class TFWav2Vec2Attention(tf.keras.layers.Layer):
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

class TFWav2Vec2FeedForward(tf.keras.layers.Layer):
    intermediate_dropout: Incomplete
    intermediate_dense: Incomplete
    intermediate_act_fn: Incomplete
    output_dense: Incomplete
    output_dropout: Incomplete
    def __init__(self, config: Wav2Vec2Config, **kwargs) -> None: ...
    def call(self, hidden_states: tf.Tensor, training: bool = False) -> tf.Tensor: ...

class TFWav2Vec2EncoderLayer(tf.keras.layers.Layer):
    attention: Incomplete
    dropout: Incomplete
    layer_norm: Incomplete
    feed_forward: Incomplete
    final_layer_norm: Incomplete
    def __init__(self, config: Wav2Vec2Config, **kwargs) -> None: ...
    def call(self, hidden_states: tf.Tensor, attention_mask: Optional[tf.Tensor] = None, output_attentions: Optional[bool] = False, training: bool = False) -> Tuple[tf.Tensor]: ...

class TFWav2Vec2EncoderLayerStableLayerNorm(tf.keras.layers.Layer):
    attention: Incomplete
    dropout: Incomplete
    layer_norm: Incomplete
    feed_forward: Incomplete
    final_layer_norm: Incomplete
    def __init__(self, config: Wav2Vec2Config, **kwargs) -> None: ...
    def call(self, hidden_states: tf.Tensor, attention_mask: Optional[tf.Tensor] = None, output_attentions: Optional[bool] = False, training: bool = False) -> Tuple[tf.Tensor]: ...

class TFWav2Vec2Encoder(tf.keras.layers.Layer):
    config: Incomplete
    pos_conv_embed: Incomplete
    layer_norm: Incomplete
    dropout: Incomplete
    layer: Incomplete
    def __init__(self, config: Wav2Vec2Config, **kwargs) -> None: ...
    def call(self, hidden_states: tf.Tensor, attention_mask: Optional[tf.Tensor] = None, output_attentions: Optional[bool] = False, output_hidden_states: Optional[bool] = False, return_dict: Optional[bool] = True, training: Optional[bool] = False) -> Union[TFBaseModelOutput, Tuple[tf.Tensor]]: ...

class TFWav2Vec2EncoderStableLayerNorm(tf.keras.layers.Layer):
    config: Incomplete
    pos_conv_embed: Incomplete
    layer_norm: Incomplete
    dropout: Incomplete
    layer: Incomplete
    def __init__(self, config: Wav2Vec2Config, **kwargs) -> None: ...
    def call(self, hidden_states: tf.Tensor, attention_mask: Optional[tf.Tensor] = None, output_attentions: Optional[bool] = False, output_hidden_states: Optional[bool] = False, return_dict: Optional[bool] = True, training: Optional[bool] = False) -> Union[TFBaseModelOutput, Tuple[tf.Tensor]]: ...

class TFWav2Vec2MainLayer(tf.keras.layers.Layer):
    config_class = Wav2Vec2Config
    config: Incomplete
    feature_extractor: Incomplete
    feature_projection: Incomplete
    encoder: Incomplete
    def __init__(self, config: Wav2Vec2Config, **kwargs) -> None: ...
    masked_spec_embed: Incomplete
    def build(self, input_shape: tf.TensorShape): ...
    def call(self, input_values: tf.Tensor, attention_mask: Optional[tf.Tensor] = None, token_type_ids: Optional[tf.Tensor] = None, position_ids: Optional[tf.Tensor] = None, head_mask: Optional[tf.Tensor] = None, inputs_embeds: Optional[tf.Tensor] = None, output_attentions: Optional[bool] = None, output_hidden_states: Optional[bool] = None, return_dict: Optional[bool] = None, training: bool = False, **kwargs: Any): ...

class TFWav2Vec2PreTrainedModel(TFPreTrainedModel):
    """
    An abstract class to handle weights initialization and a simple interface for downloading and loading pretrained
    models.
    """
    config_class = Wav2Vec2Config
    base_model_prefix: str
    main_input_name: str
    @property
    def dummy_inputs(self) -> Dict[str, tf.Tensor]: ...
    def __init__(self, config, *inputs, **kwargs) -> None: ...
    def serving(self, inputs): ...

WAV_2_VEC_2_START_DOCSTRING: str
WAV_2_VEC_2_INPUTS_DOCSTRING: str

class TFWav2Vec2Model(TFWav2Vec2PreTrainedModel):
    config: Incomplete
    wav2vec2: Incomplete
    def __init__(self, config: Wav2Vec2Config, *inputs, **kwargs) -> None: ...
    def call(self, input_values: tf.Tensor, attention_mask: Optional[tf.Tensor] = None, token_type_ids: Optional[tf.Tensor] = None, position_ids: Optional[tf.Tensor] = None, head_mask: Optional[tf.Tensor] = None, inputs_embeds: Optional[tf.Tensor] = None, output_attentions: Optional[bool] = None, output_hidden_states: Optional[bool] = None, return_dict: Optional[bool] = None, training: bool = False) -> Union[TFBaseModelOutput, Tuple[tf.Tensor]]:
        '''

        Returns:

        Example:

        ```python
        >>> from transformers import AutoProcessor, TFWav2Vec2Model
        >>> from datasets import load_dataset
        >>> import soundfile as sf

        >>> processor = AutoProcessor.from_pretrained("facebook/wav2vec2-base-960h")
        >>> model = TFWav2Vec2Model.from_pretrained("facebook/wav2vec2-base-960h")


        >>> def map_to_array(batch):
        ...     speech, _ = sf.read(batch["file"])
        ...     batch["speech"] = speech
        ...     return batch


        >>> ds = load_dataset("hf-internal-testing/librispeech_asr_dummy", "clean", split="validation")
        >>> ds = ds.map(map_to_array)

        >>> input_values = processor(ds["speech"][0], return_tensors="tf").input_values  # Batch size 1
        >>> hidden_states = model(input_values).last_hidden_state
        ```'''
    def serving_output(self, output): ...

class TFWav2Vec2ForCTC(TFWav2Vec2PreTrainedModel):
    wav2vec2: Incomplete
    dropout: Incomplete
    lm_head: Incomplete
    def __init__(self, config: Wav2Vec2Config, *inputs, **kwargs) -> None: ...
    def freeze_feature_extractor(self) -> None:
        """
        Calling this function will disable the gradient computation for the feature encoder so that its parameters will
        not be updated during training.
        """
    def freeze_feature_encoder(self) -> None:
        """
        Calling this function will disable the gradient computation for the feature encoder so that its parameter will
        not be updated during training.
        """
    def call(self, input_values: tf.Tensor, attention_mask: Optional[tf.Tensor] = None, token_type_ids: Optional[tf.Tensor] = None, position_ids: Optional[tf.Tensor] = None, head_mask: Optional[tf.Tensor] = None, inputs_embeds: Optional[tf.Tensor] = None, output_attentions: Optional[bool] = None, labels: Optional[tf.Tensor] = None, output_hidden_states: Optional[bool] = None, return_dict: Optional[bool] = None, training: Optional[bool] = False) -> Union[TFCausalLMOutput, Tuple[tf.Tensor]]:
        '''
        labels (`tf.Tensor` or `np.ndarray` of shape `(batch_size, sequence_length)`, *optional*):
            Labels for computing the masked language modeling loss. Indices should be in `[-100, 0, ...,
            config.vocab_size]` (see `input_values` docstring) Tokens with indices set to `-100` are ignored (masked),
            the loss is only computed for the tokens with labels in `[0, ..., config.vocab_size]`

        Returns:

        Example:

        ```python
        >>> import tensorflow as tf
        >>> from transformers import AutoProcessor, TFWav2Vec2ForCTC
        >>> from datasets import load_dataset
        >>> import soundfile as sf

        >>> processor = AutoProcessor.from_pretrained("facebook/wav2vec2-base-960h")
        >>> model = TFWav2Vec2ForCTC.from_pretrained("facebook/wav2vec2-base-960h")


        >>> def map_to_array(batch):
        ...     speech, _ = sf.read(batch["file"])
        ...     batch["speech"] = speech
        ...     return batch


        >>> ds = load_dataset("hf-internal-testing/librispeech_asr_dummy", "clean", split="validation")
        >>> ds = ds.map(map_to_array)

        >>> input_values = processor(ds["speech"][0], return_tensors="tf").input_values  # Batch size 1
        >>> logits = model(input_values).logits
        >>> predicted_ids = tf.argmax(logits, axis=-1)

        >>> transcription = processor.decode(predicted_ids[0])

        >>> # compute loss
        >>> target_transcription = "A MAN SAID TO THE UNIVERSE SIR I EXIST"

        >>> # Pass transcription as `text` to encode labels
        >>> labels = processor(text=transcription, return_tensors="tf").input_ids

        >>> loss = model(input_values, labels=labels).loss
        ```'''
    def serving_output(self, output: TFCausalLMOutput) -> TFCausalLMOutput: ...
