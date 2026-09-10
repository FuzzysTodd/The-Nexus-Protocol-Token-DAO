import torch
from ...activations import ACT2FN as ACT2FN
from ...modeling_outputs import BaseModelOutputWithNoAttention as BaseModelOutputWithNoAttention, BaseModelOutputWithPoolingAndNoAttention as BaseModelOutputWithPoolingAndNoAttention, ImageClassifierOutputWithNoAttention as ImageClassifierOutputWithNoAttention, SemanticSegmenterOutput as SemanticSegmenterOutput
from ...modeling_utils import PreTrainedModel as PreTrainedModel
from ...pytorch_utils import find_pruneable_heads_and_indices as find_pruneable_heads_and_indices, prune_linear_layer as prune_linear_layer
from ...utils import add_code_sample_docstrings as add_code_sample_docstrings, add_start_docstrings as add_start_docstrings, add_start_docstrings_to_model_forward as add_start_docstrings_to_model_forward, logging as logging, replace_return_docstrings as replace_return_docstrings
from .configuration_mobilevit import MobileViTConfig as MobileViTConfig
from _typeshed import Incomplete
from torch import nn
from typing import Dict, Optional, Set, Tuple, Union

logger: Incomplete
MOBILEVIT_PRETRAINED_MODEL_ARCHIVE_LIST: Incomplete

def make_divisible(value: int, divisor: int = 8, min_value: Optional[int] = None) -> int:
    """
    Ensure that all layers have a channel count that is divisible by `divisor`. This function is taken from the
    original TensorFlow repo. It can be seen here:
    https://github.com/tensorflow/models/blob/master/research/slim/nets/mobilenet/mobilenet.py
    """

class MobileViTConvLayer(nn.Module):
    convolution: Incomplete
    normalization: Incomplete
    activation: Incomplete
    def __init__(self, config: MobileViTConfig, in_channels: int, out_channels: int, kernel_size: int, stride: int = 1, groups: int = 1, bias: bool = False, dilation: int = 1, use_normalization: bool = True, use_activation: Union[bool, str] = True) -> None: ...
    def forward(self, features: torch.Tensor) -> torch.Tensor: ...

class MobileViTInvertedResidual(nn.Module):
    """
    Inverted residual block (MobileNetv2): https://arxiv.org/abs/1801.04381
    """
    use_residual: Incomplete
    expand_1x1: Incomplete
    conv_3x3: Incomplete
    reduce_1x1: Incomplete
    def __init__(self, config: MobileViTConfig, in_channels: int, out_channels: int, stride: int, dilation: int = 1) -> None: ...
    def forward(self, features: torch.Tensor) -> torch.Tensor: ...

class MobileViTMobileNetLayer(nn.Module):
    layer: Incomplete
    def __init__(self, config: MobileViTConfig, in_channels: int, out_channels: int, stride: int = 1, num_stages: int = 1) -> None: ...
    def forward(self, features: torch.Tensor) -> torch.Tensor: ...

class MobileViTSelfAttention(nn.Module):
    num_attention_heads: Incomplete
    attention_head_size: Incomplete
    all_head_size: Incomplete
    query: Incomplete
    key: Incomplete
    value: Incomplete
    dropout: Incomplete
    def __init__(self, config: MobileViTConfig, hidden_size: int) -> None: ...
    def transpose_for_scores(self, x: torch.Tensor) -> torch.Tensor: ...
    def forward(self, hidden_states: torch.Tensor) -> torch.Tensor: ...

class MobileViTSelfOutput(nn.Module):
    dense: Incomplete
    dropout: Incomplete
    def __init__(self, config: MobileViTConfig, hidden_size: int) -> None: ...
    def forward(self, hidden_states: torch.Tensor) -> torch.Tensor: ...

class MobileViTAttention(nn.Module):
    attention: Incomplete
    output: Incomplete
    pruned_heads: Incomplete
    def __init__(self, config: MobileViTConfig, hidden_size: int) -> None: ...
    def prune_heads(self, heads: Set[int]) -> None: ...
    def forward(self, hidden_states: torch.Tensor) -> torch.Tensor: ...

class MobileViTIntermediate(nn.Module):
    dense: Incomplete
    intermediate_act_fn: Incomplete
    def __init__(self, config: MobileViTConfig, hidden_size: int, intermediate_size: int) -> None: ...
    def forward(self, hidden_states: torch.Tensor) -> torch.Tensor: ...

class MobileViTOutput(nn.Module):
    dense: Incomplete
    dropout: Incomplete
    def __init__(self, config: MobileViTConfig, hidden_size: int, intermediate_size: int) -> None: ...
    def forward(self, hidden_states: torch.Tensor, input_tensor: torch.Tensor) -> torch.Tensor: ...

class MobileViTTransformerLayer(nn.Module):
    attention: Incomplete
    intermediate: Incomplete
    output: Incomplete
    layernorm_before: Incomplete
    layernorm_after: Incomplete
    def __init__(self, config: MobileViTConfig, hidden_size: int, intermediate_size: int) -> None: ...
    def forward(self, hidden_states: torch.Tensor) -> torch.Tensor: ...

class MobileViTTransformer(nn.Module):
    layer: Incomplete
    def __init__(self, config: MobileViTConfig, hidden_size: int, num_stages: int) -> None: ...
    def forward(self, hidden_states: torch.Tensor) -> torch.Tensor: ...

