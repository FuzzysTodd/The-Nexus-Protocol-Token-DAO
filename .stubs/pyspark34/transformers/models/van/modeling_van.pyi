import torch
from ...activations import ACT2FN as ACT2FN
from ...modeling_outputs import BaseModelOutputWithNoAttention as BaseModelOutputWithNoAttention, BaseModelOutputWithPoolingAndNoAttention as BaseModelOutputWithPoolingAndNoAttention, ImageClassifierOutputWithNoAttention as ImageClassifierOutputWithNoAttention
from ...modeling_utils import PreTrainedModel as PreTrainedModel
from ...utils import add_code_sample_docstrings as add_code_sample_docstrings, add_start_docstrings as add_start_docstrings, add_start_docstrings_to_model_forward as add_start_docstrings_to_model_forward, logging as logging
from .configuration_van import VanConfig as VanConfig
from _typeshed import Incomplete
from torch import nn
from typing import Optional, Tuple, Union

logger: Incomplete
VAN_PRETRAINED_MODEL_ARCHIVE_LIST: Incomplete

def drop_path(input, drop_prob: float = 0.0, training: bool = False):
    """
    Drop paths (Stochastic Depth) per sample (when applied in main path of residual blocks).

    Comment by Ross Wightman: This is the same as the DropConnect impl I created for EfficientNet, etc networks,
    however, the original name is misleading as 'Drop Connect' is a different form of dropout in a separate paper...
    See discussion: https://github.com/tensorflow/tpu/issues/494#issuecomment-532968956 ... I've opted for changing the
    layer and argument names to 'drop path' rather than mix DropConnect as a layer name and use 'survival rate' as the
    argument.
    """

class VanDropPath(nn.Module):
    """Drop paths (Stochastic Depth) per sample (when applied in main path of residual blocks)."""
    drop_prob: Incomplete
    def __init__(self, drop_prob: Optional[float] = None) -> None: ...
    def forward(self, hidden_states: torch.Tensor) -> torch.Tensor: ...
    def extra_repr(self) -> str: ...

class VanOverlappingPatchEmbedder(nn.Module):
    """
    Downsamples the input using a patchify operation with a `stride` of 4 by default making adjacent windows overlap by
    half of the area. From [PVTv2: Improved Baselines with Pyramid Vision
    Transformer](https://arxiv.org/abs/2106.13797).
    """
    convolution: Incomplete
    normalization: Incomplete
    def __init__(self, in_channels: int, hidden_size: int, patch_size: int = 7, stride: int = 4) -> None: ...
    def forward(self, input: torch.Tensor) -> torch.Tensor: ...

class VanMlpLayer(nn.Module):
    """
    MLP with depth-wise convolution, from [PVTv2: Improved Baselines with Pyramid Vision
    Transformer](https://arxiv.org/abs/2106.13797).
    """
    in_dense: Incomplete
    depth_wise: Incomplete
    activation: Incomplete
    dropout1: Incomplete
    out_dense: Incomplete
    dropout2: Incomplete
    def __init__(self, in_channels: int, hidden_size: int, out_channels: int, hidden_act: str = 'gelu', dropout_rate: float = 0.5) -> None: ...
    def forward(self, hidden_state: torch.Tensor) -> torch.Tensor: ...

class VanLargeKernelAttention(nn.Module):
    """
    Basic Large Kernel Attention (LKA).
    """
    depth_wise: Incomplete
    depth_wise_dilated: Incomplete
    point_wise: Incomplete
    def __init__(self, hidden_size: int) -> None: ...
    def forward(self, hidden_state: torch.Tensor) -> torch.Tensor: ...

class VanLargeKernelAttentionLayer(nn.Module):
    """
    Computes attention using Large Kernel Attention (LKA) and attends the input.
    """
    attention: Incomplete
    def __init__(self, hidden_size: int) -> None: ...
    def forward(self, hidden_state: torch.Tensor) -> torch.Tensor: ...

