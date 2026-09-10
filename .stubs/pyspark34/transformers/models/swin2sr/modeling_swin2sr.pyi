import torch
from ...activations import ACT2FN as ACT2FN
from ...modeling_outputs import BaseModelOutput as BaseModelOutput, ImageSuperResolutionOutput as ImageSuperResolutionOutput
from ...modeling_utils import PreTrainedModel as PreTrainedModel
from ...pytorch_utils import find_pruneable_heads_and_indices as find_pruneable_heads_and_indices, meshgrid as meshgrid, prune_linear_layer as prune_linear_layer
from ...utils import ModelOutput as ModelOutput, add_code_sample_docstrings as add_code_sample_docstrings, add_start_docstrings as add_start_docstrings, add_start_docstrings_to_model_forward as add_start_docstrings_to_model_forward, logging as logging, replace_return_docstrings as replace_return_docstrings
from .configuration_swin2sr import Swin2SRConfig as Swin2SRConfig
from _typeshed import Incomplete
from dataclasses import dataclass
from torch import nn
from typing import Optional, Tuple, Union

logger: Incomplete
SWIN2SR_PRETRAINED_MODEL_ARCHIVE_LIST: Incomplete

@dataclass
class Swin2SREncoderOutput(ModelOutput):
    """
    Swin2SR encoder's outputs, with potential hidden states and attentions.

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
    """
    last_hidden_state: torch.FloatTensor = ...
    hidden_states: Optional[Tuple[torch.FloatTensor]] = ...
    attentions: Optional[Tuple[torch.FloatTensor]] = ...
    def __init__(self, last_hidden_state, hidden_states, attentions) -> None: ...

def window_partition(input_feature, window_size):
    """
    Partitions the given input into windows.
    """
def window_reverse(windows, window_size, height, width):
    """
    Merges windows to produce higher resolution features.
    """
def drop_path(input, drop_prob: float = 0.0, training: bool = False, scale_by_keep: bool = True):
    """
    Drop paths (Stochastic Depth) per sample (when applied in main path of residual blocks).

    Comment by Ross Wightman: This is the same as the DropConnect impl I created for EfficientNet, etc networks,
    however, the original name is misleading as 'Drop Connect' is a different form of dropout in a separate paper...
    See discussion: https://github.com/tensorflow/tpu/issues/494#issuecomment-532968956 ... I've opted for changing the
    layer and argument names to 'drop path' rather than mix DropConnect as a layer name and use 'survival rate' as the
    argument.
    """

class Swin2SRDropPath(nn.Module):
    """Drop paths (Stochastic Depth) per sample (when applied in main path of residual blocks)."""
    drop_prob: Incomplete
    def __init__(self, drop_prob: Optional[float] = None) -> None: ...
    def forward(self, hidden_states: torch.Tensor) -> torch.Tensor: ...
    def extra_repr(self) -> str: ...

class Swin2SREmbeddings(nn.Module):
    """
    Construct the patch and optional position embeddings.
    """
    patch_embeddings: Incomplete
    position_embeddings: Incomplete
    dropout: Incomplete
    window_size: Incomplete
    def __init__(self, config) -> None: ...
    def forward(self, pixel_values: Optional[torch.FloatTensor]) -> Tuple[torch.Tensor]: ...

class Swin2SRPatchEmbeddings(nn.Module):
    patches_resolution: Incomplete
    num_patches: Incomplete
    projection: Incomplete
    layernorm: Incomplete
    def __init__(self, config, normalize_patches: bool = True) -> None: ...
    def forward(self, embeddings: Optional[torch.FloatTensor]) -> Tuple[torch.Tensor, Tuple[int]]: ...

class Swin2SRPatchUnEmbeddings(nn.Module):
    """Image to Patch Unembedding"""
    embed_dim: Incomplete
    def __init__(self, config) -> None: ...
    def forward(self, embeddings, x_size): ...

class Swin2SRPatchMerging(nn.Module):
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

class Swin2SRSelfAttention(nn.Module):
    num_attention_heads: Incomplete
    attention_head_size: Incomplete
    all_head_size: Incomplete
    window_size: Incomplete
    pretrained_window_size: Incomplete
    logit_scale: Incomplete
    continuous_position_bias_mlp: Incomplete
    query: Incomplete
    key: Incomplete
    value: Incomplete
    dropout: Incomplete
    def __init__(self, config, dim, num_heads, window_size, pretrained_window_size=[0, 0]) -> None: ...
    def transpose_for_scores(self, x): ...
    def forward(self, hidden_states: torch.Tensor, attention_mask: Optional[torch.FloatTensor] = None, head_mask: Optional[torch.FloatTensor] = None, output_attentions: Optional[bool] = False) -> Tuple[torch.Tensor]: ...

