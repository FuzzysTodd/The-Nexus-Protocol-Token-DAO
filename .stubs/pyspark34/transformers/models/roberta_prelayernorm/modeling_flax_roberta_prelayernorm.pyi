import flax.linen as nn
import jax
import jax.numpy as jnp
import numpy as np
from ...modeling_flax_outputs import FlaxBaseModelOutputWithPastAndCrossAttentions as FlaxBaseModelOutputWithPastAndCrossAttentions, FlaxBaseModelOutputWithPooling as FlaxBaseModelOutputWithPooling, FlaxBaseModelOutputWithPoolingAndCrossAttentions as FlaxBaseModelOutputWithPoolingAndCrossAttentions, FlaxCausalLMOutputWithCrossAttentions as FlaxCausalLMOutputWithCrossAttentions, FlaxMaskedLMOutput as FlaxMaskedLMOutput, FlaxMultipleChoiceModelOutput as FlaxMultipleChoiceModelOutput, FlaxQuestionAnsweringModelOutput as FlaxQuestionAnsweringModelOutput, FlaxSequenceClassifierOutput as FlaxSequenceClassifierOutput, FlaxTokenClassifierOutput as FlaxTokenClassifierOutput
from ...modeling_flax_utils import ACT2FN as ACT2FN, FlaxPreTrainedModel as FlaxPreTrainedModel, append_call_sample_docstring as append_call_sample_docstring, overwrite_call_docstring as overwrite_call_docstring
from ...utils import add_start_docstrings as add_start_docstrings, add_start_docstrings_to_model_forward as add_start_docstrings_to_model_forward, logging as logging
from .configuration_roberta_prelayernorm import RobertaPreLayerNormConfig as RobertaPreLayerNormConfig
from _typeshed import Incomplete
from flax.core.frozen_dict import FrozenDict as FrozenDict
from typing import Callable, Optional, Tuple

logger: Incomplete
remat: Incomplete

def create_position_ids_from_input_ids(input_ids, padding_idx):
    """
    Replace non-padding symbols with their position numbers. Position numbers begin at padding_idx+1. Padding symbols
    are ignored. This is modified from fairseq's `utils.make_positions`.

    Args:
        input_ids: jnp.ndarray
        padding_idx: int

    Returns: jnp.ndarray
    """

ROBERTA_PRELAYERNORM_START_DOCSTRING: str
ROBERTA_PRELAYERNORM_INPUTS_DOCSTRING: str

class FlaxRobertaPreLayerNormEmbeddings(nn.Module):
    """Construct the embeddings from word, position and token_type embeddings."""
    config: RobertaPreLayerNormConfig
    dtype: jnp.dtype
    word_embeddings: Incomplete
    position_embeddings: Incomplete
    token_type_embeddings: Incomplete
    LayerNorm: Incomplete
    dropout: Incomplete
    def setup(self) -> None: ...
    def __call__(self, input_ids, token_type_ids, position_ids, attention_mask, deterministic: bool = True): ...

class FlaxRobertaPreLayerNormSelfAttention(nn.Module):
    config: RobertaPreLayerNormConfig
    causal: bool
    dtype: jnp.dtype
    head_dim: Incomplete
    query: Incomplete
    key: Incomplete
    value: Incomplete
    causal_mask: Incomplete
    def setup(self) -> None: ...
    def __call__(self, hidden_states, attention_mask, layer_head_mask, key_value_states: Optional[jnp.array] = None, init_cache: bool = False, deterministic: bool = True, output_attentions: bool = False): ...

class FlaxRobertaPreLayerNormSelfOutput(nn.Module):
    config: RobertaPreLayerNormConfig
    dtype: jnp.dtype
    dense: Incomplete
    dropout: Incomplete
    def setup(self) -> None: ...
    def __call__(self, hidden_states, input_tensor, deterministic: bool = True): ...

class FlaxRobertaPreLayerNormAttention(nn.Module):
    config: RobertaPreLayerNormConfig
    causal: bool
    dtype: jnp.dtype
    self: Incomplete
    output: Incomplete
    LayerNorm: Incomplete
    def setup(self) -> None: ...
    def __call__(self, hidden_states, attention_mask, layer_head_mask, key_value_states: Incomplete | None = None, init_cache: bool = False, deterministic: bool = True, output_attentions: bool = False): ...

class FlaxRobertaPreLayerNormIntermediate(nn.Module):
    config: RobertaPreLayerNormConfig
    dtype: jnp.dtype
    LayerNorm: Incomplete
    dense: Incomplete
    activation: Incomplete
    def setup(self) -> None: ...
    def __call__(self, hidden_states): ...

class FlaxRobertaPreLayerNormOutput(nn.Module):
    config: RobertaPreLayerNormConfig
    dtype: jnp.dtype
    dense: Incomplete
    dropout: Incomplete
    def setup(self) -> None: ...
    def __call__(self, hidden_states, attention_output, deterministic: bool = True): ...

