import os
from ...configuration_utils import PretrainedConfig as PretrainedConfig
from ...utils import logging as logging
from _typeshed import Incomplete
from typing import Union

logger: Incomplete
BLIP_PRETRAINED_CONFIG_ARCHIVE_MAP: Incomplete

class BlipTextConfig(PretrainedConfig):
    '''
    This is the configuration class to store the configuration of a [`BlipTextModel`]. It is used to instantiate a BLIP
    text model according to the specified arguments, defining the model architecture. Instantiating a configuration
    with the defaults will yield a similar configuration to that of the `BlipText` used by the [base
    architectures](https://huggingface.co/Salesforce/blip-vqa-base).

    Configuration objects inherit from [`PretrainedConfig`] and can be used to control the model outputs. Read the
    documentation from [`PretrainedConfig`] for more information.


    Args:
        vocab_size (`int`, *optional*, defaults to 30522):
            Vocabulary size of the `Blip` text model. Defines the number of different tokens that can be represented by
            the `inputs_ids` passed when calling [`BlipModel`].
        hidden_size (`int`, *optional*, defaults to 768):
            Dimensionality of the encoder layers and the pooler layer.
        encoder_hidden_size (`int`, *optional*, defaults to 768):
            Dimensionality of the encoder layers from the vision model.
        intermediate_size (`int`, *optional*, defaults to 3072):
            Dimensionality of the "intermediate" (i.e., feed-forward) layer in the Transformer encoder.
        num_hidden_layers (`int`, *optional*, defaults to 12):
            Number of hidden layers in the Transformer encoder.
        num_attention_heads (`int`, *optional*, defaults to 8):
            Number of attention heads for each attention layer in the Transformer encoder.
        max_position_embeddings (`int`, *optional*, defaults to 77):
            The maximum sequence length that this model might ever be used with. Typically set this to something large
            just in case (e.g., 512 or 1024 or 2048).
        hidden_act (`str` or `function`, *optional*, defaults to `"gelu"`):
            The non-linear activation function (function or string) in the encoder and pooler. If string, `"gelu"`,
            `"relu"`, `"selu"` and `"gelu_new"` ``"gelu"` are supported. layer_norm_eps (`float`, *optional*, defaults
            to 1e-5): The epsilon used by the layer normalization layers.
        attention_dropout (`float`, *optional*, defaults to 0.0):
            The dropout ratio for the attention probabilities.
        dropout (`float`, *optional*, defaults to 0.0):
            The dropout probabilitiy for all fully connected layers in the embeddings, encoder, and pooler.
        initializer_range (`float`, *optional*, defaults to 0.02):
            The standard deviation of the truncated_normal_initializer for initializing all weight matrices.
        initializer_factor (`float``, *optional*, defaults to 1):
            A factor for initializing all weight matrices (should be kept to 1, used internally for initialization
            testing).
        bos_token_id (`int`, *optional*, defaults to 30522):
            The id of the `beginning-of-sequence` token.
        eos_token_id (`int`, *optional*, defaults to 2):
            The id of the `end-of-sequence` token.
        pad_token_id (`int`, *optional*, defaults to 0):
            The id of the `padding` token.
        sep_token_id (`int`, *optional*, defaults to 102):
            The id of the `separator` token.
        is_decoder (`bool`, *optional*, defaults to `False`):
            Whether the model is used as a decoder.
        use_cache (`bool`, *optional*, defaults to `True`):
            Whether or not the model should return the last key/values attentions (not used by all models).

    Example:

    ```python
    >>> from transformers import BlipTextConfig, BlipTextModel

    >>> # Initializing a BlipTextConfig with Salesforce/blip-vqa-base style configuration
    >>> configuration = BlipTextConfig()

    >>> # Initializing a BlipTextModel (with random weights) from the Salesforce/blip-vqa-base style configuration
    >>> model = BlipTextModel(configuration)

    >>> # Accessing the model configuration
    >>> configuration = model.config
    ```'''
    model_type: str
    vocab_size: Incomplete
    hidden_size: Incomplete
    encoder_hidden_size: Incomplete
    intermediate_size: Incomplete
    projection_dim: Incomplete
    hidden_dropout_prob: Incomplete
    num_hidden_layers: Incomplete
    num_attention_heads: Incomplete
    max_position_embeddings: Incomplete
    layer_norm_eps: Incomplete
    hidden_act: Incomplete
    initializer_range: Incomplete
    initializer_factor: Incomplete
    attention_probs_dropout_prob: Incomplete
    is_decoder: Incomplete
    use_cache: Incomplete
    def __init__(self, vocab_size: int = 30524, hidden_size: int = 768, encoder_hidden_size: int = 768, intermediate_size: int = 3072, projection_dim: int = 768, num_hidden_layers: int = 12, num_attention_heads: int = 8, max_position_embeddings: int = 512, hidden_act: str = 'gelu', layer_norm_eps: float = 1e-12, hidden_dropout_prob: float = 0.0, attention_probs_dropout_prob: float = 0.0, initializer_range: float = 0.02, initializer_factor: float = 1.0, bos_token_id: int = 30522, eos_token_id: int = 2, pad_token_id: int = 0, sep_token_id: int = 102, is_decoder: bool = True, use_cache: bool = True, **kwargs) -> None: ...
    @classmethod
    def from_pretrained(cls, pretrained_model_name_or_path: Union[str, os.PathLike], **kwargs) -> PretrainedConfig: ...