class Swin2SRSelfOutput(nn.Module):
    dense: Incomplete
    dropout: Incomplete
    def __init__(self, config, dim) -> None: ...
    def forward(self, hidden_states: torch.Tensor, input_tensor: torch.Tensor) -> torch.Tensor: ...

class Swin2SRAttention(nn.Module):
    self: Incomplete
    output: Incomplete
    pruned_heads: Incomplete
    def __init__(self, config, dim, num_heads, window_size, pretrained_window_size: int = 0) -> None: ...
    def prune_heads(self, heads) -> None: ...
    def forward(self, hidden_states: torch.Tensor, attention_mask: Optional[torch.FloatTensor] = None, head_mask: Optional[torch.FloatTensor] = None, output_attentions: Optional[bool] = False) -> Tuple[torch.Tensor]: ...

class Swin2SRIntermediate(nn.Module):
    dense: Incomplete
    intermediate_act_fn: Incomplete
    def __init__(self, config, dim) -> None: ...
    def forward(self, hidden_states: torch.Tensor) -> torch.Tensor: ...

class Swin2SROutput(nn.Module):
    dense: Incomplete
    dropout: Incomplete
    def __init__(self, config, dim) -> None: ...
    def forward(self, hidden_states: torch.Tensor) -> torch.Tensor: ...

class Swin2SRLayer(nn.Module):
    chunk_size_feed_forward: Incomplete
    shift_size: Incomplete
    window_size: Incomplete
    input_resolution: Incomplete
    attention: Incomplete
    layernorm_before: Incomplete
    drop_path: Incomplete
    intermediate: Incomplete
    output: Incomplete
    layernorm_after: Incomplete
    def __init__(self, config, dim, input_resolution, num_heads, shift_size: int = 0, pretrained_window_size: int = 0) -> None: ...
    def set_shift_and_window_size(self, input_resolution) -> None: ...
    def get_attn_mask(self, height, width, dtype): ...
    def maybe_pad(self, hidden_states, height, width): ...
    def forward(self, hidden_states: torch.Tensor, input_dimensions: Tuple[int, int], head_mask: Optional[torch.FloatTensor] = None, output_attentions: Optional[bool] = False, always_partition: Optional[bool] = False) -> Tuple[torch.Tensor, torch.Tensor]: ...

class Swin2SRStage(nn.Module):
    """
    This corresponds to the Residual Swin Transformer Block (RSTB) in the original implementation.
    """
    config: Incomplete
    dim: Incomplete
    layers: Incomplete
    conv: Incomplete
    patch_embed: Incomplete
    patch_unembed: Incomplete
    def __init__(self, config, dim, input_resolution, depth, num_heads, drop_path, pretrained_window_size: int = 0) -> None: ...
    def forward(self, hidden_states: torch.Tensor, input_dimensions: Tuple[int, int], head_mask: Optional[torch.FloatTensor] = None, output_attentions: Optional[bool] = False) -> Tuple[torch.Tensor]: ...

class Swin2SREncoder(nn.Module):
    num_stages: Incomplete
    config: Incomplete
    stages: Incomplete
    gradient_checkpointing: bool
    def __init__(self, config, grid_size) -> None: ...
    def forward(self, hidden_states: torch.Tensor, input_dimensions: Tuple[int, int], head_mask: Optional[torch.FloatTensor] = None, output_attentions: Optional[bool] = False, output_hidden_states: Optional[bool] = False, return_dict: Optional[bool] = True) -> Union[Tuple, Swin2SREncoderOutput]: ...

class Swin2SRPreTrainedModel(PreTrainedModel):
    """
    An abstract class to handle weights initialization and a simple interface for downloading and loading pretrained
    models.
    """
    config_class = Swin2SRConfig
    base_model_prefix: str
    main_input_name: str
    supports_gradient_checkpointing: bool

SWIN2SR_START_DOCSTRING: str
SWIN2SR_INPUTS_DOCSTRING: str

