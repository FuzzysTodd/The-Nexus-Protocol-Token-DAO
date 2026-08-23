import flax.linen as nn
import jax
import jax.numpy as jnp
import numpy as np
from ...modeling_flax_outputs import FlaxBaseModelOutput as FlaxBaseModelOutput, FlaxBaseModelOutputWithPastAndCrossAttentions as FlaxBaseModelOutputWithPastAndCrossAttentions, FlaxCausalLMOutputWithCrossAttentions as FlaxCausalLMOutputWithCrossAttentions, FlaxMaskedLMOutput as FlaxMaskedLMOutput, FlaxMultipleChoiceModelOutput as FlaxMultipleChoiceModelOutput, FlaxQuestionAnsweringModelOutput as FlaxQuestionAnsweringModelOutput, FlaxSequenceClassifierOutput as FlaxSequenceClassifierOutput, FlaxTokenClassifierOutput as FlaxTokenClassifierOutput
from ...modeling_flax_utils import ACT2FN as ACT2FN, FlaxPreTrainedModel as FlaxPreTrainedModel, append_call_sample_docstring as append_call_sample_docstring, append_replace_return_docstrings as append_replace_return_docstrings, overwrite_call_docstring as overwrite_call_docstring
from ...utils import ModelOutput as ModelOutput, add_start_docstrings as add_start_docstrings, add_start_docstrings_to_model_forward as add_start_docstrings_to_model_forward, logging as logging
from .configuration_electra import ElectraConfig as ElectraConfig
from _typeshed import Incomplete
from flax.core.frozen_dict import FrozenDict as FrozenDict
from typing import Callable, Optional, Tuple

logger: Incomplete
remat: Incomplete

