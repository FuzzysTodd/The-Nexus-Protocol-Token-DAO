import flax.linen as nn
import jax
import jax.numpy as jnp
import numpy as np
from ...modeling_flax_outputs import FlaxBaseModelOutputWithPastAndCrossAttentions as FlaxBaseModelOutputWithPastAndCrossAttentions, FlaxBaseModelOutputWithPooling as FlaxBaseModelOutputWithPooling, FlaxBaseModelOutputWithPoolingAndCrossAttentions as FlaxBaseModelOutputWithPoolingAndCrossAttentions, FlaxCausalLMOutputWithCrossAttentions as FlaxCausalLMOutputWithCrossAttentions, FlaxMaskedLMOutput as FlaxMaskedLMOutput, FlaxMultipleChoiceModelOutput as FlaxMultipleChoiceModelOutput, FlaxNextSentencePredictorOutput as FlaxNextSentencePredictorOutput, FlaxQuestionAnsweringModelOutput as FlaxQuestionAnsweringModelOutput, FlaxSequenceClassifierOutput as FlaxSequenceClassifierOutput, FlaxTokenClassifierOutput as FlaxTokenClassifierOutput
from ...modeling_flax_utils import ACT2FN as ACT2FN, FlaxPreTrainedModel as FlaxPreTrainedModel, append_call_sample_docstring as append_call_sample_docstring, append_replace_return_docstrings as append_replace_return_docstrings, overwrite_call_docstring as overwrite_call_docstring
from ...utils import ModelOutput as ModelOutput, add_start_docstrings as add_start_docstrings, add_start_docstrings_to_model_forward as add_start_docstrings_to_model_forward, logging as logging
from .configuration_bert import BertConfig as BertConfig
from _typeshed import Incomplete
from flax.core.frozen_dict import FrozenDict as FrozenDict
from typing import Callable, Optional, Tuple

logger: Incomplete
remat: Incomplete

