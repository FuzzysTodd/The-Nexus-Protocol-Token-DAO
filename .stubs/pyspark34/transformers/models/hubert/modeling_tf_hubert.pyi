import tensorflow as tf
from ...activations_tf import get_tf_activation as get_tf_activation
from ...modeling_tf_outputs import TFBaseModelOutput as TFBaseModelOutput, TFCausalLMOutput as TFCausalLMOutput
from ...modeling_tf_utils import TFPreTrainedModel as TFPreTrainedModel, booleans_processing as booleans_processing, get_initializer as get_initializer, keras_serializable as keras_serializable
from ...tf_utils import shape_list as shape_list, stable_softmax as stable_softmax
from ...utils import ModelOutput as ModelOutput, add_start_docstrings as add_start_docstrings, add_start_docstrings_to_model_forward as add_start_docstrings_to_model_forward, logging as logging, replace_return_docstrings as replace_return_docstrings
from .configuration_hubert import HubertConfig as HubertConfig
from _typeshed import Incomplete
from typing import Any, Dict, Optional, Tuple, Union

logger: Incomplete
TF_HUBERT_PRETRAINED_MODEL_ARCHIVE_LIST: Incomplete
LARGE_NEGATIVE: float

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

class TFHubertGroupNorm(tf.keras.layers.Layer):
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

class TFHubertWeightNormConv1D(tf.keras.layers.Conv1D):
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

class TFHubertNoLayerNormConvLayer(tf.keras.layers.Layer):
    in_conv_dim: Incomplete
    out_conv_dim: Incomplete
    conv: Incomplete
    activation: Incomplete
    def __init__(self, config: HubertConfig, layer_id: int = 0, **kwargs: Any) -> None: ...
    def call(self, hidden_states: tf.Tensor) -> tf.Tensor: ...

class TFHubertLayerNormConvLayer(tf.keras.layers.Layer):
    in_conv_dim: Incomplete
    out_conv_dim: Incomplete
    conv: Incomplete
    layer_norm: Incomplete
    activation: Incomplete
    def __init__(self, config: HubertConfig, layer_id: int = 0, **kwargs: Any) -> None: ...
    def call(self, hidden_states: tf.Tensor) -> tf.Tensor: ...

class TFHubertGroupNormConvLayer(tf.keras.layers.Layer):
    in_conv_dim: Incomplete
    out_conv_dim: Incomplete
    conv: Incomplete
    activation: Incomplete
    layer_norm: Incomplete
    def __init__(self, config: HubertConfig, layer_id: int = 0, **kwargs: Any) -> None: ...
    def call(self, hidden_states: tf.Tensor) -> tf.Tensor: ...

class TFHubertPositionalConvEmbedding(tf.keras.layers.Layer):
    conv: Incomplete
    padding: Incomplete
    activation: Incomplete
    def __init__(self, config: HubertConfig, **kwargs: Any) -> None: ...
    def call(self, hidden_states: tf.Tensor) -> tf.Tensor: ...

class TFHubertSamePadLayer(tf.keras.layers.Layer):
    num_pad_remove: Incomplete
    def __init__(self, num_conv_pos_embeddings, **kwargs) -> None: ...
    def call(self, hidden_states): ...

class TFHubertFeatureEncoder(tf.keras.layers.Layer):
    conv_layers: Incomplete
    def __init__(self, config: HubertConfig, **kwargs: Any) -> None: ...
    def call(self, input_values): ...

class TFHubertFeatureExtractor(TFHubertFeatureEncoder):
    def __init__(self, config, **kwargs) -> None: ...

class TFHubertFeatureProjection(tf.keras.layers.Layer):
    layer_norm: Incomplete
    projection: Incomplete
    dropout: Incomplete
    def __init__(self, config: HubertConfig, **kwargs) -> None: ...
    def call(self, hidden_states: tf.Tensor, training: bool = False) -> tf.Tensor: ...

class TFHubertAttention(tf.keras.layers.Layer):
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

class TFHubertFeedForward(tf.keras.layers.Layer):
    intermediate_dropout: Incomplete
    intermediate_dense: Incomplete
    intermediate_act_fn: Incomplete
    output_dense: Incomplete
    output_dropout: Incomplete
    def __init__(self, config: HubertConfig, **kwargs) -> None: ...
    def call(self, hidden_states: tf.Tensor, training: bool = False) -> tf.Tensor: ...

class TFHubertEncoderLayer(tf.keras.layers.Layer):
    attention: Incomplete
    dropout: Incomplete
    layer_norm: Incomplete
    feed_forward: Incomplete
    final_layer_norm: Incomplete
    def __init__(self, config: HubertConfig, **kwargs) -> None: ...
    def call(self, hidden_states: tf.Tensor, attention_mask: Optional[tf.Tensor] = None, output_attentions: Optional[bool] = False, training: bool = False) -> Tuple[tf.Tensor]: ...

