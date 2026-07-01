from ...configuration_utils import PretrainedConfig as PretrainedConfig
from ...utils import logging as logging
from ..auto import CONFIG_MAPPING as CONFIG_MAPPING
from _typeshed import Incomplete
from typing import Dict, List, Optional

MASK2FORMER_PRETRAINED_CONFIG_ARCHIVE_MAP: Incomplete
logger: Incomplete

class Mask2FormerConfig(PretrainedConfig):
    """
    This is the configuration class to store the configuration of a [`Mask2FormerModel`]. It is used to instantiate a
    Mask2Former model according to the specified arguments, defining the model architecture. Instantiating a
    configuration with the defaults will yield a similar configuration to that of the Mask2Former
    [facebook/mask2former-swin-small-coco-instance](https://huggingface.co/facebook/mask2former-swin-small-coco-instance)
    architecture.

    Configuration objects inherit from [`PretrainedConfig`] and can be used to control the model outputs. Read the
    documentation from [`PretrainedConfig`] for more information.

    Currently, Mask2Former only supports the [Swin Transformer](swin) as backbone.

    Args:
        backbone_config (`PretrainedConfig` or `dict`, *optional*, defaults to `SwinConfig()`):
            The configuration of the backbone model. If unset, the configuration corresponding to
            `swin-base-patch4-window12-384` will be used.
        feature_size (`int`, *optional*, defaults to 256):
            The features (channels) of the resulting feature maps.
        mask_feature_size (`int`, *optional*, defaults to 256):
            The masks' features size, this value will also be used to specify the Feature Pyramid Network features'
            size.
        hidden_dim (`int`, *optional*, defaults to 256):
            Dimensionality of the encoder layers.
        encoder_feedforward_dim (`int`, *optional*, defaults to 1024):
            Dimension of feedforward network for deformable detr encoder used as part of pixel decoder.
        encoder_layers (`int`, *optional*, defaults to 6):
            Number of layers in the deformable detr encoder used as part of pixel decoder.
        decoder_layers (`int`, *optional*, defaults to 10):
            Number of layers in the Transformer decoder.
        num_attention_heads (`int`, *optional*, defaults to 8):
            Number of attention heads for each attention layer.
        dropout (`float`, *optional*, defaults to 0.1):
            The dropout probability for all fully connected layers in the embeddings, encoder.
        dim_feedforward (`int`, *optional*, defaults to 2048):
            Feature dimension in feedforward network for transformer decoder.
        pre_norm (`bool`, *optional*, defaults to `False`):
            Whether to use pre-LayerNorm or not for transformer decoder.
        enforce_input_projection (`bool`, *optional*, defaults to `False`):
            Whether to add an input projection 1x1 convolution even if the input channels and hidden dim are identical
            in the Transformer decoder.
        common_stride (`int`, *optional*, defaults to 4):
            Parameter used for determining number of FPN levels used as part of pixel decoder.
        ignore_value (`int`, *optional*, defaults to 255):
            Category id to be ignored during training.
        num_queries (`int`, *optional*, defaults to 100):
            Number of queries for the decoder.
        no_object_weight (`int`, *optional*, defaults to 0.1):
            The weight to apply to the null (no object) class.
        class_weight (`int`, *optional*, defaults to 2.0):
            The weight for the cross entropy loss.
        mask_weight (`int`, *optional*, defaults to 5.0):
            The weight for the mask loss.
        dice_weight (`int`, *optional*, defaults to 5.0):
            The weight for the dice loss.
        train_num_points (`str` or `function`, *optional*, defaults to 12544):
            Number of points used for sampling during loss calculation.
        oversample_ratio (`float`, *optional*, defaults to 3.0):
            Oversampling parameter used for calculating no. of sampled points
        importance_sample_ratio (`float`, *optional*, defaults to 0.75):
            Ratio of points that are sampled via importance sampling.
        init_std (`float`, *optional*, defaults to 0.02):
            The standard deviation of the truncated_normal_initializer for initializing all weight matrices.
        init_xavier_std (`float``, *optional*, defaults to 1.0):
            The scaling factor used for the Xavier initialization gain in the HM Attention map module.
        use_auxiliary_loss (`boolean``, *optional*, defaults to `True`):
            If `True` [`Mask2FormerForUniversalSegmentationOutput`] will contain the auxiliary losses computed using
            the logits from each decoder's stage.
        feature_strides (`List[int]`, *optional*, defaults to `[4, 8, 16, 32]`):
            Feature strides corresponding to features generated from backbone network.
        output_auxiliary_logits (`bool`, *optional*):
            Should the model output its `auxiliary_logits` or not.

    Examples:

    ```python
    >>> from transformers import Mask2FormerConfig, Mask2FormerModel

    >>> # Initializing a Mask2Former facebook/mask2former-swin-small-coco-instance configuration
    >>> configuration = Mask2FormerConfig()

    >>> # Initializing a model (with random weights) from the facebook/mask2former-swin-small-coco-instance style configuration
    >>> model = Mask2FormerModel(configuration)

    >>> # Accessing the model configuration
    >>> configuration = model.config
    ```

    """
    model_type: str
    backbones_supported: Incomplete
    attribute_map: Incomplete
    backbone_config: Incomplete
    feature_size: Incomplete
    mask_feature_size: Incomplete
    hidden_dim: Incomplete
    encoder_feedforward_dim: Incomplete
    activation_function: Incomplete
    encoder_layers: Incomplete
    decoder_layers: Incomplete
    num_attention_heads: Incomplete
    dropout: Incomplete
    dim_feedforward: Incomplete
    pre_norm: Incomplete
    enforce_input_projection: Incomplete
    common_stride: Incomplete
    ignore_value: Incomplete
    num_queries: Incomplete
    no_object_weight: Incomplete
    class_weight: Incomplete
    mask_weight: Incomplete
    dice_weight: Incomplete
    train_num_points: Incomplete
    oversample_ratio: Incomplete
    importance_sample_ratio: Incomplete
    init_std: Incomplete
    init_xavier_std: Incomplete
    use_auxiliary_loss: Incomplete
    feature_strides: Incomplete
    output_auxiliary_logits: Incomplete
    num_hidden_layers: Incomplete
    def __init__(self, backbone_config: Optional[Dict] = None, feature_size: int = 256, mask_feature_size: int = 256, hidden_dim: int = 256, encoder_feedforward_dim: int = 1024, activation_function: str = 'relu', encoder_layers: int = 6, decoder_layers: int = 10, num_attention_heads: int = 8, dropout: float = 0.0, dim_feedforward: int = 2048, pre_norm: bool = False, enforce_input_projection: bool = False, common_stride: int = 4, ignore_value: int = 255, num_queries: int = 100, no_object_weight: float = 0.1, class_weight: float = 2.0, mask_weight: float = 5.0, dice_weight: float = 5.0, train_num_points: int = 12544, oversample_ratio: float = 3.0, importance_sample_ratio: float = 0.75, init_std: float = 0.02, init_xavier_std: float = 1.0, use_auxiliary_loss: bool = True, feature_strides: List[int] = [4, 8, 16, 32], output_auxiliary_logits: bool = None, **kwargs) -> None: ...
    @classmethod
    def from_backbone_config(cls, backbone_config: PretrainedConfig, **kwargs):
        """Instantiate a [`Mask2FormerConfig`] (or a derived class) from a pre-trained backbone model configuration.

        Args:
            backbone_config ([`PretrainedConfig`]):
                The backbone configuration.

        Returns:
            [`Mask2FormerConfig`]: An instance of a configuration object
        """
    def to_dict(self) -> Dict[str, any]:
        """
        Serializes this instance to a Python dictionary. Override the default [`~PretrainedConfig.to_dict`].

        Returns:
            `Dict[str, any]`: Dictionary of all the attributes that make up this configuration instance,
        """
