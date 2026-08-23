from ...configuration_utils import PretrainedConfig as PretrainedConfig
from ...utils import logging as logging
from ..auto import CONFIG_MAPPING as CONFIG_MAPPING
from ..detr import DetrConfig as DetrConfig
from ..swin import SwinConfig as SwinConfig
from _typeshed import Incomplete
from typing import Dict, Optional

MASKFORMER_PRETRAINED_CONFIG_ARCHIVE_MAP: Incomplete
logger: Incomplete

class MaskFormerConfig(PretrainedConfig):
    '''
    This is the configuration class to store the configuration of a [`MaskFormerModel`]. It is used to instantiate a
    MaskFormer model according to the specified arguments, defining the model architecture. Instantiating a
    configuration with the defaults will yield a similar configuration to that of the MaskFormer
    [facebook/maskformer-swin-base-ade](https://huggingface.co/facebook/maskformer-swin-base-ade) architecture trained
    on [ADE20k-150](https://huggingface.co/datasets/scene_parse_150).

    Configuration objects inherit from [`PretrainedConfig`] and can be used to control the model outputs. Read the
    documentation from [`PretrainedConfig`] for more information.

    Currently, MaskFormer only supports the [Swin Transformer](swin) as backbone.

    Args:
        mask_feature_size (`int`, *optional*, defaults to 256):
            The masks\' features size, this value will also be used to specify the Feature Pyramid Network features\'
            size.
        no_object_weight (`float`, *optional*, defaults to 0.1):
            Weight to apply to the null (no object) class.
        use_auxiliary_loss(`bool`, *optional*, defaults to `False`):
            If `True` [`MaskFormerForInstanceSegmentationOutput`] will contain the auxiliary losses computed using the
            logits from each decoder\'s stage.
        backbone_config (`Dict`, *optional*):
            The configuration passed to the backbone, if unset, the configuration corresponding to
            `swin-base-patch4-window12-384` will be used.
        decoder_config (`Dict`, *optional*):
            The configuration passed to the transformer decoder model, if unset the base config for `detr-resnet-50`
            will be used.
        init_std (`float`, *optional*, defaults to 0.02):
            The standard deviation of the truncated_normal_initializer for initializing all weight matrices.
        init_xavier_std (`float`, *optional*, defaults to 1):
            The scaling factor used for the Xavier initialization gain in the HM Attention map module.
        dice_weight (`float`, *optional*, defaults to 1.0):
            The weight for the dice loss.
        cross_entropy_weight (`float`, *optional*, defaults to 1.0):
            The weight for the cross entropy loss.
        mask_weight (`float`, *optional*, defaults to 20.0):
            The weight for the mask loss.
        output_auxiliary_logits (`bool`, *optional*):
            Should the model output its `auxiliary_logits` or not.

    Raises:
        `ValueError`:
            Raised if the backbone model type selected is not in `["swin"]` or the decoder model type selected is not
            in `["detr"]`

    Examples:

    ```python
    >>> from transformers import MaskFormerConfig, MaskFormerModel

    >>> # Initializing a MaskFormer facebook/maskformer-swin-base-ade configuration
    >>> configuration = MaskFormerConfig()

    >>> # Initializing a model (with random weights) from the facebook/maskformer-swin-base-ade style configuration
    >>> model = MaskFormerModel(configuration)

    >>> # Accessing the model configuration
    >>> configuration = model.config
    ```

    '''
    model_type: str
    attribute_map: Incomplete
    backbones_supported: Incomplete
    decoders_supported: Incomplete
    backbone_config: Incomplete
    decoder_config: Incomplete
    fpn_feature_size: Incomplete
    mask_feature_size: Incomplete
    init_std: Incomplete
    init_xavier_std: Incomplete
    cross_entropy_weight: Incomplete
    dice_weight: Incomplete
    mask_weight: Incomplete
    use_auxiliary_loss: Incomplete
    no_object_weight: Incomplete
    output_auxiliary_logits: Incomplete
    num_attention_heads: Incomplete
    num_hidden_layers: Incomplete
    def __init__(self, fpn_feature_size: int = 256, mask_feature_size: int = 256, no_object_weight: float = 0.1, use_auxiliary_loss: bool = False, backbone_config: Optional[Dict] = None, decoder_config: Optional[Dict] = None, init_std: float = 0.02, init_xavier_std: float = 1.0, dice_weight: float = 1.0, cross_entropy_weight: float = 1.0, mask_weight: float = 20.0, output_auxiliary_logits: Optional[bool] = None, **kwargs) -> None: ...
    @classmethod
    def from_backbone_and_decoder_configs(cls, backbone_config: PretrainedConfig, decoder_config: PretrainedConfig, **kwargs):
        """Instantiate a [`MaskFormerConfig`] (or a derived class) from a pre-trained backbone model configuration and DETR model
        configuration.

            Args:
                backbone_config ([`PretrainedConfig`]):
                    The backbone configuration.
                decoder_config ([`PretrainedConfig`]):
                    The transformer decoder configuration to use.

            Returns:
                [`MaskFormerConfig`]: An instance of a configuration object
        """
    def to_dict(self) -> Dict[str, any]:
        """
        Serializes this instance to a Python dictionary. Override the default [`~PretrainedConfig.to_dict`].

        Returns:
            `Dict[str, any]`: Dictionary of all the attributes that make up this configuration instance,
        """
