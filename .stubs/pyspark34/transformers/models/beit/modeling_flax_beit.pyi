import flax.linen as nn
import jax
import jax.numpy as jnp
from ...modeling_flax_outputs import FlaxBaseModelOutput as FlaxBaseModelOutput, FlaxBaseModelOutputWithPooling as FlaxBaseModelOutputWithPooling, FlaxMaskedLMOutput as FlaxMaskedLMOutput, FlaxSequenceClassifierOutput as FlaxSequenceClassifierOutput
from ...modeling_flax_utils import ACT2FN as ACT2FN, FlaxPreTrainedModel as FlaxPreTrainedModel, append_replace_return_docstrings as append_replace_return_docstrings, overwrite_call_docstring as overwrite_call_docstring
from ...utils import add_start_docstrings as add_start_docstrings, add_start_docstrings_to_model_forward as add_start_docstrings_to_model_forward
from .configuration_beit import BeitConfig as BeitConfig
from _typeshed import Incomplete
from flax.core.frozen_dict import FrozenDict as FrozenDict
from typing import Callable, List, Optional, Tuple

class FlaxBeitModelOutputWithPooling(FlaxBaseModelOutputWithPooling):
    """
    Class for outputs of [`FlaxBeitModel`].

    Args:
        last_hidden_state (`jnp.ndarray` of shape `(batch_size, sequence_length, hidden_size)`):
            Sequence of hidden-states at the output of the last layer of the model.
        pooler_output (`jnp.ndarray` of shape `(batch_size, hidden_size)`):
            Average of the last layer hidden states of the patch tokens (excluding the *[CLS]* token) if
            *config.use_mean_pooling* is set to True. If set to False, then the final hidden state of the *[CLS]* token
            will be returned.
        hidden_states (`tuple(jnp.ndarray)`, *optional*, returned when `output_hidden_states=True` is passed or when `config.output_hidden_states=True`):
            Tuple of `jnp.ndarray` (one for the output of the embeddings + one for the output of each layer) of shape
            `(batch_size, sequence_length, hidden_size)`. Hidden-states of the model at the output of each layer plus
            the initial embedding outputs.
        attentions (`tuple(jnp.ndarray)`, *optional*, returned when `output_attentions=True` is passed or when `config.output_attentions=True`):
            Tuple of `jnp.ndarray` (one for each layer) of shape `(batch_size, num_heads, sequence_length,
            sequence_length)`. Attentions weights after the attention softmax, used to compute the weighted average in
            the self-attention heads.
    """

BEIT_START_DOCSTRING: str
BEIT_INPUTS_DOCSTRING: str

def relative_position_index_init(window_size: Tuple[int, int]) -> jnp.ndarray:
    """
    get pair-wise relative position index for each token inside the window
    """
def ones_with_scale(key, shape, scale, dtype=...): ...

class FlaxBeitDropPath(nn.Module):
    """Drop paths (Stochastic Depth) per sample (when applied in main path of residual blocks)."""
    rate: float
    def __call__(self, inputs, deterministic: Optional[bool] = True): ...

class FlaxBeitPatchEmbeddings(nn.Module):
    config: BeitConfig
    dtype: jnp.dtype
    num_channels: Incomplete
    num_patches: Incomplete
    patch_shape: Incomplete
    projection: Incomplete
    def setup(self) -> None: ...
    def __call__(self, pixel_values): ...

class FlaxBeitEmbeddings(nn.Module):
    """Construct the CLS token, position and patch embeddings."""
    config: BeitConfig
    dtype: jnp.dtype
    cls_token: Incomplete
    mask_token: Incomplete
    patch_embeddings: Incomplete
    position_embeddings: Incomplete
    dropout: Incomplete
    def setup(self) -> None: ...
    def __call__(self, pixel_values, bool_masked_pos: Incomplete | None = None, deterministic: bool = True): ...

class FlaxBeitRelativePositionBias(nn.Module):
    config: BeitConfig
    window_size: Tuple[int, int]
    dtype: jnp.dtype
    relative_position_bias_table: Incomplete
    relative_position_index: Incomplete
    def setup(self) -> None: ...
    def __call__(self): ...

class FlaxBeitSelfAttention(nn.Module):
    config: BeitConfig
    window_size: Tuple[int, int]
    dtype: jnp.dtype
    query: Incomplete
    key: Incomplete
    value: Incomplete
    relative_position_bias: Incomplete
    def setup(self) -> None: ...
    def __call__(self, hidden_states, relative_position_bias: Incomplete | None = None, deterministic: bool = True, output_attentions: bool = False): ...

class FlaxBeitSelfOutput(nn.Module):
    config: BeitConfig
    dtype: jnp.dtype
    dense: Incomplete
    dropout: Incomplete
    def setup(self) -> None: ...
    def __call__(self, hidden_states, deterministic: bool = True): ...

class FlaxBeitAttention(nn.Module):
    config: BeitConfig
    window_size: Tuple[int, int]
    dtype: jnp.dtype
    attention: Incomplete
    output: Incomplete
    def setup(self) -> None: ...
    def __call__(self, hidden_states, relative_position_bias: Incomplete | None = None, deterministic: bool = True, output_attentions: bool = False): ...

