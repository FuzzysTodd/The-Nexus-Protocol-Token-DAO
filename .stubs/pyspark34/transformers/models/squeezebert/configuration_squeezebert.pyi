from ...configuration_utils import PretrainedConfig as PretrainedConfig
from ...onnx import OnnxConfig as OnnxConfig
from ...utils import logging as logging
from _typeshed import Incomplete
from typing import Mapping

logger: Incomplete
SQUEEZEBERT_PRETRAINED_CONFIG_ARCHIVE_MAP: Incomplete

class SqueezeBertConfig(PretrainedConfig):
    '''
    This is the configuration class to store the configuration of a [`SqueezeBertModel`]. It is used to instantiate a
    SqueezeBERT model according to the specified arguments, defining the model architecture. Instantiating a
    configuration with the defaults will yield a similar configuration to that of the SqueezeBERT
    [squeezebert/squeezebert-uncased](https://huggingface.co/squeezebert/squeezebert-uncased) architecture.

    Configuration objects inherit from [`PretrainedConfig`] and can be used to control the model outputs. Read the
    documentation from [`PretrainedConfig`] for more information.


    Args:
        vocab_size (`int`, *optional*, defaults to 30522):
            Vocabulary size of the SqueezeBERT model. Defines the number of different tokens that can be represented by
            the `inputs_ids` passed when calling [`SqueezeBertModel`].
        hidden_size (`int`, *optional*, defaults to 768):
            Dimensionality of the encoder layers and the pooler layer.
        num_hidden_layers (`int`, *optional*, defaults to 12):
            Number of hidden layers in the Transformer encoder.
        num_attention_heads (`int`, *optional*, defaults to 12):
            Number of attention heads for each attention layer in the Transformer encoder.
        intermediate_size (`int`, *optional*, defaults to 3072):
            Dimensionality of the "intermediate" (often named feed-forward) layer in the Transformer encoder.
        hidden_act (`str` or `Callable`, *optional*, defaults to `"gelu"`):
            The non-linear activation function (function or string) in the encoder and pooler. If string, `"gelu"`,
            `"relu"`, `"silu"` and `"gelu_new"` are supported.
        hidden_dropout_prob (`float`, *optional*, defaults to 0.1):
            The dropout probability for all fully connected layers in the embeddings, encoder, and pooler.
        attention_probs_dropout_prob (`float`, *optional*, defaults to 0.1):
            The dropout ratio for the attention probabilities.
        max_position_embeddings (`int`, *optional*, defaults to 512):
            The maximum sequence length that this model might ever be used with. Typically set this to something large
            just in case (e.g., 512 or 1024 or 2048).
        type_vocab_size (`int`, *optional*, defaults to 2):
            The vocabulary size of the `token_type_ids` passed when calling [`BertModel`] or [`TFBertModel`].
        initializer_range (`float`, *optional*, defaults to 0.02):
            The standard deviation of the truncated_normal_initializer for initializing all weight matrices.
        layer_norm_eps (`float`, *optional*, defaults to 1e-12):

        pad_token_id (`int`, *optional*, defaults to 0):
            The ID of the token in the word embedding to use as padding.
        embedding_size (`int`, *optional*, defaults to 768):
            The dimension of the word embedding vectors.

        q_groups (`int`, *optional*, defaults to 4):
            The number of groups in Q layer.
        k_groups (`int`, *optional*, defaults to 4):
            The number of groups in K layer.
        v_groups (`int`, *optional*, defaults to 4):
            The number of groups in V layer.
        post_attention_groups (`int`, *optional*, defaults to 1):
            The number of groups in the first feed forward network layer.
        intermediate_groups (`int`, *optional*, defaults to 4):
            The number of groups in the second feed forward network layer.
        output_groups (`int`, *optional*, defaults to 4):
            The number of groups in the third feed forward network layer.

    Examples:

    ```python
    >>> from transformers import SqueezeBertConfig, SqueezeBertModel

    >>> # Initializing a SqueezeBERT configuration
    >>> configuration = SqueezeBertConfig()

    >>> # Initializing a model (with random weights) from the configuration above
    >>> model = SqueezeBertModel(configuration)

    >>> # Accessing the model configuration
    >>> configuration = model.config
    ```

    Attributes: pretrained_config_archive_map (Dict[str, str]): A dictionary containing all the available pre-trained
    checkpoints.
    '''
    pretrained_config_archive_map = SQUEEZEBERT_PRETRAINED_CONFIG_ARCHIVE_MAP
    model_type: str
    vocab_size: Incomplete
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
    embedding_size: Incomplete
    q_groups: Incomplete
    k_groups: Incomplete
    v_groups: Incomplete
    post_attention_groups: Incomplete
    intermediate_groups: Incomplete
    output_groups: Incomplete
    def __init__(self, vocab_size: int = 30522, hidden_size: int = 768, num_hidden_layers: int = 12, num_attention_heads: int = 12, intermediate_size: int = 3072, hidden_act: str = 'gelu', hidden_dropout_prob: float = 0.1, attention_probs_dropout_prob: float = 0.1, max_position_embeddings: int = 512, type_vocab_size: int = 2, initializer_range: float = 0.02, layer_norm_eps: float = 1e-12, pad_token_id: int = 0, embedding_size: int = 768, q_groups: int = 4, k_groups: int = 4, v_groups: int = 4, post_attention_groups: int = 1, intermediate_groups: int = 4, output_groups: int = 4, **kwargs) -> None: ...

class SqueezeBertOnnxConfig(OnnxConfig):
    @property
    def inputs(self) -> Mapping[str, Mapping[int, str]]: ...
