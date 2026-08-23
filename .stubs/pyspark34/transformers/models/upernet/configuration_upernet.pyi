from ...configuration_utils import PretrainedConfig as PretrainedConfig
from ...utils import logging as logging
from ..auto.configuration_auto import CONFIG_MAPPING as CONFIG_MAPPING
from _typeshed import Incomplete

logger: Incomplete

class UperNetConfig(PretrainedConfig):
    """
    This is the configuration class to store the configuration of an [`UperNetForSemanticSegmentation`]. It is used to
    instantiate an UperNet model according to the specified arguments, defining the model architecture. Instantiating a
    configuration with the defaults will yield a similar configuration to that of the UperNet
    [openmmlab/upernet-convnext-tiny](https://huggingface.co/openmmlab/upernet-convnext-tiny) architecture.

    Configuration objects inherit from [`PretrainedConfig`] and can be used to control the model outputs. Read the
    documentation from [`PretrainedConfig`] for more information.

    Args:
        backbone_config (`PretrainedConfig` or `dict`, *optional*, defaults to `ResNetConfig()`):
            The configuration of the backbone model.
        hidden_size (`int`, *optional*, defaults to 512):
            The number of hidden units in the convolutional layers.
        initializer_range (`float`, *optional*, defaults to 0.02):
            The standard deviation of the truncated_normal_initializer for initializing all weight matrices.
        pool_scales (`Tuple[int]`, *optional*, defaults to `[1, 2, 3, 6]`):
            Pooling scales used in Pooling Pyramid Module applied on the last feature map.
        use_auxiliary_head (`bool`, *optional*, defaults to `True`):
            Whether to use an auxiliary head during training.
        auxiliary_loss_weight (`float`, *optional*, defaults to 0.4):
            Weight of the cross-entropy loss of the auxiliary head.
        auxiliary_channels (`int`, *optional*, defaults to 256):
            Number of channels to use in the auxiliary head.
        auxiliary_num_convs (`int`, *optional*, defaults to 1):
            Number of convolutional layers to use in the auxiliary head.
        auxiliary_concat_input (`bool`, *optional*, defaults to `False`):
            Whether to concatenate the output of the auxiliary head with the input before the classification layer.
        loss_ignore_index (`int`, *optional*, defaults to 255):
            The index that is ignored by the loss function.

    Examples:

    ```python
    >>> from transformers import UperNetConfig, UperNetForSemanticSegmentation

    >>> # Initializing a configuration
    >>> configuration = UperNetConfig()

    >>> # Initializing a model (with random weights) from the configuration
    >>> model = UperNetForSemanticSegmentation(configuration)

    >>> # Accessing the model configuration
    >>> configuration = model.config
    ```"""
    model_type: str
    backbone_config: Incomplete
    hidden_size: Incomplete
    initializer_range: Incomplete
    pool_scales: Incomplete
    use_auxiliary_head: Incomplete
    auxiliary_loss_weight: Incomplete
    auxiliary_in_channels: Incomplete
    auxiliary_channels: Incomplete
    auxiliary_num_convs: Incomplete
    auxiliary_concat_input: Incomplete
    loss_ignore_index: Incomplete
    def __init__(self, backbone_config: Incomplete | None = None, hidden_size: int = 512, initializer_range: float = 0.02, pool_scales=[1, 2, 3, 6], use_auxiliary_head: bool = True, auxiliary_loss_weight: float = 0.4, auxiliary_in_channels: int = 384, auxiliary_channels: int = 256, auxiliary_num_convs: int = 1, auxiliary_concat_input: bool = False, loss_ignore_index: int = 255, **kwargs) -> None: ...
    def to_dict(self):
        """
        Serializes this instance to a Python dictionary. Override the default [`~PretrainedConfig.to_dict`]. Returns:
            `Dict[str, any]`: Dictionary of all the attributes that make up this configuration instance,
        """
