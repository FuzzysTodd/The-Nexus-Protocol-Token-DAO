import torch
from ...modeling_utils import PreTrainedModel as PreTrainedModel
from ...utils import ModelOutput as ModelOutput, add_start_docstrings as add_start_docstrings, add_start_docstrings_to_model_forward as add_start_docstrings_to_model_forward, logging as logging, replace_return_docstrings as replace_return_docstrings
from .configuration_trajectory_transformer import TrajectoryTransformerConfig as TrajectoryTransformerConfig
from _typeshed import Incomplete
from dataclasses import dataclass
from torch import nn
from typing import Optional, Tuple, Union

logger: Incomplete
TRAJECTORY_TRANSFORMER_PRETRAINED_MODEL_ARCHIVE_LIST: Incomplete

def load_tf_weights_in_trajectory_transformer(model, config, tf_checkpoint_path):
    """Load tf checkpoints in a pytorch model."""

@dataclass
class TrajectoryTransformerOutput(ModelOutput):
    """
    Base class for model's outputs that also contains a pooling of the last hidden states.

    Args:
        loss (`torch.FloatTensor` of shape `(1,)`, *optional*, returned when `labels` is provided):
            Language modeling loss.
        logits (`torch.FloatTensor` of shape `(batch_size, sequence_length, config.vocab_size)`):
            Prediction scores of the language modeling head (scores for each vocabulary token before SoftMax).
        past_key_values (`Tuple[Tuple[torch.Tensor]]`, *optional*, returned when `use_cache=True` is passed or when `config.use_cache=True`):
            Tuple of length `config.n_layers`, containing tuples of tensors of shape `(batch_size, num_heads,
            sequence_length, embed_size_per_head)`). Contains pre-computed hidden-states (key and values in the
            attention blocks) that can be used (see `past_key_values` input) to speed up sequential decoding.
        hidden_states (`tuple(torch.FloatTensor)`, *optional*, returned when `output_hidden_states=True` is passed or when `config.output_hidden_states=True`):
            Tuple of `torch.FloatTensor` (one for the output of the embeddings + one for the output of each layer) of
            shape `(batch_size, sequence_length, hidden_size)`. Hidden-states of the model at the output of each layer
            plus the initial embedding outputs.
        attentions (`tuple(torch.FloatTensor)`, *optional*, returned when `output_attentions=True` is passed or when `config.output_attentions=True`):
            Tuple of `torch.FloatTensor` (one for each layer) of shape `(batch_size, num_heads, sequence_length,
            sequence_length)`. GPT2Attentions weights after the attention softmax, used to compute the weighted average
            in the self-attention heads.
    """
    loss: Optional[torch.FloatTensor] = ...
    logits: torch.FloatTensor = ...
    past_key_values: Optional[Tuple[Tuple[torch.FloatTensor]]] = ...
    hidden_states: Optional[Tuple[torch.FloatTensor]] = ...
    attentions: Optional[Tuple[torch.FloatTensor]] = ...
    def __init__(self, loss, logits, past_key_values, hidden_states, attentions) -> None: ...

class TrajectoryTransformerPreTrainedModel(PreTrainedModel):
    """
    An abstract class to handle weights initialization and a simple interface for downloading and loading pretrained
    models.
    """
    config_class = TrajectoryTransformerConfig
    load_tf_weights = load_tf_weights_in_trajectory_transformer
    base_model_prefix: str
    main_input_name: str
    supports_gradient_checkpointing: bool

TRAJECTORY_TRANSFORMER_START_DOCSTRING: str
TRAJECTORY_TRANSFORMER_INPUTS_DOCSTRING: str

class EinLinear(nn.Module):
    n_models: Incomplete
    out_features: Incomplete
    in_features: Incomplete
    weight: Incomplete
    bias: Incomplete
    def __init__(self, n_models, in_features, out_features, bias) -> None: ...
    def reset_parameters(self) -> None: ...
    def forward(self, input):
        """
        Args:
            input (`torch.FloatTensor` of shape `(B, n_models, input_dim)`):
                The input to the layer.
        """

class CausalSelfAttention(nn.Module):
    key: Incomplete
    query: Incomplete
    value: Incomplete
    attn_drop: Incomplete
    resid_drop: Incomplete
    proj: Incomplete
    n_head: Incomplete
    def __init__(self, config) -> None: ...
    def forward(self, hidden_states: Optional[Tuple[torch.FloatTensor]], layer_past: Optional[Tuple[torch.Tensor]] = None, use_cache: Optional[bool] = False, output_attentions: Optional[bool] = False): ...

class Block(nn.Module):
    ln1: Incomplete
    ln2: Incomplete
    attn: Incomplete
    l1: Incomplete
    act: Incomplete
    l2: Incomplete
    drop: Incomplete
    def __init__(self, config) -> None: ...
    def forward(self, hidden_states: Optional[Tuple[torch.FloatTensor]], layer_past: Optional[Tuple[torch.Tensor]] = None, use_cache: Optional[bool] = False, output_attentions: Optional[bool] = False): ...

class TrajectoryTransformerModel(TrajectoryTransformerPreTrainedModel):
    """the full GPT language model, with a context size of block_size"""
    tok_emb: Incomplete
    pos_emb: Incomplete
    drop: Incomplete
    blocks: Incomplete
    ln_f: Incomplete
    head: Incomplete
    vocab_size: Incomplete
    stop_token: Incomplete
    block_size: Incomplete
    observation_dim: Incomplete
    action_dim: Incomplete
    transition_dim: Incomplete
    embedding_dim: Incomplete
    action_weight: Incomplete
    reward_weight: Incomplete
    value_weight: Incomplete
    gradient_checkpointing: bool
    def __init__(self, config) -> None: ...
    def get_block_size(self): ...
    def offset_tokens(self, trajectories): ...
    def pad_to_full_observation(self, hidden_states): ...
    def forward(self, trajectories: Optional[torch.LongTensor] = None, past_key_values: Optional[Tuple[Tuple[torch.Tensor]]] = None, targets: Optional[torch.FloatTensor] = None, attention_mask: Optional[torch.FloatTensor] = None, use_cache: Optional[bool] = None, output_attentions: Optional[bool] = None, output_hidden_states: Optional[bool] = None, return_dict: Optional[bool] = None) -> Union[Tuple[torch.Tensor], TrajectoryTransformerOutput]:
        '''
        Returns:

        Examples:

        ```python
        >>> from transformers import TrajectoryTransformerModel
        >>> import torch

        >>> model = TrajectoryTransformerModel.from_pretrained(
        ...     "CarlCochet/trajectory-transformer-halfcheetah-medium-v2"
        ... )
        >>> model.to(device)
        >>> model.eval()

        >>> observations_dim, action_dim, batch_size = 17, 6, 256
        >>> seq_length = observations_dim + action_dim + 1

        >>> trajectories = torch.LongTensor([np.random.permutation(self.seq_length) for _ in range(batch_size)]).to(
        ...     device
        ... )
        >>> targets = torch.LongTensor([np.random.permutation(self.seq_length) for _ in range(batch_size)]).to(device)

        >>> outputs = model(
        ...     trajectories,
        ...     targets=targets,
        ...     use_cache=True,
        ...     output_attentions=True,
        ...     output_hidden_states=True,
        ...     return_dict=True,
        ... )
        ```
        '''
