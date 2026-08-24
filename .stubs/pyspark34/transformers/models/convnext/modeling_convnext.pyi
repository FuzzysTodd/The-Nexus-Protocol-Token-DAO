import torch
from ...activations import ACT2FN as ACT2FN
from ...modeling_outputs import BackboneOutput as BackboneOutput, BaseModelOutputWithNoAttention as BaseModelOutputWithNoAttention, BaseModelOutputWithPoolingAndNoAttention as BaseModelOutputWithPoolingAndNoAttention, ImageClassifierOutputWithNoAttention as ImageClassifierOutputWithNoAttention
from ...modeling_utils import BackboneMixin as BackboneMixin, PreTrainedModel as PreTrainedModel
from ...utils import add_code_sample_docstrings as add_code_sample_docstrings, add_start_docstrings as add_start_docstrings, add_start_docstrings_to_model_forward as add_start_docstrings_to_model_forward, logging as logging, replace_return_docstrings as replace_return_docstrings
from .configuration_convnext import ConvNextConfig as ConvNextConfig
from _typeshed import Incomplete
from torch import nn
from typing import Optional, Tuple, Union

logger: Incomplete
CONVNEXT_PRETRAINED_MODEL_ARCHIVE_LIST: Incomplete

def drop_path(input, drop_prob: float = 0.0, training: bool = False):
    """
    Drop paths (Stochastic Depth) per sample (when applied in main path of residual blocks).

    Comment by Ross Wightman: This is the same as the DropConnect impl I created for EfficientNet, etc networks,
    however, the original name is misleading as 'Drop Connect' is a different form of dropout in a separate paper...
    See discussion: https://github.com/tensorflow/tpu/issues/494#issuecomment-532968956 ... I've opted for changing the
    layer and argument names to 'drop path' rather than mix DropConnect as a layer name and use 'survival rate' as the
    argument.
    """

class ConvNextDropPath(nn.Module):
    """Drop paths (Stochastic Depth) per sample (when applied in main path of residual blocks)."""
    drop_prob: Incomplete
    def __init__(self, drop_prob: Optional[float] = None) -> None: ...
    def forward(self, hidden_states: torch.Tensor) -> torch.Tensor: ...
    def extra_repr(self) -> str: ...

class ConvNextLayerNorm(nn.Module):
    """LayerNorm that supports two data formats: channels_last (default) or channels_first.
    The ordering of the dimensions in the inputs. channels_last corresponds to inputs with shape (batch_size, height,
    width, channels) while channels_first corresponds to inputs with shape (batch_size, channels, height, width).
    """
    weight: Incomplete
    bias: Incomplete
    eps: Incomplete
    data_format: Incomplete
    normalized_shape: Incomplete
    def __init__(self, normalized_shape, eps: float = 1e-06, data_format: str = 'channels_last') -> None: ...
    def forward(self, x: torch.Tensor) -> torch.Tensor: ...

class ConvNextEmbeddings(nn.Module):
    """This class is comparable to (and inspired by) the SwinEmbeddings class
    found in src/transformers/models/swin/modeling_swin.py.
    """
    patch_embeddings: Incomplete
    layernorm: Incomplete
    num_channels: Incomplete
    def __init__(self, config) -> None: ...
    def forward(self, pixel_values: torch.FloatTensor) -> torch.Tensor: ...

class ConvNextLayer(nn.Module):
    """This corresponds to the `Block` class in the original implementation.

    There are two equivalent implementations: [DwConv, LayerNorm (channels_first), Conv, GELU,1x1 Conv]; all in (N, C,
    H, W) (2) [DwConv, Permute to (N, H, W, C), LayerNorm (channels_last), Linear, GELU, Linear]; Permute back

    The authors used (2) as they find it slightly faster in PyTorch.

    Args:
        config ([`ConvNextConfig`]): Model configuration class.
        dim (`int`): Number of input channels.
        drop_path (`float`): Stochastic depth rate. Default: 0.0.
    """
    dwconv: Incomplete
    layernorm: Incomplete
    pwconv1: Incomplete
    act: Incomplete
    pwconv2: Incomplete
    layer_scale_parameter: Incomplete
    drop_path: Incomplete
    def __init__(self, config, dim, drop_path: int = 0) -> None: ...
    def forward(self, hidden_states: torch.FloatTensor) -> torch.Tensor: ...

