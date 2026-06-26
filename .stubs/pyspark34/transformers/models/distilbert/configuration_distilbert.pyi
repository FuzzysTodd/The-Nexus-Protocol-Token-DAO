from ...configuration_utils import PretrainedConfig as PretrainedConfig
from ...onnx import OnnxConfig as OnnxConfig
from ...utils import logging as logging
from _typeshed import Incomplete
from typing import Mapping

logger: Incomplete
DISTILBERT_PRETRAINED_CONFIG_ARCHIVE_MAP: Incomplete

class DistilBertConfig(PretrainedConfig):
    '''
    This is the configuration class to store the configuration of a [`DistilBertModel`] or a [`TFDistilBertModel`]. It
    is used to instantiate a DistilBERT model according to the specified arguments, defining the model architecture.
    Instantiating a configuration with the defaults will yield a similar configuration to that of the DistilBERT
    [distilbert-base-uncased](https://huggingface.co/distilbert-base-uncased) architecture.

    Configuration objects inherit from [`PretrainedConfig`] and can be used to control the model outputs. Read the
    documentation from [`PretrainedConfig`] for more information.

    Args:
        vocab_size (`int`, *optional*, defaults to 30522):
            Vocabulary size of the DistilBERT model. Defines the number of different tokens that can be represented by
            the `inputs_ids` passed when calling [`DistilBertModel`] or [`TFDistilBertModel`].
        max_position_embeddings (`int`, *optional*, defaults to 512):
            The maximum sequence length that this model might ever be used with. Typically set this to something large
            just in case (e.g., 512 or 1024 or 2048).
        sinusoidal_pos_embds (`boolean`, *optional*, defaults to `False`):
            Whether to use sinusoidal positional embeddings.
        n_layers (`int`, *optional*, defaults to 6):
            Number of hidden layers in the Transformer encoder.
        n_heads (`int`, *optional*, defaults to 12):
            Number of attention heads for each attention layer in the Transformer encoder.
        dim (`int`, *optional*, defaults to 768):
            Dimensionality of the encoder layers and the pooler layer.
        hidden_dim (`int`, *optional*, defaults to 3072):
            The size of the "intermediate" (often named feed-forward) layer in the Transformer encoder.
        dropout (`float`, *optional*, defaults to 0.1):
            The dropout probability for all fully connected layers in the embeddings, encoder, and pooler.
        attention_dropout (`float`, *optional*, defaults to 0.1):
            The dropout ratio for the attention probabilities.
        activation (`str` or `Callable`, *optional*, defaults to `"gelu"`):
            The non-linear activation function (function or string) in the encoder and pooler. If string, `"gelu"`,
            `"relu"`, `"silu"` and `"gelu_new"` are supported.
        initializer_range (`float`, *optional*, defaults to 0.02):
            The standard deviation of the truncated_normal_initializer for initializing all weight matrices.
        qa_dropout (`float`, *optional*, defaults to 0.1):
            The dropout probabilities used in the question answering model [`DistilBertForQuestionAnswering`].
        seq_classif_dropout (`float`, *optional*, defaults to 0.2):
            The dropout probabilities used in the sequence classification and the multiple choice model
            [`DistilBertForSequenceClassification`].

    Examples:

    ```python
    >>> from transformers import DistilBertConfig, DistilBertModel

    >>> # Initializing a DistilBERT configuration
    >>> configuration = DistilBertConfig()

    >>> # Initializing a model (with random weights) from the configuration
    >>> model = DistilBertModel(configuration)

    >>> # Accessing the model configuration
    >>> configuration = model.config
    ```'''
    model_type: str
    attribute_map: Incomplete
    vocab_size: Incomplete
    max_position_embeddings: Incomplete
    sinusoidal_pos_embds: Incomplete
    n_layers: Incomplete
    n_heads: Incomplete
    dim: Incomplete
    hidden_dim: Incomplete
    dropout: Incomplete
    attention_dropout: Incomplete
    activation: Incomplete
    initializer_range: Incomplete
    qa_dropout: Incomplete
    seq_classif_dropout: Incomplete
    def __init__(self, vocab_size: int = 30522, max_position_embeddings: int = 512, sinusoidal_pos_embds: bool = False, n_layers: int = 6, n_heads: int = 12, dim: int = 768, hidden_dim=..., dropout: float = 0.1, attention_dropout: float = 0.1, activation: str = 'gelu', initializer_range: float = 0.02, qa_dropout: float = 0.1, seq_classif_dropout: float = 0.2, pad_token_id: int = 0, **kwargs) -> None: ...

class DistilBertOnnxConfig(OnnxConfig):
    @property
    def inputs(self) -> Mapping[str, Mapping[int, str]]: ...
