import flax.linen as nn
import jax
import jax.numpy as jnp
import numpy as np
from ...modeling_flax_outputs import FlaxBaseModelOutput as FlaxBaseModelOutput, FlaxMaskedLMOutput as FlaxMaskedLMOutput, FlaxMultipleChoiceModelOutput as FlaxMultipleChoiceModelOutput, FlaxQuestionAnsweringModelOutput as FlaxQuestionAnsweringModelOutput, FlaxSequenceClassifierOutput as FlaxSequenceClassifierOutput, FlaxTokenClassifierOutput as FlaxTokenClassifierOutput
from ...modeling_flax_utils import ACT2FN as ACT2FN, FlaxPreTrainedModel as FlaxPreTrainedModel, append_call_sample_docstring as append_call_sample_docstring, overwrite_call_docstring as overwrite_call_docstring
from ...utils import add_start_docstrings as add_start_docstrings, add_start_docstrings_to_model_forward as add_start_docstrings_to_model_forward, logging as logging
from .configuration_distilbert import DistilBertConfig as DistilBertConfig
from _typeshed import Incomplete
from flax.core.frozen_dict import FrozenDict as FrozenDict
from typing import Callable, Optional, Tuple

logger: Incomplete
FLAX_DISTILBERT_START_DOCSTRING: str
DISTILBERT_INPUTS_DOCSTRING: str

def get_angles(pos, i, d_model): ...
def positional_encoding(position, d_model): ...

class FlaxEmbeddings(nn.Module):
    """Construct the embeddings from word, position and token_type embeddings."""
    config: DistilBertConfig
    dtype: jnp.dtype
    word_embeddings: Incomplete
    position_embeddings: Incomplete
    pos_encoding: Incomplete
    LayerNorm: Incomplete
    dropout: Incomplete
    def setup(self) -> None: ...
    def __call__(self, input_ids, deterministic: bool = True): ...

class FlaxMultiHeadSelfAttention(nn.Module):
    config: DistilBertConfig
    dtype: jnp.dtype
    n_heads: Incomplete
    dim: Incomplete
    dropout: Incomplete
    q_lin: Incomplete
    k_lin: Incomplete
    v_lin: Incomplete
    out_lin: Incomplete
    def setup(self) -> None: ...
    def __call__(self, query, key, value, mask, deterministic: bool = True, output_attentions: bool = False): ...

class FlaxFFN(nn.Module):
    config: DistilBertConfig
    dtype: jnp.dtype
    dropout: Incomplete
    chunk_size_feed_forward: Incomplete
    seq_len_dim: int
    lin1: Incomplete
    lin2: Incomplete
    activation: Incomplete
    def setup(self) -> None: ...
    def __call__(self, hidden_states, deterministic: bool = True): ...

class FlaxTransformerBlock(nn.Module):
    config: DistilBertConfig
    dtype: jnp.dtype
    attention: Incomplete
    sa_layer_norm: Incomplete
    ffn: Incomplete
    output_layer_norm: Incomplete
    def setup(self) -> None: ...
    def __call__(self, hidden_states, attn_mask, output_attentions: bool = False, deterministic: bool = True): ...

class FlaxTransformer(nn.Module):
    config: DistilBertConfig
    dtype: jnp.dtype
    layers: Incomplete
    def setup(self) -> None: ...
    def __call__(self, hidden_states, attention_mask, output_attentions: bool = False, output_hidden_states: bool = False, deterministic: bool = True, return_dict: bool = False): ...

class FlaxTransformerEncoder(nn.Module):
    config: DistilBertConfig
    dtype: jnp.dtype
    layer: Incomplete
    def setup(self) -> None: ...
    def __call__(self, hidden_states, attention_mask, output_attentions: bool = False, output_hidden_states: bool = False, deterministic: bool = True, return_dict: bool = False): ...

class FlaxDistilBertLMDecoder(nn.Module):
    config: DistilBertConfig
    dtype: jnp.dtype
    bias_init: Callable[..., np.ndarray]
    bias: Incomplete
    def setup(self) -> None: ...
    def __call__(self, inputs, kernel): ...

