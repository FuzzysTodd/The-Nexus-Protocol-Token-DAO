from ... import FeatureExtractionMixin as FeatureExtractionMixin, PreTrainedTokenizerBase as PreTrainedTokenizerBase, TensorType as TensorType
from ...configuration_utils import PretrainedConfig as PretrainedConfig
from ...onnx import OnnxConfig as OnnxConfig
from ...utils import logging as logging
from _typeshed import Incomplete
from typing import Any, Mapping, Optional, Union

logger: Incomplete
DEBERTA_PRETRAINED_CONFIG_ARCHIVE_MAP: Incomplete

class DebertaConfig(PretrainedConfig):
    '''
    This is the configuration class to store the configuration of a [`DebertaModel`] or a [`TFDebertaModel`]. It is
    used to instantiate a DeBERTa model according to the specified arguments, defining the model architecture.
    Instantiating a configuration with the defaults will yield a similar configuration to that of the DeBERTa
    [microsoft/deberta-base](https://huggingface.co/microsoft/deberta-base) architecture.

    Configuration objects inherit from [`PretrainedConfig`] and can be used to control the model outputs. Read the
    documentation from [`PretrainedConfig`] for more information.

    Arguments:
        vocab_size (`int`, *optional*, defaults to 30522):
            Vocabulary size of the DeBERTa model. Defines the number of different tokens that can be represented by the
            `inputs_ids` passed when calling [`DebertaModel`] or [`TFDebertaModel`].
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
            `"relu"`, `"silu"`, `"gelu"`, `"tanh"`, `"gelu_fast"`, `"mish"`, `"linear"`, `"sigmoid"` and `"gelu_new"`
            are supported.
        hidden_dropout_prob (`float`, *optional*, defaults to 0.1):
            The dropout probability for all fully connected layers in the embeddings, encoder, and pooler.
        attention_probs_dropout_prob (`float`, *optional*, defaults to 0.1):
            The dropout ratio for the attention probabilities.
        max_position_embeddings (`int`, *optional*, defaults to 512):
            The maximum sequence length that this model might ever be used with. Typically set this to something large
            just in case (e.g., 512 or 1024 or 2048).
        type_vocab_size (`int`, *optional*, defaults to 2):
            The vocabulary size of the `token_type_ids` passed when calling [`DebertaModel`] or [`TFDebertaModel`].
        initializer_range (`float`, *optional*, defaults to 0.02):
            The standard deviation of the truncated_normal_initializer for initializing all weight matrices.
        layer_norm_eps (`float`, *optional*, defaults to 1e-12):
            The epsilon used by the layer normalization layers.
        relative_attention (`bool`, *optional*, defaults to `False`):
            Whether use relative position encoding.
        max_relative_positions (`int`, *optional*, defaults to 1):
            The range of relative positions `[-max_position_embeddings, max_position_embeddings]`. Use the same value
            as `max_position_embeddings`.
        pad_token_id (`int`, *optional*, defaults to 0):
            The value used to pad input_ids.
        position_biased_input (`bool`, *optional*, defaults to `True`):
            Whether add absolute position embedding to content embedding.
        pos_att_type (`List[str]`, *optional*):
            The type of relative position attention, it can be a combination of `["p2c", "c2p"]`, e.g. `["p2c"]`,
            `["p2c", "c2p"]`.
        layer_norm_eps (`float`, optional, defaults to 1e-12):
            The epsilon used by the layer normalization layers.

    Example:

    ```python
    >>> from transformers import DebertaConfig, DebertaModel

    >>> # Initializing a DeBERTa microsoft/deberta-base style configuration
    >>> configuration = DebertaConfig()

    >>> # Initializing a model (with random weights) from the microsoft/deberta-base style configuration
    >>> model = DebertaModel(configuration)

    >>> # Accessing the model configuration
    >>> configuration = model.config
    ```'''
    model_type: str
    hidden_size: Incomplete
    num_hidden_layers: Incomplete
    num_attention_heads: Incomplete
    intermediate_size: Incomplete
    hidden_act: Incomplete
    hidden_dropout_prob: Incomplete
    attention_probs_dropout_prob: Incomplete
    max_position_embeddings: Incomplete
    type_vocab_size: Incomplete
    initializer_range: Incomplete
    relative_attention: Incomplete
    max_relative_positions: Incomplete
    pad_token_id: Incomplete
    position_biased_input: Incomplete
    pos_att_type: Incomplete
    vocab_size: Incomplete
    layer_norm_eps: Incomplete
    pooler_hidden_size: Incomplete
    pooler_dropout: Incomplete
    pooler_hidden_act: Incomplete
    def __init__(self, vocab_size: int = 50265, hidden_size: int = 768, num_hidden_layers: int = 12, num_attention_heads: int = 12, intermediate_size: int = 3072, hidden_act: str = 'gelu', hidden_dropout_prob: float = 0.1, attention_probs_dropout_prob: float = 0.1, max_position_embeddings: int = 512, type_vocab_size: int = 0, initializer_range: float = 0.02, layer_norm_eps: float = 1e-07, relative_attention: bool = False, max_relative_positions: int = -1, pad_token_id: int = 0, position_biased_input: bool = True, pos_att_type: Incomplete | None = None, pooler_dropout: int = 0, pooler_hidden_act: str = 'gelu', **kwargs) -> None: ...

class DebertaOnnxConfig(OnnxConfig):
    @property
    def inputs(self) -> Mapping[str, Mapping[int, str]]: ...
    @property
    def default_onnx_opset(self) -> int: ...
    def generate_dummy_inputs(self, preprocessor: Union['PreTrainedTokenizerBase', 'FeatureExtractionMixin'], batch_size: int = -1, seq_length: int = -1, num_choices: int = -1, is_pair: bool = False, framework: Optional['TensorType'] = None, num_channels: int = 3, image_width: int = 40, image_height: int = 40, tokenizer: PreTrainedTokenizerBase = None) -> Mapping[str, Any]: ...
