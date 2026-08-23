import torch
from ...activations import ACT2FN as ACT2FN
from ...file_utils import add_code_sample_docstrings as add_code_sample_docstrings, add_start_docstrings as add_start_docstrings, add_start_docstrings_to_model_forward as add_start_docstrings_to_model_forward
from ...modeling_outputs import BaseModelOutputWithNoAttention as BaseModelOutputWithNoAttention, BaseModelOutputWithPoolingAndNoAttention as BaseModelOutputWithPoolingAndNoAttention, ImageClassifierOutputWithNoAttention as ImageClassifierOutputWithNoAttention
from ...modeling_utils import PreTrainedModel as PreTrainedModel
from ...utils import logging as logging
from .configuration_regnet import RegNetConfig as RegNetConfig
from _typeshed import Incomplete
from torch import Tensor as Tensor, nn
from typing import Optional

logger: Incomplete
REGNET_PRETRAINED_MODEL_ARCHIVE_LIST: Incomplete

class RegNetConvLayer(nn.Module):
    convolution: Incomplete
    normalization: Incomplete
    activation: Incomplete
    def __init__(self, in_channels: int, out_channels: int, kernel_size: int = 3, stride: int = 1, groups: int = 1, activation: Optional[str] = 'relu') -> None: ...
    def forward(self, hidden_state): ...

class RegNetEmbeddings(nn.Module):
    """
    RegNet Embedddings (stem) composed of a single aggressive convolution.
    """
    embedder: Incomplete
    num_channels: Incomplete
    def __init__(self, config: RegNetConfig) -> None: ...
    def forward(self, pixel_values): ...

class RegNetShortCut(nn.Module):
    """
    RegNet shortcut, used to project the residual features to the correct size. If needed, it is also used to
    downsample the input using `stride=2`.
    """
    convolution: Incomplete
    normalization: Incomplete
    def __init__(self, in_channels: int, out_channels: int, stride: int = 2) -> None: ...
    def forward(self, input: Tensor) -> Tensor: ...

class RegNetSELayer(nn.Module):
    """
    Squeeze and Excitation layer (SE) proposed in [Squeeze-and-Excitation Networks](https://arxiv.org/abs/1709.01507).
    """
    pooler: Incomplete
    attention: Incomplete
    def __init__(self, in_channels: int, reduced_channels: int) -> None: ...
    def forward(self, hidden_state): ...

class RegNetXLayer(nn.Module):
    """
    RegNet's layer composed by three `3x3` convolutions, same as a ResNet bottleneck layer with reduction = 1.
    """
    shortcut: Incomplete
    layer: Incomplete
    activation: Incomplete
    def __init__(self, config: RegNetConfig, in_channels: int, out_channels: int, stride: int = 1) -> None: ...
    def forward(self, hidden_state): ...

class RegNetYLayer(nn.Module):
    """
    RegNet's Y layer: an X layer with Squeeze and Excitation.
    """
    shortcut: Incomplete
    layer: Incomplete
    activation: Incomplete
    def __init__(self, config: RegNetConfig, in_channels: int, out_channels: int, stride: int = 1) -> None: ...
    def forward(self, hidden_state): ...

class RegNetStage(nn.Module):
    """
    A RegNet stage composed by stacked layers.
    """
    layers: Incomplete
    def __init__(self, config: RegNetConfig, in_channels: int, out_channels: int, stride: int = 2, depth: int = 2) -> None: ...
    def forward(self, hidden_state): ...

class RegNetEncoder(nn.Module):
    stages: Incomplete
    def __init__(self, config: RegNetConfig) -> None: ...
    def forward(self, hidden_state: Tensor, output_hidden_states: bool = False, return_dict: bool = True) -> BaseModelOutputWithNoAttention: ...

class RegNetPreTrainedModel(PreTrainedModel):
    """
    An abstract class to handle weights initialization and a simple interface for downloading and loading pretrained
    models.
    """
    config_class = RegNetConfig
    base_model_prefix: str
    main_input_name: str
    supports_gradient_checkpointing: bool

REGNET_START_DOCSTRING: str
REGNET_INPUTS_DOCSTRING: str

class RegNetModel(RegNetPreTrainedModel):
    config: Incomplete
    embedder: Incomplete
    encoder: Incomplete
    pooler: Incomplete
    def __init__(self, config) -> None: ...
    def forward(self, pixel_values: Tensor, output_hidden_states: Optional[bool] = None, return_dict: Optional[bool] = None) -> BaseModelOutputWithPoolingAndNoAttention: ...

class RegNetForImageClassification(RegNetPreTrainedModel):
    num_labels: Incomplete
    regnet: Incomplete
    classifier: Incomplete
    def __init__(self, config) -> None: ...
    def forward(self, pixel_values: Optional[torch.FloatTensor] = None, labels: Optional[torch.LongTensor] = None, output_hidden_states: Optional[bool] = None, return_dict: Optional[bool] = None) -> ImageClassifierOutputWithNoAttention:
        """
        labels (`torch.LongTensor` of shape `(batch_size,)`, *optional*):
            Labels for computing the image classification/regression loss. Indices should be in `[0, ...,
            config.num_labels - 1]`. If `config.num_labels > 1` a classification loss is computed (Cross-Entropy).
        """
