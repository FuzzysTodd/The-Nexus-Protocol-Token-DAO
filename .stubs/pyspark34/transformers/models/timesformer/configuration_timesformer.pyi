from ...configuration_utils import PretrainedConfig as PretrainedConfig
from ...utils import logging as logging
from _typeshed import Incomplete

logger: Incomplete
TIMESFORMER_PRETRAINED_CONFIG_ARCHIVE_MAP: Incomplete

class TimesformerConfig(PretrainedConfig):
    '''
    This is the configuration class to store the configuration of a [`TimesformerModel`]. It is used to instantiate a
    TimeSformer model according to the specified arguments, defining the model architecture. Instantiating a
    configuration with the defaults will yield a similar configuration to that of the TimeSformer
    [facebook/timesformer](https://huggingface.co/facebook/timesformer-base-finetuned-k600) architecture.

    Configuration objects inherit from [`PretrainedConfig`] and can be used to control the model outputs. Read the
    documentation from [`PretrainedConfig`] for more information.

    Args:
        image_size (`int`, *optional*, defaults to 224):
            The size (resolution) of each image.
        patch_size (`int`, *optional*, defaults to 16):
            The size (resolution) of each patch.
        num_channels (`int`, *optional*, defaults to 3):
            The number of input channels.
        num_frames (`int`, *optional*, defaults to 8):
            The number of frames in each video.
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
        hidden_dropout_prob (`float`, *optional*, defaults to 0.0):
            The dropout probabilitiy for all fully connected layers in the embeddings, encoder, and pooler.
        attention_probs_dropout_prob (`float`, *optional*, defaults to 0.0):
            The dropout ratio for the attention probabilities.
        initializer_range (`float`, *optional*, defaults to 0.02):
            The standard deviation of the truncated_normal_initializer for initializing all weight matrices.
        layer_norm_eps (`float`, *optional*, defaults to 1e-6):
            The epsilon used by the layer normalization layers.
        qkv_bias (`bool`, *optional*, defaults to `True`):
            Whether to add a bias to the queries, keys and values.
        attention_type (`str`, *optional*, defaults to `"divided_space_time"`):
            The attention type to use. Must be one of `"divided_space_time"`, `"space_only"`, `"joint_space_time"`.
        drop_path_rate (`float`, *optional*, defaults to 0):
            The dropout ratio for stochastic depth.

    Example:

    ```python
    >>> from transformers import TimesformerConfig, TimesformerModel

    >>> # Initializing a TimeSformer timesformer-base style configuration
    >>> configuration = TimesformerConfig()

    >>> # Randomly initializing a model from the configuration
    >>> model = TimesformerModel(configuration)

    >>> # Accessing the model configuration
    >>> configuration = model.config
    ```'''
    model_type: str
    image_size: Incomplete
    patch_size: Incomplete
    num_channels: Incomplete
    num_frames: Incomplete
    hidden_size: Incomplete
    num_hidden_layers: Incomplete
    num_attention_heads: Incomplete
    intermediate_size: Incomplete
    hidden_act: Incomplete
    hidden_dropout_prob: Incomplete
    attention_probs_dropout_prob: Incomplete
    initializer_range: Incomplete
    layer_norm_eps: Incomplete
    qkv_bias: Incomplete
    attention_type: Incomplete
    drop_path_rate: Incomplete
    def __init__(self, image_size: int = 224, patch_size: int = 16, num_channels: int = 3, num_frames: int = 8, hidden_size: int = 768, num_hidden_layers: int = 12, num_attention_heads: int = 12, intermediate_size: int = 3072, hidden_act: str = 'gelu', hidden_dropout_prob: float = 0.0, attention_probs_dropout_prob: float = 0.0, initializer_range: float = 0.02, layer_norm_eps: float = 1e-06, qkv_bias: bool = True, attention_type: str = 'divided_space_time', drop_path_rate: int = 0, **kwargs) -> None: ...