class BlipVisionConfig(PretrainedConfig):
    '''
    This is the configuration class to store the configuration of a [`BlipVisionModel`]. It is used to instantiate a
    BLIP vision model according to the specified arguments, defining the model architecture. Instantiating a
    configuration defaults will yield a similar configuration to that of the Blip-base
    [Salesforce/blip-vqa-base](https://huggingface.co/Salesforce/blip-vqa-base) architecture.

    Configuration objects inherit from [`PretrainedConfig`] and can be used to control the model outputs. Read the
    documentation from [`PretrainedConfig`] for more information.


    Args:
        hidden_size (`int`, *optional*, defaults to 768):
            Dimensionality of the encoder layers and the pooler layer.
        intermediate_size (`int`, *optional*, defaults to 3072):
            Dimensionality of the "intermediate" (i.e., feed-forward) layer in the Transformer encoder.
        num_hidden_layers (`int`, *optional*, defaults to 12):
            Number of hidden layers in the Transformer encoder.
        num_attention_heads (`int`, *optional*, defaults to 12):
            Number of attention heads for each attention layer in the Transformer encoder.
        image_size (`int`, *optional*, defaults to 224):
            The size (resolution) of each image.
        patch_size (`int`, *optional*, defaults to 32):
            The size (resolution) of each patch.
        hidden_act (`str` or `function`, *optional*, defaults to `"gelu"`):
            The non-linear activation function (function or string) in the encoder and pooler. If string, `"gelu"`,
            `"relu"`, `"selu"` and `"gelu_new"` ``"gelu"` are supported. layer_norm_eps (`float`, *optional*, defaults
            to 1e-5): The epsilon used by the layer normalization layers.
        dropout (`float`, *optional*, defaults to 0.0):
            The dropout probabilitiy for all fully connected layers in the embeddings, encoder, and pooler.
        attention_dropout (`float`, *optional*, defaults to 0.0):
            The dropout ratio for the attention probabilities.
        initializer_range (`float`, *optional*, defaults to 0.02):
            The standard deviation of the truncated_normal_initializer for initializing all weight matrices.
        initializer_factor (`float``, *optional*, defaults to 1):
            A factor for initializing all weight matrices (should be kept to 1, used internally for initialization
            testing).

    Example:

    ```python
    >>> from transformers import BlipVisionConfig, BlipVisionModel

    >>> # Initializing a BlipVisionConfig with Salesforce/blip-vqa-base style configuration
    >>> configuration = BlipVisionConfig()

    >>> # Initializing a BlipVisionModel (with random weights) from the Salesforce/blip-vqa-base style configuration
    >>> model = BlipVisionModel(configuration)

    >>> # Accessing the model configuration
    >>> configuration = model.config
    ```'''
    model_type: str
    hidden_size: Incomplete
    intermediate_size: Incomplete
    projection_dim: Incomplete
    dropout: Incomplete
    num_hidden_layers: Incomplete
    num_attention_heads: Incomplete
    num_channels: Incomplete
    patch_size: Incomplete
    image_size: Incomplete
    initializer_range: Incomplete
    initializer_factor: Incomplete
    attention_dropout: Incomplete
    layer_norm_eps: Incomplete
    hidden_act: Incomplete
    def __init__(self, hidden_size: int = 768, intermediate_size: int = 3072, projection_dim: int = 512, num_hidden_layers: int = 12, num_attention_heads: int = 12, num_channels: int = 3, image_size: int = 384, patch_size: int = 16, hidden_act: str = 'gelu', layer_norm_eps: float = 1e-05, dropout: float = 0.0, attention_dropout: float = 0.0, initializer_range: float = 1e-10, initializer_factor: float = 1.0, **kwargs) -> None: ...
    @classmethod
    def from_pretrained(cls, pretrained_model_name_or_path: Union[str, os.PathLike], **kwargs) -> PretrainedConfig: ...

