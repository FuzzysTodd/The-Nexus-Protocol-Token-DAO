from ... import PreTrainedTokenizer as PreTrainedTokenizer, TensorType as TensorType, is_torch_available as is_torch_available
from ...configuration_utils import PretrainedConfig as PretrainedConfig
from ...onnx import OnnxConfigWithPast as OnnxConfigWithPast
from ...utils import logging as logging
from _typeshed import Incomplete
from typing import Any, Mapping, Optional

logger: Incomplete
GPT_NEO_PRETRAINED_CONFIG_ARCHIVE_MAP: Incomplete

class GPTNeoConfig(PretrainedConfig):
    '''
    This is the configuration class to store the configuration of a [`GPTNeoModel`]. It is used to instantiate a GPT
    Neo model according to the specified arguments, defining the model architecture. Instantiating a configuration with
    the defaults will yield a similar configuration to that of the GPTNeo
    [EleutherAI/gpt-neo-1.3B](https://huggingface.co/EleutherAI/gpt-neo-1.3B) architecture.

    Configuration objects inherit from [`PretrainedConfig`] and can be used to control the model outputs. Read the
    documentation from [`PretrainedConfig`] for more information.


    Args:
        vocab_size (`int`, *optional*, defaults to 50257):
            Vocabulary size of the GPT Neo model. Defines the number of different tokens that can be represented by the
            `inputs_ids` passed when calling [`GPTNeoModel`]. Vocabulary size of the model. Defines the different
            tokens that can be represented by the *inputs_ids* passed to the forward method of [`GPTNeoModel`].
        attention_types (`List`, *optional*, defaults to `[[["global", "local"], 12]]`):
            The type of attention for each layer in a `List` of the following format `[[["attention_type"],
            num_layerss]]` e.g. for a 24 layer model `[[["global"], 24]]` or `[[["global", "local"], 12]]` Choose the
            value of `attention_type` from `["global", "local"]`
        hidden_size (`int`, *optional*, defaults to 2048):
            Dimensionality of the encoder layers and the pooler layer.
        num_layers (`int`, *optional*, defaults to 24):
            Number of hidden layers in the Transformer encoder.
        num_heads (`int`, *optional*, defaults to 16):
            Number of attention heads for each attention layer in the Transformer encoder.
        intermediate_size (`int`, *optional*, defaults to 8192):
            Dimensionality of the "intermediate" (i.e., feed-forward) layer in the Transformer encoder.
        activation_function (`str` or `function`, *optional*, defaults to `"gelu_new"`):
            The non-linear activation function (function or string) in the encoder and pooler. If string, `"gelu"`,
            `"relu"`, `"selu"` and `"gelu_new"` are supported.
        embed_dropout (`float`, *optional*, defaults to 0.0):
            The dropout probabilitiy for all fully connected layers in the embeddings, encoder, and pooler.
        attention_dropout (`float`, *optional*, defaults to 0.0):
            The dropout ratio for the attention probabilities.
        max_position_embeddings (`int`, *optional*, defaults to 2048):
            The maximum sequence length that this model might ever be used with. Typically set this to something large
            just in case (e.g., 512 or 1024 or 2048).
        type_vocab_size (`int`, *optional*, defaults to 2):
            The vocabulary size of the `token_type_ids` passed when calling [`GPTNeoModel`].
        initializer_range (`float`, *optional*, defaults to 0.02):
            The standard deviation of the truncated_normal_initializer for initializing all weight matrices.
        layer_norm_epsilon (`float`, *optional*, defaults to 1e-5):
            The epsilon used by the layer normalization layers.
        use_cache (`bool`, *optional*, defaults to `True`):
            Whether or not the model should return the last key/values attentions (not used by all models). Only
            relevant if `config.is_decoder=True`.

    Example:

    ```python
    >>> from transformers import GPTNeoConfig, GPTNeoModel

    >>> # Initializing a GPTNeo EleutherAI/gpt-neo-1.3B style configuration
    >>> configuration = GPTNeoConfig()

    >>> # Initializing a model (with random weights) from the EleutherAI/gpt-neo-1.3B style configuration
    >>> model = GPTNeoModel(configuration)

    >>> # Accessing the model configuration
    >>> configuration = model.config
    ```'''
    model_type: str
    keys_to_ignore_at_inference: Incomplete
    attribute_map: Incomplete
    vocab_size: Incomplete
    max_position_embeddings: Incomplete
    hidden_size: Incomplete
    num_layers: Incomplete
    num_heads: Incomplete
    intermediate_size: Incomplete
    window_size: Incomplete
    activation_function: Incomplete
    resid_dropout: Incomplete
    embed_dropout: Incomplete
    attention_dropout: Incomplete
    layer_norm_epsilon: Incomplete
    initializer_range: Incomplete
    summary_type: Incomplete
    summary_use_proj: Incomplete
    summary_activation: Incomplete
    summary_first_dropout: Incomplete
    summary_proj_to_labels: Incomplete
    use_cache: Incomplete
    bos_token_id: Incomplete
    eos_token_id: Incomplete
    attention_types: Incomplete
    attention_layers: Incomplete
    def __init__(self, vocab_size: int = 50257, max_position_embeddings: int = 2048, hidden_size: int = 2048, num_layers: int = 24, attention_types=[[['global', 'local'], 12]], num_heads: int = 16, intermediate_size: Incomplete | None = None, window_size: int = 256, activation_function: str = 'gelu_new', resid_dropout: float = 0.0, embed_dropout: float = 0.0, attention_dropout: float = 0.0, layer_norm_epsilon: float = 1e-05, initializer_range: float = 0.02, summary_type: str = 'cls_index', summary_use_proj: bool = True, summary_activation: Incomplete | None = None, summary_proj_to_labels: bool = True, summary_first_dropout: float = 0.1, use_cache: bool = True, bos_token_id: int = 50256, eos_token_id: int = 50256, **kwargs) -> None: ...
    @staticmethod
    def expand_attention_types_params(attention_types): ...

def custom_unfold(input, dimension, size, step):
    """Custom torch.Tensor.unfold implementation to enable the export to ONNX."""
def custom_get_block_length_and_num_blocks(seq_length, window_size):
    """
    Custom implementation for GPTNeoAttentionMixin._get_block_length_and_num_blocks to enable the export to ONNX as
    original implementation uses Python variables and control flow.
    """

class GPTNeoOnnxConfig(OnnxConfigWithPast):
    @property
    def inputs(self) -> Mapping[str, Mapping[int, str]]: ...
    @property
    def num_attention_heads(self) -> int: ...
    def generate_dummy_inputs(self, tokenizer: PreTrainedTokenizer, batch_size: int = -1, seq_length: int = -1, is_pair: bool = False, framework: Optional[TensorType] = None) -> Mapping[str, Any]: ...
    @property
    def default_onnx_opset(self) -> int: ...
