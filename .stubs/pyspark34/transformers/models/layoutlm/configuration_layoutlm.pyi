from ... import is_torch_available as is_torch_available
from ...onnx import OnnxConfig as OnnxConfig, PatchingSpec as PatchingSpec
from ...utils import logging as logging
from _typeshed import Incomplete
from transformers import PreTrainedTokenizer as PreTrainedTokenizer, PretrainedConfig as PretrainedConfig, TensorType as TensorType
from typing import Any, List, Mapping, Optional

logger: Incomplete
LAYOUTLM_PRETRAINED_CONFIG_ARCHIVE_MAP: Incomplete

class LayoutLMConfig(PretrainedConfig):
    '''
    This is the configuration class to store the configuration of a [`LayoutLMModel`]. It is used to instantiate a
    LayoutLM model according to the specified arguments, defining the model architecture. Instantiating a configuration
    with the defaults will yield a similar configuration to that of the LayoutLM
    [microsoft/layoutlm-base-uncased](https://huggingface.co/microsoft/layoutlm-base-uncased) architecture.

    Configuration objects inherit from [`BertConfig`] and can be used to control the model outputs. Read the
    documentation from [`BertConfig`] for more information.


    Args:
        vocab_size (`int`, *optional*, defaults to 30522):
            Vocabulary size of the LayoutLM model. Defines the different tokens that can be represented by the
            *inputs_ids* passed to the forward method of [`LayoutLMModel`].
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
            The vocabulary size of the `token_type_ids` passed into [`LayoutLMModel`].
        initializer_range (`float`, *optional*, defaults to 0.02):
            The standard deviation of the truncated_normal_initializer for initializing all weight matrices.
        layer_norm_eps (`float`, *optional*, defaults to 1e-12):
            The epsilon used by the layer normalization layers.
        max_2d_position_embeddings (`int`, *optional*, defaults to 1024):
            The maximum value that the 2D position embedding might ever used. Typically set this to something large
            just in case (e.g., 1024).

    Examples:

    ```python
    >>> from transformers import LayoutLMConfig, LayoutLMModel

    >>> # Initializing a LayoutLM configuration
    >>> configuration = LayoutLMConfig()

    >>> # Initializing a model (with random weights) from the configuration
    >>> model = LayoutLMModel(configuration)

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
    position_embedding_type: Incomplete
    use_cache: Incomplete
    classifier_dropout: Incomplete
    max_2d_position_embeddings: Incomplete
    def __init__(self, vocab_size: int = 30522, hidden_size: int = 768, num_hidden_layers: int = 12, num_attention_heads: int = 12, intermediate_size: int = 3072, hidden_act: str = 'gelu', hidden_dropout_prob: float = 0.1, attention_probs_dropout_prob: float = 0.1, max_position_embeddings: int = 512, type_vocab_size: int = 2, initializer_range: float = 0.02, layer_norm_eps: float = 1e-12, pad_token_id: int = 0, position_embedding_type: str = 'absolute', use_cache: bool = True, classifier_dropout: Incomplete | None = None, max_2d_position_embeddings: int = 1024, **kwargs) -> None: ...

class LayoutLMOnnxConfig(OnnxConfig):
    max_2d_positions: Incomplete
    def __init__(self, config: PretrainedConfig, task: str = 'default', patching_specs: List[PatchingSpec] = None) -> None: ...
    @property
    def inputs(self) -> Mapping[str, Mapping[int, str]]: ...
    def generate_dummy_inputs(self, tokenizer: PreTrainedTokenizer, batch_size: int = -1, seq_length: int = -1, is_pair: bool = False, framework: Optional[TensorType] = None) -> Mapping[str, Any]:
        """
        Generate inputs to provide to the ONNX exporter for the specific framework

        Args:
            tokenizer: The tokenizer associated with this model configuration
            batch_size: The batch size (int) to export the model for (-1 means dynamic axis)
            seq_length: The sequence length (int) to export the model for (-1 means dynamic axis)
            is_pair: Indicate if the input is a pair (sentence 1, sentence 2)
            framework: The framework (optional) the tokenizer will generate tensor for

        Returns:
            Mapping[str, Tensor] holding the kwargs to provide to the model's forward function
        """
