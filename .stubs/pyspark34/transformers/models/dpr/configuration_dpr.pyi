from ...configuration_utils import PretrainedConfig as PretrainedConfig
from ...utils import logging as logging
from _typeshed import Incomplete

logger: Incomplete
DPR_PRETRAINED_CONFIG_ARCHIVE_MAP: Incomplete

class DPRConfig(PretrainedConfig):
    '''
    [`DPRConfig`] is the configuration class to store the configuration of a *DPRModel*.

    This is the configuration class to store the configuration of a [`DPRContextEncoder`], [`DPRQuestionEncoder`], or a
    [`DPRReader`]. It is used to instantiate the components of the DPR model according to the specified arguments,
    defining the model component architectures. Instantiating a configuration with the defaults will yield a similar
    configuration to that of the DPRContextEncoder
    [facebook/dpr-ctx_encoder-single-nq-base](https://huggingface.co/facebook/dpr-ctx_encoder-single-nq-base)
    architecture.

    This class is a subclass of [`BertConfig`]. Please check the superclass for the documentation of all kwargs.

    Args:
        vocab_size (`int`, *optional*, defaults to 30522):
            Vocabulary size of the DPR model. Defines the different tokens that can be represented by the *inputs_ids*
            passed to the forward method of [`BertModel`].
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
            `"relu"`, `"silu"` and `"gelu_new"` are supported.
        hidden_dropout_prob (`float`, *optional*, defaults to 0.1):
            The dropout probability for all fully connected layers in the embeddings, encoder, and pooler.
        attention_probs_dropout_prob (`float`, *optional*, defaults to 0.1):
            The dropout ratio for the attention probabilities.
        max_position_embeddings (`int`, *optional*, defaults to 512):
            The maximum sequence length that this model might ever be used with. Typically set this to something large
            just in case (e.g., 512 or 1024 or 2048).
        type_vocab_size (`int`, *optional*, defaults to 2):
            The vocabulary size of the *token_type_ids* passed into [`BertModel`].
        initializer_range (`float`, *optional*, defaults to 0.02):
            The standard deviation of the truncated_normal_initializer for initializing all weight matrices.
        layer_norm_eps (`float`, *optional*, defaults to 1e-12):
            The epsilon used by the layer normalization layers.
        position_embedding_type (`str`, *optional*, defaults to `"absolute"`):
            Type of position embedding. Choose one of `"absolute"`, `"relative_key"`, `"relative_key_query"`. For
            positional embeddings use `"absolute"`. For more information on `"relative_key"`, please refer to
            [Self-Attention with Relative Position Representations (Shaw et al.)](https://arxiv.org/abs/1803.02155).
            For more information on `"relative_key_query"`, please refer to *Method 4* in [Improve Transformer Models
            with Better Relative Position Embeddings (Huang et al.)](https://arxiv.org/abs/2009.13658).
        projection_dim (`int`, *optional*, defaults to 0):
            Dimension of the projection for the context and question encoders. If it is set to zero (default), then no
            projection is done.

    Example:

    ```python
    >>> from transformers import DPRConfig, DPRContextEncoder

    >>> # Initializing a DPR facebook/dpr-ctx_encoder-single-nq-base style configuration
    >>> configuration = DPRConfig()

    >>> # Initializing a model (with random weights) from the facebook/dpr-ctx_encoder-single-nq-base style configuration
    >>> model = DPRContextEncoder(configuration)

    >>> # Accessing the model configuration
    >>> configuration = model.config
    ```'''
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
    projection_dim: Incomplete
    position_embedding_type: Incomplete
    def __init__(self, vocab_size: int = 30522, hidden_size: int = 768, num_hidden_layers: int = 12, num_attention_heads: int = 12, intermediate_size: int = 3072, hidden_act: str = 'gelu', hidden_dropout_prob: float = 0.1, attention_probs_dropout_prob: float = 0.1, max_position_embeddings: int = 512, type_vocab_size: int = 2, initializer_range: float = 0.02, layer_norm_eps: float = 1e-12, pad_token_id: int = 0, position_embedding_type: str = 'absolute', projection_dim: int = 0, **kwargs) -> None: ...
