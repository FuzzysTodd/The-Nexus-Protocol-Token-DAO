import torch
from ...file_utils import add_code_sample_docstrings as add_code_sample_docstrings, add_start_docstrings as add_start_docstrings, add_start_docstrings_to_model_forward as add_start_docstrings_to_model_forward
from ...modeling_outputs import BaseModelOutputWithPastAndCrossAttentions as BaseModelOutputWithPastAndCrossAttentions, CausalLMOutputWithCrossAttentions as CausalLMOutputWithCrossAttentions, QuestionAnsweringModelOutput as QuestionAnsweringModelOutput, SequenceClassifierOutputWithPast as SequenceClassifierOutputWithPast, TokenClassifierOutput as TokenClassifierOutput
from ...modeling_utils import PreTrainedModel as PreTrainedModel
from ...utils import logging as logging
from .configuration_bloom import BloomConfig as BloomConfig
from _typeshed import Incomplete
from torch import nn
from typing import Optional, Tuple, Union

logger: Incomplete
BLOOM_PRETRAINED_MODEL_ARCHIVE_LIST: Incomplete

def build_alibi_tensor(attention_mask: torch.Tensor, num_heads: int, dtype: torch.dtype) -> torch.Tensor:
    """
    Link to paper: https://arxiv.org/abs/2108.12409 Alibi tensor is not causal as the original paper mentions, it
    relies on a translation invariance of softmax for quick implementation: with l being a tensor, and a fixed value
    `softmax(l+a) = softmax(l)`. Based on
    https://github.com/ofirpress/attention_with_linear_biases/blob/a35aaca144e0eb6b789dfcb46784c4b8e31b7983/fairseq/models/transformer.py#L742
    TODO @thomasw21 this doesn't work as nicely due to the masking strategy, and so masking varies slightly.

    Args:
    Returns tensor shaped (batch_size * num_heads, 1, max_seq_len)
        attention_mask (`torch.Tensor`):
            Token-wise attention mask, this should be of shape (batch_size, max_seq_len).
        num_heads (`int`, *required*):
            number of heads
        dtype (`torch.dtype`, *optional*, default=`torch.bfloat16`):
            dtype of the output tensor
    """
def dropout_add(x: torch.Tensor, residual: torch.Tensor, prob: float, training: bool) -> torch.Tensor:
    """
    Dropout add function

    Args:
        x (`torch.tensor`, *required*):
            input tensor
        residual (`torch.tensor`, *required*):
            esidual tensor
        prob (`float`, *required*):
            dropout probability
        training (`bool`, *required*):
            training mode
    """
def bloom_gelu_forward(x: torch.Tensor) -> torch.Tensor:
    """
    Custom bias GELU function. Adapted from Megatron-DeepSpeed code. Here we use a simple implementation (inference) to
    make the model jitable.

    Args:
        x (`torch.tensor`, *required*):
            input hidden states
    """
def bloom_gelu_back(g: torch.Tensor, x: torch.Tensor) -> torch.Tensor:
    """
    gradient of tanh approximation of gelu gradient of actual gelu is: 0.5 * (1. + torch.erf(x * 0.70710678)) +
    0.3989423 * x * torch.exp(-0.5 * x * x)

    Args:
        g (`torch.tensor`, *required*):
            gradient output tensor
        x (`torch.tensor`, *required*):
            input tensor
    """

class GeLUFunction(torch.autograd.Function):
    @staticmethod
    def forward(ctx, input: torch.Tensor) -> torch.Tensor: ...
    @staticmethod
    def backward(ctx, grad_output: torch.Tensor) -> torch.Tensor: ...

class BloomGelu(nn.Module):
    """
    BloomBiasGelu wrapper function that make use of the simple function on inference mode to make the model
    torchscriptable and use the autograd function in training mode to get the accurate results of the gradients Partly
    copied from Megatron-DeepSpeed code and adapted for our needs

    See here why autograd functions are not torchscriptable: https://github.com/pytorch/pytorch/issues/22329
    """
    def __init__(self) -> None: ...
    def forward(self, x: torch.Tensor) -> torch.Tensor: ...