class FlaxElectraForPreTrainingOutput(ModelOutput):
    """
    Output type of [`ElectraForPreTraining`].

    Args:
        logits (`jnp.ndarray` of shape `(batch_size, sequence_length, config.vocab_size)`):
            Prediction scores of the language modeling head (scores for each vocabulary token before SoftMax).
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
    logits: jnp.ndarray
    hidden_states: Optional[Tuple[jnp.ndarray]]
    attentions: Optional[Tuple[jnp.ndarray]]

ELECTRA_START_DOCSTRING: str
ELECTRA_INPUTS_DOCSTRING: str

class FlaxElectraEmbeddings(nn.Module):
    """Construct the embeddings from word, position and token_type embeddings."""
    config: ElectraConfig
    dtype: jnp.dtype
    word_embeddings: Incomplete
    position_embeddings: Incomplete
    token_type_embeddings: Incomplete
    LayerNorm: Incomplete
    dropout: Incomplete
    def setup(self) -> None: ...
    def __call__(self, input_ids, token_type_ids, position_ids, attention_mask, deterministic: bool = True): ...

class FlaxElectraSelfAttention(nn.Module):
    config: ElectraConfig
    causal: bool
    dtype: jnp.dtype
    head_dim: Incomplete
    query: Incomplete
    key: Incomplete
    value: Incomplete
    causal_mask: Incomplete
    def setup(self) -> None: ...
    def __call__(self, hidden_states, attention_mask, layer_head_mask, key_value_states: Optional[jnp.array] = None, init_cache: bool = False, deterministic: bool = True, output_attentions: bool = False): ...

class FlaxElectraSelfOutput(nn.Module):
    config: ElectraConfig
    dtype: jnp.dtype
    dense: Incomplete
    LayerNorm: Incomplete
    dropout: Incomplete
    def setup(self) -> None: ...
    def __call__(self, hidden_states, input_tensor, deterministic: bool = True): ...

class FlaxElectraAttention(nn.Module):
    config: ElectraConfig
    causal: bool
    dtype: jnp.dtype
    self: Incomplete
    output: Incomplete
    def setup(self) -> None: ...
    def __call__(self, hidden_states, attention_mask, layer_head_mask, key_value_states: Incomplete | None = None, init_cache: bool = False, deterministic: bool = True, output_attentions: bool = False): ...

class FlaxElectraIntermediate(nn.Module):
    config: ElectraConfig
    dtype: jnp.dtype
    dense: Incomplete
    activation: Incomplete
    def setup(self) -> None: ...
    def __call__(self, hidden_states): ...

class FlaxElectraOutput(nn.Module):
    config: ElectraConfig
    dtype: jnp.dtype
    dense: Incomplete
    dropout: Incomplete
    LayerNorm: Incomplete
    def setup(self) -> None: ...
    def __call__(self, hidden_states, attention_output, deterministic: bool = True): ...

class FlaxElectraLayer(nn.Module):
    config: ElectraConfig
    dtype: jnp.dtype
    attention: Incomplete
    intermediate: Incomplete
    output: Incomplete
    crossattention: Incomplete
    def setup(self) -> None: ...
    def __call__(self, hidden_states, attention_mask, layer_head_mask, encoder_hidden_states: Optional[jnp.ndarray] = None, encoder_attention_mask: Optional[jnp.ndarray] = None, init_cache: bool = False, deterministic: bool = True, output_attentions: bool = False): ...

class FlaxElectraLayerCollection(nn.Module):
    config: ElectraConfig
    dtype: jnp.dtype
    gradient_checkpointing: bool
    layers: Incomplete
    def setup(self) -> None: ...
    def __call__(self, hidden_states, attention_mask, head_mask, encoder_hidden_states: Optional[jnp.ndarray] = None, encoder_attention_mask: Optional[jnp.ndarray] = None, init_cache: bool = False, deterministic: bool = True, output_attentions: bool = False, output_hidden_states: bool = False, return_dict: bool = True): ...

class FlaxElectraEncoder(nn.Module):
    config: ElectraConfig
    dtype: jnp.dtype
    gradient_checkpointing: bool
    layer: Incomplete
    def setup(self) -> None: ...
    def __call__(self, hidden_states, attention_mask, head_mask, encoder_hidden_states: Optional[jnp.ndarray] = None, encoder_attention_mask: Optional[jnp.ndarray] = None, init_cache: bool = False, deterministic: bool = True, output_attentions: bool = False, output_hidden_states: bool = False, return_dict: bool = True): ...

class FlaxElectraGeneratorPredictions(nn.Module):
    config: ElectraConfig
    dtype: jnp.dtype
    LayerNorm: Incomplete
    dense: Incomplete
    def setup(self) -> None: ...
    def __call__(self, hidden_states): ...

class FlaxElectraDiscriminatorPredictions(nn.Module):
    """Prediction module for the discriminator, made up of two dense layers."""
    config: ElectraConfig
    dtype: jnp.dtype
    dense: Incomplete
    dense_prediction: Incomplete
    def setup(self) -> None: ...
    def __call__(self, hidden_states): ...

class FlaxElectraPreTrainedModel(FlaxPreTrainedModel):
    """
    An abstract class to handle weights initialization and a simple interface for downloading and loading pretrained
    models.
    """
    config_class = ElectraConfig
    base_model_prefix: str
    module_class: nn.Module
    def __init__(self, config: ElectraConfig, input_shape: Tuple = (1, 1), seed: int = 0, dtype: jnp.dtype = ..., _do_init: bool = True, gradient_checkpointing: bool = False, **kwargs) -> None: ...
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

class FlaxElectraModule(nn.Module):
    config: ElectraConfig
    dtype: jnp.dtype
    gradient_checkpointing: bool
    embeddings: Incomplete
    embeddings_project: Incomplete
    encoder: Incomplete
    def setup(self) -> None: ...
    def __call__(self, input_ids, attention_mask, token_type_ids, position_ids, head_mask: Optional[np.ndarray] = None, encoder_hidden_states: Optional[jnp.ndarray] = None, encoder_attention_mask: Optional[jnp.ndarray] = None, init_cache: bool = False, deterministic: bool = True, output_attentions: bool = False, output_hidden_states: bool = False, return_dict: bool = True): ...

class FlaxElectraModel(FlaxElectraPreTrainedModel):
    module_class = FlaxElectraModule

class FlaxElectraTiedDense(nn.Module):
    embedding_size: int
    dtype: jnp.dtype
    precision: Incomplete
    bias_init: Callable[..., np.ndarray]
    bias: Incomplete
    def setup(self) -> None: ...
    def __call__(self, x, kernel): ...

class FlaxElectraForMaskedLMModule(nn.Module):
    config: ElectraConfig
    dtype: jnp.dtype
    gradient_checkpointing: bool
    electra: Incomplete
    generator_predictions: Incomplete
    generator_lm_head: Incomplete
    def setup(self) -> None: ...
    def __call__(self, input_ids, attention_mask: Incomplete | None = None, token_type_ids: Incomplete | None = None, position_ids: Incomplete | None = None, head_mask: Incomplete | None = None, deterministic: bool = True, output_attentions: bool = False, output_hidden_states: bool = False, return_dict: bool = True): ...

class FlaxElectraForMaskedLM(FlaxElectraPreTrainedModel):
    module_class = FlaxElectraForMaskedLMModule

class FlaxElectraForPreTrainingModule(nn.Module):
    config: ElectraConfig
    dtype: jnp.dtype
    gradient_checkpointing: bool
    electra: Incomplete
    discriminator_predictions: Incomplete
    def setup(self) -> None: ...
    def __call__(self, input_ids, attention_mask: Incomplete | None = None, token_type_ids: Incomplete | None = None, position_ids: Incomplete | None = None, head_mask: Incomplete | None = None, deterministic: bool = True, output_attentions: bool = False, output_hidden_states: bool = False, return_dict: bool = True): ...

class FlaxElectraForPreTraining(FlaxElectraPreTrainedModel):
    module_class = FlaxElectraForPreTrainingModule

FLAX_ELECTRA_FOR_PRETRAINING_DOCSTRING: str

class FlaxElectraForTokenClassificationModule(nn.Module):
    config: ElectraConfig
    dtype: jnp.dtype
    gradient_checkpointing: bool
    electra: Incomplete
    dropout: Incomplete
    classifier: Incomplete
    def setup(self) -> None: ...
    def __call__(self, input_ids, attention_mask: Incomplete | None = None, token_type_ids: Incomplete | None = None, position_ids: Incomplete | None = None, head_mask: Incomplete | None = None, deterministic: bool = True, output_attentions: bool = False, output_hidden_states: bool = False, return_dict: bool = True): ...

class FlaxElectraForTokenClassification(FlaxElectraPreTrainedModel):
    module_class = FlaxElectraForTokenClassificationModule

def identity(x, **kwargs): ...

class FlaxElectraSequenceSummary(nn.Module):
    '''
    Compute a single vector summary of a sequence hidden states.

    Args:
        config ([`PretrainedConfig`]):
            The config used by the model. Relevant arguments in the config class of the model are (refer to the actual
            config class of your model for the default values it uses):

            - **summary_use_proj** (`bool`) -- Add a projection after the vector extraction.
            - **summary_proj_to_labels** (`bool`) -- If `True`, the projection outputs to `config.num_labels` classes
              (otherwise to `config.hidden_size`).
            - **summary_activation** (`Optional[str]`) -- Set to `"tanh"` to add a tanh activation to the output,
              another string or `None` will add no activation.
            - **summary_first_dropout** (`float`) -- Optional dropout probability before the projection and activation.
            - **summary_last_dropout** (`float`)-- Optional dropout probability after the projection and activation.
    '''
    config: ElectraConfig
    dtype: jnp.dtype
    summary: Incomplete
    activation: Incomplete
    first_dropout: Incomplete
    last_dropout: Incomplete
    def setup(self): ...
    def __call__(self, hidden_states, cls_index: Incomplete | None = None, deterministic: bool = True):
        '''
        Compute a single vector summary of a sequence hidden states.

        Args:
            hidden_states (`jnp.array` of shape `[batch_size, seq_len, hidden_size]`):
                The hidden states of the last layer.
            cls_index (`jnp.array` of shape `[batch_size]` or `[batch_size, ...]` where ... are optional leading dimensions of `hidden_states`, *optional*):
                Used if `summary_type == "cls_index"` and takes the last token of the sequence as classification token.

        Returns:
            `jnp.array`: The summary of the sequence hidden states.
        '''

class FlaxElectraForMultipleChoiceModule(nn.Module):
    config: ElectraConfig
    dtype: jnp.dtype
    gradient_checkpointing: bool
    electra: Incomplete
    sequence_summary: Incomplete
    classifier: Incomplete
    def setup(self) -> None: ...
    def __call__(self, input_ids, attention_mask: Incomplete | None = None, token_type_ids: Incomplete | None = None, position_ids: Incomplete | None = None, head_mask: Incomplete | None = None, deterministic: bool = True, output_attentions: bool = False, output_hidden_states: bool = False, return_dict: bool = True): ...

class FlaxElectraForMultipleChoice(FlaxElectraPreTrainedModel):
    module_class = FlaxElectraForMultipleChoiceModule

class FlaxElectraForQuestionAnsweringModule(nn.Module):
    config: ElectraConfig
    dtype: jnp.dtype
    gradient_checkpointing: bool
    electra: Incomplete
    qa_outputs: Incomplete
    def setup(self) -> None: ...
    def __call__(self, input_ids, attention_mask: Incomplete | None = None, token_type_ids: Incomplete | None = None, position_ids: Incomplete | None = None, head_mask: Incomplete | None = None, deterministic: bool = True, output_attentions: bool = False, output_hidden_states: bool = False, return_dict: bool = True): ...

class FlaxElectraForQuestionAnswering(FlaxElectraPreTrainedModel):
    module_class = FlaxElectraForQuestionAnsweringModule

class FlaxElectraClassificationHead(nn.Module):
    """Head for sentence-level classification tasks."""
    config: ElectraConfig
    dtype: jnp.dtype
    dense: Incomplete
    dropout: Incomplete
    out_proj: Incomplete
    def setup(self) -> None: ...
    def __call__(self, hidden_states, deterministic: bool = True): ...

class FlaxElectraForSequenceClassificationModule(nn.Module):
    config: ElectraConfig
    dtype: jnp.dtype
    gradient_checkpointing: bool
    electra: Incomplete
    classifier: Incomplete
    def setup(self) -> None: ...
    def __call__(self, input_ids, attention_mask: Incomplete | None = None, token_type_ids: Incomplete | None = None, position_ids: Incomplete | None = None, head_mask: Incomplete | None = None, deterministic: bool = True, output_attentions: bool = False, output_hidden_states: bool = False, return_dict: bool = True): ...

class FlaxElectraForSequenceClassification(FlaxElectraPreTrainedModel):
    module_class = FlaxElectraForSequenceClassificationModule

class FlaxElectraForCausalLMModule(nn.Module):
    config: ElectraConfig
    dtype: jnp.dtype
    gradient_checkpointing: bool
    electra: Incomplete
    generator_predictions: Incomplete
    generator_lm_head: Incomplete
    def setup(self) -> None: ...
    def __call__(self, input_ids, attention_mask: Optional[jnp.ndarray] = None, token_type_ids: Optional[jnp.ndarray] = None, position_ids: Optional[jnp.ndarray] = None, head_mask: Optional[jnp.ndarray] = None, encoder_hidden_states: Optional[jnp.ndarray] = None, encoder_attention_mask: Optional[jnp.ndarray] = None, init_cache: bool = False, deterministic: bool = True, output_attentions: bool = False, output_hidden_states: bool = False, return_dict: bool = True): ...

class FlaxElectraForCausalLM(FlaxElectraPreTrainedModel):
    module_class = FlaxElectraForCausalLMModule
    def prepare_inputs_for_generation(self, input_ids, max_length, attention_mask: Optional[jnp.DeviceArray] = None): ...
    def update_inputs_for_generation(self, model_outputs, model_kwargs): ...
