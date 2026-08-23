import flax.linen as nn
import jax
import jax.numpy as jnp
import numpy as np
from ...modeling_flax_outputs import FlaxBaseModelOutputWithPastAndCrossAttentions as FlaxBaseModelOutputWithPastAndCrossAttentions, FlaxBaseModelOutputWithPooling as FlaxBaseModelOutputWithPooling, FlaxBaseModelOutputWithPoolingAndCrossAttentions as FlaxBaseModelOutputWithPoolingAndCrossAttentions, FlaxCausalLMOutputWithCrossAttentions as FlaxCausalLMOutputWithCrossAttentions, FlaxMaskedLMOutput as FlaxMaskedLMOutput, FlaxMultipleChoiceModelOutput as FlaxMultipleChoiceModelOutput, FlaxSequenceClassifierOutput as FlaxSequenceClassifierOutput, FlaxTokenClassifierOutput as FlaxTokenClassifierOutput
from ...modeling_flax_utils import ACT2FN as ACT2FN, FlaxPreTrainedModel as FlaxPreTrainedModel, append_call_sample_docstring as append_call_sample_docstring, append_replace_return_docstrings as append_replace_return_docstrings, overwrite_call_docstring as overwrite_call_docstring
from ...utils import ModelOutput as ModelOutput, add_start_docstrings as add_start_docstrings, add_start_docstrings_to_model_forward as add_start_docstrings_to_model_forward, logging as logging
from .configuration_big_bird import BigBirdConfig as BigBirdConfig
from _typeshed import Incomplete
from flax.core.frozen_dict import FrozenDict as FrozenDict
from typing import Callable, Optional, Tuple

logger: Incomplete
remat: Incomplete

class FlaxBigBirdForPreTrainingOutput(ModelOutput):
    """
    Output type of [`BigBirdForPreTraining`].

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

class FlaxBigBirdForQuestionAnsweringModelOutput(ModelOutput):
    """
    Base class for outputs of question answering models.

    Args:
        start_logits (`jnp.ndarray` of shape `(batch_size, sequence_length)`):
            Span-start scores (before SoftMax).
        end_logits (`jnp.ndarray` of shape `(batch_size, sequence_length)`):
            Span-end scores (before SoftMax).
        pooled_output (`jnp.ndarray` of shape `(batch_size, hidden_size)`):
            pooled_output returned by FlaxBigBirdModel.
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
    start_logits: jnp.ndarray
    end_logits: jnp.ndarray
    pooled_output: jnp.ndarray
    hidden_states: Optional[Tuple[jnp.ndarray]]
    attentions: Optional[Tuple[jnp.ndarray]]

BIG_BIRD_START_DOCSTRING: str
BIG_BIRD_INPUTS_DOCSTRING: str

class FlaxBigBirdEmbeddings(nn.Module):
    """Construct the embeddings from word, position and token_type embeddings."""
    config: BigBirdConfig
    dtype: jnp.dtype
    word_embeddings: Incomplete
    position_embeddings: Incomplete
    token_type_embeddings: Incomplete
    LayerNorm: Incomplete
    dropout: Incomplete
    def setup(self) -> None: ...
    def __call__(self, input_ids, token_type_ids, position_ids, attention_mask, deterministic: bool = True): ...

class FlaxBigBirdSelfAttention(nn.Module):
    config: BigBirdConfig
    causal: bool
    dtype: jnp.dtype
    head_dim: Incomplete
    query: Incomplete
    key: Incomplete
    value: Incomplete
    causal_mask: Incomplete
    def setup(self) -> None: ...
    def __call__(self, hidden_states, attention_mask, layer_head_mask, key_value_states: Optional[jnp.array] = None, init_cache: bool = False, deterministic: bool = True, output_attentions: bool = False): ...