class BlipConfig(PretrainedConfig):
    """
    [`BlipConfig`] is the configuration class to store the configuration of a [`BlipModel`]. It is used to instantiate
    a BLIP model according to the specified arguments, defining the text model and vision model configs. Instantiating
    a configuration with the defaults will yield a similar configuration to that of the BLIP-base
    [Salesforce/blip-vqa-base](https://huggingface.co/Salesforce/blip-vqa-base) architecture.

    Configuration objects inherit from [`PretrainedConfig`] and can be used to control the model outputs. Read the
    documentation from [`PretrainedConfig`] for more information.

    Args:
        text_config (`dict`, *optional*):
            Dictionary of configuration options used to initialize [`BlipTextConfig`].
        vision_config (`dict`, *optional*):
            Dictionary of configuration options used to initialize [`BlipVisionConfig`].
        projection_dim (`int`, *optional*, defaults to 512):
            Dimentionality of text and vision projection layers.
        logit_scale_init_value (`float`, *optional*, defaults to 2.6592):
            The inital value of the *logit_scale* paramter. Default is used as per the original BLIP implementation.
        image_text_hidden_size (`int`, *optional*, defaults to 768):
            Dimentionality of the hidden state of the image-text fusion layer.
        kwargs (*optional*):
            Dictionary of keyword arguments.

    Example:

    ```python
    >>> from transformers import BlipConfig, BlipModel

    >>> # Initializing a BlipConfig with Salesforce/blip-vqa-base style configuration
    >>> configuration = BlipConfig()

    >>> # Initializing a BlipPModel (with random weights) from the Salesforce/blip-vqa-base style configuration
    >>> model = BlipModel(configuration)

    >>> # Accessing the model configuration
    >>> configuration = model.config

    >>> # We can also initialize a BlipConfig from a BlipTextConfig and a BlipVisionConfig

    >>> # Initializing a BLIPText and BLIPVision configuration
    >>> config_text = BlipTextConfig()
    >>> config_vision = BlipVisionConfig()

    >>> config = BlipConfig.from_text_vision_configs(config_text, config_vision)
    ```"""
    model_type: str
    is_composition: bool
    text_config: Incomplete
    vision_config: Incomplete
    projection_dim: Incomplete
    logit_scale_init_value: Incomplete
    initializer_factor: float
    initializer_range: float
    image_text_hidden_size: Incomplete
    def __init__(self, text_config: Incomplete | None = None, vision_config: Incomplete | None = None, projection_dim: int = 512, logit_scale_init_value: float = 2.6592, image_text_hidden_size: int = 256, **kwargs) -> None: ...
    @classmethod
    def from_text_vision_configs(cls, text_config: BlipTextConfig, vision_config: BlipVisionConfig, **kwargs):
        """
        Instantiate a [`BlipConfig`] (or a derived class) from blip text model configuration and blip vision model
        configuration.

        Returns:
            [`BlipConfig`]: An instance of a configuration object
        """
    def to_dict(self):
        """
        Serializes this instance to a Python dictionary. Override the default [`~PretrainedConfig.to_dict`].

        Returns:
            `Dict[str, any]`: Dictionary of all the attributes that make up this configuration instance,
        """
