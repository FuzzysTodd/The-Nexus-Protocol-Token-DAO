import torch
from ...activations import ACT2FN as ACT2FN
from ...modeling_utils import PreTrainedModel as PreTrainedModel
from ...pytorch_utils import find_pruneable_heads_and_indices as find_pruneable_heads_and_indices, meshgrid as meshgrid, prune_linear_layer as prune_linear_layer
from ...utils import ModelOutput as ModelOutput, add_code_sample_docstrings as add_code_sample_docstrings, add_start_docstrings as add_start_docstrings, add_start_docstrings_to_model_forward as add_start_docstrings_to_model_forward, logging as logging
from .configuration_donut_swin import DonutSwinConfig as DonutSwinConfig
from _typeshed import Incomplete
from dataclasses import dataclass
from torch import nn
from typing import Optional, Tuple, Union

logger: Incomplete
DONUT_SWIN_PRETRAINED_MODEL_ARCHIVE_LIST: Incomplete

@dataclass
class DonutSwinEncoderOutput(ModelOutput):
    """
    DonutSwin encoder's outputs, with potential hidden states and attentions.

    Args:
        last_hidden_state (`torch.FloatTensor` of shape `(batch_size, sequence_length, hidden_size)`):
            Sequence of hidden-states at the output of the last layer of the model.
        hidden_states (`tuple(torch.FloatTensor)`, *optional*, returned when `output_hidden_states=True` is passed or when `config.output_hidden_states=True`):
            Tuple of `torch.FloatTensor` (one for the output of the embeddings + one for the output of each stage) of
            shape `(batch_size, sequence_length, hidden_size)`.

            Hidden-states of the model at the output of each layer plus the initial embedding outputs.
        attentions (`tuple(torch.FloatTensor)`, *optional*, returned when `output_attentions=True` is passed or when `config.output_attentions=True`):
            Tuple of `torch.FloatTensor` (one for each stage) of shape `(batch_size, num_heads, sequence_length,
            sequence_length)`.

            Attentions weights after the attention softmax, used to compute the weighted average in the self-attention
            heads.
        reshaped_hidden_states (`tuple(torch.FloatTensor)`, *optional*, returned when `output_hidden_states=True` is passed or when `config.output_hidden_states=True`):
            Tuple of `torch.FloatTensor` (one for the output of the embeddings + one for the output of each stage) of
            shape `(batch_size, hidden_size, height, width)`.

            Hidden-states of the model at the output of each layer plus the initial embedding outputs reshaped to
            include the spatial dimensions.
    """
    last_hidden_state: torch.FloatTensor = ...
    hidden_states: Optional[Tuple[torch.FloatTensor]] = ...
    attentions: Optional[Tuple[torch.FloatTensor]] = ...
    reshaped_hidden_states: Optional[Tuple[torch.FloatTensor]] = ...
    def __init__(self, last_hidden_state, hidden_states, attentions, reshaped_hidden_states) -> None: ...

@dataclass
class DonutSwinModelOutput(ModelOutput):
    """
    DonutSwin model's outputs that also contains a pooling of the last hidden states.

    Args:
        last_hidden_state (`torch.FloatTensor` of shape `(batch_size, sequence_length, hidden_size)`):
            Sequence of hidden-states at the output of the last layer of the model.
        pooler_output (`torch.FloatTensor` of shape `(batch_size, hidden_size)`, *optional*, returned when `add_pooling_layer=True` is passed):
            Average pooling of the last layer hidden-state.
        hidden_states (`tuple(torch.FloatTensor)`, *optional*, returned when `output_hidden_states=True` is passed or when `config.output_hidden_states=True`):
            Tuple of `torch.FloatTensor` (one for the output of the embeddings + one for the output of each stage) of
            shape `(batch_size, sequence_length, hidden_size)`.

            Hidden-states of the model at the output of each layer plus the initial embedding outputs.
        attentions (`tuple(torch.FloatTensor)`, *optional*, returned when `output_attentions=True` is passed or when `config.output_attentions=True`):
            Tuple of `torch.FloatTensor` (one for each stage) of shape `(batch_size, num_heads, sequence_length,
            sequence_length)`.

            Attentions weights after the attention softmax, used to compute the weighted average in the self-attention
            heads.
        reshaped_hidden_states (`tuple(torch.FloatTensor)`, *optional*, returned when `output_hidden_states=True` is passed or when `config.output_hidden_states=True`):
            Tuple of `torch.FloatTensor` (one for the output of the embeddings + one for the output of each stage) of
            shape `(batch_size, hidden_size, height, width)`.

            Hidden-states of the model at the output of each layer plus the initial embedding outputs reshaped to
            include the spatial dimensions.
    """
    last_hidden_state: torch.FloatTensor = ...
    pooler_output: Optional[torch.FloatTensor] = ...
    hidden_states: Optional[Tuple[torch.FloatTensor]] = ...
    attentions: Optional[Tuple[torch.FloatTensor]] = ...
    reshaped_hidden_states: Optional[Tuple[torch.FloatTensor]] = ...
    def __init__(self, last_hidden_state, pooler_output, hidden_states, attentions, reshaped_hidden_states) -> None: ...

