from ...configuration_utils import PretrainedConfig as PretrainedConfig
from ...utils import logging as logging
from _typeshed import Incomplete

logger: Incomplete
FNET_PRETRAINED_CONFIG_ARCHIVE_MAP: Incomplete

class FNetConfig(PretrainedConfig):
    '''
    This is the configuration class to store the configuration of a [`FNetModel`]. It is used to instantiate an FNet
    model according to the specified arguments, defining the model architecture. Instantiating a configuration with the
    defaults will yield a similar configuration to that of the FNet
    [google/fnet-base](https://huggingface.co/google/fnet-base) architecture.

    Configuration objects inherit from [`PretrainedConfig`] and can be used to control the model outputs. Read the
    documentation from [`PretrainedConfig`] for more information.


    Args:
        vocab_size (`int`, *optional*, defaults to 32000):
            Vocabulary size of the FNet model. Defines the number of different tokens that can be represented by the
            `inputs_ids` passed when calling [`FNetModel`] or [`TFFNetModel`].
        hidden_size (`int`, *optional*, defaults to 768):
            Dimension of the encoder layers and the pooler layer.
        num_hidden_layers (`int`, *optional*, defaults to 12):
            Number of hidden layers in the Transformer encoder.
        intermediate_size (`int`, *optional*, defaults to 3072):
            Dimension of the "intermediate" (i.e., feed-forward) layer in the Transformer encoder.
        hidden_act (`str` or `function`, *optional*, defaults to `"gelu_new"`):
            The non-linear activation function (function or string) in the encoder and pooler. If string, `"gelu"`,
            `"relu"`, `"selu"` and `"gelu_new"` are supported.
        hidden_dropout_prob (`float`, *optional*, defaults to 0.1):
            The dropout probabilitiy for all fully connected layers in the embeddings, encoder, and pooler.
        max_position_embeddings (`int`, *optional*, defaults to 512):
            The maximum sequence length that this model might ever be used with. Typically set this to something large
            just in case (e.g., 512 or 1024 or 2048).
        type_vocab_size (`int`, *optional*, defaults to 4):
            The vocabulary size of the `token_type_ids` passed when calling [`FNetModel`] or [`TFFNetModel`].
        initializer_range (`float`, *optional*, defaults to 0.02):
            The standard deviation of the truncated_normal_initializer for initializing all weight matrices.
        layer_norm_eps (`float`, *optional*, defaults to 1e-12):
            The epsilon used by the layer normalization layers.
        use_tpu_fourier_optimizations (`bool`, *optional*, defaults to `False`):
            Determines whether to use TPU optimized FFTs. If `True`, the model will favor axis-wise FFTs transforms.
            Set to `False` for GPU/CPU hardware, in which case n-dimensional FFTs are used.
        tpu_short_seq_length (`int`, *optional*, defaults to 512):
            The sequence length that is expected by the model when using TPUs. This will be used to initialize the DFT
            matrix only when *use_tpu_fourier_optimizations* is set to `True` and the input sequence is shorter than or
            equal to 4096 tokens.

    Example:

    ```python
    >>> from transformers import FNetConfig, FNetModel

    >>> # Initializing a FNet fnet-base style configuration
    >>> configuration = FNetConfig()

    >>> # Initializing a model (with random weights) from the fnet-base style configuration
    >>> model = FNetModel(configuration)

    >>> # Accessing the model configuration
    >>> configuration = model.config
    ```'''
    model_type: str
    vocab_size: Incomplete
    max_position_embeddings: Incomplete
    hidden_size: Incomplete
    num_hidden_layers: Incomplete
    intermediate_size: Incomplete
    hidden_act: Incomplete
    hidden_dropout_prob: Incomplete
    initializer_range: Incomplete
    type_vocab_size: Incomplete
    layer_norm_eps: Incomplete
    use_tpu_fourier_optimizations: Incomplete
    tpu_short_seq_length: Incomplete
    def __init__(self, vocab_size: int = 32000, hidden_size: int = 768, num_hidden_layers: int = 12, intermediate_size: int = 3072, hidden_act: str = 'gelu_new', hidden_dropout_prob: float = 0.1, max_position_embeddings: int = 512, type_vocab_size: int = 4, initializer_range: float = 0.02, layer_norm_eps: float = 1e-12, use_tpu_fourier_optimizations: bool = False, tpu_short_seq_length: int = 512, pad_token_id: int = 3, bos_token_id: int = 1, eos_token_id: int = 2, **kwargs) -> None: ...
