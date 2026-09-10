from ...configuration_utils import PretrainedConfig as PretrainedConfig
from ...utils import logging as logging
from ..auto.configuration_auto import CONFIG_MAPPING as CONFIG_MAPPING
from ..bit import BitConfig as BitConfig
from _typeshed import Incomplete
from typing import Dict

logger: Incomplete
VIT_HYBRID_PRETRAINED_CONFIG_ARCHIVE_MAP: Incomplete

class ViTHybridConfig(PretrainedConfig):
    '''
    This is the configuration class to store the configuration of a [`ViTHybridModel`]. It is used to instantiate a ViT
    Hybrid model according to the specified arguments, defining the model architecture. Instantiating a configuration
    with the defaults will yield a similar configuration to that of the ViT Hybrid
    [google/vit-hybrid-base-bit-384](https://huggingface.co/google/vit-hybrid-base-bit-384) architecture.

    Configuration objects inherit from [`PretrainedConfig`] and can be used to control the model outputs. Read the
    documentation from [`PretrainedConfig`] for more information.

    Args:
        hidden_size (`int`, *optional*, defaults to 768):
            Dimensionality of the encoder layers and the pooler layer.
        num_hidden_layers (`int`, *optional*, defaults to 12):
            Number of hidden layers in the Transformer encoder.
        num_attention_heads (`int`, *optional*, defaults to 12):
            Number of attention heads for each attention layer in the Transformer encoder.
        intermediate_size (`int`, *optional*, defaults to 3072):
            Dimensionality of the "intermediate" (i.e., feed-forward) layer in the Transformer encoder.
        hidden_act (`str` or `function`, *optional*, defaults to `"gelu"`):
            The non-linear activation function (function or string) in the encoder and pooler. If string, `"gelu"`,
            `"relu"`, `"selu"` and `"gelu_new"` are supported.
        hidden_dropout_prob (`float`, *optional*, defaults to 0.1):
            The dropout probability for all fully connected layers in the embeddings, encoder, and pooler.
        attention_probs_dropout_prob (`float`, *optional*, defaults to 0.1):
            The dropout ratio for the attention probabilities.
        initializer_range (`float`, *optional*, defaults to 0.02):
            The standard deviation of the truncated_normal_initializer for initializing all weight matrices.
        layer_norm_eps (`float`, *optional*, defaults to 1e-12):
            The epsilon used by the layer normalization layers.
        image_size (`int`, *optional*, defaults to 224):
            The size (resolution) of each image.
        patch_size (`int`, *optional*, defaults to 1):
            The size (resolution) of each patch.
        num_channels (`int`, *optional*, defaults to 3):
            The number of input channels.
        qkv_bias (`bool`, *optional*, defaults to `True`):
            Whether to add a bias to the queries, keys and values.
        backbone_config (`Union[Dict[str, Any], PretrainedConfig]`, *optional*, defaults to `None`):
            The configuration of the backbone in a dictionary or the config object of the backbone.
        backbone_featmap_shape (`List[int]`, *optional*, defaults to `[1, 1024, 24, 24]`):
            Used only for the `hybrid` embedding type. The shape of the feature maps of the backbone.

    Example:

    ```python
    >>> from transformers import ViTHybridConfig, ViTHybridModel

    >>> # Initializing a ViT Hybrid vit-hybrid-base-bit-384 style configuration
    >>> configuration = ViTHybridConfig()

    >>> # Initializing a model (with random weights) from the vit-hybrid-base-bit-384 style configuration
    >>> model = ViTHybridModel(configuration)

    >>> # Accessing the model configuration
    >>> configuration = model.config
    ```'''
    model_type: str
    backbone_featmap_shape: Incomplete
    backbone_config: Incomplete
    hidden_size: Incomplete
    num_hidden_layers: Incomplete
    num_attention_heads: Incomplete
    intermediate_size: Incomplete
    hidden_act: Incomplete
    hidden_dropout_prob: Incomplete
    attention_probs_dropout_prob: Incomplete
    initializer_range: Incomplete
    layer_norm_eps: Incomplete
    image_size: Incomplete
    patch_size: Incomplete
    num_channels: Incomplete
    qkv_bias: Incomplete
    def __init__(self, backbone_config: Incomplete | None = None, hidden_size: int = 768, num_hidden_layers: int = 12, num_attention_heads: int = 12, intermediate_size: int = 3072, hidden_act: str = 'gelu', hidden_dropout_prob: float = 0.0, attention_probs_dropout_prob: float = 0.0, initializer_range: float = 0.02, layer_norm_eps: float = 1e-12, image_size: int = 224, patch_size: int = 1, num_channels: int = 3, backbone_featmap_shape=[1, 1024, 24, 24], qkv_bias: bool = True, **kwargs) -> None: ...
    def to_dict(self) -> Dict[str, any]:
        """
        Serializes this instance to a Python dictionary. Override the default [`~PretrainedConfig.to_dict`]. Returns:
            `Dict[str, any]`: Dictionary of all the attributes that make up this configuration instance,
        """
