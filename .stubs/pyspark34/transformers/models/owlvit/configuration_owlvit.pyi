import os
from ...configuration_utils import PretrainedConfig as PretrainedConfig
from ...onnx import OnnxConfig as OnnxConfig
from ...processing_utils import ProcessorMixin as ProcessorMixin
from ...utils import TensorType as TensorType, logging as logging
from _typeshed import Incomplete
from typing import Any, Dict, Mapping, Optional, Union

logger: Incomplete
OWLVIT_PRETRAINED_CONFIG_ARCHIVE_MAP: Incomplete

class OwlViTTextConfig(PretrainedConfig):
    '''
    This is the configuration class to store the configuration of an [`OwlViTTextModel`]. It is used to instantiate an
    OwlViT text encoder according to the specified arguments, defining the model architecture. Instantiating a
    configuration with the defaults will yield a similar configuration to that of the OwlViT
    [google/owlvit-base-patch32](https://huggingface.co/google/owlvit-base-patch32) architecture.

    Configuration objects inherit from [`PretrainedConfig`] and can be used to control the model outputs. Read the
    documentation from [`PretrainedConfig`] for more information.


    Args:
        vocab_size (`int`, *optional*, defaults to 49408):
            Vocabulary size of the OWL-ViT text model. Defines the number of different tokens that can be represented
            by the `inputs_ids` passed when calling [`OwlViTTextModel`].
        hidden_size (`int`, *optional*, defaults to 512):
            Dimensionality of the encoder layers and the pooler layer.
        intermediate_size (`int`, *optional*, defaults to 2048):
            Dimensionality of the "intermediate" (i.e., feed-forward) layer in the Transformer encoder.
        num_hidden_layers (`int`, *optional*, defaults to 12):
            Number of hidden layers in the Transformer encoder.
        num_attention_heads (`int`, *optional*, defaults to 8):
            Number of attention heads for each attention layer in the Transformer encoder.
        max_position_embeddings (`int`, *optional*, defaults to 16):
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
        initializer_factor (`float`, *optional*, defaults to 1):
            A factor for initializing all weight matrices (should be kept to 1, used internally for initialization
            testing).

    Example:

    ```python
    >>> from transformers import OwlViTTextConfig, OwlViTTextModel

    >>> # Initializing a OwlViTTextModel with google/owlvit-base-patch32 style configuration
    >>> configuration = OwlViTTextConfig()

    >>> # Initializing a OwlViTTextConfig from the google/owlvit-base-patch32 style configuration
    >>> model = OwlViTTextModel(configuration)

    >>> # Accessing the model configuration
    >>> configuration = model.config
    ```'''
    model_type: str
    vocab_size: Incomplete
    hidden_size: Incomplete
    intermediate_size: Incomplete
    num_hidden_layers: Incomplete
    num_attention_heads: Incomplete
    max_position_embeddings: Incomplete
    hidden_act: Incomplete
    layer_norm_eps: Incomplete
    dropout: Incomplete
    attention_dropout: Incomplete
    initializer_range: Incomplete
    initializer_factor: Incomplete
    def __init__(self, vocab_size: int = 49408, hidden_size: int = 512, intermediate_size: int = 2048, num_hidden_layers: int = 12, num_attention_heads: int = 8, max_position_embeddings: int = 16, hidden_act: str = 'quick_gelu', layer_norm_eps: float = 1e-05, dropout: float = 0.0, attention_dropout: float = 0.0, initializer_range: float = 0.02, initializer_factor: float = 1.0, pad_token_id: int = 0, bos_token_id: int = 49406, eos_token_id: int = 49407, **kwargs) -> None: ...
    @classmethod
    def from_pretrained(cls, pretrained_model_name_or_path: Union[str, os.PathLike], **kwargs) -> PretrainedConfig: ...