class BloomAttention(nn.Module):
    pretraining_tp: Incomplete
    slow_but_exact: Incomplete
    hidden_size: Incomplete
    num_heads: Incomplete
    head_dim: Incomplete
    split_size: Incomplete
    hidden_dropout: Incomplete
    inv_norm_factor: Incomplete
    beta: float
    query_key_value: Incomplete
    dense: Incomplete
    attention_dropout: Incomplete
    def __init__(self, config: BloomConfig) -> None: ...
    def forward(self, hidden_states: torch.Tensor, residual: torch.Tensor, alibi: torch.Tensor, attention_mask: torch.Tensor, layer_past: Optional[Tuple[torch.Tensor, torch.Tensor]] = None, head_mask: Optional[torch.Tensor] = None, use_cache: bool = False, output_attentions: bool = False): ...

class BloomMLP(nn.Module):
    pretraining_tp: Incomplete
    slow_but_exact: Incomplete
    dense_h_to_4h: Incomplete
    gelu_impl: Incomplete
    dense_4h_to_h: Incomplete
    hidden_dropout: Incomplete
    def __init__(self, config: BloomConfig) -> None: ...
    def forward(self, hidden_states: torch.Tensor, residual: torch.Tensor) -> torch.Tensor: ...

class BloomBlock(nn.Module):
    input_layernorm: Incomplete
    num_heads: Incomplete
    self_attention: Incomplete
    post_attention_layernorm: Incomplete
    mlp: Incomplete
    apply_residual_connection_post_layernorm: Incomplete
    hidden_dropout: Incomplete
    def __init__(self, config: BloomConfig) -> None: ...
    def forward(self, hidden_states: torch.Tensor, alibi: torch.Tensor, attention_mask: torch.Tensor, layer_past: Optional[Tuple[torch.Tensor, torch.Tensor]] = None, head_mask: Optional[torch.Tensor] = None, use_cache: bool = False, output_attentions: bool = False): ...

class BloomPreTrainedModel(PreTrainedModel):
    config_class = BloomConfig
    base_model_prefix: str
    supports_gradient_checkpointing: bool
    def __init__(self, *inputs, **kwargs) -> None: ...

BLOOM_START_DOCSTRING: str
BLOOM_INPUTS_DOCSTRING: str

class BloomModel(BloomPreTrainedModel):
    embed_dim: Incomplete
    num_heads: Incomplete
    word_embeddings: Incomplete
    word_embeddings_layernorm: Incomplete
    h: Incomplete
    ln_f: Incomplete
    gradient_checkpointing: bool
    def __init__(self, config: BloomConfig) -> None: ...
    def get_input_embeddings(self): ...
    def set_input_embeddings(self, new_embeddings: torch.Tensor): ...
    def forward(self, input_ids: Optional[torch.LongTensor] = None, past_key_values: Optional[Tuple[Tuple[torch.Tensor, torch.Tensor], ...]] = None, attention_mask: Optional[torch.Tensor] = None, head_mask: Optional[torch.LongTensor] = None, inputs_embeds: Optional[torch.LongTensor] = None, use_cache: Optional[bool] = None, output_attentions: Optional[bool] = None, output_hidden_states: Optional[bool] = None, return_dict: Optional[bool] = None, **deprecated_arguments) -> Union[Tuple[torch.Tensor, ...], BaseModelOutputWithPastAndCrossAttentions]: ...

class BloomForCausalLM(BloomPreTrainedModel):
    transformer: Incomplete
    lm_head: Incomplete
    def __init__(self, config: BloomConfig) -> None: ...
    def get_output_embeddings(self): ...
    def set_output_embeddings(self, new_embeddings: torch.Tensor): ...
    def prepare_inputs_for_generation(self, input_ids: torch.LongTensor, past_key_values: Optional[torch.Tensor] = None, attention_mask: Optional[torch.Tensor] = None, **kwargs) -> dict: ...
    def forward(self, input_ids: Optional[torch.LongTensor] = None, past_key_values: Optional[Tuple[Tuple[torch.Tensor, torch.Tensor], ...]] = None, attention_mask: Optional[torch.Tensor] = None, head_mask: Optional[torch.Tensor] = None, inputs_embeds: Optional[torch.Tensor] = None, labels: Optional[torch.Tensor] = None, use_cache: Optional[bool] = None, output_attentions: Optional[bool] = None, output_hidden_states: Optional[bool] = None, return_dict: Optional[bool] = None, **deprecated_arguments) -> Union[Tuple[torch.Tensor], CausalLMOutputWithCrossAttentions]:
        """
        labels (`torch.LongTensor` of shape `(batch_size, sequence_length)`, *optional*):
            Labels for language modeling. Note that the labels **are shifted** inside the model, i.e. you can set
            `labels = input_ids` Indices are selected in `[-100, 0, ..., config.vocab_size]` All labels set to `-100`
            are ignored (masked), the loss is only computed for labels in `[0, ..., config.vocab_size]`
        """

