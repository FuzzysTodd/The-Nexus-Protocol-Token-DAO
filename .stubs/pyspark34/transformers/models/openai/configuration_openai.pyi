from ...configuration_utils import PretrainedConfig as PretrainedConfig
from ...utils import logging as logging
from _typeshed import Incomplete

logger: Incomplete
OPENAI_GPT_PRETRAINED_CONFIG_ARCHIVE_MAP: Incomplete

class OpenAIGPTConfig(PretrainedConfig):
    '''
    This is the configuration class to store the configuration of a [`OpenAIGPTModel`] or a [`TFOpenAIGPTModel`]. It is
    used to instantiate a GPT model according to the specified arguments, defining the model architecture.
    Instantiating a configuration with the defaults will yield a similar configuration to that of the GPT
    [openai-gpt](https://huggingface.co/openai-gpt) architecture from OpenAI.

    Configuration objects inherit from [`PretrainedConfig`] and can be used to control the model outputs. Read the
    documentation from [`PretrainedConfig`] for more information.

    Args:
        vocab_size (`int`, *optional*, defaults to 40478):
            Vocabulary size of the GPT-2 model. Defines the number of different tokens that can be represented by the
            `inputs_ids` passed when calling [`OpenAIGPTModel`] or [`TFOpenAIGPTModel`].
        n_positions (`int`, *optional*, defaults to 512):
            The maximum sequence length that this model might ever be used with. Typically set this to something large
            just in case (e.g., 512 or 1024 or 2048).
        n_embd (`int`, *optional*, defaults to 768):
            Dimensionality of the embeddings and hidden states.
        n_layer (`int`, *optional*, defaults to 12):
            Number of hidden layers in the Transformer encoder.
        n_head (`int`, *optional*, defaults to 12):
            Number of attention heads for each attention layer in the Transformer encoder.
        afn (`str` or `Callable`, *optional*, defaults to `"gelu"`):
            The non-linear activation function (function or string) in the encoder and pooler. If string, `"gelu"`,
            `"relu"`, `"silu"` and `"gelu_new"` are supported.
        resid_pdrop (`float`, *optional*, defaults to 0.1):
            The dropout probability for all fully connected layers in the embeddings, encoder, and pooler.
        embd_pdrop (`int`, *optional*, defaults to 0.1):
            The dropout ratio for the embeddings.
        attn_pdrop (`float`, *optional*, defaults to 0.1):
            The dropout ratio for the attention.
        layer_norm_epsilon (`float`, *optional*, defaults to 1e-5):
            The epsilon to use in the layer normalization layers
        initializer_range (`float`, *optional*, defaults to 0.02):
            The standard deviation of the truncated_normal_initializer for initializing all weight matrices.
        summary_type (`str`, *optional*, defaults to `"cls_index"`):
            Argument used when doing sequence summary, used in the models [`OpenAIGPTDoubleHeadsModel`] and
            [`OpenAIGPTDoubleHeadsModel`].

            Has to be one of the following options:

                - `"last"`: Take the last token hidden state (like XLNet).
                - `"first"`: Take the first token hidden state (like BERT).
                - `"mean"`: Take the mean of all tokens hidden states.
                - `"cls_index"`: Supply a Tensor of classification token position (like GPT/GPT-2).
                - `"attn"`: Not implemented now, use multi-head attention.
        summary_use_proj (`bool`, *optional*, defaults to `True`):
            Argument used when doing sequence summary, used in the models [`OpenAIGPTDoubleHeadsModel`] and
            [`OpenAIGPTDoubleHeadsModel`].

            Whether or not to add a projection after the vector extraction.
        summary_activation (`str`, *optional*):
            Argument used when doing sequence summary, used in the models [`OpenAIGPTDoubleHeadsModel`] and
            [`OpenAIGPTDoubleHeadsModel`].

            Pass `"tanh"` for a tanh activation to the output, any other value will result in no activation.
        summary_proj_to_labels (`bool`, *optional*, defaults to `True`):
            Argument used when doing sequence summary, used in the models [`OpenAIGPTDoubleHeadsModel`] and
            [`OpenAIGPTDoubleHeadsModel`].

            Whether the projection outputs should have `config.num_labels` or `config.hidden_size` classes.
        summary_first_dropout (`float`, *optional*, defaults to 0.1):
            Argument used when doing sequence summary, used in the models [`OpenAIGPTDoubleHeadsModel`] and
            [`OpenAIGPTDoubleHeadsModel`].

            The dropout ratio to be used after the projection and activation.
        use_cache (`bool`, *optional*, defaults to `True`):
            Whether or not the model should return the last key/values attentions (not used by all models).


    Examples:

    ```python
    >>> from transformers import OpenAIGPTConfig, OpenAIGPTModel

    >>> # Initializing a GPT configuration
    >>> configuration = OpenAIGPTConfig()

    >>> # Initializing a model (with random weights) from the configuration
    >>> model = OpenAIGPTModel(configuration)

    >>> # Accessing the model configuration
    >>> configuration = model.config
    ```'''
    model_type: str
    attribute_map: Incomplete
    vocab_size: Incomplete
    n_positions: Incomplete
    n_embd: Incomplete
    n_layer: Incomplete
    n_head: Incomplete
    afn: Incomplete
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
    def __init__(self, vocab_size: int = 40478, n_positions: int = 512, n_embd: int = 768, n_layer: int = 12, n_head: int = 12, afn: str = 'gelu', resid_pdrop: float = 0.1, embd_pdrop: float = 0.1, attn_pdrop: float = 0.1, layer_norm_epsilon: float = 1e-05, initializer_range: float = 0.02, summary_type: str = 'cls_index', summary_use_proj: bool = True, summary_activation: Incomplete | None = None, summary_proj_to_labels: bool = True, summary_first_dropout: float = 0.1, **kwargs) -> None: ...
