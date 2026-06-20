from ...configuration_utils import PretrainedConfig as PretrainedConfig
from ...utils import logging as logging
from _typeshed import Incomplete

logger: Incomplete
MVP_PRETRAINED_CONFIG_ARCHIVE_MAP: Incomplete

class MvpConfig(PretrainedConfig):
    '''
    This is the configuration class to store the configuration of a [`MvpModel`]. It is used to instantiate a MVP model
    according to the specified arguments, defining the model architecture. Instantiating a configuration with the
    defaults will yield a similar configuration to that of the MVP [RUCAIBox/mvp](https://huggingface.co/RUCAIBox/mvp)
    architecture.

    Configuration objects inherit from [`PretrainedConfig`] and can be used to control the model outputs. Read the
    documentation from [`PretrainedConfig`] for more information.


    Args:
        vocab_size (`int`, *optional*, defaults to 50267):
            Vocabulary size of the MVP model. Defines the number of different tokens that can be represented by the
            `inputs_ids` passed when calling [`MvpModel`].
        d_model (`int`, *optional*, defaults to 1024):
            Dimensionality of the layers and the pooler layer.
        encoder_layers (`int`, *optional*, defaults to 12):
            Number of encoder layers.
        decoder_layers (`int`, *optional*, defaults to 12):
            Number of decoder layers.
        encoder_attention_heads (`int`, *optional*, defaults to 16):
            Number of attention heads for each attention layer in the Transformer encoder.
        decoder_attention_heads (`int`, *optional*, defaults to 16):
            Number of attention heads for each attention layer in the Transformer decoder.
        decoder_ffn_dim (`int`, *optional*, defaults to 4096):
            Dimensionality of the "intermediate" (often named feed-forward) layer in decoder.
        encoder_ffn_dim (`int`, *optional*, defaults to 4096):
            Dimensionality of the "intermediate" (often named feed-forward) layer in decoder.
        activation_function (`str` or `function`, *optional*, defaults to `"gelu"`):
            The non-linear activation function (function or string) in the encoder and pooler. If string, `"gelu"`,
            `"relu"`, `"silu"` and `"gelu_new"` are supported.
        dropout (`float`, *optional*, defaults to 0.1):
            The dropout probability for all fully connected layers in the embeddings, encoder, and pooler.
        attention_dropout (`float`, *optional*, defaults to 0.0):
            The dropout ratio for the attention probabilities.
        activation_dropout (`float`, *optional*, defaults to 0.0):
            The dropout ratio for activations inside the fully connected layer.
        classifier_dropout (`float`, *optional*, defaults to 0.0):
            The dropout ratio for classifier.
        max_position_embeddings (`int`, *optional*, defaults to 1024):
            The maximum sequence length that this model might ever be used with. Typically set this to something large
            just in case (e.g., 512 or 1024 or 2048).
        init_std (`float`, *optional*, defaults to 0.02):
            The standard deviation of the truncated_normal_initializer for initializing all weight matrices.
        encoder_layerdrop (`float`, *optional*, defaults to 0.0):
            The LayerDrop probability for the encoder. See the [LayerDrop paper](see https://arxiv.org/abs/1909.11556)
            for more details.
        decoder_layerdrop (`float`, *optional*, defaults to 0.0):
            The LayerDrop probability for the decoder. See the [LayerDrop paper](see https://arxiv.org/abs/1909.11556)
            for more details.
        scale_embedding (`bool`, *optional*, defaults to `False`):
            Scale embeddings by diving by sqrt(d_model).
        use_cache (`bool`, *optional*, defaults to `True`):
            Whether or not the model should return the last key/values attentions (not used by all models).
        forced_eos_token_id (`int`, *optional*, defaults to 2):
            The id of the token to force as the last generated token when `max_length` is reached. Usually set to
            `eos_token_id`.
        use_prompt (`bool`, *optional*, defaults to `False`):
            Whether or not to use prompt.
        prompt_length (`int`, *optional*, defaults to 100):
            The length of prompt.
        prompt_mid_dim (`int`, *optional*, defaults to 800):
            Dimensionality of the "intermediate" layer in prompt.
    Example:

    ```python
    >>> from transformers import MvpModel, MvpConfig

    >>> # Initializing a MVP RUCAIBox/mvp style configuration
    >>> configuration = MvpConfig()

    >>> # Initializing a model from the RUCAIBox/mvp style configuration
    >>> model = MvpModel(configuration)

    >>> # Accessing the model configuration
    >>> configuration = model.config
    ```'''
    model_type: str
    keys_to_ignore_at_inference: Incomplete
    attribute_map: Incomplete
    vocab_size: Incomplete
    max_position_embeddings: Incomplete
    d_model: Incomplete
    encoder_ffn_dim: Incomplete
    encoder_layers: Incomplete
    encoder_attention_heads: Incomplete
    decoder_ffn_dim: Incomplete
    decoder_layers: Incomplete
    decoder_attention_heads: Incomplete
    dropout: Incomplete
    attention_dropout: Incomplete
    activation_dropout: Incomplete
    activation_function: Incomplete
    init_std: Incomplete
    encoder_layerdrop: Incomplete
    decoder_layerdrop: Incomplete
    classifier_dropout: Incomplete
    use_cache: Incomplete
    num_hidden_layers: Incomplete
    scale_embedding: Incomplete
    use_prompt: Incomplete
    prompt_length: Incomplete
    prompt_mid_dim: Incomplete
    forced_bos_token_id: Incomplete
    def __init__(self, vocab_size: int = 50267, max_position_embeddings: int = 1024, encoder_layers: int = 12, encoder_ffn_dim: int = 4096, encoder_attention_heads: int = 16, decoder_layers: int = 12, decoder_ffn_dim: int = 4096, decoder_attention_heads: int = 16, encoder_layerdrop: float = 0.0, decoder_layerdrop: float = 0.0, activation_function: str = 'gelu', d_model: int = 1024, dropout: float = 0.1, attention_dropout: float = 0.0, activation_dropout: float = 0.0, init_std: float = 0.02, classifier_dropout: float = 0.0, scale_embedding: bool = False, use_cache: bool = True, pad_token_id: int = 1, bos_token_id: int = 0, eos_token_id: int = 2, is_encoder_decoder: bool = True, decoder_start_token_id: int = 2, forced_eos_token_id: int = 2, use_prompt: bool = False, prompt_length: int = 100, prompt_mid_dim: int = 800, **kwargs) -> None: ...
