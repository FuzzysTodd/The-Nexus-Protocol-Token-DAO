import os
from ...configuration_utils import PretrainedConfig as PretrainedConfig
from ...utils import logging as logging
from _typeshed import Incomplete
from typing import Union

logger: Incomplete
XCLIP_PRETRAINED_CONFIG_ARCHIVE_MAP: Incomplete

class XCLIPTextConfig(PretrainedConfig):
    '''
    This is the configuration class to store the configuration of a [`XCLIPModel`]. It is used to instantiate an X-CLIP
    model according to the specified arguments, defining the model architecture. Instantiating a configuration with the
    defaults will yield a similar configuration to that of the X-CLIP
    [microsoft/xclip-base-patch32](https://huggingface.co/microsoft/xclip-base-patch32) architecture.

    Configuration objects inherit from [`PretrainedConfig`] and can be used to control the model outputs. Read the
    documentation from [`PretrainedConfig`] for more information.


    Args:
        vocab_size (`int`, *optional*, defaults to 49408):
            Vocabulary size of the X-CLIP text model. Defines the number of different tokens that can be represented by
            the `inputs_ids` passed when calling [`XCLIPModel`].
        hidden_size (`int`, *optional*, defaults to 512):
            Dimensionality of the encoder layers and the pooler layer.
        intermediate_size (`int`, *optional*, defaults to 2048):
            Dimensionality of the "intermediate" (i.e., feed-forward) layer in the Transformer encoder.
        num_hidden_layers (`int`, *optional*, defaults to 12):
            Number of hidden layers in the Transformer encoder.
        num_attention_heads (`int`, *optional*, defaults to 8):
            Number of attention heads for each attention layer in the Transformer encoder.
        max_position_embeddings (`int`, *optional*, defaults to 77):
            The maximum sequence length that this model might ever be used with. Typically set this to something large
            just in case (e.g., 512 or 1024 or 2048).
        hidden_act (`str` or `function`, *optional*, defaults to `"quick_gelu"`):
            The non-linear activation function (function or string) in the encoder and pooler. If string, `"gelu"`,
            `"relu"`, `"selu"` and `"gelu_new"` ``"quick_gelu"` are supported.
        layer_norm_eps (`float`, *optional*, defaults to 1e-5):
            The epsilon used by the layer normalization layers.
        attention_dropout (`float`, *optional*, defaults to 0.0):
            The dropout ratio for the attention probabilities.
        dropout (`float`, *optional*, defaults to 0.0):
            The dropout probabilitiy for all fully connected layers in the embeddings, encoder, and pooler.
        initializer_range (`float`, *optional*, defaults to 0.02):
            The standard deviation of the truncated_normal_initializer for initializing all weight matrices.
        initializer_factor (`float``, *optional*, defaults to 1):
            A factor for initializing all weight matrices (should be kept to 1, used internally for initialization
            testing).

    Example:

    ```python
    >>> from transformers import XCLIPTextModel, XCLIPTextConfig

    >>> # Initializing a XCLIPTextModel with microsoft/xclip-base-patch32 style configuration
    >>> configuration = XCLIPTextConfig()

    >>> # Initializing a XCLIPTextConfig from the microsoft/xclip-base-patch32 style configuration
    >>> model = XCLIPTextModel(configuration)

    >>> # Accessing the model configuration
    >>> configuration = model.config
    ```'''
    model_type: str
    vocab_size: Incomplete
    hidden_size: Incomplete
    intermediate_size: Incomplete
    dropout: Incomplete
    num_hidden_layers: Incomplete
    num_attention_heads: Incomplete
    max_position_embeddings: Incomplete
    layer_norm_eps: Incomplete
    hidden_act: Incomplete
    initializer_range: Incomplete
    initializer_factor: Incomplete
    attention_dropout: Incomplete
    def __init__(self, vocab_size: int = 49408, hidden_size: int = 512, intermediate_size: int = 2048, num_hidden_layers: int = 12, num_attention_heads: int = 8, max_position_embeddings: int = 77, hidden_act: str = 'quick_gelu', layer_norm_eps: float = 1e-05, dropout: float = 0.0, attention_dropout: float = 0.0, initializer_range: float = 0.02, initializer_factor: float = 1.0, pad_token_id: int = 1, bos_token_id: int = 0, eos_token_id: int = 2, **kwargs) -> None: ...
    @classmethod
    def from_pretrained(cls, pretrained_model_name_or_path: Union[str, os.PathLike], **kwargs) -> PretrainedConfig: ...