class FlaxBigBirdBlockSparseAttention(nn.Module):
    config: BigBirdConfig
    block_sparse_seed: int
    dtype: jnp.dtype
    query: Incomplete
    key: Incomplete
    value: Incomplete
    def setup(self) -> None: ...
    @staticmethod
    def transpose_for_scores(x, n_heads, head_size): ...
    def __call__(self, hidden_states, attention_mask, deterministic: bool = True, output_attentions: bool = False): ...
    @staticmethod
    def create_masks_for_block_sparse_attn(attention_mask, block_size: int): ...
    def bigbird_block_sparse_attention(self, query_layer, key_layer, value_layer, band_mask, from_mask, to_mask, from_blocked_mask, to_blocked_mask, n_heads, head_size, plan_from_length: Incomplete | None = None, plan_num_rand_blocks: Incomplete | None = None, output_attentions: Incomplete | None = None): ...
    @staticmethod
    def jax_gather(params, indices, batch_dims: int = 2):
        """
        Gather the indices from params correctly (equivalent to tf.gather but with modifications)

        Args:
            params: (bsz, n_heads, num_blocks, block_size, head_dim)
            indices: (<num_blocks, 1)
        """

class FlaxBigBirdSelfOutput(nn.Module):
    config: BigBirdConfig
    dtype: jnp.dtype
    dense: Incomplete
    LayerNorm: Incomplete
    dropout: Incomplete
    def setup(self) -> None: ...
    def __call__(self, hidden_states, input_tensor, deterministic: bool = True): ...

class FlaxBigBirdAttention(nn.Module):
    config: BigBirdConfig
    layer_id: int
    causal: bool
    dtype: jnp.dtype
    self: Incomplete
    output: Incomplete
    def setup(self) -> None: ...
    def __call__(self, hidden_states, attention_mask, layer_head_mask, key_value_states: Incomplete | None = None, init_cache: bool = False, deterministic: bool = True, output_attentions: bool = False): ...

class FlaxBigBirdIntermediate(nn.Module):
    config: BigBirdConfig
    dtype: jnp.dtype
    dense: Incomplete
    activation: Incomplete
    def setup(self) -> None: ...
    def __call__(self, hidden_states): ...

class FlaxBigBirdOutput(nn.Module):
    config: BigBirdConfig
    dtype: jnp.dtype
    dense: Incomplete
    dropout: Incomplete
    LayerNorm: Incomplete
    def setup(self) -> None: ...
    def __call__(self, hidden_states, attention_output, deterministic: bool = True): ...

class FlaxBigBirdLayer(nn.Module):
    config: BigBirdConfig
    layer_id: int
    dtype: jnp.dtype
    attention: Incomplete
    intermediate: Incomplete
    output: Incomplete
    crossattention: Incomplete
    def setup(self) -> None: ...
    def __call__(self, hidden_states, attention_mask, layer_head_mask, encoder_hidden_states: Optional[jnp.ndarray] = None, encoder_attention_mask: Optional[jnp.ndarray] = None, init_cache: bool = False, deterministic: bool = True, output_attentions: bool = False): ...

class FlaxBigBirdLayerCollection(nn.Module):
    config: BigBirdConfig
    dtype: jnp.dtype
    gradient_checkpointing: bool
    layers: Incomplete
    def setup(self) -> None: ...
    def __call__(self, hidden_states, attention_mask, head_mask, encoder_hidden_states: Optional[jnp.ndarray] = None, encoder_attention_mask: Optional[jnp.ndarray] = None, init_cache: bool = False, deterministic: bool = True, output_attentions: bool = False, output_hidden_states: bool = False, return_dict: bool = True): ...

class FlaxBigBirdEncoder(nn.Module):
    config: BigBirdConfig
    dtype: jnp.dtype
    gradient_checkpointing: bool
    layer: Incomplete
    def setup(self) -> None: ...
    def __call__(self, hidden_states, attention_mask, head_mask, encoder_hidden_states: Optional[jnp.ndarray] = None, encoder_attention_mask: Optional[jnp.ndarray] = None, init_cache: bool = False, deterministic: bool = True, output_attentions: bool = False, output_hidden_states: bool = False, return_dict: bool = True): ...

class FlaxBigBirdPredictionHeadTransform(nn.Module):
    config: BigBirdConfig
    dtype: jnp.dtype
    dense: Incomplete
    activation: Incomplete
    LayerNorm: Incomplete
    def setup(self) -> None: ...
    def __call__(self, hidden_states): ...

class FlaxBigBirdLMPredictionHead(nn.Module):
    config: BigBirdConfig
    dtype: jnp.dtype
    bias_init: Callable[..., np.ndarray]
    transform: Incomplete
    decoder: Incomplete
    bias: Incomplete
    def setup(self) -> None: ...
    def __call__(self, hidden_states, shared_embedding: Incomplete | None = None): ...