class ConvNextStage(nn.Module):
    """ConvNeXT stage, consisting of an optional downsampling layer + multiple residual blocks.

    Args:
        config ([`ConvNextConfig`]): Model configuration class.
        in_channels (`int`): Number of input channels.
        out_channels (`int`): Number of output channels.
        depth (`int`): Number of residual blocks.
        drop_path_rates(`List[float]`): Stochastic depth rates for each layer.
    """
    downsampling_layer: Incomplete
    layers: Incomplete
    def __init__(self, config, in_channels, out_channels, kernel_size: int = 2, stride: int = 2, depth: int = 2, drop_path_rates: Incomplete | None = None) -> None: ...
    def forward(self, hidden_states: torch.FloatTensor) -> torch.Tensor: ...

class ConvNextEncoder(nn.Module):
    stages: Incomplete
    def __init__(self, config) -> None: ...
    def forward(self, hidden_states: torch.FloatTensor, output_hidden_states: Optional[bool] = False, return_dict: Optional[bool] = True) -> Union[Tuple, BaseModelOutputWithNoAttention]: ...

class ConvNextPreTrainedModel(PreTrainedModel):
    """
    An abstract class to handle weights initialization and a simple interface for downloading and loading pretrained
    models.
    """
    config_class = ConvNextConfig
    base_model_prefix: str
    main_input_name: str
    supports_gradient_checkpointing: bool

CONVNEXT_START_DOCSTRING: str
CONVNEXT_INPUTS_DOCSTRING: str

class ConvNextModel(ConvNextPreTrainedModel):
    config: Incomplete
    embeddings: Incomplete
    encoder: Incomplete
    layernorm: Incomplete
    def __init__(self, config) -> None: ...
    def forward(self, pixel_values: torch.FloatTensor = None, output_hidden_states: Optional[bool] = None, return_dict: Optional[bool] = None) -> Union[Tuple, BaseModelOutputWithPoolingAndNoAttention]: ...

class ConvNextForImageClassification(ConvNextPreTrainedModel):
    num_labels: Incomplete
    convnext: Incomplete
    classifier: Incomplete
    def __init__(self, config) -> None: ...
    def forward(self, pixel_values: torch.FloatTensor = None, labels: Optional[torch.LongTensor] = None, output_hidden_states: Optional[bool] = None, return_dict: Optional[bool] = None) -> Union[Tuple, ImageClassifierOutputWithNoAttention]:
        """
        labels (`torch.LongTensor` of shape `(batch_size,)`, *optional*):
            Labels for computing the image classification/regression loss. Indices should be in `[0, ...,
            config.num_labels - 1]`. If `config.num_labels == 1` a regression loss is computed (Mean-Square loss), If
            `config.num_labels > 1` a classification loss is computed (Cross-Entropy).
        """

class ConvNextBackbone(ConvNextPreTrainedModel, BackboneMixin):
    stage_names: Incomplete
    embeddings: Incomplete
    encoder: Incomplete
    out_features: Incomplete
    out_feature_channels: Incomplete
    hidden_states_norms: Incomplete
    def __init__(self, config) -> None: ...
    @property
    def channels(self): ...
    def forward(self, pixel_values: torch.Tensor, output_hidden_states: Optional[bool] = None, return_dict: Optional[bool] = None) -> BackboneOutput:
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

        >>> processor = AutoImageProcessor.from_pretrained("facebook/convnext-tiny-224")
        >>> model = AutoBackbone.from_pretrained("facebook/convnext-tiny-224")

        >>> inputs = processor(image, return_tensors="pt")
        >>> outputs = model(**inputs)
        ```'''
