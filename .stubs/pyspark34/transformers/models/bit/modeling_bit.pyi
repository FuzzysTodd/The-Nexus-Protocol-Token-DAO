import torch
from ...activations import ACT2FN as ACT2FN
from ...modeling_outputs import BackboneOutput as BackboneOutput, BaseModelOutputWithNoAttention as BaseModelOutputWithNoAttention, BaseModelOutputWithPoolingAndNoAttention as BaseModelOutputWithPoolingAndNoAttention, ImageClassifierOutputWithNoAttention as ImageClassifierOutputWithNoAttention
from ...modeling_utils import BackboneMixin as BackboneMixin, PreTrainedModel as PreTrainedModel
from ...utils import add_code_sample_docstrings as add_code_sample_docstrings, add_start_docstrings as add_start_docstrings, add_start_docstrings_to_model_forward as add_start_docstrings_to_model_forward, logging as logging, replace_return_docstrings as replace_return_docstrings
from .configuration_bit import BitConfig as BitConfig
from _typeshed import Incomplete
from torch import Tensor as Tensor, nn
from typing import Optional, Tuple

logger: Incomplete
BIT_PRETRAINED_MODEL_ARCHIVE_LIST: Incomplete

def get_padding_value(padding: Incomplete | None = None, kernel_size: int = 7, stride: int = 1, dilation: int = 1) -> Tuple[Tuple, bool]:
    '''
    Utility function to get the tuple padding value given the kernel_size and padding.

    Args:
        padding (Union[`str`, `int`], *optional*):
            Padding value, can be either `"same"`, `"valid"`. If a different value is provided the default padding from
            PyTorch is used.
        kernel_size (`int`, *optional*, defaults to 7):
            Kernel size of the convolution layers.
        stride (`int`, *optional*, defaults to 1):
            Stride value of the convolution layers.
        dilation (`int`, *optional*, defaults to 1):
            Dilation value of the convolution layers.
    '''

class WeightStandardizedConv2d(nn.Conv2d):
    """Conv2d with Weight Standardization. Includes TensorFlow compatible SAME padding. Used for ViT Hybrid model.

    Paper: [Micro-Batch Training with Batch-Channel Normalization and Weight
    Standardization](https://arxiv.org/abs/1903.10520v2)
    """
    pad: Incomplete
    eps: Incomplete
    def __init__(self, in_channel, out_channels, kernel_size, stride: int = 1, padding: str = 'SAME', dilation: int = 1, groups: int = 1, bias: bool = False, eps: float = 1e-06) -> None: ...
    def forward(self, hidden_state): ...

class BitGroupNormActivation(nn.GroupNorm):
    """
    A module that combines group normalization with an activation function.
    """
    activation: Incomplete
    def __init__(self, config, num_channels, eps: float = 1e-05, affine: bool = True, apply_activation: bool = True) -> None: ...
    def forward(self, hidden_state): ...

class DynamicPad2d(nn.Module):
    """
    A module that wraps dynamic padding of any input, given the parameters of the convolutional layer and the input
    hidden states.
    """
    kernel_size: Incomplete
    stride: Incomplete
    dilation: Incomplete
    value: Incomplete
    compute_padding: Incomplete
    def __init__(self, kernel_size, stride, dilation, value: int = 0) -> None: ...
    def __call__(self, input): ...

class BitMaxPool2d(nn.MaxPool2d):
    """Tensorflow like 'SAME' wrapper for 2D max pooling"""
    pad: Incomplete
    def __init__(self, kernel_size: int, stride: Incomplete | None = None, dilation: int = 1, ceil_mode: bool = False, padding=(0, 0), padding_value: int = 0, use_dynamic_padding: bool = True) -> None: ...
    def forward(self, hidden_states): ...

class BitEmbeddings(nn.Module):
    """
    BiT Embeddings (stem) composed of a single aggressive convolution.
    """
    convolution: Incomplete
    pooler: Incomplete
    pad: Incomplete
    norm: Incomplete
    num_channels: Incomplete
    def __init__(self, config: BitConfig) -> None: ...
    def forward(self, pixel_values: Tensor) -> Tensor: ...

def drop_path(input, drop_prob: float = 0.0, training: bool = False):
    """
    Drop paths (Stochastic Depth) per sample (when applied in main path of residual blocks).

    Comment by Ross Wightman: This is the same as the DropConnect impl I created for EfficientNet, etc networks,
    however, the original name is misleading as 'Drop Connect' is a different form of dropout in a separate paper...
    See discussion: https://github.com/tensorflow/tpu/issues/494#issuecomment-532968956 ... I've opted for changing the
    layer and argument names to 'drop path' rather than mix DropConnect as a layer name and use 'survival rate' as the
    argument.
    """

class BitDropPath(nn.Module):
    """Drop paths (Stochastic Depth) per sample (when applied in main path of residual blocks)."""
    drop_prob: Incomplete
    def __init__(self, drop_prob: Optional[float] = None) -> None: ...
    def forward(self, hidden_states: torch.Tensor) -> torch.Tensor: ...
    def extra_repr(self) -> str: ...

def make_div(value, divisor: int = 8): ...