class FlaxBigBirdOnlyMLMHead(nn.Module):
    config: BigBirdConfig
    dtype: jnp.dtype
    predictions: Incomplete
    def setup(self) -> None: ...
    def __call__(self, hidden_states, shared_embedding: Incomplete | None = None): ...

class FlaxBigBirdPreTrainingHeads(nn.Module):
    config: BigBirdConfig
    dtype: jnp.dtype
    predictions: Incomplete
    seq_relationship: Incomplete
    def setup(self) -> None: ...
    def __call__(self, hidden_states, pooled_output, shared_embedding: Incomplete | None = None): ...

class FlaxBigBirdPreTrainedModel(FlaxPreTrainedModel):
    """
    An abstract class to handle weights initialization and a simple interface for downloading and loading pretrained
    models.
    """
    config_class = BigBirdConfig
    base_model_prefix: str
    module_class: nn.Module
    def __init__(self, config: BigBirdConfig, input_shape: Optional[tuple] = None, seed: int = 0, dtype: jnp.dtype = ..., _do_init: bool = True, gradient_checkpointing: bool = False, **kwargs) -> None: ...
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

class FlaxBigBirdModule(nn.Module):
    config: BigBirdConfig
    dtype: jnp.dtype
    add_pooling_layer: bool
    gradient_checkpointing: bool
    embeddings: Incomplete
    encoder: Incomplete
    pooler: Incomplete
    def setup(self) -> None: ...
    def __call__(self, input_ids, attention_mask, token_type_ids, position_ids, head_mask, encoder_hidden_states: Optional[jnp.ndarray] = None, encoder_attention_mask: Optional[jnp.ndarray] = None, init_cache: bool = False, deterministic: bool = True, output_attentions: bool = False, output_hidden_states: bool = False, return_dict: bool = True): ...

class FlaxBigBirdModel(FlaxBigBirdPreTrainedModel):
    module_class = FlaxBigBirdModule

class FlaxBigBirdForPreTrainingModule(nn.Module):
    config: BigBirdConfig
    dtype: jnp.dtype
    gradient_checkpointing: bool
    bert: Incomplete
    cls: Incomplete
    def setup(self) -> None: ...
    def __call__(self, input_ids, attention_mask, token_type_ids, position_ids, head_mask, deterministic: bool = True, output_attentions: bool = False, output_hidden_states: bool = False, return_dict: bool = True): ...

class FlaxBigBirdForPreTraining(FlaxBigBirdPreTrainedModel):
    module_class = FlaxBigBirdForPreTrainingModule

FLAX_BIG_BIRD_FOR_PRETRAINING_DOCSTRING: str

class FlaxBigBirdForMaskedLMModule(nn.Module):
    config: BigBirdConfig
    dtype: jnp.dtype
    gradient_checkpointing: bool
    bert: Incomplete
    cls: Incomplete
    def setup(self) -> None: ...
    def __call__(self, input_ids, attention_mask, token_type_ids, position_ids, head_mask, deterministic: bool = True, output_attentions: bool = False, output_hidden_states: bool = False, return_dict: bool = True): ...

class FlaxBigBirdForMaskedLM(FlaxBigBirdPreTrainedModel):
    module_class = FlaxBigBirdForMaskedLMModule

class FlaxBigBirdClassificationHead(nn.Module):
    """Head for sentence-level classification tasks."""
    config: BigBirdConfig
    dtype: jnp.dtype
    dense: Incomplete
    dropout: Incomplete
    out_proj: Incomplete
    def setup(self) -> None: ...
    def __call__(self, features, deterministic: bool = True): ...

class FlaxBigBirdForSequenceClassificationModule(nn.Module):
    config: BigBirdConfig
    dtype: jnp.dtype
    gradient_checkpointing: bool
    bert: Incomplete
    classifier: Incomplete
    def setup(self) -> None: ...
    def __call__(self, input_ids, attention_mask, token_type_ids, position_ids, head_mask, deterministic: bool = True, output_attentions: bool = False, output_hidden_states: bool = False, return_dict: bool = True): ...

class FlaxBigBirdForSequenceClassification(FlaxBigBirdPreTrainedModel):
    module_class = FlaxBigBirdForSequenceClassificationModule

