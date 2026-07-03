import flax.linen as nn
import jax
import jax.numpy as jnp
import numpy as np
from ...modeling_flax_outputs import FlaxBaseModelOutput as FlaxBaseModelOutput, FlaxBaseModelOutputWithPooling as FlaxBaseModelOutputWithPooling, FlaxMaskedLMOutput as FlaxMaskedLMOutput, FlaxMultipleChoiceModelOutput as FlaxMultipleChoiceModelOutput, FlaxQuestionAnsweringModelOutput as FlaxQuestionAnsweringModelOutput, FlaxSequenceClassifierOutput as FlaxSequenceClassifierOutput, FlaxTokenClassifierOutput as FlaxTokenClassifierOutput
from ...modeling_flax_utils import ACT2FN as ACT2FN, FlaxPreTrainedModel as FlaxPreTrainedModel, append_call_sample_docstring as append_call_sample_docstring, append_replace_return_docstrings as append_replace_return_docstrings, overwrite_call_docstring as overwrite_call_docstring
from ...utils import ModelOutput as ModelOutput, add_start_docstrings as add_start_docstrings, add_start_docstrings_to_model_forward as add_start_docstrings_to_model_forward, logging as logging
from .configuration_albert import AlbertConfig as AlbertConfig
from _typeshed import Incomplete
from flax.core.frozen_dict import FrozenDict as FrozenDict
from typing import Callable, Optional, Tuple

logger: Incomplete

