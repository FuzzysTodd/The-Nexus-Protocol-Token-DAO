from ...configuration_utils import PretrainedConfig as PretrainedConfig
from ...onnx import OnnxConfig as OnnxConfig
from ...utils import logging as logging
from _typeshed import Incomplete
from typing import Mapping

logger: Incomplete
ROFORMER_PRETRAINED_CONFIG_ARCHIVE_MAP: Incomplete

class RoFormerConfig(PretrainedConfig):
    '''
    This is the configuration class to store the configuration of a [`RoFormerModel`]. It is used to instantiate an
    RoFormer model according to the specified arguments, defining the model architecture. Instantiating a configuration
    with the defaults will yield a similar configuration to that of the RoFormer
    [junnyu/roformer_chinese_base](https://huggingface.co/junnyu/roformer_chinese_base) architecture.

    Configuration objects inherit from [`PretrainedConfig`] and can be used to control the model outputs. Read the
    documentation from [`PretrainedConfig`] for more information.


    Args:
        vocab_size (`int`, *optional*, defaults to 50000):
            Vocabulary size of the RoFormer model. Defines the number of different tokens that can be represented by
            the `inputs_ids` passed when calling [`RoFormerModel`] or [`TFRoFormerModel`].
        embedding_size (`int`, *optional*, defaults to None):
            Dimensionality of the encoder layers and the pooler layer. Defaults to the `hidden_size` if not provided.
        hidden_size (`int`, *optional*, defaults to 768):
            Dimension of the encoder layers and the pooler layer.
        num_hidden_layers (`int`, *optional*, defaults to 12):
            Number of hidden layers in the Transformer encoder.
        num_attention_heads (`int`, *optional*, defaults to 12):
            Number of attention heads for each attention layer in the Transformer encoder.
        intermediate_size (`int`, *optional*, defaults to 3072):
            Dimension of the "intermediate" (i.e., feed-forward) layer in the Transformer encoder.
        hidden_act (`str` or `function`, *optional*, defaults to `"gelu"`):
            The non-linear activation function (function or string) in the encoder and pooler. If string, `"gelu"`,
            `"relu"`, `"selu"` and `"gelu_new"` are supported.
        hidden_dropout_prob (`float`, *optional*, defaults to 0.1):
            The dropout probabilitiy for all fully connected layers in the embeddings, encoder, and pooler.
        attention_probs_dropout_prob (`float`, *optional*, defaults to 0.1):
            The dropout ratio for the attention probabilities.
        max_position_embeddings (`int`, *optional*, defaults to 1536):
            The maximum sequence length that this model might ever be used with. Typically set this to something large
            just in case (e.g., 512 or 1024 or 1536).
        type_vocab_size (`int`, *optional*, defaults to 2):
            The vocabulary size of the `token_type_ids` passed when calling [`RoFormerModel`] or [`TFRoFormerModel`].
        initializer_range (`float`, *optional*, defaults to 0.02):
            The standard deviation of the truncated_normal_initializer for initializing all weight matrices.
        layer_norm_eps (`float`, *optional*, defaults to 1e-12):
            The epsilon used by the layer normalization layers.
        is_decoder (`bool`, *optional*, defaults to `False`):
            Whether the model is used as a decoder or not. If `False`, the model is used as an encoder.
        use_cache (`bool`, *optional*, defaults to `True`):
            Whether or not the model should return the last key/values attentions (not used by all models). Only
            relevant if `config.is_decoder=True`.
        rotary_value (`bool`, *optional*, defaults to `False`):
            Whether or not apply rotary position embeddings on value layer.

    Example:

    ```python
    >>> from transformers import RoFormerModel, RoFormerConfig

    >>> # Initializing a RoFormer junnyu/roformer_chinese_base style configuration
    >>> configuration = RoFormerConfig()

    >>> # Initializing a model from the junnyu/roformer_chinese_base style configuration
    >>> model = RoFormerModel(configuration)

    >>> # Accessing the model configuration
    >>> configuration = model.config
    ```'''
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
    type_vocab_size: Incomplete
    initializer_range: Incomplete
    layer_norm_eps: Incomplete
    rotary_value: Incomplete
    use_cache: Incomplete
    def __init__(self, vocab_size: int = 50000, embedding_size: Incomplete | None = None, hidden_size: int = 768, num_hidden_layers: int = 12, num_attention_heads: int = 12, intermediate_size: int = 3072, hidden_act: str = 'gelu', hidden_dropout_prob: float = 0.1, attention_probs_dropout_prob: float = 0.1, max_position_embeddings: int = 1536, type_vocab_size: int = 2, initializer_range: float = 0.02, layer_norm_eps: float = 1e-12, pad_token_id: int = 0, rotary_value: bool = False, use_cache: bool = True, **kwargs) -> None: ...

class RoFormerOnnxConfig(OnnxConfig):
    @property
    def inputs(self) -> Mapping[str, Mapping[int, str]]: ...