class FlaxBeitIntermediate(nn.Module):
    config: BeitConfig
    dtype: jnp.dtype
    dense: Incomplete
    activation: Incomplete
    def setup(self) -> None: ...
    def __call__(self, hidden_states): ...

class FlaxBeitOutput(nn.Module):
    config: BeitConfig
    dtype: jnp.dtype
    dense: Incomplete
    dropout: Incomplete
    def setup(self) -> None: ...
    def __call__(self, hidden_states, deterministic: bool = True): ...

class FlaxBeitLayer(nn.Module):
    config: BeitConfig
    window_size: Tuple[int, int]
    drop_path_rate: float
    dtype: jnp.dtype
    attention: Incomplete
    intermediate: Incomplete
    output: Incomplete
    layernorm_before: Incomplete
    drop_path: Incomplete
    layernorm_after: Incomplete
    init_values: Incomplete
    lambda_1: Incomplete
    lambda_2: Incomplete
    def setup(self) -> None: ...
    def __call__(self, hidden_states, relative_position_bias: Incomplete | None = None, deterministic: bool = True, output_attentions: bool = False): ...

class FlaxBeitLayerCollection(nn.Module):
    config: BeitConfig
    window_size: Tuple[int, int]
    drop_path_rates: List[float]
    relative_position_bias: Callable[[], jnp.ndarray]
    dtype: jnp.dtype
    layers: Incomplete
    def setup(self) -> None: ...
    def __call__(self, hidden_states, deterministic: bool = True, output_attentions: bool = False, output_hidden_states: bool = False, return_dict: bool = True): ...

class FlaxBeitEncoder(nn.Module):
    config: BeitConfig
    window_size: Tuple[int, int]
    dtype: jnp.dtype
    relative_position_bias: Incomplete
    layer: Incomplete
    def setup(self) -> None: ...
    def __call__(self, hidden_states, deterministic: bool = True, output_attentions: bool = False, output_hidden_states: bool = False, return_dict: bool = True): ...

class FlaxBeitPreTrainedModel(FlaxPreTrainedModel):
    """
    An abstract class to handle weights initialization and a simple interface for downloading and loading pretrained
    models.
    """
    config_class = BeitConfig
    base_model_prefix: str
    main_input_name: str
    module_class: nn.Module
    def __init__(self, config: BeitConfig, input_shape: Incomplete | None = None, seed: int = 0, dtype: jnp.dtype = ..., _do_init: bool = True, **kwargs) -> None: ...
    def init_weights(self, rng: jax.random.PRNGKey, input_shape: Tuple, params: FrozenDict = None) -> FrozenDict: ...
    def __call__(self, pixel_values, bool_masked_pos: Incomplete | None = None, params: dict = None, dropout_rng: jax.random.PRNGKey = None, train: bool = False, output_attentions: Optional[bool] = None, output_hidden_states: Optional[bool] = None, return_dict: Optional[bool] = None): ...

class FlaxBeitPooler(nn.Module):
    config: BeitConfig
    dtype: jnp.dtype
    layernorm: Incomplete
    def setup(self) -> None: ...
    def __call__(self, hidden_states): ...

class FlaxBeitModule(nn.Module):
    config: BeitConfig
    dtype: jnp.dtype
    add_pooling_layer: bool
    embeddings: Incomplete
    encoder: Incomplete
    layernorm: Incomplete
    pooler: Incomplete
    def setup(self) -> None: ...
    def __call__(self, pixel_values, bool_masked_pos: Incomplete | None = None, deterministic: bool = True, output_attentions: bool = False, output_hidden_states: bool = False, return_dict: bool = True): ...

class FlaxBeitModel(FlaxBeitPreTrainedModel):
    module_class = FlaxBeitModule

FLAX_BEIT_MODEL_DOCSTRING: str

class FlaxBeitForMaskedImageModelingModule(nn.Module):
    config: BeitConfig
    dtype: jnp.dtype
    beit: Incomplete
    layernorm: Incomplete
    lm_head: Incomplete
    def setup(self) -> None: ...
    def __call__(self, pixel_values: Incomplete | None = None, bool_masked_pos: Incomplete | None = None, deterministic: bool = True, output_attentions: Incomplete | None = None, output_hidden_states: Incomplete | None = None, return_dict: Incomplete | None = None): ...

class FlaxBeitForMaskedImageModeling(FlaxBeitPreTrainedModel):
    module_class = FlaxBeitForMaskedImageModelingModule

FLAX_BEIT_MLM_DOCSTRING: str

class FlaxBeitForImageClassificationModule(nn.Module):
    config: BeitConfig
    dtype: jnp.dtype
    beit: Incomplete
    classifier: Incomplete
    def setup(self) -> None: ...
    def __call__(self, pixel_values: Incomplete | None = None, bool_masked_pos: Incomplete | None = None, deterministic: bool = True, output_attentions: Incomplete | None = None, output_hidden_states: Incomplete | None = None, return_dict: Incomplete | None = None): ...

class FlaxBeitForImageClassification(FlaxBeitPreTrainedModel):
    module_class = FlaxBeitForImageClassificationModule

FLAX_BEIT_CLASSIF_DOCSTRING: str
