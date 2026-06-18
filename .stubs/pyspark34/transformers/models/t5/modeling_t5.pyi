import torch
from ...activations import ACT2FN as ACT2FN
from ...modeling_outputs import BaseModelOutput as BaseModelOutput, BaseModelOutputWithPastAndCrossAttentions as BaseModelOutputWithPastAndCrossAttentions, Seq2SeqLMOutput as Seq2SeqLMOutput, Seq2SeqModelOutput as Seq2SeqModelOutput
from ...modeling_utils import PreTrainedModel as PreTrainedModel
from ...pytorch_utils import ALL_LAYERNORM_LAYERS as ALL_LAYERNORM_LAYERS, find_pruneable_heads_and_indices as find_pruneable_heads_and_indices, prune_linear_layer as prune_linear_layer
from ...utils import DUMMY_INPUTS as DUMMY_INPUTS, DUMMY_MASK as DUMMY_MASK, add_start_docstrings as add_start_docstrings, add_start_docstrings_to_model_forward as add_start_docstrings_to_model_forward, is_torch_fx_proxy as is_torch_fx_proxy, logging as logging, replace_return_docstrings as replace_return_docstrings
from ...utils.model_parallel_utils import assert_device_map as assert_device_map, get_device_map as get_device_map
from .configuration_t5 import T5Config as T5Config
from _typeshed import Incomplete
from apex.normalization import FusedRMSNorm
from torch import nn
from typing import Optional, Tuple, Union

logger: Incomplete
T5_PRETRAINED_MODEL_ARCHIVE_LIST: Incomplete

def load_tf_weights_in_t5(model, config, tf_checkpoint_path):
    """Load tf checkpoints in a pytorch model."""

PARALLELIZE_DOCSTRING: str
DEPARALLELIZE_DOCSTRING: str

class T5LayerNorm(nn.Module):
    weight: Incomplete
    variance_epsilon: Incomplete
    def __init__(self, hidden_size, eps: float = 1e-06) -> None:
        """
        Construct a layernorm module in the T5 style. No bias and no subtraction of mean.
        """
    def forward(self, hidden_states): ...
T5LayerNorm = FusedRMSNorm

class T5DenseActDense(nn.Module):
    wi: Incomplete
    wo: Incomplete
    dropout: Incomplete
    act: Incomplete
    def __init__(self, config: T5Config) -> None: ...
    def forward(self, hidden_states): ...

class T5DenseGatedActDense(nn.Module):
    wi_0: Incomplete
    wi_1: Incomplete
    wo: Incomplete
    dropout: Incomplete
    act: Incomplete
    def __init__(self, config: T5Config) -> None: ...
    def forward(self, hidden_states): ...

class T5LayerFF(nn.Module):
    DenseReluDense: Incomplete
    layer_norm: Incomplete
    dropout: Incomplete
    def __init__(self, config: T5Config) -> None: ...
    def forward(self, hidden_states): ...

class T5Attention(nn.Module):
    is_decoder: Incomplete
    has_relative_attention_bias: Incomplete
    relative_attention_num_buckets: Incomplete
    relative_attention_max_distance: Incomplete
    d_model: Incomplete
    key_value_proj_dim: Incomplete
    n_heads: Incomplete
    dropout: Incomplete
    inner_dim: Incomplete
    q: Incomplete
    k: Incomplete
    v: Incomplete
    o: Incomplete
    relative_attention_bias: Incomplete
    pruned_heads: Incomplete
    gradient_checkpointing: bool
    def __init__(self, config: T5Config, has_relative_attention_bias: bool = False) -> None: ...
    def prune_heads(self, heads) -> None: ...
    def compute_bias(self, query_length, key_length, device: Incomplete | None = None):
        """Compute binned relative position bias"""
    def forward(self, hidden_states, mask: Incomplete | None = None, key_value_states: Incomplete | None = None, position_bias: Incomplete | None = None, past_key_value: Incomplete | None = None, layer_head_mask: Incomplete | None = None, query_length: Incomplete | None = None, use_cache: bool = False, output_attentions: bool = False):
        """
        Self-attention (if key_value_states is None) or attention over source sentence (provided by key_value_states).
        """

class T5LayerSelfAttention(nn.Module):
    SelfAttention: Incomplete
    layer_norm: Incomplete
    dropout: Incomplete
    def __init__(self, config, has_relative_attention_bias: bool = False) -> None: ...
    def forward(self, hidden_states, attention_mask: Incomplete | None = None, position_bias: Incomplete | None = None, layer_head_mask: Incomplete | None = None, past_key_value: Incomplete | None = None, use_cache: bool = False, output_attentions: bool = False): ...

class T5LayerCrossAttention(nn.Module):
    EncDecAttention: Incomplete
    layer_norm: Incomplete
    dropout: Incomplete
    def __init__(self, config) -> None: ...
    def forward(self, hidden_states, key_value_states, attention_mask: Incomplete | None = None, position_bias: Incomplete | None = None, layer_head_mask: Incomplete | None = None, past_key_value: Incomplete | None = None, use_cache: bool = False, query_length: Incomplete | None = None, output_attentions: bool = False): ...

