from ...configuration_utils import PretrainedConfig as PretrainedConfig
from ...utils import logging as logging
from _typeshed import Incomplete

logger: Incomplete
CANINE_PRETRAINED_CONFIG_ARCHIVE_MAP: Incomplete

class CanineConfig(PretrainedConfig):
    '''
    This is the configuration class to store the configuration of a [`CanineModel`]. It is used to instantiate an
    CANINE model according to the specified arguments, defining the model architecture. Instantiating a configuration
    with the defaults will yield a similar configuration to that of the CANINE
    [google/canine-s](https://huggingface.co/google/canine-s) architecture.

    Configuration objects inherit from [`PretrainedConfig`] and can be used to control the model outputs. Read the
    documentation from [`PretrainedConfig`] for more information.


    Args:
        hidden_size (`int`, *optional*, defaults to 768):
            Dimension of the encoder layers and the pooler layer.
        num_hidden_layers (`int`, *optional*, defaults to 12):
            Number of hidden layers in the deep Transformer encoder.
        num_attention_heads (`int`, *optional*, defaults to 12):
            Number of attention heads for each attention layer in the Transformer encoders.
        intermediate_size (`int`, *optional*, defaults to 3072):
            Dimension of the "intermediate" (i.e., feed-forward) layer in the Transformer encoders.
        hidden_act (`str` or `function`, *optional*, defaults to `"gelu"`):
            The non-linear activation function (function or string) in the encoder and pooler. If string, `"gelu"`,
            `"relu"`, `"selu"` and `"gelu_new"` are supported.
        hidden_dropout_prob (`float`, *optional*, defaults to 0.1):
            The dropout probabilitiy for all fully connected layers in the embeddings, encoders, and pooler.
        attention_probs_dropout_prob (`float`, *optional*, defaults to 0.1):
            The dropout ratio for the attention probabilities.
        max_position_embeddings (`int`, *optional*, defaults to 16384):
            The maximum sequence length that this model might ever be used with.
        type_vocab_size (`int`, *optional*, defaults to 16):
            The vocabulary size of the `token_type_ids` passed when calling [`CanineModel`].
        initializer_range (`float`, *optional*, defaults to 0.02):
            The standard deviation of the truncated_normal_initializer for initializing all weight matrices.
        layer_norm_eps (`float`, *optional*, defaults to 1e-12):
            The epsilon used by the layer normalization layers.
        downsampling_rate (`int`, *optional*, defaults to 4):
            The rate at which to downsample the original character sequence length before applying the deep Transformer
            encoder.
        upsampling_kernel_size (`int`, *optional*, defaults to 4):
            The kernel size (i.e. the number of characters in each window) of the convolutional projection layer when
            projecting back from `hidden_size`*2 to `hidden_size`.
        num_hash_functions (`int`, *optional*, defaults to 8):
            The number of hash functions to use. Each hash function has its own embedding matrix.
        num_hash_buckets (`int`, *optional*, defaults to 16384):
            The number of hash buckets to use.
        local_transformer_stride (`int`, *optional*, defaults to 128):
            The stride of the local attention of the first shallow Transformer encoder. Defaults to 128 for good
            TPU/XLA memory alignment.

    Example:

    ```python
    >>> from transformers import CanineConfig, CanineModel

    >>> # Initializing a CANINE google/canine-s style configuration
    >>> configuration = CanineConfig()

    >>> # Initializing a model (with random weights) from the google/canine-s style configuration
    >>> model = CanineModel(configuration)

    >>> # Accessing the model configuration
    >>> configuration = model.config
    ```'''
    model_type: str
    max_position_embeddings: Incomplete
    hidden_size: Incomplete
    num_hidden_layers: Incomplete
    num_attention_heads: Incomplete
    intermediate_size: Incomplete
    hidden_act: Incomplete
    hidden_dropout_prob: Incomplete
    attention_probs_dropout_prob: Incomplete
    initializer_range: Incomplete
    type_vocab_size: Incomplete
    layer_norm_eps: Incomplete
    downsampling_rate: Incomplete
    upsampling_kernel_size: Incomplete
    num_hash_functions: Incomplete
    num_hash_buckets: Incomplete
    local_transformer_stride: Incomplete
    def __init__(self, hidden_size: int = 768, num_hidden_layers: int = 12, num_attention_heads: int = 12, intermediate_size: int = 3072, hidden_act: str = 'gelu', hidden_dropout_prob: float = 0.1, attention_probs_dropout_prob: float = 0.1, max_position_embeddings: int = 16384, type_vocab_size: int = 16, initializer_range: float = 0.02, layer_norm_eps: float = 1e-12, pad_token_id: int = 0, bos_token_id: int = 57344, eos_token_id: int = 57345, downsampling_rate: int = 4, upsampling_kernel_size: int = 4, num_hash_functions: int = 8, num_hash_buckets: int = 16384, local_transformer_stride: int = 128, **kwargs) -> None: ...
