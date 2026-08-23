import os
from ...configuration_utils import PretrainedConfig as PretrainedConfig
from ...utils import logging as logging
from _typeshed import Incomplete
from typing import Union

logger: Incomplete
ALTCLIP_PRETRAINED_CONFIG_ARCHIVE_MAP: Incomplete

class AltCLIPTextConfig(PretrainedConfig):
    '''
    This is the configuration class to store the configuration of a [`AltCLIPTextModel`]. It is used to instantiate a
    AltCLIP text model according to the specified arguments, defining the model architecture. Instantiating a
    configuration with the defaults will yield a similar configuration to that of the AltCLIP
    [BAAI/AltCLIP](https://huggingface.co/BAAI/AltCLIP) architecture.

    Configuration objects inherit from [`PretrainedConfig`] and can be used to control the model outputs. Read the
    documentation from [`PretrainedConfig`] for more information.


    Args:
        vocab_size (`int`, *optional*, defaults to 250002):
            Vocabulary size of the AltCLIP model. Defines the number of different tokens that can be represented by the
            `inputs_ids` passed when calling [`AltCLIPTextModel`].
        hidden_size (`int`, *optional*, defaults to 1024):
            Dimensionality of the encoder layers and the pooler layer.
        num_hidden_layers (`int`, *optional*, defaults to 24):
            Number of hidden layers in the Transformer encoder.
        num_attention_heads (`int`, *optional*, defaults to 16):
            Number of attention heads for each attention layer in the Transformer encoder.
        intermediate_size (`int`, *optional*, defaults to 4096):
            Dimensionality of the "intermediate" (often named feed-forward) layer in the Transformer encoder.
        hidden_act (`str` or `Callable`, *optional*, defaults to `"gelu"`):
            The non-linear activation function (function or string) in the encoder and pooler. If string, `"gelu"`,
            `"relu"`, `"silu"` and `"gelu_new"` are supported.
        hidden_dropout_prob (`float`, *optional*, defaults to 0.1):
            The dropout probability for all fully connected layers in the embeddings, encoder, and pooler.
        attention_probs_dropout_prob (`float`, *optional*, defaults to 0.1):
            The dropout ratio for the attention probabilities.
        max_position_embeddings (`int`, *optional*, defaults to 514):
            The maximum sequence length that this model might ever be used with. Typically set this to something large
            just in case (e.g., 512 or 1024 or 2048).
        type_vocab_size (`int`, *optional*, defaults to 2):
            The vocabulary size of the `token_type_ids` passed when calling [`AltCLIPTextModel`]
        initializer_range (`float`, *optional*, defaults to 0.02):
            The standard deviation of the truncated_normal_initializer for initializing all weight matrices.
        layer_norm_eps (`float`, *optional*, defaults to 1e-5):
            The epsilon used by the layer normalization layers.
        position_embedding_type (`str`, *optional*, defaults to `"absolute"`):
            Type of position embedding. Choose one of `"absolute"`, `"relative_key"`, `"relative_key_query"`. For
            positional embeddings use `"absolute"`. For more information on `"relative_key"`, please refer to
            [Self-Attention with Relative Position Representations (Shaw et al.)](https://arxiv.org/abs/1803.02155).
            For more information on `"relative_key_query"`, please refer to *Method 4* in [Improve Transformer Models
            with Better Relative Position Embeddings (Huang et al.)](https://arxiv.org/abs/2009.13658).
        use_cache (`bool`, *optional*, defaults to `True`):
            Whether or not the model should return the last key/values attentions (not used by all models). Only
            relevant if `config.is_decoder=True`.
        classifier_dropout (`float`, *optional*):
            The dropout ratio for the classification head.
        project_dim (`int`, *optional*, defaults to 768):
            The dimentions of the teacher model before the mapping layer.
        pooler_fn (`str`, *optional*, defaults to `"cls"`):
            Type of pooler we use. We take the first token as pooled output.

    Examples:

    ```python
    >>> from transformers import AltCLIPTextModel, AltCLIPTextConfig

    >>> # Initializing a AltCLIPTextConfig with BAAI/AltCLIP style configuration
    >>> configuration = AltCLIPTextConfig()

    >>> # Initializing a AltCLIPTextModel (with random weights) from the BAAI/AltCLIP style configuration
    >>> model = AltCLIPTextModel(configuration)

    >>> # Accessing the model configuration
    >>> configuration = model.config
    ```'''
    model_type: str
    vocab_size: Incomplete
    hidden_size: Incomplete
    num_hidden_layers: Incomplete
    num_attention_heads: Incomplete
    hidden_act: Incomplete
    intermediate_size: Incomplete
    hidden_dropout_prob: Incomplete
    attention_probs_dropout_prob: Incomplete
    max_position_embeddings: Incomplete
    type_vocab_size: Incomplete
    initializer_range: Incomplete
    initializer_factor: Incomplete
    layer_norm_eps: Incomplete
    position_embedding_type: Incomplete
    use_cache: Incomplete
    classifier_dropout: Incomplete
    project_dim: Incomplete
    pooler_fn: Incomplete
    def __init__(self, vocab_size: int = 250002, hidden_size: int = 1024, num_hidden_layers: int = 24, num_attention_heads: int = 16, intermediate_size: int = 4096, hidden_act: str = 'gelu', hidden_dropout_prob: float = 0.1, attention_probs_dropout_prob: float = 0.1, max_position_embeddings: int = 514, type_vocab_size: int = 1, initializer_range: float = 0.02, initializer_factor: float = 0.02, layer_norm_eps: float = 1e-05, pad_token_id: int = 1, bos_token_id: int = 0, eos_token_id: int = 2, position_embedding_type: str = 'absolute', use_cache: bool = True, classifier_dropout: Incomplete | None = None, project_dim: int = 768, pooler_fn: str = 'cls', **kwargs) -> None: ...

