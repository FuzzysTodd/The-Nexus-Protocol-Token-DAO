from ...configuration_utils import PretrainedConfig as PretrainedConfig
from ...utils import logging as logging
from _typeshed import Incomplete

logger: Incomplete
GPT_NEOX_JAPANESE_PRETRAINED_CONFIG_ARCHIVE_MAP: Incomplete

class GPTNeoXJapaneseConfig(PretrainedConfig):
    '''
    This is the configuration class to store the configuration of a [`GPTNeoXModelJapanese`]. It is used to instantiate
    a GPTNeoX model according to the specified arguments, defining the model architecture. Instantiating a
    configuration with the defaults will yield a similar configuration to that of the GPTNeoXJapanese
    [abeja/gpt-neox-japanese-2.7b](https://huggingface.co/abeja/gpt-neox-japanese-2.7b) architecture.

    Configuration objects inherit from [`PretrainedConfig`] and can be used to control the model outputs. Read the
    documentation from [`PretrainedConfig`] for more information. Default configs is set as 2.7B model

    Args:
        vocab_size (`int`, *optional*, defaults to 32000):
            Vocabulary size of the GPTNeoXJapanese model. Defines the number of different tokens that can be
            represented by the `inputs_ids` passed when calling [`GPTNeoXJapanese`].
        hidden_size (`int`, *optional*, defaults to 2560):
            Dimension of the encoder layers and the pooler layer.
        num_hidden_layers (`int`, *optional*, defaults to 32):
            Number of hidden layers in the Transformer encoder.
        num_attention_heads (`int`, *optional*, defaults to 32):
            Number of attention heads for each attention layer in the Transformer encoder.
        intermediate_multiple_size (`int`, *optional*, defaults to 4):
            Dimension of the "intermediate" layer in the Transformer encoder is calculated by hidden_size *
            intermediate_multiple_size.
        hidden_act (`str` or `function`, *optional*, defaults to `"gelu"`):
            The non-linear activation function (function or string) in the encoder and pooler.
        rotary_pct (`float`, *optional*, defaults to 1.00):
            percentage of hidden dimensions to allocate to rotary embeddings
        rotary_emb_base (`int`, *optional*, defaults to 10000)
            base for computing rotary embeddings frequency
        max_position_embeddings (`int`, *optional*, defaults to 2048):
            The maximum sequence length that this model might ever be used with.
        initializer_range (`float`, *optional*, defaults to 0.02):
            The standard deviation of the truncated_normal_initializer for initializing all weight matrices.
        layer_norm_eps (`float`, *optional*, defaults to 1e-5):
            The epsilon used by the layer normalization layers.
        use_cache (`bool`, *optional*, defaults to `True`):
            Whether or not the model should return the last key/values attentions (not used by all models). Only
            relevant if `config.is_decoder=True`.
        weight_tying (`bool`, *optional*, defaults to `True`):
            Whhether or not use weight tying between input and output embedding weight
        attention_dropout (`float`, *optional*, defaults to 0.1):
            The dropout ratio for the attention.
        hidden_dropout (`float`, *optional*, defaults to 0.0):
            The dropout ratio for the hidden layer.
        Example:

    ```python
    >>> from transformers import GPTNeoXJapaneseConfig, GPTNeoXJapaneseModel

    >>> # Initializing a GPTNeoXJapanese gpt-neox-japanese-2.7b style configuration
    >>> configuration = GPTNeoXJapaneseConfig()

    >>> # Initializing a model (with random weights) from the gpt-neox-japanese-2.7b style configuration
    >>> model = GPTNeoXJapaneseModel(configuration)

    >>> # Accessing the model configuration
    >>> configuration = model.config
    ```'''
    model_type: str
    vocab_size: Incomplete
    max_position_embeddings: Incomplete
    hidden_size: Incomplete
    num_hidden_layers: Incomplete
    num_attention_heads: Incomplete
    intermediate_multiple_size: Incomplete
    hidden_act: Incomplete
    rotary_pct: Incomplete
    rotary_emb_base: Incomplete
    initializer_range: Incomplete
    layer_norm_eps: Incomplete
    use_cache: Incomplete
    weight_tying: Incomplete
    attention_dropout: Incomplete
    hidden_dropout: Incomplete
    def __init__(self, vocab_size: int = 32000, hidden_size: int = 2560, num_hidden_layers: int = 32, num_attention_heads: int = 32, intermediate_multiple_size: int = 4, hidden_act: str = 'gelu', rotary_pct: float = 1.0, rotary_emb_base: int = 10000, max_position_embeddings: int = 2048, initializer_range: float = 0.02, layer_norm_eps: float = 1e-05, use_cache: bool = True, bos_token_id: int = 31996, eos_token_id: int = 31999, weight_tying: bool = True, attention_dropout: float = 0.1, hidden_dropout: float = 0.0, **kwargs) -> None: ...
