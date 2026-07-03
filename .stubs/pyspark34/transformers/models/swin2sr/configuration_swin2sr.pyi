from ...configuration_utils import PretrainedConfig as PretrainedConfig
from ...utils import logging as logging
from _typeshed import Incomplete

logger: Incomplete
SWIN2SR_PRETRAINED_CONFIG_ARCHIVE_MAP: Incomplete

class Swin2SRConfig(PretrainedConfig):
    '''
    This is the configuration class to store the configuration of a [`Swin2SRModel`]. It is used to instantiate a Swin
    Transformer v2 model according to the specified arguments, defining the model architecture. Instantiating a
    configuration with the defaults will yield a similar configuration to that of the Swin Transformer v2
    [caidas/swin2sr-classicalsr-x2-64](https://huggingface.co/caidas/swin2sr-classicalsr-x2-64) architecture.

    Configuration objects inherit from [`PretrainedConfig`] and can be used to control the model outputs. Read the
    documentation from [`PretrainedConfig`] for more information.

    Args:
        image_size (`int`, *optional*, defaults to 64):
            The size (resolution) of each image.
        patch_size (`int`, *optional*, defaults to 1):
            The size (resolution) of each patch.
        num_channels (`int`, *optional*, defaults to 3):
            The number of input channels.
        embed_dim (`int`, *optional*, defaults to 180):
            Dimensionality of patch embedding.
        depths (`list(int)`, *optional*, defaults to `[6, 6, 6, 6, 6, 6]`):
            Depth of each layer in the Transformer encoder.
        num_heads (`list(int)`, *optional*, defaults to `[6, 6, 6, 6, 6, 6]`):
            Number of attention heads in each layer of the Transformer encoder.
        window_size (`int`, *optional*, defaults to 8):
            Size of windows.
        mlp_ratio (`float`, *optional*, defaults to 2.0):
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
        use_absolute_embeddings (`bool`, *optional*, defaults to `False`):
            Whether or not to add absolute position embeddings to the patch embeddings.
        patch_norm (`bool`, *optional*, defaults to `True`):
            Whether or not to add layer normalization after patch embedding.
        initializer_range (`float`, *optional*, defaults to 0.02):
            The standard deviation of the truncated_normal_initializer for initializing all weight matrices.
        layer_norm_eps (`float`, *optional*, defaults to 1e-12):
            The epsilon used by the layer normalization layers.
        upscale (`int`, *optional*, defaults to 2):
            The upscale factor for the image. 2/3/4/8 for image super resolution, 1 for denoising and compress artifact
            reduction
        img_range (`float`, *optional*, defaults to 1.):
            The range of the values of the input image.
        resi_connection (`str`, *optional*, defaults to `"1conv"`):
            The convolutional block to use before the residual connection in each stage.
        upsampler (`str`, *optional*, defaults to `"pixelshuffle"`):
            The reconstruction reconstruction module. Can be \'pixelshuffle\'/\'pixelshuffledirect\'/\'nearest+conv\'/None.

    Example:

    ```python
    >>> from transformers import Swin2SRConfig, Swin2SRModel

    >>> # Initializing a Swin2SR caidas/swin2sr-classicalsr-x2-64 style configuration
    >>> configuration = Swin2SRConfig()

    >>> # Initializing a model (with random weights) from the caidas/swin2sr-classicalsr-x2-64 style configuration
    >>> model = Swin2SRModel(configuration)

    >>> # Accessing the model configuration
    >>> configuration = model.config
    ```'''
    model_type: str
    attribute_map: Incomplete
    image_size: Incomplete
    patch_size: Incomplete
    num_channels: Incomplete
    embed_dim: Incomplete
    depths: Incomplete
    num_layers: Incomplete
    num_heads: Incomplete
    window_size: Incomplete
    mlp_ratio: Incomplete
    qkv_bias: Incomplete
    hidden_dropout_prob: Incomplete
    attention_probs_dropout_prob: Incomplete
    drop_path_rate: Incomplete
    hidden_act: Incomplete
    use_absolute_embeddings: Incomplete
    path_norm: Incomplete
    layer_norm_eps: Incomplete
    initializer_range: Incomplete
    upscale: Incomplete
    img_range: Incomplete
    resi_connection: Incomplete
    upsampler: Incomplete
    def __init__(self, image_size: int = 64, patch_size: int = 1, num_channels: int = 3, embed_dim: int = 180, depths=[6, 6, 6, 6, 6, 6], num_heads=[6, 6, 6, 6, 6, 6], window_size: int = 8, mlp_ratio: float = 2.0, qkv_bias: bool = True, hidden_dropout_prob: float = 0.0, attention_probs_dropout_prob: float = 0.0, drop_path_rate: float = 0.1, hidden_act: str = 'gelu', use_absolute_embeddings: bool = False, patch_norm: bool = True, initializer_range: float = 0.02, layer_norm_eps: float = 1e-05, upscale: int = 2, img_range: float = 1.0, resi_connection: str = '1conv', upsampler: str = 'pixelshuffle', **kwargs) -> None: ...