class FlaxAlbertForPreTrainingOutput(ModelOutput):
    """
    Output type of [`FlaxAlbertForPreTraining`].

    Args:
        prediction_logits (`jnp.ndarray` of shape `(batch_size, sequence_length, config.vocab_size)`):
            Prediction scores of the language modeling head (scores for each vocabulary token before SoftMax).
        sop_logits (`jnp.ndarray` of shape `(batch_size, 2)`):
            Prediction scores of the next sequence prediction (classification) head (scores of True/False continuation
            before SoftMax).
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
    prediction_logits: jnp.ndarray
    sop_logits: jnp.ndarray
    hidden_states: Optional[Tuple[jnp.ndarray]]
    attentions: Optional[Tuple[jnp.ndarray]]

ALBERT_START_DOCSTRING: str
ALBERT_INPUTS_DOCSTRING: str

class FlaxAlbertEmbeddings(nn.Module):
    """Construct the embeddings from word, position and token_type embeddings."""
    config: AlbertConfig
    dtype: jnp.dtype
    word_embeddings: Incomplete
    position_embeddings: Incomplete
    token_type_embeddings: Incomplete
    LayerNorm: Incomplete
    dropout: Incomplete
    def setup(self) -> None: ...
    def __call__(self, input_ids, token_type_ids, position_ids, deterministic: bool = True): ...

class FlaxAlbertSelfAttention(nn.Module):
    config: AlbertConfig
    dtype: jnp.dtype
    query: Incomplete
    key: Incomplete
    value: Incomplete
    dense: Incomplete
    LayerNorm: Incomplete
    dropout: Incomplete
    def setup(self) -> None: ...
    def __call__(self, hidden_states, attention_mask, deterministic: bool = True, output_attentions: bool = False): ...

class FlaxAlbertLayer(nn.Module):
    config: AlbertConfig
    dtype: jnp.dtype
    attention: Incomplete
    ffn: Incomplete
    activation: Incomplete
    ffn_output: Incomplete
    full_layer_layer_norm: Incomplete
    dropout: Incomplete
    def setup(self) -> None: ...
    def __call__(self, hidden_states, attention_mask, deterministic: bool = True, output_attentions: bool = False): ...

class FlaxAlbertLayerCollection(nn.Module):
    config: AlbertConfig
    dtype: jnp.dtype
    layers: Incomplete
    def setup(self) -> None: ...
    def __call__(self, hidden_states, attention_mask, deterministic: bool = True, output_attentions: bool = False, output_hidden_states: bool = False): ...

class FlaxAlbertLayerCollections(nn.Module):
    config: AlbertConfig
    dtype: jnp.dtype
    layer_index: Optional[str]
    albert_layers: Incomplete
    def setup(self) -> None: ...
    def __call__(self, hidden_states, attention_mask, deterministic: bool = True, output_attentions: bool = False, output_hidden_states: bool = False): ...

class FlaxAlbertLayerGroups(nn.Module):
    config: AlbertConfig
    dtype: jnp.dtype
    layers: Incomplete
    def setup(self) -> None: ...
    def __call__(self, hidden_states, attention_mask, deterministic: bool = True, output_attentions: bool = False, output_hidden_states: bool = False, return_dict: bool = True): ...

class FlaxAlbertEncoder(nn.Module):
    config: AlbertConfig
    dtype: jnp.dtype
    embedding_hidden_mapping_in: Incomplete
    albert_layer_groups: Incomplete
    def setup(self) -> None: ...
    def __call__(self, hidden_states, attention_mask, deterministic: bool = True, output_attentions: bool = False, output_hidden_states: bool = False, return_dict: bool = True): ...

class FlaxAlbertOnlyMLMHead(nn.Module):
    config: AlbertConfig
    dtype: jnp.dtype
    bias_init: Callable[..., np.ndarray]
    dense: Incomplete
    activation: Incomplete
    LayerNorm: Incomplete
    decoder: Incomplete
    bias: Incomplete
    def setup(self) -> None: ...
    def __call__(self, hidden_states, shared_embedding: Incomplete | None = None): ...

class FlaxAlbertSOPHead(nn.Module):
    config: AlbertConfig
    dtype: jnp.dtype
    dropout: Incomplete
    classifier: Incomplete
    def setup(self) -> None: ...
    def __call__(self, pooled_output, deterministic: bool = True): ...

class FlaxAlbertPreTrainedModel(FlaxPreTrainedModel):
    """
    An abstract class to handle weights initialization and a simple interface for downloading and loading pretrained
    models.
    """
    config_class = AlbertConfig
    base_model_prefix: str
    module_class: nn.Module
    def __init__(self, config: AlbertConfig, input_shape: Tuple = (1, 1), seed: int = 0, dtype: jnp.dtype = ..., _do_init: bool = True, **kwargs) -> None: ...
    def init_weights(self, rng: jax.random.PRNGKey, input_shape: Tuple, params: FrozenDict = None) -> FrozenDict: ...
    def __call__(self, input_ids, attention_mask: Incomplete | None = None, token_type_ids: Incomplete | None = None, position_ids: Incomplete | None = None, params: dict = None, dropout_rng: jax.random.PRNGKey = None, train: bool = False, output_attentions: Optional[bool] = None, output_hidden_states: Optional[bool] = None, return_dict: Optional[bool] = None): ...

class FlaxAlbertModule(nn.Module):
    config: AlbertConfig
    dtype: jnp.dtype
    add_pooling_layer: bool
    embeddings: Incomplete
    encoder: Incomplete
    pooler: Incomplete
    pooler_activation: Incomplete
    def setup(self) -> None: ...
    def __call__(self, input_ids, attention_mask, token_type_ids: Optional[np.ndarray] = None, position_ids: Optional[np.ndarray] = None, deterministic: bool = True, output_attentions: bool = False, output_hidden_states: bool = False, return_dict: bool = True): ...

class FlaxAlbertModel(FlaxAlbertPreTrainedModel):
    module_class = FlaxAlbertModule

class FlaxAlbertForPreTrainingModule(nn.Module):
    config: AlbertConfig
    dtype: jnp.dtype
    albert: Incomplete
    predictions: Incomplete
    sop_classifier: Incomplete
    def setup(self) -> None: ...
    def __call__(self, input_ids, attention_mask, token_type_ids, position_ids, deterministic: bool = True, output_attentions: bool = False, output_hidden_states: bool = False, return_dict: bool = True): ...

class FlaxAlbertForPreTraining(FlaxAlbertPreTrainedModel):
    module_class = FlaxAlbertForPreTrainingModule

FLAX_ALBERT_FOR_PRETRAINING_DOCSTRING: str

class FlaxAlbertForMaskedLMModule(nn.Module):
    config: AlbertConfig
    dtype: jnp.dtype
    albert: Incomplete
    predictions: Incomplete
    def setup(self) -> None: ...
    def __call__(self, input_ids, attention_mask, token_type_ids, position_ids, deterministic: bool = True, output_attentions: bool = False, output_hidden_states: bool = False, return_dict: bool = True): ...

class FlaxAlbertForMaskedLM(FlaxAlbertPreTrainedModel):
    module_class = FlaxAlbertForMaskedLMModule

class FlaxAlbertForSequenceClassificationModule(nn.Module):
    config: AlbertConfig
    dtype: jnp.dtype
    albert: Incomplete
    dropout: Incomplete
    classifier: Incomplete
    def setup(self) -> None: ...
    def __call__(self, input_ids, attention_mask, token_type_ids, position_ids, deterministic: bool = True, output_attentions: bool = False, output_hidden_states: bool = False, return_dict: bool = True): ...

class FlaxAlbertForSequenceClassification(FlaxAlbertPreTrainedModel):
    module_class = FlaxAlbertForSequenceClassificationModule

class FlaxAlbertForMultipleChoiceModule(nn.Module):
    config: AlbertConfig
    dtype: jnp.dtype
    albert: Incomplete
    dropout: Incomplete
    classifier: Incomplete
    def setup(self) -> None: ...
    def __call__(self, input_ids, attention_mask, token_type_ids, position_ids, deterministic: bool = True, output_attentions: bool = False, output_hidden_states: bool = False, return_dict: bool = True): ...

class FlaxAlbertForMultipleChoice(FlaxAlbertPreTrainedModel):
    module_class = FlaxAlbertForMultipleChoiceModule

class FlaxAlbertForTokenClassificationModule(nn.Module):
    config: AlbertConfig
    dtype: jnp.dtype
    albert: Incomplete
    dropout: Incomplete
    classifier: Incomplete
    def setup(self) -> None: ...
    def __call__(self, input_ids, attention_mask, token_type_ids, position_ids, deterministic: bool = True, output_attentions: bool = False, output_hidden_states: bool = False, return_dict: bool = True): ...

class FlaxAlbertForTokenClassification(FlaxAlbertPreTrainedModel):
    module_class = FlaxAlbertForTokenClassificationModule

class FlaxAlbertForQuestionAnsweringModule(nn.Module):
    config: AlbertConfig
    dtype: jnp.dtype
    albert: Incomplete
    qa_outputs: Incomplete
    def setup(self) -> None: ...
    def __call__(self, input_ids, attention_mask, token_type_ids, position_ids, deterministic: bool = True, output_attentions: bool = False, output_hidden_states: bool = False, return_dict: bool = True): ...

class FlaxAlbertForQuestionAnswering(FlaxAlbertPreTrainedModel):
    module_class = FlaxAlbertForQuestionAnsweringModule
