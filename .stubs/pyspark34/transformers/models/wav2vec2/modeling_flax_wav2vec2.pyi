import flax.linen as nn
import jax
import jax.numpy as jnp
from ...modeling_flax_outputs import FlaxBaseModelOutput as FlaxBaseModelOutput, FlaxCausalLMOutput as FlaxCausalLMOutput
from ...modeling_flax_utils import ACT2FN as ACT2FN, FlaxPreTrainedModel as FlaxPreTrainedModel, append_replace_return_docstrings as append_replace_return_docstrings, overwrite_call_docstring as overwrite_call_docstring
from ...utils import ModelOutput as ModelOutput, add_start_docstrings as add_start_docstrings, add_start_docstrings_to_model_forward as add_start_docstrings_to_model_forward, logging as logging
from .configuration_wav2vec2 import Wav2Vec2Config as Wav2Vec2Config
from _typeshed import Incomplete
from flax.core.frozen_dict import FrozenDict as FrozenDict
from typing import Optional, Tuple

logger: Incomplete

class FlaxWav2Vec2BaseModelOutput(ModelOutput):
    """
    Output type of [`FlaxWav2Vec2BaseModelOutput`], with potential hidden states and attentions.

    Args:
        last_hidden_state (`jnp.ndarray` of shape `(batch_size, sequence_length, hidden_size)`):
            Sequence of hidden-states at the output of the last layer of the model.
        extract_features (`jnp.ndarray` of shape `(batch_size, sequence_length, last_conv_dim)`):
            Sequence of extracted feature vectors of the last convolutional layer of the model with `last_conv_dim`
            being the dimension of the last convolutional layer.
        hidden_states (`tuple(jnp.ndarray)`, *optional*, returned when `output_hidden_states=True` is passed or when `config.output_hidden_states=True`):
            Tuple of `jnp.ndarray` (one for the output of the embeddings + one for the output of each layer) of shape
            `(batch_size, sequence_length, hidden_size)`.

            Hidden-states of the model at the output of each layer plus the initial embedding outputs.
        attentions (`tuple(jnp.ndarray)`, *optional*, returned when `output_attentions=True` is passed or when `config.output_attentions=True`):
            Tuple of `jnp.ndarray` (one for each layer) of shape `(batch_size, num_heads, sequence_length,
            sequence_length)`.

            Attentions weights after the attention softmax, used to compute the weighted average in the self-attention
            heads.
    """
    last_hidden_state: jnp.ndarray
    extract_features: jnp.ndarray
    hidden_states: Optional[Tuple[jnp.ndarray]]
    attentions: Optional[Tuple[jnp.ndarray]]

class FlaxWav2Vec2ForPreTrainingOutput(ModelOutput):
    """
    Output type of [`FlaxWav2Vec2ForPreTrainingOutput`], with potential hidden states and attentions.

    Args:
        loss (*optional*, returned when model is in train mode, `jnp.ndarray` of shape `(1,)`):
            Total loss as the sum of the contrastive loss (L_m) and the diversity loss (L_d) as stated in the [official
            paper](https://arxiv.org/pdf/2006.11477.pdf) . (classification) loss.
        projected_states (`jnp.ndarray` of shape `(batch_size, sequence_length, config.proj_codevector_dim)`):
            Hidden-states of the model projected to *config.proj_codevector_dim* that can be used to predict the masked
            projected quantized states.
        projected_quantized_states (`jnp.ndarray` of shape `(batch_size, sequence_length, config.proj_codevector_dim)`):
            Quantized extracted feature vectors projected to *config.proj_codevector_dim* representing the positive
            target vectors for contrastive loss.
        hidden_states (`tuple(jnp.ndarray)`, *optional*, returned when `output_hidden_states=True` is passed or when `config.output_hidden_states=True`):
            Tuple of `jnp.ndarray` (one for the output of the embeddings + one for the output of each layer) of shape
            `(batch_size, sequence_length, hidden_size)`.

            Hidden-states of the model at the output of each layer plus the initial embedding outputs.
        attentions (`tuple(jnp.ndarray)`, *optional*, returned when `output_attentions=True` is passed or when `config.output_attentions=True`):
            Tuple of `jnp.ndarray` (one for each layer) of shape `(batch_size, num_heads, sequence_length,
            sequence_length)`.

            Attentions weights after the attention softmax, used to compute the weighted average in the self-attention
            heads.
    """
    projected_states: jnp.ndarray
    projected_quantized_states: jnp.ndarray
    codevector_perplexity: jnp.ndarray
    hidden_states: Optional[Tuple[jnp.ndarray]]
    attentions: Optional[Tuple[jnp.ndarray]]

WAV_2_VEC_2_START_DOCSTRING: str
WAV_2_VEC_2_INPUTS_DOCSTRING: str