class FlaxRobertaPreLayerNormLayer(nn.Module):
    config: RobertaPreLayerNormConfig
    dtype: jnp.dtype
    attention: Incomplete
    intermediate: Incomplete
    output: Incomplete
    crossattention: Incomplete
    def setup(self) -> None: ...
    def __call__(self, hidden_states, attention_mask, layer_head_mask, encoder_hidden_states: Optional[jnp.ndarray] = None, encoder_attention_mask: Optional[jnp.ndarray] = None, init_cache: bool = False, deterministic: bool = True, output_attentions: bool = False): ...

class FlaxRobertaPreLayerNormLayerCollection(nn.Module):
    config: RobertaPreLayerNormConfig
    dtype: jnp.dtype
    gradient_checkpointing: bool
    layers: Incomplete
    def setup(self) -> None: ...
    def __call__(self, hidden_states, attention_mask, head_mask, encoder_hidden_states: Optional[jnp.ndarray] = None, encoder_attention_mask: Optional[jnp.ndarray] = None, init_cache: bool = False, deterministic: bool = True, output_attentions: bool = False, output_hidden_states: bool = False, return_dict: bool = True): ...

class FlaxRobertaPreLayerNormEncoder(nn.Module):
    config: RobertaPreLayerNormConfig
    dtype: jnp.dtype
    gradient_checkpointing: bool
    layer: Incomplete
    def setup(self) -> None: ...
    def __call__(self, hidden_states, attention_mask, head_mask, encoder_hidden_states: Optional[jnp.ndarray] = None, encoder_attention_mask: Optional[jnp.ndarray] = None, init_cache: bool = False, deterministic: bool = True, output_attentions: bool = False, output_hidden_states: bool = False, return_dict: bool = True): ...

class FlaxRobertaPreLayerNormPooler(nn.Module):
    config: RobertaPreLayerNormConfig
    dtype: jnp.dtype
    dense: Incomplete
    def setup(self) -> None: ...
    def __call__(self, hidden_states): ...

class FlaxRobertaPreLayerNormLMHead(nn.Module):
    config: RobertaPreLayerNormConfig
    dtype: jnp.dtype
    bias_init: Callable[..., np.ndarray]
    dense: Incomplete
    layer_norm: Incomplete
    decoder: Incomplete
    bias: Incomplete
    def setup(self) -> None: ...
    def __call__(self, hidden_states, shared_embedding: Incomplete | None = None): ...

class FlaxRobertaPreLayerNormClassificationHead(nn.Module):
    config: RobertaPreLayerNormConfig
    dtype: jnp.dtype
    dense: Incomplete
    dropout: Incomplete
    out_proj: Incomplete
    def setup(self) -> None: ...
    def __call__(self, hidden_states, deterministic: bool = True): ...

class FlaxRobertaPreLayerNormPreTrainedModel(FlaxPreTrainedModel):
    """
    An abstract class to handle weights initialization and a simple interface for downloading and loading pretrained
    models.
    """
    config_class = RobertaPreLayerNormConfig
    base_model_prefix: str
    module_class: nn.Module
    def __init__(self, config: RobertaPreLayerNormConfig, input_shape: Tuple = (1, 1), seed: int = 0, dtype: jnp.dtype = ..., _do_init: bool = True, gradient_checkpointing: bool = False, **kwargs) -> None: ...
    def enable_gradient_checkpointing(self) -> None: ...
    def init_weights(self, rng: jax.random.PRNGKey, input_shape: Tuple, params: FrozenDict = None) -> FrozenDict: ...
    def init_cache(self, batch_size, max_length):
        """
        Args:
            batch_size (`int`):
                batch_size used for fast auto-regressive decoding. Defines the batch size of the initialized cache.
            max_length (`int`):
                maximum possible length for auto-regressive decoding. Defines the sequence length of the initialized
                cache.
        """
    def __call__(self, input_ids, attention_mask: Incomplete | None = None, token_type_ids: Incomplete | None = None, position_ids: Incomplete | None = None, head_mask: Incomplete | None = None, encoder_hidden_states: Incomplete | None = None, encoder_attention_mask: Incomplete | None = None, params: dict = None, dropout_rng: jax.random.PRNGKey = None, train: bool = False, output_attentions: Optional[bool] = None, output_hidden_states: Optional[bool] = None, return_dict: Optional[bool] = None, past_key_values: dict = None): ...

class FlaxRobertaPreLayerNormModule(nn.Module):
    config: RobertaPreLayerNormConfig
    dtype: jnp.dtype
    add_pooling_layer: bool
    gradient_checkpointing: bool
    embeddings: Incomplete
    encoder: Incomplete
    LayerNorm: Incomplete
    pooler: Incomplete
    def setup(self) -> None: ...
    def __call__(self, input_ids, attention_mask, token_type_ids: Optional[jnp.ndarray] = None, position_ids: Optional[jnp.ndarray] = None, head_mask: Optional[jnp.ndarray] = None, encoder_hidden_states: Optional[jnp.ndarray] = None, encoder_attention_mask: Optional[jnp.ndarray] = None, init_cache: bool = False, deterministic: bool = True, output_attentions: bool = False, output_hidden_states: bool = False, return_dict: bool = True): ...

