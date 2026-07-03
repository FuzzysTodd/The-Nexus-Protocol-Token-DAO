from ...configuration_utils import PretrainedConfig as PretrainedConfig
from ...utils import logging as logging
from _typeshed import Incomplete

logger: Incomplete
NAT_PRETRAINED_CONFIG_ARCHIVE_MAP: Incomplete

class NatConfig(PretrainedConfig):
    '''
    This is the configuration class to store the configuration of a [`NatModel`]. It is used to instantiate a Nat model
    according to the specified arguments, defining the model architecture. Instantiating a configuration with the
    defaults will yield a similar configuration to that of the Nat
    [shi-labs/nat-mini-in1k-224](https://huggingface.co/shi-labs/nat-mini-in1k-224) architecture.

    Configuration objects inherit from [`PretrainedConfig`] and can be used to control the model outputs. Read the
    documentation from [`PretrainedConfig`] for more information.

    Args:
        patch_size (`int`, *optional*, defaults to 4):
            The size (resolution) of each patch. NOTE: Only patch size of 4 is supported at the moment.
        num_channels (`int`, *optional*, defaults to 3):
            The number of input channels.
        embed_dim (`int`, *optional*, defaults to 64):
            Dimensionality of patch embedding.
        depths (`List[int]`, *optional*, defaults to `[2, 2, 6, 2]`):
            Number of layers in each level of the encoder.
        num_heads (`List[int]`, *optional*, defaults to `[3, 6, 12, 24]`):
            Number of attention heads in each layer of the Transformer encoder.
        kernel_size (`int`, *optional*, defaults to 7):
            Neighborhood Attention kernel size.
        mlp_ratio (`float`, *optional*, defaults to 3.0):
            Ratio of MLP hidden dimensionality to embedding dimensionality.
        qkv_bias (`bool`, *optional*, defaults to `True`):
            Whether or not a learnable bias should be added to the queries, keys and values.
        hidden_dropout_prob (`float`, *optional*, defaults to 0.0):
            The dropout probability for all fully connected layers in the embeddings and encoder.
        attention_probs_dropout_prob (`float`, *optional*, defaults to 0.0):
            The dropout ratio for the attention probabilities.
        drop_path_rate (`float`, *optional*, defaults to 0.1):
            Stochastic depth rate.
        hidden_act (`str` or `function`, *optional*, defaults to `"gelu"`):
            The non-linear activation function (function or string) in the encoder. If string, `"gelu"`, `"relu"`,
            `"selu"` and `"gelu_new"` are supported.
        patch_norm (`bool`, *optional*, defaults to `True`):
            Whether or not to add layer normalization after patch embedding.
        initializer_range (`float`, *optional*, defaults to 0.02):
            The standard deviation of the truncated_normal_initializer for initializing all weight matrices.
        layer_norm_eps (`float`, *optional*, defaults to 1e-12):
            The epsilon used by the layer normalization layers.
        layer_scale_init_value (`float`, *optional*, defaults to 0.0):
            The initial value for the layer scale. Disabled if <=0.
        out_features (`List[str]`, *optional*):
            If used as backbone, list of features to output. Can be any of `"stem"`, `"stage1"`, `"stage2"`, etc.
            (depending on how many stages the model has). Will default to the last stage if unset.

    Example:

    ```python
    >>> from transformers import NatConfig, NatModel

    >>> # Initializing a Nat shi-labs/nat-mini-in1k-224 style configuration
    >>> configuration = NatConfig()

    >>> # Initializing a model (with random weights) from the shi-labs/nat-mini-in1k-224 style configuration
    >>> model = NatModel(configuration)

    >>> # Accessing the model configuration
    >>> configuration = model.config
    ```'''
    model_type: str
    attribute_map: Incomplete
    patch_size: Incomplete
    num_channels: Incomplete
    embed_dim: Incomplete
    depths: Incomplete
    num_layers: Incomplete
    num_heads: Incomplete
    kernel_size: Incomplete
    mlp_ratio: Incomplete
    qkv_bias: Incomplete
    hidden_dropout_prob: Incomplete
    attention_probs_dropout_prob: Incomplete
    drop_path_rate: Incomplete
    hidden_act: Incomplete
    path_norm: Incomplete
    layer_norm_eps: Incomplete
    initializer_range: Incomplete
    hidden_size: Incomplete
    layer_scale_init_value: Incomplete
    stage_names: Incomplete
    out_features: Incomplete
    def __init__(self, patch_size: int = 4, num_channels: int = 3, embed_dim: int = 64, depths=[3, 4, 6, 5], num_heads=[2, 4, 8, 16], kernel_size: int = 7, mlp_ratio: float = 3.0, qkv_bias: bool = True, hidden_dropout_prob: float = 0.0, attention_probs_dropout_prob: float = 0.0, drop_path_rate: float = 0.1, hidden_act: str = 'gelu', patch_norm: bool = True, initializer_range: float = 0.02, layer_norm_eps: float = 1e-05, layer_scale_init_value: float = 0.0, out_features: Incomplete | None = None, **kwargs) -> None: ...
