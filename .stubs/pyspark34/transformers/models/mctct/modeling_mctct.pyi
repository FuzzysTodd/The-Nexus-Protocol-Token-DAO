import torch
from ...activations import ACT2FN as ACT2FN
from ...deepspeed import is_deepspeed_zero3_enabled as is_deepspeed_zero3_enabled
from ...file_utils import add_code_sample_docstrings as add_code_sample_docstrings, add_start_docstrings as add_start_docstrings, add_start_docstrings_to_model_forward as add_start_docstrings_to_model_forward
from ...modeling_outputs import BaseModelOutput as BaseModelOutput, CausalLMOutput as CausalLMOutput
from ...modeling_utils import PreTrainedModel as PreTrainedModel, apply_chunking_to_forward as apply_chunking_to_forward, find_pruneable_heads_and_indices as find_pruneable_heads_and_indices, prune_linear_layer as prune_linear_layer
from ...pytorch_utils import is_torch_less_than_1_9 as is_torch_less_than_1_9
from ...utils import logging as logging
from .configuration_mctct import MCTCTConfig as MCTCTConfig
from _typeshed import Incomplete
from torch import nn
from typing import Optional, Tuple, Union

logger: Incomplete
MCTCT_PRETRAINED_MODEL_ARCHIVE_LIST: Incomplete

class MCTCTConv1dSubsampler(nn.Module):
    """
    Convolutional subsampler: a stack of 1D convolution (along temporal dimension) followed by non-linear activation
    via gated linear units (https://arxiv.org/abs/1911.08460)
    """
    config: Incomplete
    glu_dim: Incomplete
    dropout: Incomplete
    num_layers: Incomplete
    in_channels: Incomplete
    mid_channels: Incomplete
    out_channels: Incomplete
    kernel_size: Incomplete
    stride: Incomplete
    conv_layers: Incomplete
    def __init__(self, config) -> None: ...
    def forward(self, input_features): ...

class MCTCTEmbeddings(nn.Module):
    """Construct the embeddings from word, position and token_type embeddings."""
    word_embeddings: Incomplete
    position_embeddings: Incomplete
    token_type_embeddings: Incomplete
    LayerNorm: Incomplete
    dropout: Incomplete
    def __init__(self, config) -> None: ...
    def forward(self, input_features: Incomplete | None = None, token_type_ids: Incomplete | None = None, position_ids: Incomplete | None = None, inputs_embeds: Incomplete | None = None, past_key_values_length: int = 0): ...

class MCTCTSelfAttention(nn.Module):
    num_attention_heads: Incomplete
    attention_head_size: Incomplete
    all_head_size: Incomplete
    query: Incomplete
    key: Incomplete
    value: Incomplete
    dropout: Incomplete
    max_position_embeddings: Incomplete
    distance_embedding: Incomplete
    is_decoder: Incomplete
    def __init__(self, config) -> None: ...
    def transpose_for_scores(self, x): ...
    def reshape_fortran(self, x, shape): ...
    def relative_position_embedding_rotate(self, scores): ...
    def forward(self, hidden_states, attention_mask: Incomplete | None = None, head_mask: Incomplete | None = None, output_attentions: bool = False): ...

class MCTCTLayerNorm(nn.Module):
    singleton_weight: Incomplete
    singleton_bias: Incomplete
    def __init__(self) -> None: ...
    def forward(self, hidden_states): ...

class MCTCTSelfOutput(nn.Module):
    config: Incomplete
    dense: Incomplete
    LayerNorm: Incomplete
    dropout: Incomplete
    def __init__(self, config) -> None: ...
    def forward(self, hidden_states, input_tensor): ...

class MCTCTAttention(nn.Module):
    self: Incomplete
    output: Incomplete
    pruned_heads: Incomplete
    def __init__(self, config) -> None: ...
    def prune_heads(self, heads) -> None: ...
    def forward(self, hidden_states, attention_mask: Incomplete | None = None, head_mask: Incomplete | None = None, output_attentions: bool = False): ...

class MCTCTIntermediate(nn.Module):
    dense: Incomplete
    intermediate_act_fn: Incomplete
    def __init__(self, config) -> None: ...
    def forward(self, hidden_states): ...

class MCTCTOutput(nn.Module):
    dense: Incomplete
    LayerNorm: Incomplete
    dropout: Incomplete
    def __init__(self, config) -> None: ...
    def forward(self, hidden_states, input_tensor): ...

class MCTCTLayer(nn.Module):
    seq_len_dim: int
    chunk_size_feed_forward: Incomplete
    intermediate: Incomplete
    attention: Incomplete
    is_decoder: Incomplete
    output: Incomplete
    def __init__(self, config: MCTCTConfig) -> None: ...
    def forward(self, hidden_states, attention_mask: Incomplete | None = None, head_mask: Incomplete | None = None, output_attentions: bool = False): ...
    def feed_forward_chunk(self, attention_output): ...

class MCTCTPreTrainedModel(PreTrainedModel):
    """
    An abstract class to handle weights initialization and a simple interface for downloading and loading pretrained
    models.
    """
    config_class = MCTCTConfig
    base_model_prefix: str
    main_input_name: str
    supports_gradient_checkpointing: bool

MCTCT_START_DOCSTRING: str
MCTCT_INPUTS_DOCSTRING: str

class MCTCTEncoder(MCTCTPreTrainedModel):
    hidden_dropout_prob: Incomplete
    layer_norm: Incomplete
    conv: Incomplete
    layers: Incomplete
    gradient_checkpointing: bool
    def __init__(self, config: MCTCTConfig) -> None: ...
    def forward(self, input_features: torch.Tensor, attention_mask: torch.Tensor, head_mask: torch.Tensor, output_attentions: bool = False, output_hidden_states: bool = False, return_dict: bool = True) -> Union[Tuple, BaseModelOutput]: ...

class MCTCTModel(MCTCTPreTrainedModel):
    config: Incomplete
    encoder: Incomplete
    def __init__(self, config) -> None: ...
    def forward(self, input_features: torch.Tensor, attention_mask: Optional[torch.Tensor] = None, head_mask: Optional[torch.Tensor] = None, output_attentions: Optional[bool] = None, output_hidden_states: Optional[bool] = None, return_dict: Optional[bool] = None) -> Union[Tuple, BaseModelOutput]: ...

class MCTCTForCTC(MCTCTPreTrainedModel):
    mctct: Incomplete
    ctc_head: Incomplete
    def __init__(self, config) -> None: ...
    def forward(self, input_features: torch.Tensor, attention_mask: Optional[torch.Tensor] = None, head_mask: Optional[torch.Tensor] = None, output_attentions: Optional[bool] = None, output_hidden_states: Optional[bool] = None, return_dict: Optional[bool] = None, labels: Optional[torch.LongTensor] = None) -> Union[Tuple, CausalLMOutput]:
        """
        labels (`torch.LongTensor` of shape `(batch_size, target_length)`, *optional*):
            Labels for connectionist temporal classification. Note that `target_length` has to be smaller or equal to
            the sequence length of the output logits. Indices are selected in `[-100, 0, ..., config.vocab_size - 1]`.
            All labels set to `-100` are ignored (masked), the loss is only computed for labels in `[0, ...,
            config.vocab_size - 1]`.
        """
