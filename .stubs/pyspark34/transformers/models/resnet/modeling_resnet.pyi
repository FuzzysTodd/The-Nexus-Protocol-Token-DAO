import torch
from ...activations import ACT2FN as ACT2FN
from ...modeling_outputs import BackboneOutput as BackboneOutput, BaseModelOutputWithNoAttention as BaseModelOutputWithNoAttention, BaseModelOutputWithPoolingAndNoAttention as BaseModelOutputWithPoolingAndNoAttention, ImageClassifierOutputWithNoAttention as ImageClassifierOutputWithNoAttention
from ...modeling_utils import BackboneMixin as BackboneMixin, PreTrainedModel as PreTrainedModel
from ...utils import add_code_sample_docstrings as add_code_sample_docstrings, add_start_docstrings as add_start_docstrings, add_start_docstrings_to_model_forward as add_start_docstrings_to_model_forward, logging as logging, replace_return_docstrings as replace_return_docstrings
from .configuration_resnet import ResNetConfig as ResNetConfig
from _typeshed import Incomplete
from torch import Tensor as Tensor, nn
from typing import Optional

logger: Incomplete
RESNET_PRETRAINED_MODEL_ARCHIVE_LIST: Incomplete

class ResNetConvLayer(nn.Module):
    convolution: Incomplete
    normalization: Incomplete
    activation: Incomplete
    def __init__(self, in_channels: int, out_channels: int, kernel_size: int = 3, stride: int = 1, activation: str = 'relu') -> None: ...
    def forward(self, input: Tensor) -> Tensor: ...

class ResNetEmbeddings(nn.Module):
    """
    ResNet Embeddings (stem) composed of a single aggressive convolution.
    """
    embedder: Incomplete
    pooler: Incomplete
    num_channels: Incomplete
    def __init__(self, config: ResNetConfig) -> None: ...
    def forward(self, pixel_values: Tensor) -> Tensor: ...

class ResNetShortCut(nn.Module):
    """
    ResNet shortcut, used to project the residual features to the correct size. If needed, it is also used to
    downsample the input using `stride=2`.
    """
    convolution: Incomplete
    normalization: Incomplete
    def __init__(self, in_channels: int, out_channels: int, stride: int = 2) -> None: ...
    def forward(self, input: Tensor) -> Tensor: ...

class ResNetBasicLayer(nn.Module):
    """
    A classic ResNet's residual layer composed by two `3x3` convolutions.
    """
    shortcut: Incomplete
    layer: Incomplete
    activation: Incomplete
    def __init__(self, in_channels: int, out_channels: int, stride: int = 1, activation: str = 'relu') -> None: ...
    def forward(self, hidden_state): ...

class ResNetBottleNeckLayer(nn.Module):
    """
    A classic ResNet's bottleneck layer composed by three `3x3` convolutions.

    The first `1x1` convolution reduces the input by a factor of `reduction` in order to make the second `3x3`
    convolution faster. The last `1x1` convolution remaps the reduced features to `out_channels`.
    """
    shortcut: Incomplete
    layer: Incomplete
    activation: Incomplete
    def __init__(self, in_channels: int, out_channels: int, stride: int = 1, activation: str = 'relu', reduction: int = 4) -> None: ...
    def forward(self, hidden_state): ...

class ResNetStage(nn.Module):
    """
    A ResNet stage composed by stacked layers.
    """
    layers: Incomplete
    def __init__(self, config: ResNetConfig, in_channels: int, out_channels: int, stride: int = 2, depth: int = 2) -> None: ...
    def forward(self, input: Tensor) -> Tensor: ...

class ResNetEncoder(nn.Module):
    stages: Incomplete
    def __init__(self, config: ResNetConfig) -> None: ...
    def forward(self, hidden_state: Tensor, output_hidden_states: bool = False, return_dict: bool = True) -> BaseModelOutputWithNoAttention: ...

class ResNetPreTrainedModel(PreTrainedModel):
    """
    An abstract class to handle weights initialization and a simple interface for downloading and loading pretrained
    models.
    """
    config_class = ResNetConfig
    base_model_prefix: str
    main_input_name: str
    supports_gradient_checkpointing: bool

RESNET_START_DOCSTRING: str
RESNET_INPUTS_DOCSTRING: str

class ResNetModel(ResNetPreTrainedModel):
    config: Incomplete
    embedder: Incomplete
    encoder: Incomplete
    pooler: Incomplete
    def __init__(self, config) -> None: ...
    def forward(self, pixel_values: Tensor, output_hidden_states: Optional[bool] = None, return_dict: Optional[bool] = None) -> BaseModelOutputWithPoolingAndNoAttention: ...

class ResNetForImageClassification(ResNetPreTrainedModel):
    num_labels: Incomplete
    resnet: Incomplete
    classifier: Incomplete
    def __init__(self, config) -> None: ...
    def forward(self, pixel_values: Optional[torch.FloatTensor] = None, labels: Optional[torch.LongTensor] = None, output_hidden_states: Optional[bool] = None, return_dict: Optional[bool] = None) -> ImageClassifierOutputWithNoAttention:
        """
        labels (`torch.LongTensor` of shape `(batch_size,)`, *optional*):
            Labels for computing the image classification/regression loss. Indices should be in `[0, ...,
            config.num_labels - 1]`. If `config.num_labels > 1` a classification loss is computed (Cross-Entropy).
        """

class ResNetBackbone(ResNetPreTrainedModel, BackboneMixin):
    stage_names: Incomplete
    embedder: Incomplete
    encoder: Incomplete
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

        >>> processor = AutoImageProcessor.from_pretrained("microsoft/resnet-50")
        >>> model = AutoBackbone.from_pretrained(
        ...     "microsoft/resnet-50", out_features=["stage1", "stage2", "stage3", "stage4"]
        ... )

        >>> inputs = processor(image, return_tensors="pt")

        >>> outputs = model(**inputs)
        >>> feature_maps = outputs.feature_maps
        >>> list(feature_maps[-1].shape)
        [1, 2048, 7, 7]
        ```'''
