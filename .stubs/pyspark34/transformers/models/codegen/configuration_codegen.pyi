from ... import PreTrainedTokenizer as PreTrainedTokenizer, TensorType as TensorType, is_torch_available as is_torch_available
from ...configuration_utils import PretrainedConfig as PretrainedConfig
from ...onnx import OnnxConfigWithPast as OnnxConfigWithPast, PatchingSpec as PatchingSpec
from ...utils import logging as logging
from _typeshed import Incomplete
from typing import Any, List, Mapping, Optional

logger: Incomplete
CODEGEN_PRETRAINED_CONFIG_ARCHIVE_MAP: Incomplete

class CodeGenConfig(PretrainedConfig):
    '''
    This is the configuration class to store the configuration of a [`CodeGenModel`]. It is used to instantiate a
    CodeGen model according to the specified arguments, defining the model architecture. Instantiating a configuration
    with the defaults will yield a similar configuration to that of the CodeGen
    [Salesforce/codegen-2B-mono](https://huggingface.co/Salesforce/codegen-2B-mono) architecture. Configuration objects
    inherit from [`PretrainedConfig`] and can be used to control the model outputs. Read the documentation from
    [`PretrainedConfig`] for more information.

    Args:
        vocab_size (`int`, *optional*, defaults to 50400):
            Vocabulary size of the CodeGen model. Defines the number of different tokens that can be represented by the
            `inputs_ids` passed when calling [`CodeGenModel`].
        n_positions (`int`, *optional*, defaults to 2048):
            The maximum sequence length that this model might ever be used with. Typically set this to something large
            just in case (e.g., 512 or 1024 or 2048).
        n_embd (`int`, *optional*, defaults to 4096):
            Dimensionality of the embeddings and hidden states.
        n_layer (`int`, *optional*, defaults to 28):
            Number of hidden layers in the Transformer encoder.
        n_head (`int`, *optional*, defaults to 16):
            Number of attention heads for each attention layer in the Transformer encoder.
        rotary_dim (`int`, *optional*, defaults to 64):
            Number of dimensions in the embedding that Rotary Position Embedding is applied to.
        n_inner (`int`, *optional*, defaults to None):
            Dimensionality of the inner feed-forward layers. `None` will set it to 4 times n_embd
        activation_function (`str`, *optional*, defaults to `"gelu_new"`):
            Activation function, to be selected in the list `["relu", "silu", "gelu", "tanh", "gelu_new"]`.
        resid_pdrop (`float`, *optional*, defaults to 0.1):
            The dropout probability for all fully connected layers in the embeddings, encoder, and pooler.
        embd_pdrop (`int`, *optional*, defaults to 0.1):
            The dropout ratio for the embeddings.
        attn_pdrop (`float`, *optional*, defaults to 0.1):
            The dropout ratio for the attention.
        layer_norm_epsilon (`float`, *optional*, defaults to 1e-5):
            The epsilon to use in the layer normalization layers.
        initializer_range (`float`, *optional*, defaults to 0.02):
            The standard deviation of the truncated_normal_initializer for initializing all weight matrices.
        scale_attn_weights (`bool`, *optional*, defaults to `True`):
            Scale attention weights by dividing by sqrt(hidden_size).
        use_cache (`bool`, *optional*, defaults to `True`):
            Whether or not the model should return the last key/values attentions (not used by all models).

    Example:

    ```python
    >>> from transformers import CodeGenConfig, CodeGenModel

    >>> # Initializing a CodeGen 6B configuration
    >>> configuration = CodeGenConfig()

    >>> # Initializing a model (with random weights) from the configuration
    >>> model = CodeGenModel(configuration)

    >>> # Accessing the model configuration
    >>> configuration = model.config
    ```'''
    model_type: str
    attribute_map: Incomplete
    vocab_size: Incomplete
    n_ctx: Incomplete
    n_positions: Incomplete
    n_embd: Incomplete
    n_layer: Incomplete
    n_head: Incomplete
    n_inner: Incomplete
    rotary_dim: Incomplete
    activation_function: Incomplete
    resid_pdrop: Incomplete
    embd_pdrop: Incomplete
    attn_pdrop: Incomplete
    layer_norm_epsilon: Incomplete
    initializer_range: Incomplete
    scale_attn_weights: Incomplete
    use_cache: Incomplete
    bos_token_id: Incomplete
    eos_token_id: Incomplete
    def __init__(self, vocab_size: int = 50400, n_positions: int = 2048, n_ctx: int = 2048, n_embd: int = 4096, n_layer: int = 28, n_head: int = 16, rotary_dim: int = 64, n_inner: Incomplete | None = None, activation_function: str = 'gelu_new', resid_pdrop: float = 0.0, embd_pdrop: float = 0.0, attn_pdrop: float = 0.0, layer_norm_epsilon: float = 1e-05, initializer_range: float = 0.02, scale_attn_weights: bool = True, use_cache: bool = True, bos_token_id: int = 50256, eos_token_id: int = 50256, tie_word_embeddings: bool = False, **kwargs) -> None: ...

class CodeGenOnnxConfig(OnnxConfigWithPast):
    def __init__(self, config: PretrainedConfig, task: str = 'default', patching_specs: List[PatchingSpec] = None, use_past: bool = False) -> None: ...
    @property
    def inputs(self) -> Mapping[str, Mapping[int, str]]: ...
    @property
    def num_layers(self) -> int: ...
    @property
    def num_attention_heads(self) -> int: ...
    def generate_dummy_inputs(self, tokenizer: PreTrainedTokenizer, batch_size: int = -1, seq_length: int = -1, is_pair: bool = False, framework: Optional[TensorType] = None) -> Mapping[str, Any]: ...
    @property
    def default_onnx_opset(self) -> int: ...