class OwlViTVisionConfig(PretrainedConfig):
    '''
    This is the configuration class to store the configuration of an [`OwlViTVisionModel`]. It is used to instantiate
    an OWL-ViT image encoder according to the specified arguments, defining the model architecture. Instantiating a
    configuration with the defaults will yield a similar configuration to that of the OWL-ViT
    [google/owlvit-base-patch32](https://huggingface.co/google/owlvit-base-patch32) architecture.

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
        num_channels (`int`, *optional*, defaults to 3):
            Number of channels in the input images.
        image_size (`int`, *optional*, defaults to 768):
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
    >>> from transformers import OwlViTVisionConfig, OwlViTVisionModel

    >>> # Initializing a OwlViTVisionModel with google/owlvit-base-patch32 style configuration
    >>> configuration = OwlViTVisionConfig()

    >>> # Initializing a OwlViTVisionModel model from the google/owlvit-base-patch32 style configuration
    >>> model = OwlViTVisionModel(configuration)

    >>> # Accessing the model configuration
    >>> configuration = model.config
    ```'''
    model_type: str
    hidden_size: Incomplete
    intermediate_size: Incomplete
    num_hidden_layers: Incomplete
    num_attention_heads: Incomplete
    num_channels: Incomplete
    image_size: Incomplete
    patch_size: Incomplete
    hidden_act: Incomplete
    layer_norm_eps: Incomplete
    dropout: Incomplete
    attention_dropout: Incomplete
    initializer_range: Incomplete
    initializer_factor: Incomplete
    def __init__(self, hidden_size: int = 768, intermediate_size: int = 3072, num_hidden_layers: int = 12, num_attention_heads: int = 12, num_channels: int = 3, image_size: int = 768, patch_size: int = 32, hidden_act: str = 'quick_gelu', layer_norm_eps: float = 1e-05, dropout: float = 0.0, attention_dropout: float = 0.0, initializer_range: float = 0.02, initializer_factor: float = 1.0, **kwargs) -> None: ...
    @classmethod
    def from_pretrained(cls, pretrained_model_name_or_path: Union[str, os.PathLike], **kwargs) -> PretrainedConfig: ...

class OwlViTConfig(PretrainedConfig):
    """
    [`OwlViTConfig`] is the configuration class to store the configuration of an [`OwlViTModel`]. It is used to
    instantiate an OWL-ViT model according to the specified arguments, defining the text model and vision model
    configs. Instantiating a configuration with the defaults will yield a similar configuration to that of the OWL-ViT
    [google/owlvit-base-patch32](https://huggingface.co/google/owlvit-base-patch32) architecture.

    Configuration objects inherit from [`PretrainedConfig`] and can be used to control the model outputs. Read the
    documentation from [`PretrainedConfig`] for more information.

    Args:
        text_config (`dict`, *optional*):
            Dictionary of configuration options used to initialize [`OwlViTTextConfig`].
        vision_config (`dict`, *optional*):
            Dictionary of configuration options used to initialize [`OwlViTVisionConfig`].
        projection_dim (`int`, *optional*, defaults to 512):
            Dimensionality of text and vision projection layers.
        logit_scale_init_value (`float`, *optional*, defaults to 2.6592):
            The inital value of the *logit_scale* parameter. Default is used as per the original OWL-ViT
            implementation.
        kwargs (*optional*):
            Dictionary of keyword arguments.
    """
    model_type: str
    is_composition: bool
    text_config: Incomplete
    vision_config: Incomplete
    projection_dim: Incomplete
    logit_scale_init_value: Incomplete
    return_dict: Incomplete
    initializer_factor: float
    def __init__(self, text_config: Incomplete | None = None, vision_config: Incomplete | None = None, projection_dim: int = 512, logit_scale_init_value: float = 2.6592, return_dict: bool = True, **kwargs) -> None: ...
    @classmethod
    def from_pretrained(cls, pretrained_model_name_or_path: Union[str, os.PathLike], **kwargs) -> PretrainedConfig: ...
    @classmethod
    def from_text_vision_configs(cls, text_config: Dict, vision_config: Dict, **kwargs):
        """
        Instantiate a [`OwlViTConfig`] (or a derived class) from owlvit text model configuration and owlvit vision
        model configuration.

        Returns:
            [`OwlViTConfig`]: An instance of a configuration object
        """
    def to_dict(self):
        """
        Serializes this instance to a Python dictionary. Override the default [`~PretrainedConfig.to_dict`].

        Returns:
            `Dict[str, any]`: Dictionary of all the attributes that make up this configuration instance,
        """

class OwlViTOnnxConfig(OnnxConfig):
    @property
    def inputs(self) -> Mapping[str, Mapping[int, str]]: ...
    @property
    def outputs(self) -> Mapping[str, Mapping[int, str]]: ...
    @property
    def atol_for_validation(self) -> float: ...
    def generate_dummy_inputs(self, processor: ProcessorMixin, batch_size: int = -1, seq_length: int = -1, framework: Optional['TensorType'] = None) -> Mapping[str, Any]: ...
    @property
    def default_onnx_opset(self) -> int: ...