class BloomForSequenceClassification(BloomPreTrainedModel):
    num_labels: Incomplete
    transformer: Incomplete
    score: Incomplete
    def __init__(self, config: BloomConfig) -> None: ...
    def forward(self, input_ids: Optional[torch.LongTensor] = None, past_key_values: Optional[Tuple[Tuple[torch.Tensor, torch.Tensor], ...]] = None, attention_mask: Optional[torch.Tensor] = None, head_mask: Optional[torch.Tensor] = None, inputs_embeds: Optional[torch.Tensor] = None, labels: Optional[torch.Tensor] = None, use_cache: Optional[bool] = None, output_attentions: Optional[bool] = None, output_hidden_states: Optional[bool] = None, return_dict: Optional[bool] = None, **deprecated_arguments) -> Union[Tuple[torch.Tensor], SequenceClassifierOutputWithPast]:
        """
        labels (`torch.LongTensor` of shape `(batch_size,)`, *optional*):
            Labels for computing the sequence classification/regression loss. Indices should be in `[0, ...,
            config.num_labels - 1]`. If `config.num_labels == 1` a regression loss is computed (Mean-Square loss), If
            `config.num_labels > 1` a classification loss is computed (Cross-Entropy).
        """

class BloomForTokenClassification(BloomPreTrainedModel):
    num_labels: Incomplete
    transformer: Incomplete
    dropout: Incomplete
    classifier: Incomplete
    def __init__(self, config: BloomConfig) -> None: ...
    def forward(self, input_ids: Optional[torch.LongTensor] = None, past_key_values: Optional[Tuple[Tuple[torch.Tensor, torch.Tensor], ...]] = None, attention_mask: Optional[torch.Tensor] = None, head_mask: Optional[torch.Tensor] = None, inputs_embeds: Optional[torch.Tensor] = None, labels: Optional[torch.Tensor] = None, use_cache: Optional[bool] = None, output_attentions: Optional[bool] = None, output_hidden_states: Optional[bool] = None, return_dict: Optional[bool] = None, **deprecated_arguments) -> Union[Tuple[torch.Tensor], TokenClassifierOutput]:
        """
        labels (`torch.LongTensor` of shape `(batch_size,)`, *optional*):
            Labels for computing the sequence classification/regression loss. Indices should be in `[0, ...,
            config.num_labels - 1]`. If `config.num_labels == 1` a regression loss is computed (Mean-Square loss), If
            `config.num_labels > 1` a classification loss is computed (Cross-Entropy).
        """

class BloomForQuestionAnswering(BloomPreTrainedModel):
    transformer: Incomplete
    qa_outputs: Incomplete
    def __init__(self, config) -> None: ...
    def forward(self, input_ids: Optional[torch.LongTensor] = None, attention_mask: Optional[torch.FloatTensor] = None, position_ids: Optional[torch.LongTensor] = None, head_mask: Optional[torch.FloatTensor] = None, inputs_embeds: Optional[torch.FloatTensor] = None, start_positions: Optional[torch.LongTensor] = None, end_positions: Optional[torch.LongTensor] = None, output_attentions: Optional[bool] = None, output_hidden_states: Optional[bool] = None, return_dict: Optional[bool] = None) -> Union[Tuple, QuestionAnsweringModelOutput]:
        """
        start_positions (`torch.LongTensor` of shape `(batch_size,)`, *optional*):
            Labels for position (index) of the start of the labelled span for computing the token classification loss.
            Positions are clamped to the length of the sequence (`sequence_length`). Position outside of the sequence
            are not taken into account for computing the loss.
        end_positions (`torch.LongTensor` of shape `(batch_size,)`, *optional*):
            Labels for position (index) of the end of the labelled span for computing the token classification loss.
            Positions are clamped to the length of the sequence (`sequence_length`). Position outside of the sequence
            are not taken into account for computing the loss.
        """