class XCLIPVisionConfig(PretrainedConfig):
    '''
    This is the configuration class to store the configuration of a [`XCLIPModel`]. It is used to instantiate an X-CLIP
    model according to the specified arguments, defining the model architecture. Instantiating a configuration with the
    defaults will yield a similar configuration to that of the X-CLIP
    [microsoft/xclip-base-patch32](https://huggingface.co/microsoft/xclip-base-patch32) architecture.

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
        mit_hidden_size (`int`, *optional*, defaults to 512):
            Dimensionality of the encoder layers of the Multiframe Integration Transformer (MIT).
        mit_intermediate_size (`int`, *optional*, defaults to 2048):
            Dimensionality of the "intermediate" (i.e., feed-forward) layer in the Multiframe Integration Transformer
            (MIT).
        mit_num_hidden_layers (`int`, *optional*, defaults to 1):
            Number of hidden layers in the Multiframe Integration Transformer (MIT).
        mit_num_attention_heads (`int`, *optional*, defaults to 8):
            Number of attention heads for each attention layer in the Multiframe Integration Transformer (MIT).
        image_size (`int`, *optional*, defaults to 224):
            The size (resolution) of each image.
        patch_size (`int`, *optional*, defaults to 32):
            The size (resolution) of each patch.
        hidden_act (`str` or `function`, *optional*, defaults to `"quick_gelu"`):
            The non-linear activation function (function or string) in the encoder and pooler. If string, `"gelu"`,
            `"relu"`, `"selu"`, `"gelu_new"` and ``"quick_gelu"` are supported.
        layer_norm_eps (`float`, *optional*, defaults to 1e-5):
            The epsilon used by the layer normalization layers.
        dropout (`float`, *optional*, defaults to 0.0):
            The dropout probabilitiy for all fully connected layers in the embeddings, encoder, and pooler.
        attention_dropout (`float`, *optional*, defaults to 0.0):
            The dropout ratio for the attention probabilities.
        initializer_range (`float`, *optional*, defaults to 0.02):
            The standard deviation of the truncated_normal_initializer for initializing all weight matrices.
        initializer_factor (`float``, *optional*, defaults to 1):
            A factor for initializing all weight matrices (should be kept to 1, used internally for initialization
            testing).
        drop_path_rate (`float`, *optional*, defaults to 0.0):
            Stochastic depth rate.

    Example:

    ```python
    >>> from transformers import XCLIPVisionModel, XCLIPVisionConfig

    >>> # Initializing a XCLIPVisionModel with microsoft/xclip-base-patch32 style configuration
    >>> configuration = XCLIPVisionConfig()

    >>> # Initializing a XCLIPVisionModel model from the microsoft/xclip-base-patch32 style configuration
    >>> model = XCLIPVisionModel(configuration)

    >>> # Accessing the model configuration
    >>> configuration = model.config
    ```'''
    model_type: str
    hidden_size: Incomplete
    intermediate_size: Incomplete
    dropout: Incomplete
    num_hidden_layers: Incomplete
    num_attention_heads: Incomplete
    mit_hidden_size: Incomplete
    mit_intermediate_size: Incomplete
    mit_num_hidden_layers: Incomplete
    mit_num_attention_heads: Incomplete
    num_channels: Incomplete
    patch_size: Incomplete
    num_frames: Incomplete
    image_size: Incomplete
    initializer_range: Incomplete
    initializer_factor: Incomplete
    attention_dropout: Incomplete
    layer_norm_eps: Incomplete
    hidden_act: Incomplete
    drop_path_rate: Incomplete
    def __init__(self, hidden_size: int = 768, intermediate_size: int = 3072, num_hidden_layers: int = 12, num_attention_heads: int = 12, mit_hidden_size: int = 512, mit_intermediate_size: int = 2048, mit_num_hidden_layers: int = 1, mit_num_attention_heads: int = 8, num_channels: int = 3, image_size: int = 224, patch_size: int = 32, num_frames: int = 8, hidden_act: str = 'quick_gelu', layer_norm_eps: float = 1e-05, dropout: float = 0.0, attention_dropout: float = 0.0, initializer_range: float = 0.02, initializer_factor: float = 1.0, drop_path_rate: float = 0.0, **kwargs) -> None: ...
    @classmethod
    def from_pretrained(cls, pretrained_model_name_or_path: Union[str, os.PathLike], **kwargs) -> PretrainedConfig: ...

