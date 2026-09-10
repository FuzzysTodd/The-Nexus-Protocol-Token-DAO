import torch
from ...activations import ACT2FN as ACT2FN
from ...modeling_outputs import BaseModelOutputWithPast as BaseModelOutputWithPast, BaseModelOutputWithPastAndCrossAttentions as BaseModelOutputWithPastAndCrossAttentions, CausalLMOutputWithCrossAttentions as CausalLMOutputWithCrossAttentions, CausalLMOutputWithPast as CausalLMOutputWithPast, SequenceClassifierOutputWithPast as SequenceClassifierOutputWithPast
from ...modeling_utils import PreTrainedModel as PreTrainedModel
from ...utils import add_code_sample_docstrings as add_code_sample_docstrings, add_start_docstrings as add_start_docstrings, add_start_docstrings_to_model_forward as add_start_docstrings_to_model_forward, logging as logging
from .configuration_gpt_neo import GPTNeoConfig as GPTNeoConfig
from _typeshed import Incomplete
from torch import nn
from typing import Optional, Tuple, Union

logger: Incomplete
GPT_NEO_PRETRAINED_MODEL_ARCHIVE_LIST: Incomplete

def load_tf_weights_in_gpt_neo(model, config, gpt_neo_checkpoint_path):
    """Load tf checkpoints in a pytorch model"""

class GPTNeoSelfAttention(nn.Module):
    attn_dropout: Incomplete
    resid_dropout: Incomplete
    embed_dim: Incomplete
    num_heads: Incomplete
    head_dim: Incomplete
    k_proj: Incomplete
    v_proj: Incomplete
    q_proj: Incomplete
    out_proj: Incomplete
    def __init__(self, config, attention_type) -> None: ...
    def forward(self, hidden_states, attention_mask: Incomplete | None = None, layer_past: Incomplete | None = None, head_mask: Incomplete | None = None, use_cache: bool = False, output_attentions: bool = False): ...

class GPTNeoAttention(nn.Module):
    layer_id: Incomplete
    attention_layers: Incomplete
    attention_type: Incomplete
    attention: Incomplete
    def __init__(self, config, layer_id: int = 0) -> None: ...
    def forward(self, hidden_states, layer_past: Incomplete | None = None, attention_mask: Incomplete | None = None, head_mask: Incomplete | None = None, use_cache: bool = False, output_attentions: bool = False): ...

class GPTNeoMLP(nn.Module):
    c_fc: Incomplete
    c_proj: Incomplete
    act: Incomplete
    dropout: Incomplete
    def __init__(self, intermediate_size, config) -> None: ...
    def forward(self, hidden_states): ...

class GPTNeoBlock(nn.Module):
    ln_1: Incomplete
    attn: Incomplete
    ln_2: Incomplete
    mlp: Incomplete
    def __init__(self, config, layer_id) -> None: ...
    def forward(self, hidden_states, layer_past: Incomplete | None = None, attention_mask: Incomplete | None = None, head_mask: Incomplete | None = None, use_cache: bool = False, output_attentions: bool = False): ...

class GPTNeoPreTrainedModel(PreTrainedModel):
    """
    An abstract class to handle weights initialization and a simple interface for downloading and loading pretrained
    models.
    """
    config_class = GPTNeoConfig
    load_tf_weights = load_tf_weights_in_gpt_neo
    base_model_prefix: str
    supports_gradient_checkpointing: bool
    def __init__(self, *inputs, **kwargs) -> None: ...

GPT_NEO_START_DOCSTRING: str
GPT_NEO_INPUTS_DOCSTRING: str

class GPTNeoModel(GPTNeoPreTrainedModel):
    embed_dim: Incomplete
    wte: Incomplete
    wpe: Incomplete
    drop: Incomplete
    h: Incomplete
    ln_f: Incomplete
    gradient_checkpointing: bool
    def __init__(self, config) -> None: ...
    def get_input_embeddings(self): ...
    def set_input_embeddings(self, new_embeddings) -> None: ...
    def forward(self, input_ids: Optional[torch.Tensor] = None, past_key_values: Optional[Tuple[torch.FloatTensor]] = None, attention_mask: Optional[torch.Tensor] = None, token_type_ids: Optional[torch.Tensor] = None, position_ids: Optional[torch.Tensor] = None, head_mask: Optional[torch.Tensor] = None, inputs_embeds: Optional[torch.Tensor] = None, use_cache: Optional[bool] = None, output_attentions: Optional[bool] = None, output_hidden_states: Optional[bool] = None, return_dict: Optional[bool] = None) -> Union[Tuple[torch.Tensor], BaseModelOutputWithPastAndCrossAttentions]: ...

class GPTNeoForCausalLM(GPTNeoPreTrainedModel):
    transformer: Incomplete
    lm_head: Incomplete
    def __init__(self, config) -> None: ...
    def get_output_embeddings(self): ...
    def set_output_embeddings(self, new_embeddings) -> None: ...
    def prepare_inputs_for_generation(self, input_ids, past_key_values: Incomplete | None = None, **kwargs): ...
    def forward(self, input_ids: Optional[torch.Tensor] = None, past_key_values: Optional[Tuple[torch.FloatTensor]] = None, attention_mask: Optional[torch.Tensor] = None, token_type_ids: Optional[torch.Tensor] = None, position_ids: Optional[torch.Tensor] = None, head_mask: Optional[torch.Tensor] = None, inputs_embeds: Optional[torch.Tensor] = None, labels: Optional[torch.Tensor] = None, use_cache: Optional[bool] = None, output_attentions: Optional[bool] = None, output_hidden_states: Optional[bool] = None, return_dict: Optional[bool] = None) -> Union[Tuple[torch.Tensor], CausalLMOutputWithCrossAttentions]:
        """
        labels (`torch.LongTensor` of shape `(batch_size, sequence_length)`, *optional*):
            Labels for language modeling. Note that the labels **are shifted** inside the model, i.e. you can set
            `labels = input_ids` Indices are selected in `[-100, 0, ..., config.vocab_size]` All labels set to `-100`
            are ignored (masked), the loss is only computed for labels in `[0, ..., config.vocab_size]`
        """

class GPTNeoForSequenceClassification(GPTNeoPreTrainedModel):
    num_labels: Incomplete
    transformer: Incomplete
    score: Incomplete
    def __init__(self, config) -> None: ...
    def forward(self, input_ids: Optional[torch.Tensor] = None, past_key_values: Optional[Tuple[torch.FloatTensor]] = None, attention_mask: Optional[torch.Tensor] = None, token_type_ids: Optional[torch.Tensor] = None, position_ids: Optional[torch.Tensor] = None, head_mask: Optional[torch.Tensor] = None, inputs_embeds: Optional[torch.Tensor] = None, labels: Optional[torch.Tensor] = None, use_cache: Optional[bool] = None, output_attentions: Optional[bool] = None, output_hidden_states: Optional[bool] = None, return_dict: Optional[bool] = None) -> Union[Tuple[torch.Tensor], SequenceClassifierOutputWithPast]:
        """
        labels (`torch.LongTensor` of shape `(batch_size,)`, *optional*):
            Labels for computing the sequence classification/regression loss. Indices should be in `[0, ...,
            config.num_labels - 1]`. If `config.num_labels == 1` a regression loss is computed (Mean-Square loss), If
            `config.num_labels > 1` a classification loss is computed (Cross-Entropy).
        """
