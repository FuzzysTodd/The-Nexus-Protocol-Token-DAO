from _typeshed import Incomplete
from transformers import PretrainedConfig as PretrainedConfig

NEZHA_PRETRAINED_CONFIG_ARCHIVE_MAP: Incomplete

class NezhaConfig(PretrainedConfig):
    '''
    This is the configuration class to store the configuration of an [`NezhaModel`]. It is used to instantiate an Nezha
    model according to the specified arguments, defining the model architecture. Instantiating a configuration with the
    defaults will yield a similar configuration to that of the Nezha
    [sijunhe/nezha-cn-base](https://huggingface.co/sijunhe/nezha-cn-base) architecture.

    Configuration objects inherit from [`PretrainedConfig`] and can be used to control the model outputs. Read the
    documentation from [`PretrainedConfig`] for more information.


    Args:
        vocab_size (`int`, optional, defaults to 21128):
            Vocabulary size of the NEZHA model. Defines the different tokens that can be represented by the
            *inputs_ids* passed to the forward method of [`NezhaModel`].
        embedding_size (`int`, optional, defaults to 128):
            Dimensionality of vocabulary embeddings.
        hidden_size (`int`, optional, defaults to 768):
            Dimensionality of the encoder layers and the pooler layer.
        num_hidden_layers (`int`, optional, defaults to 12):
            Number of hidden layers in the Transformer encoder.
        num_attention_heads (`int`, optional, defaults to 12):
            Number of attention heads for each attention layer in the Transformer encoder.
        intermediate_size (`int`, optional, defaults to 3072):
            The dimensionality of the "intermediate" (i.e., feed-forward) layer in the Transformer encoder.
        hidden_act (`str` or `function`, optional, defaults to "gelu"):
            The non-linear activation function (function or string) in the encoder and pooler.
        hidden_dropout_prob (`float`, optional, defaults to 0.1):
            The dropout probability for all fully connected layers in the embeddings, encoder, and pooler.
        attention_probs_dropout_prob (`float`, optional, defaults to 0.1):
            The dropout ratio for the attention probabilities.
        max_position_embeddings (`int`, optional, defaults to 512):
            The maximum sequence length that this model might ever be used with. Typically set this to something large
            (e.g., 512 or 1024 or 2048).
        type_vocab_size (`int`, optional, defaults to 2):
            The vocabulary size of the *token_type_ids* passed into [`NezhaModel`].
        initializer_range (`float`, optional, defaults to 0.02):
            The standard deviation of the truncated_normal_initializer for initializing all weight matrices.
        layer_norm_eps (`float`, optional, defaults to 1e-12):
            The epsilon used by the layer normalization layers.
        classifier_dropout (`float`, optional, defaults to 0.1):
            The dropout ratio for attached classifiers.
        is_decoder (`bool`, *optional*, defaults to `False`):
            Whether the model is used as a decoder or not. If `False`, the model is used as an encoder.

    Example:

    ```python
    >>> from transformers import NezhaConfig, NezhaModel

    >>> # Initializing an Nezha configuration
    >>> configuration = NezhaConfig()

    >>> # Initializing a model (with random weights) from the Nezha-base style configuration model
    >>> model = NezhaModel(configuration)

    >>> # Accessing the model configuration
    >>> configuration = model.config
    ```'''
    pretrained_config_archive_map = NEZHA_PRETRAINED_CONFIG_ARCHIVE_MAP
    model_type: str
    vocab_size: Incomplete
    embedding_size: Incomplete
    hidden_size: Incomplete
    num_hidden_layers: Incomplete
    num_attention_heads: Incomplete
    hidden_act: Incomplete
    intermediate_size: Incomplete
    hidden_dropout_prob: Incomplete
    attention_probs_dropout_prob: Incomplete
    max_position_embeddings: Incomplete
    max_relative_position: Incomplete
    type_vocab_size: Incomplete
    initializer_range: Incomplete
    layer_norm_eps: Incomplete
    classifier_dropout: Incomplete
    use_cache: Incomplete
    def __init__(self, vocab_size: int = 21128, embedding_size: int = 128, hidden_size: int = 768, num_hidden_layers: int = 12, num_attention_heads: int = 12, intermediate_size: int = 3072, hidden_act: str = 'gelu', hidden_dropout_prob: float = 0.1, attention_probs_dropout_prob: float = 0.1, max_position_embeddings: int = 512, max_relative_position: int = 64, type_vocab_size: int = 2, initializer_range: float = 0.02, layer_norm_eps: float = 1e-12, classifier_dropout: float = 0.1, pad_token_id: int = 0, bos_token_id: int = 2, eos_token_id: int = 3, use_cache: bool = True, **kwargs) -> None: ...
