from ...configuration_utils import PretrainedConfig as PretrainedConfig
from ...utils import logging as logging
from _typeshed import Incomplete

logger: Incomplete
TRANSFO_XL_PRETRAINED_CONFIG_ARCHIVE_MAP: Incomplete

class TransfoXLConfig(PretrainedConfig):
    '''
    This is the configuration class to store the configuration of a [`TransfoXLModel`] or a [`TFTransfoXLModel`]. It is
    used to instantiate a Transformer-XL model according to the specified arguments, defining the model architecture.
    Instantiating a configuration with the defaults will yield a similar configuration to that of the TransfoXL
    [transfo-xl-wt103](https://huggingface.co/transfo-xl-wt103) architecture.

    Configuration objects inherit from [`PretrainedConfig`] and can be used to control the model outputs. Read the
    documentation from [`PretrainedConfig`] for more information.

    Args:
        vocab_size (`int`, *optional*, defaults to 267735):
            Vocabulary size of the BERT model. Defines the number of different tokens that can be represented by the
            `inputs_ids` passed when calling [`TransfoXLModel`] or [`TFTransfoXLModel`].
        cutoffs (`List[int]`, *optional*, defaults to `[20000, 40000, 200000]`):
            Cutoffs for the adaptive softmax.
        d_model (`int`, *optional*, defaults to 1024):
            Dimensionality of the model\'s hidden states.
        d_embed (`int`, *optional*, defaults to 1024):
            Dimensionality of the embeddings
        n_head (`int`, *optional*, defaults to 16):
            Number of attention heads for each attention layer in the Transformer encoder.
        d_head (`int`, *optional*, defaults to 64):
            Dimensionality of the model\'s heads.
        d_inner (`int`, *optional*, defaults to 4096):
            Inner dimension in FF
        div_val (`int`, *optional*, defaults to 4):
            Divident value for adapative input and softmax
        pre_lnorm (`boolean`, *optional*, defaults to `False`):
            Whether or not to apply LayerNorm to the input instead of the output in the blocks.
        n_layer (`int`, *optional*, defaults to 18):
            Number of hidden layers in the Transformer encoder.
        mem_len (`int`, *optional*, defaults to 1600):
            Length of the retained previous heads.
        clamp_len (`int`, *optional*, defaults to 1000):
            Use the same pos embeddings after clamp_len.
        same_length (`boolean`, *optional*, defaults to `True`):
            Whether or not to use the same attn length for all tokens
        proj_share_all_but_first (`boolean`, *optional*, defaults to `True`):
            True to share all but first projs, False not to share.
        attn_type (`int`, *optional*, defaults to 0):
            Attention type. 0 for Transformer-XL, 1 for Shaw et al, 2 for Vaswani et al, 3 for Al Rfou et al.
        sample_softmax (`int`, *optional*, defaults to -1):
            Number of samples in the sampled softmax.
        adaptive (`boolean`, *optional*, defaults to `True`):
            Whether or not to use adaptive softmax.
        dropout (`float`, *optional*, defaults to 0.1):
            The dropout probability for all fully connected layers in the embeddings, encoder, and pooler.
        dropatt (`float`, *optional*, defaults to 0):
            The dropout ratio for the attention probabilities.
        untie_r (`boolean`, *optional*, defaults to `True`):
            Whether ot not to untie relative position biases.
        init (`str`, *optional*, defaults to `"normal"`):
            Parameter initializer to use.
        init_range (`float`, *optional*, defaults to 0.01):
            Parameters initialized by U(-init_range, init_range).
        proj_init_std (`float`, *optional*, defaults to 0.01):
            Parameters initialized by N(0, init_std)
        init_std (`float`, *optional*, defaults to 0.02):
            Parameters initialized by N(0, init_std)
        layer_norm_epsilon (`float`, *optional*, defaults to 1e-5):
            The epsilon to use in the layer normalization layers

    Examples:

    ```python
    >>> from transformers import TransfoXLConfig, TransfoXLModel

    >>> # Initializing a Transformer XL configuration
    >>> configuration = TransfoXLConfig()

    >>> # Initializing a model (with random weights) from the configuration
    >>> model = TransfoXLModel(configuration)

    >>> # Accessing the model configuration
    >>> configuration = model.config
    ```'''
    model_type: str
    keys_to_ignore_at_inference: Incomplete
    attribute_map: Incomplete
    vocab_size: Incomplete
    cutoffs: Incomplete
    tie_projs: Incomplete
    d_model: Incomplete
    d_embed: Incomplete
    d_head: Incomplete
    d_inner: Incomplete
    div_val: Incomplete
    pre_lnorm: Incomplete
    n_layer: Incomplete
    n_head: Incomplete
    mem_len: Incomplete
    same_length: Incomplete
    attn_type: Incomplete
    clamp_len: Incomplete
    sample_softmax: Incomplete
    adaptive: Incomplete
    dropout: Incomplete
    dropatt: Incomplete
    untie_r: Incomplete
    init: Incomplete
    init_range: Incomplete
    proj_init_std: Incomplete
    init_std: Incomplete
    layer_norm_epsilon: Incomplete
    def __init__(self, vocab_size: int = 267735, cutoffs=[20000, 40000, 200000], d_model: int = 1024, d_embed: int = 1024, n_head: int = 16, d_head: int = 64, d_inner: int = 4096, div_val: int = 4, pre_lnorm: bool = False, n_layer: int = 18, mem_len: int = 1600, clamp_len: int = 1000, same_length: bool = True, proj_share_all_but_first: bool = True, attn_type: int = 0, sample_softmax: int = -1, adaptive: bool = True, dropout: float = 0.1, dropatt: float = 0.0, untie_r: bool = True, init: str = 'normal', init_range: float = 0.01, proj_init_std: float = 0.01, init_std: float = 0.02, layer_norm_epsilon: float = 1e-05, eos_token_id: int = 0, **kwargs) -> None: ...
    @property
    def max_position_embeddings(self): ...
    @max_position_embeddings.setter
    def max_position_embeddings(self, value) -> None: ...
