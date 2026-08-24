import flax.linen as nn
import jax
import jax.numpy as jnp
from ...modeling_flax_outputs import FlaxBaseModelOutput as FlaxBaseModelOutput, FlaxBaseModelOutputWithPooling as FlaxBaseModelOutputWithPooling, FlaxSequenceClassifierOutput as FlaxSequenceClassifierOutput
from ...modeling_flax_utils import ACT2FN as ACT2FN, FlaxPreTrainedModel as FlaxPreTrainedModel, append_replace_return_docstrings as append_replace_return_docstrings, overwrite_call_docstring as overwrite_call_docstring
from ...utils import add_start_docstrings as add_start_docstrings, add_start_docstrings_to_model_forward as add_start_docstrings_to_model_forward
from .configuration_vit import ViTConfig as ViTConfig
from _typeshed import Incomplete
from flax.core.frozen_dict import FrozenDict as FrozenDict
from typing import Optional, Tuple

VIT_START_DOCSTRING: str
VIT_INPUTS_DOCSTRING: str

class FlaxViTPatchEmbeddings(nn.Module):
    config: ViTConfig
    dtype: jnp.dtype
    num_patches: Incomplete
    num_channels: Incomplete
    projection: Incomplete
    def setup(self) -> None: ...
    def __call__(self, pixel_values): ...

class FlaxViTEmbeddings(nn.Module):
    """Construct the CLS token, position and patch embeddings."""
    config: ViTConfig
    dtype: jnp.dtype
    cls_token: Incomplete
    patch_embeddings: Incomplete
    position_embeddings: Incomplete
    dropout: Incomplete
    def setup(self) -> None: ...
    def __call__(self, pixel_values, deterministic: bool = True): ...

class FlaxViTSelfAttention(nn.Module):
    config: ViTConfig
    dtype: jnp.dtype
    query: Incomplete
    key: Incomplete
    value: Incomplete
    def setup(self) -> None: ...
    def __call__(self, hidden_states, deterministic: bool = True, output_attentions: bool = False): ...

class FlaxViTSelfOutput(nn.Module):
    config: ViTConfig
    dtype: jnp.dtype
    dense: Incomplete
    dropout: Incomplete
    def setup(self) -> None: ...
    def __call__(self, hidden_states, input_tensor, deterministic: bool = True): ...

class FlaxViTAttention(nn.Module):
    config: ViTConfig
    dtype: jnp.dtype
    attention: Incomplete
    output: Incomplete
    def setup(self) -> None: ...
    def __call__(self, hidden_states, deterministic: bool = True, output_attentions: bool = False): ...

class FlaxViTIntermediate(nn.Module):
    config: ViTConfig
    dtype: jnp.dtype
    dense: Incomplete
    activation: Incomplete
    def setup(self) -> None: ...
    def __call__(self, hidden_states): ...

class FlaxViTOutput(nn.Module):
    config: ViTConfig
    dtype: jnp.dtype
    dense: Incomplete
    dropout: Incomplete
    def setup(self) -> None: ...
    def __call__(self, hidden_states, attention_output, deterministic: bool = True): ...

class FlaxViTLayer(nn.Module):
    config: ViTConfig
    dtype: jnp.dtype
    attention: Incomplete
    intermediate: Incomplete
    output: Incomplete
    layernorm_before: Incomplete
    layernorm_after: Incomplete
    def setup(self) -> None: ...
    def __call__(self, hidden_states, deterministic: bool = True, output_attentions: bool = False): ...

class FlaxViTLayerCollection(nn.Module):
    config: ViTConfig
    dtype: jnp.dtype
    layers: Incomplete
    def setup(self) -> None: ...
    def __call__(self, hidden_states, deterministic: bool = True, output_attentions: bool = False, output_hidden_states: bool = False, return_dict: bool = True): ...

class FlaxViTEncoder(nn.Module):
    config: ViTConfig
    dtype: jnp.dtype
    layer: Incomplete
    def setup(self) -> None: ...
    def __call__(self, hidden_states, deterministic: bool = True, output_attentions: bool = False, output_hidden_states: bool = False, return_dict: bool = True): ...

class FlaxViTPooler(nn.Module):
    config: ViTConfig
    dtype: jnp.dtype
    dense: Incomplete
    def setup(self) -> None: ...
    def __call__(self, hidden_states): ...

class FlaxViTPreTrainedModel(FlaxPreTrainedModel):
    """
    An abstract class to handle weights initialization and a simple interface for downloading and loading pretrained
    models.
    """
    config_class = ViTConfig
    base_model_prefix: str
    main_input_name: str
    module_class: nn.Module
    def __init__(self, config: ViTConfig, input_shape: Incomplete | None = None, seed: int = 0, dtype: jnp.dtype = ..., _do_init: bool = True, **kwargs) -> None: ...
    def init_weights(self, rng: jax.random.PRNGKey, input_shape: Tuple, params: FrozenDict = None) -> FrozenDict: ...
    def __call__(self, pixel_values, params: dict = None, dropout_rng: jax.random.PRNGKey = None, train: bool = False, output_attentions: Optional[bool] = None, output_hidden_states: Optional[bool] = None, return_dict: Optional[bool] = None): ...

class FlaxViTModule(nn.Module):
    config: ViTConfig
    dtype: jnp.dtype
    add_pooling_layer: bool
    embeddings: Incomplete
    encoder: Incomplete
    layernorm: Incomplete
    pooler: Incomplete
    def setup(self) -> None: ...
    def __call__(self, pixel_values, deterministic: bool = True, output_attentions: bool = False, output_hidden_states: bool = False, return_dict: bool = True): ...

class FlaxViTModel(FlaxViTPreTrainedModel):
    module_class = FlaxViTModule

FLAX_VISION_MODEL_DOCSTRING: str

class FlaxViTForImageClassificationModule(nn.Module):
    config: ViTConfig
    dtype: jnp.dtype
    vit: Incomplete
    classifier: Incomplete
    def setup(self) -> None: ...
    def __call__(self, pixel_values: Incomplete | None = None, deterministic: bool = True, output_attentions: Incomplete | None = None, output_hidden_states: Incomplete | None = None, return_dict: Incomplete | None = None): ...

class FlaxViTForImageClassification(FlaxViTPreTrainedModel):
    module_class = FlaxViTForImageClassificationModule

FLAX_VISION_CLASSIF_DOCSTRING: str
