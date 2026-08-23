from ...configuration_utils import PretrainedConfig as PretrainedConfig
from ...utils import logging as logging
from _typeshed import Incomplete

logger: Incomplete
AUDIO_SPECTROGRAM_TRANSFORMER_PRETRAINED_CONFIG_ARCHIVE_MAP: Incomplete

class ASTConfig(PretrainedConfig):
    '''
    This is the configuration class to store the configuration of a [`ASTModel`]. It is used to instantiate an AST
    model according to the specified arguments, defining the model architecture. Instantiating a configuration with the
    defaults will yield a similar configuration to that of the AST
    [MIT/ast-finetuned-audioset-10-10-0.4593](https://huggingface.co/MIT/ast-finetuned-audioset-10-10-0.4593)
    architecture.

    Configuration objects inherit from [`PretrainedConfig`] and can be used to control the model outputs. Read the
    documentation from [`PretrainedConfig`] for more information.

    Args:
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
        hidden_dropout_prob (`float`, *optional*, defaults to 0.1):
            The dropout probability for all fully connected layers in the embeddings, encoder, and pooler.
        attention_probs_dropout_prob (`float`, *optional*, defaults to 0.1):
            The dropout ratio for the attention probabilities.
        initializer_range (`float`, *optional*, defaults to 0.02):
            The standard deviation of the truncated_normal_initializer for initializing all weight matrices.
        layer_norm_eps (`float`, *optional*, defaults to 1e-12):
            The epsilon used by the layer normalization layers.
        patch_size (`int`, *optional*, defaults to `16`):
            The size (resolution) of each patch.
        qkv_bias (`bool`, *optional*, defaults to `True`):
            Whether to add a bias to the queries, keys and values.
        frequency_stride (`int`, *optional*, defaults to 10):
            Frequency stride to use when patchifying the spectrograms.
        time_stride (`int`, *optional*, defaults to 10):
            Temporal stride to use when patchifying the spectrograms.
        max_length (`int`, *optional*, defaults to 1024):
            Temporal dimension of the spectrograms.
        num_mel_bins (`int`, *optional*, defaults to 128):
            Frequency dimension of the spectrograms (number of Mel-frequency bins).

    Example:

    ```python
    >>> from transformers import ASTConfig, ASTModel

    >>> # Initializing a AST MIT/ast-finetuned-audioset-10-10-0.4593 style configuration
    >>> configuration = ASTConfig()

    >>> # Initializing a model (with random weights) from the MIT/ast-finetuned-audioset-10-10-0.4593 style configuration
    >>> model = ASTModel(configuration)

    >>> # Accessing the model configuration
    >>> configuration = model.config
    ```'''
    model_type: str
    hidden_size: Incomplete
    num_hidden_layers: Incomplete
    num_attention_heads: Incomplete
    intermediate_size: Incomplete
    hidden_act: Incomplete
    hidden_dropout_prob: Incomplete
    attention_probs_dropout_prob: Incomplete
    initializer_range: Incomplete
    layer_norm_eps: Incomplete
    patch_size: Incomplete
    qkv_bias: Incomplete
    frequency_stride: Incomplete
    time_stride: Incomplete
    max_length: Incomplete
    num_mel_bins: Incomplete
    def __init__(self, hidden_size: int = 768, num_hidden_layers: int = 12, num_attention_heads: int = 12, intermediate_size: int = 3072, hidden_act: str = 'gelu', hidden_dropout_prob: float = 0.0, attention_probs_dropout_prob: float = 0.0, initializer_range: float = 0.02, layer_norm_eps: float = 1e-12, patch_size: int = 16, qkv_bias: bool = True, frequency_stride: int = 10, time_stride: int = 10, max_length: int = 1024, num_mel_bins: int = 128, **kwargs) -> None: ...
