import torch
from ...activations import ACT2FN as ACT2FN
from ...modeling_outputs import BaseModelOutputWithPastAndCrossAttentions as BaseModelOutputWithPastAndCrossAttentions
from ...modeling_utils import PreTrainedModel as PreTrainedModel
from ...pytorch_utils import Conv1D as Conv1D, find_pruneable_heads_and_indices as find_pruneable_heads_and_indices, prune_conv1d_layer as prune_conv1d_layer
from ...utils import ModelOutput as ModelOutput, add_start_docstrings as add_start_docstrings, add_start_docstrings_to_model_forward as add_start_docstrings_to_model_forward, logging as logging, replace_return_docstrings as replace_return_docstrings
from .configuration_decision_transformer import DecisionTransformerConfig as DecisionTransformerConfig
from _typeshed import Incomplete
from dataclasses import dataclass
from torch import nn
from typing import Optional, Tuple, Union

logger: Incomplete
DECISION_TRANSFORMER_PRETRAINED_MODEL_ARCHIVE_LIST: Incomplete

def load_tf_weights_in_gpt2(model, config, gpt2_checkpoint_path):
    """Load tf checkpoints in a pytorch model"""

class DecisionTransformerGPT2Attention(nn.Module):
    embed_dim: Incomplete
    num_heads: Incomplete
    head_dim: Incomplete
    split_size: Incomplete
    scale_attn_weights: Incomplete
    is_cross_attention: Incomplete
    scale_attn_by_inverse_layer_idx: Incomplete
    layer_idx: Incomplete
    reorder_and_upcast_attn: Incomplete
    c_attn: Incomplete
    q_attn: Incomplete
    c_proj: Incomplete
    attn_dropout: Incomplete
    resid_dropout: Incomplete
    pruned_heads: Incomplete
    def __init__(self, config, is_cross_attention: bool = False, layer_idx: Incomplete | None = None) -> None: ...
    def prune_heads(self, heads) -> None: ...
    def forward(self, hidden_states: Optional[Tuple[torch.FloatTensor]], layer_past: Optional[Tuple[torch.Tensor]] = None, attention_mask: Optional[torch.FloatTensor] = None, head_mask: Optional[torch.FloatTensor] = None, encoder_hidden_states: Optional[torch.Tensor] = None, encoder_attention_mask: Optional[torch.FloatTensor] = None, use_cache: Optional[bool] = False, output_attentions: Optional[bool] = False) -> Tuple[Union[torch.Tensor, Tuple[torch.Tensor]], ...]: ...

class DecisionTransformerGPT2MLP(nn.Module):
    c_fc: Incomplete
    c_proj: Incomplete
    act: Incomplete
    dropout: Incomplete
    def __init__(self, intermediate_size, config) -> None: ...
    def forward(self, hidden_states: Optional[Tuple[torch.FloatTensor]]) -> torch.FloatTensor: ...

class DecisionTransformerGPT2Block(nn.Module):
    ln_1: Incomplete
    attn: Incomplete
    ln_2: Incomplete
    crossattention: Incomplete
    ln_cross_attn: Incomplete
    mlp: Incomplete
    def __init__(self, config, layer_idx: Incomplete | None = None) -> None: ...
    def forward(self, hidden_states: Optional[Tuple[torch.FloatTensor]], layer_past: Optional[Tuple[torch.Tensor]] = None, attention_mask: Optional[torch.FloatTensor] = None, head_mask: Optional[torch.FloatTensor] = None, encoder_hidden_states: Optional[torch.Tensor] = None, encoder_attention_mask: Optional[torch.FloatTensor] = None, use_cache: Optional[bool] = False, output_attentions: Optional[bool] = False) -> Union[Tuple[torch.Tensor], Optional[Tuple[torch.Tensor, Tuple[torch.FloatTensor, ...]]]]: ...

class DecisionTransformerGPT2PreTrainedModel(PreTrainedModel):
    """
    An abstract class to handle weights initialization and a simple interface for downloading and loading pretrained
    models.
    """
    config_class = DecisionTransformerConfig
    load_tf_weights = load_tf_weights_in_gpt2
    base_model_prefix: str
    is_parallelizable: bool
    supports_gradient_checkpointing: bool
    def __init__(self, *inputs, **kwargs) -> None: ...

class DecisionTransformerGPT2Model(DecisionTransformerGPT2PreTrainedModel):
    embed_dim: Incomplete
    wte: Incomplete
    wpe: Incomplete
    drop: Incomplete
    h: Incomplete
    ln_f: Incomplete
    model_parallel: bool
    device_map: Incomplete
    gradient_checkpointing: bool
    def __init__(self, config) -> None: ...
    def get_input_embeddings(self): ...
    def set_input_embeddings(self, new_embeddings) -> None: ...
    def forward(self, input_ids: Optional[torch.LongTensor] = None, past_key_values: Optional[Tuple[Tuple[torch.Tensor]]] = None, attention_mask: Optional[torch.FloatTensor] = None, token_type_ids: Optional[torch.LongTensor] = None, position_ids: Optional[torch.LongTensor] = None, head_mask: Optional[torch.FloatTensor] = None, inputs_embeds: Optional[torch.FloatTensor] = None, encoder_hidden_states: Optional[torch.Tensor] = None, encoder_attention_mask: Optional[torch.FloatTensor] = None, use_cache: Optional[bool] = None, output_attentions: Optional[bool] = None, output_hidden_states: Optional[bool] = None, return_dict: Optional[bool] = None) -> Union[Tuple, BaseModelOutputWithPastAndCrossAttentions]: ...