def window_partition(input_feature, window_size):
    """
    Partitions the given input into windows.
    """
def window_reverse(windows, window_size, height, width):
    """
    Merges windows to produce higher resolution features.
    """

class DonutSwinEmbeddings(nn.Module):
    """
    Construct the patch and position embeddings. Optionally, also the mask token.
    """
    patch_embeddings: Incomplete
    patch_grid: Incomplete
    mask_token: Incomplete
    position_embeddings: Incomplete
    norm: Incomplete
    dropout: Incomplete
    def __init__(self, config, use_mask_token: bool = False) -> None: ...
    def forward(self, pixel_values: Optional[torch.FloatTensor], bool_masked_pos: Optional[torch.BoolTensor] = None) -> Tuple[torch.Tensor]: ...

class DonutSwinPatchEmbeddings(nn.Module):
    """
    This class turns `pixel_values` of shape `(batch_size, num_channels, height, width)` into the initial
    `hidden_states` (patch embeddings) of shape `(batch_size, seq_length, hidden_size)` to be consumed by a
    Transformer.
    """
    image_size: Incomplete
    patch_size: Incomplete
    num_channels: Incomplete
    num_patches: Incomplete
    grid_size: Incomplete
    projection: Incomplete
    def __init__(self, config) -> None: ...
    def maybe_pad(self, pixel_values, height, width): ...
    def forward(self, pixel_values: Optional[torch.FloatTensor]) -> Tuple[torch.Tensor, Tuple[int]]: ...

class DonutSwinPatchMerging(nn.Module):
    """
    Patch Merging Layer.

    Args:
        input_resolution (`Tuple[int]`):
            Resolution of input feature.
        dim (`int`):
            Number of input channels.
        norm_layer (`nn.Module`, *optional*, defaults to `nn.LayerNorm`):
            Normalization layer class.
    """
    input_resolution: Incomplete
    dim: Incomplete
    reduction: Incomplete
    norm: Incomplete
    def __init__(self, input_resolution: Tuple[int], dim: int, norm_layer: nn.Module = ...) -> None: ...
    def maybe_pad(self, input_feature, height, width): ...
    def forward(self, input_feature: torch.Tensor, input_dimensions: Tuple[int, int]) -> torch.Tensor: ...

def drop_path(input, drop_prob: float = 0.0, training: bool = False, scale_by_keep: bool = True):
    """
    Drop paths (Stochastic Depth) per sample (when applied in main path of residual blocks).

    Comment by Ross Wightman: This is the same as the DropConnect impl I created for EfficientNet, etc networks,
    however, the original name is misleading as 'Drop Connect' is a different form of dropout in a separate paper...
    See discussion: https://github.com/tensorflow/tpu/issues/494#issuecomment-532968956 ... I've opted for changing the
    layer and argument names to 'drop path' rather than mix DropConnect as a layer name and use 'survival rate' as the
    argument.
    """

class DonutSwinDropPath(nn.Module):
    """Drop paths (Stochastic Depth) per sample (when applied in main path of residual blocks)."""
    drop_prob: Incomplete
    def __init__(self, drop_prob: Optional[float] = None) -> None: ...
    def forward(self, hidden_states: torch.Tensor) -> torch.Tensor: ...
    def extra_repr(self) -> str: ...

class DonutSwinSelfAttention(nn.Module):
    num_attention_heads: Incomplete
    attention_head_size: Incomplete
    all_head_size: Incomplete
    window_size: Incomplete
    relative_position_bias_table: Incomplete
    query: Incomplete
    key: Incomplete
    value: Incomplete
    dropout: Incomplete
    def __init__(self, config, dim, num_heads, window_size) -> None: ...
    def transpose_for_scores(self, x): ...
    def forward(self, hidden_states: torch.Tensor, attention_mask: Optional[torch.FloatTensor] = None, head_mask: Optional[torch.FloatTensor] = None, output_attentions: Optional[bool] = False) -> Tuple[torch.Tensor]: ...

