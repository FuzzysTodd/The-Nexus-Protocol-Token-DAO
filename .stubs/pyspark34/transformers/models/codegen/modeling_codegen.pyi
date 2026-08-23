import torch
from ...activations import ACT2FN as ACT2FN
from ...modeling_outputs import BaseModelOutputWithPast as BaseModelOutputWithPast, CausalLMOutputWithPast as CausalLMOutputWithPast
from ...modeling_utils import PreTrainedModel as PreTrainedModel
from ...utils import add_code_sample_docstrings as add_code_sample_docstrings, add_start_docstrings as add_start_docstrings, add_start_docstrings_to_model_forward as add_start_docstrings_to_model_forward, logging as logging
from .configuration_codegen import CodeGenConfig as CodeGenConfig
from _typeshed import Incomplete
from torch import nn
from typing import Optional, Tuple, Union

logger: Incomplete
CODEGEN_PRETRAINED_MODEL_ARCHIVE_LIST: Incomplete

def fixed_pos_embedding(x, seq_dim: int = 1, seq_len: Incomplete | None = None): ...
def rotate_every_two(x): ...
def duplicate_interleave(m):
    """
    A simple version of `torch.repeat_interleave` for duplicating a matrix while interleaving the copy.
    """
def apply_rotary_pos_emb(x, sincos, offset: int = 0): ...

class CodeGenAttention(nn.Module):
    attn_dropout: Incomplete
    resid_dropout: Incomplete
    embed_dim: Incomplete
    num_attention_heads: Incomplete
    head_dim: Incomplete
    scale_attn: Incomplete
    qkv_proj: Incomplete
    out_proj: Incomplete
    rotary_dim: Incomplete
    def __init__(self, config) -> None: ...
    def forward(self, hidden_states: Optional[torch.FloatTensor], attention_mask: Optional[torch.FloatTensor] = None, layer_past: Optional[Tuple[torch.Tensor]] = None, head_mask: Optional[torch.FloatTensor] = None, use_cache: Optional[bool] = False, output_attentions: Optional[bool] = False) -> Union[Tuple[torch.Tensor, Tuple[torch.Tensor]], Optional[Tuple[torch.Tensor, Tuple[torch.Tensor], Tuple[torch.Tensor, ...]]]]: ...

class CodeGenMLP(nn.Module):
    fc_in: Incomplete
    fc_out: Incomplete
    act: Incomplete
    dropout: Incomplete
    def __init__(self, intermediate_size, config) -> None: ...
    def forward(self, hidden_states: Optional[torch.FloatTensor]) -> torch.FloatTensor: ...

class CodeGenBlock(nn.Module):
    ln_1: Incomplete
    attn: Incomplete
    mlp: Incomplete
    def __init__(self, config) -> None: ...
    def forward(self, hidden_states: Optional[torch.FloatTensor], layer_past: Optional[Tuple[torch.Tensor]] = None, attention_mask: Optional[torch.FloatTensor] = None, head_mask: Optional[torch.FloatTensor] = None, use_cache: Optional[bool] = False, output_attentions: Optional[bool] = False) -> Union[Tuple[torch.Tensor], Optional[Tuple[torch.Tensor, Tuple[torch.FloatTensor, ...]]]]: ...

class CodeGenPreTrainedModel(PreTrainedModel):
    """
    An abstract class to handle weights initialization and a simple interface for downloading and loading pretrained
    models.
    """
    config_class = CodeGenConfig
    base_model_prefix: str
    supports_gradient_checkpointing: bool
    def __init__(self, *inputs, **kwargs) -> None: ...

CODEGEN_START_DOCSTRING: str
CODEGEN_INPUTS_DOCSTRING: str

class CodeGenModel(CodeGenPreTrainedModel):
    embed_dim: Incomplete
    vocab_size: Incomplete
    wte: Incomplete
    drop: Incomplete
    h: Incomplete
    ln_f: Incomplete
    rotary_dim: Incomplete
    gradient_checkpointing: bool
    def __init__(self, config) -> None: ...
    def get_input_embeddings(self): ...
    def set_input_embeddings(self, new_embeddings) -> None: ...
    def forward(self, input_ids: Optional[torch.LongTensor] = None, past_key_values: Optional[Tuple[Tuple[torch.Tensor]]] = None, attention_mask: Optional[torch.FloatTensor] = None, token_type_ids: Optional[torch.LongTensor] = None, position_ids: Optional[torch.LongTensor] = None, head_mask: Optional[torch.FloatTensor] = None, inputs_embeds: Optional[torch.FloatTensor] = None, use_cache: Optional[bool] = None, output_attentions: Optional[bool] = None, output_hidden_states: Optional[bool] = None, return_dict: Optional[bool] = None) -> Union[Tuple, BaseModelOutputWithPast]: ...

class CodeGenForCausalLM(CodeGenPreTrainedModel):
    transformer: Incomplete
    lm_head: Incomplete
    def __init__(self, config) -> None: ...
    def get_output_embeddings(self): ...
    def set_output_embeddings(self, new_embeddings) -> None: ...
    def prepare_inputs_for_generation(self, input_ids, past_key_values: Incomplete | None = None, **kwargs): ...
    def forward(self, input_ids: Optional[torch.LongTensor] = None, past_key_values: Optional[Tuple[Tuple[torch.Tensor]]] = None, attention_mask: Optional[torch.FloatTensor] = None, token_type_ids: Optional[torch.LongTensor] = None, position_ids: Optional[torch.LongTensor] = None, head_mask: Optional[torch.FloatTensor] = None, inputs_embeds: Optional[torch.FloatTensor] = None, labels: Optional[torch.LongTensor] = None, use_cache: Optional[bool] = None, output_attentions: Optional[bool] = None, output_hidden_states: Optional[bool] = None, return_dict: Optional[bool] = None) -> Union[Tuple, CausalLMOutputWithPast]:
        """
        labels (`torch.LongTensor` of shape `(batch_size, sequence_length)`, *optional*):
            Labels for language modeling. Note that the labels **are shifted** inside the model, i.e. you can set
            `labels = input_ids` Indices are selected in `[-100, 0, ..., config.vocab_size]` All labels set to `-100`
            are ignored (masked), the loss is only computed for labels in `[0, ..., config.vocab_size]`
        """
