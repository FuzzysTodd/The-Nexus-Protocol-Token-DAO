from ...configuration_utils import PretrainedConfig as PretrainedConfig
from ...utils import logging as logging
from _typeshed import Incomplete

logger: Incomplete
FUNNEL_PRETRAINED_CONFIG_ARCHIVE_MAP: Incomplete

class FunnelConfig(PretrainedConfig):
    '''
    This is the configuration class to store the configuration of a [`FunnelModel`] or a [`TFBertModel`]. It is used to
    instantiate a Funnel Transformer model according to the specified arguments, defining the model architecture.
    Instantiating a configuration with the defaults will yield a similar configuration to that of the Funnel
    Transformer [funnel-transformer/small](https://huggingface.co/funnel-transformer/small) architecture.

    Configuration objects inherit from [`PretrainedConfig`] and can be used to control the model outputs. Read the
    documentation from [`PretrainedConfig`] for more information.

    Args:
        vocab_size (`int`, *optional*, defaults to 30522):
            Vocabulary size of the Funnel transformer. Defines the number of different tokens that can be represented
            by the `inputs_ids` passed when calling [`FunnelModel`] or [`TFFunnelModel`].
        block_sizes (`List[int]`, *optional*, defaults to `[4, 4, 4]`):
            The sizes of the blocks used in the model.
        block_repeats (`List[int]`, *optional*):
            If passed along, each layer of each block is repeated the number of times indicated.
        num_decoder_layers (`int`, *optional*, defaults to 2):
            The number of layers in the decoder (when not using the base model).
        d_model (`int`, *optional*, defaults to 768):
            Dimensionality of the model\'s hidden states.
        n_head (`int`, *optional*, defaults to 12):
            Number of attention heads for each attention layer in the Transformer encoder.
        d_head (`int`, *optional*, defaults to 64):
            Dimensionality of the model\'s heads.
        d_inner (`int`, *optional*, defaults to 3072):
            Inner dimension in the feed-forward blocks.
        hidden_act (`str` or `callable`, *optional*, defaults to `"gelu_new"`):
            The non-linear activation function (function or string) in the encoder and pooler. If string, `"gelu"`,
            `"relu"`, `"silu"` and `"gelu_new"` are supported.
        hidden_dropout (`float`, *optional*, defaults to 0.1):
            The dropout probability for all fully connected layers in the embeddings, encoder, and pooler.
        attention_dropout (`float`, *optional*, defaults to 0.1):
            The dropout probability for the attention probabilities.
        activation_dropout (`float`, *optional*, defaults to 0.0):
            The dropout probability used between the two layers of the feed-forward blocks.
        type_vocab_size (`int`, *optional*, defaults to 3):
            The vocabulary size of the `token_type_ids` passed when calling [`FunnelModel`] or [`TFFunnelModel`].
        initializer_range (`float`, *optional*, defaults to 0.1):
            The upper bound of the *uniform initializer* for initializing all weight matrices in attention layers.
        initializer_std (`float`, *optional*):
            The standard deviation of the *normal initializer* for initializing the embedding matrix and the weight of
            linear layers. Will default to 1 for the embedding matrix and the value given by Xavier initialization for
            linear layers.
        layer_norm_eps (`float`, *optional*, defaults to 1e-9):
            The epsilon used by the layer normalization layers.
        pooling_type (`str`, *optional*, defaults to `"mean"`):
            Possible values are `"mean"` or `"max"`. The way pooling is performed at the beginning of each block.
        attention_type (`str`, *optional*, defaults to `"relative_shift"`):
            Possible values are `"relative_shift"` or `"factorized"`. The former is faster on CPU/GPU while the latter
            is faster on TPU.
        separate_cls (`bool`, *optional*, defaults to `True`):
            Whether or not to separate the cls token when applying pooling.
        truncate_seq (`bool`, *optional*, defaults to `False`):
            When using `separate_cls`, whether or not to truncate the last token when pooling, to avoid getting a
            sequence length that is not a multiple of 2.
        pool_q_only (`bool`, *optional*, defaults to `False`):
            Whether or not to apply the pooling only to the query or to query, key and values for the attention layers.
    '''
    model_type: str
    attribute_map: Incomplete
    vocab_size: Incomplete
    block_sizes: Incomplete
    block_repeats: Incomplete
    num_decoder_layers: Incomplete
    d_model: Incomplete
    n_head: Incomplete
    d_head: Incomplete
    d_inner: Incomplete
    hidden_act: Incomplete
    hidden_dropout: Incomplete
    attention_dropout: Incomplete
    activation_dropout: Incomplete
    type_vocab_size: Incomplete
    initializer_range: Incomplete
    initializer_std: Incomplete
    layer_norm_eps: Incomplete
    pooling_type: Incomplete
    attention_type: Incomplete
    separate_cls: Incomplete
    truncate_seq: Incomplete
    pool_q_only: Incomplete
    def __init__(self, vocab_size: int = 30522, block_sizes=[4, 4, 4], block_repeats: Incomplete | None = None, num_decoder_layers: int = 2, d_model: int = 768, n_head: int = 12, d_head: int = 64, d_inner: int = 3072, hidden_act: str = 'gelu_new', hidden_dropout: float = 0.1, attention_dropout: float = 0.1, activation_dropout: float = 0.0, type_vocab_size: int = 3, initializer_range: float = 0.1, initializer_std: Incomplete | None = None, layer_norm_eps: float = 1e-09, pooling_type: str = 'mean', attention_type: str = 'relative_shift', separate_cls: bool = True, truncate_seq: bool = True, pool_q_only: bool = True, **kwargs) -> None: ...
    @property
    def num_hidden_layers(self): ...
    @num_hidden_layers.setter
    def num_hidden_layers(self, value) -> None: ...
    @property
    def num_blocks(self): ...
    @num_blocks.setter
    def num_blocks(self, value) -> None: ...
