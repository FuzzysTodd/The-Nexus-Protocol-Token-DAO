from ...configuration_utils import PretrainedConfig as PretrainedConfig
from ...utils import logging as logging
from _typeshed import Incomplete

logger: Incomplete
BIOGPT_PRETRAINED_CONFIG_ARCHIVE_MAP: Incomplete

class BioGptConfig(PretrainedConfig):
    '''
    This is the configuration class to store the configuration of a [`BioGptModel`]. It is used to instantiate an
    BioGPT model according to the specified arguments, defining the model architecture. Instantiating a configuration
    with the defaults will yield a similar configuration to that of the BioGPT
    [microsoft/biogpt](https://huggingface.co/microsoft/biogpt) architecture.

    Configuration objects inherit from [`PretrainedConfig`] and can be used to control the model outputs. Read the
    documentation from [`PretrainedConfig`] for more information.


    Args:
        vocab_size (`int`, *optional*, defaults to 42384):
            Vocabulary size of the BioGPT model. Defines the number of different tokens that can be represented by the
            `inputs_ids` passed when calling [`BioGptModel`].
        hidden_size (`int`, *optional*, defaults to 1024):
            Dimension of the encoder layers and the pooler layer.
        num_hidden_layers (`int`, *optional*, defaults to 24):
            Number of hidden layers in the Transformer encoder.
        num_attention_heads (`int`, *optional*, defaults to 16):
            Number of attention heads for each attention layer in the Transformer encoder.
        intermediate_size (`int`, *optional*, defaults to 4096):
            Dimension of the "intermediate" (i.e., feed-forward) layer in the Transformer encoder.
        hidden_act (`str` or `function`, *optional*, defaults to `"gelu"`):
            The non-linear activation function (function or string) in the encoder and pooler. If string, `"gelu"`,
            `"relu"`, `"selu"` and `"gelu_new"` are supported.
        hidden_dropout_prob (`float`, *optional*, defaults to 0.1):
            The dropout probabilitiy for all fully connected layers in the embeddings, encoder, and pooler.
        attention_probs_dropout_prob (`float`, *optional*, defaults to 0.1):
            The dropout ratio for the attention probabilities.
        max_position_embeddings (`int`, *optional*, defaults to 1024):
            The maximum sequence length that this model might ever be used with. Typically set this to something large
            just in case (e.g., 512 or 1024 or 2048).
        initializer_range (`float`, *optional*, defaults to 0.02):
            The standard deviation of the truncated_normal_initializer for initializing all weight matrices.
        layer_norm_eps (`float`, *optional*, defaults to 1e-12):
            The epsilon used by the layer normalization layers.
        scale_embedding (`bool`, *optional*, defaults to `True`):
            Scale embeddings by diving by sqrt(d_model).
        use_cache (`bool`, *optional*, defaults to `True`):
            Whether or not the model should return the last key/values attentions (not used by all models). Only
            relevant if `config.is_decoder=True`.
        is_encoder_decoder (`bool`, *optional*, defaults to `False`):
            Whether this is an encoder/decoder model.
        layerdrop (`float`, *optional*, defaults to 0.0):
            Please refer to the paper about LayerDrop: https://arxiv.org/abs/1909.11556 for further details
        activation_dropout (`float`, *optional*, defaults to 0.0):
            The dropout ratio for activations inside the fully connected layer.
        pad_token_id (`int`, *optional*, defaults to 1)
            Padding token id.
        bos_token_id (`int`, *optional*, defaults to 0)
            Beginning of stream token id.
        eos_token_id (`int`, *optional*, defaults to 2)
            End of stream token id.
        Example:

    ```python
    >>> from transformers import BioGptModel, BioGptConfig

    >>> # Initializing a BioGPT microsoft/biogpt style configuration
    >>> configuration = BioGptConfig()

    >>> # Initializing a model from the microsoft/biogpt style configuration
    >>> model = BioGptModel(configuration)

    >>> # Accessing the model configuration
    >>> configuration = model.config
    ```'''
    model_type: str
    vocab_size: Incomplete
    max_position_embeddings: Incomplete
    hidden_size: Incomplete
    num_hidden_layers: Incomplete
    num_attention_heads: Incomplete
    intermediate_size: Incomplete
    hidden_act: Incomplete
    hidden_dropout_prob: Incomplete
    attention_probs_dropout_prob: Incomplete
    initializer_range: Incomplete
    layer_norm_eps: Incomplete
    scale_embedding: Incomplete
    use_cache: Incomplete
    is_encoder_decoder: Incomplete
    layerdrop: Incomplete
    activation_dropout: Incomplete
    def __init__(self, vocab_size: int = 42384, hidden_size: int = 1024, num_hidden_layers: int = 24, num_attention_heads: int = 16, intermediate_size: int = 4096, hidden_act: str = 'gelu', hidden_dropout_prob: float = 0.1, attention_probs_dropout_prob: float = 0.1, max_position_embeddings: int = 1024, initializer_range: float = 0.02, layer_norm_eps: float = 1e-12, scale_embedding: bool = True, use_cache: bool = True, is_encoder_decoder: bool = False, layerdrop: float = 0.0, activation_dropout: float = 0.0, pad_token_id: int = 1, bos_token_id: int = 0, eos_token_id: int = 2, **kwargs) -> None: ...