class FlaxRobertaPreLayerNormModel(FlaxRobertaPreLayerNormPreTrainedModel):
    module_class = FlaxRobertaPreLayerNormModule

class FlaxRobertaPreLayerNormForMaskedLMModule(nn.Module):
    config: RobertaPreLayerNormConfig
    dtype: jnp.dtype
    gradient_checkpointing: bool
    roberta_prelayernorm: Incomplete
    lm_head: Incomplete
    def setup(self) -> None: ...
    def __call__(self, input_ids, attention_mask, token_type_ids, position_ids, head_mask, deterministic: bool = True, output_attentions: bool = False, output_hidden_states: bool = False, return_dict: bool = True): ...

class FlaxRobertaPreLayerNormForMaskedLM(FlaxRobertaPreLayerNormPreTrainedModel):
    module_class = FlaxRobertaPreLayerNormForMaskedLMModule

class FlaxRobertaPreLayerNormForSequenceClassificationModule(nn.Module):
    config: RobertaPreLayerNormConfig
    dtype: jnp.dtype
    gradient_checkpointing: bool
    roberta_prelayernorm: Incomplete
    classifier: Incomplete
    def setup(self) -> None: ...
    def __call__(self, input_ids, attention_mask, token_type_ids, position_ids, head_mask, deterministic: bool = True, output_attentions: bool = False, output_hidden_states: bool = False, return_dict: bool = True): ...

class FlaxRobertaPreLayerNormForSequenceClassification(FlaxRobertaPreLayerNormPreTrainedModel):
    module_class = FlaxRobertaPreLayerNormForSequenceClassificationModule

class FlaxRobertaPreLayerNormForMultipleChoiceModule(nn.Module):
    config: RobertaPreLayerNormConfig
    dtype: jnp.dtype
    gradient_checkpointing: bool
    roberta_prelayernorm: Incomplete
    dropout: Incomplete
    classifier: Incomplete
    def setup(self) -> None: ...
    def __call__(self, input_ids, attention_mask, token_type_ids, position_ids, head_mask, deterministic: bool = True, output_attentions: bool = False, output_hidden_states: bool = False, return_dict: bool = True): ...

class FlaxRobertaPreLayerNormForMultipleChoice(FlaxRobertaPreLayerNormPreTrainedModel):
    module_class = FlaxRobertaPreLayerNormForMultipleChoiceModule

class FlaxRobertaPreLayerNormForTokenClassificationModule(nn.Module):
    config: RobertaPreLayerNormConfig
    dtype: jnp.dtype
    gradient_checkpointing: bool
    roberta_prelayernorm: Incomplete
    dropout: Incomplete
    classifier: Incomplete
    def setup(self) -> None: ...
    def __call__(self, input_ids, attention_mask, token_type_ids, position_ids, head_mask, deterministic: bool = True, output_attentions: bool = False, output_hidden_states: bool = False, return_dict: bool = True): ...

class FlaxRobertaPreLayerNormForTokenClassification(FlaxRobertaPreLayerNormPreTrainedModel):
    module_class = FlaxRobertaPreLayerNormForTokenClassificationModule

class FlaxRobertaPreLayerNormForQuestionAnsweringModule(nn.Module):
    config: RobertaPreLayerNormConfig
    dtype: jnp.dtype
    gradient_checkpointing: bool
    roberta_prelayernorm: Incomplete
    qa_outputs: Incomplete
    def setup(self) -> None: ...
    def __call__(self, input_ids, attention_mask, token_type_ids, position_ids, head_mask, deterministic: bool = True, output_attentions: bool = False, output_hidden_states: bool = False, return_dict: bool = True): ...

class FlaxRobertaPreLayerNormForQuestionAnswering(FlaxRobertaPreLayerNormPreTrainedModel):
    module_class = FlaxRobertaPreLayerNormForQuestionAnsweringModule

class FlaxRobertaPreLayerNormForCausalLMModule(nn.Module):
    config: RobertaPreLayerNormConfig
    dtype: jnp.dtype
    gradient_checkpointing: bool
    roberta_prelayernorm: Incomplete
    lm_head: Incomplete
    def setup(self) -> None: ...
    def __call__(self, input_ids, attention_mask, position_ids, token_type_ids: Optional[jnp.ndarray] = None, head_mask: Optional[jnp.ndarray] = None, encoder_hidden_states: Optional[jnp.ndarray] = None, encoder_attention_mask: Optional[jnp.ndarray] = None, init_cache: bool = False, deterministic: bool = True, output_attentions: bool = False, output_hidden_states: bool = False, return_dict: bool = True): ...

class FlaxRobertaPreLayerNormForCausalLM(FlaxRobertaPreLayerNormPreTrainedModel):
    module_class = FlaxRobertaPreLayerNormForCausalLMModule
    def prepare_inputs_for_generation(self, input_ids, max_length, attention_mask: Optional[jnp.DeviceArray] = None): ...
    def update_inputs_for_generation(self, model_outputs, model_kwargs): ...
