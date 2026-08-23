import torch
from ...modeling_outputs import SemanticSegmenterOutput as SemanticSegmenterOutput
from ...modeling_utils import BackboneMixin as BackboneMixin, PreTrainedModel as PreTrainedModel
from ...utils import add_start_docstrings as add_start_docstrings, add_start_docstrings_to_model_forward as add_start_docstrings_to_model_forward, replace_return_docstrings as replace_return_docstrings
from .configuration_upernet import UperNetConfig as UperNetConfig
from _typeshed import Incomplete
from torch import nn
from transformers import AutoBackbone as AutoBackbone
from typing import List, Optional, Tuple, Union

UPERNET_PRETRAINED_MODEL_ARCHIVE_LIST: Incomplete

class UperNetConvModule(nn.Module):
    """
    A convolutional block that bundles conv/norm/activation layers. This block simplifies the usage of convolution
    layers, which are commonly used with a norm layer (e.g., BatchNorm) and activation layer (e.g., ReLU).
    """
    conv: Incomplete
    batch_norm: Incomplete
    activation: Incomplete
    def __init__(self, in_channels: int, out_channels: int, kernel_size: Union[int, Tuple[int, int]], padding: Union[int, Tuple[int, int], str] = 0, bias: bool = False, dilation: Union[int, Tuple[int, int]] = 1) -> None: ...
    def forward(self, input: torch.Tensor) -> torch.Tensor: ...

class UperNetPyramidPoolingBlock(nn.Module):
    layers: Incomplete
    def __init__(self, pool_scale: int, in_channels: int, channels: int) -> None: ...
    def forward(self, input: torch.Tensor) -> torch.Tensor: ...

class UperNetPyramidPoolingModule(nn.Module):
    """
    Pyramid Pooling Module (PPM) used in PSPNet.

    Args:
        pool_scales (`Tuple[int]`):
            Pooling scales used in Pooling Pyramid Module.
        in_channels (`int`):
            Input channels.
        channels (`int`):
            Channels after modules, before conv_seg.
        align_corners (`bool`):
            align_corners argument of F.interpolate.
    """
    pool_scales: Incomplete
    align_corners: Incomplete
    in_channels: Incomplete
    channels: Incomplete
    blocks: Incomplete
    def __init__(self, pool_scales: Tuple[int, ...], in_channels: int, channels: int, align_corners: bool) -> None: ...
    def forward(self, x: torch.Tensor) -> List[torch.Tensor]: ...

class UperNetHead(nn.Module):
    """
    Unified Perceptual Parsing for Scene Understanding. This head is the implementation of
    [UPerNet](https://arxiv.org/abs/1807.10221).
    """
    config: Incomplete
    pool_scales: Incomplete
    in_channels: Incomplete
    channels: Incomplete
    align_corners: bool
    classifier: Incomplete
    psp_modules: Incomplete
    bottleneck: Incomplete
    lateral_convs: Incomplete
    fpn_convs: Incomplete
    fpn_bottleneck: Incomplete
    def __init__(self, config, in_channels) -> None: ...
    def init_weights(self) -> None: ...
    def psp_forward(self, inputs): ...
    def forward(self, encoder_hidden_states: torch.Tensor) -> torch.Tensor: ...

class UperNetFCNHead(nn.Module):
    """
    Fully Convolution Networks for Semantic Segmentation. This head is the implementation of
    [FCNNet](https://arxiv.org/abs/1411.4038>).

    Args:
        config:
            Configuration.
        in_channels (int):
            Number of input channels.
        kernel_size (int):
            The kernel size for convs in the head. Default: 3.
        dilation (int):
            The dilation rate for convs in the head. Default: 1.
    """
    config: Incomplete
    in_channels: Incomplete
    channels: Incomplete
    num_convs: Incomplete
    concat_input: Incomplete
    in_index: Incomplete
    convs: Incomplete
    conv_cat: Incomplete
    classifier: Incomplete
    def __init__(self, config, in_index: int = 2, kernel_size: int = 3, dilation: Union[int, Tuple[int, int]] = 1) -> None: ...
    def init_weights(self) -> None: ...
    def forward(self, encoder_hidden_states: torch.Tensor) -> torch.Tensor: ...

class UperNetPreTrainedModel(PreTrainedModel):
    """
    An abstract class to handle weights initialization and a simple interface for downloading and loading pretrained
    models.
    """
    config_class = UperNetConfig
    main_input_name: str
    supports_gradient_checkpointing: bool
    def init_weights(self) -> None:
        """Initialize the weights"""

UPERNET_START_DOCSTRING: str
UPERNET_INPUTS_DOCSTRING: str

class UperNetForSemanticSegmentation(UperNetPreTrainedModel):
    backbone: Incomplete
    decode_head: Incomplete
    auxiliary_head: Incomplete
    def __init__(self, config) -> None: ...
    def forward(self, pixel_values: Optional[torch.Tensor] = None, output_attentions: Optional[bool] = None, output_hidden_states: Optional[bool] = None, labels: Optional[torch.Tensor] = None, return_dict: Optional[bool] = None) -> Union[tuple, SemanticSegmenterOutput]:
        '''
        labels (`torch.LongTensor` of shape `(batch_size, height, width)`, *optional*):
            Ground truth semantic segmentation maps for computing the loss. Indices should be in `[0, ...,
            config.num_labels - 1]`. If `config.num_labels > 1`, a classification loss is computed (Cross-Entropy).

        Returns:

        Examples:
        ```python
        >>> from transformers import AutoImageProcessor, UperNetForSemanticSegmentation
        >>> from PIL import Image
        >>> from huggingface_hub import hf_hub_download

        >>> image_processor = AutoImageProcessor.from_pretrained("openmmlab/upernet-convnext-tiny")
        >>> model = UperNetForSemanticSegmentation.from_pretrained("openmmlab/upernet-convnext-tiny")

        >>> filepath = hf_hub_download(
        ...     repo_id="hf-internal-testing/fixtures_ade20k", filename="ADE_val_00000001.jpg", repo_type="dataset"
        ... )
        >>> image = Image.open(filepath).convert("RGB")

        >>> inputs = image_processor(images=image, return_tensors="pt")

        >>> outputs = model(**inputs)

        >>> logits = outputs.logits  # shape (batch_size, num_labels, height, width)
        >>> list(logits.shape)
        [1, 150, 512, 512]
        ```'''
