import torch
from ...activations import ACT2FN as ACT2FN
from ...modeling_outputs import BaseModelOutputWithPoolingAndNoAttention as BaseModelOutputWithPoolingAndNoAttention, ImageClassifierOutputWithNoAttention as ImageClassifierOutputWithNoAttention, SemanticSegmenterOutput as SemanticSegmenterOutput
from ...modeling_utils import PreTrainedModel as PreTrainedModel
from ...utils import add_code_sample_docstrings as add_code_sample_docstrings, add_start_docstrings as add_start_docstrings, add_start_docstrings_to_model_forward as add_start_docstrings_to_model_forward, logging as logging, replace_return_docstrings as replace_return_docstrings
from .configuration_mobilenet_v2 import MobileNetV2Config as MobileNetV2Config
from _typeshed import Incomplete
from torch import nn
from typing import Optional, Union

logger: Incomplete
MOBILENET_V2_PRETRAINED_MODEL_ARCHIVE_LIST: Incomplete

def load_tf_weights_in_mobilenet_v2(model, config, tf_checkpoint_path):
    """Load TensorFlow checkpoints in a PyTorch model."""
def make_divisible(value: int, divisor: int = 8, min_value: Optional[int] = None) -> int:
    """
    Ensure that all layers have a channel count that is divisible by `divisor`. This function is taken from the
    original TensorFlow repo. It can be seen here:
    https://github.com/tensorflow/models/blob/master/research/slim/nets/mobilenet/mobilenet.py
    """
def apply_depth_multiplier(config: MobileNetV2Config, channels: int) -> int: ...
def apply_tf_padding(features: torch.Tensor, conv_layer: nn.Conv2d) -> torch.Tensor:
    '''
    Apply TensorFlow-style "SAME" padding to a convolution layer. See the notes at:
    https://www.tensorflow.org/api_docs/python/tf/nn#notes_on_padding_2
    '''

class MobileNetV2ConvLayer(nn.Module):
    config: Incomplete
    convolution: Incomplete
    normalization: Incomplete
    activation: Incomplete
    def __init__(self, config: MobileNetV2Config, in_channels: int, out_channels: int, kernel_size: int, stride: int = 1, groups: int = 1, bias: bool = False, dilation: int = 1, use_normalization: bool = True, use_activation: Union[bool, str] = True, layer_norm_eps: Optional[float] = None) -> None: ...
    def forward(self, features: torch.Tensor) -> torch.Tensor: ...

class MobileNetV2InvertedResidual(nn.Module):
    use_residual: Incomplete
    expand_1x1: Incomplete
    conv_3x3: Incomplete
    reduce_1x1: Incomplete
    def __init__(self, config: MobileNetV2Config, in_channels: int, out_channels: int, stride: int, dilation: int = 1) -> None: ...
    def forward(self, features: torch.Tensor) -> torch.Tensor: ...

class MobileNetV2Stem(nn.Module):
    first_conv: Incomplete
    expand_1x1: Incomplete
    conv_3x3: Incomplete
    reduce_1x1: Incomplete
    def __init__(self, config: MobileNetV2Config, in_channels: int, expanded_channels: int, out_channels: int) -> None: ...
    def forward(self, features: torch.Tensor) -> torch.Tensor: ...

class MobileNetV2PreTrainedModel(PreTrainedModel):
    """
    An abstract class to handle weights initialization and a simple interface for downloading and loading pretrained
    models.
    """
    config_class = MobileNetV2Config
    load_tf_weights = load_tf_weights_in_mobilenet_v2
    base_model_prefix: str
    main_input_name: str
    supports_gradient_checkpointing: bool

MOBILENET_V2_START_DOCSTRING: str
MOBILENET_V2_INPUTS_DOCSTRING: str

class MobileNetV2Model(MobileNetV2PreTrainedModel):
    config: Incomplete
    conv_stem: Incomplete
    layer: Incomplete
    conv_1x1: Incomplete
    pooler: Incomplete
    def __init__(self, config: MobileNetV2Config, add_pooling_layer: bool = True) -> None: ...
    def forward(self, pixel_values: Optional[torch.Tensor] = None, output_hidden_states: Optional[bool] = None, return_dict: Optional[bool] = None) -> Union[tuple, BaseModelOutputWithPoolingAndNoAttention]: ...

class MobileNetV2ForImageClassification(MobileNetV2PreTrainedModel):
    num_labels: Incomplete
    mobilenet_v2: Incomplete
    dropout: Incomplete
    classifier: Incomplete
    def __init__(self, config: MobileNetV2Config) -> None: ...
    def forward(self, pixel_values: Optional[torch.Tensor] = None, output_hidden_states: Optional[bool] = None, labels: Optional[torch.Tensor] = None, return_dict: Optional[bool] = None) -> Union[tuple, ImageClassifierOutputWithNoAttention]:
        """
        labels (`torch.LongTensor` of shape `(batch_size,)`, *optional*):
            Labels for computing the image classification/regression loss. Indices should be in `[0, ...,
            config.num_labels - 1]`. If `config.num_labels == 1` a regression loss is computed (Mean-Square loss). If
            `config.num_labels > 1` a classification loss is computed (Cross-Entropy).
        """

class MobileNetV2DeepLabV3Plus(nn.Module):
    '''
    The neural network from the paper "Encoder-Decoder with Atrous Separable Convolution for Semantic Image
    Segmentation" https://arxiv.org/abs/1802.02611
    '''
    avg_pool: Incomplete
    conv_pool: Incomplete
    conv_aspp: Incomplete
    conv_projection: Incomplete
    dropout: Incomplete
    classifier: Incomplete
    def __init__(self, config: MobileNetV2Config) -> None: ...
    def forward(self, features: torch.Tensor) -> torch.Tensor: ...

class MobileNetV2ForSemanticSegmentation(MobileNetV2PreTrainedModel):
    num_labels: Incomplete
    mobilenet_v2: Incomplete
    segmentation_head: Incomplete
    def __init__(self, config: MobileNetV2Config) -> None: ...
    def forward(self, pixel_values: Optional[torch.Tensor] = None, labels: Optional[torch.Tensor] = None, output_hidden_states: Optional[bool] = None, return_dict: Optional[bool] = None) -> Union[tuple, SemanticSegmenterOutput]:
        '''
        labels (`torch.LongTensor` of shape `(batch_size, height, width)`, *optional*):
            Ground truth semantic segmentation maps for computing the loss. Indices should be in `[0, ...,
            config.num_labels - 1]`. If `config.num_labels > 1`, a classification loss is computed (Cross-Entropy).

        Returns:

        Examples:

        ```python
        >>> from transformers import AutoImageProcessor, MobileNetV2ForSemanticSegmentation
        >>> from PIL import Image
        >>> import requests

        >>> url = "http://images.cocodataset.org/val2017/000000039769.jpg"
        >>> image = Image.open(requests.get(url, stream=True).raw)

        >>> image_processor = AutoImageProcessor.from_pretrained("google/deeplabv3_mobilenet_v2_1.0_513")
        >>> model = MobileNetV2ForSemanticSegmentation.from_pretrained("google/deeplabv3_mobilenet_v2_1.0_513")

        >>> inputs = image_processor(images=image, return_tensors="pt")

        >>> with torch.no_grad():
        ...     outputs = model(**inputs)

        >>> # logits are of shape (batch_size, num_labels, height, width)
        >>> logits = outputs.logits
        ```'''
