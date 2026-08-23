from ...configuration_utils import PretrainedConfig as PretrainedConfig
from ...onnx import OnnxConfigWithPast as OnnxConfigWithPast, PatchingSpec as PatchingSpec
from ...utils import logging as logging
from _typeshed import Incomplete
from transformers import PreTrainedTokenizer as PreTrainedTokenizer, TensorType as TensorType, is_torch_available as is_torch_available
from typing import Any, List, Mapping, Optional

logger: Incomplete
GPT2_PRETRAINED_CONFIG_ARCHIVE_MAP: Incomplete

class GPT2Config(PretrainedConfig):
    '''
    This is the configuration class to store the configuration of a [`GPT2Model`] or a [`TFGPT2Model`]. It is used to
    instantiate a GPT-2 model according to the specified arguments, defining the model architecture. Instantiating a
    configuration with the defaults will yield a similar configuration to that of the GPT-2
    [gpt2](https://huggingface.co/gpt2) architecture.

    Configuration objects inherit from [`PretrainedConfig`] and can be used to control the model outputs. Read the
    documentation from [`PretrainedConfig`] for more information.


    Args:
        vocab_size (`int`, *optional*, defaults to 50257):
            Vocabulary size of the GPT-2 model. Defines the number of different tokens that can be represented by the
            `inputs_ids` passed when calling [`GPT2Model`] or [`TFGPT2Model`].
        n_positions (`int`, *optional*, defaults to 1024):
            The maximum sequence length that this model might ever be used with. Typically set this to something large
            just in case (e.g., 512 or 1024 or 2048).
        n_embd (`int`, *optional*, defaults to 768):
            Dimensionality of the embeddings and hidden states.
        n_layer (`int`, *optional*, defaults to 12):
            Number of hidden layers in the Transformer encoder.
        n_head (`int`, *optional*, defaults to 12):
            Number of attention heads for each attention layer in the Transformer encoder.
        n_inner (`int`, *optional*, defaults to None):
            Dimensionality of the inner feed-forward layers. `None` will set it to 4 times n_embd
        activation_function (`str`, *optional*, defaults to `"gelu"`):
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
        summary_type (`string`, *optional*, defaults to `"cls_index"`):
            Argument used when doing sequence summary, used in the models [`GPT2DoubleHeadsModel`] and
            [`TFGPT2DoubleHeadsModel`].

            Has to be one of the following options:

                - `"last"`: Take the last token hidden state (like XLNet).
                - `"first"`: Take the first token hidden state (like BERT).
                - `"mean"`: Take the mean of all tokens hidden states.
                - `"cls_index"`: Supply a Tensor of classification token position (like GPT/GPT-2).
                - `"attn"`: Not implemented now, use multi-head attention.
        summary_use_proj (`bool`, *optional*, defaults to `True`):
            Argument used when doing sequence summary, used in the models [`GPT2DoubleHeadsModel`] and
            [`TFGPT2DoubleHeadsModel`].

            Whether or not to add a projection after the vector extraction.
        summary_activation (`str`, *optional*):
            Argument used when doing sequence summary. Used in for the multiple choice head in
            [`GPT2DoubleHeadsModel`].

            Pass `"tanh"` for a tanh activation to the output, any other value will result in no activation.
        summary_proj_to_labels (`bool`, *optional*, defaults to `True`):
            Argument used when doing sequence summary, used in the models [`GPT2DoubleHeadsModel`] and
            [`TFGPT2DoubleHeadsModel`].

            Whether the projection outputs should have `config.num_labels` or `config.hidden_size` classes.
        summary_first_dropout (`float`, *optional*, defaults to 0.1):
            Argument used when doing sequence summary, used in the models [`GPT2DoubleHeadsModel`] and
            [`TFGPT2DoubleHeadsModel`].

            The dropout ratio to be used after the projection and activation.
        scale_attn_weights (`bool`, *optional*, defaults to `True`):
            Scale attention weights by dividing by sqrt(hidden_size)..
        use_cache (`bool`, *optional*, defaults to `True`):
            Whether or not the model should return the last key/values attentions (not used by all models).
        scale_attn_by_inverse_layer_idx (`bool`, *optional*, defaults to `False`):
            Whether to additionally scale attention weights by `1 / layer_idx + 1`.
        reorder_and_upcast_attn (`bool`, *optional*, defaults to `False`):
            Whether to scale keys (K) prior to computing attention (dot-product) and upcast attention
            dot-product/softmax to float() when training with mixed precision.

    Example:

    ```python
    >>> from transformers import GPT2Config, GPT2Model

    >>> # Initializing a GPT2 configuration
    >>> configuration = GPT2Config()

    >>> # Initializing a model (with random weights) from the configuration
    >>> model = GPT2Model(configuration)

    >>> # Accessing the model configuration
    >>> configuration = model.config
    ```'''
    model_type: str
    keys_to_ignore_at_inference: Incomplete
    attribute_map: Incomplete
    vocab_size: Incomplete
    n_positions: Incomplete
    n_embd: Incomplete
    n_layer: Incomplete
    n_head: Incomplete
    n_inner: Incomplete
    activation_function: Incomplete
    resid_pdrop: Incomplete
    embd_pdrop: Incomplete
    attn_pdrop: Incomplete
    layer_norm_epsilon: Incomplete
    initializer_range: Incomplete
    summary_type: Incomplete
    summary_use_proj: Incomplete
    summary_activation: Incomplete
    summary_first_dropout: Incomplete
    summary_proj_to_labels: Incomplete
    scale_attn_weights: Incomplete
    use_cache: Incomplete
    scale_attn_by_inverse_layer_idx: Incomplete
    reorder_and_upcast_attn: Incomplete
    bos_token_id: Incomplete
    eos_token_id: Incomplete
    def __init__(self, vocab_size: int = 50257, n_positions: int = 1024, n_embd: int = 768, n_layer: int = 12, n_head: int = 12, n_inner: Incomplete | None = None, activation_function: str = 'gelu_new', resid_pdrop: float = 0.1, embd_pdrop: float = 0.1, attn_pdrop: float = 0.1, layer_norm_epsilon: float = 1e-05, initializer_range: float = 0.02, summary_type: str = 'cls_index', summary_use_proj: bool = True, summary_activation: Incomplete | None = None, summary_proj_to_labels: bool = True, summary_first_dropout: float = 0.1, scale_attn_weights: bool = True, use_cache: bool = True, bos_token_id: int = 50256, eos_token_id: int = 50256, scale_attn_by_inverse_layer_idx: bool = False, reorder_and_upcast_attn: bool = False, **kwargs) -> None: ...

class GPT2OnnxConfig(OnnxConfigWithPast):
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