@dataclass
class DecisionTransformerOutput(ModelOutput):
    """
    Base class for model's outputs that also contains a pooling of the last hidden states.

    Args:
        last_hidden_state (`torch.FloatTensor` of shape `(batch_size, sequence_length, hidden_size)`):
            Sequence of hidden-states at the output of the last layer of the model.
        state_preds (`torch.FloatTensor` of shape `(batch_size, sequence_length, state_dim)`):
            Environment state predictions
        action_preds (`torch.FloatTensor` of shape `(batch_size, sequence_length, action_dim)`):
            Model action predictions
        return_preds (`torch.FloatTensor` of shape `(batch_size, sequence_length, 1)`):
            Predicted returns for each state
        hidden_states (`tuple(torch.FloatTensor)`, *optional*, returned when `output_hidden_states=True` is passed or when `config.output_hidden_states=True`):
            Tuple of `torch.FloatTensor` (one for the output of the embeddings + one for the output of each layer) of
            shape `(batch_size, sequence_length, hidden_size)`.

            Hidden-states of the model at the output of each layer plus the initial embedding outputs.
        attentions (`tuple(torch.FloatTensor)`, *optional*, returned when `output_attentions=True` is passed or when `config.output_attentions=True`):
            Tuple of `torch.FloatTensor` (one for each layer) of shape `(batch_size, num_heads, sequence_length,
            sequence_length)`.

            Attentions weights after the attention softmax, used to compute the weighted average in the self-attention
            heads.
    """
    state_preds: torch.FloatTensor = ...
    action_preds: torch.FloatTensor = ...
    return_preds: torch.FloatTensor = ...
    hidden_states: torch.FloatTensor = ...
    attentions: torch.FloatTensor = ...
    last_hidden_state: torch.FloatTensor = ...
    def __init__(self, state_preds, action_preds, return_preds, hidden_states, attentions, last_hidden_state) -> None: ...

class DecisionTransformerPreTrainedModel(PreTrainedModel):
    """
    An abstract class to handle weights initialization and a simple interface for downloading and loading pretrained
    models.
    """
    config_class = DecisionTransformerConfig
    base_model_prefix: str
    main_input_name: str
    supports_gradient_checkpointing: bool

DECISION_TRANSFORMER_START_DOCSTRING: str
DECISION_TRANSFORMER_INPUTS_DOCSTRING: str

class DecisionTransformerModel(DecisionTransformerPreTrainedModel):
    """

    The model builds upon the GPT2 architecture to perform autoregressive prediction of actions in an offline RL
    setting. Refer to the paper for more details: https://arxiv.org/abs/2106.01345

    """
    config: Incomplete
    hidden_size: Incomplete
    encoder: Incomplete
    embed_timestep: Incomplete
    embed_return: Incomplete
    embed_state: Incomplete
    embed_action: Incomplete
    embed_ln: Incomplete
    predict_state: Incomplete
    predict_action: Incomplete
    predict_return: Incomplete
    def __init__(self, config) -> None: ...
    def forward(self, states: Incomplete | None = None, actions: Incomplete | None = None, rewards: Incomplete | None = None, returns_to_go: Incomplete | None = None, timesteps: Incomplete | None = None, attention_mask: Incomplete | None = None, output_hidden_states: Incomplete | None = None, output_attentions: Incomplete | None = None, return_dict: Incomplete | None = None) -> Union[Tuple, DecisionTransformerOutput]:
        '''
        Returns:

        Examples:

        ```python
        >>> from transformers import DecisionTransformerModel
        >>> import torch

        >>> model = DecisionTransformerModel.from_pretrained("edbeeching/decision-transformer-gym-hopper-medium")
        >>> # evaluation
        >>> model = model.to(device)
        >>> model.eval()

        >>> env = gym.make("Hopper-v3")
        >>> state_dim = env.observation_space.shape[0]
        >>> act_dim = env.action_space.shape[0]

        >>> state = env.reset()
        >>> states = torch.from_numpy(state).reshape(1, 1, state_dim).to(device=device, dtype=torch.float32)
        >>> actions = torch.zeros((1, 1, act_dim), device=device, dtype=torch.float32)
        >>> rewards = torch.zeros(1, 1, device=device, dtype=torch.float32)
        >>> target_return = torch.tensor(TARGET_RETURN, dtype=torch.float32).reshape(1, 1)
        >>> timesteps = torch.tensor(0, device=device, dtype=torch.long).reshape(1, 1)
        >>> attention_mask = torch.zeros(1, 1, device=device, dtype=torch.float32)

        >>> # forward pass
        >>> with torch.no_grad():
        ...     state_preds, action_preds, return_preds = model(
        ...         states=states,
        ...         actions=actions,
        ...         rewards=rewards,
        ...         returns_to_go=target_return,
        ...         timesteps=timesteps,
        ...         attention_mask=attention_mask,
        ...         return_dict=False,
        ...     )
        ```'''