class VanSpatialAttentionLayer(nn.Module):
    """
    Van spatial attention layer composed by projection (via conv) -> act -> Large Kernel Attention (LKA) attention ->
    projection (via conv) + residual connection.
    """
    pre_projection: Incomplete
    attention_layer: Incomplete
    post_projection: Incomplete
    def __init__(self, hidden_size: int, hidden_act: str = 'gelu') -> None: ...
    def forward(self, hidden_state: torch.Tensor) -> torch.Tensor: ...

class VanLayerScaling(nn.Module):
    """
    Scales the inputs by a learnable parameter initialized by `initial_value`.
    """
    weight: Incomplete
    def __init__(self, hidden_size: int, initial_value: float = 0.01) -> None: ...
    def forward(self, hidden_state: torch.Tensor) -> torch.Tensor: ...

class VanLayer(nn.Module):
    """
    Van layer composed by normalization layers, large kernel attention (LKA) and a multi layer perceptron (MLP).
    """
    drop_path: Incomplete
    pre_normomalization: Incomplete
    attention: Incomplete
    attention_scaling: Incomplete
    post_normalization: Incomplete
    mlp: Incomplete
    mlp_scaling: Incomplete
    def __init__(self, config: VanConfig, hidden_size: int, mlp_ratio: int = 4, drop_path_rate: float = 0.5) -> None: ...
    def forward(self, hidden_state: torch.Tensor) -> torch.Tensor: ...

class VanStage(nn.Module):
    """
    VanStage, consisting of multiple layers.
    """
    embeddings: Incomplete
    layers: Incomplete
    normalization: Incomplete
    def __init__(self, config: VanConfig, in_channels: int, hidden_size: int, patch_size: int, stride: int, depth: int, mlp_ratio: int = 4, drop_path_rate: float = 0.0) -> None: ...
    def forward(self, hidden_state: torch.Tensor) -> torch.Tensor: ...

class VanEncoder(nn.Module):
    """
    VanEncoder, consisting of multiple stages.
    """
    stages: Incomplete
    def __init__(self, config: VanConfig) -> None: ...
    def forward(self, hidden_state: torch.Tensor, output_hidden_states: Optional[bool] = False, return_dict: Optional[bool] = True) -> Union[Tuple, BaseModelOutputWithNoAttention]: ...

class VanPreTrainedModel(PreTrainedModel):
    """
    An abstract class to handle weights initialization and a simple interface for downloading and loading pretrained
    models.
    """
    config_class = VanConfig
    base_model_prefix: str
    main_input_name: str
    supports_gradient_checkpointing: bool

VAN_START_DOCSTRING: str
VAN_INPUTS_DOCSTRING: str

class VanModel(VanPreTrainedModel):
    config: Incomplete
    encoder: Incomplete
    layernorm: Incomplete
    def __init__(self, config) -> None: ...
    def forward(self, pixel_values: Optional[torch.FloatTensor], output_hidden_states: Optional[bool] = None, return_dict: Optional[bool] = None) -> Union[Tuple, BaseModelOutputWithPoolingAndNoAttention]: ...

class VanForImageClassification(VanPreTrainedModel):
    van: Incomplete
    classifier: Incomplete
    def __init__(self, config) -> None: ...
    def forward(self, pixel_values: Optional[torch.FloatTensor] = None, labels: Optional[torch.LongTensor] = None, output_hidden_states: Optional[bool] = None, return_dict: Optional[bool] = None) -> Union[Tuple, ImageClassifierOutputWithNoAttention]:
        """
        labels (`torch.LongTensor` of shape `(batch_size,)`, *optional*):
            Labels for computing the image classification/regression loss. Indices should be in `[0, ...,
            config.num_labels - 1]`. If `config.num_labels == 1` a regression loss is computed (Mean-Square loss), If
            `config.num_labels > 1` a classification loss is computed (Cross-Entropy).
        """