class TFHubertEncoderLayerStableLayerNorm(tf.keras.layers.Layer):
    attention: Incomplete
    dropout: Incomplete
    layer_norm: Incomplete
    feed_forward: Incomplete
    final_layer_norm: Incomplete
    def __init__(self, config: HubertConfig, **kwargs) -> None: ...
    def call(self, hidden_states: tf.Tensor, attention_mask: Optional[tf.Tensor] = None, output_attentions: Optional[bool] = False, training: bool = False) -> Tuple[tf.Tensor]: ...

class TFHubertEncoder(tf.keras.layers.Layer):
    config: Incomplete
    pos_conv_embed: Incomplete
    layer_norm: Incomplete
    dropout: Incomplete
    layer: Incomplete
    def __init__(self, config: HubertConfig, **kwargs) -> None: ...
    def call(self, hidden_states: tf.Tensor, attention_mask: Optional[tf.Tensor] = None, output_attentions: Optional[bool] = False, output_hidden_states: Optional[bool] = False, return_dict: Optional[bool] = True, training: Optional[bool] = False) -> Union[TFBaseModelOutput, Tuple[tf.Tensor]]: ...

class TFHubertEncoderStableLayerNorm(tf.keras.layers.Layer):
    config: Incomplete
    pos_conv_embed: Incomplete
    layer_norm: Incomplete
    dropout: Incomplete
    layer: Incomplete
    def __init__(self, config: HubertConfig, **kwargs) -> None: ...
    def call(self, hidden_states: tf.Tensor, attention_mask: Optional[tf.Tensor] = None, output_attentions: Optional[bool] = False, output_hidden_states: Optional[bool] = False, return_dict: Optional[bool] = True, training: Optional[bool] = False) -> Union[TFBaseModelOutput, Tuple[tf.Tensor]]: ...

class TFHubertMainLayer(tf.keras.layers.Layer):
    config_class = HubertConfig
    config: Incomplete
    feature_extractor: Incomplete
    feature_projection: Incomplete
    encoder: Incomplete
    def __init__(self, config: HubertConfig, **kwargs) -> None: ...
    masked_spec_embed: Incomplete
    def build(self, input_shape: tf.TensorShape): ...
    def call(self, input_values: tf.Tensor, attention_mask: Optional[tf.Tensor] = None, token_type_ids: Optional[tf.Tensor] = None, position_ids: Optional[tf.Tensor] = None, head_mask: Optional[tf.Tensor] = None, inputs_embeds: Optional[tf.Tensor] = None, output_attentions: Optional[tf.Tensor] = None, output_hidden_states: Optional[tf.Tensor] = None, return_dict: Optional[bool] = None, training: bool = False, **kwargs: Any): ...

class TFHubertPreTrainedModel(TFPreTrainedModel):
    """
    An abstract class to handle weights initialization and a simple interface for downloading and loading pretrained
    models.
    """
    config_class = HubertConfig
    base_model_prefix: str
    main_input_name: str
    @property
    def dummy_inputs(self) -> Dict[str, tf.Tensor]: ...
    def __init__(self, config, *inputs, **kwargs) -> None: ...
    def serving(self, inputs): ...

HUBERT_START_DOCSTRING: str
HUBERT_INPUTS_DOCSTRING: str

class TFHubertModel(TFHubertPreTrainedModel):
    config: Incomplete
    hubert: Incomplete
    def __init__(self, config: HubertConfig, *inputs, **kwargs) -> None: ...
    def call(self, input_values: tf.Tensor, attention_mask: Optional[tf.Tensor] = None, token_type_ids: Optional[tf.Tensor] = None, position_ids: Optional[tf.Tensor] = None, head_mask: Optional[tf.Tensor] = None, inputs_embeds: Optional[tf.Tensor] = None, output_attentions: Optional[bool] = None, output_hidden_states: Optional[bool] = None, return_dict: Optional[bool] = None, training: bool = False) -> Union[TFBaseModelOutput, Tuple[tf.Tensor]]:
        '''

        Returns:

        Example:

        ```python
        >>> from transformers import AutoProcessor, TFHubertModel
        >>> from datasets import load_dataset
        >>> import soundfile as sf

        >>> processor = AutoProcessor.from_pretrained("facebook/hubert-large-ls960-ft")
        >>> model = TFHubertModel.from_pretrained("facebook/hubert-large-ls960-ft")


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

class TFHubertForCTC(TFHubertPreTrainedModel):
    hubert: Incomplete
    dropout: Incomplete
    lm_head: Incomplete
    def __init__(self, config: HubertConfig, *inputs, **kwargs) -> None: ...
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
        >>> from transformers import AutoProcessor, TFHubertForCTC
        >>> from datasets import load_dataset
        >>> import soundfile as sf

        >>> processor = AutoProcessor.from_pretrained("facebook/hubert-large-ls960-ft")
        >>> model = TFHubertForCTC.from_pretrained("facebook/hubert-large-ls960-ft")


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

        >>> # Pass the transcription as text to encode labels
        >>> labels = processor(text=transcription, return_tensors="tf").input_values

        >>> loss = model(input_values, labels=labels).loss
        ```'''
    def serving_output(self, output: TFCausalLMOutput) -> TFCausalLMOutput: ...