class FlaxWav2Vec2LayerNormConvLayer(nn.Module):
    config: Wav2Vec2Config
    layer_id: int
    dtype: jnp.dtype
    in_conv_dim: Incomplete
    out_conv_dim: Incomplete
    conv: Incomplete
    layer_norm: Incomplete
    activation: Incomplete
    def setup(self) -> None: ...
    def __call__(self, hidden_states): ...

class FlaxConvWithWeightNorm(nn.Module):
    config: Wav2Vec2Config
    dtype: jnp.dtype
    conv: Incomplete
    weight_v: Incomplete
    weight_g: Incomplete
    bias: Incomplete
    prev_padding: Incomplete
    def setup(self): ...
    def __call__(self, hidden_states): ...

class FlaxWav2Vec2PositionalConvEmbedding(nn.Module):
    config: Wav2Vec2Config
    dtype: jnp.dtype
    conv: Incomplete
    activation: Incomplete
    num_pad_remove: Incomplete
    def setup(self) -> None: ...
    def __call__(self, hidden_states): ...

class FlaxConvLayersCollection(nn.Module):
    config: Wav2Vec2Config
    dtype: jnp.dtype
    layers: Incomplete
    def setup(self) -> None: ...
    def __call__(self, hidden_states): ...

class FlaxWav2Vec2FeatureEncoder(nn.Module):
    """Construct the features from raw audio waveform"""
    config: Wav2Vec2Config
    dtype: jnp.dtype
    conv_layers: Incomplete
    def setup(self) -> None: ...
    def __call__(self, input_values, freeze_feature_encoder: bool = False): ...

class FlaxWav2Vec2FeatureProjection(nn.Module):
    config: Wav2Vec2Config
    dtype: jnp.dtype
    layer_norm: Incomplete
    projection: Incomplete
    dropout: Incomplete
    def setup(self) -> None: ...
    def __call__(self, hidden_states, deterministic: bool = True): ...

class FlaxWav2Vec2Attention(nn.Module):
    config: Wav2Vec2Config
    embed_dim: int
    num_heads: int
    dropout: float
    bias: bool
    dtype: jnp.dtype
    head_dim: Incomplete
    out_proj: Incomplete
    dropout_layer: Incomplete
    def setup(self) -> None: ...
    def __call__(self, hidden_states: jnp.ndarray, key_value_states: Optional[jnp.ndarray] = None, attention_mask: Optional[jnp.ndarray] = None, deterministic: bool = True) -> Tuple[jnp.ndarray]:
        """Input shape: Batch x Time x Channel"""

class FlaxWav2Vec2FeedForward(nn.Module):
    config: Wav2Vec2Config
    dtype: jnp.dtype
    intermediate_dropout: Incomplete
    intermediate_dense: Incomplete
    intermediate_act_fn: Incomplete
    output_dense: Incomplete
    output_dropout: Incomplete
    def setup(self) -> None: ...
    def __call__(self, hidden_states, deterministic: bool = True): ...

class FlaxWav2Vec2EncoderLayerStableLayerNorm(nn.Module):
    config: Wav2Vec2Config
    dtype: jnp.dtype
    attention: Incomplete
    dropout: Incomplete
    layer_norm: Incomplete
    feed_forward: Incomplete
    final_layer_norm: Incomplete
    def setup(self) -> None: ...
    def __call__(self, hidden_states, attention_mask: Incomplete | None = None, deterministic: bool = True, output_attentions: bool = False): ...

class FlaxWav2Vec2EncoderLayerStableLayerNormCollection(nn.Module):
    config: Wav2Vec2Config
    dtype: jnp.dtype
    layers: Incomplete
    def setup(self) -> None: ...
    def __call__(self, hidden_states, attention_mask: Incomplete | None = None, deterministic: bool = True, output_attentions: bool = False, output_hidden_states: bool = False, return_dict: bool = True): ...

class FlaxWav2Vec2StableLayerNormEncoder(nn.Module):
    config: Wav2Vec2Config
    dtype: jnp.dtype
    pos_conv_embed: Incomplete
    layer_norm: Incomplete
    dropout: Incomplete
    layers: Incomplete
    def setup(self) -> None: ...
    def __call__(self, hidden_states, attention_mask: Incomplete | None = None, deterministic: bool = True, output_attentions: bool = False, output_hidden_states: bool = False, return_dict: bool = True): ...

class FlaxWav2Vec2GumbelVectorQuantizer(nn.Module):
    """
    Vector quantization using gumbel softmax. See [CATEGORICAL REPARAMETERIZATION WITH
    GUMBEL-SOFTMAX](https://arxiv.org/pdf/1611.01144.pdf) for more information.
    """
    config: Wav2Vec2Config
    dtype: jnp.dtype
    num_groups: Incomplete
    num_vars: Incomplete
    codevectors: Incomplete
    weight_proj: Incomplete
    def setup(self) -> None: ...
    def __call__(self, hidden_states, mask_time_indices: Incomplete | None = None, deterministic: bool = True, temperature: int = 1): ...