class FlaxDistilBertPreTrainedModel(FlaxPreTrainedModel):
    """
    An abstract class to handle weights initialization and a simple interface for downloading and loading pretrained
    models.
    """
    config_class = DistilBertConfig
    base_model_prefix: str
    module_class: nn.Module
    def __init__(self, config: DistilBertConfig, input_shape: Tuple = (1, 1), seed: int = 0, dtype: jnp.dtype = ..., _do_init: bool = True, **kwargs) -> None: ...
    def init_weights(self, rng: jax.random.PRNGKey, input_shape: Tuple, params: FrozenDict = None) -> FrozenDict: ...
    def __call__(self, input_ids, attention_mask: Incomplete | None = None, head_mask: Incomplete | None = None, params: dict = None, dropout_rng: jax.random.PRNGKey = None, train: bool = False, output_attentions: Optional[bool] = None, output_hidden_states: Optional[bool] = None, return_dict: Optional[bool] = None): ...

class FlaxDistilBertModule(nn.Module):
    config: DistilBertConfig
    dtype: jnp.dtype
    embeddings: Incomplete
    transformer: Incomplete
    def setup(self) -> None: ...
    def __call__(self, input_ids, attention_mask, deterministic: bool = True, output_attentions: bool = False, output_hidden_states: bool = False, return_dict: bool = True): ...

class FlaxDistilBertModel(FlaxDistilBertPreTrainedModel):
    module_class = FlaxDistilBertModule

class FlaxDistilBertForMaskedLMModule(nn.Module):
    config: DistilBertConfig
    dtype: jnp.dtype
    distilbert: Incomplete
    vocab_transform: Incomplete
    vocab_layer_norm: Incomplete
    vocab_projector: Incomplete
    def setup(self) -> None: ...
    def __call__(self, input_ids, attention_mask, deterministic: bool = True, output_attentions: bool = False, output_hidden_states: bool = False, return_dict: bool = True): ...

class FlaxDistilBertForMaskedLM(FlaxDistilBertPreTrainedModel):
    module_class = FlaxDistilBertForMaskedLMModule

class FlaxDistilBertForSequenceClassificationModule(nn.Module):
    config: DistilBertConfig
    dtype: jnp.dtype
    distilbert: Incomplete
    pre_classifier: Incomplete
    dropout: Incomplete
    classifier: Incomplete
    def setup(self) -> None: ...
    def __call__(self, input_ids, attention_mask, deterministic: bool = True, output_attentions: bool = False, output_hidden_states: bool = False, return_dict: bool = True): ...

class FlaxDistilBertForSequenceClassification(FlaxDistilBertPreTrainedModel):
    module_class = FlaxDistilBertForSequenceClassificationModule

class FlaxDistilBertForMultipleChoiceModule(nn.Module):
    config: DistilBertConfig
    dtype: jnp.dtype
    distilbert: Incomplete
    pre_classifier: Incomplete
    dropout: Incomplete
    classifier: Incomplete
    def setup(self) -> None: ...
    def __call__(self, input_ids, attention_mask, deterministic: bool = True, output_attentions: bool = False, output_hidden_states: bool = False, return_dict: bool = True): ...

class FlaxDistilBertForMultipleChoice(FlaxDistilBertPreTrainedModel):
    module_class = FlaxDistilBertForMultipleChoiceModule

class FlaxDistilBertForTokenClassificationModule(nn.Module):
    config: DistilBertConfig
    dtype: jnp.dtype
    distilbert: Incomplete
    dropout: Incomplete
    classifier: Incomplete
    def setup(self) -> None: ...
    def __call__(self, input_ids, attention_mask, deterministic: bool = True, output_attentions: bool = False, output_hidden_states: bool = False, return_dict: bool = True): ...

class FlaxDistilBertForTokenClassification(FlaxDistilBertPreTrainedModel):
    module_class = FlaxDistilBertForTokenClassificationModule

class FlaxDistilBertForQuestionAnsweringModule(nn.Module):
    config: DistilBertConfig
    dtype: jnp.dtype
    distilbert: Incomplete
    qa_outputs: Incomplete
    dropout: Incomplete
    def setup(self) -> None: ...
    def __call__(self, input_ids, attention_mask, deterministic: bool = True, output_attentions: bool = False, output_hidden_states: bool = False, return_dict: bool = True): ...

class FlaxDistilBertForQuestionAnswering(FlaxDistilBertPreTrainedModel):
    module_class = FlaxDistilBertForQuestionAnsweringModule
