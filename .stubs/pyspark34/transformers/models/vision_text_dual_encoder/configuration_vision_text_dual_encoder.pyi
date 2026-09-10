from ...configuration_utils import PretrainedConfig as PretrainedConfig
from ...utils import logging as logging
from ..auto.configuration_auto import AutoConfig as AutoConfig
from ..clip.configuration_clip import CLIPVisionConfig as CLIPVisionConfig
from _typeshed import Incomplete

logger: Incomplete

class VisionTextDualEncoderConfig(PretrainedConfig):
    '''
    [`VisionTextDualEncoderConfig`] is the configuration class to store the configuration of a
    [`VisionTextDualEncoderModel`]. It is used to instantiate [`VisionTextDualEncoderModel`] model according to the
    specified arguments, defining the text model and vision model configs.

    Configuration objects inherit from [`PretrainedConfig`] and can be used to control the model outputs. Read the
    documentation from [`PretrainedConfig`] for more information.

    Args:
        text_config (`dict`):
            Dictionary of configuration options that defines text model config.
        vision_config (`dict`):
            Dictionary of configuration options that defines vison model config.
        projection_dim (`int`, *optional*, defaults to 512):
            Dimentionality of text and vision projection layers.
        logit_scale_init_value (`float`, *optional*, defaults to 2.6592):
            The inital value of the *logit_scale* paramter. Default is used as per the original CLIP implementation.
        kwargs (*optional*):
            Dictionary of keyword arguments.

    Examples:

    ```python
    >>> from transformers import ViTConfig, BertConfig, VisionTextDualEncoderConfig, VisionTextDualEncoderModel

    >>> # Initializing a BERT and ViT configuration
    >>> config_vision = ViTConfig()
    >>> config_text = BertConfig()

    >>> config = VisionTextDualEncoderConfig.from_vision_text_configs(config_vision, config_text, projection_dim=512)

    >>> # Initializing a BERT and ViT model (with random weights)
    >>> model = VisionTextDualEncoderModel(config=config)

    >>> # Accessing the model configuration
    >>> config_vision = model.config.vision_config
    >>> config_text = model.config.text_config

    >>> # Saving the model, including its configuration
    >>> model.save_pretrained("vit-bert")

    >>> # loading model and config from pretrained folder
    >>> vision_text_config = VisionTextDualEncoderConfig.from_pretrained("vit-bert")
    >>> model = VisionTextDualEncoderModel.from_pretrained("vit-bert", config=vision_text_config)
    ```'''
    model_type: str
    is_composition: bool
    vision_config: Incomplete
    text_config: Incomplete
    projection_dim: Incomplete
    logit_scale_init_value: Incomplete
    def __init__(self, projection_dim: int = 512, logit_scale_init_value: float = 2.6592, **kwargs) -> None: ...
    @classmethod
    def from_vision_text_configs(cls, vision_config: PretrainedConfig, text_config: PretrainedConfig, **kwargs):
        """
        Instantiate a [`VisionTextDualEncoderConfig`] (or a derived class) from text model configuration and vision
        model configuration.

        Returns:
            [`VisionTextDualEncoderConfig`]: An instance of a configuration object
        """
    def to_dict(self):
        """
        Serializes this instance to a Python dictionary. Override the default [`~PretrainedConfig.to_dict`].

        Returns:
            `Dict[str, any]`: Dictionary of all the attributes that make up this configuration instance,
        """