class T5Block(nn.Module):
    is_decoder: Incomplete
    layer: Incomplete
    def __init__(self, config, has_relative_attention_bias: bool = False) -> None: ...
    def forward(self, hidden_states, attention_mask: Incomplete | None = None, position_bias: Incomplete | None = None, encoder_hidden_states: Incomplete | None = None, encoder_attention_mask: Incomplete | None = None, encoder_decoder_position_bias: Incomplete | None = None, layer_head_mask: Incomplete | None = None, cross_attn_layer_head_mask: Incomplete | None = None, past_key_value: Incomplete | None = None, use_cache: bool = False, output_attentions: bool = False, return_dict: bool = True): ...

class T5PreTrainedModel(PreTrainedModel):
    """
    An abstract class to handle weights initialization and a simple interface for downloading and loading pretrained
    models.
    """
    config_class = T5Config
    load_tf_weights = load_tf_weights_in_t5
    base_model_prefix: str
    is_parallelizable: bool
    supports_gradient_checkpointing: bool
    @property
    def dummy_inputs(self): ...

class T5Stack(T5PreTrainedModel):
    embed_tokens: Incomplete
    is_decoder: Incomplete
    block: Incomplete
    final_layer_norm: Incomplete
    dropout: Incomplete
    model_parallel: bool
    device_map: Incomplete
    gradient_checkpointing: bool
    def __init__(self, config, embed_tokens: Incomplete | None = None) -> None: ...
    first_device: Incomplete
    last_device: Incomplete
    def parallelize(self, device_map: Incomplete | None = None) -> None: ...
    def deparallelize(self) -> None: ...
    def get_input_embeddings(self): ...
    def set_input_embeddings(self, new_embeddings) -> None: ...
    def forward(self, input_ids: Incomplete | None = None, attention_mask: Incomplete | None = None, encoder_hidden_states: Incomplete | None = None, encoder_attention_mask: Incomplete | None = None, inputs_embeds: Incomplete | None = None, head_mask: Incomplete | None = None, cross_attn_head_mask: Incomplete | None = None, past_key_values: Incomplete | None = None, use_cache: Incomplete | None = None, output_attentions: Incomplete | None = None, output_hidden_states: Incomplete | None = None, return_dict: Incomplete | None = None): ...

T5_START_DOCSTRING: str
T5_INPUTS_DOCSTRING: str
T5_ENCODER_INPUTS_DOCSTRING: str

class T5Model(T5PreTrainedModel):
    shared: Incomplete
    encoder: Incomplete
    decoder: Incomplete
    model_parallel: bool
    device_map: Incomplete
    def __init__(self, config: T5Config) -> None: ...
    def parallelize(self, device_map: Incomplete | None = None) -> None: ...
    def deparallelize(self) -> None: ...
    def get_input_embeddings(self): ...
    def set_input_embeddings(self, new_embeddings) -> None: ...
    def get_encoder(self): ...
    def get_decoder(self): ...
    def forward(self, input_ids: Optional[torch.LongTensor] = None, attention_mask: Optional[torch.FloatTensor] = None, decoder_input_ids: Optional[torch.LongTensor] = None, decoder_attention_mask: Optional[torch.BoolTensor] = None, head_mask: Optional[torch.FloatTensor] = None, decoder_head_mask: Optional[torch.FloatTensor] = None, cross_attn_head_mask: Optional[torch.Tensor] = None, encoder_outputs: Optional[Tuple[Tuple[torch.FloatTensor]]] = None, past_key_values: Optional[Tuple[Tuple[torch.FloatTensor]]] = None, inputs_embeds: Optional[torch.Tensor] = None, decoder_inputs_embeds: Optional[torch.Tensor] = None, use_cache: Optional[bool] = None, output_attentions: Optional[bool] = None, output_hidden_states: Optional[bool] = None, return_dict: Optional[bool] = None) -> Union[Tuple[torch.FloatTensor], Seq2SeqModelOutput]:
        '''
        Returns:

        Example:

        ```python
        >>> from transformers import AutoTokenizer, T5Model

        >>> tokenizer = AutoTokenizer.from_pretrained("t5-small")
        >>> model = T5Model.from_pretrained("t5-small")

        >>> input_ids = tokenizer(
        ...     "Studies have been shown that owning a dog is good for you", return_tensors="pt"
        ... ).input_ids  # Batch size 1
        >>> decoder_input_ids = tokenizer("Studies show that", return_tensors="pt").input_ids  # Batch size 1

        >>> # preprocess: Prepend decoder_input_ids with start token which is pad token for T5Model.
        >>> # This is not needed for torch\'s T5ForConditionalGeneration as it does this internally using labels arg.
        >>> decoder_input_ids = model._shift_right(decoder_input_ids)

        >>> # forward pass
        >>> outputs = model(input_ids=input_ids, decoder_input_ids=decoder_input_ids)
        >>> last_hidden_states = outputs.last_hidden_state
        ```'''