class XCLIPConfig(PretrainedConfig):
    '''
    [`XCLIPConfig`] is the configuration class to store the configuration of a [`XCLIPModel`]. It is used to
    instantiate X-CLIP model according to the specified arguments, defining the text model and vision model configs.
    Instantiating a configuration with the defaults will yield a similar configuration to that of the X-CLIP
    [microsoft/xclip-base-patch32](https://huggingface.co/microsoft/xclip-base-patch32) architecture.

    Configuration objects inherit from [`PretrainedConfig`] and can be used to control the model outputs. Read the
    documentation from [`PretrainedConfig`] for more information.

    Args:
        text_config (`dict`, *optional*):
            Dictionary of configuration options used to initialize [`XCLIPTextConfig`].
        vision_config (`dict`, *optional*):
            Dictionary of configuration options used to initialize [`XCLIPVisionConfig`].
        projection_dim (`int`, *optional*, defaults to 512):
            Dimentionality of text and vision projection layers.
        prompt_layers (`int`, *optional*, defaults to 2):
            Number of layers in the video specific prompt generator.
        prompt_alpha (`float`, *optional*, defaults to 0.1):
            Alpha value to use in the video specific prompt generator.
        prompt_hidden_act (`str` or `function`, *optional*, defaults to `"quick_gelu"`):
            The non-linear activation function (function or string) in the video specific prompt generator. If string,
            `"gelu"`, `"relu"`, `"selu"` and `"gelu_new"` ``"quick_gelu"` are supported.
        prompt_num_attention_heads (`int`, *optional*, defaults to 8):
            Number of attention heads in the cross-attention of the video specific prompt generator.
        prompt_attention_dropout (`float`, *optional*, defaults to 0.0):
            The dropout probability for the attention layers in the video specific prompt generator.
        prompt_projection_dropout (`float`, *optional*, defaults to 0.0):
            The dropout probability for the projection layers in the video specific prompt generator.
        logit_scale_init_value (`float`, *optional*, defaults to 2.6592):
            The inital value of the *logit_scale* parameter. Default is used as per the original XCLIP implementation.
        kwargs (*optional*):
            Dictionary of keyword arguments.
    '''
    model_type: str
    is_composition: bool
    text_config: Incomplete
    vision_config: Incomplete
    projection_dim: Incomplete
    prompt_layers: Incomplete
    prompt_alpha: Incomplete
    prompt_hidden_act: Incomplete
    prompt_num_attention_heads: Incomplete
    prompt_attention_dropout: Incomplete
    prompt_projection_dropout: Incomplete
    logit_scale_init_value: Incomplete
    initializer_factor: float
    def __init__(self, text_config: Incomplete | None = None, vision_config: Incomplete | None = None, projection_dim: int = 512, prompt_layers: int = 2, prompt_alpha: float = 0.1, prompt_hidden_act: str = 'quick_gelu', prompt_num_attention_heads: int = 8, prompt_attention_dropout: float = 0.0, prompt_projection_dropout: float = 0.0, logit_scale_init_value: float = 2.6592, **kwargs) -> None: ...
    @classmethod
    def from_text_vision_configs(cls, text_config: XCLIPTextConfig, vision_config: XCLIPVisionConfig, **kwargs):
        """
        Instantiate a [`XCLIPConfig`] (or a derived class) from xclip text model configuration and xclip vision model
        configuration.

        Returns:
            [`XCLIPConfig`]: An instance of a configuration object
        """
    def to_dict(self):
        """
        Serializes this instance to a Python dictionary. Override the default [`~PretrainedConfig.to_dict`].

        Returns:
            `Dict[str, any]`: Dictionary of all the attributes that make up this configuration instance,
        """