class FlaxWav2Vec2Adapter(nn.Module):
    config: Wav2Vec2Config
    dtype: jnp.dtype
    proj: Incomplete
    proj_layer_norm: Incomplete
    layers: Incomplete
    def setup(self) -> None: ...
    def __call__(self, hidden_states, deterministic: bool = True): ...

class FlaxWav2Vec2AdapterLayer(nn.Module):
    config: Wav2Vec2Config
    dtype: jnp.dtype
    conv: Incomplete
    def setup(self) -> None: ...
    def __call__(self, hidden_states): ...

class FlaxWav2Vec2AdapterLayersCollection(nn.Module):
    config: Wav2Vec2Config
    dtype: jnp.dtype
    layers: Incomplete
    def setup(self) -> None: ...
    def __call__(self, hidden_states): ...

class FlaxWav2Vec2PreTrainedModel(FlaxPreTrainedModel):
    """
    An abstract class to handle weights initialization and a simple interface for downloading and loading pretrained
    models.
    """
    config_class = Wav2Vec2Config
    base_model_prefix: str
    main_input_name: str
    module_class: nn.Module
    def __init__(self, config: Wav2Vec2Config, input_shape: Tuple = (1, 1024), seed: int = 0, dtype: jnp.dtype = ..., _do_init: bool = True, **kwargs) -> None: ...
    def init_weights(self, rng: jax.random.PRNGKey, input_shape: Tuple, params: FrozenDict = None) -> FrozenDict: ...
    def __call__(self, input_values, attention_mask: Incomplete | None = None, mask_time_indices: Incomplete | None = None, params: dict = None, dropout_rng: jax.random.PRNGKey = None, train: bool = False, output_attentions: Optional[bool] = None, output_hidden_states: Optional[bool] = None, freeze_feature_encoder: bool = False, return_dict: Optional[bool] = None): ...

class FlaxWav2Vec2Module(nn.Module):
    config: Wav2Vec2Config
    dtype: jnp.dtype
    feature_extractor: Incomplete
    feature_projection: Incomplete
    masked_spec_embed: Incomplete
    encoder: Incomplete
    adapter: Incomplete
    def setup(self) -> None: ...
    def __call__(self, input_values, attention_mask: Incomplete | None = None, mask_time_indices: Incomplete | None = None, deterministic: bool = True, output_attentions: Incomplete | None = None, output_hidden_states: Incomplete | None = None, freeze_feature_encoder: bool = False, return_dict: Incomplete | None = None): ...

class FlaxWav2Vec2Model(FlaxWav2Vec2PreTrainedModel):
    module_class = FlaxWav2Vec2Module

FLAX_WAV2VEC2_MODEL_DOCSTRING: str

class FlaxWav2Vec2ForCTCModule(nn.Module):
    config: Wav2Vec2Config
    dtype: jnp.dtype
    wav2vec2: Incomplete
    dropout: Incomplete
    lm_head: Incomplete
    def setup(self) -> None: ...
    def __call__(self, input_values, attention_mask: Incomplete | None = None, mask_time_indices: Incomplete | None = None, deterministic: bool = True, output_attentions: Incomplete | None = None, output_hidden_states: Incomplete | None = None, freeze_feature_encoder: bool = False, return_dict: Incomplete | None = None): ...

class FlaxWav2Vec2ForCTC(FlaxWav2Vec2PreTrainedModel):
    module_class = FlaxWav2Vec2ForCTCModule

FLAX_WAV2VEC2_FOR_CTC_DOCSTRING: str

class FlaxWav2Vec2ForPreTrainingModule(nn.Module):
    config: Wav2Vec2Config
    dtype: jnp.dtype
    wav2vec2: Incomplete
    dropout_features: Incomplete
    quantizer: Incomplete
    project_q: Incomplete
    project_hid: Incomplete
    def setup(self) -> None: ...
    def __call__(self, input_values, attention_mask: Incomplete | None = None, mask_time_indices: Incomplete | None = None, gumbel_temperature: int = 1, deterministic: bool = True, output_attentions: Incomplete | None = None, output_hidden_states: Incomplete | None = None, freeze_feature_encoder: bool = False, return_dict: Incomplete | None = None):
        """
        Returns:

        Example:

        ```python

        ```"""

class FlaxWav2Vec2ForPreTraining(FlaxWav2Vec2PreTrainedModel):
    module_class = FlaxWav2Vec2ForPreTrainingModule
    def __call__(self, input_values, attention_mask: Incomplete | None = None, mask_time_indices: Incomplete | None = None, gumbel_temperature: int = 1, params: dict = None, dropout_rng: jax.random.PRNGKey = None, gumbel_rng: jax.random.PRNGKey = None, train: bool = False, output_attentions: Optional[bool] = None, output_hidden_states: Optional[bool] = None, freeze_feature_encoder: bool = False, return_dict: Optional[bool] = None): ...

FLAX_WAV2VEC2_FOR_PRETRAINING_DOCSTRING: str
