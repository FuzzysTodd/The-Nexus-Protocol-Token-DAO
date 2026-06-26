from ...configuration_utils import PretrainedConfig as PretrainedConfig
from ...onnx import OnnxConfig as OnnxConfig
from ...utils import logging as logging
from _typeshed import Incomplete
from typing import Mapping

logger: Incomplete
MOBILEVIT_PRETRAINED_CONFIG_ARCHIVE_MAP: Incomplete

class MobileViTConfig(PretrainedConfig):
    '''
    This is the configuration class to store the configuration of a [`MobileViTModel`]. It is used to instantiate a
    MobileViT model according to the specified arguments, defining the model architecture. Instantiating a
    configuration with the defaults will yield a similar configuration to that of the MobileViT
    [apple/mobilevit-small](https://huggingface.co/apple/mobilevit-small) architecture.

    Configuration objects inherit from [`PretrainedConfig`] and can be used to control the model outputs. Read the
    documentation from [`PretrainedConfig`] for more information.

    Args:
        num_channels (`int`, *optional*, defaults to 3):
            The number of input channels.
        image_size (`int`, *optional*, defaults to 256):
            The size (resolution) of each image.
        patch_size (`int`, *optional*, defaults to 2):
            The size (resolution) of each patch.
        hidden_sizes (`List[int]`, *optional*, defaults to `[144, 192, 240]`):
            Dimensionality (hidden size) of the Transformer encoders at each stage.
        neck_hidden_sizes (`List[int]`, *optional*, defaults to `[16, 32, 64, 96, 128, 160, 640]`):
            The number of channels for the feature maps of the backbone.
        num_attention_heads (`int`, *optional*, defaults to 4):
            Number of attention heads for each attention layer in the Transformer encoder.
        mlp_ratio (`float`, *optional*, defaults to 2.0):
            The ratio of the number of channels in the output of the MLP to the number of channels in the input.
        expand_ratio (`float`, *optional*, defaults to 4.0):
            Expansion factor for the MobileNetv2 layers.
        hidden_act (`str` or `function`, *optional*, defaults to `"silu"`):
            The non-linear activation function (function or string) in the Transformer encoder and convolution layers.
        conv_kernel_size (`int`, *optional*, defaults to 3):
            The size of the convolutional kernel in the MobileViT layer.
        output_stride (`int`, `optional`, defaults to 32):
            The ratio of the spatial resolution of the output to the resolution of the input image.
        hidden_dropout_prob (`float`, *optional*, defaults to 0.1):
            The dropout probabilitiy for all fully connected layers in the Transformer encoder.
        attention_probs_dropout_prob (`float`, *optional*, defaults to 0.0):
            The dropout ratio for the attention probabilities.
        classifier_dropout_prob (`float`, *optional*, defaults to 0.1):
            The dropout ratio for attached classifiers.
        initializer_range (`float`, *optional*, defaults to 0.02):
            The standard deviation of the truncated_normal_initializer for initializing all weight matrices.
        layer_norm_eps (`float`, *optional*, defaults to 1e-5):
            The epsilon used by the layer normalization layers.
        qkv_bias (`bool`, *optional*, defaults to `True`):
            Whether to add a bias to the queries, keys and values.
        aspp_out_channels (`int`, `optional`, defaults to 256):
            Number of output channels used in the ASPP layer for semantic segmentation.
        atrous_rates (`List[int]`, *optional*, defaults to `[6, 12, 18]`):
            Dilation (atrous) factors used in the ASPP layer for semantic segmentation.
        aspp_dropout_prob (`float`, *optional*, defaults to 0.1):
            The dropout ratio for the ASPP layer for semantic segmentation.
        semantic_loss_ignore_index (`int`, *optional*, defaults to 255):
            The index that is ignored by the loss function of the semantic segmentation model.

    Example:

    ```python
    >>> from transformers import MobileViTConfig, MobileViTModel

    >>> # Initializing a mobilevit-small style configuration
    >>> configuration = MobileViTConfig()

    >>> # Initializing a model from the mobilevit-small style configuration
    >>> model = MobileViTModel(configuration)

    >>> # Accessing the model configuration
    >>> configuration = model.config
    ```'''
    model_type: str
    num_channels: Incomplete
    image_size: Incomplete
    patch_size: Incomplete
    hidden_sizes: Incomplete
    neck_hidden_sizes: Incomplete
    num_attention_heads: Incomplete
    mlp_ratio: Incomplete
    expand_ratio: Incomplete
    hidden_act: Incomplete
    conv_kernel_size: Incomplete
    output_stride: Incomplete
    hidden_dropout_prob: Incomplete
    attention_probs_dropout_prob: Incomplete
    classifier_dropout_prob: Incomplete
    initializer_range: Incomplete
    layer_norm_eps: Incomplete
    qkv_bias: Incomplete
    aspp_out_channels: Incomplete
    atrous_rates: Incomplete
    aspp_dropout_prob: Incomplete
    semantic_loss_ignore_index: Incomplete
    def __init__(self, num_channels: int = 3, image_size: int = 256, patch_size: int = 2, hidden_sizes=[144, 192, 240], neck_hidden_sizes=[16, 32, 64, 96, 128, 160, 640], num_attention_heads: int = 4, mlp_ratio: float = 2.0, expand_ratio: float = 4.0, hidden_act: str = 'silu', conv_kernel_size: int = 3, output_stride: int = 32, hidden_dropout_prob: float = 0.1, attention_probs_dropout_prob: float = 0.0, classifier_dropout_prob: float = 0.1, initializer_range: float = 0.02, layer_norm_eps: float = 1e-05, qkv_bias: bool = True, aspp_out_channels: int = 256, atrous_rates=[6, 12, 18], aspp_dropout_prob: float = 0.1, semantic_loss_ignore_index: int = 255, **kwargs) -> None: ...

class MobileViTOnnxConfig(OnnxConfig):
    torch_onnx_minimum_version: Incomplete
    @property
    def inputs(self) -> Mapping[str, Mapping[int, str]]: ...
    @property
    def outputs(self) -> Mapping[str, Mapping[int, str]]: ...
    @property
    def atol_for_validation(self) -> float: ...
