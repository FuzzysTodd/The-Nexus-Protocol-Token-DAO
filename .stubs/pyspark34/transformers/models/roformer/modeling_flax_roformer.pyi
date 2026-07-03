import flax.linen as nn
import jax
import jax.numpy as jnp
import numpy as np
from ...modeling_flax_outputs import FlaxBaseModelOutput as FlaxBaseModelOutput, FlaxMaskedLMOutput as FlaxMaskedLMOutput, FlaxMultipleChoiceModelOutput as FlaxMultipleChoiceModelOutput, FlaxQuestionAnsweringModelOutput as FlaxQuestionAnsweringModelOutput, FlaxSequenceClassifierOutput as FlaxSequenceClassifierOutput, FlaxTokenClassifierOutput as FlaxTokenClassifierOutput
from ...modeling_flax_utils import ACT2FN as ACT2FN, FlaxPreTrainedModel as FlaxPreTrainedModel, append_call_sample_docstring as append_call_sample_docstring, overwrite_call_docstring as overwrite_call_docstring
from ...utils import add_start_docstrings as add_start_docstrings, add_start_docstrings_to_model_forward as add_start_docstrings_to_model_forward, logging as logging
from .configuration_roformer import RoFormerConfig as RoFormerConfig
from _typeshed import Incomplete
from flax.core.frozen_dict import FrozenDict as FrozenDict
from typing import Callable, Optional, Tuple

logger: Incomplete
FLAX_ROFORMER_PRETRAINED_MODEL_ARCHIVE_LIST: Incomplete
ROFORMER_START_DOCSTRING: str
ROFORMER_INPUTS_DOCSTRING: str

def create_sinusoidal_positions(n_pos, dim): ...

class FlaxRoFormerEmbeddings(nn.Module):
    """Construct the embeddings from word and token_type embeddings."""
    config: RoFormerConfig
    dtype: jnp.dtype
    word_embeddings: Incomplete
    token_type_embeddings: Incomplete
    LayerNorm: Incomplete
    dropout: Incomplete
    def setup(self) -> None: ...
    def __call__(self, input_ids, token_type_ids, attention_mask, deterministic: bool = True): ...

class FlaxRoFormerSelfAttention(nn.Module):
    config: RoFormerConfig
    dtype: jnp.dtype
    query: Incomplete
    key: Incomplete
    value: Incomplete
    rotary_value: Incomplete
    def setup(self) -> None: ...
    def __call__(self, hidden_states, attention_mask, sinusoidal_pos, layer_head_mask, deterministic: bool = True, output_attentions: bool = False): ...
    @staticmethod
    def apply_rotary_position_embeddings(sinusoidal_pos, query_layer, key_layer, value_layer: Incomplete | None = None): ...

class FlaxRoFormerSelfOutput(nn.Module):
    config: RoFormerConfig
    dtype: jnp.dtype
    dense: Incomplete
    LayerNorm: Incomplete
    dropout: Incomplete
    def setup(self) -> None: ...
    def __call__(self, hidden_states, input_tensor, deterministic: bool = True): ...

class FlaxRoFormerAttention(nn.Module):
    config: RoFormerConfig
    dtype: jnp.dtype
    self: Incomplete
    output: Incomplete
    def setup(self) -> None: ...
    def __call__(self, hidden_states, attention_mask, sinusoidal_pos, layer_head_mask, deterministic: bool = True, output_attentions: bool = False): ...

class FlaxRoFormerIntermediate(nn.Module):
    config: RoFormerConfig
    dtype: jnp.dtype
    dense: Incomplete
    activation: Incomplete
    def setup(self) -> None: ...
    def __call__(self, hidden_states): ...

class FlaxRoFormerOutput(nn.Module):
    config: RoFormerConfig
    dtype: jnp.dtype
    dense: Incomplete
    dropout: Incomplete
    LayerNorm: Incomplete
    def setup(self) -> None: ...
    def __call__(self, hidden_states, attention_output, deterministic: bool = True): ...

class FlaxRoFormerLayer(nn.Module):
    config: RoFormerConfig
    dtype: jnp.dtype
    attention: Incomplete
    intermediate: Incomplete
    output: Incomplete
    def setup(self) -> None: ...
    def __call__(self, hidden_states, attention_mask, sinusiodal_pos, layer_head_mask, deterministic: bool = True, output_attentions: bool = False): ...

class FlaxRoFormerLayerCollection(nn.Module):
    config: RoFormerConfig
    dtype: jnp.dtype
    layers: Incomplete
    def setup(self) -> None: ...
    def __call__(self, hidden_states, attention_mask, sinusoidal_pos, head_mask, deterministic: bool = True, output_attentions: bool = False, output_hidden_states: bool = False, return_dict: bool = True): ...

class FlaxRoFormerEncoder(nn.Module):
    config: RoFormerConfig
    dtype: jnp.dtype
    embed_positions: Incomplete
    layer: Incomplete
    def setup(self) -> None: ...
    def __call__(self, hidden_states, attention_mask, head_mask, deterministic: bool = True, output_attentions: bool = False, output_hidden_states: bool = False, return_dict: bool = True): ...

class FlaxRoFormerPredictionHeadTransform(nn.Module):
    config: RoFormerConfig
    dtype: jnp.dtype
    dense: Incomplete
    activation: Incomplete
    LayerNorm: Incomplete
    def setup(self) -> None: ...
    def __call__(self, hidden_states): ...