class BitPreActivationBottleneckLayer(nn.Module):
    '''Pre-activation (v2) bottleneck block.
    Follows the implementation of "Identity Mappings in Deep Residual Networks":
    https://github.com/KaimingHe/resnet-1k-layers/blob/master/resnet-pre-act.lua

    Except it puts the stride on 3x3 conv when available.
    '''
    downsample: Incomplete
    norm1: Incomplete
    conv1: Incomplete
    norm2: Incomplete
    conv2: Incomplete
    norm3: Incomplete
    conv3: Incomplete
    drop_path: Incomplete
    def __init__(self, config, in_channels, out_channels: Incomplete | None = None, bottle_ratio: float = 0.25, stride: int = 1, dilation: int = 1, first_dilation: Incomplete | None = None, groups: int = 1, drop_path_rate: float = 0.0, is_first_layer: bool = False) -> None: ...
    def forward(self, hidden_states): ...

class BitBottleneckLayer(nn.Module):
    """Non Pre-activation bottleneck block, equivalent to V1.5/V1b bottleneck. Used for ViT Hybrid."""
    downsample: Incomplete
    conv1: Incomplete
    norm1: Incomplete
    conv2: Incomplete
    norm2: Incomplete
    conv3: Incomplete
    norm3: Incomplete
    drop_path: Incomplete
    activation: Incomplete
    def __init__(self, config, in_channels, out_channels: Incomplete | None = None, bottle_ratio: float = 0.25, stride: int = 1, dilation: int = 1, first_dilation: Incomplete | None = None, groups: int = 1, drop_path_rate: float = 0.0, is_first_layer: bool = False) -> None: ...
    def forward(self, hidden_states): ...

class BitDownsampleConv(nn.Module):
    conv: Incomplete
    norm: Incomplete
    def __init__(self, config, in_channels, out_channels, stride: int = 1, preact: bool = True) -> None: ...
    def forward(self, x): ...

class BitStage(nn.Module):
    """
    A ResNet v2 stage composed by stacked layers.
    """
    layers: Incomplete
    def __init__(self, config, in_channels, out_channels, stride, dilation, depth, bottle_ratio: float = 0.25, layer_dropout: Incomplete | None = None) -> None: ...
    def forward(self, input: Tensor) -> Tensor: ...

class BitEncoder(nn.Module):
    stages: Incomplete
    def __init__(self, config: BitConfig) -> None: ...
    def forward(self, hidden_state: Tensor, output_hidden_states: bool = False, return_dict: bool = True) -> BaseModelOutputWithNoAttention: ...

class BitPreTrainedModel(PreTrainedModel):
    """
    An abstract class to handle weights initialization and a simple interface for downloading and loading pretrained
    models.
    """
    config_class = BitConfig
    base_model_prefix: str
    main_input_name: str
    supports_gradient_checkpointing: bool

BIT_START_DOCSTRING: str
BIT_INPUTS_DOCSTRING: str

class BitModel(BitPreTrainedModel):
    config: Incomplete
    embedder: Incomplete
    encoder: Incomplete
    norm: Incomplete
    pooler: Incomplete
    def __init__(self, config) -> None: ...
    def forward(self, pixel_values: Tensor, output_hidden_states: Optional[bool] = None, return_dict: Optional[bool] = None) -> BaseModelOutputWithPoolingAndNoAttention: ...

class BitForImageClassification(BitPreTrainedModel):
    num_labels: Incomplete
    bit: Incomplete
    classifier: Incomplete
    def __init__(self, config) -> None: ...
    def forward(self, pixel_values: Optional[torch.FloatTensor] = None, labels: Optional[torch.LongTensor] = None, output_hidden_states: Optional[bool] = None, return_dict: Optional[bool] = None) -> ImageClassifierOutputWithNoAttention:
        """
        labels (`torch.LongTensor` of shape `(batch_size,)`, *optional*):
            Labels for computing the image classification/regression loss. Indices should be in `[0, ...,
            config.num_labels - 1]`. If `config.num_labels > 1` a classification loss is computed (Cross-Entropy).
        """

class BitBackbone(BitPreTrainedModel, BackboneMixin):
    stage_names: Incomplete
    bit: Incomplete
    out_features: Incomplete
    out_feature_channels: Incomplete
    def __init__(self, config) -> None: ...
    @property
    def channels(self): ...
    def forward(self, pixel_values: Tensor, output_hidden_states: Optional[bool] = None, return_dict: Optional[bool] = None) -> BackboneOutput:
        '''
        Returns:

        Examples:

        ```python
        >>> from transformers import AutoImageProcessor, AutoBackbone
        >>> import torch
        >>> from PIL import Image
        >>> import requests

        >>> url = "http://images.cocodataset.org/val2017/000000039769.jpg"
        >>> image = Image.open(requests.get(url, stream=True).raw)

        >>> processor = AutoImageProcessor.from_pretrained("google/resnetnv2-50")
        >>> model = AutoBackbone.from_pretrained("google/resnetnv2-50")

        >>> inputs = processor(image, return_tensors="pt")
        >>> outputs = model(**inputs)
        ```'''
