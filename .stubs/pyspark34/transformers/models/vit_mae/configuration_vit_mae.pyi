from ...configuration_utils import PretrainedConfig as PretrainedConfig
from ...utils import logging as logging
from _typeshed import Incomplete

logger: Incomplete
VIT_MAE_PRETRAINED_CONFIG_ARCHIVE_MAP: Incomplete

class ViTMAEConfig(PretrainedConfig):
    '''
    This is the configuration class to store the configuration of a [`ViTMAEModel`]. It is used to instantiate an ViT
    MAE model according to the specified arguments, defining the model architecture. Instantiating a configuration with
    the defaults will yield a similar configuration to that of the ViT
    [facebook/vit-mae-base](https://huggingface.co/facebook/vit-mae-base) architecture.

    Configuration objects inherit from [`PretrainedConfig`] and can be used to control the model outputs. Read the
    documentation from [`PretrainedConfig`] for more information.


    Args:
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
            `"relu"`, `"selu"` and `"gelu_new"` are supported.
        hidden_dropout_prob (`float`, *optional*, defaults to 0.0):
            The dropout probabilitiy for all fully connected layers in the embeddings, encoder, and pooler.
        attention_probs_dropout_prob (`float`, *optional*, defaults to 0.0):
            The dropout ratio for the attention probabilities.
        initializer_range (`float`, *optional*, defaults to 0.02):
            The standard deviation of the truncated_normal_initializer for initializing all weight matrices.
        layer_norm_eps (`float`, *optional*, defaults to 1e-12):
            The epsilon used by the layer normalization layers.
        image_size (`int`, *optional*, defaults to 224):
            The size (resolution) of each image.
        patch_size (`int`, *optional*, defaults to 16):
            The size (resolution) of each patch.
        num_channels (`int`, *optional*, defaults to 3):
            The number of input channels.
        qkv_bias (`bool`, *optional*, defaults to `True`):
            Whether to add a bias to the queries, keys and values.
        decoder_num_attention_heads (`int`, *optional*, defaults to 12):
            Number of attention heads for each attention layer in the decoder.
        decoder_hidden_size (`int`, *optional*, defaults to 512):
            Dimensionality of the decoder.
        decoder_num_hidden_layers (`int`, *optional*, defaults to 8):
            Number of hidden layers in the decoder.
        decoder_intermediate_size (`int`, *optional*, defaults to 2048):
            Dimensionality of the "intermediate" (i.e., feed-forward) layer in the decoder.
        mask_ratio (`float`, *optional*, defaults to 0.75):
            The ratio of the number of masked tokens in the input sequence.
        norm_pix_loss (`bool`, *optional*, defaults to `False`):
            Whether or not to train with normalized pixels (see Table 3 in the paper). Using normalized pixels improved
            representation quality in the experiments of the authors.

    Example:

    ```python
    >>> from transformers import ViTMAEConfig, ViTMAEModel

    >>> # Initializing a ViT MAE vit-mae-base style configuration
    >>> configuration = ViTMAEConfig()

    >>> # Initializing a model (with random weights) from the vit-mae-base style configuration
    >>> model = ViTMAEModel(configuration)

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
    initializer_range: Incomplete
    layer_norm_eps: Incomplete
    image_size: Incomplete
    patch_size: Incomplete
    num_channels: Incomplete
    qkv_bias: Incomplete
    decoder_num_attention_heads: Incomplete
    decoder_hidden_size: Incomplete
    decoder_num_hidden_layers: Incomplete
    decoder_intermediate_size: Incomplete
    mask_ratio: Incomplete
    norm_pix_loss: Incomplete
    def __init__(self, hidden_size: int = 768, num_hidden_layers: int = 12, num_attention_heads: int = 12, intermediate_size: int = 3072, hidden_act: str = 'gelu', hidden_dropout_prob: float = 0.0, attention_probs_dropout_prob: float = 0.0, initializer_range: float = 0.02, layer_norm_eps: float = 1e-12, image_size: int = 224, patch_size: int = 16, num_channels: int = 3, qkv_bias: bool = True, decoder_num_attention_heads: int = 16, decoder_hidden_size: int = 512, decoder_num_hidden_layers: int = 8, decoder_intermediate_size: int = 2048, mask_ratio: float = 0.75, norm_pix_loss: bool = False, **kwargs) -> None: ...
