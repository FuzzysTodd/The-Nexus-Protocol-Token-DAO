from ...configuration_utils import PretrainedConfig as PretrainedConfig
from ...utils import logging as logging
from _typeshed import Incomplete

logger: Incomplete
SPEECH_TO_TEXT_2_PRETRAINED_CONFIG_ARCHIVE_MAP: Incomplete

class Speech2Text2Config(PretrainedConfig):
    '''
    This is the configuration class to store the configuration of a [`Speech2Text2ForCausalLM`]. It is used to
    instantiate an Speech2Text2 model according to the specified arguments, defining the model architecture.
    Instantiating a configuration with the defaults will yield a similar configuration to that of the Speech2Text2
    [facebook/s2t-wav2vec2-large-en-de](https://huggingface.co/facebook/s2t-wav2vec2-large-en-de) architecture.

    Configuration objects inherit from [`PretrainedConfig`] and can be used to control the model outputs. Read the
    documentation from [`PretrainedConfig`] for more information.


    Args:
        vocab_size (`int`, *optional*, defaults to 50265):
            Vocabulary size of the Speech2Text model. Defines the number of different tokens that can be represented by
            the `inputs_ids` passed when calling [`Speech2TextModel`]
        d_model (`int`, *optional*, defaults to 1024):
            Dimensionality of the layers and the pooler layer.
        decoder_layers (`int`, *optional*, defaults to 12):
            Number of decoder layers.
        decoder_attention_heads (`int`, *optional*, defaults to 16):
            Number of attention heads for each attention layer in the Transformer decoder.
        decoder_ffn_dim (`int`, *optional*, defaults to 4096):
            Dimensionality of the "intermediate" (often named feed-forward) layer in decoder.
        activation_function (`str` or `function`, *optional*, defaults to `"gelu"`):
            The non-linear activation function (function or string) in the pooler. If string, `"gelu"`, `"relu"`,
            `"silu"` and `"gelu_new"` are supported.
        dropout (`float`, *optional*, defaults to 0.1):
            The dropout probability for all fully connected layers in the embeddings, and pooler.
        attention_dropout (`float`, *optional*, defaults to 0.0):
            The dropout ratio for the attention probabilities.
        activation_dropout (`float`, *optional*, defaults to 0.0):
            The dropout ratio for activations inside the fully connected layer.
        init_std (`float`, *optional*, defaults to 0.02):
            The standard deviation of the truncated_normal_initializer for initializing all weight matrices.
            https://arxiv.org/abs/1909.11556>`__ for more details.
        decoder_layerdrop (`float`, *optional*, defaults to 0.0):
            The LayerDrop probability for the decoder. See the [LayerDrop paper](see https://arxiv.org/abs/1909.11556)
            for more details.
        use_cache (`bool`, *optional*, defaults to `True`):
            Whether or not the model should return the last key/values attentions (not used by all models).
        max_target_positions (`int`, *optional*, defaults to 1024):
            The maximum sequence length that this model might ever be used with. Typically set this to something large
            just in case (e.g., 512 or 1024 or 2048).

    Example:

    ```python
    >>> from transformers import Speech2Text2Config, Speech2Text2ForCausalLM

    >>> # Initializing a Speech2Text2 s2t_transformer_s style configuration
    >>> configuration = Speech2Text2Config()

    >>> # Initializing a model (with random weights) from the s2t_transformer_s style configuration
    >>> model = Speech2Text2ForCausalLM(configuration)

    >>> # Accessing the model configuration
    >>> configuration = model.config
    ```'''
    model_type: str
    keys_to_ignore_at_inference: Incomplete
    attribute_map: Incomplete
    vocab_size: Incomplete
    d_model: Incomplete
    decoder_ffn_dim: Incomplete
    decoder_layers: Incomplete
    decoder_attention_heads: Incomplete
    dropout: Incomplete
    attention_dropout: Incomplete
    activation_dropout: Incomplete
    activation_function: Incomplete
    init_std: Incomplete
    decoder_layerdrop: Incomplete
    use_cache: Incomplete
    num_hidden_layers: Incomplete
    scale_embedding: Incomplete
    max_target_positions: Incomplete
    def __init__(self, vocab_size: int = 10000, decoder_layers: int = 6, decoder_ffn_dim: int = 2048, decoder_attention_heads: int = 4, decoder_layerdrop: float = 0.0, use_cache: bool = True, activation_function: str = 'relu', d_model: int = 256, dropout: float = 0.1, attention_dropout: float = 0.0, activation_dropout: float = 0.0, init_std: float = 0.02, decoder_start_token_id: int = 2, scale_embedding: bool = True, pad_token_id: int = 1, bos_token_id: int = 0, eos_token_id: int = 2, max_target_positions: int = 1024, **kwargs) -> None: ...