class MobileViTLayer(nn.Module):
    """
    MobileViT block: https://arxiv.org/abs/2110.02178
    """
    patch_width: Incomplete
    patch_height: Incomplete
    downsampling_layer: Incomplete
    conv_kxk: Incomplete
    conv_1x1: Incomplete
    transformer: Incomplete
    layernorm: Incomplete
    conv_projection: Incomplete
    fusion: Incomplete
    def __init__(self, config: MobileViTConfig, in_channels: int, out_channels: int, stride: int, hidden_size: int, num_stages: int, dilation: int = 1) -> None: ...
    def unfolding(self, features: torch.Tensor) -> Tuple[torch.Tensor, Dict]: ...
    def folding(self, patches: torch.Tensor, info_dict: Dict) -> torch.Tensor: ...
    def forward(self, features: torch.Tensor) -> torch.Tensor: ...

class MobileViTEncoder(nn.Module):
    config: Incomplete
    layer: Incomplete
    gradient_checkpointing: bool
    def __init__(self, config: MobileViTConfig) -> None: ...
    def forward(self, hidden_states: torch.Tensor, output_hidden_states: bool = False, return_dict: bool = True) -> Union[tuple, BaseModelOutputWithNoAttention]: ...

class MobileViTPreTrainedModel(PreTrainedModel):
    """
    An abstract class to handle weights initialization and a simple interface for downloading and loading pretrained
    models.
    """
    config_class = MobileViTConfig
    base_model_prefix: str
    main_input_name: str
    supports_gradient_checkpointing: bool

MOBILEVIT_START_DOCSTRING: str
MOBILEVIT_INPUTS_DOCSTRING: str

class MobileViTModel(MobileViTPreTrainedModel):
    config: Incomplete
    expand_output: Incomplete
    conv_stem: Incomplete
    encoder: Incomplete
    conv_1x1_exp: Incomplete
    def __init__(self, config: MobileViTConfig, expand_output: bool = True) -> None: ...
    def forward(self, pixel_values: Optional[torch.Tensor] = None, output_hidden_states: Optional[bool] = None, return_dict: Optional[bool] = None) -> Union[tuple, BaseModelOutputWithPoolingAndNoAttention]: ...

class MobileViTForImageClassification(MobileViTPreTrainedModel):
    num_labels: Incomplete
    mobilevit: Incomplete
    dropout: Incomplete
    classifier: Incomplete
    def __init__(self, config: MobileViTConfig) -> None: ...
    def forward(self, pixel_values: Optional[torch.Tensor] = None, output_hidden_states: Optional[bool] = None, labels: Optional[torch.Tensor] = None, return_dict: Optional[bool] = None) -> Union[tuple, ImageClassifierOutputWithNoAttention]:
        """
        labels (`torch.LongTensor` of shape `(batch_size,)`, *optional*):
            Labels for computing the image classification/regression loss. Indices should be in `[0, ...,
            config.num_labels - 1]`. If `config.num_labels == 1` a regression loss is computed (Mean-Square loss). If
            `config.num_labels > 1` a classification loss is computed (Cross-Entropy).
        """

class MobileViTASPPPooling(nn.Module):
    global_pool: Incomplete
    conv_1x1: Incomplete
    def __init__(self, config: MobileViTConfig, in_channels: int, out_channels: int) -> None: ...
    def forward(self, features: torch.Tensor) -> torch.Tensor: ...

class MobileViTASPP(nn.Module):
    """
    ASPP module defined in DeepLab papers: https://arxiv.org/abs/1606.00915, https://arxiv.org/abs/1706.05587
    """
    convs: Incomplete
    project: Incomplete
    dropout: Incomplete
    def __init__(self, config: MobileViTConfig) -> None: ...
    def forward(self, features: torch.Tensor) -> torch.Tensor: ...

class MobileViTDeepLabV3(nn.Module):
    """
    DeepLabv3 architecture: https://arxiv.org/abs/1706.05587
    """
    aspp: Incomplete
    dropout: Incomplete
    classifier: Incomplete
    def __init__(self, config: MobileViTConfig) -> None: ...
    def forward(self, hidden_states: torch.Tensor) -> torch.Tensor: ...

class MobileViTForSemanticSegmentation(MobileViTPreTrainedModel):
    num_labels: Incomplete
    mobilevit: Incomplete
    segmentation_head: Incomplete
    def __init__(self, config: MobileViTConfig) -> None: ...
    def forward(self, pixel_values: Optional[torch.Tensor] = None, labels: Optional[torch.Tensor] = None, output_hidden_states: Optional[bool] = None, return_dict: Optional[bool] = None) -> Union[tuple, SemanticSegmenterOutput]:
        '''
        labels (`torch.LongTensor` of shape `(batch_size, height, width)`, *optional*):
            Ground truth semantic segmentation maps for computing the loss. Indices should be in `[0, ...,
            config.num_labels - 1]`. If `config.num_labels > 1`, a classification loss is computed (Cross-Entropy).

        Returns:

        Examples:

        ```python
        >>> from transformers import AutoImageProcessor, MobileViTForSemanticSegmentation
        >>> from PIL import Image
        >>> import requests

        >>> url = "http://images.cocodataset.org/val2017/000000039769.jpg"
        >>> image = Image.open(requests.get(url, stream=True).raw)

        >>> image_processor = AutoImageProcessor.from_pretrained("apple/deeplabv3-mobilevit-small")
        >>> model = MobileViTForSemanticSegmentation.from_pretrained("apple/deeplabv3-mobilevit-small")

        >>> inputs = image_processor(images=image, return_tensors="pt")

        >>> with torch.no_grad():
        ...     outputs = model(**inputs)

        >>> # logits are of shape (batch_size, num_labels, height, width)
        >>> logits = outputs.logits
        ```'''