class FlaxBertForPreTrainingOutput(ModelOutput):
    """
    Output type of [`BertForPreTraining`].

    Args:
        prediction_logits (`jnp.ndarray` of shape `(batch_size, sequence_length, config.vocab_size)`):
            Prediction scores of the language modeling head (scores for each vocabulary token before SoftMax).
        seq_relationship_logits (`jnp.ndarray` of shape `(batch_size, 2)`):
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
    seq_relationship_logits: jnp.ndarray
    hidden_states: Optional[Tuple[jnp.ndarray]]
    attentions: Optional[Tuple[jnp.ndarray]]

BERT_START_DOCSTRING: str
BERT_INPUTS_DOCSTRING: str

class FlaxBertEmbeddings(nn.Module):
    """Construct the embeddings from word, position and token_type embeddings."""
    config: BertConfig
    dtype: jnp.dtype
    word_embeddings: Incomplete
    position_embeddings: Incomplete
    token_type_embeddings: Incomplete
    LayerNorm: Incomplete
    dropout: Incomplete
    def setup(self) -> None: ...
    def __call__(self, input_ids, token_type_ids, position_ids, attention_mask, deterministic: bool = True): ...

class FlaxBertSelfAttention(nn.Module):
    config: BertConfig
    causal: bool
    dtype: jnp.dtype
    head_dim: Incomplete
    query: Incomplete
    key: Incomplete
    value: Incomplete
    causal_mask: Incomplete
    def setup(self) -> None: ...
    def __call__(self, hidden_states, attention_mask, layer_head_mask, key_value_states: Optional[jnp.array] = None, init_cache: bool = False, deterministic: bool = True, output_attentions: bool = False): ...

class FlaxBertSelfOutput(nn.Module):
    config: BertConfig
    dtype: jnp.dtype
    dense: Incomplete
    LayerNorm: Incomplete
    dropout: Incomplete
    def setup(self) -> None: ...
    def __call__(self, hidden_states, input_tensor, deterministic: bool = True): ...

class FlaxBertAttention(nn.Module):
    config: BertConfig
    causal: bool
    dtype: jnp.dtype
    self: Incomplete
    output: Incomplete
    def setup(self) -> None: ...
    def __call__(self, hidden_states, attention_mask, layer_head_mask, key_value_states: Incomplete | None = None, init_cache: bool = False, deterministic: bool = True, output_attentions: bool = False): ...

class FlaxBertIntermediate(nn.Module):
    config: BertConfig
    dtype: jnp.dtype
    dense: Incomplete
    activation: Incomplete
    def setup(self) -> None: ...
    def __call__(self, hidden_states): ...

class FlaxBertOutput(nn.Module):
    config: BertConfig
    dtype: jnp.dtype
    dense: Incomplete
    dropout: Incomplete
    LayerNorm: Incomplete
    def setup(self) -> None: ...
    def __call__(self, hidden_states, attention_output, deterministic: bool = True): ...

class FlaxBertLayer(nn.Module):
    config: BertConfig
    dtype: jnp.dtype
    attention: Incomplete
    intermediate: Incomplete
    output: Incomplete
    crossattention: Incomplete
    def setup(self) -> None: ...
    def __call__(self, hidden_states, attention_mask, layer_head_mask, encoder_hidden_states: Optional[jnp.ndarray] = None, encoder_attention_mask: Optional[jnp.ndarray] = None, init_cache: bool = False, deterministic: bool = True, output_attentions: bool = False): ...

class FlaxBertLayerCollection(nn.Module):
    config: BertConfig
    dtype: jnp.dtype
    gradient_checkpointing: bool
    layers: Incomplete
    def setup(self) -> None: ...
    def __call__(self, hidden_states, attention_mask, head_mask, encoder_hidden_states: Optional[jnp.ndarray] = None, encoder_attention_mask: Optional[jnp.ndarray] = None, init_cache: bool = False, deterministic: bool = True, output_attentions: bool = False, output_hidden_states: bool = False, return_dict: bool = True): ...

class FlaxBertEncoder(nn.Module):
    config: BertConfig
    dtype: jnp.dtype
    gradient_checkpointing: bool
    layer: Incomplete
    def setup(self) -> None: ...
    def __call__(self, hidden_states, attention_mask, head_mask, encoder_hidden_states: Optional[jnp.ndarray] = None, encoder_attention_mask: Optional[jnp.ndarray] = None, init_cache: bool = False, deterministic: bool = True, output_attentions: bool = False, output_hidden_states: bool = False, return_dict: bool = True): ...

class FlaxBertPooler(nn.Module):
    config: BertConfig
    dtype: jnp.dtype
    dense: Incomplete
    def setup(self) -> None: ...
    def __call__(self, hidden_states): ...

class FlaxBertPredictionHeadTransform(nn.Module):
    config: BertConfig
    dtype: jnp.dtype
    dense: Incomplete
    activation: Incomplete
    LayerNorm: Incomplete
    def setup(self) -> None: ...
    def __call__(self, hidden_states): ...

class FlaxBertLMPredictionHead(nn.Module):
    config: BertConfig
    dtype: jnp.dtype
    bias_init: Callable[..., np.ndarray]
    transform: Incomplete
    decoder: Incomplete
    bias: Incomplete
    def setup(self) -> None: ...
    def __call__(self, hidden_states, shared_embedding: Incomplete | None = None): ...

class FlaxBertOnlyMLMHead(nn.Module):
    config: BertConfig
    dtype: jnp.dtype
    predictions: Incomplete
    def setup(self) -> None: ...
    def __call__(self, hidden_states, shared_embedding: Incomplete | None = None): ...

class FlaxBertOnlyNSPHead(nn.Module):
    dtype: jnp.dtype
    seq_relationship: Incomplete
    def setup(self) -> None: ...
    def __call__(self, pooled_output): ...

class FlaxBertPreTrainingHeads(nn.Module):
    config: BertConfig
    dtype: jnp.dtype
    predictions: Incomplete
    seq_relationship: Incomplete
    def setup(self) -> None: ...
    def __call__(self, hidden_states, pooled_output, shared_embedding: Incomplete | None = None): ...

class FlaxBertPreTrainedModel(FlaxPreTrainedModel):
    """
    An abstract class to handle weights initialization and a simple interface for downloading and loading pretrained
    models.
    """
    config_class = BertConfig
    base_model_prefix: str
    module_class: nn.Module
    def __init__(self, config: BertConfig, input_shape: Tuple = (1, 1), seed: int = 0, dtype: jnp.dtype = ..., _do_init: bool = True, gradient_checkpointing: bool = False, **kwargs) -> None: ...
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

class FlaxBertModule(nn.Module):
    config: BertConfig
    dtype: jnp.dtype
    add_pooling_layer: bool
    gradient_checkpointing: bool
    embeddings: Incomplete
    encoder: Incomplete
    pooler: Incomplete
    def setup(self) -> None: ...
    def __call__(self, input_ids, attention_mask, token_type_ids: Optional[jnp.ndarray] = None, position_ids: Optional[jnp.ndarray] = None, head_mask: Optional[jnp.ndarray] = None, encoder_hidden_states: Optional[jnp.ndarray] = None, encoder_attention_mask: Optional[jnp.ndarray] = None, init_cache: bool = False, deterministic: bool = True, output_attentions: bool = False, output_hidden_states: bool = False, return_dict: bool = True): ...

class FlaxBertModel(FlaxBertPreTrainedModel):
    module_class = FlaxBertModule

class FlaxBertForPreTrainingModule(nn.Module):
    config: BertConfig
    dtype: jnp.dtype
    gradient_checkpointing: bool
    bert: Incomplete
    cls: Incomplete
    def setup(self) -> None: ...
    def __call__(self, input_ids, attention_mask, token_type_ids, position_ids, head_mask, deterministic: bool = True, output_attentions: bool = False, output_hidden_states: bool = False, return_dict: bool = True): ...

class FlaxBertForPreTraining(FlaxBertPreTrainedModel):
    module_class = FlaxBertForPreTrainingModule

FLAX_BERT_FOR_PRETRAINING_DOCSTRING: str

class FlaxBertForMaskedLMModule(nn.Module):
    config: BertConfig
    dtype: jnp.dtype
    gradient_checkpointing: bool
    bert: Incomplete
    cls: Incomplete
    def setup(self) -> None: ...
    def __call__(self, input_ids, attention_mask, token_type_ids, position_ids, head_mask, deterministic: bool = True, output_attentions: bool = False, output_hidden_states: bool = False, return_dict: bool = True): ...

class FlaxBertForMaskedLM(FlaxBertPreTrainedModel):
    module_class = FlaxBertForMaskedLMModule

class FlaxBertForNextSentencePredictionModule(nn.Module):
    config: BertConfig
    dtype: jnp.dtype
    gradient_checkpointing: bool
    bert: Incomplete
    cls: Incomplete
    def setup(self) -> None: ...
    def __call__(self, input_ids, attention_mask, token_type_ids, position_ids, head_mask, deterministic: bool = True, output_attentions: bool = False, output_hidden_states: bool = False, return_dict: bool = True): ...

class FlaxBertForNextSentencePrediction(FlaxBertPreTrainedModel):
    module_class = FlaxBertForNextSentencePredictionModule

FLAX_BERT_FOR_NEXT_SENT_PRED_DOCSTRING: str

class FlaxBertForSequenceClassificationModule(nn.Module):
    config: BertConfig
    dtype: jnp.dtype
    gradient_checkpointing: bool
    bert: Incomplete
    dropout: Incomplete
    classifier: Incomplete
    def setup(self) -> None: ...
    def __call__(self, input_ids, attention_mask, token_type_ids, position_ids, head_mask, deterministic: bool = True, output_attentions: bool = False, output_hidden_states: bool = False, return_dict: bool = True): ...

class FlaxBertForSequenceClassification(FlaxBertPreTrainedModel):
    module_class = FlaxBertForSequenceClassificationModule

class FlaxBertForMultipleChoiceModule(nn.Module):
    config: BertConfig
    dtype: jnp.dtype
    gradient_checkpointing: bool
    bert: Incomplete
    dropout: Incomplete
    classifier: Incomplete
    def setup(self) -> None: ...
    def __call__(self, input_ids, attention_mask, token_type_ids, position_ids, head_mask, deterministic: bool = True, output_attentions: bool = False, output_hidden_states: bool = False, return_dict: bool = True): ...

class FlaxBertForMultipleChoice(FlaxBertPreTrainedModel):
    module_class = FlaxBertForMultipleChoiceModule

class FlaxBertForTokenClassificationModule(nn.Module):
    config: BertConfig
    dtype: jnp.dtype
    gradient_checkpointing: bool
    bert: Incomplete
    dropout: Incomplete
    classifier: Incomplete
    def setup(self) -> None: ...
    def __call__(self, input_ids, attention_mask, token_type_ids, position_ids, head_mask, deterministic: bool = True, output_attentions: bool = False, output_hidden_states: bool = False, return_dict: bool = True): ...

class FlaxBertForTokenClassification(FlaxBertPreTrainedModel):
    module_class = FlaxBertForTokenClassificationModule

class FlaxBertForQuestionAnsweringModule(nn.Module):
    config: BertConfig
    dtype: jnp.dtype
    gradient_checkpointing: bool
    bert: Incomplete
    qa_outputs: Incomplete
    def setup(self) -> None: ...
    def __call__(self, input_ids, attention_mask, token_type_ids, position_ids, head_mask, deterministic: bool = True, output_attentions: bool = False, output_hidden_states: bool = False, return_dict: bool = True): ...

class FlaxBertForQuestionAnswering(FlaxBertPreTrainedModel):
    module_class = FlaxBertForQuestionAnsweringModule

class FlaxBertForCausalLMModule(nn.Module):
    config: BertConfig
    dtype: jnp.dtype
    gradient_checkpointing: bool
    bert: Incomplete
    cls: Incomplete
    def setup(self) -> None: ...
    def __call__(self, input_ids, attention_mask, position_ids, token_type_ids: Optional[jnp.ndarray] = None, head_mask: Optional[jnp.ndarray] = None, encoder_hidden_states: Optional[jnp.ndarray] = None, encoder_attention_mask: Optional[jnp.ndarray] = None, init_cache: bool = False, deterministic: bool = True, output_attentions: bool = False, output_hidden_states: bool = False, return_dict: bool = True): ...

class FlaxBertForCausalLM(FlaxBertPreTrainedModel):
    module_class = FlaxBertForCausalLMModule
    def prepare_inputs_for_generation(self, input_ids, max_length, attention_mask: Optional[jnp.DeviceArray] = None): ...
    def update_inputs_for_generation(self, model_outputs, model_kwargs): ...