class AltCLIPVisionConfig(PretrainedConfig):
    '''
    This is the configuration class to store the configuration of a [`AltCLIPModel`]. It is used to instantiate an
    AltCLIP model according to the specified arguments, defining the model architecture. Instantiating a configuration
    with the defaults will yield a similar configuration to that of the AltCLIP
    [BAAI/AltCLIP](https://huggingface.co/BAAI/AltCLIP) architecture.

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
        hidden_act (`str` or `function`, *optional*, defaults to `"quick_gelu"`):
            The non-linear activation function (function or string) in the encoder and pooler. If string, `"gelu"`,
            `"relu"`, `"selu"` and `"gelu_new"` ``"quick_gelu"` are supported. layer_norm_eps (`float`, *optional*,
            defaults to 1e-5): The epsilon used by the layer normalization layers.
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
    >>> from transformers import AltCLIPVisionConfig, AltCLIPVisionModel

    >>> # Initializing a AltCLIPVisionConfig with BAAI/AltCLIP style configuration
    >>> configuration = AltCLIPVisionConfig()

    >>> # Initializing a AltCLIPVisionModel (with random weights) from the BAAI/AltCLIP style configuration
    >>> model = AltCLIPVisionModel(configuration)

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
    def __init__(self, hidden_size: int = 768, intermediate_size: int = 3072, projection_dim: int = 512, num_hidden_layers: int = 12, num_attention_heads: int = 12, num_channels: int = 3, image_size: int = 224, patch_size: int = 32, hidden_act: str = 'quick_gelu', layer_norm_eps: float = 1e-05, dropout: float = 0.0, attention_dropout: float = 0.0, initializer_range: float = 0.02, initializer_factor: float = 1.0, **kwargs) -> None: ...
    @classmethod
    def from_pretrained(cls, pretrained_model_name_or_path: Union[str, os.PathLike], **kwargs) -> PretrainedConfig: ...

class AltCLIPConfig(PretrainedConfig):
    """
    This is the configuration class to store the configuration of a [`AltCLIPModel`]. It is used to instantiate an
    AltCLIP model according to the specified arguments, defining the model architecture. Instantiating a configuration
    with the defaults will yield a similar configuration to that of the AltCLIP
    [BAAI/AltCLIP](https://huggingface.co/BAAI/AltCLIP) architecture.

    Configuration objects inherit from [`PretrainedConfig`] and can be used to control the model outputs. Read the
    documentation from [`PretrainedConfig`] for more information.

    Args:
        text_config (`dict`, *optional*):
            Dictionary of configuration options used to initialize [`AltCLIPTextConfig`].
        vision_config (`dict`, *optional*):
            Dictionary of configuration options used to initialize [`AltCLIPVisionConfig`].
        projection_dim (`int`, *optional*, defaults to 512):
            Dimentionality of text and vision projection layers.
        logit_scale_init_value (`float`, *optional*, defaults to 2.6592):
            The inital value of the *logit_scale* paramter. Default is used as per the original CLIP implementation.
        kwargs (*optional*):
            Dictionary of keyword arguments.

    Example:

    ```python
    >>> from transformers import AltCLIPConfig, AltCLIPModel

    >>> # Initializing a AltCLIPConfig with BAAI/AltCLIP style configuration
    >>> configuration = AltCLIPConfig()

    >>> # Initializing a AltCLIPModel (with random weights) from the BAAI/AltCLIP style configuration
    >>> model = AltCLIPModel(configuration)

    >>> # Accessing the model configuration
    >>> configuration = model.config

    >>> # We can also initialize a AltCLIPConfig from a AltCLIPTextConfig and a AltCLIPVisionConfig

    >>> # Initializing a AltCLIPText and AltCLIPVision configuration
    >>> config_text = AltCLIPTextConfig()
    >>> config_vision = AltCLIPVisionConfig()

    >>> config = AltCLIPConfig.from_text_vision_configs(config_text, config_vision)
    ```"""
    model_type: str
    is_composition: bool
    text_config: Incomplete
    vision_config: Incomplete
    projection_dim: Incomplete
    logit_scale_init_value: Incomplete
    initializer_factor: float
    def __init__(self, text_config: Incomplete | None = None, vision_config: Incomplete | None = None, projection_dim: int = 768, logit_scale_init_value: float = 2.6592, **kwargs) -> None: ...
    @classmethod
    def from_text_vision_configs(cls, text_config: AltCLIPTextConfig, vision_config: AltCLIPVisionConfig, **kwargs):
        """
        Instantiate a [`AltCLIPConfig`] (or a derived class) from altclip text model configuration and altclip vision
        model configuration.

        Returns:
            [`AltCLIPConfig`]: An instance of a configuration object
        """
    def to_dict(self):
        """
        Serializes this instance to a Python dictionary. Override the default [`~PretrainedConfig.to_dict`].

        Returns:
            `Dict[str, any]`: Dictionary of all the attributes that make up this configuration instance,
        """