class FlaxRoFormerLMPredictionHead(nn.Module):
    config: RoFormerConfig
    dtype: jnp.dtype
    bias_init: Callable[..., np.ndarray]
    transform: Incomplete
    decoder: Incomplete
    bias: Incomplete
    def setup(self) -> None: ...
    def __call__(self, hidden_states, shared_embedding: Incomplete | None = None): ...

class FlaxRoFormerOnlyMLMHead(nn.Module):
    config: RoFormerConfig
    dtype: jnp.dtype
    predictions: Incomplete
    def setup(self) -> None: ...
    def __call__(self, hidden_states, shared_embedding: Incomplete | None = None): ...

class FlaxRoFormerClassificationHead(nn.Module):
    config: RoFormerConfig
    dtype: jnp.dtype
    dense: Incomplete
    dropout: Incomplete
    out_proj: Incomplete
    activation: Incomplete
    def setup(self) -> None: ...
    def __call__(self, hidden_states, deterministic: bool = True): ...

class FlaxRoFormerPreTrainedModel(FlaxPreTrainedModel):
    """
    An abstract class to handle weights initialization and a simple interface for downloading and loading pretrained
    models.
    """
    config_class = RoFormerConfig
    base_model_prefix: str
    module_class: nn.Module
    def __init__(self, config: RoFormerConfig, input_shape: Tuple = (1, 1), seed: int = 0, dtype: jnp.dtype = ..., _do_init: bool = True, **kwargs) -> None: ...
    def init_weights(self, rng: jax.random.PRNGKey, input_shape: Tuple, params: FrozenDict = None) -> FrozenDict: ...
    def __call__(self, input_ids, attention_mask: Incomplete | None = None, token_type_ids: Incomplete | None = None, head_mask: Incomplete | None = None, params: dict = None, dropout_rng: jax.random.PRNGKey = None, train: bool = False, output_attentions: Optional[bool] = None, output_hidden_states: Optional[bool] = None, return_dict: Optional[bool] = None): ...

class FlaxRoFormerModule(nn.Module):
    config: RoFormerConfig
    dtype: jnp.dtype
    embeddings: Incomplete
    encoder: Incomplete
    def setup(self) -> None: ...
    def __call__(self, input_ids, attention_mask, token_type_ids, head_mask, deterministic: bool = True, output_attentions: bool = False, output_hidden_states: bool = False, return_dict: bool = True): ...

class FlaxRoFormerModel(FlaxRoFormerPreTrainedModel):
    module_class = FlaxRoFormerModule

class FlaxRoFormerForMaskedLMModule(nn.Module):
    config: RoFormerConfig
    dtype: jnp.dtype
    roformer: Incomplete
    cls: Incomplete
    def setup(self) -> None: ...
    def __call__(self, input_ids, attention_mask, token_type_ids, head_mask, deterministic: bool = True, output_attentions: bool = False, output_hidden_states: bool = False, return_dict: bool = True): ...

class FlaxRoFormerForMaskedLM(FlaxRoFormerPreTrainedModel):
    module_class = FlaxRoFormerForMaskedLMModule

class FlaxRoFormerForSequenceClassificationModule(nn.Module):
    config: RoFormerConfig
    dtype: jnp.dtype
    roformer: Incomplete
    classifier: Incomplete
    def setup(self) -> None: ...
    def __call__(self, input_ids, attention_mask, token_type_ids, head_mask, deterministic: bool = True, output_attentions: bool = False, output_hidden_states: bool = False, return_dict: bool = True): ...

class FlaxRoFormerForSequenceClassification(FlaxRoFormerPreTrainedModel):
    module_class = FlaxRoFormerForSequenceClassificationModule

class FlaxRoFormerForMultipleChoiceModule(nn.Module):
    config: RoFormerConfig
    dtype: jnp.dtype
    roformer: Incomplete
    dropout: Incomplete
    classifier: Incomplete
    def setup(self) -> None: ...
    def __call__(self, input_ids, attention_mask, token_type_ids, head_mask, deterministic: bool = True, output_attentions: bool = False, output_hidden_states: bool = False, return_dict: bool = True): ...

class FlaxRoFormerForMultipleChoice(FlaxRoFormerPreTrainedModel):
    module_class = FlaxRoFormerForMultipleChoiceModule

class FlaxRoFormerForTokenClassificationModule(nn.Module):
    config: RoFormerConfig
    dtype: jnp.dtype
    roformer: Incomplete
    dropout: Incomplete
    classifier: Incomplete
    def setup(self) -> None: ...
    def __call__(self, input_ids, attention_mask, token_type_ids, head_mask, deterministic: bool = True, output_attentions: bool = False, output_hidden_states: bool = False, return_dict: bool = True): ...

class FlaxRoFormerForTokenClassification(FlaxRoFormerPreTrainedModel):
    module_class = FlaxRoFormerForTokenClassificationModule

class FlaxRoFormerForQuestionAnsweringModule(nn.Module):
    config: RoFormerConfig
    dtype: jnp.dtype
    roformer: Incomplete
    qa_outputs: Incomplete
    def setup(self) -> None: ...
    def __call__(self, input_ids, attention_mask, token_type_ids, head_mask, deterministic: bool = True, output_attentions: bool = False, output_hidden_states: bool = False, return_dict: bool = True): ...

class FlaxRoFormerForQuestionAnswering(FlaxRoFormerPreTrainedModel):
    module_class = FlaxRoFormerForQuestionAnsweringModule
