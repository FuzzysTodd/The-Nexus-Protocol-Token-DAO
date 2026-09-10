import os
from ...configuration_utils import PretrainedConfig as PretrainedConfig
from ...utils import logging as logging
from _typeshed import Incomplete
from typing import Union

logger: Incomplete
CLIPSEG_PRETRAINED_CONFIG_ARCHIVE_MAP: Incomplete

class CLIPSegTextConfig(PretrainedConfig):
    '''
    This is the configuration class to store the configuration of a [`CLIPSegModel`]. It is used to instantiate an
    CLIPSeg model according to the specified arguments, defining the model architecture. Instantiating a configuration
    with the defaults will yield a similar configuration to that of the CLIPSeg
    [CIDAS/clipseg-rd64](https://huggingface.co/CIDAS/clipseg-rd64) architecture.

    Configuration objects inherit from [`PretrainedConfig`] and can be used to control the model outputs. Read the
    documentation from [`PretrainedConfig`] for more information.

    Args:
        vocab_size (`int`, *optional*, defaults to 49408):
            Vocabulary size of the CLIPSeg text model. Defines the number of different tokens that can be represented
            by the `inputs_ids` passed when calling [`CLIPSegModel`].
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
            `"relu"`, `"selu"` and `"gelu_new"` ``"quick_gelu"` are supported. layer_norm_eps (`float`, *optional*,
            defaults to 1e-5): The epsilon used by the layer normalization layers.
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
    >>> from transformers import CLIPSegTextConfig, CLIPSegTextModel

    >>> # Initializing a CLIPSegTextConfig with CIDAS/clipseg-rd64 style configuration
    >>> configuration = CLIPSegTextConfig()

    >>> # Initializing a CLIPSegTextModel (with random weights) from the CIDAS/clipseg-rd64 style configuration
    >>> model = CLIPSegTextModel(configuration)

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

class CLIPSegVisionConfig(PretrainedConfig):
    '''
    This is the configuration class to store the configuration of a [`CLIPSegModel`]. It is used to instantiate an
    CLIPSeg model according to the specified arguments, defining the model architecture. Instantiating a configuration
    with the defaults will yield a similar configuration to that of the CLIPSeg
    [CIDAS/clipseg-rd64](https://huggingface.co/CIDAS/clipseg-rd64) architecture.

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
    >>> from transformers import CLIPSegVisionConfig, CLIPSegVisionModel

    >>> # Initializing a CLIPSegVisionConfig with CIDAS/clipseg-rd64 style configuration
    >>> configuration = CLIPSegVisionConfig()

    >>> # Initializing a CLIPSegVisionModel (with random weights) from the CIDAS/clipseg-rd64 style configuration
    >>> model = CLIPSegVisionModel(configuration)

    >>> # Accessing the model configuration
    >>> configuration = model.config
    ```'''
    model_type: str
    hidden_size: Incomplete
    intermediate_size: Incomplete
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
    def __init__(self, hidden_size: int = 768, intermediate_size: int = 3072, num_hidden_layers: int = 12, num_attention_heads: int = 12, num_channels: int = 3, image_size: int = 224, patch_size: int = 32, hidden_act: str = 'quick_gelu', layer_norm_eps: float = 1e-05, dropout: float = 0.0, attention_dropout: float = 0.0, initializer_range: float = 0.02, initializer_factor: float = 1.0, **kwargs) -> None: ...
    @classmethod
    def from_pretrained(cls, pretrained_model_name_or_path: Union[str, os.PathLike], **kwargs) -> PretrainedConfig: ...

class CLIPSegConfig(PretrainedConfig):
    '''
    [`CLIPSegConfig`] is the configuration class to store the configuration of a [`CLIPSegModel`]. It is used to
    instantiate a CLIPSeg model according to the specified arguments, defining the text model and vision model configs.
    Instantiating a configuration with the defaults will yield a similar configuration to that of the CLIPSeg
    [CIDAS/clipseg-rd64](https://huggingface.co/CIDAS/clipseg-rd64) architecture.

    Configuration objects inherit from [`PretrainedConfig`] and can be used to control the model outputs. Read the
    documentation from [`PretrainedConfig`] for more information.

    Args:
        text_config (`dict`, *optional*):
            Dictionary of configuration options used to initialize [`CLIPSegTextConfig`].
        vision_config (`dict`, *optional*):
            Dictionary of configuration options used to initialize [`CLIPSegVisionConfig`].
        projection_dim (`int`, *optional*, defaults to 512):
            Dimensionality of text and vision projection layers.
        logit_scale_init_value (`float`, *optional*, defaults to 2.6592):
            The inital value of the *logit_scale* paramter. Default is used as per the original CLIPSeg implementation.
        extract_layers (`List[int]`, *optional*, defaults to [3, 6, 9]):
            Layers to extract when forwarding the query image through the frozen visual backbone of CLIP.
        reduce_dim (`int`, *optional*, defaults to 64):
            Dimensionality to reduce the CLIP vision embedding.
        decoder_num_attention_heads (`int`, *optional*, defaults to 4):
            Number of attention heads in the decoder of CLIPSeg.
        decoder_attention_dropout (`float`, *optional*, defaults to 0.0):
            The dropout ratio for the attention probabilities.
        decoder_hidden_act (`str` or `function`, *optional*, defaults to `"quick_gelu"`):
            The non-linear activation function (function or string) in the encoder and pooler. If string, `"gelu"`,
            `"relu"`, `"selu"` and `"gelu_new"` ``"quick_gelu"` are supported. layer_norm_eps (`float`, *optional*,
            defaults to 1e-5): The epsilon used by the layer normalization layers.
        decoder_intermediate_size (`int`, *optional*, defaults to 2048):
            Dimensionality of the "intermediate" (i.e., feed-forward) layers in the Transformer decoder.
        conditional_layer (`int`, *optional*, defaults to 0):
            The layer to use of the Transformer encoder whose activations will be combined with the condition
            embeddings using FiLM (Feature-wise Linear Modulation). If 0, the last layer is used.
        use_complex_transposed_convolution (`bool`, *optional*, defaults to `False`):
            Whether to use a more complex transposed convolution in the decoder, enabling more fine-grained
            segmentation.
        kwargs (*optional*):
            Dictionary of keyword arguments.

    Example:

    ```python
    >>> from transformers import CLIPSegConfig, CLIPSegModel

    >>> # Initializing a CLIPSegConfig with CIDAS/clipseg-rd64 style configuration
    >>> configuration = CLIPSegConfig()

    >>> # Initializing a CLIPSegModel (with random weights) from the CIDAS/clipseg-rd64 style configuration
    >>> model = CLIPSegModel(configuration)

    >>> # Accessing the model configuration
    >>> configuration = model.config

    >>> # We can also initialize a CLIPSegConfig from a CLIPSegTextConfig and a CLIPSegVisionConfig

    >>> # Initializing a CLIPSegText and CLIPSegVision configuration
    >>> config_text = CLIPSegTextConfig()
    >>> config_vision = CLIPSegVisionConfig()

    >>> config = CLIPSegConfig.from_text_vision_configs(config_text, config_vision)
    ```'''
    model_type: str
    is_composition: bool
    text_config: Incomplete
    vision_config: Incomplete
    projection_dim: Incomplete
    logit_scale_init_value: Incomplete
    extract_layers: Incomplete
    reduce_dim: Incomplete
    decoder_num_attention_heads: Incomplete
    decoder_attention_dropout: Incomplete
    decoder_hidden_act: Incomplete
    decoder_intermediate_size: Incomplete
    conditional_layer: Incomplete
    initializer_factor: float
    use_complex_transposed_convolution: Incomplete
    def __init__(self, text_config: Incomplete | None = None, vision_config: Incomplete | None = None, projection_dim: int = 512, logit_scale_init_value: float = 2.6592, extract_layers=[3, 6, 9], reduce_dim: int = 64, decoder_num_attention_heads: int = 4, decoder_attention_dropout: float = 0.0, decoder_hidden_act: str = 'quick_gelu', decoder_intermediate_size: int = 2048, conditional_layer: int = 0, use_complex_transposed_convolution: bool = False, **kwargs) -> None: ...
    @classmethod
    def from_text_vision_configs(cls, text_config: CLIPSegTextConfig, vision_config: CLIPSegVisionConfig, **kwargs):
        """
        Instantiate a [`CLIPSegConfig`] (or a derived class) from clipseg text model configuration and clipseg vision
        model configuration.

        Returns:
            [`CLIPSegConfig`]: An instance of a configuration object
        """
    def to_dict(self):
        """
        Serializes this instance to a Python dictionary. Override the default [`~PretrainedConfig.to_dict`].

        Returns:
            `Dict[str, any]`: Dictionary of all the attributes that make up this configuration instance,
        """