class Swin2SRModel(Swin2SRPreTrainedModel):
    config: Incomplete
    mean: Incomplete
    img_range: Incomplete
    first_convolution: Incomplete
    embeddings: Incomplete
    encoder: Incomplete
    layernorm: Incomplete
    patch_unembed: Incomplete
    conv_after_body: Incomplete
    def __init__(self, config) -> None: ...
    def get_input_embeddings(self): ...
    def pad_and_normalize(self, pixel_values): ...
    def forward(self, pixel_values, head_mask: Optional[torch.FloatTensor] = None, output_attentions: Optional[bool] = None, output_hidden_states: Optional[bool] = None, return_dict: Optional[bool] = None) -> Union[Tuple, BaseModelOutput]: ...

class Upsample(nn.Module):
    """Upsample module.

    Args:
        scale (`int`):
            Scale factor. Supported scales: 2^n and 3.
        num_features (`int`):
            Channel number of intermediate features.
    """
    scale: Incomplete
    convolution: Incomplete
    pixelshuffle: Incomplete
    def __init__(self, scale, num_features) -> None: ...
    def forward(self, hidden_state): ...

class UpsampleOneStep(nn.Module):
    """UpsampleOneStep module (the difference with Upsample is that it always only has 1conv + 1pixelshuffle)

    Used in lightweight SR to save parameters.

    Args:
        scale (int):
            Scale factor. Supported scales: 2^n and 3.
        in_channels (int):
            Channel number of intermediate features.
    """
    conv: Incomplete
    pixel_shuffle: Incomplete
    def __init__(self, scale, in_channels, out_channels) -> None: ...
    def forward(self, x): ...

class PixelShuffleUpsampler(nn.Module):
    conv_before_upsample: Incomplete
    activation: Incomplete
    upsample: Incomplete
    final_convolution: Incomplete
    def __init__(self, config, num_features) -> None: ...
    def forward(self, sequence_output): ...

class NearestConvUpsampler(nn.Module):
    conv_before_upsample: Incomplete
    activation: Incomplete
    conv_up1: Incomplete
    conv_up2: Incomplete
    conv_hr: Incomplete
    final_convolution: Incomplete
    lrelu: Incomplete
    def __init__(self, config, num_features) -> None: ...
    def forward(self, sequence_output): ...

class PixelShuffleAuxUpsampler(nn.Module):
    upscale: Incomplete
    conv_bicubic: Incomplete
    conv_before_upsample: Incomplete
    activation: Incomplete
    conv_aux: Incomplete
    conv_after_aux: Incomplete
    upsample: Incomplete
    final_convolution: Incomplete
    def __init__(self, config, num_features) -> None: ...
    def forward(self, sequence_output, bicubic, height, width): ...

class Swin2SRForImageSuperResolution(Swin2SRPreTrainedModel):
    swin2sr: Incomplete
    upsampler: Incomplete
    upscale: Incomplete
    upsample: Incomplete
    final_convolution: Incomplete
    def __init__(self, config) -> None: ...
    def forward(self, pixel_values: Optional[torch.FloatTensor] = None, head_mask: Optional[torch.FloatTensor] = None, labels: Optional[torch.LongTensor] = None, output_attentions: Optional[bool] = None, output_hidden_states: Optional[bool] = None, return_dict: Optional[bool] = None) -> Union[Tuple, ImageSuperResolutionOutput]:
        '''
        Returns:

        Example:
         ```python
         >>> import torch
         >>> import numpy as np
         >>> from PIL import Image
         >>> import requests

         >>> from transformers import AutoImageProcessor, Swin2SRForImageSuperResolution

         >>> processor = AutoImageProcessor.from_pretrained("caidas/swin2SR-classical-sr-x2-64")
         >>> model = Swin2SRForImageSuperResolution.from_pretrained("caidas/swin2SR-classical-sr-x2-64")

         >>> url = "https://huggingface.co/spaces/jjourney1125/swin2sr/resolve/main/samples/butterfly.jpg"
         >>> image = Image.open(requests.get(url, stream=True).raw)
         >>> # prepare image for the model
         >>> inputs = processor(image, return_tensors="pt")

         >>> # forward pass
         >>> with torch.no_grad():
         ...     outputs = model(**inputs)

         >>> output = outputs.reconstruction.data.squeeze().float().cpu().clamp_(0, 1).numpy()
         >>> output = np.moveaxis(output, source=0, destination=-1)
         >>> output = (output * 255.0).round().astype(np.uint8)  # float32 to uint8
         >>> # you can visualize `output` with `Image.fromarray`
         ```'''