class T5ForConditionalGeneration(T5PreTrainedModel):
    model_dim: Incomplete
    shared: Incomplete
    encoder: Incomplete
    decoder: Incomplete
    lm_head: Incomplete
    model_parallel: bool
    device_map: Incomplete
    def __init__(self, config: T5Config) -> None: ...
    def parallelize(self, device_map: Incomplete | None = None) -> None: ...
    def deparallelize(self) -> None: ...
    def get_input_embeddings(self): ...
    def set_input_embeddings(self, new_embeddings) -> None: ...
    def set_output_embeddings(self, new_embeddings) -> None: ...
    def get_output_embeddings(self): ...
    def get_encoder(self): ...
    def get_decoder(self): ...
    def forward(self, input_ids: Optional[torch.LongTensor] = None, attention_mask: Optional[torch.FloatTensor] = None, decoder_input_ids: Optional[torch.LongTensor] = None, decoder_attention_mask: Optional[torch.BoolTensor] = None, head_mask: Optional[torch.FloatTensor] = None, decoder_head_mask: Optional[torch.FloatTensor] = None, cross_attn_head_mask: Optional[torch.Tensor] = None, encoder_outputs: Optional[Tuple[Tuple[torch.Tensor]]] = None, past_key_values: Optional[Tuple[Tuple[torch.Tensor]]] = None, inputs_embeds: Optional[torch.FloatTensor] = None, decoder_inputs_embeds: Optional[torch.FloatTensor] = None, labels: Optional[torch.LongTensor] = None, use_cache: Optional[bool] = None, output_attentions: Optional[bool] = None, output_hidden_states: Optional[bool] = None, return_dict: Optional[bool] = None) -> Union[Tuple[torch.FloatTensor], Seq2SeqLMOutput]:
        '''
        labels (`torch.LongTensor` of shape `(batch_size,)`, *optional*):
            Labels for computing the sequence classification/regression loss. Indices should be in `[-100, 0, ...,
            config.vocab_size - 1]`. All labels set to `-100` are ignored (masked), the loss is only computed for
            labels in `[0, ..., config.vocab_size]`

        Returns:

        Examples:

        ```python
        >>> from transformers import AutoTokenizer, T5ForConditionalGeneration

        >>> tokenizer = AutoTokenizer.from_pretrained("t5-small")
        >>> model = T5ForConditionalGeneration.from_pretrained("t5-small")

        >>> # training
        >>> input_ids = tokenizer("The <extra_id_0> walks in <extra_id_1> park", return_tensors="pt").input_ids
        >>> labels = tokenizer("<extra_id_0> cute dog <extra_id_1> the <extra_id_2>", return_tensors="pt").input_ids
        >>> outputs = model(input_ids=input_ids, labels=labels)
        >>> loss = outputs.loss
        >>> logits = outputs.logits

        >>> # inference
        >>> input_ids = tokenizer(
        ...     "summarize: studies have shown that owning a dog is good for you", return_tensors="pt"
        ... ).input_ids  # Batch size 1
        >>> outputs = model.generate(input_ids)
        >>> print(tokenizer.decode(outputs[0], skip_special_tokens=True))
        >>> # studies have shown that owning a dog is good for you.
        ```'''
    def prepare_inputs_for_generation(self, input_ids, past_key_values: Incomplete | None = None, attention_mask: Incomplete | None = None, head_mask: Incomplete | None = None, decoder_head_mask: Incomplete | None = None, cross_attn_head_mask: Incomplete | None = None, use_cache: Incomplete | None = None, encoder_outputs: Incomplete | None = None, **kwargs): ...
    def prepare_decoder_input_ids_from_labels(self, labels: torch.Tensor): ...

class T5EncoderModel(T5PreTrainedModel):
    shared: Incomplete
    encoder: Incomplete
    model_parallel: bool
    device_map: Incomplete
    def __init__(self, config: T5Config) -> None: ...
    def parallelize(self, device_map: Incomplete | None = None) -> None: ...
    def deparallelize(self) -> None: ...
    def get_input_embeddings(self): ...
    def set_input_embeddings(self, new_embeddings) -> None: ...
    def get_encoder(self): ...
    def forward(self, input_ids: Optional[torch.LongTensor] = None, attention_mask: Optional[torch.FloatTensor] = None, head_mask: Optional[torch.FloatTensor] = None, inputs_embeds: Optional[torch.FloatTensor] = None, output_attentions: Optional[bool] = None, output_hidden_states: Optional[bool] = None, return_dict: Optional[bool] = None) -> Union[Tuple[torch.FloatTensor], BaseModelOutput]:
        '''
        Returns:

        Example:

        ```python
        >>> from transformers import AutoTokenizer, T5EncoderModel

        >>> tokenizer = AutoTokenizer.from_pretrained("t5-small")
        >>> model = T5EncoderModel.from_pretrained("t5-small")
        >>> input_ids = tokenizer(
        ...     "Studies have been shown that owning a dog is good for you", return_tensors="pt"
        ... ).input_ids  # Batch size 1
        >>> outputs = model(input_ids=input_ids)
        >>> last_hidden_states = outputs.last_hidden_state
        ```'''