class FlaxBigBirdForMultipleChoiceModule(nn.Module):
    config: BigBirdConfig
    dtype: jnp.dtype
    gradient_checkpointing: bool
    bert: Incomplete
    dropout: Incomplete
    classifier: Incomplete
    def setup(self) -> None: ...
    def __call__(self, input_ids, attention_mask, token_type_ids, position_ids, head_mask, deterministic: bool = True, output_attentions: bool = False, output_hidden_states: bool = False, return_dict: bool = True): ...

class FlaxBigBirdForMultipleChoice(FlaxBigBirdPreTrainedModel):
    module_class = FlaxBigBirdForMultipleChoiceModule
    def __init__(self, config: BigBirdConfig, input_shape: Optional[tuple] = None, seed: int = 0, dtype: jnp.dtype = ..., _do_init: bool = True, **kwargs) -> None: ...

class FlaxBigBirdForTokenClassificationModule(nn.Module):
    config: BigBirdConfig
    dtype: jnp.dtype
    gradient_checkpointing: bool
    bert: Incomplete
    dropout: Incomplete
    classifier: Incomplete
    def setup(self) -> None: ...
    def __call__(self, input_ids, attention_mask, token_type_ids, position_ids, head_mask, deterministic: bool = True, output_attentions: bool = False, output_hidden_states: bool = False, return_dict: bool = True): ...

class FlaxBigBirdForTokenClassification(FlaxBigBirdPreTrainedModel):
    module_class = FlaxBigBirdForTokenClassificationModule

class FlaxBigBirdForQuestionAnsweringHead(nn.Module):
    config: BigBirdConfig
    dtype: jnp.dtype
    dropout: Incomplete
    intermediate: Incomplete
    output: Incomplete
    qa_outputs: Incomplete
    def setup(self) -> None: ...
    def __call__(self, encoder_output, deterministic: bool = True): ...

class FlaxBigBirdForQuestionAnsweringModule(nn.Module):
    config: BigBirdConfig
    dtype: jnp.dtype
    add_pooling_layer: bool
    gradient_checkpointing: bool
    bert: Incomplete
    qa_classifier: Incomplete
    def setup(self) -> None: ...
    def __call__(self, input_ids, attention_mask, token_type_ids, position_ids, head_mask, logits_mask: Incomplete | None = None, deterministic: bool = True, output_attentions: bool = False, output_hidden_states: bool = False, return_dict: bool = True): ...

class FlaxBigBirdForQuestionAnswering(FlaxBigBirdPreTrainedModel):
    module_class = FlaxBigBirdForQuestionAnsweringModule
    def __call__(self, input_ids, attention_mask: Incomplete | None = None, token_type_ids: Incomplete | None = None, position_ids: Incomplete | None = None, head_mask: Incomplete | None = None, question_lengths: Incomplete | None = None, params: dict = None, dropout_rng: jax.random.PRNGKey = None, train: bool = False, output_attentions: Optional[bool] = None, output_hidden_states: Optional[bool] = None, return_dict: Optional[bool] = None): ...
    @staticmethod
    def prepare_question_mask(q_lengths, maxlen: int): ...

class FlaxBigBirdForCausalLMModule(nn.Module):
    config: BigBirdConfig
    dtype: jnp.dtype
    gradient_checkpointing: bool
    bert: Incomplete
    cls: Incomplete
    def setup(self) -> None: ...
    def __call__(self, input_ids, attention_mask, position_ids, token_type_ids: Optional[jnp.ndarray] = None, head_mask: Optional[jnp.ndarray] = None, encoder_hidden_states: Optional[jnp.ndarray] = None, encoder_attention_mask: Optional[jnp.ndarray] = None, init_cache: bool = False, deterministic: bool = True, output_attentions: bool = False, output_hidden_states: bool = False, return_dict: bool = True): ...

class FlaxBigBirdForCausalLM(FlaxBigBirdPreTrainedModel):
    module_class = FlaxBigBirdForCausalLMModule
    def prepare_inputs_for_generation(self, input_ids, max_length, attention_mask: Optional[jnp.DeviceArray] = None): ...
    def update_inputs_for_generation(self, model_outputs, model_kwargs): ...