class DonutSwinSelfOutput(nn.Module):
    dense: Incomplete
    dropout: Incomplete
    def __init__(self, config, dim) -> None: ...
    def forward(self, hidden_states: torch.Tensor, input_tensor: torch.Tensor) -> torch.Tensor: ...

class DonutSwinAttention(nn.Module):
    self: Incomplete
    output: Incomplete
    pruned_heads: Incomplete
    def __init__(self, config, dim, num_heads, window_size) -> None: ...
    def prune_heads(self, heads) -> None: ...
    def forward(self, hidden_states: torch.Tensor, attention_mask: Optional[torch.FloatTensor] = None, head_mask: Optional[torch.FloatTensor] = None, output_attentions: Optional[bool] = False) -> Tuple[torch.Tensor]: ...

class DonutSwinIntermediate(nn.Module):
    dense: Incomplete
    intermediate_act_fn: Incomplete
    def __init__(self, config, dim) -> None: ...
    def forward(self, hidden_states: torch.Tensor) -> torch.Tensor: ...

class DonutSwinOutput(nn.Module):
    dense: Incomplete
    dropout: Incomplete
    def __init__(self, config, dim) -> None: ...
    def forward(self, hidden_states: torch.Tensor) -> torch.Tensor: ...

class DonutSwinLayer(nn.Module):
    chunk_size_feed_forward: Incomplete
    shift_size: Incomplete
    window_size: Incomplete
    input_resolution: Incomplete
    layernorm_before: Incomplete
    attention: Incomplete
    drop_path: Incomplete
    layernorm_after: Incomplete
    intermediate: Incomplete
    output: Incomplete
    def __init__(self, config, dim, input_resolution, num_heads, shift_size: int = 0) -> None: ...
    def set_shift_and_window_size(self, input_resolution) -> None: ...
    def get_attn_mask(self, height, width, dtype): ...
    def maybe_pad(self, hidden_states, height, width): ...
    def forward(self, hidden_states: torch.Tensor, input_dimensions: Tuple[int, int], head_mask: Optional[torch.FloatTensor] = None, output_attentions: Optional[bool] = False, always_partition: Optional[bool] = False) -> Tuple[torch.Tensor, torch.Tensor]: ...

class DonutSwinStage(nn.Module):
    config: Incomplete
    dim: Incomplete
    blocks: Incomplete
    downsample: Incomplete
    pointing: bool
    def __init__(self, config, dim, input_resolution, depth, num_heads, drop_path, downsample) -> None: ...
    def forward(self, hidden_states: torch.Tensor, input_dimensions: Tuple[int, int], head_mask: Optional[torch.FloatTensor] = None, output_attentions: Optional[bool] = False, always_partition: Optional[bool] = False) -> Tuple[torch.Tensor]: ...

class DonutSwinEncoder(nn.Module):
    num_layers: Incomplete
    config: Incomplete
    layers: Incomplete
    gradient_checkpointing: bool
    def __init__(self, config, grid_size) -> None: ...
    def forward(self, hidden_states: torch.Tensor, input_dimensions: Tuple[int, int], head_mask: Optional[torch.FloatTensor] = None, output_attentions: Optional[bool] = False, output_hidden_states: Optional[bool] = False, output_hidden_states_before_downsampling: Optional[bool] = False, always_partition: Optional[bool] = False, return_dict: Optional[bool] = True) -> Union[Tuple, DonutSwinEncoderOutput]: ...

class DonutSwinPreTrainedModel(PreTrainedModel):
    """
    An abstract class to handle weights initialization and a simple interface for downloading and loading pretrained
    models.
    """
    config_class = DonutSwinConfig
    base_model_prefix: str
    main_input_name: str
    supports_gradient_checkpointing: bool

SWIN_START_DOCSTRING: str
SWIN_INPUTS_DOCSTRING: str

class DonutSwinModel(DonutSwinPreTrainedModel):
    config: Incomplete
    num_layers: Incomplete
    num_features: Incomplete
    embeddings: Incomplete
    encoder: Incomplete
    pooler: Incomplete
    def __init__(self, config, add_pooling_layer: bool = True, use_mask_token: bool = False) -> None: ...
    def get_input_embeddings(self): ...
    def forward(self, pixel_values: Optional[torch.FloatTensor] = None, bool_masked_pos: Optional[torch.BoolTensor] = None, head_mask: Optional[torch.FloatTensor] = None, output_attentions: Optional[bool] = None, output_hidden_states: Optional[bool] = None, return_dict: Optional[bool] = None) -> Union[Tuple, DonutSwinModelOutput]: ...
